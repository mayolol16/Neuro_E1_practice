#!/usr/bin/env python3
import json
import os
import re
import random
import shutil

import set2_overrides
import p150_overrides

print("=== Building Clean & Randomized Exam 2 'Set 2' Combined Bank (250 Qs) ===")

CATEGORY_MAP_P1 = {
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

CATEGORY_MAP_P2 = {
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

# --- Part 1: Ingest 100 Qs from first set ---
raw_path_1 = "/Users/markyoussef_1/.gemini/antigravity-ide/scratch/usmle_exam1/raw_set2_questions.json"
with open(raw_path_1, "r", encoding="utf-8") as f:
    raw_data_1 = json.load(f)

cleaned_p1 = []
for q in raw_data_1:
    qnum = q['q_num']
    raw_cat = q['category']
    cat = CATEGORY_MAP_P1.get(raw_cat, raw_cat)
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
    cleaned_p1.append({
        'category': cat,
        'q_num': qnum,
        'sub_set': 'Part 1 (100 Qs)',
        'stem': stem,
        'options': opts,
        'correct_answer': c_ans,
        'explanation': expl,
        'high_yield_pearl': pearl,
        'source': f"USMLE Step 1 Set 2 (Part 1): {cat}"
    })

print(f"Loaded and cleaned {len(cleaned_p1)} questions from Part 1.")

# --- Part 2: Ingest 150 Qs from second set ---
p2_md_path = "/Users/markyoussef_1/Downloads/Neuro E2 – USMLE Step 1 Practice Questions (150).md"
with open(p2_md_path, "r", encoding="utf-8") as f:
    text_p2 = f.read()

raw_sections_p2 = re.split(r'\n## ', text_p2)[1:]
cleaned_p2 = []

for s in raw_sections_p2:
    sec_title = s.split('\n')[0].strip()
    clean_cat = None
    for k, v in CATEGORY_MAP_P2.items():
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
        # Clean any leading markdown bullets in stem
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
        cleaned_p2.append({
            'category': clean_cat,
            'q_num': q_num,
            'sub_set': 'Part 2 (150 Qs)',
            'stem': stem,
            'options': options,
            'correct_answer': corr,
            'explanation': exp,
            'high_yield_pearl': pearl,
            'source': f"USMLE Step 1 Set 2 (Part 2): {clean_cat}"
        })

print(f"Loaded and cleaned {len(cleaned_p2)} questions from Part 2.")

all_cleaned = cleaned_p1 + cleaned_p2
print(f"Combined total: {len(all_cleaned)} questions across 9 units.")

# --- Comprehensive Quality & Bias Audit on All 250 Qs ---
audit_flags = []
for idx, q in enumerate(all_cleaned):
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
    # Length ratio check
    if ratio > 1.45 and len_c > max_d + 15:
        issues.append(f"noticeably longer (ratio={ratio:.2f}, {len_c} vs avg {avg_d:.1f})")
    elif ratio < 0.65 and len_c < min_d - 15:
        issues.append(f"noticeably shorter (ratio={ratio:.2f}, {len_c} vs avg {avg_d:.1f})")
        
    # Parentheses check
    corr_has_paren = '(' in c_opt and ')' in c_opt
    dist_with_paren = sum(1 for d in distractors if '(' in d and ')' in d)
    if corr_has_paren and dist_with_paren == 0:
        issues.append(f"correct answer has parens while NO distractors do: {c_opt}")
    elif not corr_has_paren and dist_with_paren == len(distractors):
        issues.append("all distractors have parens while correct answer does not")
    elif '(' in c_opt or dist_with_paren > 0:
        if 0 < dist_with_paren + (1 if corr_has_paren else 0) < len(q['options']):
            issues.append(f"inconsistent parentheses usage ({dist_with_paren + (1 if corr_has_paren else 0)}/{len(q['options'])})")
            
    # Cross-references check
    if re.search(r'(question\s+\d+|above\s+patient|previous\s+patient|same\s+patient|referring\s+to)', q['stem'], re.IGNORECASE):
        issues.append(f"cross-reference stem: {q['stem'][:50]}")
        
    if issues:
        audit_flags.append((q['sub_set'], q['category'], q['q_num'], issues, c_letter, c_opt))

print(f"\nAudit completed across all 250 questions. Flags found: {len(audit_flags)}")
if audit_flags:
    for sub, cat, qnum, iss, c_l, c_o in audit_flags:
        print(f"FLAG [{sub} Q{qnum} {cat}] ({c_l}): {c_o} -> {iss}")
    raise ValueError(f"Audit failed with {len(audit_flags)} flags!")

print("All 250 questions PASSED the bias, length, and giveaway audit with 0 flags!\n")

# Verify category counts
cat_counts = {}
for q in all_cleaned:
    cat_counts[q['category']] = cat_counts.get(q['category'], 0) + 1
print("Category Breakdown (Combined 250 Qs):")
for cat, cnt in sorted(cat_counts.items()):
    print(f"  - {cat}: {cnt} Qs")

# Randomize question order across All Topics using deterministic seed 42
rng = random.Random(42)
shuffled_questions = all_cleaned.copy()
rng.shuffle(shuffled_questions)

for i, q in enumerate(shuffled_questions):
    q['id'] = f"set2_{i+1}"
    q['index'] = i

# Save JSON
out_json_path = "/Users/markyoussef_1/.gemini/antigravity-ide/scratch/usmle_exam1/exam2_set2_questions.json"
with open(out_json_path, "w", encoding="utf-8") as f:
    json.dump(shuffled_questions, f, indent=2)
print(f"\nSaved combined clean questions JSON to: {out_json_path}")

# Review Markdown
review_md_path = "/Users/markyoussef_1/.gemini/antigravity-ide/scratch/usmle_exam1/exam2_set2_questions_review.md"
with open(review_md_path, "w", encoding="utf-8") as f:
    f.write("# USMLE Step 1 - Exam 2 'Set 2' Bank (Combined 250 Questions)\n\n")
    f.write("Full audit completed. All option length biases, asymmetric parentheses, and giveaway punctuation removed.\n\n")
    f.write(f"Randomized across All Topics with 9 category filters. Total questions: {len(shuffled_questions)}\n\n")
    f.write("### Category Breakdown:\n")
    for cat, cnt in sorted(cat_counts.items()):
        f.write(f"- **{cat}**: {cnt} Questions\n")
    f.write("\n---\n\n")
    for q in shuffled_questions:
        f.write(f"### Question {q['index']+1} ({q['sub_set']} Original Q{q['q_num']}) — {q['category']}\n\n")
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
