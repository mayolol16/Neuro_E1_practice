const { spawn } = require('child_process');
const http = require('http');
const fs = require('fs');

const CHROME_BIN = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
const HTML_URL = 'file:///Users/markyoussef_1/.gemini/antigravity-ide/scratch/usmle_exam1/index.html';
const SCREENSHOT_PATH = '/Users/markyoussef_1/.gemini/antigravity/brain/f5d39382-784d-4636-a513-d94a978a1ea0/exam3_step1_150_verified.png';
const PORT = 9229;
const USER_DATA_DIR = `/tmp/chrome_verify_step1_150_${Date.now()}`;

function assert(cond, msg) {
  if (!cond) throw new Error(`ASSERTION FAILED: ${msg}`);
}

function getJson(url) {
  return new Promise((resolve, reject) => {
    http.get(url, (res) => {
      let data = '';
      res.on('data', (chunk) => (data += chunk));
      res.on('end', () => {
        try {
          resolve(JSON.parse(data));
        } catch (e) {
          reject(e);
        }
      });
    }).on('error', reject);
  });
}

async function waitForTarget() {
  for (let i = 0; i < 40; i++) {
    try {
      const targets = await getJson(`http://127.0.0.1:${PORT}/json`);
      const page = targets.find((t) => t.type === 'page' && t.webSocketDebuggerUrl);
      if (page) return page.webSocketDebuggerUrl;
    } catch (_) {}
    await new Promise((r) => setTimeout(r, 250));
  }
  throw new Error('Timed out waiting for Chrome DevTools target');
}

class CDPClient {
  constructor(wsUrl) {
    this.ws = new WebSocket(wsUrl);
    this.id = 0;
    this.pending = new Map();
    this.events = [];
    this.errors = [];
    this.ready = new Promise((resolve, reject) => {
      this.ws.addEventListener('open', resolve);
      this.ws.addEventListener('error', reject);
    });
    this.ws.addEventListener('message', (evt) => {
      const msg = JSON.parse(evt.data);
      if (msg.id && this.pending.has(msg.id)) {
        const { resolve, reject } = this.pending.get(msg.id);
        this.pending.delete(msg.id);
        if (msg.error) reject(new Error(JSON.stringify(msg.error)));
        else resolve(msg.result);
      } else if (msg.method === 'Runtime.exceptionThrown') {
        this.errors.push(JSON.stringify(msg.params));
      } else if (msg.method === 'Runtime.consoleAPICalled' && msg.params.type === 'error') {
        this.errors.push(JSON.stringify(msg.params.args));
      }
    });
  }

  send(method, params = {}) {
    const id = ++this.id;
    return new Promise((resolve, reject) => {
      this.pending.set(id, { resolve, reject });
      this.ws.send(JSON.stringify({ id, method, params }));
    });
  }

  async eval(expression) {
    const res = await this.send('Runtime.evaluate', {
      expression,
      returnByValue: true,
      awaitPromise: true,
    });
    if (res.exceptionDetails) {
      throw new Error(`JS Eval Exception: ${JSON.stringify(res.exceptionDetails)}`);
    }
    return res.result ? res.result.value : undefined;
  }

  close() {
    this.ws.close();
  }
}

