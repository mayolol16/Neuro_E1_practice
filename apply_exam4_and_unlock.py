import os
import json

script_dir = os.path.dirname(os.path.abspath(__file__))
builder_path = os.path.join(script_dir, 'update_builder.py')

with open(builder_path, 'r', encoding='utf-8') as f:
    content = f.read()

patches = []

# 1. Add Exam 4 loading in Python
p1_old = '''# Exam 3 Step 1-Style (exam3_step1_150: 150 Questions)
exam3_step1_150_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'exam3_step1_150_questions.json')
with open(exam3_step1_150_path, 'r', encoding='utf-8') as f:
    exam3_step1_150_questions = json.load(f)

exam3_step1_150_categories = [
    'Demyelinating Disease',
    'Cerebellum',
    'Tumors',
    'Opportunistic Infection',
    'Stroke (Blood Supply, Cerebrovascular, Brainstem)',
    'Dementia',
    'CBIL Epilepsy',
]

exam3_step1_150_json_data_str = json.dumps(exam3_step1_150_questions, ensure_ascii=False)
exam3_step1_150_categories_json_str = json.dumps(exam3_step1_150_categories, ensure_ascii=False)'''

p1_new = p1_old + '''

# Load Exam 4 Psychiatry Practice (50 Questions, 16 Topics)
exam4_psych_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'exam4_psych_questions.json')
with open(exam4_psych_path, 'r', encoding='utf-8') as f:
    exam4_psych_questions = json.load(f)

exam4_psych_categories = [
    'Mental status exam',
    'Schizophrenia and Psychosis',
    'Antipsychotics',
    'Substance use',
    'Anxiety & Trauma',
    'OCD & Defense Mechanisms',
    'Depressive Disorders',
    'Suicide and Eating Disorders',
    'Perinatal Psych and Somatic Symptom Disorders',
    'LGBTQIA Mental Health',
    'Bipolar Disorders and Mood Stabilizers',
    'Disruptive Disorders and Forensic Psychiatry',
    'Personality Disorder',
    'ADHD',
    'Psychotherapy',
    'Autism'
]

exam4_psych_json_data_str = json.dumps(exam4_psych_questions, ensure_ascii=False)
exam4_psych_categories_json_str = json.dumps(exam4_psych_categories, ensure_ascii=False)'''
patches.append((p1_old, p1_new))

# 2. CSS for Exam 4
p2_old = '''    .exam-tab-btn.active-exam3 {
      background: linear-gradient(135deg, #059669, #10b981, #06b6d4);
      color: #ffffff;
      font-weight: 800;
      box-shadow: 0 2px 10px rgba(16, 185, 129, 0.45);
    }'''

p2_new = p2_old + '''

    .exam-tab-btn.active-exam4 {
      background: linear-gradient(135deg, #e11d48, #f43f5e, #fb7185);
      color: #ffffff;
      font-weight: 800;
      box-shadow: 0 2px 10px rgba(244, 63, 94, 0.45);
    }

    .track-btn.exam4-active {
      background: linear-gradient(135deg, #e11d48, #f43f5e);
      color: #ffffff;
      border-color: #fb7185;
      box-shadow: 0 4px 14px rgba(244, 63, 94, 0.35);
    }

    .tag.exam4, .q-track-tag.exam4 {
      background: rgba(244, 63, 94, 0.15);
      color: #fda4af;
      border: 1px solid rgba(244, 63, 94, 0.3);
    }

    .cat-chip.exam4-cat, .cat-item.exam4-cat {
      background: rgba(244, 63, 94, 0.08);
      border-color: rgba(244, 63, 94, 0.25);
      color: #fecdd3;
    }
    .cat-chip.exam4-cat.active, .cat-item.exam4-cat.active {
      background: #e11d48;
      color: #ffffff;
      border-color: #f43f5e;
      box-shadow: 0 4px 12px rgba(244, 63, 94, 0.4);
    }

    .timer-display.exam4 {
      border-color: rgba(244, 63, 94, 0.4);
      color: #fda4af;
    }'''
patches.append((p2_old, p2_new))

# 3. HTML exam tabs
p3_old = '''        <button id="exam3TabBtn" class="exam-tab-btn" onclick="selectExam('exam3')">
          <span>⚡</span>
          <span>Exam 3</span>
        </button>
      </div>'''

