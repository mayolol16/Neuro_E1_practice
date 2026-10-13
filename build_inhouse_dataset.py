# -*- coding: utf-8 -*-
# build_inhouse_dataset.py
import json
import sys
import os

sys.path.insert(0, '/Users/markyoussef_1/.gemini/antigravity-ide/scratch/usmle_exam1/inhouse_data')

from inhouse_section1 import questions_section1
from inhouse_section2 import questions_section2
from inhouse_section3 import questions_section3
from inhouse_section4 import questions_section4

all_inhouse_questions = []
all_inhouse_questions.extend(questions_section1)
all_inhouse_questions.extend(questions_section2)
all_inhouse_questions.extend(questions_section3)
all_inhouse_questions.extend(questions_section4)

print(f"Total compiled In-House questions: {len(all_inhouse_questions)}")

# Standardize categories for elegant UI navigation
category_mapping = {
    "In House: CNS Anatomy": "In House: CNS Anatomy & Glia",
    "In House: CNS Anatomy & Glia": "In House: CNS Anatomy & Glia",
    "In House: CNS Development": "In House: CNS Development & Genetics",
    "In House: CNS Development Cases": "In House: CNS Development & Genetics",
    "In House: CNS Development & Genetics": "In House: CNS Development & Genetics",
    "In House: CNS Development & Biochemistry": "In House: CNS Development & Genetics",
    "In House: CNS Development & Milestones": "In House: CNS Development & Genetics",
    "In House: CNS Development & Spine": "In House: CNS Development & Genetics",
    "In House: Neurotransmission": "In House: Neurotransmission & Synapse",
    "In House: Neurotransmission & Anesthesia": "In House: Neurotransmission & Synapse",
    "In House: Ventricular System & CSF": "In House: Ventricular System & CSF",
    "In House: Neuromuscular Junction Disorders": "In House: Neuromuscular Junction Disorders",
    "In House: Anesthetic Pharmacology": "In House: Anesthetic Pharmacology",
    "In House: Somatosensory DCML Pathway": "In House: Somatosensory DCML Pathway",
    "In House: Somatosensory & Cortical Syndromes": "In House: Somatosensory DCML Pathway",
    "In House: Somatosensory ALS Pathway": "In House: Somatosensory ALS & Pain",
    "In House: Pain Mechanisms & Sensitization": "In House: Somatosensory ALS & Pain",
    "In House: Trigeminal Somatosensory Pathway": "In House: Trigeminal Pathways & Reflexes",
    "In House: Somatosensory & Spinal Cord": "In House: Spinal Cord Syndromes & Radiculopathies",
    "In House: Spinal Cord & Neuropathies": "In House: Spinal Cord Syndromes & Radiculopathies",
    "In House: Spinal Cord Syndromes": "In House: Spinal Cord Syndromes & Radiculopathies",
    "In House: Radiculopathies & Spine": "In House: Spinal Cord Syndromes & Radiculopathies",
    "In House: Radiculopathies & Neuropathies": "In House: Neuropathies & Electrodiagnosis",
    "In House: Neuropathies & Electrodiagnosis": "In House: Neuropathies & Electrodiagnosis",
    "In House: Headache Disorders": "In House: Headache Disorders",
    "In House: Traumatic Brain Injuries": "In House: Traumatic Brain Injuries",
    "In House: Meningitis & Infections": "In House: Meningitis & CNS Infections"
}

cleaned_questions = []
for idx, q in enumerate(all_inhouse_questions, start=1):
    q_id = f"IH_Q{idx:03d}"
    
    options = q["options"]
    assert len(options) == 5, f"Question {q_id} has {len(options)} options, expected 5!"
    correct_count = sum(1 for opt in options if opt.get("is_correct") is True)
    assert correct_count == 1, f"Question {q_id} has {correct_count} correct options, expected exactly 1!"
    
    raw_cat = q["category"]
    clean_cat = category_mapping.get(raw_cat, raw_cat)
    
    cleaned_item = {
        "id": q_id,
        "question_number": idx,
        "category": clean_cat,
        "stem": q["stem"].strip(),
        "options": options,
        "explanation": q["explanation"].strip()
    }
    cleaned_questions.append(cleaned_item)

out_path = '/Users/markyoussef_1/.gemini/antigravity-ide/scratch/usmle_exam1/inhouse_questions_data.json'
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(cleaned_questions, f, ensure_ascii=False, indent=2)

print(f"Successfully saved {len(cleaned_questions)} questions to {out_path}!")

cats = {}
for q in cleaned_questions:
    cats[q["category"]] = cats.get(q["category"], 0) + 1

print("\nRefined 14-Module Category Breakdown:")
for cat, count in sorted(cats.items()):
    print(f"  • {cat}: {count} Qs")