(async () => {
  const chrome = spawn(
    CHROME_BIN,
    [
      '--headless=new',
      '--disable-gpu',
      '--no-sandbox',
      `--remote-debugging-port=${PORT}`,
      `--user-data-dir=${USER_DATA_DIR}`,
      '--window-size=1440,950',
      HTML_URL,
    ],
    { stdio: 'ignore' }
  );

  let client;
  try {
    const wsUrl = await waitForTarget();
    client = new CDPClient(wsUrl);
    await client.ready;
    await client.send('Page.enable');
    await client.send('Runtime.enable');

    console.log('--- TEST 1: Load page and unlock Exam 3 banks via "mike" ---');
    await client.eval(`localStorage.clear(); sessionStorage.clear(); true;`);
    await client.send('Page.reload', { ignoreCache: true });
    await new Promise((r) => setTimeout(r, 1200));

    // Click Exam 3 Tab
    await client.eval(`document.getElementById('exam3TabBtn').click();`);
    await new Promise((r) => setTimeout(r, 400));

    // Type "mike" to unlock
    for (const ch of 'mike'.split('')) {
      await client.send('Input.dispatchKeyEvent', {
        type: 'keyDown',
        key: ch,
        text: ch,
        unmodifiedText: ch,
        windowsVirtualKeyCode: ch.toUpperCase().charCodeAt(0),
      });
      await client.send('Input.dispatchKeyEvent', {
        type: 'keyUp',
        key: ch,
        text: ch,
        unmodifiedText: ch,
        windowsVirtualKeyCode: ch.toUpperCase().charCodeAt(0),
      });
    }
    await new Promise((r) => setTimeout(r, 600));

    const unlockCheck = await client.eval(`(() => ({
      unlocked: isExam3Unlocked(),
      banks: EXAM_BANKS.exam3.map(b => b.id)
    }))()`);
    console.log('Unlock check:', unlockCheck);
    assert(unlockCheck.unlocked, 'Exam 3 must be unlocked via "mike"');
    assert(unlockCheck.banks.includes('exam3_step1_150'), 'exam3_step1_150 must be in EXAM_BANKS.exam3');

    console.log('--- TEST 2: Switch to "Step 1–Style (150 Qs)" bank ---');
    await client.eval(`switchTrack('exam3_step1_150');`);
    await new Promise((r) => setTimeout(r, 600));

    const trackStatus = await client.eval(`(() => {
      return {
        currentTrack,
        qCount: questions.length,
        prefix: getStoragePrefix(),
        categories: getCategoriesForTrack(),
        firstQuestionStem: questions[0] ? questions[0].stem.substring(0, 80) : null
      };
    })()`);
    console.log('Track status:', trackStatus);
    assert(trackStatus.currentTrack === 'exam3_step1_150', 'Active track must be exam3_step1_150');
    assert(trackStatus.qCount === 150, `Expected 150 questions, found ${trackStatus.qCount}`);
    assert(trackStatus.prefix === 'usmle_exam3_step1_150_', `Storage prefix must be usmle_exam3_step1_150_, got ${trackStatus.prefix}`);

    console.log('--- TEST 3: Verify category distribution (150 Qs) ---');
    const catCheck = await client.eval(`(() => {
      const counts = {};
      questions.forEach(q => { counts[q.category] = (counts[q.category] || 0) + 1; });
      return counts;
    })()`);
    console.log('Category distribution:', catCheck);
    assert(catCheck['Demyelinating Disease'] === 15, `Demyelinating Disease should be 15, got ${catCheck['Demyelinating Disease']}`);
    assert(catCheck['Cerebellum'] === 12, `Cerebellum should be 12, got ${catCheck['Cerebellum']}`);
    assert(catCheck['Tumors'] === 21, `Tumors should be 21, got ${catCheck['Tumors']}`);
    assert(catCheck['Opportunistic Infection'] === 15, `Opportunistic Infection should be 15, got ${catCheck['Opportunistic Infection']}`);
    assert(catCheck['Stroke (Blood Supply, Cerebrovascular, Brainstem)'] === 45, `Stroke should be 45, got ${catCheck['Stroke (Blood Supply, Cerebrovascular, Brainstem)']}`);
    assert(catCheck['Dementia'] === 15, `Dementia should be 15, got ${catCheck['Dementia']}`);
    assert(catCheck['CBIL Epilepsy'] === 27, `CBIL Epilepsy should be 27, got ${catCheck['CBIL Epilepsy']}`);

    console.log('--- TEST 4: Verify answer key balancing (Exactly 30 A, 30 B, 30 C, 30 D, 30 E) ---');
    const keyCheck = await client.eval(`(() => {
      const keys = { A: 0, B: 0, C: 0, D: 0, E: 0 };
      questions.forEach(q => {
        const correctOpt = q.options.find(o => o.is_correct);
        if (correctOpt) keys[correctOpt.letter]++;
      });
      return keys;
    })()`);
    console.log('Key distribution:', keyCheck);
    assert(keyCheck['A'] === 30, `Key A count must be 30, got ${keyCheck['A']}`);
    assert(keyCheck['B'] === 30, `Key B count must be 30, got ${keyCheck['B']}`);
    assert(keyCheck['C'] === 30, `Key C count must be 30, got ${keyCheck['C']}`);
    assert(keyCheck['D'] === 30, `Key D count must be 30, got ${keyCheck['D']}`);
    assert(keyCheck['E'] === 30, `Key E count must be 30, got ${keyCheck['E']}`);

    console.log('--- TEST 5: Verify zero parentheses in options & option length spread <= 7 ---');
    const optFormatCheck = await client.eval(`(() => {
      let parenCount = 0;
      let maxSpread = 0;
      const issues = [];
      questions.forEach((q, idx) => {
        const lens = q.options.map(o => o.text.length);
        const spread = Math.max(...lens) - Math.min(...lens);
        if (spread > maxSpread) maxSpread = spread;
        q.options.forEach(o => {
          if (o.text.includes('(') || o.text.includes(')')) {
            parenCount++;
            issues.push('Q' + (idx+1) + ' ' + o.letter + ': ' + o.text);
          }
        });
      });
      return { parenCount, maxSpread, issues };
    })()`);
    console.log('Option formatting check:', optFormatCheck);
    assert(optFormatCheck.parenCount === 0, `Expected 0 parentheses in options, found ${optFormatCheck.parenCount}: ${JSON.stringify(optFormatCheck.issues)}`);
    assert(optFormatCheck.maxSpread <= 7, `Max option spread must be <= 7, got ${optFormatCheck.maxSpread}`);

    console.log('--- TEST 6: Verify standalone stems for cross-referencing questions ---');
    const stemCheck = await client.eval(`(() => {
      const crossRefs = [2, 3, 10, 52, 101, 117, 122];
      return crossRefs.map(num => ({
        qNum: num,
        stem: questions[num-1].stem,
        hasQuestionRef: /question\s+\d+|in\s+question/i.test(questions[num-1].stem)
      }));
    })()`);
    console.log('Stem check for cross-refs:', stemCheck);
    stemCheck.forEach(item => {
      assert(!item.hasQuestionRef, `Q${item.qNum} still references another question: ${item.stem}`);
      assert(item.stem.length > 50, `Q${item.qNum} stem is too short to be standalone: ${item.stem}`);
    });

    console.log('--- TEST 7: Interactive question answering & feedback ---');
    // Answer question 1 (Marcus Gunn / optic nerve)
    const q1Ans = await client.eval(`(() => {
      const q = questions[0];
      const state = userState[q.id];
      const correctIdx = state.shuffledOptions.findIndex(o => o.is_correct);
      selectChoice(correctIdx);
      return {
        selectedChoiceIndex: state.selectedChoiceIndex,
        isCorrect: state.isCorrect
      };
    })()`);
    console.log('Q1 answering result:', q1Ans);
    assert(q1Ans.isCorrect === true, 'Q1 should be marked correct');

    // Verify localStorage prefix isolation
    const prefixStorageCheck = await client.eval(`(() => {
      const stepStateRaw = localStorage.getItem('usmle_exam3_step1_150_state') || '{}';
      const pracStateRaw = localStorage.getItem('usmle_exam3_practice_state') || '{}';
      const stepState = JSON.parse(stepStateRaw);
      const pracState = JSON.parse(pracStateRaw);
      return {
        stepHasQ1: !!stepState['exam3_step1_150_q1'],
        pracHasQ1: !!pracState['exam3_step1_150_q1']
      };
    })()`);
    console.log('Storage prefix isolation check:', prefixStorageCheck);
    assert(prefixStorageCheck.stepHasQ1 === true, 'Current track state must contain answered question');
    assert(prefixStorageCheck.pracHasQ1 === false, 'Other tracks must not contain current track answers');

    // Verify item grid shows 150 items
    const gridCheck = await client.eval(`(() => {
      openItemGrid();
      const cnt = document.querySelectorAll('.grid-item').length;
      closeItemGridDirect();
      return cnt;
    })()`);
    console.log('Item grid count:', gridCheck);
    assert(gridCheck === 150, `Item grid should show 150 items, got ${gridCheck}`);

    console.log('--- TEST 8: Open Score Report and check rendering ---');
    await client.eval(`showScoreReport();`);
    await new Promise((r) => setTimeout(r, 400));
    const reportTitle = await client.eval(`document.getElementById('reportModalTitle').textContent;`);
    console.log('Score Report Title:', reportTitle);
    assert(reportTitle.includes('Step 1–Style') && reportTitle.includes('150 Qs'), `Score report title unexpected: ${reportTitle}`);
    await client.eval(`closeScoreReportDirect();`);

    console.log('--- TEST 9: Check Weakness Assessment Exam List & Rendering ---');
    await client.eval(`openWeaknessAssessmentModal();`);
    await new Promise((r) => setTimeout(r, 400));
    const modalCheck = await client.eval(`(() => {
      const modal = document.getElementById('weaknessModal');
      const isVisible = modal && modal.classList.contains('show');
      const hasStep1InList = EXAM3_BANKS_METADATA.some(e => e.id === 'exam3_step1_150');
      const assessmentData = collectWeaknessData();
      return {
        isVisible,
        hasStep1InList,
        totalQuestionsCount: assessmentData.totalQuestionsCount
      };
    })()`);
    console.log('Weakness assessment check:', modalCheck);
    assert(modalCheck.isVisible, 'Weakness modal should be visible');
    assert(modalCheck.hasStep1InList, 'EXAM3_BANKS_METADATA must include exam3_step1_150');
    assert(modalCheck.totalQuestionsCount === 150, `Expected 150 total questions in current scope, got ${modalCheck.totalQuestionsCount}`);
    await client.eval(`closeWeaknessModalDirect();`);

    console.log('--- TEST 10: Capture high-resolution screenshot ---');
    await client.eval(`renderCurrentQuestion();`);
    await new Promise((r) => setTimeout(r, 500));
    const shot = await client.send('Page.captureScreenshot', { format: 'png' });
    fs.writeFileSync(SCREENSHOT_PATH, Buffer.from(shot.data, 'base64'));
    console.log(`Saved screenshot to: ${SCREENSHOT_PATH}`);

    assert(client.errors.length === 0, `Console errors occurred: ${JSON.stringify(client.errors)}`);
    console.log('=== ALL 10 TESTS PASSED CLEANLY WITH ZERO ERRORS ===');

  } finally {
    if (client) client.close();
    chrome.kill('SIGTERM');
    try {
      fs.rmSync(USER_DATA_DIR, { recursive: true, force: true });
    } catch (_) {}
  }
})();
