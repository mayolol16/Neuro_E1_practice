# -*- coding: utf-8 -*-
"""
patch_final_builder.py
Adds rawExam2Questions, exam2Categories, and Exam 2 CSS into update_builder.py,
then executes update_builder.py to compile the unified index.html.
"""
import os

BUILDER_PATH = '/Users/markyoussef_1/.gemini/antigravity-ide/scratch/usmle_exam1/update_builder.py'

def main():
    with open(BUILDER_PATH, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Add rawExam2Questions and exam2Categories
    cat_target = 'const inHouseCategories = """ + inhouse_categories_json_str + """;'
    cat_addition = '''const inHouseCategories = """ + inhouse_categories_json_str + """;
    const rawExam2Questions = """ + exam2_json_data_str + """;
    const exam2Categories = """ + exam2_categories_json_str + """;'''

    if cat_target in content and 'const rawExam2Questions' not in content:
        content = content.replace(cat_target, cat_addition, 1)
        print("Added rawExam2Questions and exam2Categories to script data.")

    # 2. Add timer CSS
    timer_target = '''.timer-box.focused-zen {
      border-color: rgba(139, 92, 246, 0.4);
      color: #c084fc;
    }'''
    timer_addition = '''.timer-box.exam2 {
      border-color: rgba(56, 189, 248, 0.4);
      color: #38bdf8;
    }

    .timer-box.focused-zen {
      border-color: rgba(139, 92, 246, 0.4);
      color: #c084fc;
    }'''

    if timer_target in content and '.timer-box.exam2' not in content:
        content = content.replace(timer_target, timer_addition, 1)
        print("Added .timer-box.exam2 CSS.")

    # 3. Add q-track-tag and cat-item CSS
    tag_target = '''.q-track-tag.focused-zen {
      background: rgba(139, 92, 246, 0.2);
      color: #c084fc;
      border-color: rgba(139, 92, 246, 0.4);
    }'''

    tag_addition = '''.q-track-tag.exam2 {
      background: rgba(14, 165, 233, 0.2);
      color: #38bdf8;
      border-color: rgba(14, 165, 233, 0.4);
    }

    .cat-item.exam2-cat.active {
      background: rgba(14, 165, 233, 0.15);
      border-color: #0ea5e9;
    }

    .q-track-tag.focused-zen {
      background: rgba(139, 92, 246, 0.2);
      color: #c084fc;
      border-color: rgba(139, 92, 246, 0.4);
    }'''

    if tag_target in content and '.q-track-tag.exam2' not in content:
        content = content.replace(tag_target, tag_addition, 1)
        print("Added .q-track-tag.exam2 CSS.")

    with open(BUILDER_PATH, 'w', encoding='utf-8') as f:
        f.write(content)

    print("update_builder.py successfully patched.")

if __name__ == '__main__':
    main()
