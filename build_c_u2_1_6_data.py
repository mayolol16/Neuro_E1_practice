import re
import json
import os
import random
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from c_u2_unit1_unit2 import unit1_overrides, unit2_overrides
from c_u2_unit3_unit4 import unit3_overrides, unit4_overrides
from c_u2_unit5_unit6 import unit5_overrides, unit6_overrides

SOURCE_MD = '/Users/markyoussef_1/Downloads/Neuro_E3_USMLE_MCQs_Set2_Units1-6.md'
OUTPUT_JSON = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'exam3_c_u2_1_6_questions.json')

ALL_OVERRIDES = {
    1: unit1_overrides,
    2: unit2_overrides,
    3: unit3_overrides,
    4: unit4_overrides,
    5: unit5_overrides,
    6: unit6_overrides,
}

unit_category_names = {
    1: "Unit 01: Demyelinating Diseases",
    2: "Unit 02: Cerebellum",
    3: "Unit 03: Tumors & Neurocutaneous Syndromes",
    4: "Unit 04: Infections of the Nervous System",
    5: "Unit 05: CBIL — Epilepsy & Seizure Disorders",
    6: "Unit 06: Blood Supply of the Central Nervous System"
}

EXPECTED_COUNTS = {
    1: 33,
    2: 34,
    3: 34,
    4: 34,
    5: 33,
    6: 34
}

def parse_unit(u_text):
    parts = re.split(r'### Answer Key', u_text, flags=re.IGNORECASE)
    q_part = parts[0]
    ans_part = parts[1] if len(parts) > 1 else ''
    
    q_blocks = re.split(r'(?=\*\*\d+\.\*\*)', q_part)
    questions = {}
    for block in q_blocks:
        m = re.match(r'\*\*(\d+)\.\*\*\s*(.+)', block.strip(), re.DOTALL)
        if not m:
            continue
        qnum = int(m.group(1))
        rest = m.group(2).strip()
        opt_start = re.search(r'\n[ \t]*A\.\s*', rest)
        if opt_start:
            stem = rest[:opt_start.start()].strip()
            opt_text = rest[opt_start.start():].strip()
        else:
            stem = rest
            opt_text = ''
        
        opts = {}
        for opt_m in re.finditer(r'^[ \t]*([A-E])\.\s*(.+)$', opt_text, re.MULTILINE):
            opts[opt_m.group(1)] = opt_m.group(2).strip()
        questions[qnum] = {'stem': stem, 'opts': opts}
        
    ans_keys = {}
    for row in ans_part.split('\n'):
        if '|' in row:
            cols = [c.strip() for c in row.split('|')[1:-1]]
            if len(cols) >= 3 and cols[0].isdigit():
                qnum = int(cols[0])
                corr = cols[1].replace('*', '').strip()
                expl = cols[2].replace('*', '').strip()
                ans_keys[qnum] = {'corr': corr, 'expl': expl}
    return questions, ans_keys

def build_data():
    with open(SOURCE_MD, 'r', encoding='utf-8') as f:
        text = f.read()

    units_split = re.split(r'#+\s*Unit\s*0?(\d+):', text)

    raw_questions = []

    for u_num in range(1, 7):
        u_content = units_split[2 * u_num]
        cat_name = unit_category_names[u_num]
        qs, ans_keys = parse_unit(u_content)
        overrides = ALL_OVERRIDES[u_num]
        
        expected_cnt = EXPECTED_COUNTS[u_num]
        assert len(qs) == expected_cnt, f"Unit {u_num} expected {expected_cnt} questions, found {len(qs)}"
        assert len(ans_keys) == expected_cnt, f"Unit {u_num} expected {expected_cnt} answer keys, found {len(ans_keys)}"
        
        for q_idx in range(1, expected_cnt + 1):
            q_data = qs[q_idx]
            a_data = ans_keys[q_idx]
            
            stem = q_data['stem']
            
            # Options (with override if any)
            opts_dict = overrides.get(q_idx, q_data['opts'])
            assert len(opts_dict) == 5, f"Unit {u_num} Q{q_idx} does not have 5 options: {opts_dict}"
            
            corr_letter = a_data['corr']
            assert corr_letter in ['A', 'B', 'C', 'D', 'E'], f"Invalid corr_letter {corr_letter} in U{u_num} Q{q_idx}"
            
            opt_list = []
            corr_idx = -1
            for idx, letter in enumerate(['A', 'B', 'C', 'D', 'E']):
                is_corr = (letter == corr_letter)
                if is_corr:
                    corr_idx = idx
                opt_list.append({
                    "letter": letter,
                    "is_correct": is_corr,
                    "text": opts_dict[letter]
                })
            assert corr_idx >= 0, f"Correct choice index not found in U{u_num} Q{q_idx}"
            
            explanation_text = a_data['expl']
            
            q_obj = {
                "orig_unit": u_num,
                "orig_q_num": q_idx,
                "stem": stem,
                "category": cat_name,
                "source": "Neuro E3 Set 2 Units 1–6 (c_u2_1-6)",
                "options": opt_list,
                "correct_idx": corr_idx,
                "explanation": explanation_text,
                "high_yield_pearl": f"High-Yield Rule: {cat_name}",
                "image": None
            }
            raw_questions.append(q_obj)

    print(f"Total raw questions parsed: {len(raw_questions)}")
    assert len(raw_questions) == 202, f"Expected 202 questions, got {len(raw_questions)}"

    # Randomize question order across all units using fixed seed for reproducible state
    random.Random(42).shuffle(raw_questions)

    # Renumber questions sequentially
    formatted_questions = []
    for new_idx, q in enumerate(raw_questions, 1):
        q_obj = {
            "id": f"exam3_c_u2_1_6_q{new_idx}",
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
    print(f"Successfully saved {len(formatted_questions)} questions to {OUTPUT_JSON}")

if __name__ == '__main__':
    build_data()
