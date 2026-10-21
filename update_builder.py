# generate_complete_app.py
import json
import os

with open('/Users/markyoussef_1/.gemini/antigravity-ide/scratch/usmle_exam1/questions_data.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

with open('/Users/markyoussef_1/.gemini/antigravity-ide/scratch/usmle_exam1/focused_zen_questions_data.json', 'r', encoding='utf-8') as f:
    focused_zen_questions = json.load(f)

with open('/Users/markyoussef_1/.gemini/antigravity-ide/scratch/usmle_exam1/zen_questions_data.json', 'r', encoding='utf-8') as f:
    zen_questions = json.load(f)

with open('/Users/markyoussef_1/.gemini/antigravity-ide/scratch/usmle_exam1/inhouse_questions_data.json', 'r', encoding='utf-8') as f:
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
]

inhouse_categories = [
    'CNS Anatomy & Gross Morphology',
    'CNS Development & Congenital Malformations',
    'Ventricular System, CSF Dynamics & Glial Histology',
    'Action Potentials & Synaptic Neurotransmission',
    'Neuromuscular Junction Disorders & Toxicology',
    'Anesthetic Pharmacology & Neuromuscular Blockade',
    'Somatosensory DCML Pathway & Mechanoreceptors',
    'Anterolateral System & Spinal Cord Syndromes',
    'Trigeminal System, Facial Sensation & Reflexes',
    'Headache Disorders & Neurovascular Syndromes',
    'Traumatic Brain Injury, Hematomas & Critical Care',
    'CNS Infectious Diseases & Meningitis'
]

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

json_data_str = json.dumps(questions, ensure_ascii=False)
focused_zen_json_data_str = json.dumps(focused_zen_questions, ensure_ascii=False)
zen_json_data_str = json.dumps(zen_questions, ensure_ascii=False)
inhouse_json_data_str = json.dumps(inhouse_questions, ensure_ascii=False)
exam2_json_data_str = json.dumps(exam2_questions, ensure_ascii=False)
categories_json_str = json.dumps(categories, ensure_ascii=False)
inhouse_categories_json_str = json.dumps(inhouse_categories, ensure_ascii=False)
exam2_categories_json_str = json.dumps(exam2_categories, ensure_ascii=False)

