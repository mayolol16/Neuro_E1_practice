import json
import base64
import os
import re

pdf_text_path = '/Users/markyoussef_1/.gemini/antigravity-ide/brain/f5d39382-784d-4636-a513-d94a978a1ea0/scratch/extracted_pdf_text.txt'
img_dir = '/Users/markyoussef_1/.gemini/antigravity-ide/scratch/usmle_exam1/images'

with open(pdf_text_path, 'r', encoding='utf-8') as f:
    raw = f.read()

# Clean page marks and headers
cleaned = re.sub(r'=== PAGE \d+ ===\s*\n\s*\d+\s*\n', '\n', raw)
cleaned = re.sub(r'EXAM 1 PRACTICE QUESTIONS', '', cleaned)

# Split by question numbers: (e.g. 1., 2., ... 52A., 52B., 52C., etc.)
pattern = r'(?:\n|^)\s*(\d+[A-Za-z]?)\s*[\.:]\s*'
splits = list(re.finditer(pattern, cleaned))

def get_b64(fname):
    p = os.path.join(img_dir, fname)
    if os.path.exists(p):
        with open(p, 'rb') as f:
            data = base64.b64encode(f.read()).decode('utf-8')
            return f'data:image/png;base64,{data}'
    return None

images_map = {
    '15': get_b64('q15_figure.png'),
    '18': get_b64('q18_figure.png'),
    '25': get_b64('q25_figure_enhanced.png'),
    '50': get_b64('q50_figure.png'),
    '51': get_b64('q50_figure.png'),
    '52A': get_b64('q52_figure.png'),
    '52B': get_b64('q52_figure.png'),
    '52C': get_b64('q52_figure.png'),
    '53': get_b64('q53_figure.png'),
    '54': get_b64('q54_figure.png'),
    '113': get_b64('q113_figure.png'),
    '117': get_b64('q117_figure.png'),
}

copyright_pattern = re.compile(r'This document contains copyright information.*?outside of UB\.?', re.DOTALL | re.IGNORECASE)

categories = [
    'Central Nervous System Anatomy',
    'Central Nervous System Development',
    'Neurotransmitters and Action Potentials',
    'Ventricular System',
    'Acetylcholine / Neuromuscular Junction Disorder',
    'Neuroimaging',
    'Tactile Pathway',
    'Spinal Cord',
    'Pain Pathway',
    'Trigeminal Pathway',
    'Anesthetic & NMJ Blocking Agents',
    'Headache',
    'Cannabis Management',
    'Pathways and Opioids',
    'Traumatic Brain Injuries',
    'Meningitis'
]

