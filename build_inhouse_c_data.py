import json
import os
import random
import re
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from inhouse_c_explanations import STEM_OVERRIDES, EXPLANATIONS_33_100
from inhouse_c_overrides import OPTION_OVERRIDES

SOURCE_MD = '/Users/markyoussef_1/Downloads/Neuro Exam 3 – USMLE Step 1-Style Practice Exam.md'
OUTPUT_JSON = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'exam3_inhouse_c_questions.json')

CATEGORIES = [
    "Demyelinating Disease",
    "Cerebellum",
    "Tumors",
    "Opportunistic Infection",
    "Stroke (Blood Supply, Cerebrovascular, Brainstem)",
    "Dementia",
    "CBIL Epilepsy",
]


def get_category_and_section(qnum):
    if 1 <= qnum <= 10:
        return "Demyelinating Disease", "Demyelinating Disease (Q1–10)"
    if 11 <= qnum <= 18:
        return "Cerebellum", "Cerebellum (Q11–18)"
    if 19 <= qnum <= 32:
        return "Tumors", "Tumors (Q19–32)"
    if 33 <= qnum <= 42:
        return "Opportunistic Infection", "Opportunistic Infection (Q33–42)"
    if 43 <= qnum <= 52:
        return "Stroke (Blood Supply, Cerebrovascular, Brainstem)", "Stroke — Blood Supply (Q43–52)"
    if 53 <= qnum <= 62:
        return "Stroke (Blood Supply, Cerebrovascular, Brainstem)", "Stroke — Cerebrovascular Disease (Q53–62)"
    if 63 <= qnum <= 72:
        return "Stroke (Blood Supply, Cerebrovascular, Brainstem)", "Stroke — Brainstem (Q63–72)"
    if 73 <= qnum <= 82:
        return "Dementia", "Dementia (Q73–82)"
    if 83 <= qnum <= 100:
        return "CBIL Epilepsy", "CBIL Epilepsy (Q83–100)"
    raise ValueError(f"Unexpected question number: {qnum}")


def parse_part1(part1_text):
    q_blocks = re.split(r'\n\*\*(\d+)\.\*\*\s+', '\n' + part1_text)
    questions = {}
    for i in range(1, len(q_blocks), 2):
        qnum = int(q_blocks[i])
        block = q_blocks[i + 1]
        # Strip trailing markdown section headers or horizontal rules from block
        block = re.split(r'\n(?:---|##+ )', block, maxsplit=1)[0].strip()
        opt_split = re.search(r'\n- \*\*A\.\*\*', block)
        assert opt_split, f"Could not find option A for Q{qnum}"
        stem = re.sub(r'\s+', ' ', block[:opt_split.start()].strip())
        opt_block = block[opt_split.start():]
        opts_matches = re.findall(r'^- \*\*([A-E])\.\*\*\s*(.+)$', opt_block, re.M)
        opts = {letter: text.strip() for letter, text in opts_matches}
        assert list(opts.keys()) == ['A', 'B', 'C', 'D', 'E'], f"Q{qnum} options invalid: {opts}"
        questions[qnum] = {'stem': stem, 'opts': opts}
    return questions


def parse_part2_1_to_32(part2_text):
    # Explanations formatted as **1. B.** text...
    cleaned = re.sub(r'\n(?:---|##+ ).*', '', part2_text)
    e_blocks = re.split(r'\n\*\*(\d+)\.\s+([A-E])\.\*\*\s*', '\n' + part2_text)
    keys = {}
    for i in range(1, len(e_blocks), 3):
        qnum = int(e_blocks[i])
        letter = e_blocks[i + 1].strip()
        body = e_blocks[i + 2]
        # Strip trailing section headers or dividers that belonged to the next section
        body = re.split(r'\n(?:---|###? )', body, maxsplit=1)[0].strip()
        body = re.sub(r'\s+', ' ', body)
        keys[qnum] = (letter, body)
    return keys


