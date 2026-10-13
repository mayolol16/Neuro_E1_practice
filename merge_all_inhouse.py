import json

with open("part1_questions.json") as f:
    p1 = json.load(f)

with open("part2_questions.json") as f:
    p2 = json.load(f)

with open("part3_questions.json") as f:
    p3 = json.load(f)

with open("part4_headache.json") as f:
    p4_h = json.load(f)

with open("part4_trauma.json") as f:
    p4_t = json.load(f)

with open("part4_meningitis.json") as f:
    p4_m = json.load(f)

p4 = p4_h + p4_t + p4_m

with open("part4_questions.json", "w") as f:
    json.dump(p4, f, indent=2)

all_inhouse = p1 + p2 + p3 + p4

print(f"Part 1: {len(p1)} questions")
print(f"Part 2: {len(p2)} questions")
print(f"Part 3: {len(p3)} questions")
print(f"Part 4: {len(p4)} questions")
print(f"Total In-House Questions: {len(all_inhouse)}")

categories = {}
# Validation
for idx, q in enumerate(all_inhouse):
    qid = q.get("id")
    cat = q.get("category")
    categories[cat] = categories.get(cat, 0) + 1
    text = q.get("question", "")
    opts = q.get("options", [])
    exp = q.get("explanation", "")
    
    assert len(text) > 20, f"Question text too short at {qid}"
    assert len(exp) > 20, f"Explanation too short at {qid}"
    assert len(opts) == 5, f"Options not 5 at {qid}: {len(opts)}"
    
    correct_count = sum(1 for o in opts if o.get("is_correct") is True)
    assert correct_count == 1, f"Question {qid} does not have exactly 1 correct answer (has {correct_count})"

print("\n--- CATEGORY BREAKDOWN ---")
for cat, count in categories.items():
    print(f"- {cat}: {count} questions")

with open("inhouse_questions_data.json", "w") as f:
    json.dump(all_inhouse, f, indent=2)

print("\nSuccessfully validated and saved inhouse_questions_data.json with 385 questions!")