html_template = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>USMLE Step 1 - NeuroPsych Practice Exam & Focused Zen Mode</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg-primary: #0f172a;
      --bg-secondary: #1e293b;
      --bg-card: #1e293b;
      --bg-hover: #334155;
      --border-color: #334155;
      --border-light: #475569;
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
      --text-dim: #64748b;
      --accent: #38bdf8;
      --accent-glow: rgba(56, 189, 248, 0.25);
      --success: #10b981;
      --success-glow: rgba(16, 185, 129, 0.2);
      --error: #f43f5e;
      --error-glow: rgba(244, 63, 94, 0.2);
      --warning: #f59e0b;
      --warning-glow: rgba(245, 158, 11, 0.2);
      --purple: #a855f7;
      --purple-glow: rgba(168, 85, 247, 0.25);
      --zen-primary: #10b981;
      --zen-glow: rgba(16, 185, 129, 0.35);
      --focused-primary: #8b5cf6;
      --focused-glow: rgba(139, 92, 246, 0.35);
      --font-sans: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
      --font-mono: 'JetBrains Mono', monospace;
      --radius-sm: 6px;
      --radius-md: 10px;
      --radius-lg: 16px;
      --shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.3);
      --shadow-md: 0 4px 12px rgba(0, 0, 0, 0.4);
      --shadow-lg: 0 12px 32px rgba(0, 0, 0, 0.5);
    }

    [data-theme="light"] {
      --bg-primary: #f8fafc;
      --bg-secondary: #ffffff;
      --bg-card: #ffffff;
      --bg-hover: #f1f5f9;
      --border-color: #e2e8f0;
      --border-light: #cbd5e1;
      --text-main: #0f172a;
      --text-muted: #64748b;
      --text-dim: #94a3b8;
      --accent: #0284c7;
      --accent-glow: rgba(2, 132, 199, 0.2);
      --success: #059669;
      --success-glow: rgba(5, 150, 105, 0.15);
      --error: #e11d48;
      --error-glow: rgba(225, 29, 72, 0.15);
      --warning: #d97706;
      --warning-glow: rgba(217, 119, 6, 0.15);
      --purple: #9333ea;
      --zen-primary: #059669;
      --focused-primary: #7c3aed;
      --shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.05);
      --shadow-md: 0 4px 12px rgba(0, 0, 0, 0.08);
      --shadow-lg: 0 12px 32px rgba(0, 0, 0, 0.12);
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      font-family: var(--font-sans);
      background-color: var(--bg-primary);
      color: var(--text-main);
      height: 100vh;
      display: flex;
      flex-direction: column;
      overflow: hidden;
      line-height: 1.5;
    }

        /* Level 1: Exam Selector Tabs */
    .exam-selector-tabs {
      display: inline-flex;
      background: rgba(15, 23, 42, 0.7);
      border: 1.5px solid rgba(255, 255, 255, 0.12);
      border-radius: 999px;
      padding: 3px;
      gap: 3px;
      box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.4);
    }

    .exam-tab-btn {
      display: flex;
      align-items: center;
      gap: 7px;
      background: transparent;
      border: none;
      color: var(--text-muted);
      font-family: inherit;
      font-size: 0.82rem;
      font-weight: 700;
      padding: 5px 14px;
      border-radius: 999px;
      cursor: pointer;
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
      white-space: nowrap;
    }

    .exam-tab-btn:hover {
      color: var(--text-main);
      background: rgba(255, 255, 255, 0.05);
    }

    .exam-tab-btn.active-exam1 {
      background: linear-gradient(135deg, #0284c7, #38bdf8);
      color: #041324;
      font-weight: 800;
      box-shadow: 0 2px 10px rgba(56, 189, 248, 0.45);
    }

    .exam-tab-btn.active-exam2 {
      background: linear-gradient(135deg, #8b5cf6, #3b82f6);
      color: #ffffff;
      font-weight: 800;
      box-shadow: 0 2px 10px rgba(139, 92, 246, 0.45);
    }

    .switcher-separator {
      width: 1px;
      height: 22px;
      background: var(--border-color);
      margin: 0 2px;
    }

    /* Track switcher tabs */
    .track-switcher {
      display: inline-flex;
      background: rgba(0, 0, 0, 0.25);
      border: 1px solid var(--border-color);
      border-radius: 999px;
      padding: 3px;
      gap: 3px;
    }

    .track-btn {
      display: flex;
      align-items: center;
      gap: 6px;
      background: transparent;
      border: none;
      color: var(--text-muted);
      font-family: inherit;
      font-size: 0.78rem;
      font-weight: 600;
      padding: 5px 12px;
      border-radius: 999px;
      cursor: pointer;
      transition: all 0.2s ease;
      white-space: nowrap;
    }

    .track-btn:hover {
      color: var(--text-main);
    }

    .track-btn.active {
      background: var(--accent);
      color: #0f172a;
      box-shadow: 0 2px 8px var(--accent-glow);
    }

    .track-btn.exam2-active {
      background: linear-gradient(135deg, #0ea5e9, #2563eb);
      color: #ffffff;
      box-shadow: 0 2px 10px rgba(14, 165, 233, 0.45);
    }

    .track-btn.inhouse-active {
      background: linear-gradient(135deg, #f59e0b, #ea580c);
      color: #ffffff;
      box-shadow: 0 2px 10px rgba(245, 158, 11, 0.45);
    }

    .track-btn.focused-zen-active {
      background: linear-gradient(135deg, #8b5cf6, #3b82f6);
      color: #ffffff;
      box-shadow: 0 2px 10px rgba(139, 92, 246, 0.45);
    }

    .track-btn.zen-active {
      background: linear-gradient(135deg, #10b981, #06b6d4);
      color: #ffffff;
      box-shadow: 0 2px 10px var(--zen-glow);
    }

    .zen-pill-badge {
      background: rgba(255, 255, 255, 0.25);
      font-size: 0.65rem;
      padding: 1px 6px;
      border-radius: 999px;
      font-weight: 700;
    }

    /* Header */
    header.exam-header {
      background: var(--bg-secondary);
      border-bottom: 1px solid var(--border-color);
      height: 56px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 16px;
      flex-shrink: 0;
      z-index: 20;
    }

    .header-left, .header-center, .header-right {
      display: flex;
      align-items: center;
      gap: 12px;
    }

    .logo-badge {
      display: flex;
      align-items: center;
      gap: 8px;
      font-weight: 700;
      font-size: 0.95rem;
      letter-spacing: -0.01em;
      color: var(--accent);
    }

    .logo-badge svg {
      width: 22px;
      height: 22px;
      fill: currentColor;
    }

    .timer-box {
      display: flex;
      align-items: center;
      gap: 6px;
      background: rgba(0, 0, 0, 0.2);
      border: 1px solid var(--border-color);
      padding: 4px 10px;
      border-radius: var(--radius-sm);
      font-family: var(--font-mono);
      font-size: 0.85rem;
      font-weight: 600;
      color: var(--text-muted);
    }

    .timer-box.zen {
      border-color: rgba(16, 185, 129, 0.4);
      color: #34d399;
    }

    .timer-box.exam2 {
      border-color: rgba(56, 189, 248, 0.4);
      color: #38bdf8;
    }

    .timer-box.focused-zen {
      border-color: rgba(139, 92, 246, 0.4);
      color: #c084fc;
    }

    /* Buttons */
    .btn {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      color: var(--text-main);
      padding: 6px 12px;
      border-radius: var(--radius-sm);
      font-family: inherit;
      font-size: 0.82rem;
      font-weight: 500;
      cursor: pointer;
      transition: all 0.15s ease;
      user-select: none;
      white-space: nowrap;
    }

    .btn:hover {
      background: var(--bg-hover);
      border-color: var(--border-light);
    }

    .btn-accent {
      background: var(--accent);
      border-color: var(--accent);
      color: #0f172a;
      font-weight: 600;
    }

    .btn-accent:hover {
      filter: brightness(1.1);
      box-shadow: 0 0 12px var(--accent-glow);
    }

    .btn-purple {
      background: linear-gradient(135deg, #8b5cf6, #d946ef);
      border-color: #a855f7;
      color: #ffffff;
      font-weight: 600;
      box-shadow: 0 2px 8px var(--purple-glow);
    }

    .btn-purple:hover {
      filter: brightness(1.12);
      box-shadow: 0 0 14px var(--purple-glow);
    }

    .btn-icon {
      padding: 6px;
      width: 32px;
      height: 32px;
    }

    .btn-success {
      background: var(--success);
      border-color: var(--success);
      color: white;
    }

    .btn-error {
      background: var(--error);
      border-color: var(--error);
      color: white;
    }

    /* Zen Mode Top Tray */
    .zen-section-tray {
      background: #090d16;
      border-bottom: 1px solid var(--border-color);
      padding: 8px 16px;
      display: flex;
      align-items: center;
      gap: 8px;
      overflow-x: auto;
      scrollbar-width: thin;
      flex-shrink: 0;
      z-index: 15;
    }

    .zen-section-tray::-webkit-scrollbar {
      height: 4px;
    }

    .zen-section-tray::-webkit-scrollbar-thumb {
      background: var(--border-color);
      border-radius: 4px;
    }

    .zen-tray-label {
      font-size: 0.75rem;
      font-weight: 700;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.05em;
      white-space: nowrap;
      display: flex;
      align-items: center;
      gap: 4px;
      margin-right: 4px;
    }

    .zen-topic-pill {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid rgba(255, 255, 255, 0.1);
      color: var(--text-muted);
      padding: 4px 10px;
      border-radius: 999px;
      font-size: 0.75rem;
      font-weight: 500;
      cursor: pointer;
      white-space: nowrap;
      transition: all 0.15s ease;
    }

    .zen-topic-pill:hover {
      background: rgba(255, 255, 255, 0.1);
      color: var(--text-main);
    }

    .zen-topic-pill.active {
      background: linear-gradient(135deg, rgba(139, 92, 246, 0.25), rgba(56, 189, 248, 0.25));
      border-color: var(--accent);
      color: var(--text-main);
      font-weight: 600;
      box-shadow: 0 0 10px var(--accent-glow);
    }

    .zen-topic-pill .chip-count {
      background: rgba(0, 0, 0, 0.35);
      padding: 1px 6px;
      border-radius: 999px;
      font-size: 0.68rem;
      font-family: var(--font-mono);
      font-weight: 600;
    }

    /* Main Layout */
    .app-body {
      display: flex;
      flex: 1;
      overflow: hidden;
      position: relative;
    }

    /* Left Sidebar */
    aside.sidebar-left {
      width: 310px;
      background: var(--bg-secondary);
      border-right: 1px solid var(--border-color);
      display: flex;
      flex-direction: column;
      flex-shrink: 0;
      transition: width 0.2s ease, transform 0.2s ease;
      z-index: 10;
    }

    aside.sidebar-left.collapsed {
      width: 0;
      overflow: hidden;
      border-right: none;
    }

    .sidebar-header {
      padding: 14px 16px;
      border-bottom: 1px solid var(--border-color);
      display: flex;
      align-items: center;
      justify-content: space-between;
    }

    .sidebar-header h2 {
      font-size: 0.88rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--text-muted);
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .overall-stats-card {
      margin: 12px 14px;
      background: rgba(0, 0, 0, 0.25);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-md);
      padding: 12px;
    }

    .overall-stats-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 6px;
      text-align: center;
    }

    .stat-item .val {
      font-size: 1.05rem;
      font-weight: 700;
      font-family: var(--font-mono);
      color: var(--accent);
    }

    .stat-item .lbl {
      font-size: 0.65rem;
      color: var(--text-dim);
      text-transform: uppercase;
      margin-top: 2px;
    }

    .sidebar-actions-wrap {
      padding: 0 14px 8px;
    }

    .quick-filter-row {
      display: flex;
      gap: 6px;
      margin-bottom: 6px;
    }

    .quick-filter-row .btn {
      flex: 1;
      font-size: 0.72rem;
      padding: 5px 6px;
    }

    .btn.active-filter {
      background: var(--error);
      border-color: var(--error);
      color: white;
      box-shadow: 0 0 8px var(--error-glow);
    }

    .all-topics-btn {
      width: 100%;
      text-align: center;
      font-size: 0.75rem;
      padding: 5px 8px;
    }

    .category-list {
      flex: 1;
      overflow-y: auto;
      padding: 4px 10px 14px;
    }

    .cat-item {
      display: flex;
      flex-direction: column;
      padding: 8px 10px;
      border-radius: var(--radius-sm);
      cursor: pointer;
      margin-bottom: 4px;
      border: 1px solid transparent;
      transition: all 0.15s ease;
    }

    .cat-item:hover {
      background: var(--bg-hover);
    }

    .cat-item.active {
      background: rgba(56, 189, 248, 0.12);
      border-color: rgba(56, 189, 248, 0.3);
      border-left: 3px solid var(--accent);
    }

    .cat-item.focused-zen-cat.active {
      border-left-color: #a855f7;
      background: rgba(168, 85, 247, 0.15);
    }

    .cat-item.zen-cat.active {
      border-left-color: #10b981;
      background: rgba(16, 185, 129, 0.12);
    }

    .cat-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-size: 0.78rem;
      margin-bottom: 4px;
    }

    .cat-name {
      font-weight: 500;
      color: var(--text-main);
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      max-width: 200px;
    }

    .cat-count {
      font-family: var(--font-mono);
      font-size: 0.7rem;
      color: var(--text-muted);
    }

    .cat-progress-wrap {
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .cat-progress-bar {
      flex: 1;
      height: 5px;
      background: rgba(255, 255, 255, 0.08);
      border-radius: 999px;
      overflow: hidden;
      display: flex;
    }

    .bar-seg-correct {
      background: var(--success);
      height: 100%;
    }

    .bar-seg-incorrect {
      background: var(--error);
      height: 100%;
    }

    .cat-pct {
      font-size: 0.68rem;
      font-family: var(--font-mono);
      color: var(--text-dim);
      width: 26px;
      text-align: right;
    }

    /* Main Question View */
    main.question-viewport {
      flex: 1;
      overflow-y: auto;
      padding: 24px 32px 48px;
      display: flex;
      flex-direction: column;
      align-items: center;
    }

    .question-card {
      width: 100%;
      max-width: 900px;
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-lg);
      padding: 28px 32px;
      box-shadow: var(--shadow-md);
      position: relative;
    }

    .q-meta-bar {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 20px;
      padding-bottom: 14px;
      border-bottom: 1px solid var(--border-color);
    }

    .q-meta-left {
      display: flex;
      align-items: center;
      gap: 10px;
      flex-wrap: wrap;
    }

    .q-num-badge {
      background: var(--accent);
      color: #0f172a;
      font-weight: 700;
      font-size: 0.75rem;
      padding: 3px 10px;
      border-radius: 999px;
      font-family: var(--font-mono);
    }

    .q-num-badge.focused-zen {
      background: linear-gradient(135deg, #8b5cf6, #3b82f6);
      color: white;
    }

    .q-num-badge.zen {
      background: linear-gradient(135deg, #10b981, #06b6d4);
      color: white;
    }

    .q-track-tag {
      font-size: 0.72rem;
      font-weight: 700;
      padding: 2px 8px;
      border-radius: 999px;
      border: 1px solid transparent;
    }

    .q-track-tag.exam2 {
      background: rgba(14, 165, 233, 0.2);
      color: #38bdf8;
      border-color: rgba(14, 165, 233, 0.4);
    }

    .cat-item.exam2-cat.active {
      background: rgba(14, 165, 233, 0.15);
      border-color: #0ea5e9;
    }

    .q-track-tag.focused-zen {
      background: rgba(139, 92, 246, 0.2);
      color: #c084fc;
      border-color: rgba(139, 92, 246, 0.4);
    }

    .q-track-tag.zen {
      background: rgba(16, 185, 129, 0.2);
      color: #34d399;
      border-color: rgba(16, 185, 129, 0.4);
    }

    .q-category-tag {
      font-size: 0.75rem;
      font-weight: 600;
      color: var(--text-muted);
      background: var(--bg-hover);
      padding: 3px 10px;
      border-radius: var(--radius-sm);
    }

    .q-flag-btn {
      background: transparent;
      border: none;
      color: var(--text-dim);
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 6px;
      font-size: 0.78rem;
      font-weight: 500;
      transition: all 0.15s ease;
    }

    .q-flag-btn:hover {
      color: var(--warning);
    }

    .q-flag-btn.flagged {
      color: var(--warning);
    }

    .q-flag-btn.flagged svg {
      fill: var(--warning);
    }

    /* Question Stem with Highlighting */
    .question-stem {
      font-size: 1.05rem;
      line-height: 1.7;
      color: var(--text-main);
      margin-bottom: 24px;
      user-select: text;
    }

    mark.user-highlight {
      background-color: #fef08a;
      color: #1e293b;
      padding: 1px 3px;
      border-radius: 3px;
      cursor: pointer;
      position: relative;
    }

    mark.user-highlight:hover::after {
      content: 'Click to remove';
      position: absolute;
      bottom: 100%;
      left: 50%;
      transform: translateX(-50%);
      background: #0f172a;
      color: white;
      font-size: 0.65rem;
      padding: 2px 6px;
      border-radius: 4px;
      white-space: nowrap;
      pointer-events: none;
      z-index: 50;
    }

    /* Question Image / Neuroimaging */
    .question-image-box {
      margin: 16px 0 24px;
      text-align: center;
      border: 1px solid var(--border-color);
      border-radius: var(--radius-md);
      padding: 12px;
      background: rgba(0, 0, 0, 0.2);
    }

    .question-image-box img {
      max-width: 100%;
      max-height: 380px;
      border-radius: var(--radius-sm);
      cursor: zoom-in;
      transition: transform 0.2s ease;
    }

    .question-image-box img:hover {
      transform: scale(1.01);
    }

    .image-caption {
      font-size: 0.78rem;
      color: var(--text-muted);
      margin-top: 8px;
    }

    /* Options List */
    .options-list {
      display: flex;
      flex-direction: column;
      gap: 10px;
      margin-bottom: 28px;
    }

    .option-item {
      display: flex;
      align-items: flex-start;
      gap: 14px;
      background: rgba(255, 255, 255, 0.02);
      border: 1.5px solid var(--border-color);
      border-radius: var(--radius-md);
      padding: 14px 18px;
      cursor: pointer;
      transition: all 0.15s ease;
      position: relative;
    }

    .option-item:hover:not(.disabled) {
      background: var(--bg-hover);
      border-color: var(--border-light);
    }

    .option-item.selected:not(.disabled) {
      border-color: var(--accent);
      background: rgba(56, 189, 248, 0.08);
    }

    .option-item.struck {
      opacity: 0.35;
      text-decoration: line-through;
    }

    .option-item.disabled {
      cursor: default;
    }

    /* Correct / Incorrect states */
    .option-item.state-correct {
      border-color: var(--success);
      background: var(--success-glow);
    }

    .option-item.state-incorrect {
      border-color: var(--error);
      background: var(--error-glow);
    }

    .option-letter {
      width: 28px;
      height: 28px;
      border-radius: 50%;
      border: 1.5px solid var(--border-color);
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 700;
      font-size: 0.85rem;
      flex-shrink: 0;
      font-family: var(--font-mono);
      color: var(--text-muted);
      transition: all 0.15s ease;
    }

    .option-item.selected .option-letter {
      background: var(--accent);
      border-color: var(--accent);
      color: #0f172a;
    }

    .option-item.state-correct .option-letter {
      background: var(--success);
      border-color: var(--success);
      color: #ffffff;
    }

    .option-item.state-incorrect .option-letter {
      background: var(--error);
      border-color: var(--error);
      color: #ffffff;
    }

    .option-text {
      flex: 1;
      font-size: 0.96rem;
      line-height: 1.5;
      color: var(--text-main);
      padding-top: 2px;
    }

    .strike-btn {
      background: transparent;
      border: none;
      color: var(--text-dim);
      padding: 4px;
      cursor: pointer;
      border-radius: var(--radius-sm);
      display: flex;
      align-items: center;
      justify-content: center;
      opacity: 0.5;
      transition: all 0.15s ease;
    }

    .strike-btn:hover {
      opacity: 1;
      color: var(--error);
      background: rgba(244, 63, 94, 0.1);
    }

    /* Action Toolbar */
    .action-toolbar {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding-top: 20px;
      border-top: 1px solid var(--border-color);
    }

    /* Explanation Card */
    .explanation-card {
      margin-top: 28px;
      background: rgba(0, 0, 0, 0.25);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-md);
      overflow: hidden;
      display: none;
    }

    .explanation-card.show {
      display: block;
      animation: fadeIn 0.25s ease;
    }

    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(6px); }
      to { opacity: 1; transform: translateY(0); }
    }

    .exp-header {
      padding: 12px 18px;
      font-weight: 700;
      font-size: 0.9rem;
      display: flex;
      align-items: center;
      gap: 8px;
      border-bottom: 1px solid var(--border-color);
    }

    .exp-header.correct {
      background: rgba(16, 185, 129, 0.15);
      color: #34d399;
      border-color: rgba(16, 185, 129, 0.3);
    }

    .exp-header.incorrect {
      background: rgba(244, 63, 94, 0.15);
      color: #fb7185;
      border-color: rgba(244, 63, 94, 0.3);
    }

    .exp-body {
      padding: 20px;
      font-size: 0.94rem;
      line-height: 1.7;
      color: var(--text-main);
      white-space: pre-wrap;
    }

    /* Modals */
    .modal-backdrop {
      position: fixed;
      inset: 0;
      background: rgba(0, 0, 0, 0.75);
      backdrop-filter: blur(4px);
      display: none;
      align-items: center;
      justify-content: center;
      z-index: 100;
      padding: 20px;
    }

    .modal-backdrop.show {
      display: flex;
      animation: fadeIn 0.15s ease;
    }

    .modal-box {
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-lg);
      width: 100%;
      max-width: 650px;
      max-height: 85vh;
      display: flex;
      flex-direction: column;
      box-shadow: var(--shadow-lg);
      overflow: hidden;
    }

    .modal-header {
      padding: 16px 20px;
      border-bottom: 1px solid var(--border-color);
      display: flex;
      align-items: center;
      justify-content: space-between;
    }

    .modal-header h3 {
      font-size: 1.05rem;
      font-weight: 700;
    }

    .modal-content {
      padding: 20px;
      overflow-y: auto;
      flex: 1;
    }

    /* Lightbox Modal */
    .lightbox-img {
      max-width: 90vw;
      max-height: 85vh;
      object-fit: contain;
      border-radius: var(--radius-md);
      box-shadow: var(--shadow-lg);
    }

    /* Gemini Modal */
    .gemini-prompt-box {
      background: rgba(0, 0, 0, 0.3);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-md);
      padding: 14px;
      font-family: var(--font-mono);
      font-size: 0.82rem;
      color: var(--text-muted);
      white-space: pre-wrap;
      max-height: 240px;
      overflow-y: auto;
      margin-bottom: 16px;
    }

    /* Navigator Grid */
    .grid-container {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(44px, 1fr));
      gap: 8px;
      max-height: 480px;
      overflow-y: auto;
      padding: 4px;
    }

    .grid-item {
      aspect-ratio: 1;
      display: flex;
      align-items: center;
      justify-content: center;
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-sm);
      font-family: var(--font-mono);
      font-size: 0.82rem;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.15s ease;
      position: relative;
    }

    .grid-item:hover {
      background: var(--bg-hover);
      border-color: var(--accent);
    }

    .grid-item.current {
      border: 2px solid var(--accent);
      box-shadow: 0 0 8px var(--accent-glow);
    }

    .grid-item.correct {
      background: rgba(16, 185, 129, 0.2);
      border-color: var(--success);
      color: #34d399;
    }

    .grid-item.incorrect {
      background: rgba(244, 63, 94, 0.2);
      border-color: var(--error);
      color: #fb7185;
    }

    .grid-item.flagged::after {
      content: '';
      position: absolute;
      top: 3px;
      right: 3px;
      width: 6px;
      height: 6px;
      background: var(--warning);
      border-radius: 50%;
    }

    /* Toast Notification */
    .toast-notice {
      position: fixed;
      bottom: 24px;
      right: 24px;
      background: #0f172a;
      border: 1px solid var(--border-light);
      box-shadow: var(--shadow-lg);
      border-radius: var(--radius-md);
      padding: 10px 18px;
      display: flex;
      align-items: center;
      gap: 10px;
      font-size: 0.85rem;
      font-weight: 500;
      color: white;
      z-index: 200;
      opacity: 0;
      transform: translateY(12px);
      transition: all 0.25s ease;
      pointer-events: none;
    }

    .toast-notice.show {
      opacity: 1;
      transform: translateY(0);
      pointer-events: auto;
    }

    /* Responsive */
    @media (max-width: 900px) {
      aside.sidebar-left {
        position: absolute;
        top: 0;
        bottom: 0;
        left: 0;
        box-shadow: var(--shadow-lg);
      }
    }
  </style>
