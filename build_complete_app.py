# -*- coding: utf-8 -*-
# build_complete_app.py
import json
import os
import re

print("Starting build_complete_app.py...")

# Load datasets
with open('/Users/markyoussef_1/.gemini/antigravity-ide/scratch/usmle_exam1/questions_data.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

with open('/Users/markyoussef_1/.gemini/antigravity-ide/scratch/usmle_exam1/focused_zen_questions_data.json', 'r', encoding='utf-8') as f:
    focused_zen_questions = json.load(f)

with open('/Users/markyoussef_1/.gemini/antigravity-ide/scratch/usmle_exam1/zen_questions_data.json', 'r', encoding='utf-8') as f:
    zen_questions = json.load(f)

with open('/Users/markyoussef_1/.gemini/antigravity-ide/scratch/usmle_exam1/inhouse_questions_data.json', 'r', encoding='utf-8') as f:
    inhouse_questions = json.load(f)

categories = [
    'Central Nervous System Anatomy',
    'Central Nervous System Development',
    'Neurotransmitters and Action Potentials',
    'Ventricular System',
    'Acetylcholine / Neuromuscular Junction Disorder',
    'Neuroimaging',
    'Tactile Pathway',
    'Spinal Cord',
    'Pain Pathway',
    'Trigeminal Pathway',
    'Anesthetic & NMJ Blocking Agents',
    'Headache',
    'Cannabis Management',
    'Pathways and Opioids',
    'Traumatic Brain Injuries',
    'Meningitis'
]

inhouse_categories = [
    'In House: CNS Anatomy & Glia',
    'In House: CNS Development & Genetics',
    'In House: Neurotransmission & Synapse',
    'In House: Ventricular System & CSF',
    'In House: Neuromuscular Junction Disorders',
    'In House: Anesthetic Pharmacology',
    'In House: Somatosensory DCML Pathway',
    'In House: Somatosensory ALS & Pain',
    'In House: Trigeminal Pathways & Reflexes',
    'In House: Spinal Cord Syndromes & Radiculopathies',
    'In House: Neuropathies & Electrodiagnosis',
    'In House: Headache Disorders',
    'In House: Traumatic Brain Injuries',
    'In House: Meningitis & CNS Infections'
]

json_data_str = json.dumps(questions, ensure_ascii=False)
focused_zen_json_data_str = json.dumps(focused_zen_questions, ensure_ascii=False)
zen_json_data_str = json.dumps(zen_questions, ensure_ascii=False)
inhouse_json_data_str = json.dumps(inhouse_questions, ensure_ascii=False)
categories_json_str = json.dumps(categories, ensure_ascii=False)
inhouse_categories_json_str = json.dumps(inhouse_categories, ensure_ascii=False)

# Read base build_html.py
with open('/Users/markyoussef_1/.gemini/antigravity-ide/scratch/usmle_exam1/build_html.py', 'r', encoding='utf-8') as f:
    src = f.read()

# 1. Update dataset loading at the top
old_top = """with open('/Users/markyoussef_1/.gemini/antigravity-ide/scratch/usmle_exam1/zen_questions_data.json', 'r', encoding='utf-8') as f:
    zen_questions = json.load(f)"""

new_top = """with open('/Users/markyoussef_1/.gemini/antigravity-ide/scratch/usmle_exam1/zen_questions_data.json', 'r', encoding='utf-8') as f:
    zen_questions = json.load(f)

with open('/Users/markyoussef_1/.gemini/antigravity-ide/scratch/usmle_exam1/inhouse_questions_data.json', 'r', encoding='utf-8') as f:
    inhouse_questions = json.load(f)

inhouse_categories = [
    'In House: CNS Anatomy & Glia',
    'In House: CNS Development & Genetics',
    'In House: Neurotransmission & Synapse',
    'In House: Ventricular System & CSF',
    'In House: Neuromuscular Junction Disorders',
    'In House: Anesthetic Pharmacology',
    'In House: Somatosensory DCML Pathway',
    'In House: Somatosensory ALS & Pain',
    'In House: Trigeminal Pathways & Reflexes',
    'In House: Spinal Cord Syndromes & Radiculopathies',
    'In House: Neuropathies & Electrodiagnosis',
    'In House: Headache Disorders',
    'In House: Traumatic Brain Injuries',
    'In House: Meningitis & CNS Infections'
]"""

src = src.replace(old_top, new_top, 1)

old_dumps = """zen_json_data_str = json.dumps(zen_questions, ensure_ascii=False)
categories_json_str = json.dumps(categories, ensure_ascii=False)"""

new_dumps = """zen_json_data_str = json.dumps(zen_questions, ensure_ascii=False)
inhouse_json_data_str = json.dumps(inhouse_questions, ensure_ascii=False)
categories_json_str = json.dumps(categories, ensure_ascii=False)
inhouse_categories_json_str = json.dumps(inhouse_categories, ensure_ascii=False)"""

src = src.replace(old_dumps, new_dumps, 1)

# 2. Add CSS rules for inhouse track
old_css_btn = """.track-btn.focused-zen-active {
      background: linear-gradient(135deg, #8b5cf6, #3b82f6);
      color: #ffffff;
      box-shadow: 0 2px 10px rgba(139, 92, 246, 0.45);
    }"""

new_css_btn = """.track-btn.inhouse-active {
      background: linear-gradient(135deg, #f59e0b, #ea580c);
      color: #ffffff;
      box-shadow: 0 2px 10px rgba(245, 158, 11, 0.45);
    }

    .track-btn.focused-zen-active {
      background: linear-gradient(135deg, #8b5cf6, #3b82f6);
      color: #ffffff;
      box-shadow: 0 2px 10px rgba(139, 92, 246, 0.45);
    }"""

src = src.replace(old_css_btn, new_css_btn, 1)

old_css_timer = """.timer-box.focused-zen {
      color: #a78bfa;
      border-color: rgba(139, 92, 246, 0.4);
      background: rgba(139, 92, 246, 0.1);
    }"""

new_css_timer = """.timer-box.inhouse {
      color: #f59e0b;
      border-color: rgba(245, 158, 11, 0.4);
      background: rgba(245, 158, 11, 0.1);
    }

    .timer-box.focused-zen {
      color: #a78bfa;
      border-color: rgba(139, 92, 246, 0.4);
      background: rgba(139, 92, 246, 0.1);
    }"""

src = src.replace(old_css_timer, new_css_timer, 1)

old_css_cat = """.cat-item.focused-zen-cat.active {
      background: rgba(139, 92, 246, 0.15);
      border-color: #8b5cf6;
    }"""

new_css_cat = """.cat-item.inhouse-cat.active {
      background: rgba(245, 158, 11, 0.15);
      border-color: #f59e0b;
    }

    .cat-item.focused-zen-cat.active {
      background: rgba(139, 92, 246, 0.15);
      border-color: #8b5cf6;
    }"""

src = src.replace(old_css_cat, new_css_cat, 1)

old_css_badge = """.q-num-badge.focused-zen {
      background: rgba(139, 92, 246, 0.15);
      color: #a78bfa;
      border: 1px solid rgba(139, 92, 246, 0.35);
    }"""

new_css_badge = """.q-num-badge.inhouse {
      background: rgba(245, 158, 11, 0.15);
      color: #f59e0b;
      border: 1px solid rgba(245, 158, 11, 0.35);
    }

    .q-num-badge.focused-zen {
      background: rgba(139, 92, 246, 0.15);
      color: #a78bfa;
      border: 1px solid rgba(139, 92, 246, 0.35);
    }"""

src = src.replace(old_css_badge, new_css_badge, 1)

old_css_tag = """.q-track-tag.focused-zen {
      background: linear-gradient(135deg, rgba(139, 92, 246, 0.2), rgba(59, 130, 246, 0.2));
      color: #c4b5fd;
      border: 1px solid rgba(139, 92, 246, 0.4);
    }"""

new_css_tag = """.q-track-tag.inhouse {
      background: linear-gradient(135deg, rgba(245, 158, 11, 0.2), rgba(234, 88, 12, 0.2));
      color: #fbbf24;
      border: 1px solid rgba(245, 158, 11, 0.4);
    }

    .q-track-tag.focused-zen {
      background: linear-gradient(135deg, rgba(139, 92, 246, 0.2), rgba(59, 130, 246, 0.2));
      color: #c4b5fd;
      border: 1px solid rgba(139, 92, 246, 0.4);
    }"""

src = src.replace(old_css_tag, new_css_tag, 1)

# 3. Add In House track switcher button in Header
old_header_switcher = """        <button id=\"trackFocusedZenBtn\" class=\"track-btn focused-zen-active\" onclick=\"switchTrack('focused_zen')\">
          <span>🎯</span>
          <span>Focused Zen (320 Qs)</span>
          <span class=\"zen-pill-badge\">Study Guide</span>
        </button>"""

new_header_switcher = """        <button id=\"trackInHouseBtn\" class=\"track-btn inhouse-active\" onclick=\"switchTrack('inhouse')\">
          <span>🏠</span>
          <span>In House (150 Qs)</span>
          <span class=\"zen-pill-badge\">Course Modules</span>
        </button>
        <button id=\"trackFocusedZenBtn\" class=\"track-btn\" onclick=\"switchTrack('focused_zen')\">
          <span>🎯</span>
          <span>Focused Zen (320 Qs)</span>
          <span class=\"zen-pill-badge\">Study Guide</span>
        </button>"""

src = src.replace(old_header_switcher, new_header_switcher, 1)

# 4. Update JavaScript raw data variables
old_raw_vars = """    const rawFocusedZenQuestions = \"\"\" + focused_zen_json_data_str + \"\"\";
    const rawZenQuestions = \"\"\" + zen_json_data_str + \"\"\";
    const subjectCategories = \"\"\" + categories_json_str + \"\"\";"""

new_raw_vars = """    const rawFocusedZenQuestions = \"\"\" + focused_zen_json_data_str + \"\"\";
    const rawZenQuestions = \"\"\" + zen_json_data_str + \"\"\";
    const rawInHouseQuestions = \"\"\" + inhouse_json_data_str + \"\"\";
    const subjectCategories = \"\"\" + categories_json_str + \"\"\";
    const inHouseCategories = \"\"\" + inhouse_categories_json_str + \"\"\";"""

src = src.replace(old_raw_vars, new_raw_vars, 1)

# 5. Update default track to inhouse and switchTrack logic
old_switch_track = """      const examBtn = document.getElementById('trackExamBtn');
      const focusedZenBtn = document.getElementById('trackFocusedZenBtn');
      const zenBtn = document.getElementById('trackZenBtn');
      const zenTray = document.getElementById('zenSectionTray');
      const trayIcon = document.getElementById('zenTrayIcon');
      const trayLabelText = document.getElementById('zenTrayLabelText');
      const trackTag = document.getElementById('currentQTrackTag');
      const sidebarTitle = document.getElementById('sidebarTitle');
      const timerDisplay = document.getElementById('timerDisplay');

      examBtn.className = 'track-btn';
      focusedZenBtn.className = 'track-btn';
      zenBtn.className = 'track-btn';
      timerDisplay.classList.remove('zen', 'focused-zen');

      if (currentTrack === 'focused_zen') {
        focusedZenBtn.className = 'track-btn focused-zen-active';
        zenTray.style.display = 'flex';
        trayIcon.textContent = '🎯';
        trayLabelText.textContent = 'Study Guide Topics:';
        trackTag.style.display = 'inline-block';
        trackTag.className = 'q-track-tag focused-zen';
        trackTag.textContent = '🎯 Focused Zen';
        timerDisplay.classList.add('focused-zen');
        sidebarTitle.innerHTML = `<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 8v8"/><path d="M8 12h8"/></svg> Study Guide Topics (20/each)`;
      } else if (currentTrack === 'zen') {
        zenBtn.className = 'track-btn zen-active';
        zenTray.style.display = 'flex';
        trayIcon.textContent = '🧘';
        trayLabelText.textContent = 'General Topics:';
        trackTag.style.display = 'inline-block';
        trackTag.className = 'q-track-tag zen';
        trackTag.textContent = '🧘 Zen Mode';
        timerDisplay.classList.add('zen');
        sidebarTitle.innerHTML = `<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2a10 10 0 1 0 10 10A10 10 0 0 0 12 2zm0 18a8 8 0 1 1 8-8 8 8 0 0 1-8 8z"/></svg> Zen Topics (20/each)`;
      } else {
        examBtn.className = 'track-btn active';
        zenTray.style.display = 'none';
        trackTag.style.display = 'none';
        sidebarTitle.innerHTML = `<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/></svg> Subject Areas`;
      }

      activeCategoryFilter = null;
      filterFlaggedOnly = false;
      filterIncorrectOnly = false;

      loadTrackState();
      if (currentTrack === 'focused_zen' || currentTrack === 'zen') {
        renderZenTray();
      }
      applyFilter();
      renderSidebarCategories();
      updateOverallStats();
      renderCurrentQuestion();

      const toastMsg = currentTrack === 'focused_zen'
        ? 'Switched to 🎯 Focused Zen Mode (Study Guide 20 Qs/topic)'
        : currentTrack === 'zen'
        ? 'Switched to 🧘 General Zen Mode (20 Qs/topic)'
        : 'Switched to 📝 Exam 1 Practice (125 Qs)';"""

new_switch_track = """      const inHouseBtn = document.getElementById('trackInHouseBtn');
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

      if (currentTrack === 'inhouse') {
        if (inHouseBtn) inHouseBtn.className = 'track-btn inhouse-active';
        zenTray.style.display = 'flex';
        trayIcon.textContent = '🏠';
        trayLabelText.textContent = 'In-House Modules:';
        trackTag.style.display = 'inline-block';
        trackTag.className = 'q-track-tag inhouse';
        trackTag.textContent = '🏠 In House';
        timerDisplay.classList.add('inhouse');
        sidebarTitle.innerHTML = `<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg> In-House Course Modules (14)`;
      } else if (currentTrack === 'focused_zen') {
        focusedZenBtn.className = 'track-btn focused-zen-active';
        zenTray.style.display = 'flex';
        trayIcon.textContent = '🎯';
        trayLabelText.textContent = 'Study Guide Topics:';
        trackTag.style.display = 'inline-block';
        trackTag.className = 'q-track-tag focused-zen';
        trackTag.textContent = '🎯 Focused Zen';
        timerDisplay.classList.add('focused-zen');
        sidebarTitle.innerHTML = `<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 8v8"/><path d="M8 12h8"/></svg> Study Guide Topics (20/each)`;
      } else if (currentTrack === 'zen') {
        zenBtn.className = 'track-btn zen-active';
        zenTray.style.display = 'flex';
        trayIcon.textContent = '🧘';
        trayLabelText.textContent = 'General Topics:';
        trackTag.style.display = 'inline-block';
        trackTag.className = 'q-track-tag zen';
        trackTag.textContent = '🧘 Zen Mode';
        timerDisplay.classList.add('zen');
        sidebarTitle.innerHTML = `<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2a10 10 0 1 0 10 10A10 10 0 0 0 12 2zm0 18a8 8 0 1 1 8-8 8 8 0 0 1-8 8z"/></svg> Zen Topics (20/each)`;
      } else {
        examBtn.className = 'track-btn active';
        zenTray.style.display = 'none';
        trackTag.style.display = 'none';
        sidebarTitle.innerHTML = `<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/></svg> Subject Areas`;
      }

      activeCategoryFilter = null;
      filterFlaggedOnly = false;
      filterIncorrectOnly = false;

      loadTrackState();
      if (currentTrack === 'inhouse' || currentTrack === 'focused_zen' || currentTrack === 'zen') {
        renderZenTray();
      }
      applyFilter();
      renderSidebarCategories();
      updateOverallStats();
      renderCurrentQuestion();

      const toastMsg = currentTrack === 'inhouse'
        ? 'Switched to 🏠 In-House Course Track (150 Qs from Lectures & Cases)'
        : currentTrack === 'focused_zen'
        ? 'Switched to 🎯 Focused Zen Mode (Study Guide 20 Qs/topic)'
        : currentTrack === 'zen'
        ? 'Switched to 🧘 General Zen Mode (20 Qs/topic)'
        : 'Switched to 📝 Exam 1 Practice (125 Qs)';"""

src = src.replace(old_switch_track, new_switch_track, 1)

# 6. Update loadTrackState and saveState
old_load_state = """      let storagePrefix = 'usmle_exam1_';
      let rawData = rawExamQuestions;
      if (currentTrack === 'focused_zen') {
        storagePrefix = 'usmle_focused_zen_';
        rawData = rawFocusedZenQuestions;
      } else if (currentTrack === 'zen') {
        storagePrefix = 'usmle_zen_';
        rawData = rawZenQuestions;
      }"""

new_load_state = """      let storagePrefix = 'usmle_exam1_';
      let rawData = rawExamQuestions;
      if (currentTrack === 'inhouse') {
        storagePrefix = 'usmle_inhouse_';
        rawData = rawInHouseQuestions;
      } else if (currentTrack === 'focused_zen') {
        storagePrefix = 'usmle_focused_zen_';
        rawData = rawFocusedZenQuestions;
      } else if (currentTrack === 'zen') {
        storagePrefix = 'usmle_zen_';
        rawData = rawZenQuestions;
      }"""

src = src.replace(old_load_state, new_load_state, 1)

old_save_state = """      let storagePrefix = 'usmle_exam1_';
      if (currentTrack === 'focused_zen') storagePrefix = 'usmle_focused_zen_';
      else if (currentTrack === 'zen') storagePrefix = 'usmle_zen_';"""

new_save_state = """      let storagePrefix = 'usmle_exam1_';
      if (currentTrack === 'inhouse') storagePrefix = 'usmle_inhouse_';
      else if (currentTrack === 'focused_zen') storagePrefix = 'usmle_focused_zen_';
      else if (currentTrack === 'zen') storagePrefix = 'usmle_zen_';"""

src = src.replace(old_save_state, new_save_state, 1)

# 7. Update renderZenTray categories
old_render_tray = """    function renderZenTray() {
      const container = document.getElementById('zenTopicPillsContainer');
      const allPill = document.getElementById('zenTopicPillAll');
      allPill.className = 'zen-topic-pill ' + (activeCategoryFilter === null ? 'active' : '');
      allPill.innerHTML = `<span>All 16 Topics</span><span class="chip-count">${questions.length}</span>`;

      let html = '';
      subjectCategories.forEach((cat) => {"""

new_render_tray = """    function renderZenTray() {
      const container = document.getElementById('zenTopicPillsContainer');
      const allPill = document.getElementById('zenTopicPillAll');
      allPill.className = 'zen-topic-pill ' + (activeCategoryFilter === null ? 'active' : '');
      const catsToUse = currentTrack === 'inhouse' ? inHouseCategories : subjectCategories;
      allPill.innerHTML = `<span>All ${catsToUse.length} Topics</span><span class=\"chip-count\">${questions.length}</span>`;

      let html = '';
      catsToUse.forEach((cat) => {"""

src = src.replace(old_render_tray, new_render_tray, 1)

# 8. Update renderSidebarCategories
old_render_sidebar = """    function renderSidebarCategories() {
      const container = document.getElementById('categoryList');
      container.innerHTML = '';

      subjectCategories.forEach((cat) => {"""

new_render_sidebar = """    function renderSidebarCategories() {
      const container = document.getElementById('categoryList');
      container.innerHTML = '';

      const catsToUse = currentTrack === 'inhouse' ? inHouseCategories : subjectCategories;
      catsToUse.forEach((cat) => {"""

src = src.replace(old_render_sidebar, new_render_sidebar, 1)

old_cat_class = """const catClass = currentTrack === 'focused_zen' ? 'focused-zen-cat' : currentTrack === 'zen' ? 'zen-cat' : '';"""
new_cat_class = """const catClass = currentTrack === 'inhouse' ? 'inhouse-cat' : currentTrack === 'focused_zen' ? 'focused-zen-cat' : currentTrack === 'zen' ? 'zen-cat' : '';"""
src = src.replace(old_cat_class, new_cat_class, 1)

# 9. Update badge styling in renderCurrentQuestion
old_badge_class = """badgeElem.className = 'q-num-badge ' + (currentTrack === 'focused_zen' ? 'focused-zen' : currentTrack === 'zen' ? 'zen' : '');"""
new_badge_class = """badgeElem.className = 'q-num-badge ' + (currentTrack === 'inhouse' ? 'inhouse' : currentTrack === 'focused_zen' ? 'focused-zen' : currentTrack === 'zen' ? 'zen' : '');"""
src = src.replace(old_badge_class, new_badge_class, 1)

# 10. Update resetProgress track detection
old_reset = """      let storagePrefix = 'usmle_exam1_';
      let trackName = 'Exam 1 (125 Qs)';
      if (currentTrack === 'focused_zen') {
        trackName = '🎯 Focused Zen Mode (320 Qs)';
        storagePrefix = 'usmle_focused_zen_';
      } else if (currentTrack === 'zen') {
        trackName = '🧘 General Zen Mode (320 Qs)';
        storagePrefix = 'usmle_zen_';
      }"""

new_reset = """      let storagePrefix = 'usmle_exam1_';
      let trackName = 'Exam 1 (125 Qs)';
      if (currentTrack === 'inhouse') {
        trackName = '🏠 In-House Course Track (150 Qs)';
        storagePrefix = 'usmle_inhouse_';
      } else if (currentTrack === 'focused_zen') {
        trackName = '🎯 Focused Zen Mode (320 Qs)';
        storagePrefix = 'usmle_focused_zen_';
      } else if (currentTrack === 'zen') {
        trackName = '🧘 General Zen Mode (320 Qs)';
        storagePrefix = 'usmle_zen_';
      }"""

src = src.replace(old_reset, new_reset, 1)

# 11. Update bootstrapper
old_boot = """      // Check saved track, defaulting to Focused Zen Mode
      const savedTrack = localStorage.getItem('usmle_active_track');
      if (savedTrack === 'exam') {
        currentTrack = 'exam';
        document.getElementById('trackExamBtn').className = 'track-btn active';
        document.getElementById('trackFocusedZenBtn').className = 'track-btn';
        document.getElementById('trackZenBtn').className = 'track-btn';
        document.getElementById('zenSectionTray').style.display = 'none';
        document.getElementById('currentQTrackTag').style.display = 'none';
        document.getElementById('timerDisplay').classList.remove('zen', 'focused-zen');
        document.getElementById('sidebarTitle').innerHTML = `<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/></svg> Subject Areas`;
      } else if (savedTrack === 'zen') {
        currentTrack = 'zen';
        document.getElementById('trackExamBtn').className = 'track-btn';
        document.getElementById('trackFocusedZenBtn').className = 'track-btn';
        document.getElementById('trackZenBtn').className = 'track-btn zen-active';
        document.getElementById('zenSectionTray').style.display = 'flex';
        document.getElementById('zenTrayIcon').textContent = '🧘';
        document.getElementById('zenTrayLabelText').textContent = 'General Topics:';
        document.getElementById('currentQTrackTag').style.display = 'inline-block';
        document.getElementById('currentQTrackTag').className = 'q-track-tag zen';
        document.getElementById('currentQTrackTag').textContent = '🧘 Zen Mode';
        document.getElementById('timerDisplay').classList.add('zen');
        document.getElementById('sidebarTitle').innerHTML = `<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2a10 10 0 1 0 10 10A10 10 0 0 0 12 2zm0 18a8 8 0 1 1 8-8 8 8 0 0 1-8 8z"/></svg> Zen Topics (20/each)`;
      } else {
        // Default to Focused Zen Mode
        currentTrack = 'focused_zen';
        document.getElementById('trackExamBtn').className = 'track-btn';
        document.getElementById('trackFocusedZenBtn').className = 'track-btn focused-zen-active';
        document.getElementById('trackZenBtn').className = 'track-btn';
        document.getElementById('zenSectionTray').style.display = 'flex';
        document.getElementById('zenTrayIcon').textContent = '🎯';
        document.getElementById('zenTrayLabelText').textContent = 'Study Guide Topics:';
        document.getElementById('currentQTrackTag').style.display = 'inline-block';
        document.getElementById('currentQTrackTag').className = 'q-track-tag focused-zen';
        document.getElementById('currentQTrackTag').textContent = '🎯 Focused Zen';
        document.getElementById('timerDisplay').classList.add('focused-zen');
        document.getElementById('sidebarTitle').innerHTML = `<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 8v8"/><path d="M8 12h8"/></svg> Study Guide Topics (20/each)`;
      }"""

new_boot = """      // Check saved track, defaulting to In House Mode
      const savedTrack = localStorage.getItem('usmle_active_track');
      const inHouseBtn = document.getElementById('trackInHouseBtn');
      const examBtn = document.getElementById('trackExamBtn');
      const focusedZenBtn = document.getElementById('trackFocusedZenBtn');
      const zenBtn = document.getElementById('trackZenBtn');
      const zenTray = document.getElementById('zenSectionTray');
      const trayIcon = document.getElementById('zenTrayIcon');
      const trayLabelText = document.getElementById('zenTrayLabelText');
      const trackTag = document.getElementById('currentQTrackTag');
      const sidebarTitle = document.getElementById('sidebarTitle');
      const timerDisplay = document.getElementById('timerDisplay');

      timerDisplay.classList.remove('zen', 'focused-zen', 'inhouse');
      if (inHouseBtn) inHouseBtn.className = 'track-btn';
      examBtn.className = 'track-btn';
      focusedZenBtn.className = 'track-btn';
      zenBtn.className = 'track-btn';

      if (savedTrack === 'exam') {
        currentTrack = 'exam';
        examBtn.className = 'track-btn active';
        zenTray.style.display = 'none';
        trackTag.style.display = 'none';
        sidebarTitle.innerHTML = `<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/></svg> Subject Areas`;
      } else if (savedTrack === 'focused_zen') {
        currentTrack = 'focused_zen';
        focusedZenBtn.className = 'track-btn focused-zen-active';
        zenTray.style.display = 'flex';
        trayIcon.textContent = '🎯';
        trayLabelText.textContent = 'Study Guide Topics:';
        trackTag.style.display = 'inline-block';
        trackTag.className = 'q-track-tag focused-zen';
        trackTag.textContent = '🎯 Focused Zen';
        timerDisplay.classList.add('focused-zen');
        sidebarTitle.innerHTML = `<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 8v8"/><path d="M8 12h8"/></svg> Study Guide Topics (20/each)`;
      } else if (savedTrack === 'zen') {
        currentTrack = 'zen';
        zenBtn.className = 'track-btn zen-active';
        zenTray.style.display = 'flex';
        trayIcon.textContent = '🧘';
        trayLabelText.textContent = 'General Topics:';
        trackTag.style.display = 'inline-block';
        trackTag.className = 'q-track-tag zen';
        trackTag.textContent = '🧘 Zen Mode';
        timerDisplay.classList.add('zen');
        sidebarTitle.innerHTML = `<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2a10 10 0 1 0 10 10A10 10 0 0 0 12 2zm0 18a8 8 0 1 1 8-8 8 8 0 0 1-8 8z"/></svg> Zen Topics (20/each)`;
      } else {
        // Default to In-House Course Track
        currentTrack = 'inhouse';
        if (inHouseBtn) inHouseBtn.className = 'track-btn inhouse-active';
        zenTray.style.display = 'flex';
        trayIcon.textContent = '🏠';
        trayLabelText.textContent = 'In-House Modules:';
        trackTag.style.display = 'inline-block';
        trackTag.className = 'q-track-tag inhouse';
        trackTag.textContent = '🏠 In House';
        timerDisplay.classList.add('inhouse');
        sidebarTitle.innerHTML = `<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg> In-House Course Modules (14)`;
      }"""

src = src.replace(old_boot, new_boot, 1)

# Write the updated build_html.py
with open('/Users/markyoussef_1/.gemini/antigravity-ide/scratch/usmle_exam1/build_html.py', 'w', encoding='utf-8') as f:
    f.write(src)

print("build_html.py successfully updated with 4-track support! Now running build_html.py to generate index.html...")
