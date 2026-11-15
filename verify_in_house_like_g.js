const { spawn } = require('child_process');
const http = require('http');
const fs = require('fs');

const CHROME_BIN = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
const HTML_URL = 'file:///Users/markyoussef_1/.gemini/antigravity-ide/scratch/usmle_exam1/index.html';
const SCREENSHOT_PATH = '/Users/markyoussef_1/.gemini/antigravity/brain/f5d39382-784d-4636-a513-d94a978a1ea0/exam3_in_house_like_g_verified.png';
const PORT = 9228;
const USER_DATA_DIR = `/tmp/chrome_verify_in_house_like_g_${Date.now()}`;

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
    assert(unlockCheck.banks.includes('exam3_in_house_like_g'), 'in_house_like_G must be in EXAM_BANKS.exam3');

    console.log('--- TEST 2: Switch to "in_house_like_G" bank ---');
    await client.eval(`switchTrack('exam3_in_house_like_g');`);
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
    assert(trackStatus.currentTrack === 'exam3_in_house_like_g', 'Active track must be exam3_in_house_like_g');
    assert(trackStatus.qCount === 150, `Expected 150 questions, found ${trackStatus.qCount}`);
    assert(trackStatus.prefix === 'usmle_exam3_in_house_like_g_', `Storage prefix must be usmle_exam3_in_house_like_g_, got ${trackStatus.prefix}`);

    console.log('--- TEST 3: Verify category counts in active question set ---');
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

    console.log('--- TEST 3b: Verify exact course content alignment (No PSEN1, Q110 is Patient H.M., 0 parens in options) ---');
    const contentCheck = await client.eval(`(() => {
      const hasPsen1 = questions.some(q => JSON.stringify(q).toLowerCase().includes('psen1'));
      const q110 = questions[109];
      const parensCount = questions.reduce((acc, q) => {
        return acc + q.options.filter(opt => opt.text.includes('(') || opt.text.includes(')')).length;
      }, 0);
      const maxSpread = questions.reduce((max, q) => {
        const lens = q.options.map(o => o.text.length);
        const spread = Math.max(...lens) - Math.min(...lens);
        return Math.max(max, spread);
      }, 0);
      return {
        hasPsen1,
        q110Stem: q110 ? q110.stem.substring(0, 50) : null,
        parensCount,
        maxSpread
      };
    })()`);
    console.log('Content check:', contentCheck);
    assert(!contentCheck.hasPsen1, 'There must be NO PSEN1 question anywhere in the bank');
    assert(contentCheck.q110Stem.includes('Patient H.M.'), `Q110 must be Patient H.M., got: ${contentCheck.q110Stem}`);
    assert(contentCheck.parensCount === 0, `There must be 0 parentheses in options, found: ${contentCheck.parensCount}`);
    assert(contentCheck.maxSpread <= 6, `Max option length spread must be <= 6, got: ${contentCheck.maxSpread}`);

    console.log('--- TEST 4: Interact and Answer Question 1 ---');
    await client.eval(`selectChoice(questions[0].options[questions[0].correct_idx].letter); submitAnswer();`);
    await new Promise((r) => setTimeout(r, 300));
    const q1State = await client.eval(`userState[questions[0].id]`);
    console.log('Q1 state:', q1State);
    assert(q1State && q1State.selectedChoiceIndex !== undefined, 'Q1 answer should be recorded in userState');

    // Verify item grid shows 150 items
    const gridCheck = await client.eval(`(() => {
      openItemGrid();
      const cnt = document.querySelectorAll('.grid-item').length;
      closeItemGridDirect();
      return cnt;
    })()`);
    console.log('Item grid count:', gridCheck);
    assert(gridCheck === 150, `Item grid should show 150 items, got ${gridCheck}`);

    console.log('--- TEST 5: Verify slider positioning and active tab ---');
    const sliderCheck = await client.eval(`(() => {
      const activeBtn = document.querySelector('#bankSwitcherContainer .track-btn.exam3-active') || document.getElementById('trackBtn_exam3_in_house_like_g');
      return {
        activeBtnText: activeBtn ? activeBtn.innerText.trim().replace(/\\s+/g, ' ') : null,
        sliderBoxExists: !!document.getElementById('bankSliderContainer'),
        scrubberExists: !!document.getElementById('bankScrubberBox')
      };
    })()`);
    console.log('Slider check:', sliderCheck);
    assert(sliderCheck.activeBtnText.includes('in_house_like_G'), 'Active bank button text should include in_house_like_G');

    // Capture screenshot
    const shot = await client.send('Page.captureScreenshot', { format: 'png' });
    fs.writeFileSync(SCREENSHOT_PATH, Buffer.from(shot.data, 'base64'));
    console.log(`Saved screenshot to: ${SCREENSHOT_PATH}`);

    assert(client.errors.length === 0, `Console errors detected: ${JSON.stringify(client.errors)}`);
    console.log('>>> ALL VERIFICATION CHECKS FOR in_house_like_G PASSED WITH 100% ACCURACY! <<<');
  } finally {
    if (client) client.close();
    chrome.kill('SIGKILL');
  }
})();
