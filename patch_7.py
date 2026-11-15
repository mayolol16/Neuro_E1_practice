import json

with open('/Users/markyoussef_1/.gemini/antigravity-ide/scratch/usmle_exam1/exam3_high_yield_questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

overrides = {
    69: {
        'B': 'Left middle cerebral artery inferior division; superior temporal lobe'
    },
    76: {
        'A': 'Superficial veins drain to superior sagittal sinus, and deep veins drain to straight sinus',
        'B': 'Deep cerebral veins drain to internal carotids, and superficial veins drain to cavernous sinus',
        'C': 'Superficial veins drain to straight sinus, and deep veins drain to transverse sinus',
        'D': 'Dural sinuses drain to vertebral veins, and superficial veins drain to jugular veins',
        'E': 'Superior sagittal sinus drains to cavernous sinus, and straight sinus drains to petrosal sinuses'
    },
    100: {
        'A': 'Left red nucleus and oculomotor nerve fibers',
        'B': 'Right corticospinal and corticobulbar tracts',
        'C': 'Left medial lemniscus and spinothalamic tract',
        'D': 'Right superior cerebellar peduncle and substantia nigra',
        'E': 'Left dentate nucleus and cerebellar cortex'
    },
    111: {
        'A': 'Hyperorality, hypersexuality, and psychic blindness',
        'B': 'Anterograde amnesia with preserved social comportment',
        'C': 'Fluent paraphasic speech with impaired comprehension',
        'D': 'Violent unilateral choreiform flinging movements',
        'E': 'Inability to recognize familiar objects visually'
    },
    125: {
        'A': 'Focal aware motor seizure with retained consciousness',
        'B': 'Focal impaired awareness seizure with automatisms',
        'C': 'Generalized typical absence seizure without aura',
        'D': 'Generalized atonic seizure with sudden drop attack',
        'E': 'Generalized tonic seizure with sustained stiffening'
    },
    131: {
        'A': 'Both seizure types originate simultaneously from bilateral cerebral hemispheres',
        'B': 'Focal seizures invariably cause complete immediate loss of consciousness',
        'C': 'Focal seizures begin in one hemisphere, whereas generalized involve both hemispheres',
        'D': 'Generalized seizures originate from a discrete circumscribed cortical focus',
        'E': 'Focal and generalized seizures display identical electroencephalographic patterns'
    },
    146: {
        'A': 'Neuronal channelopathy (voltage-gated potassium channel mutation)',
        'B': 'Systemic metabolic disturbance (acute profound hypoglycemia)',
        'C': 'Focal intracranial structural lesion (oligodendroglioma)',
        'D': 'Benign genetic syndrome (familial febrile convulsions)',
        'E': 'Substance withdrawal syndrome (acute sedative cessation)'
    }
}

for q in questions:
    qnum = int(q['q_num'])
    if qnum in overrides:
        for opt in q['options']:
            if opt['letter'] in overrides[qnum]:
                opt['text'] = overrides[qnum][opt['letter']]

with open('/Users/markyoussef_1/.gemini/antigravity-ide/scratch/usmle_exam1/exam3_high_yield_questions.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, indent=2, ensure_ascii=False)

print("Applied patch_7.py successfully")
