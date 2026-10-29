# generate_complete_app.py
import json
import os
import random


with open('/Users/markyoussef_1/.gemini/antigravity-ide/scratch/usmle_exam1/questions_data.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

with open('/Users/markyoussef_1/.gemini/antigravity-ide/scratch/usmle_exam1/focused_zen_questions_data.json', 'r', encoding='utf-8') as f:
    focused_zen_questions = json.load(f)

with open('/Users/markyoussef_1/.gemini/antigravity-ide/scratch/usmle_exam1/zen_questions_data.json', 'r', encoding='utf-8') as f:
    zen_questions = json.load(f)

with open('/Users/markyoussef_1/.gemini/antigravity-ide/scratch/usmle_exam1/inhouse_questions_data.json', 'r', encoding='utf-8') as f:
    inhouse_questions = json.load(f)

exam2_path = '/Users/markyoussef_1/.gemini/antigravity-ide/scratch/usmle_exam1/exam2_questions_data.json'
if not os.path.exists(exam2_path):
    exam2_path = '/Users/markyoussef_1/.gemini/antigravity-ide/scratch/usmle_exam2/exam2_questions_data.json'

with open(exam2_path, 'r', encoding='utf-8') as f:
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
        'source': q.get('source', 'Official Exam 2 PDF'),
        'options': opts,
        'correct_idx': correct_idx,
        'explanation': q['explanation'],
        'high_yield_pearl': q.get('high_yield_pearl', ''),
        'image': q.get('image', None)
    })

# Load Exam 2 Zen (Units 1-6 In-House Bank: 315 Questions)
local_zen_u13_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'exam2_zen_units1_3_questions.json')
external_zen_u13_path = '/Users/markyoussef_1/.gemini/antigravity-ide/scratch/usmle_exam2/new_bank_units1_3/units1_3_questions.json'
u13_path = local_zen_u13_path if os.path.exists(local_zen_u13_path) else external_zen_u13_path

local_zen_u46_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'units4_6_questions.json')
external_zen_u46_path = '/Users/markyoussef_1/.gemini/antigravity-ide/scratch/usmle_exam2/new_bank_units4_6/units4_6_questions.json'
u46_path = local_zen_u46_path if os.path.exists(local_zen_u46_path) else external_zen_u46_path

with open(u13_path, 'r', encoding='utf-8') as f:
    raw_exam2_zen_u13 = json.load(f)

with open(u46_path, 'r', encoding='utf-8') as f:
    raw_exam2_zen_u46 = json.load(f)

raw_exam2_zen = raw_exam2_zen_u13 + raw_exam2_zen_u46

# Also save combined units1_6 JSON for reference
combined_zen_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'exam2_zen_units1_6_questions.json')
with open(combined_zen_path, 'w', encoding='utf-8') as f:
    json.dump(raw_exam2_zen, f, indent=2, ensure_ascii=False)

exam2_zen_questions = []
for q in raw_exam2_zen:
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
    exam2_zen_questions.append({
        'id': q['id'],
        'q_num': str(q['q_num']),
        'stem': q['question'],
        'category': q['category'],
        'source': q.get('source', ''),
        'options': opts,
        'correct_idx': correct_idx,
        'explanation': q['explanation'],
        'high_yield_pearl': q.get('high_yield_pearl', ''),
        'image': q.get('image', None)
    })

# Load Exam 2 In-House (Units 1-5 Course QBank: 181 Questions)
local_inhouse_e2_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'exam2_inhouse_questions.json')
external_inhouse_e2_path = '/Users/markyoussef_1/.gemini/antigravity-ide/scratch/usmle_exam2/exam2_inhouse_questions.json'
inhouse_e2_path = local_inhouse_e2_path if os.path.exists(local_inhouse_e2_path) else external_inhouse_e2_path

with open(inhouse_e2_path, 'r', encoding='utf-8') as f:
    raw_exam2_inhouse = json.load(f)

exam2_inhouse_questions = []
for q in raw_exam2_inhouse:
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
    exam2_inhouse_questions.append({
        'id': q['id'],
        'q_num': str(q['q_num']),
        'stem': q['stem'],
        'category': q['category'],
        'source': q.get('source', ''),
        'options': opts,
        'correct_idx': correct_idx,
        'explanation': q['explanation'],
        'high_yield_pearl': q.get('high_yield_pearl', ''),
        'image': q.get('image', None)
    })

# Randomize In House (181 Qs) across all topics using fixed seed
random.Random(42).shuffle(exam2_inhouse_questions)

exam2_inhouse_categories = [
    'Visual System',
    'Visual Reflexes',
    'Eye Disorders',
    'Auditory & Vestibular Systems',
    'UMN / LMN'
]

# Load Exam 2 In-House 2 (5 Units Randomized: 275 Questions)
local_inhouse2_e2_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'exam2_inhouse2_questions.json')
external_inhouse2_e2_path = '/Users/markyoussef_1/.gemini/antigravity-ide/scratch/usmle_exam2/exam2_inhouse2_questions.json'
inhouse2_e2_path = local_inhouse2_e2_path if os.path.exists(local_inhouse2_e2_path) else external_inhouse2_e2_path

with open(inhouse2_e2_path, 'r', encoding='utf-8') as f:
    raw_exam2_inhouse2 = json.load(f)

exam2_inhouse2_questions = []
for q in raw_exam2_inhouse2:
    opts = []
    correct_idx = 0
    if isinstance(q['options'], dict):
        for idx, (letter, text) in enumerate(sorted(q['options'].items())):
            is_cor = (letter == q['correct_answer'])
            if is_cor:
                correct_idx = idx
            opts.append({
                'letter': letter,
                'is_correct': is_cor,
                'text': text
            })
    else:
        for idx, opt in enumerate(q['options']):
            is_cor = (opt['id'] == q['correct_answer'])
            if is_cor:
                correct_idx = idx
            opts.append({
                'letter': opt['id'],
                'is_correct': is_cor,
                'text': opt['text']
            })
    exam2_inhouse2_questions.append({
        'id': q['id'],
        'q_num': str(q['q_num']),
        'stem': q['stem'],
        'category': q['category'],
        'source': q.get('source', 'In-House Step 1 Bank 2'),
        'options': opts,
        'correct_idx': correct_idx,
        'explanation': q['explanation'],
        'high_yield_pearl': q.get('high_yield_pearl', ''),
        'image': q.get('image', None)
    })

exam2_inhouse2_categories = [
    'Visual System',
    'Visual Reflexes',
    'Auditory & Vestibular Systems',
    'UMN / LMN',
    'Sleep & Sleep Disorders'
]

# Load Exam 2 Replicate (9 Units: 100 Questions)
local_replicate_e2_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'exam2_replicate_questions.json')
external_replicate_e2_path = '/Users/markyoussef_1/.gemini/antigravity-ide/scratch/usmle_exam2/exam2_replicate_questions.json'
replicate_e2_path = local_replicate_e2_path if os.path.exists(local_replicate_e2_path) else external_replicate_e2_path

with open(replicate_e2_path, 'r', encoding='utf-8') as f:
    raw_exam2_replicate = json.load(f)

exam2_replicate_questions = []
for q in raw_exam2_replicate:
    opts = []
    correct_idx = 0
    if isinstance(q['options'], dict):
        for idx, (letter, text) in enumerate(sorted(q['options'].items())):
            is_cor = (letter == q['correct_answer'])
            if is_cor:
                correct_idx = idx
            opts.append({
                'letter': letter,
                'is_correct': is_cor,
                'text': text
            })
    else:
        for idx, opt in enumerate(q['options']):
            is_cor = (opt.get('letter', opt.get('id')) == q['correct_answer'])
            if is_cor:
                correct_idx = idx
            opts.append({
                'letter': opt.get('letter', opt.get('id')),
                'is_correct': is_cor,
                'text': opt['text']
            })
    exam2_replicate_questions.append({
        'id': q['id'],
        'q_num': str(q['q_num']),
        'stem': q['stem'],
        'category': q['category'],
        'source': q.get('source', 'USMLE Step 1 Replicate Bank'),
        'options': opts,
        'correct_idx': correct_idx,
        'explanation': q['explanation'],
        'high_yield_pearl': q.get('high_yield_pearl', ''),
        'image': q.get('image', None)
    })

exam2_replicate_categories = [
    'Visual System',
    'Visual Reflexes',
    'Ophthalmology',
    'Auditory & Vestibular',
    'UMN/LMN',
    'Hypothalamus & Smell/Taste',
    'Basal Ganglia',
    'CBIL: Sleep',
    'CBIL: ALS'
]

# Load Exam 2 Deep (9 Units: 150 Questions)
local_deep_e2_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'exam2_deep_questions.json')
external_deep_e2_path = '/Users/markyoussef_1/.gemini/antigravity-ide/scratch/usmle_exam2/exam2_deep_questions.json'
deep_e2_path = local_deep_e2_path if os.path.exists(local_deep_e2_path) else external_deep_e2_path

with open(deep_e2_path, 'r', encoding='utf-8') as f:
    raw_exam2_deep = json.load(f)

exam2_deep_questions = []
for q in raw_exam2_deep:
    opts = []
    correct_idx = 0
    if isinstance(q['options'], dict):
        for idx, (letter, text) in enumerate(sorted(q['options'].items())):
            is_cor = (letter == q['correct_answer'])
            if is_cor:
                correct_idx = idx
            opts.append({
                'letter': letter,
                'is_correct': is_cor,
                'text': text
            })
    else:
        for idx, opt in enumerate(q['options']):
            is_cor = (opt.get('letter', opt.get('id')) == q['correct_answer'])
            if is_cor:
                correct_idx = idx
            opts.append({
                'letter': opt.get('letter', opt.get('id')),
                'is_correct': is_cor,
                'text': opt['text']
            })
    exam2_deep_questions.append({
        'id': q['id'],
        'q_num': str(q['q_num']),
        'stem': q['stem'],
        'category': q['category'],
        'source': q.get('source', 'USMLE Step 1 Deep Review Bank'),
        'options': opts,
        'correct_idx': correct_idx,
        'explanation': q['explanation'],
        'high_yield_pearl': q.get('high_yield_pearl', ''),
        'image': q.get('image', None)
    })

exam2_deep_categories = [
    'Visual System',
    'Visual Reflexes',
    'Ophthalmology',
    'Auditory & Vestibular System',
    'UMN / LMN',
    'Hypothalamus, Smell & Taste',
    'Basal Ganglia',
    'Sleep & Sleep Disorders',
    'Amyotrophic Lateral Sclerosis (ALS)'
]

# Load Exam 2 Set 2 (9 Units: 100 Questions)
local_set2_e2_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'exam2_set2_questions.json')
external_set2_e2_path = '/Users/markyoussef_1/.gemini/antigravity-ide/scratch/usmle_exam2/exam2_set2_questions.json'
set2_e2_path = local_set2_e2_path if os.path.exists(local_set2_e2_path) else external_set2_e2_path

with open(set2_e2_path, 'r', encoding='utf-8') as f:
    raw_exam2_set2 = json.load(f)

exam2_set2_questions = []
for q in raw_exam2_set2:
    opts = []
    correct_idx = 0
    if isinstance(q['options'], dict):
        for idx, (letter, text) in enumerate(sorted(q['options'].items())):
            is_cor = (letter == q['correct_answer'])
            if is_cor:
                correct_idx = idx
            opts.append({
                'letter': letter,
                'is_correct': is_cor,
                'text': text
            })
    else:
        for idx, opt in enumerate(q['options']):
            is_cor = (opt.get('letter', opt.get('id')) == q['correct_answer'])
            if is_cor:
                correct_idx = idx
            opts.append({
                'letter': opt.get('letter', opt.get('id')),
                'is_correct': is_cor,
                'text': opt['text']
            })
    exam2_set2_questions.append({
        'id': q['id'],
        'q_num': str(q['q_num']),
        'stem': q['stem'],
        'category': q['category'],
        'source': q.get('source', 'USMLE Step 1 Set 2 Bank'),
        'options': opts,
        'correct_idx': correct_idx,
        'explanation': q['explanation'],
        'high_yield_pearl': q.get('high_yield_pearl', ''),
        'image': q.get('image', None)
    })

