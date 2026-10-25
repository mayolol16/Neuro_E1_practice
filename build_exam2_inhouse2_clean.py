#!/usr/bin/env python3
import json, os, random, re, shutil
import build_m2_solutions
import build_other_modules_overrides

print("=== Building Clean & Randomized Exam 2 In-House 2 Bank (275 Qs) ===")

raw_path = '/Users/markyoussef_1/.gemini/antigravity-ide/scratch/usmle_exam1/raw_temp_questions.json'
with open(raw_path, 'r', encoding='utf-8') as f:
    raw_data = json.load(f)

print(f"Loaded {len(raw_data)} raw questions from {raw_path}")

cleaned_questions = []

for q in raw_data:
    mod = q['module']
    qnum = q['q_num']
    key = f'{mod}_{qnum}'
    
    if mod == 'Visual Reflexes':
        sol = build_m2_solutions.M2_SOLUTIONS[qnum]
        ans = sol['ans']
        opts = sol['opts']
        expl = sol['explanation']
        pearl = sol['high_yield_pearl']
        stem = q['stem']
        if qnum == 55:
            stem = 'An anatomical study reviews the cavernous sinus. Which of the following groups of cranial nerves and associated vascular structures passes through or within the cavernous sinus?'
    else:
        ans = q['correct_answer']
        opts = q['options'].copy()
        expl = q['explanation']
        pearl = f'High-Yield Point: {opts.get(ans, "")}'
        stem = q['stem']
        
        if key in build_other_modules_overrides.OTHER_OVERRIDES:
            ov = build_other_modules_overrides.OTHER_OVERRIDES[key]
            if 'opts' in ov:
                opts = ov['opts']
            if 'ans' in ov:
                ans = ov['ans']
            if 'expl' in ov:
                expl = ov['expl']
            if 'stem' in ov:
                stem = ov['stem']
            if 'pearl' in ov:
                pearl = ov['pearl']
                
    cleaned_questions.append({
        'category': mod,
        'q_num': qnum,
        'stem': stem,
        'options': opts,
        'correct_answer': ans,
        'explanation': expl,
        'high_yield_pearl': pearl,
        'source': f'In-House Step 1 Bank 2: {mod}'
    })

# Automated Quality & Bias Audit
audit_flags = []
for idx, q in enumerate(cleaned_questions):
    c_letter = q['correct_answer']
    c_opt = q['options'].get(c_letter, '')
    distractors = [v for k, v in q['options'].items() if k != c_letter]
    len_c = len(c_opt)
    lens_d = [len(d) for d in distractors]
    avg_d = sum(lens_d) / len(lens_d) if lens_d else 1
    ratio = len_c / avg_d
    
    issues = []
    if ratio > 1.65 or ratio < 0.60:
        issues.append(f'length ratio={ratio:.2f} ({len_c} vs {avg_d:.1f})')
    if '(' in c_opt and not all('(' in d for d in distractors):
        issues.append('asymmetric parens in correct answer')
    if not '(' in c_opt and any('(' in d for d in distractors):
        if sum(1 for d in distractors if '(' in d) == 1:
            issues.append('single distractor paren')
    if ';' in c_opt and not all(';' in d for d in distractors):
        issues.append('asymmetric semicolon')
    if any(k in c_opt.lower() for k in ['due to', 'which is', 'all of the above', 'none of the above']):
        issues.append('giveaway phrasing')
        
    if issues:
        audit_flags.append((q['category'], q['q_num'], issues, c_letter, c_opt))

print(f"Audit completed. Flags found: {len(audit_flags)}")
if audit_flags:
    for cat, qnum, iss, c_l, c_o in audit_flags:
        print(f"FLAG [{cat} Q{qnum}] ({c_l}): {c_o} -> {iss}")
    raise ValueError(f"Audit failed with {len(audit_flags)} flags!")

# Randomize the question order across all topics using fixed seed
rng = random.Random(42)
shuffled_questions = cleaned_questions.copy()
rng.shuffle(shuffled_questions)

for i, q in enumerate(shuffled_questions):
    q['id'] = f'q_{i+1}'
    q['index'] = i

print(f"Shuffled {len(shuffled_questions)} questions across all 5 modules with seed=42.")

# Output JSON
out_json_path = '/Users/markyoussef_1/.gemini/antigravity-ide/scratch/usmle_exam1/exam2_inhouse2_questions.json'
with open(out_json_path, 'w', encoding='utf-8') as f:
    json.dump(shuffled_questions, f, indent=2, ensure_ascii=False)
print(f"Saved clean questions JSON to: {out_json_path}")

# Output Markdown Review Document
out_md_path = '/Users/markyoussef_1/.gemini/antigravity-ide/scratch/usmle_exam1/exam2_inhouse2_questions_review.md'
with open(out_md_path, 'w', encoding='utf-8') as f:
    f.write("# Exam 2: In-House Step 1 Bank 2 (275 Questions - Randomized)\n\n")
    f.write("All questions have been audited and cleaned for option length parity, eliminated giveaway parentheticals/punctuation, and randomized across all 5 modules.\n\n")
    f.write("### Category Summary\n")
    counts = {}
    for q in shuffled_questions:
        counts[q['category']] = counts.get(q['category'], 0) + 1
    for cat, cnt in counts.items():
        f.write(f"- **{cat}**: {cnt} questions\n")
    f.write(f"\n**Total Questions**: {len(shuffled_questions)}\n\n---\n\n")
    
    for q in shuffled_questions:
        f.write(f"## Question {q['index'] + 1} of {len(shuffled_questions)}\n")
        f.write(f"**Topic**: `{q['category']}` | **Original Unit Q#**: `Q{q['q_num']}`\n\n")
        f.write(f"{q['stem']}\n\n")
        for l, opt in sorted(q['options'].items()):
            marker = " ✅" if l == q['correct_answer'] else ""
            f.write(f"- **({l})** {opt}{marker}\n")
        f.write(f"\n**Correct Answer**: **({q['correct_answer']})**\n\n")
        f.write(f"**Explanation**: {q['explanation']}\n\n")
        f.write(f"**High-Yield Pearl**: {q['high_yield_pearl']}\n\n")
        f.write("---\n\n")

print(f"Saved review markdown to: {out_md_path}")

# Also copy both files to scratch/usmle_exam2
e2_dir = '/Users/markyoussef_1/.gemini/antigravity-ide/scratch/usmle_exam2'
if os.path.isdir(e2_dir):
    shutil.copy(out_json_path, os.path.join(e2_dir, 'exam2_inhouse2_questions.json'))
    shutil.copy(out_md_path, os.path.join(e2_dir, 'exam2_inhouse2_questions_review.md'))
    print(f"Copied clean JSON & review doc to: {e2_dir}")

print("=== Build Completed Successfully with 0 Flags ===")
