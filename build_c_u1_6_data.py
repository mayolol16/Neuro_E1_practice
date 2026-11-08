import re
import json
import os
import random
from build_c_u1_6_overrides import ALL_OVERRIDES, STEM_OVERRIDES

SOURCE_MD = '/Users/markyoussef_1/Downloads/Neuro_E3_USMLE_MCQs_Units1-6.md'
OUTPUT_JSON = '/Users/markyoussef_1/.gemini/antigravity-ide/scratch/usmle_exam1/exam3_c_u1_6_questions.json'

def build_data():
    with open(SOURCE_MD, 'r', encoding='utf-8') as f:
        text = f.read()

    unit_splits = re.split(r'\n# Unit (\d+): ([^\n]+)', text)
    units = []
    for i in range(1, len(unit_splits), 3):
        u_num = int(unit_splits[i])
        u_title = unit_splits[i+1].strip()
        u_body = unit_splits[i+2]
        units.append((u_num, u_title, u_body))

    raw_questions = []

    for u_num, u_title, u_body in units:
        unit_category = f"Unit 0{u_num}: {u_title}"
        parts = re.split(r'###\s+Answer Key\s*&?\s*Explanations?', u_body)
        q_section, ans_section = parts[0], parts[1]
        
        ans_map = {}
        for row in ans_section.split('\n'):
            row = row.strip()
            if not row.startswith('|'): continue
            cols = [c.strip() for c in row.split('|')[1:-1]]
            if len(cols) >= 3 and cols[0].isdigit():
                ans_map[int(cols[0])] = (cols[1].replace('*', '').strip(), cols[2].strip())
                
        q_blocks = re.split(r'\n\*\*(\d+)\.\*\*\s*', '\n' + q_section)
        for j in range(1, len(q_blocks), 2):
            q_idx = int(q_blocks[j])
            q_content = q_blocks[j+1].strip()
            lines = q_content.split('\n')
            stem_lines, options = [], {}
            curr_opt = None
            for line in lines:
                m = re.match(r'^([A-E])\.\s*(.*)', line.strip())
                if m:
                    curr_opt = m.group(1)
                    options[curr_opt] = m.group(2).strip()
                elif curr_opt:
                    options[curr_opt] += ' ' + line.strip()
                else:
                    stem_lines.append(line)
            
            # Apply balance override if present
            if (u_num, q_idx) in ALL_OVERRIDES:
                options = ALL_OVERRIDES[(u_num, q_idx)]
                
            stem = ' '.join(stem_lines).strip()
            # Apply standalone stem override if question referenced another question
            if (u_num, q_idx) in STEM_OVERRIDES:
                stem = STEM_OVERRIDES[(u_num, q_idx)]

            correct_key, explanation = ans_map[q_idx]
            
            opt_list = []
            corr_idx = -1
            for idx, letter in enumerate(['A', 'B', 'C', 'D', 'E']):
                is_corr = (letter == correct_key)
                if is_corr:
                    corr_idx = idx
                opt_list.append({
                    "letter": letter,
                    "is_correct": is_corr,
                    "text": options[letter]
                })
                
            assert corr_idx >= 0, f"Correct answer {correct_key} not found in options for U{u_num} Q{q_idx}"
            
            q_obj = {
                "orig_unit": u_num,
                "orig_q_num": q_idx,
                "stem": stem,
                "category": unit_category,
                "source": f"Neuro E3 Curriculum Unit {u_num}",
                "options": opt_list,
                "correct_idx": corr_idx,
                "explanation": explanation,
                "high_yield_pearl": f"High-Yield Rule: {unit_category}",
                "image": None
            }
            raw_questions.append(q_obj)

    print(f"Total raw questions parsed: {len(raw_questions)}")

    # Randomize question order across all units using fixed seed for reproducible state
    random.Random(42).shuffle(raw_questions)

    # Renumber questions sequentially
    formatted_questions = []
    for new_idx, q in enumerate(raw_questions, 1):
        q_obj = {
            "id": f"exam3_c_u1_6_q{new_idx}",
            "q_num": str(new_idx),
            "orig_unit": q["orig_unit"],
            "orig_q_num": q["orig_q_num"],
            "stem": q["stem"],
            "category": q["category"],
            "source": q["source"],
            "options": q["options"],
            "correct_idx": q["correct_idx"],
            "explanation": q["explanation"],
            "high_yield_pearl": q["high_yield_pearl"],
            "image": q["image"]
        }
        formatted_questions.append(q_obj)

    print(f"Total formatted questions after randomization: {len(formatted_questions)}")
    with open(OUTPUT_JSON, 'w', encoding='utf-8') as f:
        json.dump(formatted_questions, f, indent=2, ensure_ascii=False)
    print(f"Saved to {OUTPUT_JSON}")

if __name__ == '__main__':
    build_data()