exam2_set2_categories = [
    'Visual System',
    'Visual Reflexes',
    'Ophthalmology',
    'Auditory & Vestibular System',
    'UMN / LMN',
    'Hypothalamus, Smell & Taste',
    'Basal Ganglia',
    'Sleep & Sleep Disorders',
    'Amyotrophic Lateral Sclerosis (ALS)'
]

# Load Exam 2 Set 3 (9 Units: 150 Questions)
local_set3_e2_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'exam2_set3_questions.json')
external_set3_e2_path = '/Users/markyoussef_1/.gemini/antigravity-ide/scratch/usmle_exam2/exam2_set3_questions.json'
set3_e2_path = local_set3_e2_path if os.path.exists(local_set3_e2_path) else external_set3_e2_path

with open(set3_e2_path, 'r', encoding='utf-8') as f:
    raw_exam2_set3 = json.load(f)

exam2_set3_questions = []
for q in raw_exam2_set3:
    opts = []
    correct_idx = 0
    if isinstance(q['options'], dict):
        for idx, (letter, text) in enumerate(sorted(q['options'].items())):
            is_cor = (letter == q['correct_answer'])
            if is_cor:
                correct_idx = idx
            opts.append({
                'letter': letter,
                'is_correct': is_cor,
                'text': text
            })
    else:
        for idx, opt in enumerate(q['options']):
            is_cor = (opt.get('letter', opt.get('id')) == q['correct_answer'])
            if is_cor:
                correct_idx = idx
            opts.append({
                'letter': opt.get('letter', opt.get('id')),
                'is_correct': is_cor,
                'text': opt['text']
            })
    exam2_set3_questions.append({
        'id': q['id'],
        'q_num': str(q['q_num']),
        'stem': q['stem'],
        'category': q['category'],
        'source': q.get('source', 'USMLE Step 1 Set 3 Bank'),
        'options': opts,
        'correct_idx': correct_idx,
        'explanation': q['explanation'],
        'high_yield_pearl': q.get('high_yield_pearl', ''),
        'image': q.get('image', None)
    })

exam2_set3_categories = [
    'Visual System',
    'Visual Reflexes',
    'Ophthalmology',
    'Auditory & Vestibular System',
    'UMN / LMN',
    'Hypothalamus, Smell & Taste',
    'Basal Ganglia',
    'Sleep & Sleep Disorders',
    'Amyotrophic Lateral Sclerosis (ALS)'
]





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

