import sys
import os
import json
from collections import Counter

sys.path.insert(0, '/Users/markyoussef_1/.gemini/antigravity-ide/scratch/usmle_exam1')

from generate_in_house_g_part1 import get_part1_questions
from generate_in_house_g_part2 import get_part2_questions
from generate_in_house_g_part3 import get_part3_questions

p1 = get_part1_questions()
p2 = get_part2_questions()
p3 = get_part3_questions()

print(f"Loaded: Part 1 = {len(p1)}, Part 2 = {len(p2)}, Part 3 = {len(p3)}")
all_qs = p1 + p2 + p3
assert len(all_qs) == 150, f"Expected 150 questions, got {len(all_qs)}"

letters = ["A", "B", "C", "D", "E"]

# Balance keys evenly across A, B, C, D, E
balanced_qs = []
for i, q in enumerate(all_qs):
    target_idx = i % 5  # 0->A, 1->B, 2->C, 3->D, 4->E
    target_letter = letters[target_idx]
    
    # Current correct option text
    curr_corr_idx = q['correct_idx']
    corr_opt = q['options'][curr_corr_idx]
    other_opts = [opt for j, opt in enumerate(q['options']) if j != curr_corr_idx]
    
    # Create new options list with target_idx holding the correct option
    new_options = []
    other_iter = iter(other_opts)
    for pos in range(5):
        if pos == target_idx:
            new_options.append({
                "letter": letters[pos],
                "is_correct": True,
                "text": corr_opt['text']
            })
        else:
            opt = next(other_iter)
            new_options.append({
                "letter": letters[pos],
                "is_correct": False,
                "text": opt['text']
            })
            
    q['options'] = new_options
    q['correct_idx'] = target_idx
    q['q_num'] = str(i + 1)
    q['id'] = f"exam3_in_house_like_g_q{i + 1}"
    q['source'] = "in_house_like_G (150 Questions)"
    
    # Ensure correct category names
    if i < 15:
        q['category'] = "Demyelinating Disease"
    elif i < 27:
        q['category'] = "Cerebellum"
    elif i < 48:
        q['category'] = "Tumors"
    elif i < 63:
        q['category'] = "Opportunistic Infection"
    elif i < 108:
        q['category'] = "Stroke (Blood Supply, Cerebrovascular, Brainstem)"
    elif i < 123:
        q['category'] = "Dementia"
    else:
        q['category'] = "CBIL Epilepsy"
        
    balanced_qs.append(q)

# Verifications
cat_counts = Counter(q['category'] for q in balanced_qs)
print("\nCategory Breakdown:")
for cat, cnt in cat_counts.items():
    print(f"  {cat}: {cnt} ({cnt/150*100:.1f}%)")

key_counts = Counter(q['options'][q['correct_idx']]['letter'] for q in balanced_qs)
print("\nKey Distribution:")
for k in sorted(key_counts.keys()):
    print(f"  {k}: {key_counts[k]} ({key_counts[k]/150*100:.1f}%)")

# Audit length differences
diffs = [max([len(opt['text']) for opt in q['options']]) - min([len(opt['text']) for opt in q['options']]) for q in balanced_qs]
print(f"\nOption Length Differences: Max = {max(diffs)}, Min = {min(diffs)}, Avg = {sum(diffs)/len(diffs):.2f}")
assert max(diffs) <= 12, f"Option length diff too large: {max(diffs)}"

# Save output
out_path = '/Users/markyoussef_1/.gemini/antigravity-ide/scratch/usmle_exam1/exam3_in_house_like_g_questions.json'
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(balanced_qs, f, indent=2, ensure_ascii=False)

print(f"\nSuccessfully wrote {len(balanced_qs)} questions to {out_path}")
