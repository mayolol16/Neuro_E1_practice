const { spawn } = require('child_process');
const http = require('http');
const fs = require('fs');

const CHROME_BIN = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
const HTML_URL = 'file:///Users/markyoussef_1/.gemini/antigravity-ide/scratch/usmle_exam1/index.html';
const SCREENSHOT_PATH = '/Users/markyoussef_1/.gemini/antigravity/brain/f5d39382-784d-4636-a513-d94a978a1ea0/exam3_high_yield_clean_verified.png';
const PORT = 9235;
const USER_DATA_DIR = `/tmp/chrome_verify_hy_${Date.now()}`;

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
    console.log('2. Connected to Chrome WebSocket:', wsUrl);
    client = new CDPClient(wsUrl);
    await client.ready;

    await client.send('Page.enable');
    await client.send('Runtime.enable');

    console.log('3. Waiting for page initialization...');
    await new Promise((r) => setTimeout(r, 1200));

    // Unlock Exam 3 and select exam3
    console.log('4. Unlocking Exam 3 and selecting exam3...');
    await client.eval(`
      if (typeof unlockExam3 === 'function') {
        unlockExam3();
      }
      selectExam('exam3');
    `);
    await new Promise((r) => setTimeout(r, 600));

    // Switch track to exam3_high_yield
    console.log('5. Switching track to exam3_high_yield...');
    const trackSwitchResult = await client.eval(`
      switchTrack('exam3_high_yield');
      ({
        currentExam,
        currentTrack,
        questionCount: questions.length,
        categoryCount: getCategoriesForTrack().length
      })
    `);
    console.log('Track state:', trackSwitchResult);
    assert(trackSwitchResult.currentTrack === 'exam3_high_yield', 'currentTrack must be exam3_high_yield');
    assert(trackSwitchResult.questionCount === 150, 'High-yield mode must contain 150 questions');

    // Verify cross-reference fixes:
    console.log('6. Verifying standalone stems for Q8, Q32, Q58, Q90...');
    const stemsCheck = await client.eval(`
      const q8 = questions.find(q => q.q_num === "8");
      const q32 = questions.find(q => q.q_num === "32");
      const q58 = questions.find(q => q.q_num === "58");
      const q90 = questions.find(q => q.q_num === "90");
      ({
        q8_stem: q8 ? q8.stem : null,
        q32_stem: q32 ? q32.stem : null,
        q58_stem: q58 ? q58.stem : null,
        q90_stem: q90 ? q90.stem : null
      })
    `);

    assert(!stemsCheck.q8_stem.includes('previous question'), 'Q8 must not mention previous question');
    assert(stemsCheck.q8_stem.includes('chills and diarrhea'), 'Q8 must contain the GBS clinical stem');

    assert(!stemsCheck.q32_stem.includes('previous question'), 'Q32 must not mention previous question');
    assert(stemsCheck.q32_stem.includes('posterior fossa mass'), 'Q32 must contain the posterior fossa clinical stem');

    assert(!stemsCheck.q58_stem.includes('previous question'), 'Q58 must not mention previous question');
    assert(stemsCheck.q58_stem.includes('HSV-1'), 'Q58 must contain the HSV-1 clinical stem');

    assert(!stemsCheck.q90_stem.includes('previous question'), 'Q90 must not mention previous question');
    assert(stemsCheck.q90_stem.includes('brain death'), 'Q90 must contain the brain death clinical stem');

    console.log('Standalone stems verified successfully!');

    // Verify option balance / giveaway removal:
    console.log('7. Verifying giveaway audit on sample questions...');
    const optionsAudit = await client.eval(`
      const q3 = questions.find(q => q.q_num === "3");
      const q10 = questions.find(q => q.q_num === "10");
      const q138 = questions.find(q => q.q_num === "138");
      const q150 = questions.find(q => q.q_num === "150");

      ({
        q3_opts: q3.options.map(o => o.text),
        q10_opts: q10.options.map(o => o.text),
        q138_opts: q138.options.map(o => o.text),
        q150_opts: q150.options.map(o => o.text)
      })
    `);

    // Q3 should NOT have "(Marcus Gunn pupil)" in correct answer
    assert(!optionsAudit.q3_opts.some(t => t.includes('Marcus Gunn pupil')), 'Q3 should not have Marcus Gunn giveaway');
    // Q10 should NOT have ", which occurs in about two-thirds of patients"
    assert(!optionsAudit.q10_opts.some(t => t.includes('which occurs in about')), 'Q10 should not have frequency giveaway');
    // Q138 should NOT have "(meningitis), since this is a provoked seizure"
    assert(!optionsAudit.q138_opts.some(t => t.includes('since this is a provoked')), 'Q138 should not have giveaway clause');
    // Q150 correct option should be balanced (~75-85 chars, not 226 chars)
    const q150_max = Math.max(...optionsAudit.q150_opts.map(t => t.length));
    const q150_min = Math.min(...optionsAudit.q150_opts.map(t => t.length));
    assert(q150_max < 110, 'Q150 options should be concise and balanced');
    assert(q150_max - q150_min < 50, 'Q150 options should be of comparable lengths');

    console.log('Option balance verified successfully!');

    // Test answering question 1 and checking persistence:
    console.log('8. Testing answering a question and verifying answer state...');
    await client.eval(`
      currentIndex = 0;
      renderCurrentQuestion();
      selectChoice(userState[questions[0].id].shuffledOptions.findIndex(o => o.letter === 'C'));
    `);
    await new Promise((r) => setTimeout(r, 400));

    const answerPersistCheck = await client.eval(`
      const prefix = getStoragePrefix('exam3_high_yield');
      const savedState = JSON.parse(localStorage.getItem(prefix + 'state') || '{}');
      const q0 = questions[0];
      ({
        prefix,
        currentQIndex: currentIndex,
        userStateForQ0: userState[q0.id],
        savedStateForQ0: savedState[q0.id]
      })
    `);
    console.log('Answer persistence check:', {
      prefix: answerPersistCheck.prefix,
      userStateCorrect: answerPersistCheck.userStateForQ0 ? answerPersistCheck.userStateForQ0.isCorrect : null,
      savedStateCorrect: answerPersistCheck.savedStateForQ0 ? answerPersistCheck.savedStateForQ0.isCorrect : null
    });
    assert(answerPersistCheck.userStateForQ0.isCorrect === true, 'Option C is the correct answer for Q1');
    assert(answerPersistCheck.savedStateForQ0.isCorrect === true, 'Saved state in localStorage must persist');

    // Take screenshot:
    console.log('9. Taking screenshot of cleaned High-Yield exam mode...');
    const shot = await client.send('Page.captureScreenshot', { format: 'png' });
    fs.writeFileSync(SCREENSHOT_PATH, Buffer.from(shot.data, 'base64'));
    console.log(`Saved screenshot to: ${SCREENSHOT_PATH}`);

    assert(client.errors.length === 0, `Console errors detected: ${JSON.stringify(client.errors)}`);
    console.log('ALL HIGH-YIELD TESTS PASSED PERFECTLY!');
  } finally {
    if (client) client.close();
    chrome.kill('SIGKILL');
  }
})();