</head>
<body data-theme="dark">

  <!-- Header -->
  <header class="exam-header">
    <div class="header-left">
      <div class="logo-badge">
        <svg viewBox="0 0 24 24"><path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-7 3c1.66 0 3 1.34 3 3s-1.34 3-3 3-3-1.34-3-3 1.34-3 3-3zm6 12H6v-1.4c0-2 4-3.1 6-3.1s6 1.1 6 3.1V18z"/></svg>
        <span>USMLE Step 1</span>
      </div>

      <!-- 2-Level Exam & Bank Selector -->
      <div class="exam-selector-tabs">
        <button id="exam1TabBtn" class="exam-tab-btn active-exam1" onclick="selectExam('exam1')">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>
          <span>Exam 1</span>
        </button>
        <button id="exam2TabBtn" class="exam-tab-btn" onclick="selectExam('exam2')">
          <span>🧠</span>
          <span>Exam 2</span>
        </button>
      </div>

      <div class="switcher-separator"></div>

      <div class="track-switcher" id="bankSwitcherContainer">
        <!-- Dynamically rendered based on active Exam -->
      </div>

      <div class="timer-box focused-zen" id="timerDisplay">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
        <span id="timerText">00:00</span>
      </div>
    </div>

    <div class="header-right">
      <!-- Gemini Questions Generator Button -->
      <button class="btn btn-purple" onclick="openGeminiModal()" title="Generate new USMLE practice questions tailored to your incorrect concepts in Gemini">
        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
        <span>Ask Gemini For Similar Qs</span>
      </button>

      <button class="btn" onclick="toggleRandomizeOptions()" id="randomizeToggleBtn" title="Answer choices are dynamically shuffled">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="16 3 21 3 21 8"/><line x1="4" y1="20" x2="21" y2="3"/><polyline points="21 16 21 21 16 21"/><line x1="15" y1="15" x2="21" y2="21"/><line x1="4" y1="4" x2="9" y2="9"/></svg>
        <span id="randomizeBtnText">Shuffled Choices: ON</span>
      </button>

      <button class="btn btn-icon" onclick="toggleTheme()" title="Toggle Dark/Light Mode">
        <svg id="themeIcon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>
      </button>

      <button class="btn btn-accent" onclick="showScoreReport()">
        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 12h-4l-3 9L9 3l-3 9H2"/></svg>
        <span>Performance Report</span>
      </button>
    </div>
  </header>

  <!-- Zen Mode Section Selector Tray (Only shown when a Zen Mode is active) -->
  <div class="zen-section-tray" id="zenSectionTray" style="display: flex;">
    <div class="zen-tray-label">
      <span id="zenTrayIcon">🎯</span>
      <span id="zenTrayLabelText">Study Guide Topics:</span>
    </div>
    <button class="zen-topic-pill active" onclick="selectZenTopic(null)" id="zenTopicPillAll">
      <span>All 16 Topics</span>
      <span class="chip-count">320</span>
    </button>
    <div id="zenTopicPillsContainer" style="display: contents;">
      <!-- Populated dynamically -->
    </div>
  </div>

  <!-- App Body -->
  <div class="app-body">
    <!-- Left Sidebar: Subject Areas Performance Breakdown -->
    <aside class="sidebar-left" id="sidebarLeft">
      <div class="sidebar-header">
        <h2 id="sidebarTitle">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 8v8"/><path d="M8 12h8"/></svg>
          Study Guide Topics (20/each)
        </h2>
        <button class="btn btn-icon" onclick="toggleSidebar()" title="Collapse Sidebar">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="15 18 9 12 15 6"/></svg>
        </button>
      </div>

      <!-- Overall Performance Card -->
      <div class="overall-stats-card">
        <div class="overall-stats-grid">
          <div class="stat-item">
            <div class="val" id="totalScorePct">0%</div>
            <div class="lbl">Score</div>
          </div>
          <div class="stat-item">
            <div class="val" id="totalAnsweredCount">0/320</div>
            <div class="lbl">Done</div>
          </div>
          <div class="stat-item">
            <div class="val" id="totalIncorrectCount" style="color: var(--error);">0</div>
            <div class="lbl">Wrong</div>
          </div>
          <div class="stat-item">
            <div class="val" id="totalFlaggedCount" style="color: var(--warning);">0</div>
            <div class="lbl">Flagged</div>
          </div>
        </div>
      </div>

      <!-- Quick Action Buttons: Review Wrong & Redo Wrong -->
      <div class="sidebar-actions-wrap">
        <div class="quick-filter-row">
          <button class="btn" id="reviewWrongBtn" onclick="filterIncorrect()" title="Filter view to only questions you answered incorrectly">
            <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"/><line x1="15" y1="9" x2="9" y2="15"/><line x1="9" y1="9" x2="15" y2="15"/></svg>
            <span id="reviewWrongBtnText">Review Wrong (0)</span>
          </button>
          <button class="btn" onclick="redoIncorrectQuestions()" title="Reset and re-attempt all questions you answered incorrectly">
            <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="1 4 1 10 7 10"/><path d="M3.51 15a9 9 0 1 0 2.13-9.36L1 10"/></svg>
            <span>Redo Wrong</span>
          </button>
        </div>
        <button class="btn all-topics-btn" onclick="filterCategory(null)" id="allSubjectsFilterBtn">
          All Topics (320)
        </button>
      </div>

      <!-- Subject Area List -->
      <div class="category-list" id="categoryList">
        <!-- Dynamically rendered -->
      </div>
    </aside>

    <!-- Main Question View -->
    <main class="question-viewport" id="mainContent">
      <div class="question-card">
        <!-- Question Meta Header -->
        <div class="q-meta-bar">
          <div class="q-meta-left">
            <button class="btn btn-icon" onclick="toggleSidebar()" title="Toggle Sidebar">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="18" x2="21" y2="18"/></svg>
            </button>
            <span class="q-num-badge focused-zen" id="currentQBadge">Question 1 of 320</span>
            <span class="q-track-tag focused-zen" id="currentQTrackTag">🎯 Focused Zen</span>
            <span class="q-category-tag" id="currentQCategory">Curricular Topic</span>
          </div>
          <div class="q-meta-right">
            <button class="q-flag-btn" onclick="toggleFlagCurrentQuestion()" id="flagBtn" title="Flag this question for review">
              <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 15s1-1 4-1 5 2 8 2 4-1 4-1V3s-1 1-4 1-5-2-8-2-4 1-4 1z"/><line x1="4" y1="22" x2="4" y2="15"/></svg>
              <span id="flagBtnText">Flag</span>
            </button>
          </div>
        </div>

        <!-- Question Stem (Auto-highlighter enabled) -->
        <div class="question-stem" id="questionStemText">
          Loading question stem...
        </div>

        <!-- Question Image Container -->
        <div class="question-image-box" id="questionImageContainer" style="display: none;">
          <img id="questionImageElem" src="" alt="Medical Exam Exhibit" onclick="openLightbox(this.src)" />
          <div class="image-caption" id="questionImageCaption">Click image to enlarge high-resolution view</div>
        </div>

        <!-- Answer Options -->
        <div class="options-list" id="optionsList">
          <!-- Dynamically generated options -->
        </div>

        <!-- Action Toolbar -->
        <div class="action-toolbar">
          <div style="display: flex; gap: 8px;">
            <button class="btn" onclick="openItemGrid()" title="Open question grid navigator">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/></svg>
              <span>Navigator</span>
            </button>
            <button class="btn" onclick="clearHighlights()" title="Clear all yellow text highlights on this question">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 20h9"/><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/></svg>
              <span>Clear Highlights</span>
            </button>
          </div>

          <div style="display: flex; gap: 8px;">
            <button class="btn btn-accent" id="submitChoiceBtn" onclick="submitAnswer()">
              <span>Submit Answer</span>
            </button>
            <button class="btn" onclick="prevQuestion()" id="prevBtn" title="Previous Question (Arrow Left)">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="15 18 9 12 15 6"/></svg>
              <span>Previous</span>
            </button>
            <button class="btn btn-accent" onclick="nextQuestion()" id="nextBtn" title="Next Question (Arrow Right)">
              <span>Next</span>
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 18 15 12 9 6"/></svg>
            </button>
          </div>
        </div>

        <!-- Explanation Card -->
        <div class="explanation-card" id="explanationCard">
          <div class="exp-header" id="expHeader">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2a10 10 0 1 0 10 10A10 10 0 0 0 12 2zm1 15h-2v-6h2zm0-8h-2V7h2z"/></svg>
            <span id="expHeaderText">Explanation</span>
          </div>
          <div class="exp-body" id="explanationText">
            <!-- Full comprehensive rationale -->
          </div>
        </div>
      </div>
    </main>
  </div>

  <!-- Lightbox Modal -->
  <div class="modal-backdrop" id="imageModal" onclick="closeLightbox(event)">
    <div style="position: relative; max-width: 90vw; max-height: 85vh; display: flex; align-items: center; justify-content: center;">
      <button class="btn btn-icon" onclick="closeLightboxDirect()" style="position: absolute; top: 12px; right: 12px; background: rgba(0,0,0,0.85); color: #fff; width: 36px; height: 36px; border-radius: 50%; display: flex; align-items: center; justify-content: center; cursor: pointer; z-index: 10; font-size: 20px; border: 1px solid rgba(255,255,255,0.4);">&times;</button>
      <img id="lightboxImg" class="lightbox-img" src="" alt="Enlarged Medical Exhibit" />
    </div>
  </div>

  <!-- Question Grid Navigator Modal -->
  <div class="modal-backdrop" id="gridModal" onclick="closeItemGrid(event)">
    <div class="modal-box" onclick="event.stopPropagation()">
      <div class="modal-header">
        <h3 id="gridModalTitle">Question Navigator</h3>
        <button class="btn btn-icon" onclick="closeItemGridDirect()">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
        </button>
      </div>
      <div class="modal-content">
        <div class="grid-container" id="gridItemsContainer">
          <!-- Dynamically populated numbers 1..N -->
        </div>
      </div>
    </div>
  </div>

  <!-- Performance Score Report Modal -->
  <div class="modal-backdrop" id="scoreModal" onclick="closeScoreReport(event)">
    <div class="modal-box" onclick="event.stopPropagation()">
      <div class="modal-header">
        <h3 id="reportModalTitle">Performance Report</h3>
        <button class="btn btn-icon" onclick="closeScoreReportDirect()">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
        </button>
      </div>
      <div class="modal-content">
        <div style="display: flex; gap: 16px; margin-bottom: 20px;">
          <div style="flex: 1; background: rgba(0,0,0,0.2); padding: 16px; border-radius: var(--radius-md); text-align: center; border: 1px solid var(--border-color);">
            <div style="font-size: 2.2rem; font-weight: 800; font-family: var(--font-mono); color: var(--accent);" id="reportAccuracyVal">0%</div>
            <div style="font-size: 0.75rem; color: var(--text-dim); text-transform: uppercase;">Overall Accuracy</div>
          </div>
          <div style="flex: 1; background: rgba(0,0,0,0.2); padding: 16px; border-radius: var(--radius-md); text-align: center; border: 1px solid var(--border-color);">
            <div style="font-size: 2.2rem; font-weight: 800; font-family: var(--font-mono); color: var(--success);" id="reportCorrectCount">0</div>
            <div style="font-size: 0.75rem; color: var(--text-dim); text-transform: uppercase;">Correct Answers</div>
          </div>
          <div style="flex: 1; background: rgba(0,0,0,0.2); padding: 16px; border-radius: var(--radius-md); text-align: center; border: 1px solid var(--border-color);">
            <div style="font-size: 2.2rem; font-weight: 800; font-family: var(--font-mono); color: var(--error);" id="reportIncorrectCount">0</div>
            <div style="font-size: 0.75rem; color: var(--text-dim); text-transform: uppercase;">Incorrect Answers</div>
          </div>
        </div>

        <h4 style="font-size: 0.85rem; font-weight: 700; text-transform: uppercase; margin-bottom: 12px; color: var(--text-muted);">
          Performance by Curricular Topic Area
        </h4>
        <div id="reportCategoryBreakdown" style="display: flex; flex-direction: column; gap: 8px;">
          <!-- Dynamically populated topic breakdown -->
        </div>

        <div style="margin-top: 24px; padding-top: 16px; border-top: 1px solid var(--border-color); display: flex; justify-content: space-between; align-items: center;">
          <button class="btn btn-error" onclick="resetCurrentTrack()" title="Reset progress for the current track">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="3 6 5 6 21 6"/><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"/></svg>
            <span>Reset Track Progress</span>
          </button>
          <button class="btn btn-purple" onclick="closeScoreReportDirect(); openGeminiModal();">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
            <span>Generate Gemini Practice Questions</span>
          </button>
        </div>
      </div>
    </div>
  </div>

  <!-- Gemini Prompt Modal -->
  <div class="modal-backdrop" id="geminiModal" onclick="closeGeminiModal(event)">
    <div class="modal-box" onclick="event.stopPropagation()">
      <div class="modal-header">
        <div style="display: flex; align-items: center; gap: 8px;">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#a855f7" stroke-width="2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
          <h3>Ask Gemini For Tailored USMLE Questions</h3>
        </div>
        <button class="btn btn-icon" onclick="closeGeminiModalDirect()">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
        </button>
      </div>
      <div class="modal-content">
        <p style="font-size: 0.88rem; color: var(--text-muted); margin-bottom: 12px; line-height: 1.5;">
          Antigravity has automatically analyzed the specific questions and curricular topics you answered incorrectly and formulated an optimized medical board prompt for Google Gemini to generate high-yield clinical questions targeting your weak areas.
        </p>

        <textarea id="geminiPromptTextarea" class="gemini-prompt-box" rows="10" readonly style="width: 100%; resize: vertical;"></textarea>

        <div style="display: flex; justify-content: flex-end; gap: 10px;">
          <button class="btn" onclick="copyGeminiPrompt()">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
            <span>Copy Prompt</span>
          </button>
          <button class="btn btn-purple" onclick="launchGeminiTab()">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>
            <span>Copy & Launch Gemini</span>
          </button>
        </div>
      </div>
    </div>
  </div>

  <!-- Toast Notice -->
  <div class="toast-notice" id="toastNotice">
    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
    <span id="toastNoticeText">Notification message</span>
  </div>

  <!-- Application Script -->
  <script>
    // RAW DATA
    const rawExamQuestions = """ + json_data_str + """;
    const rawFocusedZenQuestions = """ + focused_zen_json_data_str + """;
    const rawZenQuestions = """ + zen_json_data_str + """;
    const rawInHouseQuestions = """ + inhouse_json_data_str + """;
    const subjectCategories = """ + categories_json_str + """;
    const inHouseCategories = """ + inhouse_categories_json_str + """;
    const rawExam2Questions = """ + exam2_json_data_str + """;
    const exam2Categories = """ + exam2_categories_json_str + """;

    // ACTIVE TRACK: 'focused_zen' (320 Qs from Study Guide), 'exam' (125 Qs), or 'zen' (320 Qs)
    let currentTrack = 'focused_zen';

    // Track states
    let questions = [];
    let userState = {};
    let currentIndex = 0;
    let filteredIndices = [];
    let activeCategoryFilter = null;
    let filterFlaggedOnly = false;
    let filterIncorrectOnly = false;
    let timerSeconds = 0;
    let timerInterval = null;
    let randomizeChoices = true;
    let currentGeneratedPrompt = '';

    function showToast(msg) {
      const toast = document.getElementById('toastNotice');
      document.getElementById('toastNoticeText').textContent = msg;
      toast.classList.add('show');
      setTimeout(() => {
        toast.classList.remove('show');
      }, 3000);
    }

    function shuffleArray(arr) {
      const copy = [...arr];
      for (let i = copy.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [copy[i], copy[j]] = [copy[j], copy[i]];
      }
      return copy;
    }

    // =========================================================================
    // 2-LEVEL EXAM & BANK NAVIGATION
    // Level 1: Exam 1 vs Exam 2
    // Level 2: Specific Banks for that Exam
    // =========================================================================
    let currentExam = 'exam1'; // 'exam1' or 'exam2'

    const EXAM_BANKS = {
      exam1: [
        {
          id: 'exam',
          label: 'Simulation (125 Qs)',
          icon: '<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>',
          badge: 'Official',
          type: 'sim'
        },
        {
          id: 'inhouse',
          label: 'In House (385 Qs)',
          icon: '🏠',
          badge: '12 Modules',
          type: 'inhouse'
        },
        {
          id: 'focused_zen',
          label: 'Focused Zen (320 Qs)',
          icon: '🎯',
          badge: 'Study Guide',
          type: 'focused_zen'
        },
        {
          id: 'zen',
          label: 'General Zen (320 Qs)',
          icon: '🧘',
          badge: '20 / Topic',
          type: 'zen'
        }
      ],
      exam2: [
        {
          id: 'exam2_sim',
          label: 'Simulation (103 Qs)',
          icon: '<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>',
          badge: 'Official PDF',
          type: 'sim'
        },
        {
          id: 'exam2_zen',
          label: 'Section Mastery (9 Topics)',
          icon: '🎯',
          badge: '9 Sections',
          type: 'exam2'
        }
      ]
    };

    function isExam2Track(track) {
      return track === 'exam2' || track === 'exam2_sim' || track === 'exam2_zen';
    }

    function selectExam(examId) {
      currentExam = examId;
      localStorage.setItem('usmle_active_exam', currentExam);

      const e1Tab = document.getElementById('exam1TabBtn');
      const e2Tab = document.getElementById('exam2TabBtn');
      if (e1Tab && e2Tab) {
        if (currentExam === 'exam1') {
          e1Tab.className = 'exam-tab-btn active-exam1';
          e2Tab.className = 'exam-tab-btn';
        } else {
          e1Tab.className = 'exam-tab-btn';
          e2Tab.className = 'exam-tab-btn active-exam2';
        }
      }

      renderBankSwitcher();

      // Pick active bank for this exam
      if (currentExam === 'exam2') {
        const savedBank = localStorage.getItem('usmle_exam2_active_bank') || 'exam2_zen';
        switchTrack(savedBank);
      } else {
        const savedBank = localStorage.getItem('usmle_exam1_active_bank') || 'inhouse';
        switchTrack(savedBank);
      }
    }

    function renderBankSwitcher() {
      const container = document.getElementById('bankSwitcherContainer');
      if (!container) return;
      container.innerHTML = '';

      const banks = EXAM_BANKS[currentExam] || EXAM_BANKS.exam1;
      banks.forEach(b => {
        const btn = document.createElement('button');
        btn.id = 'trackBtn_' + b.id;
        const isActive = (currentTrack === b.id || (b.id === 'exam2_zen' && currentTrack === 'exam2'));
        let activeClass = '';
        if (isActive) {
          if (b.type === 'sim') activeClass = ' active';
          else if (b.type === 'inhouse') activeClass = ' inhouse-active';
          else if (b.type === 'focused_zen') activeClass = ' focused-zen-active';
          else if (b.type === 'zen') activeClass = ' zen-active';
          else if (b.type === 'exam2') activeClass = ' exam2-active';
        }
        btn.className = 'track-btn' + activeClass;
        btn.onclick = () => switchTrack(b.id);
        btn.innerHTML = `
          <span>${b.icon}</span>
          <span>${b.label}</span>
          ${b.badge ? `<span class="zen-pill-badge">${b.badge}</span>` : ''}
        `;
        container.appendChild(btn);
      });
    }

    function switchTrack(newTrack) {
      saveState();

      if (isExam2Track(newTrack)) {
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
      if (e1Tab && e2Tab) {
        if (currentExam === 'exam1') {
          e1Tab.className = 'exam-tab-btn active-exam1';
          e2Tab.className = 'exam-tab-btn';
        } else {
          e1Tab.className = 'exam-tab-btn';
          e2Tab.className = 'exam-tab-btn active-exam2';
        }
      }

      // Re-render level 2 bank pills with new active state
      renderBankSwitcher();

      const zenTray = document.getElementById('zenSectionTray');
      const trayIcon = document.getElementById('zenTrayIcon');
      const trayLabelText = document.getElementById('zenTrayLabelText');
      const trackTag = document.getElementById('currentQTrackTag');
      const sidebarTitle = document.getElementById('sidebarTitle');
      const timerDisplay = document.getElementById('timerDisplay');

      timerDisplay.classList.remove('zen', 'focused-zen', 'inhouse', 'exam2');

      if (currentTrack === 'exam2_sim') {
        zenTray.style.display = 'none';
        trackTag.style.display = 'inline-block';
        trackTag.className = 'q-track-tag exam2';
        trackTag.textContent = '🧠 Exam 2 Sim';
        timerDisplay.classList.add('exam2');
        sidebarTitle.innerHTML = `<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/></svg> Exam 2 Sections (9)`;
      } else if (currentTrack === 'exam2_zen' || currentTrack === 'exam2') {
        zenTray.style.display = 'flex';
        trayIcon.textContent = '🧠';
        trayLabelText.textContent = 'Exam 2 Sections:';
        trackTag.style.display = 'inline-block';
        trackTag.className = 'q-track-tag exam2';
        trackTag.textContent = '🧠 Exam 2 Mastery';
        timerDisplay.classList.add('exam2');
        sidebarTitle.innerHTML = `<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 8v8"/><path d="M8 12h8"/></svg> Exam 2 Sections (9)`;
      } else if (currentTrack === 'inhouse') {
        zenTray.style.display = 'flex';
        trayIcon.textContent = '🏠';
        trayLabelText.textContent = 'In-House Modules:';
        trackTag.style.display = 'inline-block';
        trackTag.className = 'q-track-tag inhouse';
        trackTag.textContent = '🏠 In House';
        timerDisplay.classList.add('inhouse');
        sidebarTitle.innerHTML = `<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg> In-House Course Modules (12)`;
      } else if (currentTrack === 'focused_zen') {
        zenTray.style.display = 'flex';
        trayIcon.textContent = '🎯';
        trayLabelText.textContent = 'Study Guide Topics:';
        trackTag.style.display = 'inline-block';
        trackTag.className = 'q-track-tag focused-zen';
        trackTag.textContent = '🎯 Focused Zen';
        timerDisplay.classList.add('focused-zen');
        sidebarTitle.innerHTML = `<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 8v8"/><path d="M8 12h8"/></svg> Study Guide Topics (20/each)`;
      } else if (currentTrack === 'zen') {
        zenTray.style.display = 'flex';
        trayIcon.textContent = '🧘';
        trayLabelText.textContent = 'General Topics:';
        trackTag.style.display = 'inline-block';
        trackTag.className = 'q-track-tag zen';
        trackTag.textContent = '🧘 Zen Mode';
        timerDisplay.classList.add('zen');
        sidebarTitle.innerHTML = `<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2a10 10 0 1 0 10 10A10 10 0 0 0 12 2zm0 18a8 8 0 1 1 8-8 8 8 0 0 1-8 8z"/></svg> Zen Topics (20/each)`;
      } else {
        // Exam 1 Simulation
        zenTray.style.display = 'none';
        trackTag.style.display = 'none';
        sidebarTitle.innerHTML = `<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/></svg> Subject Areas`;
      }

      activeCategoryFilter = null;
      filterFlaggedOnly = false;
      filterIncorrectOnly = false;

      loadTrackState();
      if (currentTrack === 'exam2_zen' || currentTrack === 'exam2' || currentTrack === 'inhouse' || currentTrack === 'focused_zen' || currentTrack === 'zen') {
        renderZenTray();
      }
      applyFilter();
      renderSidebarCategories();
      updateOverallStats();
      renderCurrentQuestion();

      const toastMsg = currentTrack === 'exam2_sim'
        ? 'Exam 2: Loaded 📝 Simulation Bank (103 Qs)'
        : (currentTrack === 'exam2_zen' || currentTrack === 'exam2')
        ? 'Exam 2: Loaded 🎯 Section Mastery (9 Topics)'
        : currentTrack === 'inhouse'
        ? 'Exam 1: Loaded 🏠 In-House Lectures & Cases (385 Qs)'
        : currentTrack === 'focused_zen'
        ? 'Exam 1: Loaded 🎯 Focused Zen Bank (320 Qs)'
        : currentTrack === 'zen'
        ? 'Exam 1: Loaded 🧘 General Zen Bank (320 Qs)'
        : 'Exam 1: Loaded 📝 Simulation Practice (125 Qs)';
      showToast(toastMsg);
    }

    // Load track-specific questions and state
    function loadTrackState() {
      let storagePrefix = 'usmle_exam1_';
      let rawData = rawExamQuestions;

      if (currentTrack === 'exam2_sim') {
        storagePrefix = 'usmle_exam2_sim_';
        rawData = rawExam2Questions;
      } else if (currentTrack === 'exam2_zen' || currentTrack === 'exam2') {
        storagePrefix = 'usmle_exam2_zen_';
        rawData = rawExam2Questions;
      } else if (currentTrack === 'inhouse') {
        storagePrefix = 'usmle_inhouse_';
        rawData = rawInHouseQuestions;
      } else if (currentTrack === 'focused_zen') {
        storagePrefix = 'usmle_focused_zen_';
        rawData = rawFocusedZenQuestions;
      } else if (currentTrack === 'zen') {
        storagePrefix = 'usmle_zen_';
        rawData = rawZenQuestions;
      }

      questions = rawData.map((q, idx) => ({
        ...q,
        stem: q.stem || q.question,
        image: q.image || q.image_base64 || null,
        index: idx
      }));

      userState = {};
      let saved = localStorage.getItem(storagePrefix + 'state');
      // Graceful fallback for exam2 if switching between zen and sim
      if (!saved && (currentTrack === 'exam2_zen' || currentTrack === 'exam2')) {
        saved = localStorage.getItem('usmle_exam2_state');
      }

      let restoredState = null;
      if (saved) {
        try { restoredState = JSON.parse(saved); } catch (e) {}
      }

      questions.forEach((q) => {
        if (restoredState && restoredState[q.id]) {
          const s = restoredState[q.id];
          const hasOptionMismatch = !s.shuffledOptions || s.shuffledOptions.length !== q.options.length;
          let chosenIdx = hasOptionMismatch ? null : s.selectedChoiceIndex;
          let restoredIsCorrect = hasOptionMismatch ? null : s.isCorrect;
          if (chosenIdx !== null && s.shuffledOptions && s.shuffledOptions[chosenIdx]) {
            restoredIsCorrect = (s.shuffledOptions[chosenIdx].is_correct === true);
          }
          userState[q.id] = {
            selectedChoiceIndex: chosenIdx,
            isCorrect: restoredIsCorrect,
            flagged: s.flagged || false,
            struckChoices: new Set(hasOptionMismatch ? [] : (s.struckChoices || [])),
            shuffledOptions: hasOptionMismatch ? (randomizeChoices ? shuffleArray(q.options) : [...q.options]) : s.shuffledOptions,
            stemHtml: s.stemHtml || null
          };
        } else {
          userState[q.id] = {
            selectedChoiceIndex: null,
            isCorrect: null,
            flagged: false,
            struckChoices: new Set(),
            shuffledOptions: randomizeChoices ? shuffleArray(q.options) : [...q.options],
            stemHtml: null
          };
        }
      });

      const savedIdx = localStorage.getItem(storagePrefix + 'current_index') || (isExam2Track(currentTrack) ? localStorage.getItem('usmle_exam2_current_index') : null);
      if (savedIdx !== null && !isNaN(parseInt(savedIdx, 10))) {
        const parsedIdx = parseInt(savedIdx, 10);
        currentIndex = (parsedIdx >= 0 && parsedIdx < questions.length) ? parsedIdx : 0;
      } else {
        currentIndex = 0;
      }

      const savedTimer = localStorage.getItem(storagePrefix + 'timer_seconds');
      if (savedTimer !== null && !isNaN(parseInt(savedTimer, 10))) {
        timerSeconds = parseInt(savedTimer, 10);
      } else {
        timerSeconds = 0;
      }
    }

    function saveState() {
      let storagePrefix = 'usmle_exam1_';
      if (currentTrack === 'exam2_sim') storagePrefix = 'usmle_exam2_sim_';
      else if (currentTrack === 'exam2_zen' || currentTrack === 'exam2') storagePrefix = 'usmle_exam2_zen_';
      else if (currentTrack === 'inhouse') storagePrefix = 'usmle_inhouse_';
      else if (currentTrack === 'focused_zen') storagePrefix = 'usmle_focused_zen_';
      else if (currentTrack === 'zen') storagePrefix = 'usmle_zen_';

      const serializable = {};
      for (const qId in userState) {
        const s = userState[qId];
        serializable[qId] = {
          selectedChoiceIndex: s.selectedChoiceIndex,
          isCorrect: s.isCorrect,
          flagged: s.flagged,
          struckChoices: Array.from(s.struckChoices),
          shuffledOptions: s.shuffledOptions,
          stemHtml: s.stemHtml
        };
      }

      localStorage.setItem(storagePrefix + 'state', JSON.stringify(serializable));
      localStorage.setItem(storagePrefix + 'current_index', currentIndex);
      localStorage.setItem(storagePrefix + 'timer_seconds', timerSeconds);
    }

    // Timer
    function startTimer() {
      if (timerInterval) clearInterval(timerInterval);
      timerInterval = setInterval(() => {
        timerSeconds++;
        const mins = Math.floor(timerSeconds / 60);
        const secs = timerSeconds % 60;
        const text = `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
        if (isExam2Track(currentTrack)) {
          document.getElementById('timerText').textContent = `🧠 ${text}`;
        } else if (currentTrack === 'focused_zen') {
          document.getElementById('timerText').textContent = `🎯 ${text}`;
        } else if (currentTrack === 'zen') {
          document.getElementById('timerText').textContent = `🧘 ${text}`;
        } else if (currentTrack === 'inhouse') {
          document.getElementById('timerText').textContent = `🏠 ${text}`;
        } else {
          document.getElementById('timerText').textContent = text;
        }

        if (timerSeconds % 10 === 0) saveState();
      }, 1000);
    }

    // Render Zen Section Tray Pills
    function renderZenTray() {
      const container = document.getElementById('zenTopicPillsContainer');
      const allPill = document.getElementById('zenTopicPillAll');
      if (!allPill || !container) return;
      allPill.className = 'zen-topic-pill ' + (activeCategoryFilter === null ? 'active' : '');
      const catsToUse = isExam2Track(currentTrack) ? exam2Categories : (currentTrack === 'inhouse' ? inHouseCategories : subjectCategories);
      allPill.innerHTML = `<span>All ${catsToUse.length} Topics</span><span class="chip-count">${questions.length}</span>`;

      let html = '';
      catsToUse.forEach((cat) => {
        const isActive = activeCategoryFilter === cat;
        const catQuestions = questions.filter(q => q.category === cat);
        const answered = catQuestions.filter(q => userState[q.id] && userState[q.id].isCorrect !== null).length;
        html += `
          <button class="zen-topic-pill ${isActive ? 'active' : ''}" onclick="selectZenTopic('${cat.replace(/'/g, "\\'")}')">
            <span>${cat}</span>
            <span class="chip-count">${answered}/${catQuestions.length}</span>
          </button>
        `;
      });
      container.innerHTML = html;
    }

    function selectZenTopic(cat) {
      activeCategoryFilter = cat;
      filterIncorrectOnly = false;
      filterFlaggedOnly = false;
      applyFilter();
      renderZenTray();
      renderSidebarCategories();
      updateOverallStats();
      currentIndex = filteredIndices.length > 0 ? filteredIndices[0] : 0;
      renderCurrentQuestion();
      saveState();
      const count = filteredIndices.length;
      showToast(cat ? `Filtered to: ${cat} (${count} Qs)` : `Showing all ${questions.length} Questions`);
    }

        // Auto-Highlighting
    function setupAutoHighlighting() {
      const stemContainer = document.getElementById('questionStemText');
      stemContainer.addEventListener('mouseup', handleAutoHighlight);
    }

    function handleAutoHighlight() {
      const selection = window.getSelection();
      if (!selection || selection.isCollapsed || !selection.rangeCount) return;

      const range = selection.getRangeAt(0);
      const selectedText = selection.toString().trim();
      if (selectedText.length < 2) return;

      const stemElem = document.getElementById('questionStemText');
      if (!stemElem.contains(range.commonAncestorContainer)) return;

      try {
        const mark = document.createElement('mark');
        mark.className = 'user-highlight';
        mark.textContent = range.toString();
        mark.onclick = function(e) {
          e.stopPropagation();
          removeHighlightElement(mark);
        };

        range.deleteContents();
        range.insertNode(mark);
        selection.removeAllRanges();

        const q = questions[currentIndex];
        userState[q.id].stemHtml = stemElem.innerHTML;
        saveState();
        showToast('Text highlighted');
      } catch (err) {
        console.error('Highlight failed:', err);
      }
    }

    function removeHighlightElement(markElem) {
      const parent = markElem.parentNode;
      while (markElem.firstChild) {
        parent.insertBefore(markElem.firstChild, markElem);
      }
      parent.removeChild(markElem);
      parent.normalize();

      const q = questions[currentIndex];
      userState[q.id].stemHtml = document.getElementById('questionStemText').innerHTML;
      saveState();
      showToast('Highlight removed');
    }

    function clearHighlights() {
      const q = questions[currentIndex];
      userState[q.id].stemHtml = null;
      document.getElementById('questionStemText').textContent = q.stem;
      saveState();
      showToast('All highlights cleared on this question');
    }

    // Filters
    function applyFilter() {
      filteredIndices = [];
      questions.forEach((q, idx) => {
        const state = userState[q.id];
        if (activeCategoryFilter && q.category !== activeCategoryFilter) return;
        if (filterFlaggedOnly && !state.flagged) return;
        if (filterIncorrectOnly && state.isCorrect !== false) return;
        filteredIndices.push(idx);
      });

      if (filteredIndices.length === 0) {
        filteredIndices = [currentIndex];
      }

      const revBtn = document.getElementById('reviewWrongBtn');
      if (revBtn) {
        if (filterIncorrectOnly) revBtn.classList.add('active-filter');
        else revBtn.classList.remove('active-filter');
      }

      const allBtn = document.getElementById('allSubjectsFilterBtn');
      if (allBtn) {
        if (!activeCategoryFilter && !filterIncorrectOnly && !filterFlaggedOnly) {
          allBtn.classList.add('btn-accent');
        } else {
          allBtn.classList.remove('btn-accent');
        }
      }
    }

    function filterCategory(cat) {
      activeCategoryFilter = cat;
      filterIncorrectOnly = false;
      filterFlaggedOnly = false;
      applyFilter();
      if (currentTrack === 'exam2' || currentTrack === 'inhouse' || currentTrack === 'focused_zen' || currentTrack === 'zen') renderZenTray();
      renderSidebarCategories();
      updateOverallStats();
      if (filteredIndices.length > 0 && !filteredIndices.includes(currentIndex)) {
        currentIndex = filteredIndices[0];
      }
      renderCurrentQuestion();
      saveState();
      showToast(cat ? `Filtered: ${cat}` : `Showing all ${questions.length} questions`);
    }

    function filterIncorrect() {
      const wrongCount = questions.filter(q => userState[q.id] && userState[q.id].isCorrect === false).length;
      if (wrongCount === 0) {
        showToast('Great job! You have 0 incorrect questions to review.');
        return;
      }
      filterIncorrectOnly = !filterIncorrectOnly;
      applyFilter();
      renderSidebarCategories();
      updateOverallStats();
      if (filteredIndices.length > 0 && !filteredIndices.includes(currentIndex)) {
        currentIndex = filteredIndices[0];
      }
      renderCurrentQuestion();
      saveState();
      showToast(filterIncorrectOnly ? `Reviewing ${wrongCount} incorrect questions` : 'Exited Review Wrong filter');
    }

    function redoIncorrectQuestions() {
      const wrongIndices = [];
      questions.forEach((q, idx) => {
        if (userState[q.id] && userState[q.id].isCorrect === false) {
          wrongIndices.push(idx);
        }
      });

      if (wrongIndices.length === 0) {
        showToast('You currently have no incorrect questions to redo!');
        return;
      }

      if (confirm(`Do you want to reset and re-attempt all ${wrongIndices.length} incorrect questions?`)) {
        wrongIndices.forEach((idx) => {
          const q = questions[idx];
          userState[q.id].selectedChoiceIndex = null;
          userState[q.id].isCorrect = null;
          userState[q.id].struckChoices = new Set();
          if (randomizeChoices) {
            userState[q.id].shuffledOptions = shuffleArray(q.options);
          }
        });

        filterIncorrectOnly = true;
        applyFilter();
        currentIndex = wrongIndices[0];
        renderCurrentQuestion();
        renderSidebarCategories();
        updateOverallStats();
        if (currentTrack === 'exam2' || currentTrack === 'inhouse' || currentTrack === 'focused_zen' || currentTrack === 'zen') renderZenTray();
        saveState();
        showToast(`Reset ${wrongIndices.length} incorrect questions for re-attempt!`);
      }
    }

    // Render Current Question
    function renderCurrentQuestion() {
      if (currentIndex < 0 || currentIndex >= questions.length) {
        currentIndex = 0;
      }

      const q = questions[currentIndex];
      const state = userState[q.id];
      const totalInTrack = questions.length;

      // Update question badge
      let badgeText = `Question ${currentIndex + 1} of ${totalInTrack}`;
      if (activeCategoryFilter) {
        const idxInFilter = filteredIndices.indexOf(currentIndex) + 1;
        badgeText = `Question ${idxInFilter} of ${filteredIndices.length} (${activeCategoryFilter})`;
      }
      const badgeElem = document.getElementById('currentQBadge');
      badgeElem.textContent = badgeText;
      badgeElem.className = 'q-num-badge ' + (currentTrack === 'inhouse' ? 'inhouse' : currentTrack === 'focused_zen' ? 'focused-zen' : currentTrack === 'zen' ? 'zen' : '');

      document.getElementById('currentQCategory').textContent = q.category;

      // Question Stem
      const stemElem = document.getElementById('questionStemText');
      if (state.stemHtml) {
        stemElem.innerHTML = state.stemHtml;
        Array.from(stemElem.querySelectorAll('mark.user-highlight')).forEach(m => {
          m.onclick = function(e) {
            e.stopPropagation();
            removeHighlightElement(m);
          };
        });
      } else {
        stemElem.textContent = q.stem;
      }

      // Image / Figure
      const imgContainer = document.getElementById('questionImageContainer');
      const imgElem = document.getElementById('questionImageElem');
      const imgSrc = q.image || q.image_base64;
      if (imgSrc) {
        imgElem.src = imgSrc;
        imgContainer.style.display = 'block';
      } else {
        imgContainer.style.display = 'none';
        imgElem.src = '';
      }

      // Flag Button
      const flagBtn = document.getElementById('flagBtn');
      const flagBtnText = document.getElementById('flagBtnText');
      flagBtnText.textContent = state.flagged ? 'Flagged' : 'Flag';
      if (state.flagged) {
        flagBtn.classList.add('flagged');
      } else {
        flagBtn.classList.remove('flagged');
      }

      // Render Options
      const optionsList = document.getElementById('optionsList');
      optionsList.innerHTML = '';
      const letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'];
      const isAnswered = state.isCorrect !== null;

      state.shuffledOptions.forEach((opt, optIdx) => {
        const item = document.createElement('div');
        let classes = ['option-item'];
        if (state.struckChoices.has(optIdx)) classes.push('struck');
        if (state.selectedChoiceIndex === optIdx) classes.push('selected');

        if (isAnswered) {
          classes.push('disabled');
          if (opt.is_correct) {
            classes.push('state-correct');
          } else if (state.selectedChoiceIndex === optIdx && !opt.is_correct) {
            classes.push('state-incorrect');
          }
        }

        item.className = classes.join(' ');

        const letterBox = document.createElement('div');
        letterBox.className = 'option-letter';
        letterBox.textContent = letters[optIdx] || (optIdx + 1);

        const textBox = document.createElement('div');
        textBox.className = 'option-text';
        textBox.textContent = opt.text;

        const strikeBtn = document.createElement('button');
        strikeBtn.className = 'strike-btn';
        strikeBtn.title = 'Strikethrough this choice';
        strikeBtn.innerHTML = `<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="4" y1="12" x2="20" y2="12"/></svg>`;
        strikeBtn.onclick = (e) => {
          e.stopPropagation();
          toggleStrike(optIdx);
        };

        item.appendChild(letterBox);
        item.appendChild(textBox);
        if (!isAnswered) {
          item.appendChild(strikeBtn);
        }

        item.onclick = () => {
          if (!isAnswered) {
            selectChoice(optIdx);
          }
        };

        optionsList.appendChild(item);
      });

      // Submit Button visibility
      const submitBtn = document.getElementById('submitChoiceBtn');
      if (isAnswered || currentTrack === 'exam2_zen' || currentTrack === 'exam2' || currentTrack === 'inhouse' || currentTrack === 'focused_zen' || currentTrack === 'zen') {
        submitBtn.style.display = 'none';
      } else {
        submitBtn.style.display = 'inline-flex';
        submitBtn.disabled = state.selectedChoiceIndex === null;
      }

      // Explanation Card
      const expCard = document.getElementById('explanationCard');
      if (isAnswered) {
        const expHeader = document.getElementById('expHeader');
        const expHeaderText = document.getElementById('expHeaderText');
        const correctChoice = state.shuffledOptions.find(o => o.is_correct);
        const correctOptLetter = letters[state.shuffledOptions.findIndex(o => o.is_correct)];

        if (state.isCorrect) {
          expHeader.className = 'exp-header correct';
          expHeaderText.textContent = `Correct! (${correctOptLetter}: ${correctChoice.text})`;
        } else {
          expHeader.className = 'exp-header incorrect';
          expHeaderText.textContent = `Incorrect. Correct Answer: ${correctOptLetter}: ${correctChoice.text}`;
        }

        let expText = (q.explanation || '').trim();
        if (expText.toLowerCase().indexOf('correct answer:') === 0) {
          const nlIndex = expText.indexOf(String.fromCharCode(10));
          if (nlIndex !== -1) {
            expText = expText.substring(nlIndex).trim();
          }
        }
        document.getElementById('explanationText').textContent = expText;
        expCard.classList.add('show');
      } else {
        expCard.classList.remove('show');
      }

      // Navigation Buttons
      const currPosInFilter = filteredIndices.indexOf(currentIndex);
      document.getElementById('prevBtn').disabled = currPosInFilter <= 0;
      document.getElementById('nextBtn').disabled = currPosInFilter >= filteredIndices.length - 1;
    }

    function selectChoice(optIdx) {
      const q = questions[currentIndex];
      const state = userState[q.id];
      state.selectedChoiceIndex = optIdx;

      // In In-House and Zen modes, instant submit and feedback on click!
      if (currentTrack === 'exam2_zen' || currentTrack === 'exam2' || currentTrack === 'inhouse' || currentTrack === 'focused_zen' || currentTrack === 'zen') {
        submitAnswer();
      } else {
        renderCurrentQuestion();
        saveState();
      }
    }

    function toggleStrike(optIdx) {
      const q = questions[currentIndex];
      const state = userState[q.id];
      if (state.struckChoices.has(optIdx)) {
        state.struckChoices.delete(optIdx);
      } else {
        state.struckChoices.add(optIdx);
      }
      renderCurrentQuestion();
    }

    function submitAnswer() {
      const q = questions[currentIndex];
      const state = userState[q.id];
      if (state.selectedChoiceIndex === null) {
        showToast('Please select an answer choice first!');
        return;
      }

      const selectedOption = state.shuffledOptions[state.selectedChoiceIndex];
      state.isCorrect = (selectedOption && selectedOption.is_correct === true);

      renderCurrentQuestion();
      renderSidebarCategories();
      updateOverallStats();
      if (currentTrack === 'exam2_zen' || currentTrack === 'exam2' || currentTrack === 'inhouse' || currentTrack === 'focused_zen' || currentTrack === 'zen') {
        renderZenTray();
      }
      saveState();
    }

    function prevQuestion() {
      const currPosInFilter = filteredIndices.indexOf(currentIndex);
      if (currPosInFilter > 0) {
        currentIndex = filteredIndices[currPosInFilter - 1];
        renderCurrentQuestion();
        document.getElementById('mainContent').scrollTop = 0;
      }
    }

    function nextQuestion() {
      const currPosInFilter = filteredIndices.indexOf(currentIndex);
      if (currPosInFilter < filteredIndices.length - 1) {
        currentIndex = filteredIndices[currPosInFilter + 1];
        renderCurrentQuestion();
        document.getElementById('mainContent').scrollTop = 0;
      }
    }

    function toggleFlagCurrentQuestion() {
      const q = questions[currentIndex];
      const state = userState[q.id];
      state.flagged = !state.flagged;
      renderCurrentQuestion();
      updateOverallStats();
      saveState();
      showToast(state.flagged ? 'Question flagged for review' : 'Flag removed');
    }

    function toggleRandomizeOptions() {
      randomizeChoices = !randomizeChoices;
      const btn = document.getElementById('randomizeBtnText');
      btn.textContent = `Shuffled Choices: ${randomizeChoices ? 'ON' : 'OFF'}`;

      questions.forEach((q) => {
        const state = userState[q.id];
        if (state.selectedChoiceIndex === null) {
          state.shuffledOptions = randomizeChoices ? shuffleArray(q.options) : [...q.options];
          state.struckChoices = new Set();
        }
      });

      renderCurrentQuestion();
      saveState();
      showToast(randomizeChoices ? 'Answer choices will be shuffled' : 'Answer choices shown in original order');
    }

    // Sidebar & Overall Stats
    function updateOverallStats() {
      let totalAnswered = 0;
      let totalCorrect = 0;
      let totalIncorrect = 0;
      let totalFlagged = 0;

      questions.forEach((q) => {
        const state = userState[q.id];
        if (state.isCorrect !== null) {
          totalAnswered++;
          if (state.isCorrect === true) totalCorrect++;
          else totalIncorrect++;
        }
        if (state.flagged) totalFlagged++;
      });

      const pct = totalAnswered > 0 ? Math.round((totalCorrect / totalAnswered) * 100) : 0;
      document.getElementById('totalScorePct').textContent = `${pct}%`;
      document.getElementById('totalAnsweredCount').textContent = `${totalAnswered}/${questions.length}`;
      document.getElementById('totalIncorrectCount').textContent = totalIncorrect.toString();
      document.getElementById('totalFlaggedCount').textContent = totalFlagged.toString();

      document.getElementById('reviewWrongBtnText').textContent = `Review Wrong (${totalIncorrect})`;
      document.getElementById('allSubjectsFilterBtn').textContent = `All Topics (${questions.length})`;
    }

    function renderSidebarCategories() {
      const container = document.getElementById('categoryList');
      container.innerHTML = '';

      const catsToUse = isExam2Track(currentTrack) ? exam2Categories : (currentTrack === 'inhouse' ? inHouseCategories : subjectCategories);
      catsToUse.forEach((cat) => {
        const catQuestions = questions.filter(q => q.category === cat);
        const total = catQuestions.length;
        if (total === 0) return;

        let correct = 0;
        let incorrect = 0;
        catQuestions.forEach(q => {
          const st = userState[q.id];
          if (st.isCorrect === true) correct++;
          else if (st.isCorrect === false) incorrect++;
        });

        const answered = correct + incorrect;
        const pct = answered > 0 ? Math.round((correct / answered) * 100) : 0;
        const correctWidth = (correct / total) * 100;
        const incorrectWidth = (incorrect / total) * 100;

        const item = document.createElement('div');
        const isActive = activeCategoryFilter === cat;
        const catClass = isExam2Track(currentTrack) ? 'exam2-cat' : currentTrack === 'inhouse' ? 'inhouse-cat' : currentTrack === 'focused_zen' ? 'focused-zen-cat' : currentTrack === 'zen' ? 'zen-cat' : '';
        item.className = `cat-item ${isActive ? 'active' : ''} ${catClass}`;
        item.onclick = () => filterCategory(isActive ? null : cat);

        item.innerHTML = `
          <div class="cat-header">
            <span class="cat-name" title="${cat}">${cat}</span>
            <span class="cat-count">${answered}/${total}</span>
          </div>
          <div class="cat-progress-wrap">
            <div class="cat-progress-bar">
              <div class="bar-seg-correct" style="width: ${correctWidth}%;"></div>
              <div class="bar-seg-incorrect" style="width: ${incorrectWidth}%;"></div>
            </div>
            <span class="cat-pct">${pct}%</span>
          </div>
        `;

        container.appendChild(item);
      });
    }

    function toggleSidebar() {
      const sb = document.getElementById('sidebarLeft');
      sb.classList.toggle('collapsed');
    }

    function toggleTheme() {
      const body = document.body;
      const current = body.getAttribute('data-theme');
      const next = current === 'dark' ? 'light' : 'dark';
      body.setAttribute('data-theme', next);
      localStorage.setItem('usmle_exam_theme', next);
    }

    // Lightbox
    function openLightbox(src) {
      document.getElementById('lightboxImg').src = src;
      document.getElementById('imageModal').classList.add('show');
    }

    function closeLightbox(e) {
      if (e.target.id === 'imageModal') {
        document.getElementById('imageModal').classList.remove('show');
      }
    }

    function closeLightboxDirect() {
      document.getElementById('imageModal').classList.remove('show');
    }

    // Item Grid Navigator
    function openItemGrid() {
      const container = document.getElementById('gridItemsContainer');
      container.innerHTML = '';
      const trackName = currentTrack === 'exam2'
        ? '🧠 Exam 2 (103 Qs)'
        : currentTrack === 'inhouse'
        ? '🏠 In-House Course'
        : currentTrack === 'focused_zen'
        ? '🎯 Focused Zen'
        : currentTrack === 'zen'
        ? '🧘 General Zen'
        : 'Exam 1';
      document.getElementById('gridModalTitle').textContent = `${trackName} Question Navigator (${filteredIndices.length} questions)`;

      filteredIndices.forEach((qIdx) => {
        const q = questions[qIdx];
        const state = userState[q.id];

        const item = document.createElement('div');
        let classes = ['grid-item'];
        if (qIdx === currentIndex) classes.push('current');
        if (state.isCorrect === true) classes.push('correct');
        else if (state.isCorrect === false) classes.push('incorrect');
        if (state.flagged) classes.push('flagged');

        item.className = classes.join(' ');
        item.textContent = qIdx + 1;
        item.title = `Question ${qIdx + 1}: ${q.category}`;

        item.onclick = () => {
          currentIndex = qIdx;
          renderCurrentQuestion();
          closeItemGridDirect();
        };

        container.appendChild(item);
      });

      document.getElementById('gridModal').classList.add('show');
    }

    function closeItemGrid(e) {
      if (e.target.id === 'gridModal') closeItemGridDirect();
    }

    function closeItemGridDirect() {
      document.getElementById('gridModal').classList.remove('show');
    }

    // Performance Score Report
    function showScoreReport() {
      let totalAnswered = 0;
      let totalCorrect = 0;
      let totalIncorrect = 0;

      questions.forEach((q) => {
        const state = userState[q.id];
        if (state.isCorrect !== null) {
          totalAnswered++;
          if (state.isCorrect === true) totalCorrect++;
          else totalIncorrect++;
        }
      });

      const acc = totalAnswered > 0 ? Math.round((totalCorrect / totalAnswered) * 100) : 0;
      document.getElementById('reportAccuracyVal').textContent = `${acc}%`;
      document.getElementById('reportCorrectCount').textContent = totalCorrect.toString();
      document.getElementById('reportIncorrectCount').textContent = totalIncorrect.toString();

      const reportTitle = isExam2Track(currentTrack)
        ? (currentTrack === 'exam2_sim' ? '🧠 Exam 2 Simulation (103 Qs) Score Report' : '🧠 Exam 2 Section Mastery (103 Qs) Score Report')
        : currentTrack === 'focused_zen'
        ? '🎯 Focused Zen Mode (320 Qs) Performance Report'
        : currentTrack === 'zen'
        ? '🧘 General Zen Mode (320 Qs) Performance Report'
        : 'Exam 1 (125 Qs) Performance Report';
      document.getElementById('reportModalTitle').textContent = reportTitle;

      const breakdown = document.getElementById('reportCategoryBreakdown');
      breakdown.innerHTML = '';

      subjectCategories.forEach((cat) => {
        const catQuestions = questions.filter(q => q.category === cat);
        const total = catQuestions.length;
        if (total === 0) return;

        let cor = 0;
        let incor = 0;
        catQuestions.forEach(q => {
          const st = userState[q.id];
          if (st.isCorrect === true) cor++;
          else if (st.isCorrect === false) incor++;
        });

        const answered = cor + incor;
        const pct = answered > 0 ? Math.round((cor / answered) * 100) : 0;

        const row = document.createElement('div');
        row.style.cssText = 'background: rgba(0,0,0,0.15); padding: 8px 12px; border-radius: var(--radius-sm); border: 1px solid var(--border-color); display: flex; align-items: center; justify-content: space-between; font-size: 0.8rem;';
        row.innerHTML = `
          <span style="font-weight: 500; color: var(--text-main);">${cat}</span>
          <div style="display: flex; gap: 12px; align-items: center; font-family: var(--font-mono);">
            <span style="color: var(--text-dim);">${answered}/${total} answered</span>
            <span style="color: ${pct >= 70 ? 'var(--success)' : pct >= 50 ? 'var(--warning)' : 'var(--error)'}; font-weight: 700;">${pct}%</span>
          </div>
        `;
        breakdown.appendChild(row);
      });

      document.getElementById('scoreModal').classList.add('show');
    }

    function closeScoreReport(e) {
      if (e.target.id === 'scoreModal') closeScoreReportDirect();
    }

    function closeScoreReportDirect() {
      document.getElementById('scoreModal').classList.remove('show');
    }

    // Gemini Modal
    function openGeminiModal() {
      const q = questions[currentIndex];
      const state = userState[q.id];
      const wrongList = questions
        .filter(item => userState[item.id] && userState[item.id].isCorrect === false)
        .map(item => `• Category: ${item.category} | Stem: "${item.stem.slice(0, 100)}..."`)
        .slice(0, 5);

      let conceptsStr = '';
      if (wrongList.length > 0) {
        conceptsStr = `Here are specific topics/questions I missed on my exam:\\n${wrongList.join('\\n')}\\n\\n`;
      } else {
        conceptsStr = `Current focus category: ${q.category}.\\nQuestion Stem Concept: "${q.stem.slice(0, 120)}..."\\n\\n`;
      }

      currentGeneratedPrompt = `You are an expert medical educator specializing in USMLE Step 1 preparation.

${conceptsStr}Please generate 3 brand-new, high-yield USMLE Step 1 style clinical vignette multiple choice questions targeting these exact concepts.

For each question:
1. Provide a realistic clinical vignette with patient age, history, physical exam, and pertinent laboratory/imaging findings.
2. Provide 5 distinct answer choices (A, B, C, D, E).
3. Include the correct answer with a thorough educational explanation.
4. Detail why each incorrect distractor is wrong.
5. Provide a memorable high-yield board tip / memory aid.`;

      document.getElementById('geminiPromptTextarea').value = currentGeneratedPrompt;
      document.getElementById('geminiModal').classList.add('show');
    }

    function closeGeminiModal(e) {
      if (e.target.id === 'geminiModal') closeGeminiModalDirect();
    }

    function closeGeminiModalDirect() {
      document.getElementById('geminiModal').classList.remove('show');
    }

    function copyGeminiPrompt() {
      const textarea = document.getElementById('geminiPromptTextarea');
      textarea.select();
      navigator.clipboard.writeText(textarea.value).then(() => {
        showToast('Prompt copied to clipboard!');
      }).catch(() => {
        document.execCommand('copy');
        showToast('Prompt copied to clipboard!');
      });
    }

    function launchGeminiTab() {
      copyGeminiPrompt();
      setTimeout(() => {
        window.open('https://gemini.google.com/app', '_blank');
      }, 200);
    }

    function resetCurrentTrack() {
      let trackName = 'Exam 1 (125 questions)';
      let storagePrefix = 'usmle_exam1_';
      if (currentTrack === 'exam2_sim') {
        trackName = '🧠 Exam 2 Simulation (103 questions)';
        storagePrefix = 'usmle_exam2_sim_';
      } else if (currentTrack === 'exam2_zen' || currentTrack === 'exam2') {
        trackName = '🧠 Exam 2 Section Mastery (103 questions)';
        storagePrefix = 'usmle_exam2_zen_';
      } else if (currentTrack === 'inhouse') {
        trackName = '🏠 In-House Course Track (385 questions)';
        storagePrefix = 'usmle_inhouse_';
      } else if (currentTrack === 'focused_zen') {
        trackName = '🎯 Focused Zen Mode (320 questions)';
        storagePrefix = 'usmle_focused_zen_';
      } else if (currentTrack === 'zen') {
        trackName = '🧘 General Zen Mode (320 questions)';
        storagePrefix = 'usmle_zen_';
      }

      if (confirm(`Are you sure you want to reset all answers, highlights, and score history for ${trackName}? This cannot be undone.`)) {
        localStorage.removeItem(storagePrefix + 'state');
        localStorage.removeItem(storagePrefix + 'current_index');
        localStorage.removeItem(storagePrefix + 'timer_seconds');

        loadTrackState();
        if (isExam2Track(currentTrack) || currentTrack === 'inhouse' || currentTrack === 'focused_zen' || currentTrack === 'zen') renderZenTray();
        applyFilter();
        renderSidebarCategories();
        updateOverallStats();
        renderCurrentQuestion();
        showToast(`Progress reset for ${trackName}`);
      }
    }

    // Keyboard Shortcuts
    window.addEventListener('keydown', (e) => {
      if (document.getElementById('geminiModal').classList.contains('show')) return;
      if (document.getElementById('gridModal').classList.contains('show')) return;
      if (document.getElementById('scoreModal').classList.contains('show')) return;
      if (document.getElementById('imageModal').classList.contains('show')) return;

      if (e.key === 'ArrowRight') {
        nextQuestion();
      } else if (e.key === 'ArrowLeft') {
        prevQuestion();
      } else if (e.key === 'f' || e.key === 'F') {
        toggleFlagCurrentQuestion();
      } else if (['1', '2', '3', '4', '5'].includes(e.key)) {
        const optIdx = parseInt(e.key, 10) - 1;
        const q = questions[currentIndex];
        const state = userState[q.id];
        if (optIdx < state.shuffledOptions.length && state.isCorrect === null) {
          selectChoice(optIdx);
        }
      }
    });

    // Bootstrapping
    window.addEventListener('DOMContentLoaded', () => {
      const savedTheme = localStorage.getItem('usmle_exam_theme');
      if (savedTheme) {
        document.body.setAttribute('data-theme', savedTheme);
      }

      setupAutoHighlighting();
      startTimer();

      // Restore active exam & track
      const savedExam = localStorage.getItem('usmle_active_exam') || 'exam1';
      let targetTrack = localStorage.getItem('usmle_active_track');
      if (!targetTrack) {
        targetTrack = (savedExam === 'exam2') ? 'exam2_zen' : 'inhouse';
      }

      currentExam = savedExam;
      selectExam(savedExam);
      if (targetTrack) {
        switchTrack(targetTrack);
      }

      if (currentIndex > 0) {
        setTimeout(() => {
          const trackLabel = isExam2Track(currentTrack)
            ? (currentTrack === 'exam2_sim' ? 'Exam 2 Sim' : 'Exam 2 Mastery')
            : currentTrack === 'focused_zen'
            ? 'Focused Zen'
            : currentTrack === 'zen'
            ? 'General Zen'
            : (currentTrack === 'inhouse' ? 'In House' : 'Exam 1');
          showToast(`Resumed at Question ${currentIndex + 1} of ${questions.length} (${trackLabel})`);
        }, 300);
      }
    });
  </script>
</body>
</html>
"""

output_html_path = '/Users/markyoussef_1/.gemini/antigravity-ide/scratch/usmle_exam1/index.html'
with open(output_html_path, 'w', encoding='utf-8') as f:
    f.write(html_template)

print(f'Successfully built interactive HTML exam at: {output_html_path}')
print(f'HTML file size: {os.path.getsize(output_html_path) / 1024:.1f} KB')

# Also copy directly to Downloads
downloads_path = '/Users/markyoussef_1/Downloads/Ex1-USMLEPrac_Interactive_Exam.html'
with open(downloads_path, 'w', encoding='utf-8') as f:
    f.write(html_template)
print(f'Also saved copy directly to Downloads: {downloads_path}')

# Build complete successfully.