p3_new = '''        <button id="exam3TabBtn" class="exam-tab-btn" onclick="selectExam('exam3')">
          <span>⚡</span>
          <span>Exam 3</span>
        </button>
        <button id="exam4TabBtn" class="exam-tab-btn" onclick="selectExam('exam4')">
          <span>🛋️</span>
          <span>Exam 4 (Psych)</span>
        </button>
      </div>'''
patches.append((p3_old, p3_new))

# 4. JS raw question injection
p4_old = '''    const rawExam3GHU16Questions = """ + exam3_g_h_u1_6_json_data_str + """;
    const exam3GHU16Categories = """ + exam3_g_h_u1_6_categories_json_str + """;'''

p4_new = p4_old + '''
    const rawExam4PsychQuestions = """ + exam4_psych_json_data_str + """;
    const exam4PsychCategories = """ + exam4_psych_categories_json_str + """;'''
patches.append((p4_old, p4_new))

# 5. EXAM_BANKS: add exam4
p5_old = '''        {
          id: 'exam3_step1_150',
          label: 'Step 1–Style (150 Qs)',
          icon: '⚡',
          badge: '150 Qs • Step 1–Style',
          type: 'exam3'
        }
      ]
    };'''

p5_new = '''        {
          id: 'exam3_step1_150',
          label: 'Step 1–Style (150 Qs)',
          icon: '⚡',
          badge: '150 Qs • Step 1–Style',
          type: 'exam3'
        }
      ],
      exam4: [
        {
          id: 'exam4_psych_practice',
          label: 'Psych Practice (50 Qs)',
          icon: '🛋️',
          badge: '16 Topics • Official',
          type: 'exam4'
        }
      ]
    };'''
patches.append((p5_old, p5_new))

# 6. isExam4Track & isExam3Track
p6_old = '''    function isExam3Track(track) {
      return track === 'exam3' || track === 'exam3_practice' || track === 'exam3_redo' || track === 'redo' || track === 'exam3_high_yield' || track === 'high_yield' || track === 'exam3_c_u1_6' || track === 'exam3_c_h1_6' || track === 'exam3_c_u2_1_6' || track === 'exam3_g_h_u1_6' || track === 'exam3_inhouse_c' || track === 'exam3_inhouse_c2' || track === 'exam3_in_house_like_g' || track === 'exam3_step1_150';
    }'''

p6_new = '''    function isExam4Track(track) {
      return track === 'exam4' || track === 'exam4_psych_practice' || (track && track.startsWith('exam4_'));
    }

    function isExam3Track(track) {
      return track === 'exam3' || track === 'exam3_practice' || track === 'exam3_redo' || track === 'redo' || track === 'exam3_high_yield' || track === 'high_yield' || track === 'exam3_c_u1_6' || track === 'exam3_c_h1_6' || track === 'exam3_c_u2_1_6' || track === 'exam3_g_h_u1_6' || track === 'exam3_inhouse_c' || track === 'exam3_inhouse_c2' || track === 'exam3_in_house_like_g' || track === 'exam3_step1_150';
    }'''
patches.append((p6_old, p6_new))

# 7. getCategoriesForTrack: add exam4
p7_old = '''    function getCategoriesForTrack() {
      if (currentTrack === 'exam3_step1_150') return exam3Step1150Categories;'''

p7_new = '''    function getCategoriesForTrack() {
      if (isExam4Track(currentTrack)) return exam4PsychCategories;
      if (currentTrack === 'exam3_step1_150') return exam3Step1150Categories;'''
patches.append((p7_old, p7_new))

# 8. isExam3Unlocked: permanently unlock
p8_old = '''    function isExam3Unlocked() {
      const urlParams = new URLSearchParams(window.location.search);
      if (urlParams.has('mike') || urlParams.get('unlock') === 'mike' || urlParams.get('name') === 'mike' ||
          urlParams.has('mark') || urlParams.get('unlock') === 'mark' || urlParams.get('name') === 'mark') {
        return true;
      }
      return sessionStorage.getItem('usmle_exam3_unlocked') === 'true';
    }'''

p8_new = '''    function isExam3Unlocked() {
      return true; // Permanently unlocked per user request (no password or keystroke required)
    }'''
patches.append((p8_old, p8_new))

