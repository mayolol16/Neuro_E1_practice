# -*- coding: utf-8 -*-
"""
add_exam2_to_app.py
Adds Exam 2 (103 questions, 9 sections) to the existing Exam 1 app.
Updates update_builder.py to load Exam 2 dataset, adds the Exam 2 track button,
and regenerates index.html and Downloads copy.
"""
import os
import re
import json

UPDATE_BUILDER_PATH = '/Users/markyoussef_1/.gemini/antigravity-ide/scratch/usmle_exam1/update_builder.py'

def main():
    with open(UPDATE_BUILDER_PATH, 'r', encoding='utf-8') as f:
        src = f.read()

    # 1. Add Exam 2 dataset loading at the top
    top_target = """with open('/Users/markyoussef_1/.gemini/antigravity-ide/scratch/usmle_exam1/inhouse_questions_data.json', 'r', encoding='utf-8') as f:
    inhouse_questions = json.load(f)"""

    top_replacement = """with open('/Users/markyoussef_1/.gemini/antigravity-ide/scratch/usmle_exam1/inhouse_questions_data.json', 'r', encoding='utf-8') as f:
    inhouse_questions = json.load(f)

with open('/Users/markyoussef_1/.gemini/antigravity-ide/scratch/usmle_exam2/exam2_questions_data.json', 'r', encoding='utf-8') as f:
    raw_exam2 = json.load(f)

exam2_questions = []
for q in raw_exam2:
    opts = []
    correct_idx = 0
    for idx, opt in enumerate(q['options']):
        is_cor = (opt['id'] == q['correct_answer'])
        if is_cor:
            correct_idx = idx
        opts.append({
            'letter': opt['id'],
            'is_correct': is_cor,
            'text': opt['text']
        })
    exam2_questions.append({
        'id': q['id'],
        'q_num': str(q['q_num']),
        'stem': q['question'],
        'category': q['category'],
        'options': opts,
        'correct_idx': correct_idx,
        'explanation': q['explanation'],
        'high_yield_pearl': q.get('high_yield_pearl', ''),
        'image': q.get('image', None)
    })

exam2_categories = [
    'Visual System',
    'Visual Reflexes',
    'Infection/Inflammation of eye disorders',
    'Auditory & Vestibular Systems',
    'UMN/LMN',
    'Hypothalamus & Smell/Taste',
    'Basal Ganglia',
    'ALS',
    'Sleep'
]"""

    if top_target in src:
        src = src.replace(top_target, top_replacement, 1)
        print("Replaced top dataset loading.")
    else:
        print("Warning: top_target not found!")

    # 2. Add json dumps
    dumps_target = """inhouse_json_data_str = json.dumps(inhouse_questions, ensure_ascii=False)
categories_json_str = json.dumps(categories, ensure_ascii=False)
inhouse_categories_json_str = json.dumps(inhouse_categories, ensure_ascii=False)"""

    dumps_replacement = """inhouse_json_data_str = json.dumps(inhouse_questions, ensure_ascii=False)
exam2_json_data_str = json.dumps(exam2_questions, ensure_ascii=False)
categories_json_str = json.dumps(categories, ensure_ascii=False)
inhouse_categories_json_str = json.dumps(inhouse_categories, ensure_ascii=False)
exam2_categories_json_str = json.dumps(exam2_categories, ensure_ascii=False)"""

    if dumps_target in src:
        src = src.replace(dumps_target, dumps_replacement, 1)
        print("Replaced json dumps.")
    else:
        print("Warning: dumps_target not found!")

    # 3. Add CSS for exam2
    css_target = """.track-btn.inhouse-active {
      background: linear-gradient(135deg, #f59e0b, #ea580c);
      color: #ffffff;
      box-shadow: 0 2px 10px rgba(245, 158, 11, 0.45);
    }"""

    css_replacement = """.track-btn.exam2-active {
      background: linear-gradient(135deg, #0ea5e9, #2563eb);
      color: #ffffff;
      box-shadow: 0 2px 10px rgba(14, 165, 233, 0.45);
    }

    .track-btn.inhouse-active {
      background: linear-gradient(135deg, #f59e0b, #ea580c);
      color: #ffffff;
      box-shadow: 0 2px 10px rgba(245, 158, 11, 0.45);
    }"""

    if css_target in src:
        src = src.replace(css_target, css_replacement, 1)
        print("Replaced track button CSS.")
    else:
        print("Warning: css_target not found!")

    timer_css_target = """.timer-box.inhouse {
      color: #f59e0b;
      border-color: rgba(245, 158, 11, 0.4);
      background: rgba(245, 158, 11, 0.1);
    }"""

    timer_css_replacement = """.timer-box.exam2 {
      color: #38bdf8;
      border-color: rgba(56, 189, 248, 0.4);
      background: rgba(56, 189, 248, 0.1);
    }

    .timer-box.inhouse {
      color: #f59e0b;
      border-color: rgba(245, 158, 11, 0.4);
      background: rgba(245, 158, 11, 0.1);
    }"""

    if timer_css_target in src:
        src = src.replace(timer_css_target, timer_css_replacement, 1)
        print("Replaced timer CSS.")
    else:
        print("Warning: timer_css_target not found!")

    tag_css_target = """.q-track-tag.inhouse {
      background: rgba(245, 158, 11, 0.15);
      border-color: rgba(245, 158, 11, 0.4);
      color: #fbbf24;
    }"""

    tag_css_replacement = """.q-track-tag.exam2 {
      background: rgba(14, 165, 233, 0.15);
      border-color: rgba(14, 165, 233, 0.4);
      color: #38bdf8;
    }

    .cat-item.exam2-cat.active {
      background: rgba(14, 165, 233, 0.15);
      border-color: #0ea5e9;
    }

    .q-track-tag.inhouse {
      background: rgba(245, 158, 11, 0.15);
      border-color: rgba(245, 158, 11, 0.4);
      color: #fbbf24;
    }"""

    if tag_css_target in src:
        src = src.replace(tag_css_target, tag_css_replacement, 1)
        print("Replaced tag and cat CSS.")
    else:
        print("Warning: tag_css_target not found!")

    # 4. Add Exam 2 button in track-switcher HTML
    switcher_target = """      <!-- 3-Track Mode Switcher -->
      <div class="track-switcher">
        <button id="trackExamBtn" class="track-btn" onclick="switchTrack('exam')">
          <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>
          <span>Exam 1 (125 Qs)</span>
        </button>"""

    switcher_replacement = """      <!-- 5-Track Mode Switcher -->
      <div class="track-switcher">
        <button id="trackExamBtn" class="track-btn" onclick="switchTrack('exam')">
          <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>
          <span>Exam 1 (125 Qs)</span>
        </button>
        <button id="trackExam2Btn" class="track-btn" onclick="switchTrack('exam2')">
          <span>🧠</span>
          <span>Exam 2 (103 Qs)</span>
          <span class="zen-pill-badge">9 Sections</span>
        </button>"""

    if switcher_target in src:
        src = src.replace(switcher_target, switcher_replacement, 1)
        print("Replaced track switcher HTML.")
    else:
        print("Warning: switcher_target not found!")

    # 5. Inject rawExam2Questions in script
    raw_target = """    const rawZenQuestions = {zen_json_data_str};
    const rawInHouseQuestions = {inhouse_json_data_str};
    const subjectCategories = {categories_json_str};
    const inHouseCategories = {inhouse_categories_json_str};"""

    raw_replacement = """    const rawZenQuestions = {zen_json_data_str};
    const rawInHouseQuestions = {inhouse_json_data_str};
    const rawExam2Questions = {exam2_json_data_str};
    const subjectCategories = {categories_json_str};
    const inHouseCategories = {inhouse_categories_json_str};
    const exam2Categories = {exam2_categories_json_str};"""

    if raw_target in src:
        src = src.replace(raw_target, raw_replacement, 1)
        print("Replaced raw script data.")
    else:
        print("Warning: raw_target not found!")

    # 6. Update switchTrack(newTrack)
    switch_target = """      const inHouseBtn = document.getElementById('trackInHouseBtn');
      const examBtn = document.getElementById('trackExamBtn');
      const focusedZenBtn = document.getElementById('trackFocusedZenBtn');
      const zenBtn = document.getElementById('trackZenBtn');
      const zenTray = document.getElementById('zenSectionTray');
      const trayIcon = document.getElementById('zenTrayIcon');
      const trayLabelText = document.getElementById('zenTrayLabelText');
      const trackTag = document.getElementById('currentQTrackTag');
      const sidebarTitle = document.getElementById('sidebarTitle');
      const timerDisplay = document.getElementById('timerDisplay');

      if (inHouseBtn) inHouseBtn.className = 'track-btn';
      examBtn.className = 'track-btn';
      focusedZenBtn.className = 'track-btn';
      zenBtn.className = 'track-btn';
      timerDisplay.classList.remove('zen', 'focused-zen', 'inhouse');

      if (currentTrack === 'inhouse') {"""

    switch_replacement = """      const inHouseBtn = document.getElementById('trackInHouseBtn');
      const examBtn = document.getElementById('trackExamBtn');
      const exam2Btn = document.getElementById('trackExam2Btn');
      const focusedZenBtn = document.getElementById('trackFocusedZenBtn');
      const zenBtn = document.getElementById('trackZenBtn');
      const zenTray = document.getElementById('zenSectionTray');
      const trayIcon = document.getElementById('zenTrayIcon');
      const trayLabelText = document.getElementById('zenTrayLabelText');
      const trackTag = document.getElementById('currentQTrackTag');
      const sidebarTitle = document.getElementById('sidebarTitle');
      const timerDisplay = document.getElementById('timerDisplay');

      if (inHouseBtn) inHouseBtn.className = 'track-btn';
      if (exam2Btn) exam2Btn.className = 'track-btn';
      examBtn.className = 'track-btn';
      focusedZenBtn.className = 'track-btn';
      zenBtn.className = 'track-btn';
      timerDisplay.classList.remove('zen', 'focused-zen', 'inhouse', 'exam2');

      if (currentTrack === 'exam2') {
        if (exam2Btn) exam2Btn.className = 'track-btn exam2-active';
        zenTray.style.display = 'flex';
        trayIcon.textContent = '🧠';
        trayLabelText.textContent = 'Exam 2 Sections:';
        trackTag.style.display = 'inline-block';
        trackTag.className = 'q-track-tag exam2';
        trackTag.textContent = '🧠 Exam 2';
        timerDisplay.classList.add('exam2');
        sidebarTitle.innerHTML = `<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 8v8"/><path d="M8 12h8"/></svg> Exam 2 Sections (9)`;
      } else if (currentTrack === 'inhouse') {"""

    if switch_target in src:
        src = src.replace(switch_target, switch_replacement, 1)
        print("Replaced switchTrack buttons & branches.")
    else:
        print("Warning: switch_target not found!")

    # 7. Update toast in switchTrack
    toast_target = """      const toastMsg = currentTrack === 'inhouse'
        ? 'Switched to 🏠 In-House Course Track (385 Qs from Lectures & Cases)'
        : currentTrack === 'focused_zen'
        ? 'Switched to 🎯 Focused Zen Mode (Study Guide 20 Qs/topic)'
        : currentTrack === 'zen'
        ? 'Switched to 🧘 General Zen Mode (20 Qs/topic)'
        : 'Switched to 📝 Exam 1 Practice (125 Qs)';"""

    toast_replacement = """      const toastMsg = currentTrack === 'exam2'
        ? 'Switched to 🧠 Exam 2 (103 Qs from Ex2-USMLEPracANS)'
        : currentTrack === 'inhouse'
        ? 'Switched to 🏠 In-House Course Track (385 Qs from Lectures & Cases)'
        : currentTrack === 'focused_zen'
        ? 'Switched to 🎯 Focused Zen Mode (Study Guide 20 Qs/topic)'
        : currentTrack === 'zen'
        ? 'Switched to 🧘 General Zen Mode (20 Qs/topic)'
        : 'Switched to 📝 Exam 1 Practice (125 Qs)';"""

    if toast_target in src:
        src = src.replace(toast_target, toast_replacement, 1)
        print("Replaced switchTrack toast.")
    else:
        print("Warning: toast_target not found!")

    # 8. Update loadTrackState
    load_target = """    function loadTrackState() {
      let storagePrefix = 'usmle_exam1_';
      let rawData = rawExamQuestions;
      if (currentTrack === 'inhouse') {
        storagePrefix = 'usmle_inhouse_';
        rawData = rawInHouseQuestions;
      } else if (currentTrack === 'focused_zen') {"""

    load_replacement = """    function loadTrackState() {
      let storagePrefix = 'usmle_exam1_';
      let rawData = rawExamQuestions;
      if (currentTrack === 'exam2') {
        storagePrefix = 'usmle_exam2_';
        rawData = rawExam2Questions;
      } else if (currentTrack === 'inhouse') {
        storagePrefix = 'usmle_inhouse_';
        rawData = rawInHouseQuestions;
      } else if (currentTrack === 'focused_zen') {"""

    if load_target in src:
        src = src.replace(load_target, load_replacement, 1)
        print("Replaced loadTrackState.")
    else:
        print("Warning: load_target not found!")

    # 9. Update saveState
    save_target = """    function saveState() {
      let storagePrefix = 'usmle_exam1_';
      if (currentTrack === 'inhouse') storagePrefix = 'usmle_inhouse_';
      else if (currentTrack === 'focused_zen') storagePrefix = 'usmle_focused_zen_';
      else if (currentTrack === 'zen') storagePrefix = 'usmle_zen_';"""

    save_replacement = """    function saveState() {
      let storagePrefix = 'usmle_exam1_';
      if (currentTrack === 'exam2') storagePrefix = 'usmle_exam2_';
      else if (currentTrack === 'inhouse') storagePrefix = 'usmle_inhouse_';
      else if (currentTrack === 'focused_zen') storagePrefix = 'usmle_focused_zen_';
      else if (currentTrack === 'zen') storagePrefix = 'usmle_zen_';"""

    if save_target in src:
        src = src.replace(save_target, save_replacement, 1)
        print("Replaced saveState.")
    else:
        print("Warning: save_target not found!")

    # 10. Update timer display
    timer_target = """        if (currentTrack === 'focused_zen') {
          document.getElementById('timerText').textContent = `🎯 ${text}`;
        } else if (currentTrack === 'zen') {
          document.getElementById('timerText').textContent = `🧘 ${text}`;
        } else {
          document.getElementById('timerText').textContent = text;
        }"""

    timer_replacement = """        if (currentTrack === 'exam2') {
          document.getElementById('timerText').textContent = `🧠 ${text}`;
        } else if (currentTrack === 'focused_zen') {
          document.getElementById('timerText').textContent = `🎯 ${text}`;
        } else if (currentTrack === 'zen') {
          document.getElementById('timerText').textContent = `🧘 ${text}`;
        } else {
          document.getElementById('timerText').textContent = text;
        }"""

    if timer_target in src:
        src = src.replace(timer_target, timer_replacement, 1)
        print("Replaced timer display logic.")
    else:
        print("Warning: timer_target not found!")

    # 11. Update renderZenTray and selectZenTopic and renderSidebarCategories
    cats_target = """const catsToUse = currentTrack === 'inhouse' ? inHouseCategories : subjectCategories;"""
    cats_replacement = """const catsToUse = currentTrack === 'exam2' ? exam2Categories : (currentTrack === 'inhouse' ? inHouseCategories : subjectCategories);"""
    src = src.replace(cats_target, cats_replacement)
    print(f"Replaced catsToUse occurrences.")

    # 12. Update catClass
    cat_class_target = """const catClass = currentTrack === 'inhouse' ? 'inhouse-cat' : currentTrack === 'focused_zen' ? 'focused-zen-cat' : currentTrack === 'zen' ? 'zen-cat' : '';"""
    cat_class_replacement = """const catClass = currentTrack === 'exam2' ? 'exam2-cat' : currentTrack === 'inhouse' ? 'inhouse-cat' : currentTrack === 'focused_zen' ? 'focused-zen-cat' : currentTrack === 'zen' ? 'zen-cat' : '';"""
    src = src.replace(cat_class_target, cat_class_replacement)
    print(f"Replaced catClass occurrences.")

    # 13. Update condition for zenTray rendering:
    # replace "currentTrack === 'inhouse' || currentTrack === 'focused_zen' || currentTrack === 'zen'"
    # with "currentTrack === 'exam2' || currentTrack === 'inhouse' || currentTrack === 'focused_zen' || currentTrack === 'zen'"
    src = src.replace(
        "currentTrack === 'inhouse' || currentTrack === 'focused_zen' || currentTrack === 'zen'",
        "currentTrack === 'exam2' || currentTrack === 'inhouse' || currentTrack === 'focused_zen' || currentTrack === 'zen'"
    )
    print("Replaced zenTray multi-track condition.")

    # 14. Update openItemGrid modal title
    grid_target = """      const trackName = currentTrack === 'inhouse'
        ? '🏠 In-House Course'
        : currentTrack === 'focused_zen'
        ? '🎯 Focused Zen'
        : currentTrack === 'zen'
        ? '🧘 General Zen'
        : 'Exam 1';"""

    grid_replacement = """      const trackName = currentTrack === 'exam2'
        ? '🧠 Exam 2 (103 Qs)'
        : currentTrack === 'inhouse'
        ? '🏠 In-House Course'
        : currentTrack === 'focused_zen'
        ? '🎯 Focused Zen'
        : currentTrack === 'zen'
        ? '🧘 General Zen'
        : 'Exam 1';"""

    if grid_target in src:
        src = src.replace(grid_target, grid_replacement, 1)
        print("Replaced grid modal title.")
    else:
        print("Warning: grid_target not found!")

    # 15. Update showScoreReport
    score_target = """      const reportTitle = currentTrack === 'focused_zen'
        ? '🎯 Focused Zen Mode (320 Qs) Performance Report'
        : currentTrack === 'zen'
        ? '🧘 General Zen Mode (320 Qs) Performance Report'
        : 'Exam 1 (125 Qs) Performance Report';"""

    score_replacement = """      const reportTitle = currentTrack === 'exam2'
        ? '🧠 Exam 2 (103 Qs) Performance Report'
        : currentTrack === 'focused_zen'
        ? '🎯 Focused Zen Mode (320 Qs) Performance Report'
        : currentTrack === 'zen'
        ? '🧘 General Zen Mode (320 Qs) Performance Report'
        : 'Exam 1 (125 Qs) Performance Report';"""

    if score_target in src:
        src = src.replace(score_target, score_replacement, 1)
        print("Replaced score report title.")
    else:
        print("Warning: score_target not found!")

    reset_target = """      let trackName = 'Exam 1 (125 questions)';
      let storagePrefix = 'usmle_exam1_';
      if (currentTrack === 'inhouse') {
        trackName = '🏠 In-House Course Track (385 questions)';
        storagePrefix = 'usmle_inhouse_';
      } else if (currentTrack === 'focused_zen') {
        trackName = '🎯 Focused Zen Mode (320 questions)';
        storagePrefix = 'usmle_focused_zen_';
      } else if (currentTrack === 'zen') {
        trackName = '🧘 General Zen Mode (320 questions)';
        storagePrefix = 'usmle_zen_';
      }"""

    reset_replacement = """      let trackName = 'Exam 1 (125 questions)';
      let storagePrefix = 'usmle_exam1_';
      if (currentTrack === 'exam2') {
        trackName = '🧠 Exam 2 (103 questions)';
        storagePrefix = 'usmle_exam2_';
      } else if (currentTrack === 'inhouse') {
        trackName = '🏠 In-House Course Track (385 questions)';
        storagePrefix = 'usmle_inhouse_';
      } else if (currentTrack === 'focused_zen') {
        trackName = '🎯 Focused Zen Mode (320 questions)';
        storagePrefix = 'usmle_focused_zen_';
      } else if (currentTrack === 'zen') {
        trackName = '🧘 General Zen Mode (320 questions)';
        storagePrefix = 'usmle_zen_';
      }"""

    if reset_target in src:
        src = src.replace(reset_target, reset_replacement, 1)
        print("Replaced reset track info.")
    else:
        print("Warning: reset_target not found!")

    # 16. Update Gemini prompt generator
    gemini_target = """      let prompt = `You are a medical board examination expert preparing high-yield USMLE Step 1 practice questions for a medical student.\\n\\n`;
      prompt += `The student just completed a comprehensive practice session on Neurology & Psychiatry (Course: 12 In-House Lecture Modules, 385 questions total).\\n`;"""

    gemini_replacement = """      let prompt = `You are an elite medical board examination expert preparing high-yield USMLE Step 1 practice questions for a medical student.\\n\\n`;
      if (currentTrack === 'exam2') {
        prompt += `The student just completed USMLE Practice Exam 2 (103 questions) covering the 9 core neuroscience sections:\\n`;
        prompt += `- Visual System, Visual Reflexes, Infection/Inflammation of eye disorders\\n`;
        prompt += `- Auditory & Vestibular Systems, UMN/LMN, Hypothalamus & Smell/Taste\\n`;
        prompt += `- Basal Ganglia, ALS, and Sleep.\\n\\n`;
      } else {
        prompt += `The student just completed a comprehensive practice session on Neurology & Psychiatry (Course: 12 In-House Lecture Modules, 385 questions total).\\n`;
      }"""

    if gemini_target in src:
        src = src.replace(gemini_target, gemini_replacement, 1)
        print("Replaced gemini prompt text.")
    else:
        print("Warning: gemini_target not found!")

    # 17. Update bootstrap / savedTrack handler
    boot_target = """      if (savedTrack === 'exam') {
        currentTrack = 'exam';
        examBtn.className = 'track-btn active';
        zenTray.style.display = 'none';
        trackTag.style.display = 'none';
        sidebarTitle.innerHTML = `<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/></svg> Subject Areas`;
      } else if (savedTrack === 'focused_zen') {"""

    boot_replacement = """      if (savedTrack === 'exam2') {
        currentTrack = 'exam2';
        if (exam2Btn) exam2Btn.className = 'track-btn exam2-active';
        zenTray.style.display = 'flex';
        trayIcon.textContent = '🧠';
        trayLabelText.textContent = 'Exam 2 Sections:';
        trackTag.style.display = 'inline-block';
        trackTag.className = 'q-track-tag exam2';
        trackTag.textContent = '🧠 Exam 2';
        timerDisplay.classList.add('exam2');
        sidebarTitle.innerHTML = `<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 8v8"/><path d="M8 12h8"/></svg> Exam 2 Sections (9)`;
      } else if (savedTrack === 'exam') {
        currentTrack = 'exam';
        examBtn.className = 'track-btn active';
        zenTray.style.display = 'none';
        trackTag.style.display = 'none';
        sidebarTitle.innerHTML = `<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/></svg> Subject Areas`;
      } else if (savedTrack === 'focused_zen') {"""

    if boot_target in src:
        src = src.replace(boot_target, boot_replacement, 1)
        print("Replaced boot handler.")
    else:
        print("Warning: boot_target not found!")

    # 18. Update resume toast in boot
    resume_target = """          const trackLabel = currentTrack === 'focused_zen'
            ? 'Focused Zen'
            : currentTrack === 'zen'
            ? 'General Zen'
            : 'Exam 1';"""

    resume_replacement = """          const trackLabel = currentTrack === 'exam2'
            ? 'Exam 2'
            : currentTrack === 'focused_zen'
            ? 'Focused Zen'
            : currentTrack === 'zen'
            ? 'General Zen'
            : (currentTrack === 'inhouse' ? 'In House' : 'Exam 1');"""

    if resume_target in src:
        src = src.replace(resume_target, resume_replacement, 1)
        print("Replaced resume toast.")
    else:
        print("Warning: resume_target not found!")

    # Save modified update_builder.py
    with open(UPDATE_BUILDER_PATH, 'w', encoding='utf-8') as f:
        f.write(src)
    print(f"Successfully updated {UPDATE_BUILDER_PATH}")

if __name__ == '__main__':
    main()
