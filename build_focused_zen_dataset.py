import sys
import json
from collections import Counter

sys.path.append('focused_zen_data')
from focused_zen_part1 import focused_questions_part1
from focused_zen_part2 import focused_questions_part2
from focused_zen_part3 import focused_questions_part3
from focused_zen_part4 import focused_questions_part4

all_focused_questions = (
    focused_questions_part1 +
    focused_questions_part2 +
    focused_questions_part3 +
    focused_questions_part4
)

print(f"Total focused zen questions loaded: {len(all_focused_questions)}")

# Renumber sequentially 1 to 320
for idx, q in enumerate(all_focused_questions, 1):
    q["question_number"] = idx
    q["id"] = f"FZ_Q{idx:03d}"

cat_counts = Counter(q["category"] for q in all_focused_questions)
print("\nCategory breakdown (20 per topic):")
for cat, cnt in sorted(cat_counts.items()):
    print(f"  - {cat}: {cnt} questions")

output_file = "focused_zen_questions_data.json"
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(all_focused_questions, f, indent=2)

print(f"\nSuccessfully wrote {len(all_focused_questions)} questions to {output_file}")