# 9. selectExam(examId)
p9_old = '''    function selectExam(examId) {
      currentExam = examId;
      localStorage.setItem('usmle_active_exam', currentExam);

      const e1Tab = document.getElementById('exam1TabBtn');
      const e2Tab = document.getElementById('exam2TabBtn');
      const e3Tab = document.getElementById('exam3TabBtn');
      if (e1Tab) e1Tab.className = 'exam-tab-btn' + (currentExam === 'exam1' ? ' active-exam1' : '');
      if (e2Tab) e2Tab.className = 'exam-tab-btn' + (currentExam === 'exam2' ? ' active-exam2' : '');
      if (e3Tab) e3Tab.className = 'exam-tab-btn' + (currentExam === 'exam3' ? ' active-exam3' : '');

      renderBankSwitcher();

      // Pick active bank for this exam
      if (currentExam === 'exam3') {
        let savedBank = localStorage.getItem('usmle_exam3_active_bank') || 'exam3_practice';
        if (!isExam3Unlocked() && !isExam3BaseTrack(savedBank)) {
          savedBank = 'exam3_practice';
        }
        switchTrack(savedBank);
      } else if (currentExam === 'exam2') {
        const savedBank = localStorage.getItem('usmle_exam2_active_bank') || 'exam2_zen';
        switchTrack(savedBank);
      } else {
        const savedBank = localStorage.getItem('usmle_exam1_active_bank') || 'inhouse';
        switchTrack(savedBank);
      }
    }'''

p9_new = '''    function selectExam(examId) {
      currentExam = examId;
      localStorage.setItem('usmle_active_exam', currentExam);

      const e1Tab = document.getElementById('exam1TabBtn');
      const e2Tab = document.getElementById('exam2TabBtn');
      const e3Tab = document.getElementById('exam3TabBtn');
      const e4Tab = document.getElementById('exam4TabBtn');
      if (e1Tab) e1Tab.className = 'exam-tab-btn' + (currentExam === 'exam1' ? ' active-exam1' : '');
      if (e2Tab) e2Tab.className = 'exam-tab-btn' + (currentExam === 'exam2' ? ' active-exam2' : '');
      if (e3Tab) e3Tab.className = 'exam-tab-btn' + (currentExam === 'exam3' ? ' active-exam3' : '');
      if (e4Tab) e4Tab.className = 'exam-tab-btn' + (currentExam === 'exam4' ? ' active-exam4' : '');

      renderBankSwitcher();

      // Pick active bank for this exam
      if (currentExam === 'exam4') {
        const savedBank = localStorage.getItem('usmle_exam4_active_bank') || 'exam4_psych_practice';
        switchTrack(savedBank);
      } else if (currentExam === 'exam3') {
        let savedBank = localStorage.getItem('usmle_exam3_active_bank') || 'exam3_practice';
        switchTrack(savedBank);
      } else if (currentExam === 'exam2') {
        const savedBank = localStorage.getItem('usmle_exam2_active_bank') || 'exam2_zen';
        switchTrack(savedBank);
      } else {
        const savedBank = localStorage.getItem('usmle_exam1_active_bank') || 'inhouse';
        switchTrack(savedBank);
      }
    }'''
patches.append((p9_old, p9_new))

# 10. getVisibleBanks()
p10_old = '''    function getVisibleBanks() {
      let banks = EXAM_BANKS[currentExam] || EXAM_BANKS.exam1;
      if (currentExam === 'exam3' && !isExam3Unlocked()) {
        banks = banks.filter(b => isExam3BaseTrack(b.id));
      }
      return banks;
    }'''

p10_new = '''    function getVisibleBanks() {
      let banks = EXAM_BANKS[currentExam] || EXAM_BANKS.exam1;
      return banks;
    }'''
patches.append((p10_old, p10_new))

# 11. renderBankSwitcher: exam4 button class
p11_old = '''          else if (b.type === 'exam3') activeClass = ' exam3-active';
        }'''

p11_new = '''          else if (b.type === 'exam3') activeClass = ' exam3-active';
          else if (b.type === 'exam4') activeClass = ' exam4-active';
        }'''
patches.append((p11_old, p11_new))

