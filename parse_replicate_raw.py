#!/usr/bin/env python3
import re
import json

md_path = "/Users/markyoussef_1/Downloads/Neuro Exam 2 USMLE-Style Step 1 Question Bank (100 MCQs).md"

with open(md_path, "r", encoding="utf-8") as f:
    content = f.read()

# Split into Questions part and Answer Key part
parts = content.split("# Answer Key & Explanations")
if len(parts) < 2:
    parts = re.split(r"#+\s*Answer Key", content, flags=re.IGNORECASE)

questions_text = parts[0]
answers_text = parts[1]

# Parse Answer Key
# format: **1. B.** Explanation... or **1. B** or **1. B:**
ans_pattern = re.compile(r'\*\*(\d+)\.\s*([A-E])\.?\*\*\s*(.*?)(?=\n\s*\*\*\d+\.|\n\s*##|\Z)', re.DOTALL)
answers = {}
for m in ans_pattern.finditer(answers_text):
    q_num = int(m.group(1))
    correct_letter = m.group(2).strip().upper()
    expl = m.group(3).strip()
    # Clean up single newlines in explanation
    expl = re.sub(r'\s*\n\s*', ' ', expl)
    answers[q_num] = {
        'correct_answer': correct_letter,
        'explanation': expl
    }

print(f"Parsed {len(answers)} answer keys.")

# Unit headings in questions_text
# e.g. ## Visual System (Questions 1–8)
# ## Visual Reflexes (Questions 9–24)
# ## Ophthalmology (Questions 25–30)
# ## Auditory & Vestibular System (Questions 31–44)
# ## UMN/LMN (Questions 45–64)
# ## Hypothalamus & Smell/Taste (Questions 65–70)
# ## Basal Ganglia (Questions 71–88)
# ## CBIL: Sleep (Questions 89–94)
# ## CBIL: ALS (Questions 95–100)

unit_ranges = [
    (1, 8, "Visual System"),
    (9, 24, "Visual Reflexes"),
    (25, 30, "Ophthalmology"),
    (31, 44, "Auditory & Vestibular"),
    (45, 64, "UMN/LMN"),
    (65, 70, "Hypothalamus & Smell/Taste"),
    (71, 88, "Basal Ganglia"),
    (89, 94, "CBIL: Sleep"),
    (95, 100, "CBIL: ALS")
]

def get_unit(q_num):
    for start, end, name in unit_ranges:
        if start <= q_num <= end:
            return name
    return "General"

# Parse Questions
# format: **1.** Stem text...
# - A. Option A
# - B. Option B
q_pattern = re.compile(r'\*\*(\d+)\.\*\*\s*(.*?)(?=\n\s*\*\*|\n\s*---\s*\n\s*##|\Z)', re.DOTALL)

parsed_questions = []

for q_num in range(1, 101):
    # Find question block
    # regex for **q_num.**
    block_m = re.search(r'\*\*' + str(q_num) + r'\.\*\*\s*(.*?)(?=\n\s*\*\*\d+\.\*\*|\n\s*---\s*\n\s*##|\Z)', questions_text, re.DOTALL)
    if not block_m:
        print(f"Warning: Question {q_num} not found!")
        continue
    raw_block = block_m.group(1).strip()
    
    # Split stem and options
    lines = raw_block.split('\n')
    stem_lines = []
    options = {}
    
    for line in lines:
        line_s = line.strip()
        opt_m = re.match(r'^-\s*([A-E])\.\s*(.*)$', line_s)
        if opt_m:
            options[opt_m.group(1)] = opt_m.group(2).strip()
        else:
            if not options: # still reading stem
                if line_s:
                    stem_lines.append(line_s)
    
    stem = " ".join(stem_lines).strip()
    
    ans_info = answers.get(q_num, {'correct_answer': '', 'explanation': ''})
    
    parsed_questions.append({
        'q_num': q_num,
        'category': get_unit(q_num),
        'stem': stem,
        'options': options,
        'correct_answer': ans_info['correct_answer'],
        'explanation': ans_info['explanation']
    })

print(f"Successfully parsed {len(parsed_questions)} questions.")

out_path = "/Users/markyoussef_1/.gemini/antigravity-ide/scratch/usmle_exam1/raw_replicate_questions.json"
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(parsed_questions, f, indent=2, ensure_ascii=False)
print(f"Saved to {out_path}")
