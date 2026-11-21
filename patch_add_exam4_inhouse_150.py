import os

script_dir = os.path.dirname(os.path.abspath(__file__))
builder_path = os.path.join(script_dir, 'update_builder.py')

with open(builder_path, 'r', encoding='utf-8') as f:
    content = f.read()

patches = []

# 1. Load exam4_inhouse_150 in Python
p1_old = '''exam4_psych_json_data_str = json.dumps(exam4_psych_questions, ensure_ascii=False)
exam4_psych_categories_json_str = json.dumps(exam4_psych_categories, ensure_ascii=False)'''

p1_new = p1_old + '''

# Load Exam 4 In-House Practice (150 Questions, 5 Parts from IMC 535)
exam4_inhouse_150_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'exam4_inhouse_150_questions.json')
with open(exam4_inhouse_150_path, 'r', encoding='utf-8') as f:
    exam4_inhouse_150_questions = json.load(f)

exam4_inhouse_150_categories = [
    'Part 1: Mental Status Exam',
    'Part 2: Schizophrenia Spectrum',
    'Part 3: Psychosis Workup & Early Intervention',
    'Part 4: Antipsychotic Medications',
    'Part 5: Substance Use Disorders'
]

exam4_inhouse_150_json_data_str = json.dumps(exam4_inhouse_150_questions, ensure_ascii=False)
exam4_inhouse_150_categories_json_str = json.dumps(exam4_inhouse_150_categories, ensure_ascii=False)'''
patches.append((p1_old, p1_new))

# 2. Inject raw question variables into JS
p2_old = '''    const rawExam4PsychQuestions = """ + exam4_psych_json_data_str + """;
    const exam4PsychCategories = """ + exam4_psych_categories_json_str + """;'''

p2_new = p2_old + '''
    const rawExam4InHouse150Questions = """ + exam4_inhouse_150_json_data_str + """;
    const exam4InHouse150Categories = """ + exam4_inhouse_150_categories_json_str + """;'''
patches.append((p2_old, p2_new))

# 3. EXAM_BANKS.exam4: add In-House E4 (150 Qs)
p3_old = '''      exam4: [
        {
          id: 'exam4_psych_practice',
          label: 'Psych Practice (50 Qs)',
          icon: '🛋️',
          badge: '16 Topics • Official',
          type: 'exam4'
        }
      ]'''

p3_new = '''      exam4: [
        {
          id: 'exam4_psych_practice',
          label: 'Psych Practice (50 Qs)',
          icon: '🛋️',
          badge: '16 Topics • Official',
          type: 'exam4'
        },
        {
          id: 'exam4_inhouse_150',
          label: 'In-House E4 (150 Qs)',
          icon: '📝',
          badge: '5 Parts • Need-to-Know',
          type: 'exam4'
        }
      ]'''
patches.append((p3_old, p3_new))

# 4. isExam4Track
p4_old = '''    function isExam4Track(track) {
      return track === 'exam4' || track === 'exam4_psych_practice' || (track && track.startsWith('exam4_'));
    }'''

p4_new = '''    function isExam4Track(track) {
      return track === 'exam4' || track === 'exam4_psych_practice' || track === 'exam4_inhouse_150' || (track && track.startsWith('exam4_'));
    }'''
patches.append((p4_old, p4_new))

# 5. getCategoriesForTrack
p5_old = '''    function getCategoriesForTrack() {
      if (isExam4Track(currentTrack)) return exam4PsychCategories;'''

p5_new = '''    function getCategoriesForTrack() {
      if (currentTrack === 'exam4_inhouse_150') return exam4InHouse150Categories;
      if (isExam4Track(currentTrack)) return exam4PsychCategories;'''
patches.append((p5_old, p5_new))

# 6. getStoragePrefix
p6_old = '''    function getStoragePrefix(track = currentTrack) {
      if (isExam4Track(track)) return 'usmle_exam4_psych_';'''

p6_new = '''    function getStoragePrefix(track = currentTrack) {
      if (track === 'exam4_inhouse_150') return 'usmle_exam4_inhouse_150_';
      if (isExam4Track(track)) return 'usmle_exam4_psych_';'''
patches.append((p6_old, p6_new))

# 7. loadTrackState
p7_old = '''    function loadTrackState() {
      const storagePrefix = getStoragePrefix(currentTrack);
      let rawData = rawExamQuestions;

      if (isExam4Track(currentTrack)) {
        rawData = rawExam4PsychQuestions;
      } else if (currentTrack === 'exam3_step1_150') {'''