category_mapping = {
    '1': 'Ventricular System', # constriction of cerebral aqueduct
    '2': 'Meningitis', # lumbar tap to sample CSF in suspected meningitis
    '3': 'Central Nervous System Anatomy', # internal capsule, white vs gray matter
    '4': 'Traumatic Brain Injuries', # TBI, microglia phagocytosis in CNS injury
    '5': 'Central Nervous System Anatomy', # knee-jerk & jaw-jerk reflex circuits
    '6': 'Ventricular System', # communicating hydrocephalus, arachnoid granulations
    '7': 'Central Nervous System Development', # neural tube defect / anencephaly
    '8': 'Traumatic Brain Injuries', # baseball hit head, skull fracture, epidural hematoma
    '9': 'Ventricular System', # pseudotumor cerebri, papilledema, idiopathic intracranial hypertension / elevated ICP
    '10': 'Neurotransmitters and Action Potentials', # axon ionic changes, Na+/K+ gradients
    '11': 'Neurotransmitters and Action Potentials', # synaptic plasticity, NMDA and AMPA
    '12': 'Spinal Cord', # gunshot wound, Brown-Sequard syndrome / hemisection
    '13': 'Central Nervous System Development', # rhombencephalon, foramina of Magendie/Luschka
    '14': 'Pathways and Opioids', # opioid tolerance
    '15': 'Tactile Pathway', # myelin stain dorsal columns / tabes dorsalis
    '16': 'Central Nervous System Anatomy', # VP thalamic nucleus (VPL/VPM)
    '17': 'Headache', # trigeminal neuralgia / facial pain, carbamazepine
    '18': 'Neuroimaging', # CT scan showing right sided edema
    '19': 'Traumatic Brain Injuries', # skull fracture, epidural hematoma middle meningeal artery
    '20': 'Pain Pathway', # crossed pain/temp loss (ipsilateral face, contralateral body), lateral medullary syndrome
    '21': 'Traumatic Brain Injuries', # fell off ladder, lucid interval, epidural hematoma
    '22': 'Neuroimaging', # CT vs MRI, non-contrast CT for acute hemorrhage
    '23': 'Central Nervous System Anatomy', # lateral medullary (Wallenberg) syndrome
    '24': 'Spinal Cord', # loss of pinprick at nipple level (T4 dermatome -> T2 lesion)
    '25': 'Trigeminal Pathway', # lesion of spinal trigeminal tract
    '26': 'Spinal Cord', # syringomyelia / cape-like sensory loss
    '27': 'Tactile Pathway', # tactile loss from nipple down, fasciculus cuneatus/gracilis
    '28': 'Central Nervous System Development', # neural tube embryonic week 3-4
    '29': 'Tactile Pathway', # medial lemniscus in pons/brainstem
    '30': 'Pain Pathway', # anterolateral system / spinothalamic tract
    '31': 'Pain Pathway', # ALS contralateral pain loss
    '32': 'Tactile Pathway', # internal arcuate fibers / dorsal column nuclei
    '33': 'Spinal Cord', # gunshot to spine, hemisection deficits
    '34': 'Ventricular System', # noncommunicating hydrocephalus obstruction sites
    '35': 'Tactile Pathway', # sensory ataxia / tabes dorsalis slapping gait
    '36': 'Central Nervous System Anatomy', # blood supply of internal capsule
    '37': 'Headache', # migraine without aura, NSAID / triptans
    '38': 'Trigeminal Pathway', # referred facial/jaw pain, primary afferent convergence in spinal trigeminal nucleus
    '39': 'Pathways and Opioids', # descending analgesia, periaqueductal gray (PAG)
    '40': 'Traumatic Brain Injuries', # motorcycle accident, subdural hematoma
    '41': 'Tactile Pathway', # Pacinian corpuscles / vibration and deep pressure
    '42': 'Traumatic Brain Injuries', # coup-contrecoup injury, frontal/temporal contusions
    '43': 'Tactile Pathway', # Meissner corpuscles / two-point discrimination
    '44': 'Tactile Pathway', # tuning fork vibration, dorsal column pathway
    '45': 'Ventricular System', # CSF composition vs plasma
    '46': 'Meningitis', # bacterial meningitis CSF analysis (high protein, low glucose)
    '47': 'Meningitis', # viral vs bacterial meningitis CSF findings
    '48': 'Ventricular System', # normal pressure hydrocephalus (triad: wet, wobbly, wacky)
    '49': 'Traumatic Brain Injuries', # rock climbing fall, lucid interval, temporal fracture
    '50': 'Neuroimaging', # MRI ventriculomegaly and increased ICP
    '51': 'Neuroimaging', # MRI noncommunicating hydrocephalus
    '52A': 'Traumatic Brain Injuries', # CT scan bridging vein laceration in subdural
    '52B': 'Traumatic Brain Injuries', # right pupil dilation due to uncal herniation
    '52C': 'Traumatic Brain Injuries', # CT banana shape acute subdural hematoma
    '53': 'Neuroimaging', # CT scan hydrocephalus ex vacuo in Alzheimer patient
    '54': 'Neuroimaging', # CT scan intraparenchymal hematoma in hypertensive crisis
    '55_1': 'Headache', # temporal (giant cell) arteritis, steroid management
    '55_2': 'Spinal Cord', # spinal cord injury loss of touch/vibration, left dorsal column
    '56': 'Neurotransmitters and Action Potentials', # snake venom voltage-gated Na+ channels
    '57': 'Acetylcholine / Neuromuscular Junction Disorder', # botulinum toxin vs ACh release
    '58': 'Anesthetic & NMJ Blocking Agents', # succinylcholine malignant hyperthermia/phase block
    '59': 'Anesthetic & NMJ Blocking Agents', # non-depolarizing NMJ blockers (vecuronium/rocuronium)
    '60': 'Acetylcholine / Neuromuscular Junction Disorder', # myasthenia gravis autoimmune anti-AChR
    '61': 'Central Nervous System Anatomy', # anterior spinal artery infarct
    '62': 'Neurotransmitters and Action Potentials', # cortical neuron stimulation, IPSP / GABA
    '63': 'Neurotransmitters and Action Potentials', # K+ equilibrium potential, Nernst (-90 mV)
    '64': 'Pain Pathway', # phantom limb pain, cortical reorganization
    '65': 'Pain Pathway', # spinothalamic vs spinoreticular tracts, affective pain
    '66': 'Spinal Cord', # Brown-Sequard syndrome right leg sensory deficits
    '67': 'Pathways and Opioids', # opioid receptor downregulation & tolerance
    '68': 'Tactile Pathway', # mechanoreceptors in diabetic neuropathy
    '69': 'Tactile Pathway', # dorsal column-medial lemniscal decussation
    '70': 'Pathways and Opioids', # codeine physical dependence and withdrawal
    '71': 'Pain Pathway', # sunburn, primary hyperalgesia and allodynia
    '72': 'Pain Pathway', # scraped skin, acute nociceptive pain
    '73': 'Pathways and Opioids', # descending pain pathway PAG & RVM enkephalins
    '74': 'Spinal Cord', # stab wound, anterior white commissure / central canal
    '75': 'Tactile Pathway', # Romberg sign, posterior columns at lumbar level
    '76': 'Traumatic Brain Injuries', # epidural space bleeding, handball accident
    '77': 'Pain Pathway', # gate control theory / descending pain modulation
    '78': 'Headache', # episodic migraine management in obesity
    '79': 'Traumatic Brain Injuries', # Glasgow Coma Scale (GCS) scoring
    '80': 'Tactile Pathway', # stocking-glove neuropathy vs dorsal columns
    '81': 'Acetylcholine / Neuromuscular Junction Disorder', # acetylcholinesterase kinetics
    '82': 'Cannabis Management', # endocannabinoid system, CB1 receptors, THC
    '83': 'Anesthetic & NMJ Blocking Agents', # lidocaine pKa, Henderson-Hasselbalch, ionization
    '84': 'Pathways and Opioids', # cancer pain management, step ladder opioids
    '85': 'Cannabis Management', # medical cannabis, cannabinoids in pain & nausea
    '86': 'Pathways and Opioids', # opioid antagonists: naloxone vs naltrexone
    '87': 'Pathways and Opioids', # heroin withdrawal syndrome (mydriasis, piloerection)
    '88': 'Cannabis Management', # cannabis hyperemesis syndrome / synthetic cannabinoids
    '89': 'Pathways and Opioids', # full vs partial opioid agonists, buprenorphine
    '90': 'Anesthetic & NMJ Blocking Agents', # reversal of NMJ block with neostigmine/glycopyrrolate
    '91': 'Pathways and Opioids', # post-op opioid respiratory depression & sedation
    '92': 'Anesthetic & NMJ Blocking Agents', # succinylcholine depolarizing block characteristics
    '93': 'Anesthetic & NMJ Blocking Agents', # balanced anesthesia, opioids in cardiac surgery
    '94': 'Anesthetic & NMJ Blocking Agents', # nitrous oxide (MAC, second gas effect, B12)
    '95': 'Anesthetic & NMJ Blocking Agents', # inhaled anesthetic blood:gas partition coefficient
    '96': 'Anesthetic & NMJ Blocking Agents', # Minimum Alveolar Concentration (MAC) determinants
    '97': 'Acetylcholine / Neuromuscular Junction Disorder', # myasthenia gravis treatment, pyridostigmine
    '98': 'Acetylcholine / Neuromuscular Junction Disorder', # cholinesterase inhibitors autonomic effects
    '99': 'Acetylcholine / Neuromuscular Junction Disorder', # parathion organophosphate toxicity
    '100': 'Acetylcholine / Neuromuscular Junction Disorder', # organophosphate poisoning / respiratory failure
    '101': 'Acetylcholine / Neuromuscular Junction Disorder', # anticholinergic toxicity vs cholinergic agents
    '102': 'Headache', # cluster headache clinical presentation & treatment (100% O2)
    '103': 'Headache', # migraine with aura, triptan contraindications (coronary disease)
    '104': 'Headache', # tension-type headache presentation and treatment
    '105': 'Neurotransmitters and Action Potentials', # GABA-A receptor modulation by benzodiazepines/alcohol
    '106': 'Acetylcholine / Neuromuscular Junction Disorder', # Lambert-Eaton myasthenic syndrome (anti-VGCC)
    '107': 'Headache', # medication overuse (rebound) headache
    '108': 'Ventricular System', # normal pressure hydrocephalus diagnostic tap test
    '109': 'Trigeminal Pathway', # trigeminal neuralgia microvascular decompression
    '110': 'Pathways and Opioids', # hydromorphone overdose, short half-life naloxone drip
    '111': 'Tactile Pathway', # subacute combined degeneration (B12 vs folate neuropathy)
    '112': 'Traumatic Brain Injuries', # uncal herniation compressing CN III (dilated pupil)
    '113': 'Traumatic Brain Injuries', # skull fracture epidural hemorrhage middle meningeal
    '114': 'Traumatic Brain Injuries', # chronic subdural hemorrhage in elderly/alcoholic
    '115': 'Central Nervous System Anatomy', # nuclei vs ganglia, gray vs white matter
    '116': 'Central Nervous System Anatomy', # oligodendrocytes vs Schwann cells myelination
    '117': 'Central Nervous System Anatomy', # multipolar neuron histology identification
    '118': 'Central Nervous System Anatomy', # fibrous astrocytes and oligodendrocytes in white matter
    '119': 'Central Nervous System Anatomy', # astrocytes glutamate reuptake / EAAT
    '120': 'Central Nervous System Development', # neural crest derivative cells & ganglia
    '121': 'Meningitis', # acute bacterial meningitis workup: LP, blood cultures, empiric therapy
    '122': 'Pain Pathway', # neuropathic pain management, tricyclic antidepressants / gabapentinoids
}

