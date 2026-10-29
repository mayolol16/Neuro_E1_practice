#!/usr/bin/env python3
import json
import os
import re
import random
import shutil

import p150_overrides

print("=== Building Clean & Randomized Exam 2 'Set 3' Bank (150 Qs) ===")

CATEGORY_MAP = {
    'Visual System': 'Visual System',
    'Visual Reflexes': 'Visual Reflexes',
    'Ophthalmology': 'Ophthalmology',
    'Auditory & Vestibular System': 'Auditory & Vestibular System',
    'Auditory & Vestibular': 'Auditory & Vestibular System',
    'UMN / LMN': 'UMN / LMN',
    'Hypothalamus & Smell/Taste': 'Hypothalamus, Smell & Taste',
    'Basal Ganglia': 'Basal Ganglia',
    'CBIL – Sleep': 'Sleep & Sleep Disorders',
    'CBIL – ALS': 'Amyotrophic Lateral Sclerosis (ALS)'
}

md_path = "/Users/markyoussef_1/Downloads/Neuro E2 – USMLE Step 1 Practice Questions (150).md"
with open(md_path, "r", encoding="utf-8") as f:
    text = f.read()

raw_sections = re.split(r'\n## ', text)[1:]
cleaned_questions = []

for s in raw_sections:
    sec_title = s.split('\n')[0].strip()
    clean_cat = None
    for k, v in CATEGORY_MAP.items():
        if k in sec_title:
            clean_cat = v
            break
            
    parts = re.split(r'\n### Answer key[^\n]*\n', s)
    q_part, a_part = parts[0], parts[1]
    
    ans_dict = {}
    for match in re.finditer(r'\*\*(\d+)\.\s*([A-E])\*\*\s*[–—-]\s*(.*?)(?=\n\*\*\d+\.|\Z)', a_part, re.DOTALL):
        ans_dict[int(match.group(1))] = (match.group(2).strip(), match.group(3).strip())
        
    q_matches = list(re.finditer(r'\*\*(\d+)\.\*\s*(.*?)(?=\n\*\*|\Z)', q_part, re.DOTALL))
    for qm in q_matches:
        q_num = int(qm.group(1))
        block = qm.group(2).strip()
        opt_matches = list(re.finditer(r'-\s*([A-E])\.\s*(.*?)(?=\n-\s*[A-E]\.|\Z)', block, re.DOTALL))
        stem = block[:opt_matches[0].start()].strip()
        stem = re.sub(r'^\*\s*', '', stem).strip()
        options = {om.group(1): om.group(2).strip() for om in opt_matches}
        corr, exp = ans_dict[q_num]
        
        if q_num in p150_overrides.P150_OVERRIDES:
            ov = p150_overrides.P150_OVERRIDES[q_num]
            if 'stem' in ov:
                stem = ov['stem']
            if 'options' in ov:
                options = ov['options'].copy()
            if 'correct_answer' in ov:
                corr = ov['correct_answer']
            if 'explanation' in ov:
                exp = ov['explanation']
                
        pearl = f"High-Yield Rule: {options.get(corr, '')}"
        cleaned_questions.append({
            'category': clean_cat,
            'q_num': q_num,
            'stem': stem,
            'options': options,
            'correct_answer': corr,
            'explanation': exp,
            'high_yield_pearl': pearl,
            'source': f"USMLE Step 1 Set 3: {clean_cat}"
        })

print(f"Loaded and cleaned {len(cleaned_questions)} questions from Set 3.")

