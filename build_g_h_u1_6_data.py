import json
import random
from test_gen_structure import check_q

from gen_g_h_u1 import U1_QUESTIONS as u1_questions
from gen_g_h_u2 import u2_questions
from gen_g_h_u3 import u3_questions
from gen_g_h_u4 import u4_questions
from gen_g_h_u5 import u5_questions
from gen_g_h_u6 import u6_questions

OUTPUT_JSON = '/Users/markyoussef_1/.gemini/antigravity-ide/scratch/usmle_exam1/exam3_g_h_u1_6_questions.json'

def build_data():
    all_units = [
        (1, "Unit 01: Demyelinating Diseases", u1_questions),
        (2, "Unit 02: Cerebellum", u2_questions),
        (3, "Unit 03: Tumors", u3_questions),
        (4, "Unit 04: Infections", u4_questions),
        (5, "Unit 05: Epilepsy", u5_questions),
        (6, "Unit 06: Blood Supply", u6_questions)
    ]
    
    raw_questions = []
    
    for u_num, cat_name, q_list in all_units:
        assert len(q_list) == 20, f"Unit {u_num} does not have 20 questions (found {len(q_list)})"
        for orig_idx, q in enumerate(q_list, 1):
            # Standardize options
            opt_list = []
            for idx, opt in enumerate(q["options"]):
                letter = chr(ord('A') + idx)
                opt_list.append({
                    "letter": letter,
                    "label": letter,
                    "is_correct": opt["is_correct"],
                    "text": opt["text"]
                })
            
            q_obj = {
                "orig_unit": u_num,
                "orig_q_num": orig_idx,
                "stem": q["stem"],
                "category": cat_name,
                "subcategory": q.get("subcategory", cat_name),
                "source": f"Neuro E3 Higher-Order Master Bank Unit {u_num}",
                "options": opt_list,
                "correct_idx": q["correct_idx"],
                "explanation": q["explanation"],
                "high_yield_pearl": q.get("high_yield_takeaway", f"High-Yield Rule: {cat_name}"),
                "image": None
            }
            raw_questions.append(q_obj)

    print(f"Total raw questions collected: {len(raw_questions)}")
    assert len(raw_questions) == 120, f"Expected 120 questions, got {len(raw_questions)}"

    # Randomize question order across all 6 units using fixed seed for reproducible state
    random.Random(42).shuffle(raw_questions)

    formatted_questions = []
    for new_idx, q in enumerate(raw_questions, 1):
        q_obj = {
            "id": f"exam3_g_h_u1_6_q{new_idx}",
            "q_num": str(new_idx),
            "orig_unit": q["orig_unit"],
            "orig_q_num": q["orig_q_num"],
            "stem": q["stem"],
            "category": q["category"],
            "subcategory": q["subcategory"],
            "source": q["source"],
            "options": q["options"],
            "correct_idx": q["correct_idx"],
            "explanation": q["explanation"],
            "high_yield_pearl": q["high_yield_pearl"],
            "image": q["image"]
        }
        # Run validation check on each question
        check_q(q_obj)
        formatted_questions.append(q_obj)

    print(f"All {len(formatted_questions)} questions validated successfully!")

    with open(OUTPUT_JSON, 'w', encoding='utf-8') as f:
        json.dump(formatted_questions, f, indent=2, ensure_ascii=False)
    print(f"Saved {len(formatted_questions)} questions to {OUTPUT_JSON}")

if __name__ == '__main__':
    build_data()