known_exp_starters = {
    '2': 'Subarachnoid cisterns are expanded',
    '33': 'A lesion of the AL:S at T2',
    '36': 'Migraine headaches are unilateral and can be accompanied',
    '38': 'This case involves referred pain.',
    '41': 'Descending pain inhibitory pathways originate',
    '49': 'A young healthy patient who sustains head trauma',
    '59': 'A general definition of referred pain is',
    '61': 'Touch (as well as vibration and proprioception)',
    '64': 'If a body part is amputated',
    '66': 'The lateral postcentral gyrus within the parietal lobe',
    '71': 'A temperature of 40°C activates',
    '77': 'Perhaps one of the most important discoveries',
    '79': 'The patient described in the vignette would score',
    '94': 'Anemia has not been reported in patients',
    '102': 'Cluster headache is a rare disorder',
    '107': 'A useful clinical approach is to diagnose',
    '109': 'This patient presents with trigeminal neuralgia',
    '110': 'While most opioids have effects that last hours',
    '111': 'Both vitamin B12 and folate deficiency will cause'
}

def clean_text(t):
    return ' '.join(t.split())

questions = []
q55_count = 0

for idx in range(len(splits)):
    q_num = splits[idx].group(1)
    s = splits[idx].end()
    e = splits[idx+1].start() if idx+1 < len(splits) else len(cleaned)
    chunk = cleaned[s:e].strip()
    
    # Handle two Q55s
    lookup_key = q_num
    display_num = q_num
    if q_num == '55':
        q55_count += 1
        lookup_key = f'55_{q55_count}'
        if q55_count == 2:
            display_num = '55b'

    # 1. Locate Option B to cleanly find where Option A begins
    b_match = re.search(r'\n\s*(\*?\s*[Bb])(?:[\.:\s]|(?=\d))', chunk)
    if not b_match:
        print(f'Error Q{q_num}: No B match!')
        continue
    pre_b = chunk[:b_match.start()]
    a_matches = list(re.finditer(r'(?:^|\n)\s*(\*?\s*[Aa])(?:[\.:\s]|(?=\d))', pre_b))
    if not a_matches:
        print(f'Error Q{q_num}: No A match before B!')
        continue
    a_match = a_matches[-1]
    
    stem = clean_text(chunk[:a_match.start()])
    
    # Find all sequential options A -> B -> C -> D (-> E -> F -> G -> H ...)
    opt_starts = [( 'A', a_match.start(), '*' in a_match.group(1), a_match.end() )]
    opt_starts.append(( 'B', b_match.start(), '*' in b_match.group(1), b_match.end() ))
    
    current_pos = b_match.end()
    for next_let in ['C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']:
        m = re.search(rf'\n\s*(\*?\s*[{next_let}{next_let.lower()}])(?:[\.:\s]|(?=\d))', chunk[current_pos:])
        if m:
            start_in_chunk = current_pos + m.start()
            end_in_chunk = current_pos + m.end()
            opt_starts.append(( next_let, start_in_chunk, '*' in m.group(1), end_in_chunk ))
            current_pos = end_in_chunk
        else:
            break
            
    options = []
    correct_idx = None
    
    for o_i in range(len(opt_starts) - 1):
        letter, s_pos, is_star, text_s = opt_starts[o_i]
        next_letter, next_s, _, _ = opt_starts[o_i + 1]
        opt_text = clean_text(chunk[text_s : next_s])
        options.append({'letter': letter, 'is_correct': is_star, 'text': opt_text})
        if is_star:
            correct_idx = o_i
            
    last_letter, last_s, is_star, last_text_s = opt_starts[-1]
    remaining = chunk[last_text_s:].strip()
    
    # Smart split of remaining text into last option choice and explanation
    if q_num in known_exp_starters and known_exp_starters[q_num] in remaining:
        starter = known_exp_starters[q_num]
        idx_split = remaining.find(starter)
        last_choice = clean_text(remaining[:idx_split])
        explanation = remaining[idx_split:].strip()
    else:
        rem_lines = [l.strip() for l in remaining.split('\n') if l.strip()]
        prev_lens = [len(o['text'].split('\n')) for o in options]
        avg_lines = sum(prev_lens) / len(prev_lens) if prev_lens else 1
        cut = 1 if avg_lines <= 1.4 else int(round(avg_lines))
        last_choice = clean_text(' '.join(rem_lines[:cut]))
        explanation = '\n'.join(rem_lines[cut:]).strip()
        
    options.append({'letter': last_letter, 'is_correct': is_star, 'text': last_choice})
    if is_star:
        correct_idx = len(options) - 1
        
    # Clean explanation
    explanation = copyright_pattern.sub('', explanation).strip()
    
    # Specific edge cases for answers and explanations
    if q_num == '63':
        correct_idx = 2 # C: −90 mV
        options[2]['is_correct'] = True
    elif q_num == '70':
        correct_idx = 2 # C: She had developed physical dependence to codeine
        options[2]['is_correct'] = True
    elif q_num == '75' and not explanation:
        explanation = 'Loss of touch, proprioception, and vibration in both legs with preserved pain/temperature sensation, along with a positive Romberg sign and hyporeflexia, indicates bilateral lesion of the posterior/dorsal columns (fasciculus gracilis) at the lumbar spinal cord level.'

    cat = category_mapping.get(lookup_key, 'Central Nervous System Anatomy')
    img_b64 = images_map.get(display_num, None)
    if not img_b64:
        img_b64 = images_map.get(q_num, None)

    questions.append({
        'id': idx + 1,
        'q_num': display_num,
        'stem': stem,
        'options': options,
        'correct_idx': correct_idx,
        'explanation': explanation,
        'category': cat,
        'image': img_b64
    })

out_json_path = '/Users/markyoussef_1/.gemini/antigravity-ide/scratch/usmle_exam1/questions_data.json'
with open(out_json_path, 'w', encoding='utf-8') as f:
    json.dump(questions, f, indent=2)

print(f'Successfully generated {len(questions)} questions into {out_json_path}')

cat_counts = {}
for q in questions:
    c = q['category']
    cat_counts[c] = cat_counts.get(c, 0) + 1

print('\nCategory Distribution:')
for cat in categories:
    print(f'  {cat}: {cat_counts.get(cat, 0)} questions')