# Automated Quality & Bias Audit
audit_flags = []
for idx, q in enumerate(cleaned_questions):
    c_letter = q['correct_answer']
    c_opt = q['options'].get(c_letter, '')
    distractors = [v for k, v in q['options'].items() if k != c_letter]
    len_c = len(c_opt)
    lens_d = [len(d) for d in distractors]
    avg_d = sum(lens_d) / len(lens_d) if lens_d else 1
    max_d = max(lens_d) if lens_d else 1
    min_d = min(lens_d) if lens_d else 1
    ratio = len_c / avg_d
    
    issues = []
    if ratio > 1.45 and len_c > max_d + 15:
        issues.append(f"noticeably longer (ratio={ratio:.2f}, {len_c} vs avg {avg_d:.1f})")
    elif ratio < 0.65 and len_c < min_d - 15:
        issues.append(f"noticeably shorter (ratio={ratio:.2f}, {len_c} vs avg {avg_d:.1f})")
        
    corr_has_paren = '(' in c_opt and ')' in c_opt
    dist_with_paren = sum(1 for d in distractors if '(' in d and ')' in d)
    if corr_has_paren and dist_with_paren == 0:
        issues.append(f"correct answer has parens while NO distractors do: {c_opt}")
    elif not corr_has_paren and dist_with_paren == len(distractors):
        issues.append("all distractors have parens while correct answer does not")
    elif '(' in c_opt or dist_with_paren > 0:
        if 0 < dist_with_paren + (1 if corr_has_paren else 0) < len(q['options']):
            issues.append(f"inconsistent parentheses usage ({dist_with_paren + (1 if corr_has_paren else 0)}/{len(q['options'])})")
            
    if re.search(r'(question\s+\d+|above\s+patient|previous\s+patient|same\s+patient|referring\s+to)', q['stem'], re.IGNORECASE):
        issues.append(f"cross-reference stem: {q['stem'][:50]}")
        
    if issues:
        audit_flags.append((q['category'], q['q_num'], issues, c_letter, c_opt))

print(f"\nAudit completed. Flags found: {len(audit_flags)}")
if audit_flags:
    for cat, qnum, iss, c_l, c_o in audit_flags:
        print(f"FLAG [Q{qnum} {cat}] ({c_l}): {c_o} -> {iss}")
    raise ValueError(f"Audit failed with {len(audit_flags)} flags!")

print("All 150 questions PASSED the bias and giveaway audit with 0 flags!\n")

cat_counts = {}
for q in cleaned_questions:
    cat_counts[q['category']] = cat_counts.get(q['category'], 0) + 1
print("Category Breakdown (Set 3 - 150 Qs):")
for cat, cnt in sorted(cat_counts.items()):
    print(f"  - {cat}: {cnt} Qs")

# Randomize question order across All Topics using deterministic seed 42
rng = random.Random(42)
shuffled_questions = cleaned_questions.copy()
rng.shuffle(shuffled_questions)

for i, q in enumerate(shuffled_questions):
    q['id'] = f"set3_{i+1}"
    q['index'] = i

# Save JSON
out_json_path = "/Users/markyoussef_1/.gemini/antigravity-ide/scratch/usmle_exam1/exam2_set3_questions.json"
with open(out_json_path, "w", encoding="utf-8") as f:
    json.dump(shuffled_questions, f, indent=2)
print(f"\nSaved clean questions JSON to: {out_json_path}")

# Review Markdown
review_md_path = "/Users/markyoussef_1/.gemini/antigravity-ide/scratch/usmle_exam1/exam2_set3_questions_review.md"
with open(review_md_path, "w", encoding="utf-8") as f:
    f.write("# USMLE Step 1 - Exam 2 'Set 3' Bank (150 Questions)\n\n")
    f.write("Full audit completed. All option length biases, asymmetric parentheses, and giveaway punctuation removed.\n\n")
    f.write(f"Randomized across All Topics with 9 category filters. Total questions: {len(shuffled_questions)}\n\n")
    f.write("### Category Breakdown:\n")
    for cat, cnt in sorted(cat_counts.items()):
        f.write(f"- **{cat}**: {cnt} Questions\n")
    f.write("\n---\n\n")
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
    shutil.copy(out_json_path, os.path.join(usmle_exam2_dir, "exam2_set3_questions.json"))
    shutil.copy(review_md_path, os.path.join(usmle_exam2_dir, "exam2_set3_questions_review.md"))
    print(f"Copied clean JSON & review doc to: {usmle_exam2_dir}")

print("=== Build Completed Successfully with 0 Flags ===")

