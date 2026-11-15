"""Build script to parse Neuro E3 Practice Exam 2 High-Yield USMLE Step 1 Style (150 Questions).md
into exam3_high_yield_questions.json matching the usmle_exam1 app schema.
"""
import json
import re
import os

def build_high_yield_json():
    source_path = '/Users/markyoussef_1/Downloads/Neuro E3 Practice Exam 2 High-Yield USMLE Step 1 Style (150 Questions).md'
    out_path = '/Users/markyoussef_1/.gemini/antigravity-ide/scratch/usmle_exam1/exam3_high_yield_questions.json'

    with open(source_path, 'r', encoding='utf-8') as f:
        content = f.read()

    part1_idx = content.find('## Part 1: Questions')
    part2_idx = content.find('## Part 2: Answer Key and Explanations')

    part1 = content[part1_idx:part2_idx]
    part2 = content[part2_idx:]

    ans_matches = list(re.finditer(r'\*\*(\d+)\.\s*([A-E])\.\*\*\s*(.+?)(?=\n\n\*\*|\n###|$)', part2, re.DOTALL))
    ans_dict = {}
    for m in ans_matches:
        qnum = int(m.group(1))
        letter = m.group(2).strip()
        expl = m.group(3).strip()
        ans_dict[qnum] = (letter, expl)

    def get_category(qnum):
        if 1 <= qnum <= 15:
            return 'Demyelinating Diseases'
        elif 16 <= qnum <= 27:
            return 'Cerebellum'
        elif 28 <= qnum <= 48:
            return 'Tumors'
        elif 49 <= qnum <= 63:
            return 'Infections'
        elif 64 <= qnum <= 77:
            return 'Blood Supply'
        elif 78 <= qnum <= 92:
            return 'Cerebrovascular Disease'
        elif 93 <= qnum <= 108:
            return 'Brainstem Stroke'
        elif 109 <= qnum <= 123:
            return 'Dementia'
        elif 124 <= qnum <= 150:
            return 'CBIL: Epilepsy'
        else:
            return 'High-Yield General'

    q_matches = list(re.finditer(r'\*\*(\d+)\.\*\*\s+(.+?)(?=\n\n\*\*|\n###|##|$)', part1, re.DOTALL))

    questions = []
    for m in q_matches:
        qnum = int(m.group(1))
        body = m.group(2).strip()
        first_opt = re.search(r'^[-\*]?\s*([A-E])\.\s+', body, re.MULTILINE)
        stem = body[:first_opt.start()].strip()
        opt_matches = list(re.finditer(r'^[-\*]?\s*([A-E])\.\s+(.+)$', body[first_opt.start():], re.MULTILINE))
        
        correct_letter, expl = ans_dict[qnum]
        letter_to_idx = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4}
        correct_idx = letter_to_idx[correct_letter]
        category = get_category(qnum)
        
        options = []
        for om in opt_matches:
            let = om.group(1).strip()
            text = om.group(2).strip()
            options.append({
                'letter': let,
                'is_correct': (let == correct_letter),
                'text': text
            })
            
        q_data = {
            'id': f'exam3_hy_q{qnum}',
            'q_num': str(qnum),
            'stem': stem,
            'category': category,
            'source': 'Neuro E3 Practice Exam 2 High-Yield USMLE Step 1 Style (150 Questions)',
            'options': options,
            'correct_idx': correct_idx,
            'explanation': expl,
            'high_yield_pearl': f'High-Yield Rule: {category}',
            'image': None
        }
        questions.append(q_data)

    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(questions, f, indent=2, ensure_ascii=False)

    print(f'Successfully generated {len(questions)} questions into {out_path}')

if __name__ == '__main__':
    build_high_yield_json()
