#!/usr/bin/env python3
import json
import os
import random
import shutil
import set2_overrides

print("=== Building Clean & Randomized Exam 2 'Set 2' Bank (100 Qs) ===")

raw_path = "/Users/markyoussef_1/.gemini/antigravity-ide/scratch/usmle_exam1/raw_set2_questions.json"
with open(raw_path, "r", encoding="utf-8") as f:
    raw_data = json.load(f)

print(f"Loaded {len(raw_data)} raw Set 2 questions.")

CATEGORY_MAP = {
    'Visual System': 'Visual System',
    'Visual Reflexes': 'Visual Reflexes',
    'Ophthalmology': 'Ophthalmology',
    'Auditory & Vestibular System': 'Auditory & Vestibular System',
    'UMN/LMN': 'UMN / LMN',
    'Hypothalamus & Smell/Taste': 'Hypothalamus, Smell & Taste',
    'Basal Ganglia': 'Basal Ganglia',
    'CBIL: Sleep': 'Sleep & Sleep Disorders',
    'CBIL: ALS': 'Amyotrophic Lateral Sclerosis (ALS)'
}

cleaned_questions = []

for q in raw_data:
    qnum = q['q_num']
    raw_cat = q['category']
    cat = CATEGORY_MAP.get(raw_cat, raw_cat)
    stem = q['stem']
    opts = q['options'].copy()
    c_ans = q['correct_answer']
    expl = q['explanation']
    
    if qnum in set2_overrides.SET2_OVERRIDES:
        ov = set2_overrides.SET2_OVERRIDES[qnum]
        if 'opts' in ov:
            opts = ov['opts'].copy()
        if 'stem' in ov:
            stem = ov['stem']
        if 'ans' in ov:
            c_ans = ov['ans']
        if 'expl' in ov:
            expl = ov['expl']
            
    pearl = f"High-Yield Rule: {opts.get(c_ans, '')}"
    
    cleaned_questions.append({
        'category': cat,
        'q_num': qnum,
        'stem': stem,
        'options': opts,
        'correct_answer': c_ans,
        'explanation': expl,
        'high_yield_pearl': pearl,
        'source': f"USMLE Step 1 Set 2: {cat}"
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
    if ratio > 1.55 or ratio < 0.65:
        issues.append(f"length ratio={ratio:.2f} ({len_c} vs {avg_d:.1f})")
    if '(' in c_opt and not all('(' in d for d in distractors):
        issues.append("asymmetric parens in correct answer")
    if not '(' in c_opt and any('(' in d for d in distractors):
        if sum(1 for d in distractors if '(' in d) == 1:
            issues.append("single distractor paren")
    if ';' in c_opt and not all(';' in d for d in distractors):
        issues.append("asymmetric semicolon")
    if any(k in c_opt.lower() for k in ['due to', 'which is', 'all of the above', 'none of the above']):
        issues.append("giveaway phrasing")
        
    if issues:
        audit_flags.append((q['category'], q['q_num'], issues, c_letter, c_opt))

print(f"\nAudit completed. Flags found: {len(audit_flags)}")
if audit_flags:
    for cat, qnum, iss, c_l, c_o in audit_flags:
        print(f"FLAG [Q{qnum} {cat}] ({c_l}): {c_o} -> {iss}")
    raise ValueError(f"Audit failed with {len(audit_flags)} flags!")

print("All 100 questions PASSED the bias and giveaway audit with 0 flags!\n")

# Randomize question order across All Topics using fixed seed 42
rng = random.Random(42)
shuffled_questions = cleaned_questions.copy()
rng.shuffle(shuffled_questions)

for i, q in enumerate(shuffled_questions):
    q['id'] = f"set2_{i+1}"
    q['index'] = i

# Category transition count
cats = [q['category'] for q in shuffled_questions]
transitions = sum(1 for i in range(len(cats)-1) if cats[i] != cats[i+1])
print(f"Randomized {len(shuffled_questions)} questions across all 9 units (transitions={transitions}).")

# Save JSON
out_json_path = "/Users/markyoussef_1/.gemini/antigravity-ide/scratch/usmle_exam1/exam2_set2_questions.json"
with open(out_json_path, "w", encoding="utf-8") as f:
    json.dump(shuffled_questions, f, indent=2)
print(f"Saved clean questions JSON to: {out_json_path}")

# Generate review markdown
review_md_path = "/Users/markyoussef_1/.gemini/antigravity-ide/scratch/usmle_exam1/exam2_set2_questions_review.md"
with open(review_md_path, "w", encoding="utf-8") as f:
    f.write("# USMLE Step 1 - Exam 2 'Set 2' Bank (100 Questions)\n\n")
    f.write("Full audit completed. All option length biases, asymmetric parentheses, and giveaway punctuation removed.\n\n")
    f.write(f"Randomized across All Topics with 9 category filters. Total questions: {len(shuffled_questions)}\n\n---\n\n")
    for q in shuffled_questions:
        f.write(f"### Question {q['index']+1} (Original Q{q['q_num']}) — {q['category']}\n\n")
        f.write(f"**Stem:** {q['stem']}\n\n")
        for k in sorted(q['options'].keys()):
            marker = "**(Correct)**" if k == q['correct_answer'] else ""
            f.write(f"- **{k})** {q['options'][k]} {marker}\n")
        f.write(f"\n**Explanation:** {q['explanation']}\n\n")
        f.write(f"*{q['high_yield_pearl']}*\n\n---\n\n")

print(f"Saved review markdown to: {review_md_path}")

# Copy to usmle_exam2 scratch as well
usmle_exam2_dir = "/Users/markyoussef_1/.gemini/antigravity-ide/scratch/usmle_exam2"
if os.path.exists(usmle_exam2_dir):
    shutil.copy(out_json_path, os.path.join(usmle_exam2_dir, "exam2_set2_questions.json"))
    shutil.copy(review_md_path, os.path.join(usmle_exam2_dir, "exam2_set2_questions_review.md"))
    print(f"Copied clean JSON & review doc to: {usmle_exam2_dir}")

print("=== Build Completed Successfully with 0 Flags ===")