# 12. switchTrack: support exam4
p12_old = '''      if (isExam3Track(newTrack)) {
        currentExam = 'exam3';
        localStorage.setItem('usmle_exam3_active_bank', newTrack);
      } else if (isExam2Track(newTrack)) {
        currentExam = 'exam2';
        localStorage.setItem('usmle_exam2_active_bank', newTrack);
      } else {
        currentExam = 'exam1';
        localStorage.setItem('usmle_exam1_active_bank', newTrack);
      }
      localStorage.setItem('usmle_active_exam', currentExam);

      currentTrack = newTrack;
      localStorage.setItem('usmle_active_track', currentTrack);

      // Highlight level 1 tabs
      const e1Tab = document.getElementById('exam1TabBtn');
      const e2Tab = document.getElementById('exam2TabBtn');
      const e3Tab = document.getElementById('exam3TabBtn');
      if (e1Tab) e1Tab.className = 'exam-tab-btn' + (currentExam === 'exam1' ? ' active-exam1' : '');
      if (e2Tab) e2Tab.className = 'exam-tab-btn' + (currentExam === 'exam2' ? ' active-exam2' : '');
      if (e3Tab) e3Tab.className = 'exam-tab-btn' + (currentExam === 'exam3' ? ' active-exam3' : '');'''

p12_new = '''      if (isExam4Track(newTrack)) {
        currentExam = 'exam4';
        localStorage.setItem('usmle_exam4_active_bank', newTrack);
      } else if (isExam3Track(newTrack)) {
        currentExam = 'exam3';
        localStorage.setItem('usmle_exam3_active_bank', newTrack);
      } else if (isExam2Track(newTrack)) {
        currentExam = 'exam2';
        localStorage.setItem('usmle_exam2_active_bank', newTrack);
      } else {
        currentExam = 'exam1';
        localStorage.setItem('usmle_exam1_active_bank', newTrack);
      }
      localStorage.setItem('usmle_active_exam', currentExam);

      currentTrack = newTrack;
      localStorage.setItem('usmle_active_track', currentTrack);

      // Highlight level 1 tabs
      const e1Tab = document.getElementById('exam1TabBtn');
      const e2Tab = document.getElementById('exam2TabBtn');
      const e3Tab = document.getElementById('exam3TabBtn');
      const e4Tab = document.getElementById('exam4TabBtn');
      if (e1Tab) e1Tab.className = 'exam-tab-btn' + (currentExam === 'exam1' ? ' active-exam1' : '');
      if (e2Tab) e2Tab.className = 'exam-tab-btn' + (currentExam === 'exam2' ? ' active-exam2' : '');
      if (e3Tab) e3Tab.className = 'exam-tab-btn' + (currentExam === 'exam3' ? ' active-exam3' : '');
      if (e4Tab) e4Tab.className = 'exam-tab-btn' + (currentExam === 'exam4' ? ' active-exam4' : '');'''
patches.append((p12_old, p12_new))

# 13. switchTrack tray and timer
p13_old = '''      timerDisplay.classList.remove('zen', 'focused-zen', 'inhouse', 'exam2', 'exam3');

      if (currentTrack === 'exam3_step1_150') {'''

p13_new = '''      timerDisplay.classList.remove('zen', 'focused-zen', 'inhouse', 'exam2', 'exam3', 'exam4');

      if (isExam4Track(currentTrack)) {
        zenTray.style.display = 'flex';
        trayIcon.textContent = '🛋️';
        trayLabelText.textContent = 'Psych Topics:';
        trackTag.style.display = 'inline-block';
        trackTag.className = 'q-track-tag exam4';
        trackTag.textContent = '🛋️ Psych Practice (50 Qs)';
        timerDisplay.classList.add('exam4');
        sidebarTitle.innerHTML = `<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2a10 10 0 1 0 10 10A10 10 0 0 0 12 2zm0 18a8 8 0 1 1 8-8 8 8 0 0 1-8 8z"/></svg> Psych Topics (16)`;
      } else if (currentTrack === 'exam3_step1_150') {'''
patches.append((p13_old, p13_new))

