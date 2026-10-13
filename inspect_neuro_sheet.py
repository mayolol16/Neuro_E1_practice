import os
import glob
from pptx import Presentation
import fitz # PyMuPDF

folder = "/Users/markyoussef_1/Downloads/NeuroE1ShEET"
files = sorted(os.listdir(folder))

print(f"Total files in folder: {len(files)}")

lectures = []
content_pps = []
case_pps = []
other = []

for f in files:
    if f.startswith('.'):
        continue
    f_lower = f.lower()
    if "case" in f_lower:
        case_pps.append(f)
    elif "content" in f_lower:
        content_pps.append(f)
    elif f.endswith('.pdf') or "student" in f_lower or "lecture" in f_lower or "disorders" in f_lower:
        lectures.append(f)
    else:
        other.append(f)

print(f"\n--- LECTURES ({len(lectures)}) ---")
for f in lectures:
    print(" ", f)

print(f"\n--- CONTENT POWERPOINTS ({len(content_pps)}) ---")
for f in content_pps:
    print(" ", f)

print(f"\n--- CASE POWERPOINTS ({len(case_pps)}) ---")
for f in case_pps:
    print(" ", f)

if other:
    print(f"\n--- OTHER ({len(other)}) ---")
    for f in other:
        print(" ", f)
