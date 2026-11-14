const { spawn } = require('child_process');
const http = require('http');
const fs = require('fs');

const CHROME_BIN = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
const HTML_URL = 'file:///Users/markyoussef_1/.gemini/antigravity-ide/scratch/usmle_exam1/index.html';
const SCREENSHOT_PATH = '/Users/markyoussef_1/.gemini/antigravity/brain/f5d39382-784d-4636-a513-d94a978a1ea0/exam3_inhouse_c2_verified.png';
const PORT = 9225;
const USER_DATA_DIR = `/tmp/chrome_verify_inhouse_c2_${Date.now()}`;

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

    // Clear storage to test fresh state & hidden Exam 3 gate
    await client.eval(`localStorage.clear(); true;`);
    await client.send('Page.reload', { ignoreCache: true });
    await new Promise((r) => setTimeout(r, 1200));

    // Check 1: Exam 3 hidden initially
    const initialHidden = await client.eval(`(() => {
      const btn = document.getElementById('exam3TabBtn');
      const style = btn ? getComputedStyle(btn).display : 'missing';
      return { unlocked: isExam3Unlocked(), display: style };
    })()`);
    console.log('Initial Exam 3 gate:', initialHidden);
    assert(initialHidden.unlocked === false, 'Exam 3 should start locked');
    assert(initialHidden.display === 'none', 'Exam 3 tab button should start hidden');

    // Type "mark" to unlock Exam 3
    for (const ch of ['m', 'a', 'r', 'k']) {
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
        windowsVirtualKeyCode: ch.toUpperCase().charCodeAt(0),
      });
    }
    await new Promise((r) => setTimeout(r, 400));

    const afterMark = await client.eval(`(() => {
      const btn = document.getElementById('exam3TabBtn');
      return { unlocked: isExam3Unlocked(), display: btn ? getComputedStyle(btn).display : 'missing' };
    })()`);
    console.log('After typing mark:', afterMark);
    assert(afterMark.unlocked === true, 'Exam 3 should unlock after typing mark');
    assert(afterMark.display !== 'none', 'Exam 3 tab button should be visible after unlock');

    // Check 2: Select Exam 3 and click In House c2 track button
    await client.eval(`selectExam('exam3');`);
    await new Promise((r) => setTimeout(r, 250));
    const pillClicked = await client.eval(`(() => {
      const btn = document.getElementById('trackBtn_exam3_inhouse_c2');
      if (!btn) return null;
      btn.click();
      return btn.textContent.trim();
    })()`);
    console.log('Clicked track button:', pillClicked);
    assert(pillClicked && pillClicked.includes('In House c2'), 'Expected #trackBtn_exam3_inhouse_c2 pill to exist and switch');
    await new Promise((r) => setTimeout(r, 400));

    // Check 3: Verify 100 questions, 7 categories, standalone stems, prior modes intact
    const trackAudit = await client.eval(`(() => {
      const catCounts = {};
      questions.forEach((q) => { catCounts[q.category] = (catCounts[q.category] || 0) + 1; });
      const q6 = questions.find((q) => q.orig_q_num === 6);
      const q9 = questions.find((q) => q.orig_q_num === 9);
      const q84 = questions.find((q) => q.orig_q_num === 84);
      const q86 = questions.find((q) => q.orig_q_num === 86);
      return {
        currentTrack,
        qCount: questions.length,
        inhouseC1Count: typeof rawExam3InHouseCQuestions !== 'undefined' ? rawExam3InHouseCQuestions.length : -1,
        cU2Count: typeof rawExam3CU216Questions !== 'undefined' ? rawExam3CU216Questions.length : -1,
        categories: getCategoriesForTrack(),
        catCounts,
        q6Stem: q6 ? q6.stem : '',
        q9Stem: q9 ? q9.stem : '',
        q84Stem: q84 ? q84.stem : '',
        q86Stem: q86 ? q86.stem : '',
        tagText: document.getElementById('currentQTrackTag').textContent,
        sidebarTitle: document.getElementById('sidebarTitle').textContent.trim(),
        allValid: questions.every((q) => q.options.length === 5 && q.correct_idx >= 0 && q.correct_idx < 5 && q.explanation && q.explanation.length > 30),
      };
    })()`);
    console.log('Track audit:', JSON.stringify(trackAudit, null, 2));
    assert(trackAudit.currentTrack === 'exam3_inhouse_c2', 'currentTrack must be exam3_inhouse_c2');
    assert(trackAudit.qCount === 100, 'Expected 100 questions in In House c2');
    assert(trackAudit.inhouseC1Count === 100, 'Expected In House c to still have 100 Qs');
    assert(trackAudit.cU2Count === 202, 'Expected c_u2_1-6 to still have 202 Qs');
    assert(trackAudit.categories.length === 7, 'Expected 7 blueprint categories');
    assert(trackAudit.q6Stem.includes('33-year-old man') && !/previous question/i.test(trackAudit.q6Stem), 'Q6 must be standalone');
    assert(trackAudit.q9Stem.includes('33-year-old man') && !/Question 5/i.test(trackAudit.q9Stem), 'Q9 must be standalone');
    assert(trackAudit.q84Stem.includes('25-year-old woman') && !/previous question/i.test(trackAudit.q84Stem), 'Q84 must be standalone');
    assert(trackAudit.q86Stem.includes('6-year-old girl') && !/previous question/i.test(trackAudit.q86Stem), 'Q86 must be standalone');
    assert(trackAudit.allValid, 'All 100 questions must have 5 options and explanations');

    // Check 4: Answer Q1, verify explanation renders, switch to Exam 1 and back, then reload
    const ansRes = await client.eval(`(() => {
      const q = questions[0];
      const corrOptIdx = userState[q.id].shuffledOptions.findIndex((o) => o.is_correct);
      const btns = document.querySelectorAll('#optionsList .option-item');
      btns[corrOptIdx].click();
      return {
        qId: q.id,
        selected: userState[q.id].selectedChoiceIndex,
        isCorrect: userState[q.id].isCorrect,
        explVisible: getComputedStyle(document.getElementById('explanationCard')).display !== 'none',
        savedStateLen: Object.keys(JSON.parse(localStorage.getItem('usmle_exam3_inhouse_c2_state') || '{}')).length,
      };
    })()`);
    console.log('Answered Q1:', ansRes);
    assert(ansRes.isCorrect === true, 'Selecting correct option on Q1 should mark correct');
    assert(ansRes.explVisible === true, 'Explanation card must display after answering');
    assert(ansRes.savedStateLen >= 1, 'State must save to usmle_exam3_inhouse_c2_state');

    // Switch to Exam 1 In-House and back
    await client.eval(`selectExam('exam1'); switchTrack('inhouse');`);
    await new Promise((r) => setTimeout(r, 250));
    const ex1Check = await client.eval(`({ currentTrack, len: questions.length })`);
    assert(ex1Check.currentTrack === 'inhouse' && ex1Check.len === 385, 'Exam 1 In-House must stay intact (385 Qs)');

    // Switch to In House c1 and check it
    await client.eval(`selectExam('exam3'); switchTrack('exam3_inhouse_c');`);
    await new Promise((r) => setTimeout(r, 250));
    const c1Check = await client.eval(`({ currentTrack, len: questions.length })`);
    assert(c1Check.currentTrack === 'exam3_inhouse_c' && c1Check.len === 100, 'In House c must stay intact (100 Qs)');

    // Switch back to In House c2
    await client.eval(`selectExam('exam3'); switchTrack('exam3_inhouse_c2');`);
    await new Promise((r) => setTimeout(r, 300));
    const afterSwitchBack = await client.eval(`userState[questions[0].id]`);
    assert(afterSwitchBack && afterSwitchBack.isCorrect === true, 'Answer must persist after switching tracks');

    // Capture full-page/viewport screenshot on Q1 answered state
    const shot = await client.send('Page.captureScreenshot', { format: 'png' });
    fs.writeFileSync(SCREENSHOT_PATH, Buffer.from(shot.data, 'base64'));
    console.log('Saved screenshot to:', SCREENSHOT_PATH);

    // Reload page and confirm persistence across full reload
    await client.send('Page.reload', { ignoreCache: true });
    await new Promise((r) => setTimeout(r, 1200));
    const afterReload = await client.eval(`(() => ({
      currentTrack,
      qCount: questions.length,
      q1State: userState[questions[0].id],
      explVisible: getComputedStyle(document.getElementById('explanationCard')).display !== 'none',
    }))()`);
    console.log('After full reload:', afterReload);
    assert(afterReload.currentTrack === 'exam3_inhouse_c2', 'Track must restore to exam3_inhouse_c2 after reload');
    assert(afterReload.qCount === 100, 'Question count must be 100 after reload');
    assert(afterReload.q1State && afterReload.q1State.isCorrect === true, 'Q1 answer must persist after full reload');
    assert(afterReload.explVisible === true, 'Q1 explanation must still show after reload');

    // Check 5: Item grid check (100 .grid-item nodes)
    const gridCount = await client.eval(`(() => {
      openItemGrid();
      const cnt = document.querySelectorAll('.grid-item').length;
      const title = document.getElementById('gridModalTitle').textContent;
      closeItemGridDirect();
      return { cnt, title };
    })()`);
    console.log('Item grid:', gridCount);
    assert(gridCount.cnt === 100, 'Item grid must show 100 .grid-item nodes');
    assert(gridCount.title.includes('In House c2'), 'Item grid title must include In House c2');

    assert(client.errors.length === 0, `Console/runtime errors detected: ${client.errors.join('; ')}`);
    console.log('ALL VERIFICATION CHECKS PASSED WITH 0 RUNTIME ERRORS!');
  } finally {
    if (client) client.close();
    chrome.kill('SIGKILL');
    fs.rmSync(USER_DATA_DIR, { recursive: true, force: true });
  }
})().catch((err) => {
  console.error(err);
  process.exit(1);
});