# 14. switchTrack zenTray check and toast
p14_old = '''      loadTrackState();
      if (isExam3Track(currentTrack) || currentTrack === 'exam2_set3' || currentTrack === 'exam2_set2' || currentTrack === 'exam2_deep' || currentTrack === 'exam2_replicate' || currentTrack === 'exam2_inhouse2' || currentTrack === 'exam2_inhouse' || currentTrack === 'exam2_zen' || currentTrack === 'exam2' || currentTrack === 'exam2_pdf_practice' || currentTrack === 'inhouse' || currentTrack === 'focused_zen' || currentTrack === 'zen') {
        renderZenTray();
      }
      applyFilter();
      renderSidebarCategories();
      updateOverallStats();
      renderCurrentQuestion();

      const toastMsg = currentTrack === 'exam3_step1_150'''

p14_new = '''      loadTrackState();
      if (isExam4Track(currentTrack) || isExam3Track(currentTrack) || currentTrack === 'exam2_set3' || currentTrack === 'exam2_set2' || currentTrack === 'exam2_deep' || currentTrack === 'exam2_replicate' || currentTrack === 'exam2_inhouse2' || currentTrack === 'exam2_inhouse' || currentTrack === 'exam2_zen' || currentTrack === 'exam2' || currentTrack === 'exam2_pdf_practice' || currentTrack === 'inhouse' || currentTrack === 'focused_zen' || currentTrack === 'zen') {
        renderZenTray();
      }
      applyFilter();
      renderSidebarCategories();
      updateOverallStats();
      renderCurrentQuestion();

      const toastMsg = isExam4Track(currentTrack)
        ? 'Exam 4: Loaded 🛋️ Psychiatry Practice (50 Qs - 16 Topics)'
        : currentTrack === 'exam3_step1_150' '''
patches.append((p14_old, p14_new))

# 15. getStoragePrefix
p15_old = '''    function getStoragePrefix(track = currentTrack) {
      if (track === 'exam3_redo' || track === 'redo') return 'usmle_exam3_redo_';'''

p15_new = '''    function getStoragePrefix(track = currentTrack) {
      if (isExam4Track(track)) return 'usmle_exam4_psych_';
      if (track === 'exam3_redo' || track === 'redo') return 'usmle_exam3_redo_';'''
patches.append((p15_old, p15_new))

# 16. loadTrackState
p16_old = '''    function loadTrackState() {
      const storagePrefix = getStoragePrefix(currentTrack);
      let rawData = rawExamQuestions;

      if (currentTrack === 'exam3_step1_150') {'''

p16_new = '''    function loadTrackState() {
      const storagePrefix = getStoragePrefix(currentTrack);
      let rawData = rawExamQuestions;

      if (isExam4Track(currentTrack)) {
        rawData = rawExam4PsychQuestions;
      } else if (currentTrack === 'exam3_step1_150') {'''
patches.append((p16_old, p16_new))

# 17. Score report title
p17_old = '''      const reportTitle = currentTrack === 'exam3_step1_150'''
p17_new = '''      const reportTitle = isExam4Track(currentTrack)
        ? '🛋️ Exam 4 Psychiatry Practice (50 Qs) Score Report'
        : currentTrack === 'exam3_step1_150' '''
patches.append((p17_old, p17_new))

# 18. initApp activeExam and track target
p18_old = '''      if (!targetTrack) {
        targetTrack = (savedExam === 'exam3') ? 'exam3_practice' : (savedExam === 'exam2') ? 'exam2_zen' : 'inhouse';
      }'''

p18_new = '''      if (!targetTrack) {
        targetTrack = (savedExam === 'exam4') ? 'exam4_psych_practice' : (savedExam === 'exam3') ? 'exam3_practice' : (savedExam === 'exam2') ? 'exam2_zen' : 'inhouse';
      }'''
patches.append((p18_old, p18_new))

# 19. initApp resume track label
p19_old = '''        setTimeout(() => {
          const trackLabel = currentTrack === 'exam3_step1_150'''
p19_new = '''        setTimeout(() => {
          const trackLabel = isExam4Track(currentTrack)
            ? 'Exam 4 Psych Practice (50 Qs)'
            : currentTrack === 'exam3_step1_150' '''
patches.append((p19_old, p19_new))

# Apply all patches
all_found = True
for idx, (old, new) in enumerate(patches):
    if old not in content:
        print(f'ERROR: Patch {idx+1} old string not found!')
        all_found = False
    else:
        content = content.replace(old, new, 1)

if all_found:
    with open(builder_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'SUCCESS: Applied all {len(patches)} patches to update_builder.py!')
else:
    print('Failed to apply some patches.')