def audit_question(qnum, stem, opts, corr_letter):
    # Check cross-question references
    assert not re.search(r'\bQuestion\s+\d+\b', stem, re.I), f"Q{qnum} still references another Question: {stem}"
    lens = [len(opts[l]) for l in ['A', 'B', 'C', 'D', 'E']]
    ans_idx = ord(corr_letter) - ord('A')
    ans_len = lens[ans_idx]
    other_avg = (sum(lens) - ans_len) / 4.0
    ratio = ans_len / other_avg
    max_min = max(lens) / min(lens)
    p_cnts = [opts[l].count('(') for l in ['A', 'B', 'C', 'D', 'E']]
    s_cnts = [opts[l].count(';') for l in ['A', 'B', 'C', 'D', 'E']]
    single_p = (sum(1 for c in p_cnts if c > 0) == 1)
    single_s = (sum(1 for c in s_cnts if c > 0) == 1)
    issues = []
    if not (0.72 <= ratio <= 1.38):
        issues.append(f"ratio={ratio:.2f}")
    if max_min > 1.72:
        issues.append(f"max/min={max_min:.2f}")
    if single_p:
        issues.append("single_paren")
    if single_s:
        issues.append("single_semi")
    return issues, lens, ratio, max_min


def build_data():
    with open(SOURCE_MD, 'r', encoding='utf-8') as f:
        text = f.read().replace('\r\n', '\n')

    parts = re.split(r'^#+\s+Part\s+2\b.*$', text, maxsplit=1, flags=re.M)
    assert len(parts) == 2, "Could not split Part 1 and Part 2"
    part1_text, part2_text = parts

    qs = parse_part1(part1_text)
    assert len(qs) == 100, f"Expected 100 questions in Part 1, got {len(qs)}"

    part2_1_32 = parse_part2_1_to_32(part2_text)
    assert set(part2_1_32.keys()) == set(range(1, 33)), f"Expected Q1-32 in Part 2, got {sorted(part2_1_32.keys())}"
    assert set(EXPLANATIONS_33_100.keys()) == set(range(33, 101)), "Missing Q33-100 in EXPLANATIONS_33_100"

    raw_questions = []
    flagged = []

    for qnum in range(1, 101):
        stem = STEM_OVERRIDES.get(qnum, qs[qnum]['stem'])
        opts = OPTION_OVERRIDES.get(qnum, qs[qnum]['opts'])
        if qnum <= 32:
            corr_letter, explanation = part2_1_32[qnum]
        else:
            corr_letter, explanation = EXPLANATIONS_33_100[qnum]

        assert len(explanation) >= 40, f"Q{qnum} explanation too short: {explanation}"
        issues, lens, ratio, max_min = audit_question(qnum, stem, opts, corr_letter)
        if issues:
            flagged.append((qnum, corr_letter, issues, lens, opts))

        cat_name, orig_section = get_category_and_section(qnum)
        opt_list = []
        corr_idx = ord(corr_letter) - ord('A')
        for letter in ['A', 'B', 'C', 'D', 'E']:
            opt_list.append({
                "letter": letter,
                "is_correct": (letter == corr_letter),
                "text": opts[letter],
            })

        raw_questions.append({
            "orig_q_num": qnum,
            "orig_section": orig_section,
            "stem": stem,
            "category": cat_name,
            "source": "Neuro Exam 3 In House c (100 Qs)",
            "options": opt_list,
            "correct_idx": corr_idx,
            "explanation": explanation,
            "high_yield_pearl": f"High-Yield Rule: {cat_name}",
            "image": None,
        })

    if flagged:
        print(f"AUDIT FLAGGED {len(flagged)} QUESTIONS:")
        for qnum, corr, issues, lens, opts in flagged:
            print(f"  Q{qnum} (Ans={corr}) {issues} lens={lens}")
            for l in ['A', 'B', 'C', 'D', 'E']:
                print(f"    {'*' if l == corr else ' '}{l} ({len(opts[l])}): {opts[l]}")
        sys.exit(1)

    print("Anti-giveaway audit PASSED: 0 flagged out of 100 questions!")

    random.Random(42).shuffle(raw_questions)

    formatted_questions = []
    for new_idx, q in enumerate(raw_questions, 1):
        formatted_questions.append({
            "id": f"exam3_inhouse_c_q{new_idx}",
            "q_num": str(new_idx),
            "orig_q_num": q["orig_q_num"],
            "orig_section": q["orig_section"],
            "stem": q["stem"],
            "category": q["category"],
            "source": q["source"],
            "options": q["options"],
            "correct_idx": q["correct_idx"],
            "explanation": q["explanation"],
            "high_yield_pearl": q["high_yield_pearl"],
            "image": q["image"],
        })

    with open(OUTPUT_JSON, 'w', encoding='utf-8') as f:
        json.dump(formatted_questions, f, indent=2, ensure_ascii=False)

    print(f"Successfully wrote {len(formatted_questions)} randomized questions to {OUTPUT_JSON}")


if __name__ == '__main__':
    build_data()