p7_new = '''    function loadTrackState() {
      const storagePrefix = getStoragePrefix(currentTrack);
      let rawData = rawExamQuestions;

      if (currentTrack === 'exam4_inhouse_150') {
        rawData = rawExam4InHouse150Questions;
      } else if (isExam4Track(currentTrack)) {
        rawData = rawExam4PsychQuestions;
      } else if (currentTrack === 'exam3_step1_150') {'''
patches.append((p7_old, p7_new))

# 8. switchTrack zenTray and timer
p8_old = '''      if (isExam4Track(currentTrack)) {
        zenTray.style.display = 'flex';
        trayIcon.textContent = '🛋️';
        trayLabelText.textContent = 'Psych Topics:';
        trackTag.style.display = 'inline-block';
        trackTag.className = 'q-track-tag exam4';
        trackTag.textContent = '🛋️ Psych Practice (50 Qs)';
        timerDisplay.classList.add('exam4');
        sidebarTitle.innerHTML = `<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2a10 10 0 1 0 10 10A10 10 0 0 0 12 2zm0 18a8 8 0 1 1 8-8 8 8 0 0 1-8 8z"/></svg> Psych Topics (16)`;
      } else if (currentTrack === 'exam3_step1_150') {'''

p8_new = '''      if (currentTrack === 'exam4_inhouse_150') {
        zenTray.style.display = 'flex';
        trayIcon.textContent = '📝';
        trayLabelText.textContent = 'E4 Parts:';
        trackTag.style.display = 'inline-block';
        trackTag.className = 'q-track-tag exam4';
        trackTag.textContent = '📝 In-House E4 (150 Qs)';
        timerDisplay.classList.add('exam4');
        sidebarTitle.innerHTML = `<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2a10 10 0 1 0 10 10A10 10 0 0 0 12 2zm0 18a8 8 0 1 1 8-8 8 8 0 0 1-8 8z"/></svg> In-House Parts (5)`;
      } else if (currentTrack === 'exam4_psych_practice' || isExam4Track(currentTrack)) {
        zenTray.style.display = 'flex';
        trayIcon.textContent = '🛋️';
        trayLabelText.textContent = 'Psych Topics:';
        trackTag.style.display = 'inline-block';
        trackTag.className = 'q-track-tag exam4';
        trackTag.textContent = '🛋️ Psych Practice (50 Qs)';
        timerDisplay.classList.add('exam4');
        sidebarTitle.innerHTML = `<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2a10 10 0 1 0 10 10A10 10 0 0 0 12 2zm0 18a8 8 0 1 1 8-8 8 8 0 0 1-8 8z"/></svg> Psych Topics (16)`;
      } else if (currentTrack === 'exam3_step1_150') {'''
patches.append((p8_old, p8_new))

# 9. switchTrack toast message
p9_old = '''      const toastMsg = isExam4Track(currentTrack)
        ? 'Exam 4: Loaded 🛋️ Psychiatry Practice (50 Qs - 16 Topics)'
        : currentTrack === 'exam3_step1_150'''

p9_new = '''      const toastMsg = currentTrack === 'exam4_inhouse_150'
        ? 'Exam 4: Loaded 📝 In-House E4 (150 Qs - 5 Parts)'
        : isExam4Track(currentTrack)
        ? 'Exam 4: Loaded 🛋️ Psychiatry Practice (50 Qs - 16 Topics)'
        : currentTrack === 'exam3_step1_150'''
patches.append((p9_old, p9_new))

# 10. Score report title
p10_old = '''      const reportTitle = isExam4Track(currentTrack)
        ? '🛋️ Exam 4 Psychiatry Practice (50 Qs) Score Report'
        : currentTrack === 'exam3_step1_150'''

p10_new = '''      const reportTitle = currentTrack === 'exam4_inhouse_150'
        ? '📝 Exam 4 In-House Practice (150 Qs) Score Report'
        : isExam4Track(currentTrack)
        ? '🛋️ Exam 4 Psychiatry Practice (50 Qs) Score Report'
        : currentTrack === 'exam3_step1_150'''
patches.append((p10_old, p10_new))

# 11. initApp resume track label
p11_old = '''          const trackLabel = isExam4Track(currentTrack)
            ? 'Exam 4 Psych Practice (50 Qs)'
            : currentTrack === 'exam3_step1_150'''

p11_new = '''          const trackLabel = currentTrack === 'exam4_inhouse_150'
            ? 'Exam 4 In-House E4 (150 Qs)'
            : isExam4Track(currentTrack)
            ? 'Exam 4 Psych Practice (50 Qs)'
            : currentTrack === 'exam3_step1_150'''
patches.append((p11_old, p11_new))

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
