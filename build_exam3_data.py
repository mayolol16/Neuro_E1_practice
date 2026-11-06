#!/usr/bin/env python3
import fitz
import re
import json
import base64
import os

def build_exam3():
    pdf_path = "/Users/markyoussef_1/Downloads/Ex3-USMLEPracANS.pdf"
    doc = fitz.open(pdf_path)

    # 1. Pre-extract image data URIs
    img_map = {
        '8': 22,
        '11': 25,
        '12': 26,
        '15': 29,
        '17': 34,
        '20': 37,
        '22': 40,
        '26': 43,
        '84': 102,
        '88A': 107,
        '106': 126,
        '108': 131,
        '109': 135,
        '110': 138,
        '112': 141,
        '113': 142,
        '115': 145,
        '116': 145,
    }

    img_uris = {}
    for qid, xref in img_map.items():
        img_dict = doc.extract_image(xref)
        b64 = base64.b64encode(img_dict['image']).decode('utf-8')
        ext = img_dict['ext']
        img_uris[qid] = f'data:image/{ext};base64,{b64}'

    # 2. Extract full text
    full_text_pages = []
    for page in doc:
        full_text_pages.append(page.get_text())
    full_text = "\n".join(full_text_pages)

    # Clean copyright footers and standalone page number lines
    lines = full_text.split('\n')
    cleaned_lines = []
    for line in lines:
        s = line.strip()
        if 'This document contains copyright' in s: continue
        if 'information from publisher subscriptions' in s: continue
        if 'through the UB libraries.' in s: continue
        if 'shared outside of UB.' in s: continue
        if s.isdigit() and int(s) <= 60: continue
        cleaned_lines.append(s)

    text = '\n'.join(cleaned_lines)
    # Fix known formatting quirks
    text = re.sub(r'(\n\s*89\.)([A-Z])', r'\1 \2', text)
    text = re.sub(r'at the age of\s*\n\s*60\.', 'at the age of 60.', text)

    # Categories
    categories = [
        'Demyelinating Diseases',
        'Cerebellum',
        'Tumors',
        'Infections',
        'CBIL: Epilepsy',
        'Blood Supply',
        'Cerebrovascular Disease',
        'Brainstem Stroke',
        'Dementia'
    ]

    def classify_question(qid, full_body):
        b = full_body.lower()
        
        # Specific overrides
        if qid == '91': return 'Brainstem Stroke'
        if qid == '7': return 'Brainstem Stroke'
        if qid == '24': return 'Brainstem Stroke'
        if qid in ['105', '106', '107']: return 'Brainstem Stroke'
        if qid == '109': return 'Brainstem Stroke'
        if qid in ['3', '4']: return 'Tumors' # Schwannoma CPA
        if qid == '5': return 'Brainstem Stroke' # Oculomotor dilated pupil
        if qid == '8': return 'Blood Supply' # ACA angiogram occlusion
        if qid == '11': return 'Demyelinating Diseases' # Subacute combined degeneration myelin
        if qid == '12': return 'Tumors' # NF-2 bilateral schwannomas
        if qid == '15': return 'Cerebrovascular Disease' # Putamen infarct lenticulostriate
        if qid == '17': return 'Tumors' # Sturge-Weber
        if qid == '19': return 'Dementia' # Huntington chorea
        if qid == '20': return 'Tumors' # Meningioma
        if qid == '22': return 'Dementia' # Frontotemporal dementia
        if qid == '26': return 'Demyelinating Diseases' # MS
        if qid in ['27', '28']: return 'Demyelinating Diseases' # MS / TM
        if qid in ['29', '30', '31', '32']: return 'Tumors'
        if qid in ['33', '40', '41', '42', '43', '48', '49', '50', '51', '52', '53', '54', '55']: return 'CBIL: Epilepsy'
        if qid in ['35', '36', '47']: return 'Dementia' if qid != '36' else 'Infections'
        if qid in ['37', '38']: return 'Demyelinating Diseases'
        if qid in ['44', '45', '46']: return 'Cerebrovascular Disease'
        if qid in ['56', '57', '60']: return 'Cerebrovascular Disease'
        if qid == '58': return 'Dementia'
        if qid in ['59', '61']: return 'Demyelinating Diseases'
        if qid == '62': return 'Dementia'
        if qid in ['68', '70', '71', '72']: return 'Dementia'
        if qid in ['73', '76']: return 'Demyelinating Diseases'
        if qid in ['74', '79']: return 'CBIL: Epilepsy'
        if qid in ['75']: return 'Brainstem Stroke'
        if qid in ['77']: return 'Dementia'
        if qid in ['78']: return 'Infections'
        if qid in ['80']: return 'Dementia' # Korsakoff
        if qid in ['81']: return 'Cerebrovascular Disease' # ACA infarct
        if qid in ['82']: return 'Tumors' # MPNST
        if qid in ['83']: return 'Cerebrovascular Disease' # Remote infarct cavity
        if qid in ['84']: return 'Dementia' # Alzheimer NFT
        if qid in ['85']: return 'Tumors' # Astrocytoma
        if qid in ['86']: return 'CBIL: Epilepsy' # Phenytoin toxicity
        if qid in ['87']: return 'Demyelinating Diseases' # MS
        if qid in ['88A', '88B', '88C']: return 'Cerebrovascular Disease' # Hypertensive intracerebral hematoma
        if qid in ['89']: return 'Dementia' # Donepezil
        if qid in ['90']: return 'Brainstem Stroke'
        if qid in ['92', '93']: return 'Cerebellum'
        if qid in ['94']: return 'Dementia' # Kluver-Bucy / Amygdala
        if qid in ['95', '96']: return 'Cerebrovascular Disease' # Lacunar / lenticulostriate
        if qid in ['97']: return 'Cerebrovascular Disease' # Stroke management / tPA
        if qid in ['98', '99', '100']: return 'Cerebrovascular Disease' # Aphasia MCA
        if qid in ['101', '102', '103']: return 'Dementia'
        if qid in ['104']: return 'Blood Supply' # Ophthalmic / internal carotid
        if qid in ['108']: return 'Cerebrovascular Disease' # Watershed infarct
        if qid in ['110', '111']: return 'Infections' # HSV-1
        if qid in ['112']: return 'Infections' # PML
        if qid in ['113']: return 'Infections' # Toxoplasmosis
        if qid in ['114']: return 'Dementia' # bvFTD
        if qid in ['115', '116']: return 'Demyelinating Diseases' # MS

        # Fallback keywords
        if any(k in b for k in ['epilepsy', 'seizure', 'eeg', 'carbamazepine', 'phenytoin', 'ethosuximide', 'valproic']):
            return 'CBIL: Epilepsy'
        if any(k in b for k in ['creutzfeldt', 'toxoplasmosis', 'hsv', 'jc virus', 'pml', 'meningitis', 'encephalitis']):
            return 'Infections'
        if any(k in b for k in ['astrocytoma', 'glioblastoma', 'meningioma', 'schwannoma', 'oligodendroglioma', 'tumor']):
            return 'Tumors'
        if any(k in b for k in ['multiple sclerosis', 'demyelinat', 'oligoclonal', 'neuromyelitis', 'aquaporin', 'guillain']):
            return 'Demyelinating Diseases'
        if any(k in b for k in ['alzheimer', 'dementia', 'donepezil', 'frontotemporal', 'pick', 'lewy body', 'huntington']):
            return 'Dementia'
        if any(k in b for k in ['wallenberg', 'medullary', 'weber', 'alternating hemiplegia', 'brainstem']):
            return 'Brainstem Stroke'
        if any(k in b for k in ['cerebell', 'ataxia', 'intention tremor', 'dysmetria', 'vermis']):
            return 'Cerebellum'
        if any(k in b for k in ['stroke', 'infarct', 'ischemi', 'tpa', 'hemorrhage', 'hematoma', 'aneurysm']):
            return 'Cerebrovascular Disease'
        return 'Blood Supply'

    q_regex = re.compile(r'(?:^|\n)\s*(\d{1,3}[A-C]?)\.\s+(.+?)(?=(?:\n\s*\d{1,3}[A-C]?\.\s+|$))', re.DOTALL)
    matches = list(q_regex.finditer(text))

    opt_line_pat = re.compile(r'^([*]?)\s*([A-Ga-g])(?:[\.\)]|\s+)\s*(.*)$')

    def find_best_options_chain(b_lines):
        candidate_chains = []
        for i in range(len(b_lines)):
            m_a = opt_line_pat.match(b_lines[i])
            if m_a and m_a.group(2).upper() == 'A':
                has_marker = (m_a.group(1) == '*') or b_lines[i].startswith(('A.', 'a.', 'A)', 'a)'))
                chain = [(i, m_a.group(1) == '*', 'A', m_a.group(3))]
                curr_letter = 'A'
                curr_idx = i
                while True:
                    next_letter = chr(ord(curr_letter) + 1)
                    found = False
                    for j in range(curr_idx + 1, min(curr_idx + 4, len(b_lines))):
                        m_next = opt_line_pat.match(b_lines[j])
                        if m_next and m_next.group(2).upper() == next_letter:
                            chain.append((j, m_next.group(1) == '*', next_letter, m_next.group(3)))
                            curr_letter = next_letter
                            curr_idx = j
                            found = True
                            break
                    if not found:
                        break
                if len(chain) >= 3:
                    score = len(chain) * 10
                    if has_marker: score += 5
                    if i == 0 and not has_marker: score -= 15
                    candidate_chains.append((score, chain))
        if candidate_chains:
            candidate_chains.sort(key=lambda x: x[0], reverse=True)
            return candidate_chains[0][1]
        return None

    questions = []

    for m in matches:
        qid = m.group(1).strip()
        body = m.group(2).strip()
        b_lines = [l.strip() for l in body.split('\n') if l.strip()]

        if qid == '91':
            options = [
                {"letter": "A", "is_correct": False, "text": "PCA / rostral midbrain — Drooping right eyelid, laterally deviated right eye, dilated right pupil (CN III), weak left arm/leg & left Babinski (Weber syndrome)"},
                {"letter": "B", "is_correct": False, "text": "Anterior Spinal Artery / rostral medulla — Weak right arm/leg, right Babinski sign, impaired touch/proprioception, and tongue deviation to the left (Medial medullary syndrome)"},
                {"letter": "C", "is_correct": False, "text": "Basilar penetrating branch / caudal pons — Weak left arm/leg, left Babinski sign, impaired touch/proprioception, medial deviation of right eye (CN VI), and slight left tongue deviation"},
                {"letter": "D", "is_correct": False, "text": "PICA / rostral medulla — Impaired pain/temperature over right body and left face, ataxic left arm/leg, and impaired left palate elevation (Wallenberg lateral medullary syndrome)"},
                {"letter": "E", "is_correct": True, "text": "All of the above vascular territories and clinical localization syndromes are correctly matched"}
            ]
            explanation = ("Comprehensive Brainstem Vascular Localization Review:\n\n"
                           "• PCA / rostral midbrain (Weber syndrome): Involves emerging CN III fibers (ipsilateral oculomotor palsy: ptosis, down-and-out eye, dilated pupil) and crus cerebri corticospinal tract (contralateral hemiparesis).\n\n"
                           "• Anterior Spinal Artery / rostral medulla (Medial medullary syndrome): Involves hypoglossal nerve CN XII (ipsilateral tongue deviation), medial lemniscus (contralateral loss of vibration/proprioception), and pyramid (contralateral hemiparesis).\n\n"
                           "• Basilar branch / caudal pons (Millard-Gubler / Foville): Involves CN VI (ipsilateral medial strabismus), facial motor/colliculus, and corticospinal fibers (contralateral hemiplegia).\n\n"
                           "• PICA / rostral medulla (Wallenberg syndrome): Involves nucleus ambiguus (dysphagia, hoarseness, loss of gag reflex), vestibular nuclei (vertigo, nystagmus), spinal trigeminal nucleus (ipsilateral facial pain/temp loss), spinothalamic tract (contralateral body pain/temp loss), and inferior cerebellar peduncle (ataxia).\n\n"
                           "• Basilar branch / mid-pons: Involves CN V motor nucleus (ipsilateral jaw weakness), chief sensory nucleus (ipsilateral facial touch loss), and middle cerebellar peduncle (ipsilateral ataxia).")
            
            questions.append({
                "id": f"exam3_q91",
                "q_num": "91",
                "stem": "Which of the following blood vessels and brainstem locations is correctly matched with its clinical syndrome?",
                "category": "Brainstem Stroke",
                "source": "USMLE Step 1 Exam 3 Practice Bank",
                "options": options,
                "correct_idx": 4,
                "explanation": explanation,
                "high_yield_pearl": "Brainstem alternating hemiplegias: Cranial nerve deficit is IPSILATERAL to the lesion; long-tract motor/sensory deficit is CONTRALATERAL.",
                "image": None
            })
            continue

        chain = find_best_options_chain(b_lines)
        if not chain:
            print(f"Error: No option chain for Q{qid}")
            continue

        stem = ' '.join(b_lines[:chain[0][0]]).strip()
        stem = re.sub(r'\s+', ' ', stem)

        options = []
        correct_idx = 0

        for c_i, (l_idx, is_cor, let, txt) in enumerate(chain):
            if c_i + 1 < len(chain):
                next_l_idx = chain[c_i + 1][0]
                opt_lines = [txt] + b_lines[l_idx + 1: next_l_idx]
            else:
                # Last option
                opt_lines = [txt]
                # Check if subsequent lines are continuation
                curr = l_idx + 1
                while curr < len(b_lines):
                    line_curr = b_lines[curr]
                    # Check if line_curr is explanation:
                    # Explanations in this PDF start with capitalized sentences that explain physiology, diagnosis, etc.
                    # An option continuation usually starts with lowercase or continuation words
                    if line_curr.startswith(('The ', 'This ', 'A diagnosis ', 'A lesion ', 'A simple ', 'A significant ', 'A ruptured ', 'A 4.5', 'A major ', 'Donepezil', 'NMO ', 'Once ', 'Astrocytomas', 'Characteristics', 'Hypnic', 'In this ', 'Homonymous', 'These ', 'Loss ', 'Toxoplasmosis', 'PML', 'Exercise', 'Exercise programs', 'Treatment', 'Treatment for', 'Obtaining', 'No treatment', 'Brain MRI', 'Multiple sclerosis', 'PICA', 'Longitudinally', 'Hyperdense')):
                        break
                    if line_curr[0].islower() or opt_lines[-1].endswith(('of', 'the', 'and', 'in', 'with', 'to', 'for', 'Na+', 'recent')):
                        opt_lines.append(line_curr)
                        curr += 1
                    else:
                        break
                next_l_idx = curr

            full_opt_txt = ' '.join(opt_lines).strip()
            full_opt_txt = re.sub(r'\s+', ' ', full_opt_txt)
            if is_cor:
                correct_idx = len(options)
            options.append({
                "letter": let,
                "is_correct": is_cor,
                "text": full_opt_txt
            })

        # Explanation is lines from next_l_idx onwards
        exp_lines = b_lines[next_l_idx:]
        explanation = ' '.join(exp_lines).strip()
        explanation = re.sub(r'\s+', ' ', explanation)
        if not explanation:
            explanation = "Refer to clinical neuroanatomy principles and patient presentation."

        category = classify_question(qid, body)
        img_uri = img_uris.get(qid, None)

        questions.append({
            "id": f"exam3_q{qid.lower()}",
            "q_num": qid,
            "stem": stem,
            "category": category,
            "source": "USMLE Step 1 Exam 3 Practice Bank",
            "options": options,
            "correct_idx": correct_idx,
            "explanation": explanation,
            "high_yield_pearl": f"High-Yield Rule: {category}",
            "image": img_uri
        })

    print(f"Total parsed questions: {len(questions)}")
    out_json_path = "/Users/markyoussef_1/.gemini/antigravity-ide/scratch/usmle_exam1/exam3_questions.json"
    with open(out_json_path, 'w', encoding='utf-8') as f:
        json.dump(questions, f, indent=2, ensure_ascii=False)
    print(f"Successfully saved {len(questions)} questions to {out_json_path}")

    # Category counts
    cat_counts = {}
    for q in questions:
        c = q['category']
        cat_counts[c] = cat_counts.get(c, 0) + 1
    print("\nCategory Distribution:")
    for c, cnt in sorted(cat_counts.items()):
        print(f"  {c}: {cnt} questions")

if __name__ == "__main__":
    build_exam3()