exam2_zen_categories = [
    'Visual System',
    'Visual Reflexes',
    'Infection/Inflammation of eye disorders',
    'Auditory & Vestibular Systems',
    'UMN / LMN Motor Pathways',
    'Sleep & Sleep Disorders'
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
exam2_zen_json_data_str = json.dumps(exam2_zen_questions, ensure_ascii=False)
exam2_inhouse_json_data_str = json.dumps(exam2_inhouse_questions, ensure_ascii=False)
exam2_inhouse2_json_data_str = json.dumps(exam2_inhouse2_questions, ensure_ascii=False)
exam2_replicate_json_data_str = json.dumps(exam2_replicate_questions, ensure_ascii=False)
categories_json_str = json.dumps(categories, ensure_ascii=False)
inhouse_categories_json_str = json.dumps(inhouse_categories, ensure_ascii=False)
exam2_categories_json_str = json.dumps(exam2_categories, ensure_ascii=False)
exam2_zen_categories_json_str = json.dumps(exam2_zen_categories, ensure_ascii=False)
exam2_inhouse_categories_json_str = json.dumps(exam2_inhouse_categories, ensure_ascii=False)
exam2_inhouse2_categories_json_str = json.dumps(exam2_inhouse2_categories, ensure_ascii=False)
exam2_replicate_categories_json_str = json.dumps(exam2_replicate_categories, ensure_ascii=False)
exam2_deep_json_data_str = json.dumps(exam2_deep_questions, ensure_ascii=False)
exam2_deep_categories_json_str = json.dumps(exam2_deep_categories, ensure_ascii=False)
exam2_set2_json_data_str = json.dumps(exam2_set2_questions, ensure_ascii=False)
exam2_set2_categories_json_str = json.dumps(exam2_set2_categories, ensure_ascii=False)
exam2_set3_json_data_str = json.dumps(exam2_set3_questions, ensure_ascii=False)
exam2_set3_categories_json_str = json.dumps(exam2_set3_categories, ensure_ascii=False)


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

    /* ========================================================= */
    /* SAFE VAULT & AUTHENTICATION SCREENS                       */
    /* ========================================================= */
    .safe-vault-overlay {
      position: fixed;
      inset: 0;
      z-index: 999999;
      background: radial-gradient(ellipse at center, #1e2430 0%, #101319 55%, #05070a 100%);
      display: flex;
      align-items: center;
      justify-content: center;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      overflow: hidden;
      transition: opacity 0.6s ease, transform 0.6s ease;
    }

    .safe-vault-overlay.unlocked {
      opacity: 0;
      pointer-events: none;
      transform: scale(1.08);
    }

    /* Vault Background Environment */
    .vault-bg-grid {
      position: absolute;
      inset: 0;
      background-image: 
        linear-gradient(rgba(255, 255, 255, 0.03) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255, 255, 255, 0.03) 1px, transparent 1px);
      background-size: 40px 40px;
      pointer-events: none;
    }

    .vault-door-container {
      position: relative;
      width: min(92vw, 540px);
      background: linear-gradient(145deg, #2a313d, #181d24);
      border-radius: 28px;
      padding: 32px 28px;
      box-shadow: 
        0 30px 80px rgba(0, 0, 0, 0.85),
        inset 0 2px 4px rgba(255, 255, 255, 0.15),
        inset 0 -3px 8px rgba(0, 0, 0, 0.6),
        0 0 0 8px #13171e,
        0 0 0 12px #2f3744;
      border: 1px solid rgba(255, 255, 255, 0.1);
      display: flex;
      flex-direction: column;
      align-items: center;
      z-index: 2;
    }

    /* Vault Rivets */
    .vault-rivets {
      position: absolute;
      inset: 10px;
      border: 2px dashed rgba(255, 255, 255, 0.08);
      border-radius: 20px;
      pointer-events: none;
    }

    /* Vault Combination Wheel */
    .vault-wheel-wrap {
      width: 120px;
      height: 120px;
      position: relative;
      margin-bottom: 20px;
      display: flex;
      align-items: center;
      justify-content: center;
    }

    .vault-wheel {
      width: 100px;
      height: 100px;
      border-radius: 50%;
      background: radial-gradient(circle at 35% 35%, #5a6578, #2a303c 70%, #1a1e26);
      box-shadow: 
        0 8px 24px rgba(0, 0, 0, 0.7),
        inset 0 2px 4px rgba(255, 255, 255, 0.3),
        inset 0 -3px 6px rgba(0, 0, 0, 0.8);
      border: 3px solid #717d91;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: transform 1.2s cubic-bezier(0.34, 1.56, 0.64, 1);
      position: relative;
    }

    .vault-wheel-spoke {
      position: absolute;
      background: linear-gradient(to right, #414a58, #94a3b8, #414a58);
      border-radius: 4px;
      box-shadow: 0 2px 5px rgba(0,0,0,0.5);
    }
    .spoke-h { width: 130px; height: 10px; }
    .spoke-v { width: 10px; height: 130px; }

    .vault-wheel-hub {
      width: 44px;
      height: 44px;
      border-radius: 50%;
      background: radial-gradient(circle at 35% 35%, #cbd5e1, #64748b 80%, #334155);
      border: 2px solid #94a3b8;
      box-shadow: 0 4px 10px rgba(0,0,0,0.6);
      z-index: 3;
      display: flex;
      align-items: center;
      justify-content: center;
      color: #0f172a;
      font-size: 18px;
    }

    .vault-wheel.spinning {
      transform: rotate(720deg);
    }

    /* Terminal HUD Card */
    .vault-terminal {
      width: 100%;
      background: rgba(15, 20, 27, 0.85);
      border: 1px solid rgba(56, 189, 248, 0.25);
      border-radius: 18px;
      padding: 22px 24px;
      box-shadow: inset 0 0 20px rgba(56, 189, 248, 0.05);
      text-align: center;
    }

    .terminal-status-row {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 10px;
      margin-bottom: 8px;
    }

    .terminal-led {
      width: 10px;
      height: 10px;
      border-radius: 50%;
      background: #06b6d4;
      box-shadow: 0 0 10px #06b6d4, 0 0 20px #06b6d4;
      animation: pulseLed 2s infinite ease-in-out;
    }

    @keyframes pulseLed {
      0%, 100% { opacity: 0.5; transform: scale(0.9); }
      50% { opacity: 1; transform: scale(1.15); }
    }

    .terminal-led.error {
      background: #ef4444;
      box-shadow: 0 0 10px #ef4444;
    }

    .terminal-led.success {
      background: #10b981;
      box-shadow: 0 0 10px #10b981;
    }

    .terminal-title {
      font-size: 16px;
      font-weight: 700;
      letter-spacing: 2px;
      color: #e2e8f0;
      text-transform: uppercase;
    }

    .terminal-subtitle {
      font-size: 12px;
      color: #94a3b8;
      margin-bottom: 18px;
    }

    .vault-input-group {
      margin-bottom: 14px;
      text-align: left;
    }

    .vault-input-group label {
      display: block;
      font-size: 11px;
      font-weight: 600;
      color: #64748b;
      letter-spacing: 1px;
      margin-bottom: 6px;
      text-transform: uppercase;
    }

    .vault-input {
      width: 100%;
      background: #090d14;
      border: 1px solid rgba(255, 255, 255, 0.12);
      border-radius: 10px;
      padding: 12px 14px;
      color: #f8fafc;
      font-size: 14px;
      outline: none;
      transition: border-color 0.2s, box-shadow 0.2s;
      box-sizing: border-box;
    }

    .vault-input:focus {
      border-color: #38bdf8;
      box-shadow: 0 0 0 3px rgba(56, 189, 248, 0.25);
    }

    .vault-msg {
      font-size: 12px;
      padding: 8px 12px;
      border-radius: 8px;
      margin-bottom: 14px;
      display: none;
      line-height: 1.4;
    }

    .vault-msg.error {
      display: block;
      background: rgba(239, 68, 68, 0.15);
      border: 1px solid rgba(239, 68, 68, 0.4);
      color: #fca5a5;
    }

    .vault-msg.success {
      display: block;
      background: rgba(16, 185, 129, 0.15);
      border: 1px solid rgba(16, 185, 129, 0.4);
      color: #6ee7b7;
    }

    .vault-unlock-btn {
      width: 100%;
      background: linear-gradient(135deg, #0284c7, #0369a1);
      color: #ffffff;
      border: none;
      border-radius: 10px;
      padding: 14px;
      font-size: 14px;
      font-weight: 600;
      letter-spacing: 1px;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      transition: all 0.2s;
      box-shadow: 0 4px 14px rgba(2, 132, 199, 0.35);
    }

    .vault-unlock-btn:hover {
      background: linear-gradient(135deg, #0369a1, #0284c7);
      transform: translateY(-1px);
      box-shadow: 0 6px 18px rgba(2, 132, 199, 0.45);
    }

    .vault-unlock-btn:active {
      transform: translateY(0);
    }

    /* ========================================================= */
    /* CLOWN TROLL TAKEOVER SCREEN                               */
    /* ========================================================= */
    .clown-takeover-screen {
      position: fixed;
      inset: 0;
      z-index: 1000000;
      background: repeating-linear-gradient(45deg, #b91c1c, #b91c1c 40px, #f59e0b 40px, #f59e0b 80px);
      display: none;
      align-items: center;
      justify-content: center;
      padding: 20px;
      box-sizing: border-box;
      animation: circusShift 8s infinite linear;
    }

    @keyframes circusShift {
      0% { background-position: 0 0; }
      100% { background-position: 160px 160px; }
    }

    .clown-card {
      background: rgba(15, 23, 42, 0.95);
      border: 4px solid #facc15;
      border-radius: 28px;
      max-width: 520px;
      width: 100%;
      padding: 36px 28px;
      text-align: center;
      box-shadow: 0 30px 70px rgba(0,0,0,0.85), 0 0 50px rgba(234, 179, 8, 0.5);
      position: relative;
      animation: clownWiggle 1.5s infinite ease-in-out;
    }

    @keyframes clownWiggle {
      0%, 100% { transform: translateY(0) rotate(0deg); }
      25% { transform: translateY(-8px) rotate(-2deg); }
      75% { transform: translateY(8px) rotate(2deg); }
    }

    .clown-avatar {
      font-size: 82px;
      line-height: 1;
      margin-bottom: 14px;
      display: inline-block;
      animation: spinBounce 2s infinite ease-in-out;
    }

    @keyframes spinBounce {
      0%, 100% { transform: scale(1); }
      50% { transform: scale(1.25) rotate(15deg); }
    }

    .clown-title {
      font-size: 26px;
      font-weight: 900;
      color: #facc15;
      text-transform: uppercase;
      letter-spacing: 1.5px;
      margin-bottom: 8px;
      text-shadow: 0 2px 10px rgba(250, 204, 21, 0.5);
    }

    .clown-badge {
      display: inline-block;
      background: #ef4444;
      color: #fff;
      font-weight: 700;
      font-size: 13px;
      padding: 4px 12px;
      border-radius: 20px;
      margin-bottom: 18px;
      letter-spacing: 1px;
    }

    .clown-desc {
      color: #e2e8f0;
      font-size: 15px;
      line-height: 1.6;
      margin-bottom: 24px;
    }

    .clown-btn {
      background: linear-gradient(135deg, #eab308, #ca8a04);
      color: #0f172a;
      border: none;
      border-radius: 12px;
      padding: 14px 28px;
      font-size: 15px;
      font-weight: 800;
      cursor: pointer;
      box-shadow: 0 6px 20px rgba(234, 179, 8, 0.4);
      transition: transform 0.2s;
    }

    .clown-btn:hover {
      transform: scale(1.05);
    }

    /* ========================================================= */
    /* JACOB DEBT SETTLEMENT SCREEN                              */
    /* ========================================================= */
    .jacob-debt-screen {
      position: fixed;
      inset: 0;
      z-index: 1000000;
      background: radial-gradient(circle at center, #062b19 0%, #03140c 70%, #010805 100%);
      display: none;
      align-items: center;
      justify-content: center;
      padding: 20px;
      box-sizing: border-box;
    }

    .debt-contract-card {
      background: #0b1a13;
      border: 3px double #10b981;
      border-radius: 24px;
      max-width: 520px;
      width: 100%;
      padding: 36px 30px;
      text-align: center;
      box-shadow: 0 30px 80px rgba(0,0,0,0.9), 0 0 60px rgba(16, 185, 129, 0.25);
      position: relative;
    }

    .debt-seal {
      width: 68px;
      height: 68px;
      border-radius: 50%;
      background: radial-gradient(circle at 35% 35%, #34d399, #059669);
      border: 2px solid #a7f3d0;
      margin: 0 auto 16px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 32px;
      box-shadow: 0 6px 18px rgba(16, 185, 129, 0.4);
    }

    .debt-title {
      font-size: 20px;
      font-weight: 800;
      letter-spacing: 2px;
      color: #6ee7b7;
      text-transform: uppercase;
      margin-bottom: 4px;
    }

    .debt-balance-highlight {
      font-size: 36px;
      font-weight: 900;
      color: #facc15;
      margin: 12px 0 16px;
      text-shadow: 0 2px 14px rgba(250, 204, 21, 0.4);
    }

    .debt-terms-box {
      background: rgba(6, 78, 59, 0.35);
      border: 1px solid rgba(52, 211, 153, 0.25);
      border-radius: 12px;
      padding: 16px;
      font-size: 13px;
      color: #d1fae5;
      text-align: left;
      line-height: 1.6;
      margin-bottom: 24px;
    }

    .debt-actions {
      display: flex;
      gap: 12px;
    }

    .debt-btn-accept {
      flex: 1;
      background: linear-gradient(135deg, #10b981, #059669);
      color: #ffffff;
      border: none;
      border-radius: 12px;
      padding: 14px 16px;
      font-size: 14px;
      font-weight: 700;
      cursor: pointer;
      box-shadow: 0 6px 20px rgba(16, 185, 129, 0.35);
      transition: all 0.2s;
    }

    .debt-btn-accept:hover {
      background: linear-gradient(135deg, #059669, #10b981);
      transform: translateY(-2px);
    }

    .debt-btn-decline {
      background: #1e293b;
      color: #94a3b8;
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-radius: 12px;
      padding: 14px 18px;
      font-size: 14px;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.15s;
    }

    /* ========================================================= */
    /* GOLDEN PALACE SCREEN                                      */
    /* ========================================================= */
    .golden-palace-screen {
      position: fixed;
      inset: 0;
      z-index: 1000000;
      background: radial-gradient(circle at center, #634306 0%, #301f03 60%, #120b01 100%);
      display: none;
      align-items: center;
      justify-content: center;
      padding: 20px;
      box-sizing: border-box;
      overflow: hidden;
    }

    .palace-rays {
      position: absolute;
      width: 140vmax;
      height: 140vmax;
      background: conic-gradient(from 0deg, transparent 0deg 15deg, rgba(250, 204, 21, 0.08) 15deg 30deg, transparent 30deg 45deg, rgba(250, 204, 21, 0.08) 45deg 60deg, transparent 60deg 75deg, rgba(250, 204, 21, 0.08) 75deg 90deg, transparent 90deg 105deg, rgba(250, 204, 21, 0.08) 105deg 120deg, transparent 120deg 135deg, rgba(250, 204, 21, 0.08) 135deg 150deg, transparent 150deg 165deg, rgba(250, 204, 21, 0.08) 165deg 180deg, transparent 180deg 195deg, rgba(250, 204, 21, 0.08) 195deg 210deg, transparent 210deg 225deg, rgba(250, 204, 21, 0.08) 225deg 240deg, transparent 240deg 255deg, rgba(250, 204, 21, 0.08) 255deg 270deg, transparent 270deg 285deg, rgba(250, 204, 21, 0.08) 285deg 300deg, transparent 300deg 315deg, rgba(250, 204, 21, 0.08) 315deg 330deg, transparent 330deg 345deg, rgba(250, 204, 21, 0.08) 345deg 360deg);
      animation: rotateRays 40s infinite linear;
      pointer-events: none;
    }

    @keyframes rotateRays {
      from { transform: rotate(0deg); }
      to { transform: rotate(360deg); }
    }

    .palace-card {
      background: rgba(26, 17, 3, 0.9);
      border: 3px solid #eab308;
      border-radius: 30px;
      max-width: 560px;
      width: 100%;
      padding: 42px 34px;
      text-align: center;
      box-shadow: 0 30px 90px rgba(0,0,0,0.95), 0 0 80px rgba(234, 179, 8, 0.45);
      position: relative;
      z-index: 2;
    }

    .palace-crown {
      font-size: 78px;
      line-height: 1;
      margin-bottom: 14px;
      display: inline-block;
      filter: drop-shadow(0 6px 16px rgba(250, 204, 21, 0.6));
      animation: crownFloat 3s infinite ease-in-out;
    }

    @keyframes crownFloat {
      0%, 100% { transform: translateY(0); }
      50% { transform: translateY(-10px); }
    }

    .palace-title {
      font-size: 28px;
      font-weight: 900;
      letter-spacing: 3px;
      background: linear-gradient(135deg, #fef08a, #eab308, #ca8a04);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      margin-bottom: 6px;
      text-transform: uppercase;
    }

    .palace-subtitle {
      font-size: 15px;
      font-weight: 700;
      color: #fef08a;
      letter-spacing: 1.5px;
      margin-bottom: 18px;
      text-transform: uppercase;
    }

    .palace-desc {
      color: #fef9c3;
      font-size: 14px;
      line-height: 1.7;
      margin-bottom: 28px;
    }

    .palace-btn {
      background: linear-gradient(135deg, #facc15, #ca8a04);
      color: #1a1202;
      border: none;
      border-radius: 14px;
      padding: 16px 28px;
      font-size: 15px;
      font-weight: 800;
      letter-spacing: 1px;
      cursor: pointer;
      box-shadow: 0 6px 24px rgba(234, 179, 8, 0.5);
      transition: all 0.2s;
    }

    .palace-btn:hover {
      transform: scale(1.04);
      box-shadow: 0 8px 30px rgba(234, 179, 8, 0.65);
    }


    /* ========================================================= */
    /* MARK MOG SCREEN (🗿 🤫🧏‍♂️)                                */
    /* ========================================================= */
    .mark-mog-screen {
      position: fixed;
      inset: 0;
      z-index: 1000000;
      background: radial-gradient(circle at center, #1b0a2e 0%, #0d041a 50%, #05020a 100%);
      display: none;
      align-items: center;
      justify-content: center;
      padding: 20px;
      box-sizing: border-box;
      overflow: hidden;
    }

    .mog-glow-pulse {
      position: absolute;
      width: 650px;
      height: 650px;
      border-radius: 50%;
      background: radial-gradient(circle, rgba(168, 85, 247, 0.25) 0%, rgba(59, 130, 246, 0.15) 50%, transparent 70%);
      animation: auraPulse 3s infinite ease-in-out;
      pointer-events: none;
    }

    @keyframes auraPulse {
      0%, 100% { transform: scale(1); opacity: 0.6; }
      50% { transform: scale(1.3); opacity: 0.9; }
    }

    .mog-card {
      background: rgba(18, 11, 30, 0.94);
      border: 2px solid #a855f7;
      border-radius: 28px;
      max-width: 560px;
      width: 100%;
      padding: 38px 32px;
      text-align: center;
      box-shadow: 0 0 60px rgba(168, 85, 247, 0.4), 0 0 100px rgba(59, 130, 246, 0.25);
      position: relative;
      z-index: 2;
    }

    .mog-avatar {
      font-size: 80px;
      line-height: 1;
      margin-bottom: 12px;
      display: inline-block;
      filter: drop-shadow(0 0 20px rgba(168, 85, 247, 0.8));
      animation: chadBob 2s infinite ease-in-out;
    }

    @keyframes chadBob {
      0%, 100% { transform: translateY(0); }
      50% { transform: translateY(-8px); }
    }

    .mog-title {
      font-size: 28px;
      font-weight: 900;
      letter-spacing: 2.5px;
      background: linear-gradient(135deg, #c084fc, #a855f7, #60a5fa);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      margin-bottom: 4px;
      text-transform: uppercase;
    }

    .mog-badge {
      display: inline-block;
      background: rgba(168, 85, 247, 0.2);
      border: 1px solid rgba(168, 85, 247, 0.5);
      color: #e9d5ff;
      font-weight: 700;
      font-size: 13px;
      padding: 5px 14px;
      border-radius: 20px;
      margin-bottom: 20px;
      letter-spacing: 1px;
    }

    .mog-stats-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 10px;
      margin-bottom: 20px;
    }

    .mog-stat-chip {
      background: rgba(168, 85, 247, 0.1);
      border: 1px solid rgba(168, 85, 247, 0.25);
      border-radius: 12px;
      padding: 10px 14px;
      text-align: left;
    }

    .mog-stat-label {
      font-size: 10px;
      font-weight: 700;
      color: #c084fc;
      letter-spacing: 1px;
      text-transform: uppercase;
      margin-bottom: 2px;
    }

    .mog-stat-val {
      font-size: 14px;
      font-weight: 800;
      color: #f8fafc;
    }

    .mog-quote {
      font-style: italic;
      color: #ddd6fe;
      font-size: 13px;
      line-height: 1.6;
      margin-bottom: 24px;
      border-left: 3px solid #a855f7;
      padding-left: 12px;
      text-align: left;
    }

    .mog-btn {
      width: 100%;
      background: linear-gradient(135deg, #9333ea, #3b82f6);
      color: #ffffff;
      border: none;
      border-radius: 12px;
      padding: 15px;
      font-size: 15px;
      font-weight: 800;
      letter-spacing: 1px;
      cursor: pointer;
      box-shadow: 0 6px 25px rgba(147, 51, 234, 0.45);
      transition: all 0.2s;
    }

    .mog-btn:hover {
      transform: translateY(-2px);
      box-shadow: 0 8px 30px rgba(147, 51, 234, 0.6);
    }

    /* ========================================================= */
    /* TYLER BIRTHDAY SCREEN (🎂 🎉 🎈)                         */
    /* ========================================================= */
    .tyler-bday-screen {
      position: fixed;
      inset: 0;
      z-index: 1000000;
      background: radial-gradient(circle at center, #2e1065 0%, #170836 60%, #090217 100%);
      display: none;
      align-items: center;
      justify-content: center;
      padding: 20px;
      box-sizing: border-box;
      overflow: hidden;
    }

    .bday-card {
      background: rgba(30, 15, 60, 0.95);
      border: 3px solid #f43f5e;
      border-radius: 28px;
      max-width: 540px;
      width: 100%;
      padding: 38px 32px;
      text-align: center;
      box-shadow: 0 0 60px rgba(244, 63, 94, 0.4), 0 0 100px rgba(234, 179, 8, 0.3);
      position: relative;
      z-index: 2;
    }

    .bday-cake {
      font-size: 82px;
      line-height: 1;
      margin-bottom: 12px;
      display: inline-block;
      animation: cakeWiggle 2s infinite ease-in-out;
    }

    @keyframes cakeWiggle {
      0%, 100% { transform: scale(1) rotate(0deg); }
      25% { transform: scale(1.15) rotate(-6deg); }
      75% { transform: scale(1.15) rotate(6deg); }
    }

    .bday-title {
      font-size: 28px;
      font-weight: 900;
      letter-spacing: 2px;
      background: linear-gradient(135deg, #fb7185, #f43f5e, #fbbf24);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      margin-bottom: 6px;
      text-transform: uppercase;
    }

    .bday-badge {
      display: inline-block;
      background: linear-gradient(135deg, #f43f5e, #fbbf24);
      color: #fff;
      font-weight: 800;
      font-size: 13px;
      padding: 5px 16px;
      border-radius: 20px;
      margin-bottom: 18px;
      letter-spacing: 1px;
    }

    .bday-msg {
      color: #ffe4e6;
      font-size: 15px;
      line-height: 1.7;
      margin-bottom: 26px;
    }

    .bday-btn {
      background: linear-gradient(135deg, #f43f5e, #e11d48);
      color: #ffffff;
      border: none;
      border-radius: 12px;
      padding: 15px 30px;
      font-size: 15px;
      font-weight: 800;
      cursor: pointer;
      box-shadow: 0 6px 25px rgba(244, 63, 94, 0.45);
      transition: all 0.2s;
    }

    .bday-btn:hover {
      transform: translateY(-2px);
      box-shadow: 0 8px 30px rgba(244, 63, 94, 0.6);
    }

  </style>
</head>
<body data-theme="dark">

  <!-- Safe Vault Authentication Overlay -->
  <div id="safeVaultOverlay" class="safe-vault-overlay">
    <div class="vault-bg-grid"></div>
    <div class="vault-door-container" id="vaultDoorContainer">
      <div class="vault-rivets"></div>
      
      <!-- Vault Combination Wheel -->
      <div class="vault-wheel-wrap">
        <div class="vault-wheel" id="vaultWheel">
          <div class="vault-wheel-spoke spoke-h"></div>
          <div class="vault-wheel-spoke spoke-v"></div>
          <div class="vault-wheel-hub">🔒</div>
        </div>
      </div>

      <!-- Vault Terminal Card -->
      <div class="vault-terminal" id="vaultTerminalCard">
        <div class="terminal-status-row">
          <div class="terminal-led" id="terminalLed"></div>
          <div class="terminal-title">SECURITY VAULT</div>
        </div>
        <div class="terminal-subtitle">Restricted Access • Clearance Required</div>

        <form id="vaultLoginForm" onsubmit="event.preventDefault(); handleSafeUnlock();">
          <div class="vault-input-group">
            <label for="safeNameInput">Operative Name</label>
            <input type="text" id="safeNameInput" class="vault-input" placeholder="Enter your name..." autocomplete="name" required />
          </div>

          <div class="vault-input-group">
            <label for="safePasswordInput">Passcode (Optional)</label>
            <input type="password" id="safePasswordInput" class="vault-input" placeholder="Enter passcode..." autocomplete="current-password" />
          </div>

          <div id="safeStatusMsg" class="vault-msg"></div>

          <button type="submit" class="vault-unlock-btn" id="safeUnlockBtn">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
            <span>AUTHENTICATE &amp; UNLOCK</span>
          </button>
        </form>
      </div>
    </div>
  </div>

  <!-- Clown Troll Takeover Screen (Ryan) -->
  
  <!-- Mark Mog Screen (🗿 🤫🧏‍♂️) -->
  <div id="markMogScreen" class="mark-mog-screen">
    <div class="mog-glow-pulse"></div>
    <div class="mog-card" id="mogCard">
      <div class="mog-avatar">🗿</div>
      <div class="mog-title">MARK DETECTED</div>
      <div class="mog-badge">🤫🧏‍♂️ ABSOLUTE MOGGER • +∞ AURA</div>
      
      <div class="mog-stats-grid">
        <div class="mog-stat-chip">
          <div class="mog-stat-label">AURA LEVEL</div>
          <div class="mog-stat-val">+99,999,999</div>
        </div>
        <div class="mog-stat-chip">
          <div class="mog-stat-label">CANTHAL TILT</div>
          <div class="mog-stat-val">POSITIVE MAX</div>
        </div>
        <div class="mog-stat-chip">
          <div class="mog-stat-label">JAWLINE STATUS</div>
          <div class="mog-stat-val">DIAMOND CUT</div>
        </div>
        <div class="mog-stat-chip">
          <div class="mog-stat-label">SERVER STATUS</div>
          <div class="mog-stat-val">MOGGING EVERYONE</div>
        </div>
      </div>

      <div class="mog-quote">
        "Bye bye 🤫🧏‍♂️. Neuro Step 1 questions have been completely mogged into submission."
      </div>

      <button class="mog-btn" id="enterMogBtn" onclick="enterFromMog()">
        🗿 ENTER THE SERVER (BYE BYE 🤫🧏‍♂️)
      </button>
    </div>
  </div>

  <!-- Tyler Birthday Screen (🎂 🎉 🎈) -->
  <div id="tylerBdayScreen" class="tyler-bday-screen">
    <div class="bday-card">
      <div class="bday-cake">🎂</div>
      <div class="bday-title">HAPPY BIRTHDAY TYLER!</div>
      <div class="bday-badge">🎉 BIRTHDAY CLEARANCE UNLOCKED 🎉</div>
      <div class="bday-msg">
        Wishing you the happiest of birthdays, Tyler! 🥳🎈<br>
        Another year wiser, sharper, and one step closer to crushing Step 1.<br>
        Full unrestricted clearance has been unlocked in your honor!
      </div>
      <button class="bday-btn" onclick="enterFromBirthday()">
        🎂 BLOW OUT CANDLES &amp; ENTER EXAM 🎈
      </button>
    </div>
  </div>

  <div id="clownTakeoverScreen" class="clown-takeover-screen">
    <div class="clown-card">
      <div class="clown-avatar">🤡</div>
      <div class="clown-title">RYAN DETECTED</div>
      <div class="clown-badge">🎪 CIRCUS TENT ACCESS ONLY 🎪</div>
      <div class="clown-desc">
        HONK HONK! 🎺 Access to medical knowledge has been quarantined!<br>
        You have been sentenced to the 3-ring circus playing nonstop clown music.
      </div>
      <button class="clown-btn" onclick="exitClownTakeover()">
        🎪 Honk Horn &amp; Retreat to Safe
      </button>
    </div>
  </div>

  <!-- Jacob Dollar Debt Screen -->
  <div id="jacobDebtScreen" class="jacob-debt-screen">
    <div class="debt-contract-card" id="debtContractCard">
      <div class="debt-seal">💵</div>
      <div class="debt-title">Debt Settlement Agreement</div>
      <div class="debt-balance-highlight">YOU OWE MARK $1.00</div>
      <div class="debt-terms-box">
        <strong>LEGAL DEBT NOTICE:</strong><br>
        1. Debtor (Jacob) unconditionally confirms an unpaid balance of <strong>$1.00 USD</strong> owed to Mark.<br>
        2. Unlocking Exam 2 requires legally binding consent to remit this dollar upon demand.<br>
        3. Do you accept these financial terms?
      </div>
      <div class="debt-actions">
        <button class="debt-btn-accept" onclick="acceptJacobTerms()">
          ✅ I Accept Terms (I Owe You $1.00)
        </button>
        <button class="debt-btn-decline" id="declineDebtBtn" onmouseenter="dodgeDeclineBtn()" onclick="dodgeDeclineBtn()">
          ❌ Decline
        </button>
      </div>
    </div>
  </div>

  <!-- Golden Palace Screen (Marlon) -->
  <div id="goldenPalaceScreen" class="golden-palace-screen">
    <div class="palace-rays"></div>
    <div class="palace-card">
      <div class="palace-crown">👑</div>
      <div class="palace-title">The Golden Palace</div>
      <div class="palace-subtitle">Imperial Clearance Granted • Marlon</div>
      <div class="palace-desc">
        The golden gates swing open in your honor. Full sovereign access to the complete Neurological Question Bank has been unlocked.
      </div>
      <button class="palace-btn" id="enterPalaceBtn" onclick="enterFromPalace()">
        👑 ENTER THE THRONE ROOM (TO EXAM)
      </button>
    </div>
  </div>


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

            <button class="btn btn-icon" onclick="lockVault()" title="Lock Vault (Open Safe Login)">
        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
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
    const rawExam2ZenQuestions = """ + exam2_zen_json_data_str + """;
    const rawExam2InHouseQuestions = """ + exam2_inhouse_json_data_str + """;
    const exam2Categories = """ + exam2_categories_json_str + """;
    const exam2ZenCategories = """ + exam2_zen_categories_json_str + """;
    const exam2InHouseCategories = """ + exam2_inhouse_categories_json_str + """;
    const rawExam2InHouse2Questions = """ + exam2_inhouse2_json_data_str + """;
    const exam2InHouse2Categories = """ + exam2_inhouse2_categories_json_str + """;
    const rawExam2ReplicateQuestions = """ + exam2_replicate_json_data_str + """;
    const exam2ReplicateCategories = """ + exam2_replicate_categories_json_str + """;
    const rawExam2DeepQuestions = """ + exam2_deep_json_data_str + """;
    const exam2DeepCategories = """ + exam2_deep_categories_json_str + """;
    const rawExam2Set2Questions = """ + exam2_set2_json_data_str + """;
    const exam2Set2Categories = """ + exam2_set2_categories_json_str + """;
    const rawExam2Set3Questions = """ + exam2_set3_json_data_str + """;
    const exam2Set3Categories = """ + exam2_set3_categories_json_str + """;


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
          id: 'exam2_inhouse',
          label: 'In House (181 Qs)',
          icon: '🏠',
          badge: 'Randomized 5 Units',
          type: 'inhouse'
        },
        {
          id: 'exam2_inhouse2',
          label: 'In House 2 (275 Qs)',
          icon: '🏠',
          badge: 'Randomized 5 Units',
          type: 'inhouse'
        },
        {
          id: 'exam2_replicate',
          label: 'Replicate (100 Qs)',
          icon: '🔄',
          badge: 'Randomized 9 Units',
          type: 'inhouse'
        },
        {
          id: 'exam2_deep',
          label: 'Deep (150 Qs)',
          icon: '🔬',
          badge: 'Randomized 9 Units',
          type: 'inhouse'
        },
        {
          id: 'exam2_set2',
          label: 'Set 2 (100 Qs)',
          icon: '📑',
          badge: 'Randomized 9 Units',
          type: 'inhouse'
        },
        {
          id: 'exam2_set3',
          label: 'Set 3 (150 Qs)',
          icon: '📚',
          badge: 'Randomized 9 Units',
          type: 'inhouse'
        },
        {
          id: 'exam2_zen',
          label: 'Zen Mode (315 Qs)',
          icon: '🧘',
          badge: 'Units 1–6 In-House',
          type: 'exam2'
        },
        {
          id: 'exam2_sim',
          label: 'Simulation (103 Qs)',
          icon: '<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>',
          badge: 'Official PDF',
          type: 'sim'
        },
        {
          id: 'exam2_pdf_practice',
          label: 'PDF Practice (103 Qs)',
          icon: '🎯',
          badge: '9 Sections',
          type: 'exam2'
        }
      ]
    };

    function isExam2Track(track) {
      return track === 'exam2' || track === 'exam2_inhouse' || track === 'exam2_inhouse2' || track === 'exam2_replicate' || track === 'exam2_deep' || track === 'exam2_set3' || track === 'exam2_set2' || track === 'exam2_sim' || track === 'exam2_zen' || track === 'exam2_pdf_practice';
    }

    function getCategoriesForTrack() {
      if (currentTrack === 'exam2_set3') return exam2Set3Categories;
      if (currentTrack === 'exam2_set2') return exam2Set2Categories;
      if (currentTrack === 'exam2_deep') return exam2DeepCategories;
      if (currentTrack === 'exam2_replicate') return exam2ReplicateCategories;
      if (currentTrack === 'exam2_inhouse2') return exam2InHouse2Categories;
      if (currentTrack === 'exam2_inhouse') return exam2InHouseCategories;
      if (currentTrack === 'exam2_zen' || currentTrack === 'exam2') return exam2ZenCategories;
      if (isExam2Track(currentTrack)) return exam2Categories;
      if (currentTrack === 'inhouse') return inHouseCategories;
      return subjectCategories;
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

      if (currentTrack === 'exam2_set3') {
        zenTray.style.display = 'flex';
        trayIcon.textContent = '📚';
        trayLabelText.textContent = 'Set 3 Units:';
        trackTag.style.display = 'inline-block';
        trackTag.className = 'q-track-tag inhouse';
        trackTag.textContent = '📚 Exam 2 Set 3';
        timerDisplay.classList.add('inhouse');
        sidebarTitle.innerHTML = `<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg> Set 3 Units (9)`;
      } else if (currentTrack === 'exam2_set2') {
        zenTray.style.display = 'flex';
        trayIcon.textContent = '📑';
        trayLabelText.textContent = 'Set 2 Units:';
        trackTag.style.display = 'inline-block';
        trackTag.className = 'q-track-tag inhouse';
        trackTag.textContent = '📑 Exam 2 Set 2';
        timerDisplay.classList.add('inhouse');
        sidebarTitle.innerHTML = `<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg> Set 2 Units (9)`;
      } else if (currentTrack === 'exam2_deep') {
        zenTray.style.display = 'flex';
        trayIcon.textContent = '🔬';
        trayLabelText.textContent = 'Deep Units:';
        trackTag.style.display = 'inline-block';
        trackTag.className = 'q-track-tag inhouse';
        trackTag.textContent = '🔬 Exam 2 Deep';
        timerDisplay.classList.add('inhouse');
        sidebarTitle.innerHTML = `<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20"/><path d="M2 12h20"/></svg> Deep Units (9)`;
      } else if (currentTrack === 'exam2_replicate') {
        zenTray.style.display = 'flex';
        trayIcon.textContent = '🔄';
        trayLabelText.textContent = 'Replicate Units:';
        trackTag.style.display = 'inline-block';
        trackTag.className = 'q-track-tag inhouse';
        trackTag.textContent = '🔄 Exam 2 Replicate';
        timerDisplay.classList.add('inhouse');
        sidebarTitle.innerHTML = `<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21.5 2v6h-6M21.34 15.57a10 10 0 1 1-.57-8.38l5.67-5.67"/></svg> Replicate Units (9)`;
      } else if (currentTrack === 'exam2_inhouse2') {
        zenTray.style.display = 'flex';
        trayIcon.textContent = '🏠';
        trayLabelText.textContent = 'In-House 2 Units:';
        trackTag.style.display = 'inline-block';
        trackTag.className = 'q-track-tag inhouse';
        trackTag.textContent = '🏠 Exam 2 In-House 2';
        timerDisplay.classList.add('inhouse');
        sidebarTitle.innerHTML = `<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg> In-House 2 Units (5)`;
      } else if (currentTrack === 'exam2_inhouse') {
        zenTray.style.display = 'flex';
        trayIcon.textContent = '🏠';
        trayLabelText.textContent = 'In-House Units:';
        trackTag.style.display = 'inline-block';
        trackTag.className = 'q-track-tag inhouse';
        trackTag.textContent = '🏠 Exam 2 In-House';
        timerDisplay.classList.add('inhouse');
        sidebarTitle.innerHTML = `<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg> In-House Units (5)`;
      } else if (currentTrack === 'exam2_sim') {
        zenTray.style.display = 'none';
        trackTag.style.display = 'inline-block';
        trackTag.className = 'q-track-tag exam2';
        trackTag.textContent = '🧠 Exam 2 Sim';
        timerDisplay.classList.add('exam2');
        sidebarTitle.innerHTML = `<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/></svg> Exam 2 Sections (9)`;
      } else if (currentTrack === 'exam2_zen' || currentTrack === 'exam2') {
        zenTray.style.display = 'flex';
        trayIcon.textContent = '🧘';
        trayLabelText.textContent = 'Exam 2 Units 1–6:';
        trackTag.style.display = 'inline-block';
        trackTag.className = 'q-track-tag exam2';
        trackTag.textContent = '🧘 Exam 2 Zen';
        timerDisplay.classList.add('exam2');
        sidebarTitle.innerHTML = `<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2a10 10 0 1 0 10 10A10 10 0 0 0 12 2zm0 18a8 8 0 1 1 8-8 8 8 0 0 1-8 8z"/></svg> Units 1–6 Topics (6)`;
      } else if (currentTrack === 'exam2_pdf_practice') {
        zenTray.style.display = 'flex';
        trayIcon.textContent = '🎯';
        trayLabelText.textContent = 'PDF Sections:';
        trackTag.style.display = 'inline-block';
        trackTag.className = 'q-track-tag exam2';
        trackTag.textContent = '🎯 PDF Practice';
        timerDisplay.classList.add('exam2');
        sidebarTitle.innerHTML = `<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 8v8"/><path d="M8 12h8"/></svg> PDF Sections (9)`;
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
      if (currentTrack === 'exam2_set3' || currentTrack === 'exam2_set2' || currentTrack === 'exam2_deep' || currentTrack === 'exam2_replicate' || currentTrack === 'exam2_inhouse2' || currentTrack === 'exam2_inhouse' || currentTrack === 'exam2_zen' || currentTrack === 'exam2' || currentTrack === 'exam2_pdf_practice' || currentTrack === 'inhouse' || currentTrack === 'focused_zen' || currentTrack === 'zen') {
        renderZenTray();
      }
      applyFilter();
      renderSidebarCategories();
      updateOverallStats();
      renderCurrentQuestion();

      const toastMsg = currentTrack === 'exam2_set3'
        ? 'Exam 2: Loaded 📚 Set 3 Step 1 Bank (150 Qs - Randomized)'
        : currentTrack === 'exam2_set2'
        ? 'Exam 2: Loaded 📑 Set 2 Step 1 Bank (100 Qs - Randomized)' 
        : currentTrack === 'exam2_deep'
        ? 'Exam 2: Loaded 🔬 Deep Step 1 Bank (150 Qs - Randomized)'
        : currentTrack === 'exam2_replicate'
        ? 'Exam 2: Loaded 🔄 Replicate Step 1 Bank (100 Qs - Randomized)'
        : currentTrack === 'exam2_inhouse2'
        ? 'Exam 2: Loaded 🏠 In-House Step 1 Bank 2 (275 Qs - Randomized)'
        : currentTrack === 'exam2_inhouse'
        ? 'Exam 2: Loaded 🏠 In-House Step 1 Bank (181 Qs)'
        : currentTrack === 'exam2_sim'
        ? 'Exam 2: Loaded 📝 Simulation Bank (103 Qs)'
        : (currentTrack === 'exam2_zen' || currentTrack === 'exam2')
        ? 'Exam 2: Loaded 🧘 Zen Mode Bank (315 Qs: Units 1–6)'
        : currentTrack === 'exam2_pdf_practice'
        ? 'Exam 2: Loaded 🎯 PDF Practice Bank (103 Qs)'
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

      if (currentTrack === 'exam2_set3') {
        storagePrefix = 'usmle_exam2_set3_';
        rawData = rawExam2Set3Questions;
      } else if (currentTrack === 'exam2_set2') {
        storagePrefix = 'usmle_exam2_set2_';
        rawData = rawExam2Set2Questions;
      } else if (currentTrack === 'exam2_deep') {
        storagePrefix = 'usmle_exam2_deep_';
        rawData = rawExam2DeepQuestions;
      } else if (currentTrack === 'exam2_replicate') {
        storagePrefix = 'usmle_exam2_replicate_';
        rawData = rawExam2ReplicateQuestions;
      } else if (currentTrack === 'exam2_inhouse2') {
        storagePrefix = 'usmle_exam2_inhouse2_';
        rawData = rawExam2InHouse2Questions;
      } else if (currentTrack === 'exam2_inhouse') {
        storagePrefix = 'usmle_exam2_inhouse_';
        rawData = rawExam2InHouseQuestions;
      } else if (currentTrack === 'exam2_sim') {
        storagePrefix = 'usmle_exam2_sim_';
        rawData = rawExam2Questions;
      } else if (currentTrack === 'exam2_zen' || currentTrack === 'exam2') {
        storagePrefix = 'usmle_exam2_zen_units1_3_';
        rawData = rawExam2ZenQuestions;
      } else if (currentTrack === 'exam2_pdf_practice') {
        storagePrefix = 'usmle_exam2_pdf_';
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
        source: q.source || '',
        high_yield_pearl: q.high_yield_pearl || '',
        index: idx
      }));

      // Auto-purge stale corrupted cache for Exam 2 Q46, Q19, Q35
      ['usmle_exam2_state', 'usmle_exam2_zen_state', 'usmle_exam2_sim_state'].forEach(key => {
        try {
          const raw = localStorage.getItem(key);
          if (raw && (raw.includes('menu in a dimly lit') || raw.includes('contralateral dorsal and'))) {
            const parsed = JSON.parse(raw);
            if (parsed) {
              delete parsed[46];
              delete parsed['46'];
              delete parsed[19];
              delete parsed['19'];
              delete parsed[35];
              delete parsed['35'];
              localStorage.setItem(key, JSON.stringify(parsed));
            }
          }
        } catch(e) {}
      });

      // Auto-migrate legacy Exam 2 answers so user never loses previous work
      try {
        const legacyExam2 = localStorage.getItem('usmle_exam2_state');
        if (legacyExam2) {
          if (!localStorage.getItem('usmle_exam2_sim_state')) {
            localStorage.setItem('usmle_exam2_sim_state', legacyExam2);
          }
          if (!localStorage.getItem('usmle_exam2_pdf_state')) {
            localStorage.setItem('usmle_exam2_pdf_state', legacyExam2);
          }
          const legacyIdx = localStorage.getItem('usmle_exam2_current_index');
          if (legacyIdx && !localStorage.getItem('usmle_exam2_sim_current_index')) {
            localStorage.setItem('usmle_exam2_sim_current_index', legacyIdx);
          }
        }
      } catch (e) {}

      userState = {};
      let saved = localStorage.getItem(storagePrefix + 'state');
      // For exam2_sim, if sim state is still empty, fallback to legacy usmle_exam2_state
      if (!saved && currentTrack === 'exam2_sim') {
        saved = localStorage.getItem('usmle_exam2_state');
      }
      if (!saved && (currentTrack === 'exam2_zen' || currentTrack === 'exam2')) {
        saved = localStorage.getItem('usmle_exam2_zen_units1_3_state') || localStorage.getItem('usmle_exam2_zen_state');
      }

      let restoredState = null;
      if (saved) {
        try { restoredState = JSON.parse(saved); } catch (e) {}
      }

      questions.forEach((q) => {
        const s = restoredState ? (restoredState[q.id] || restoredState[String(q.id)]) : null;
        if (s) {
          const validOptionTexts = new Set(q.options.map(o => (o.text || '').trim()));
          const hasOptionMismatch = !s.shuffledOptions || 
                                    s.shuffledOptions.length !== q.options.length ||
                                    !s.shuffledOptions.every(o => o && validOptionTexts.has((o.text || '').trim()));

          let chosenIdx = hasOptionMismatch ? null : s.selectedChoiceIndex;
          let restoredIsCorrect = hasOptionMismatch ? null : s.isCorrect;
          if (chosenIdx !== null && s.shuffledOptions && s.shuffledOptions[chosenIdx]) {
            restoredIsCorrect = (s.shuffledOptions[chosenIdx].is_correct === true);
          }

          let stemHtml = null;
          if (s.stemHtml) {
            // Strict check: only restore stemHtml if its plain text EXACTLY matches q.stem
            const tempDiv = document.createElement('div');
            tempDiv.innerHTML = s.stemHtml;
            const plainFromHtml = (tempDiv.textContent || tempDiv.innerText || '').trim().replace(/\s+/g, ' ');
            const plainFromQ = (q.stem || '').trim().replace(/\s+/g, ' ');
            if (plainFromHtml === plainFromQ) {
              stemHtml = s.stemHtml;
            }
          }

          userState[q.id] = {
            selectedChoiceIndex: chosenIdx,
            isCorrect: restoredIsCorrect,
            flagged: s.flagged || false,
            struckChoices: new Set(hasOptionMismatch ? [] : (s.struckChoices || [])),
            shuffledOptions: hasOptionMismatch ? (randomizeChoices ? shuffleArray(q.options) : [...q.options]) : s.shuffledOptions,
            stemHtml: stemHtml
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
      if (currentTrack === 'exam2_set3') storagePrefix = 'usmle_exam2_set3_';
      else if (currentTrack === 'exam2_set2') storagePrefix = 'usmle_exam2_set2_';
      else if (currentTrack === 'exam2_deep') storagePrefix = 'usmle_exam2_deep_';
      else if (currentTrack === 'exam2_replicate') storagePrefix = 'usmle_exam2_replicate_';
      else if (currentTrack === 'exam2_inhouse2') storagePrefix = 'usmle_exam2_inhouse2_';
      else if (currentTrack === 'exam2_inhouse') storagePrefix = 'usmle_exam2_inhouse_';
      else if (currentTrack === 'exam2_sim') storagePrefix = 'usmle_exam2_sim_';
      else if (currentTrack === 'exam2_zen' || currentTrack === 'exam2') storagePrefix = 'usmle_exam2_zen_units1_3_';
      else if (currentTrack === 'exam2_pdf_practice') storagePrefix = 'usmle_exam2_pdf_';
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

      // Mirror exam2_sim to legacy usmle_exam2_state for seamless compatibility
      if (currentTrack === 'exam2_sim') {
        localStorage.setItem('usmle_exam2_state', JSON.stringify(serializable));
        localStorage.setItem('usmle_exam2_current_index', currentIndex);
      }
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
      const catsToUse = getCategoriesForTrack();
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
      if (isAnswered || currentTrack === 'exam2_set3' || currentTrack === 'exam2_set2' || currentTrack === 'exam2_deep' || currentTrack === 'exam2_replicate' || currentTrack === 'exam2_inhouse2' || currentTrack === 'exam2_inhouse' || currentTrack === 'exam2_zen' || currentTrack === 'exam2' || currentTrack === 'inhouse' || currentTrack === 'focused_zen' || currentTrack === 'zen') {
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
        
        let expBodyHtml = `<div style="line-height: 1.6; color: var(--text-primary); font-size: 0.95rem;">${expText}</div>`;
        if (q.high_yield_pearl) {
          expBodyHtml += `
            <div style="margin-top: 14px; padding: 12px 14px; background: rgba(59, 130, 246, 0.08); border-left: 4px solid #3b82f6; border-radius: 6px;">
              <div style="font-weight: 700; margin-bottom: 4px; display: flex; align-items: center; gap: 6px; color: #1d4ed8; font-size: 0.88rem;">
                <span>💡</span> High-Yield Clinical Pearl
              </div>
              <div style="color: var(--text-primary); font-size: 0.9rem; line-height: 1.5;">${q.high_yield_pearl}</div>
            </div>
          `;
        }
        if (q.source) {
          expBodyHtml += `
            <div style="margin-top: 10px; font-size: 0.76rem; color: #6b7280; font-style: italic; display: flex; align-items: center; gap: 5px;">
              <span>📖</span> Reference: ${q.source}
            </div>
          `;
        }
        document.getElementById('explanationText').innerHTML = expBodyHtml;
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
      if (currentTrack === 'exam2_set3' || currentTrack === 'exam2_set2' || currentTrack === 'exam2_deep' || currentTrack === 'exam2_replicate' || currentTrack === 'exam2_inhouse2' || currentTrack === 'exam2_inhouse' || currentTrack === 'exam2_zen' || currentTrack === 'exam2' || currentTrack === 'exam2_pdf_practice' || currentTrack === 'inhouse' || currentTrack === 'focused_zen' || currentTrack === 'zen') {
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
      if (currentTrack === 'exam2_set3' || currentTrack === 'exam2_set2' || currentTrack === 'exam2_deep' || currentTrack === 'exam2_replicate' || currentTrack === 'exam2_inhouse2' || currentTrack === 'exam2_inhouse' || currentTrack === 'exam2_zen' || currentTrack === 'exam2' || currentTrack === 'exam2_pdf_practice' || currentTrack === 'inhouse' || currentTrack === 'focused_zen' || currentTrack === 'zen') {
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

      const catsToUse = getCategoriesForTrack();
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
        ? (currentTrack === 'exam2_set3'
            ? '📚 Exam 2 Set 3 (150 Qs) Score Report'
            : currentTrack === 'exam2_set2'
            ? '📑 Exam 2 Set 2 (100 Qs) Score Report' 
            : currentTrack === 'exam2_deep'
            ? '🔬 Exam 2 Deep (150 Qs) Score Report'
            : currentTrack === 'exam2_replicate'
            ? '🔄 Exam 2 Replicate (100 Qs) Score Report'
            : currentTrack === 'exam2_inhouse2'
            ? '🏠 Exam 2 In House 2 (275 Qs) Score Report'
            : currentTrack === 'exam2_inhouse'
            ? '🏠 Exam 2 In House (181 Qs) Score Report'
            : currentTrack === 'exam2_sim'
            ? '🧠 Exam 2 Simulation (103 Qs) Score Report'
            : currentTrack === 'exam2_zen'
            ? '🧘 Exam 2 Zen Mode (315 Qs) Score Report'
            : '🎯 Exam 2 Section Mastery (103 Qs) Score Report')
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
      if (currentTrack === 'exam2_set3') {
        trackName = '📚 Exam 2 Set 3 (150 questions)';
        storagePrefix = 'usmle_exam2_set3_';
      } else if (currentTrack === 'exam2_set2') {
        trackName = '📑 Exam 2 Set 2 (100 questions)';
        storagePrefix = 'usmle_exam2_set2_';
      } else if (currentTrack === 'exam2_deep') {
        trackName = '🔬 Exam 2 Deep (150 questions)';
        storagePrefix = 'usmle_exam2_deep_';
      } else if (currentTrack === 'exam2_replicate') {
        trackName = '🔄 Exam 2 Replicate (100 questions)';
        storagePrefix = 'usmle_exam2_replicate_';
      } else if (currentTrack === 'exam2_inhouse2') {
        trackName = '🏠 Exam 2 In House 2 (275 questions)';
        storagePrefix = 'usmle_exam2_inhouse2_';
      } else if (currentTrack === 'exam2_inhouse') {
        trackName = '🏠 Exam 2 In House (181 questions)';
        storagePrefix = 'usmle_exam2_inhouse_';
      } else if (currentTrack === 'exam2_sim') {
        trackName = '🧠 Exam 2 Simulation (103 questions)';
        storagePrefix = 'usmle_exam2_sim_';
      } else if (currentTrack === 'exam2_zen' || currentTrack === 'exam2') {
        trackName = '🧘 Exam 2 Zen Mode (315 questions)';
        storagePrefix = 'usmle_exam2_zen_units1_3_';
      } else if (currentTrack === 'exam2_pdf_practice') {
        trackName = '🎯 Exam 2 PDF Practice (103 questions)';
        storagePrefix = 'usmle_exam2_pdf_';
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
    
    /* ========================================================= */
    /* VAULT AUDIO SYNTHESIZER & AUTHENTICATION LOGIC           */
    /* ========================================================= */
    const VaultAudio = {
      ctx: null,
      clownTimer: null,

      phonkTimer: null,
      bdayTimer: null,
      startPhonkMusic() {
        this.init();
        if (!this.ctx) return;
        this.stopPhonkMusic();

        // Brazilian / drift phonk cowbell riff
        const riff = [
          { f: 739.99, d: 0.12, bass: 110 }, // F#5
          { f: 880.00, d: 0.12, bass: null }, // A5
          { f: 739.99, d: 0.12, bass: null }, // F#5
          { f: 659.25, d: 0.12, bass: null }, // E5
          { f: 739.99, d: 0.12, bass: 82 },   // F#5 + low E bass
          { f: 880.00, d: 0.12, bass: null }, // A5
          { f: 987.77, d: 0.24, bass: null }, // B5
          { f: 880.00, d: 0.12, bass: 110 }, // A5
          { f: 739.99, d: 0.12, bass: null }, // F#5
          { f: 659.25, d: 0.24, bass: null }, // E5
        ];

        let step = 0;
        const playStep = () => {
          if (!this.phonkTimer) return;
          const note = riff[step % riff.length];
          const now = this.ctx.currentTime;

          // Cowbell synth (square with fast decay)
          const osc = this.ctx.createOscillator();
          const gain = this.ctx.createGain();
          osc.type = 'square';
          osc.frequency.setValueAtTime(note.f, now);
          gain.gain.setValueAtTime(0.22, now);
          gain.gain.exponentialRampToValueAtTime(0.001, now + note.d * 0.85);
          osc.connect(gain);
          gain.connect(this.ctx.destination);
          osc.start(now);
          osc.stop(now + note.d);

          // 808 Sub-bass kick
          if (note.bass) {
            const bass = this.ctx.createOscillator();
            const bassGain = this.ctx.createGain();
            bass.type = 'sine';
            bass.frequency.setValueAtTime(note.bass, now);
            bass.frequency.exponentialRampToValueAtTime(35, now + 0.3);
            bassGain.gain.setValueAtTime(0.55, now);
            bassGain.gain.exponentialRampToValueAtTime(0.01, now + 0.3);
            bass.connect(bassGain);
            bassGain.connect(this.ctx.destination);
            bass.start(now);
            bass.stop(now + 0.3);
          }

          step++;
          this.phonkTimer = setTimeout(playStep, note.d * 1000);
        };
        this.phonkTimer = setTimeout(playStep, 20);
      },
      stopPhonkMusic() {
        if (this.phonkTimer) {
          clearTimeout(this.phonkTimer);
          this.phonkTimer = null;
        }
      },

      startBirthdayMusic() {
        this.init();
        if (!this.ctx) return;
        this.stopBirthdayMusic();

        // Happy Birthday to You melody
        const bdayMelody = [
          { f: 392.00, d: 0.25 }, // G4
          { f: 392.00, d: 0.25 }, // G4
          { f: 440.00, d: 0.5 },  // A4
          { f: 392.00, d: 0.5 },  // G4
          { f: 523.25, d: 0.5 },  // C5
          { f: 493.88, d: 0.8 },  // B4

          { f: 392.00, d: 0.25 }, // G4
          { f: 392.00, d: 0.25 }, // G4
          { f: 440.00, d: 0.5 },  // A4
          { f: 392.00, d: 0.5 },  // G4
          { f: 587.33, d: 0.5 },  // D5
          { f: 523.25, d: 0.8 },  // C5

          { f: 392.00, d: 0.25 }, // G4
          { f: 392.00, d: 0.25 }, // G4
          { f: 783.99, d: 0.5 },  // G5
          { f: 659.25, d: 0.5 },  // E5
          { f: 523.25, d: 0.5 },  // C5
          { f: 493.88, d: 0.5 },  // B4
          { f: 440.00, d: 0.8 },  // A4

          { f: 698.46, d: 0.25 }, // F5
          { f: 698.46, d: 0.25 }, // F5
          { f: 659.25, d: 0.5 },  // E5
          { f: 523.25, d: 0.5 },  // C5
          { f: 587.33, d: 0.5 },  // D5
          { f: 523.25, d: 1.0 }   // C5
        ];

        let step = 0;
        const playStep = () => {
          if (!this.bdayTimer) return;
          const note = bdayMelody[step % bdayMelody.length];
          const now = this.ctx.currentTime;
          const osc = this.ctx.createOscillator();
          const gain = this.ctx.createGain();
          osc.type = 'triangle';
          osc.frequency.setValueAtTime(note.f, now);
          gain.gain.setValueAtTime(0.24, now);
          gain.gain.exponentialRampToValueAtTime(0.01, now + note.d * 0.9);
          osc.connect(gain);
          gain.connect(this.ctx.destination);
          osc.start(now);
          osc.stop(now + note.d);

          step++;
          this.bdayTimer = setTimeout(playStep, note.d * 1000);
        };
        this.bdayTimer = setTimeout(playStep, 20);
      },
      stopBirthdayMusic() {
        if (this.bdayTimer) {
          clearTimeout(this.bdayTimer);
          this.bdayTimer = null;
        }
      },

      init() {
        if (!this.ctx) {
          const AC = window.AudioContext || window.webkitAudioContext;
          if (AC) this.ctx = new AC();
        }
        if (this.ctx && this.ctx.state === 'suspended') {
          this.ctx.resume();
        }
      },
      playClick() {
        this.init();
        if (!this.ctx) return;
        const now = this.ctx.currentTime;
        const osc = this.ctx.createOscillator();
        const gain = this.ctx.createGain();
        osc.type = 'triangle';
        osc.frequency.setValueAtTime(600, now);
        osc.frequency.exponentialRampToValueAtTime(120, now + 0.04);
        gain.gain.setValueAtTime(0.25, now);
        gain.gain.exponentialRampToValueAtTime(0.01, now + 0.04);
        osc.connect(gain);
        gain.connect(this.ctx.destination);
        osc.start(now);
        osc.stop(now + 0.04);
      },
      playUnlockSequence() {
        this.init();
        if (!this.ctx) return;
        const now = this.ctx.currentTime;
        [0, 0.07, 0.14, 0.21, 0.28].forEach((t, i) => {
          const osc = this.ctx.createOscillator();
          const gain = this.ctx.createGain();
          osc.type = 'sawtooth';
          osc.frequency.setValueAtTime(320 + i * 90, now + t);
          gain.gain.setValueAtTime(0.2, now + t);
          gain.gain.exponentialRampToValueAtTime(0.01, now + t + 0.05);
          osc.connect(gain);
          gain.connect(this.ctx.destination);
          osc.start(now + t);
          osc.stop(now + t + 0.05);
        });
        // Heavy bass vault clunk
        const bass = this.ctx.createOscillator();
        const bassGain = this.ctx.createGain();
        bass.type = 'sine';
        bass.frequency.setValueAtTime(110, now + 0.38);
        bass.frequency.exponentialRampToValueAtTime(30, now + 0.85);
        bassGain.gain.setValueAtTime(0.5, now + 0.38);
        bassGain.gain.exponentialRampToValueAtTime(0.01, now + 0.85);
        bass.connect(bassGain);
        bassGain.connect(this.ctx.destination);
        bass.start(now + 0.38);
        bass.stop(now + 0.85);
      },
      playBuzzer() {
        this.init();
        if (!this.ctx) return;
        const now = this.ctx.currentTime;
        const osc = this.ctx.createOscillator();
        const gain = this.ctx.createGain();
        osc.type = 'sawtooth';
        osc.frequency.setValueAtTime(130, now);
        osc.frequency.setValueAtTime(95, now + 0.16);
        gain.gain.setValueAtTime(0.4, now);
        gain.gain.linearRampToValueAtTime(0.01, now + 0.35);
        osc.connect(gain);
        gain.connect(this.ctx.destination);
        osc.start(now);
        osc.stop(now + 0.35);
      },
      playKaChing() {
        this.init();
        if (!this.ctx) return;
        const now = this.ctx.currentTime;
        // High dual bell chime
        const bell1 = this.ctx.createOscillator();
        const g1 = this.ctx.createGain();
        bell1.type = 'sine';
        bell1.frequency.setValueAtTime(987.77, now);
        g1.gain.setValueAtTime(0.4, now);
        g1.gain.exponentialRampToValueAtTime(0.001, now + 0.35);
        bell1.connect(g1);
        g1.connect(this.ctx.destination);
        bell1.start(now);
        bell1.stop(now + 0.35);

        const bell2 = this.ctx.createOscillator();
        const g2 = this.ctx.createGain();
        bell2.type = 'sine';
        bell2.frequency.setValueAtTime(1318.51, now + 0.1);
        g2.gain.setValueAtTime(0.5, now + 0.1);
        g2.gain.exponentialRampToValueAtTime(0.001, now + 0.75);
        bell2.connect(g2);
        g2.connect(this.ctx.destination);
        bell2.start(now + 0.1);
        bell2.stop(now + 0.75);
      },
      playFanfare() {
        this.init();
        if (!this.ctx) return;
        const now = this.ctx.currentTime;
        const notes = [
          { f: 261.63, t: 0, d: 0.18 },
          { f: 329.63, t: 0.2, d: 0.18 },
          { f: 392.00, t: 0.4, d: 0.22 },
          { f: 523.25, t: 0.65, d: 0.9 }
        ];
        notes.forEach(n => {
          [-3, 0, 3].forEach(det => {
            const osc = this.ctx.createOscillator();
            const gain = this.ctx.createGain();
            osc.type = 'sawtooth';
            osc.frequency.setValueAtTime(n.f, now + n.t);
            osc.detune.setValueAtTime(det, now + n.t);
            gain.gain.setValueAtTime(0.18, now + n.t);
            gain.gain.exponentialRampToValueAtTime(0.01, now + n.t + n.d);
            osc.connect(gain);
            gain.connect(this.ctx.destination);
            osc.start(now + n.t);
            osc.stop(now + n.t + n.d);
          });
        });
      },
      startClownMusic() {
        this.init();
        if (!this.ctx) return;
        this.stopClownMusic();

        // Entry of the Gladiators / circus march melody
        const melody = [
          { f: 587.33, d: 0.13 },
          { f: 554.37, d: 0.13 },
          { f: 587.33, d: 0.13 },
          { f: 622.25, d: 0.13 },
          { f: 659.25, d: 0.26 },
          { f: 587.33, d: 0.13 },
          { f: 523.25, d: 0.26 },
          { f: 493.88, d: 0.13 },
          { f: 440.00, d: 0.26 },
          { f: 415.30, d: 0.13 },
          { f: 440.00, d: 0.13 },
          { f: 466.16, d: 0.13 },
          { f: 493.88, d: 0.26 },
          { f: 587.33, d: 0.26 },
          { f: 523.25, d: 0.38 }
        ];

        let step = 0;
        const playStep = () => {
          if (!this.clownTimer) return;
          const note = melody[step % melody.length];
          const now = this.ctx.currentTime;
          const osc = this.ctx.createOscillator();
          const gain = this.ctx.createGain();
          osc.type = 'square';
          osc.frequency.setValueAtTime(note.f, now);
          gain.gain.setValueAtTime(0.16, now);
          gain.gain.exponentialRampToValueAtTime(0.01, now + note.d * 0.88);
          osc.connect(gain);
          gain.connect(this.ctx.destination);
          osc.start(now);
          osc.stop(now + note.d);

          step++;
          this.clownTimer = setTimeout(playStep, note.d * 1000);
        };

        this.clownTimer = setTimeout(playStep, 20);
      },
      stopClownMusic() {
        if (this.clownTimer) {
          clearTimeout(this.clownTimer);
          this.clownTimer = null;
        }
      }
    };

    let palaceCountdownTimer = null;

    function handleSafeUnlock() {
      const nameInput = document.getElementById('safeNameInput');
      const pwdInput = document.getElementById('safePasswordInput');
      const name = (nameInput ? nameInput.value : '').trim().toLowerCase();
      const pwd = (pwdInput ? pwdInput.value : '').trim().toLowerCase();

      // Check Condition 0A: password is tyler OR name is tyler -> Happy Birthday Tyler
      if (pwd === 'tyler' || name === 'tyler') {
        triggerBirthdayTyler();
        return;
      }

      // Check Condition 0B: name is mark (or password is mark) -> Mark Mogs
      if (name === 'mark' || pwd === 'mark') {
        triggerMarkMog();
        return;
      }

      if (!name) {
        showSafeStatus('Please enter your name.', 'error');
        return;
      }

      // Check Condition 1: ryan -> Clown Troll (will/william commented out)
      // if (name === 'will' || name === 'william' || pwd === 'will' || pwd === 'william') { triggerClownTakeover(); return; }
      if (name === 'ryan' || pwd === 'ryan') {
        triggerClownTakeover();
        return;
      }

      // Check Condition 2: jacob -> You owe me a dollar terms
      if (name === 'jacob' || pwd === 'jacob') {
        triggerJacobDebt();
        return;
      }

      // Check Condition 3: name is marlon -> Golden Palace (marlon password removed)
      if (name === 'marlon') {
        triggerGoldenPalace();
        return;
      }

      // Check Condition 4: nick or alex -> Direct Entry
      if (name === 'nick' || name === 'alex' || pwd === 'nick' || pwd === 'alex') {
        triggerDirectUnlock(name || pwd);
        return;
      }

      // Any other name -> Access Denied
      VaultAudio.playBuzzer();
      const led = document.getElementById('terminalLed');
      if (led) {
        led.className = 'terminal-led error';
        setTimeout(() => { if (led) led.className = 'terminal-led'; }, 1500);
      }
      showSafeStatus('Access Denied: Unrecognized operative name.', 'error');
      
      const card = document.getElementById('vaultTerminalCard');
      if (card) {
        card.style.animation = 'none';
        card.offsetHeight; // trigger reflow
        card.style.animation = 'clownWiggle 0.4s ease-in-out';
      }
    }

    function showSafeStatus(text, type) {
      const msg = document.getElementById('safeStatusMsg');
      if (!msg) return;
      if (!text) {
        msg.style.display = 'none';
        msg.textContent = '';
        msg.className = 'vault-msg';
        return;
      }
      msg.style.display = 'block';
      msg.textContent = text;
      msg.className = 'vault-msg ' + (type || 'error');
    }

    
    /* Condition 0: Mark Mogs */
    function triggerMarkMog() {
      const overlay = document.getElementById('safeVaultOverlay');
      const mog = document.getElementById('markMogScreen');
      if (overlay) overlay.style.display = 'none';
      if (mog) mog.style.display = 'flex';
      VaultAudio.startPhonkMusic();
    }

    function enterFromMog() {
      VaultAudio.stopPhonkMusic();
      const mog = document.getElementById('markMogScreen');
      if (mog) mog.style.display = 'none';
      executeUnlockExam('mark');
      showToast('🤫🧏‍♂️ Mark has entered. Server mogging in progress.');
    }

    /* Condition: Happy Birthday Tyler */
    function triggerBirthdayTyler() {
      const overlay = document.getElementById('safeVaultOverlay');
      const bday = document.getElementById('tylerBdayScreen');
      if (overlay) overlay.style.display = 'none';
      if (bday) bday.style.display = 'flex';
      VaultAudio.startBirthdayMusic();
    }

    function enterFromBirthday() {
      VaultAudio.stopBirthdayMusic();
      const bday = document.getElementById('tylerBdayScreen');
      if (bday) bday.style.display = 'none';
      executeUnlockExam('tyler');
      showToast('🎂 Happy Birthday Tyler! Exam unlocked.');
    }

    /* Condition 1: Clown Troll */
    function triggerClownTakeover() {
      const overlay = document.getElementById('safeVaultOverlay');
      const clown = document.getElementById('clownTakeoverScreen');
      if (overlay) overlay.style.display = 'none';
      if (clown) clown.style.display = 'flex';
      VaultAudio.startClownMusic();
    }

    function exitClownTakeover() {
      VaultAudio.stopClownMusic();
      const clown = document.getElementById('clownTakeoverScreen');
      const overlay = document.getElementById('safeVaultOverlay');
      if (clown) clown.style.display = 'none';
      if (overlay) {
        overlay.style.display = 'flex';
        showSafeStatus('Access Denied: Please enter a valid operative name.', 'error');
      }
    }

    /* Condition 2: Jacob Debt */
    function triggerJacobDebt() {
      const overlay = document.getElementById('safeVaultOverlay');
      const debt = document.getElementById('jacobDebtScreen');
      if (overlay) overlay.style.display = 'none';
      if (debt) debt.style.display = 'flex';
    }

    function acceptJacobTerms() {
      VaultAudio.playKaChing();
      const debtCard = document.getElementById('debtContractCard');
      if (debtCard) {
        debtCard.innerHTML = `
          <div class="debt-seal">✅</div>
          <div class="debt-title" style="color: #6ee7b7;">Terms Accepted!</div>
          <div class="debt-balance-highlight" style="font-size: 24px; color: #a7f3d0;">$1.00 Debt Confirmed to Mark</div>
          <div class="debt-terms-box" style="text-align: center;">
            Thank you, Jacob. Payment agreement officially registered in the vault ledger.<br>
            <strong>Unlocking Neuro Exam 2...</strong>
          </div>
        `;
      }
      setTimeout(() => {
        const debt = document.getElementById('jacobDebtScreen');
        if (debt) debt.style.display = 'none';
        executeUnlockExam('jacob');
      }, 1600);
    }

    function dodgeDeclineBtn() {
      const btn = document.getElementById('declineDebtBtn');
      if (!btn) return;
      VaultAudio.playClick();
      const x = (Math.random() - 0.5) * 120;
      const y = (Math.random() - 0.5) * 80;
      btn.style.transform = `translate(${x}px, ${y}px)`;
      btn.textContent = "Can't Decline!";
      setTimeout(() => {
        btn.textContent = "❌ Decline";
      }, 1200);
    }

    /* Condition 3: Golden Palace (Marlon) */
    function triggerGoldenPalace() {
      const overlay = document.getElementById('safeVaultOverlay');
      const palace = document.getElementById('goldenPalaceScreen');
      if (overlay) overlay.style.display = 'none';
      if (palace) palace.style.display = 'flex';
      VaultAudio.playFanfare();

      let seconds = 3;
      const btn = document.getElementById('enterPalaceBtn');
      if (btn) btn.textContent = `👑 ENTER THE THRONE ROOM (${seconds}s)`;

      if (palaceCountdownTimer) clearInterval(palaceCountdownTimer);
      palaceCountdownTimer = setInterval(() => {
        seconds--;
        if (btn) btn.textContent = `👑 ENTER THE THRONE ROOM (${seconds}s)`;
        if (seconds <= 0) {
          clearInterval(palaceCountdownTimer);
          enterFromPalace();
        }
      }, 1000);
    }

    function enterFromPalace() {
      if (palaceCountdownTimer) clearInterval(palaceCountdownTimer);
      const palace = document.getElementById('goldenPalaceScreen');
      if (palace) palace.style.display = 'none';
      executeUnlockExam('marlon');
    }

    /* Condition 4: Direct Unlock (Nick / Alex) */
    function triggerDirectUnlock(name) {
      const led = document.getElementById('terminalLed');
      if (led) led.className = 'terminal-led success';
      showSafeStatus(`Clearance Confirmed. Welcome, ${name.toUpperCase()}!`, 'success');
      
      const wheel = document.getElementById('vaultWheel');
      if (wheel) wheel.className = 'vault-wheel spinning';
      
      VaultAudio.playUnlockSequence();
      
      setTimeout(() => {
        executeUnlockExam(name);
      }, 1100);
    }

    /* Final execution of unlock */
    function executeUnlockExam(userName) {
      sessionStorage.setItem('usmle_vault_unlocked', 'true');
      sessionStorage.setItem('usmle_vault_user', userName || 'operative');

      const wheel = document.getElementById('vaultWheel');
      if (wheel) wheel.className = 'vault-wheel spinning';

      const overlay = document.getElementById('safeVaultOverlay');
      if (overlay) {
        overlay.classList.add('unlocked');
        setTimeout(() => {
          overlay.style.display = 'none';
        }, 600);
      }

      showToast(`🔓 Vault Unlocked. Welcome, ${(userName || '').toUpperCase()}!`);
    }

    function lockVault() {
      sessionStorage.removeItem('usmle_vault_unlocked');
      const overlay = document.getElementById('safeVaultOverlay');
      if (overlay) {
        overlay.classList.remove('unlocked');
        overlay.style.display = 'flex';
      }
      const wheel = document.getElementById('vaultWheel');
      if (wheel) wheel.className = 'vault-wheel';
      const nameInput = document.getElementById('safeNameInput');
      if (nameInput) nameInput.value = '';
      const pwdInput = document.getElementById('safePasswordInput');
      if (pwdInput) pwdInput.value = '';
      showSafeStatus('', '');
      showToast('🔒 Vault Locked.');
    }

    function checkVaultAccessOnLoad() {
      // Always purge stored unlock state so every reload requires login
      sessionStorage.removeItem('usmle_vault_unlocked');
      localStorage.removeItem('usmle_vault_unlocked');

      const urlParams = new URLSearchParams(window.location.search);
      if (urlParams.has('name') || urlParams.has('pwd')) {
        if (urlParams.has('name')) {
          const testName = urlParams.get('name');
          const nameInput = document.getElementById('safeNameInput');
          if (nameInput) nameInput.value = testName;
        }
        if (urlParams.has('pwd')) {
          const pwdInput = document.getElementById('safePasswordInput');
          if (pwdInput) pwdInput.value = urlParams.get('pwd');
        }
        handleSafeUnlock();
        return;
      }

      // Always require safe unlock on every reload
      const overlay = document.getElementById('safeVaultOverlay');
      if (overlay) {
        overlay.classList.remove('unlocked');
        overlay.style.display = 'flex';
      }
      const wheel = document.getElementById('vaultWheel');
      if (wheel) wheel.className = 'vault-wheel';
      const nameInput = document.getElementById('safeNameInput');
      if (nameInput) {
        nameInput.value = '';
        setTimeout(() => nameInput.focus(), 100);
      }
      const pwdInput = document.getElementById('safePasswordInput');
      if (pwdInput) pwdInput.value = '';
      showSafeStatus('', '');
    }

    window.addEventListener('DOMContentLoaded', () => {
      checkVaultAccessOnLoad();
      const savedTheme = localStorage.getItem('usmle_exam_theme');
      if (savedTheme) {
        document.body.setAttribute('data-theme', savedTheme);
      }

      setupAutoHighlighting();
      startTimer();

      // Restore active exam & track
      const urlParams = new URLSearchParams(window.location.search);
      const urlExam = urlParams.get('exam');
      const urlTrack = urlParams.get('track');

      const savedExam = urlExam || localStorage.getItem('usmle_active_exam') || 'exam1';
      let targetTrack = urlTrack || localStorage.getItem('usmle_active_track');
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
            ? (currentTrack === 'exam2_set3' ? 'Exam 2 Set 3' : currentTrack === 'exam2_set2' ? 'Exam 2 Set 2' : currentTrack === 'exam2_deep' ? 'Exam 2 Deep' : currentTrack === 'exam2_replicate' ? 'Exam 2 Replicate' : currentTrack === 'exam2_inhouse2' ? 'Exam 2 In-House 2' : currentTrack === 'exam2_inhouse' ? 'Exam 2 In-House' : currentTrack === 'exam2_sim' ? 'Exam 2 Sim' : 'Exam 2 Zen')
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
