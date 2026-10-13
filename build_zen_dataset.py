# build_zen_dataset.py
import json
import os
import sys

sys.path.insert(0, '/Users/markyoussef_1/.gemini/antigravity-ide/scratch/usmle_exam1/zen_data')

from zen_part1 import part1_questions
from zen_part2 import part2_questions
from zen_part3 import part3_questions
from zen_part4 import part4_questions

all_raw = part1_questions + part2_questions + part3_questions + part4_questions

print(f"Total raw questions collected: {len(all_raw)}")

expected_categories = [
    "Central Nervous System Anatomy",
    "Central Nervous System Development",
    "Neurotransmitters and Action Potentials",
    "Ventricular System",
    "Acetylcholine / Neuromuscular Junction Disorder",
    "Neuroimaging",
    "Tactile Pathway",
    "Spinal Cord",
    "Pain Pathway",
    "Trigeminal Pathway",
    "Anesthetic & NMJ Blocking Agents",
    "Headache",
    "Cannabis Management",
    "Pathways and Opioids",
    "Traumatic Brain Injuries",
    "Meningitis"
]

cat_counts = {c: 0 for c in expected_categories}
processed_questions = []

for idx, q in enumerate(all_raw):
    cat = q['category']
    if cat not in cat_counts:
        raise ValueError(f"Unknown category: {cat} in Q {q.get('q_num')}")
    cat_counts[cat] += 1
    
    # Check options and correct_idx
    opts = q['options']
    correct_indices = [i for i, o in enumerate(opts) if o.get('is_correct')]
    if len(correct_indices) != 1:
        raise ValueError(f"Q {q.get('q_num')} does not have exactly 1 correct answer! Found: {correct_indices}")
    correct_idx = correct_indices[0]
    
    if not q['stem'].strip():
        raise ValueError(f"Q {q.get('q_num')} has empty stem!")
    if not q['explanation'].strip():
        raise ValueError(f"Q {q.get('q_num')} has empty explanation!")
        
    processed_q = {
        'id': f"zen_{idx + 1}",
        'zen_num': idx + 1,
        'q_num': q['q_num'],
        'category': cat,
        'stem': q['stem'].strip(),
        'options': opts,
        'correct_idx': correct_idx,
        'explanation': q['explanation'].strip(),
        'image': None
    }
    processed_questions.append(processed_q)

print("\n--- Category Breakdown ---")
for cat, count in cat_counts.items():
    print(f"  {cat}: {count} questions")
    if count != 20:
        raise ValueError(f"Category '{cat}' has {count} questions instead of 20!")

out_path = '/Users/markyoussef_1/.gemini/antigravity-ide/scratch/usmle_exam1/zen_questions_data.json'
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(processed_questions, f, indent=2, ensure_ascii=False)

print(f"\nSUCCESS! Saved {len(processed_questions)} validated Zen Mode questions to {out_path}")
