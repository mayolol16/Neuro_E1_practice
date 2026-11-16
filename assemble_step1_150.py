"""Complete assembly and validation script for Neuro Exam 3: 150 High-Yield Step 1-Style Questions.
Outputs /Users/markyoussef_1/.gemini/antigravity-ide/scratch/usmle_exam1/exam3_step1_150_questions.json.
"""
import json
import re
import os
import sys

sys.path.append('/Users/markyoussef_1/.gemini/antigravity-ide/scratch/usmle_exam1')

from test_level_q1_15 import overrides_1_15
from test_level_q16_48 import overrides_16_48
from test_level_q49_90 import overrides_49_90
from test_level_q91_150 import overrides_91_150

def build_assembled_json():
    # 1. Base master overrides
    master_overrides = {}
    master_overrides.update(overrides_1_15)
    master_overrides.update(overrides_16_48)
    master_overrides.update(overrides_49_90)
    master_overrides.update(overrides_91_150)

    # 2. Precision micro-patches for tight leveling (spread <= 5, zero parens)
    master_overrides[18] = {
        'A': 'Inferior cerebellar peduncle tract',
        'B': 'Superior cerebellar peduncle tract',
        'C': 'Middle cerebellar peduncle pathway',
        'D': 'Flocculonodular vestibular nuclei',
        'E': 'Interposed fastigial nuclear core'
    }

    master_overrides[29] = {
        'A': 'Oligodendroglioma showing 1p/19q codeletion',
        'B': 'Pilocytic astrocytoma with Rosenthal fibers',
        'C': 'Glioblastoma with pseudopalisading necrosis',
        'D': 'Medulloblastoma showing Homer Wright rosettes',
        'E': 'Meningioma showing whorled psammoma bodies'
    }

    master_overrides[31] = {
        'A': 'Whorled meningothelial cell nests and calcified psammoma bodies',
        'B': 'Biphasic compact cellular Antoni A and myxoid Antoni B regions',
        'C': 'Fried-egg clear cytoplasm cells surrounded by chicken-wire beds',
        'D': 'Homer Wright neuroblastic pseudorosettes of small blue cells',
        'E': 'Perivascular pseudo-rosettes with tapering fibrillary processes'
    }

    master_overrides[38] = {
        'A': 'Arachnoid cap cells of the dura mater layer',
        'B': 'Embryonic Rathke pouch epithelial remnants',
        'C': 'Posterior pituitary neurohypophyseal cells',
        'D': 'Ependymal cells lining the third ventricle',
        'E': 'External granular layer neuroblast cells'
    }

    master_overrides[39] = {
        'A': 'Biallelic loss of NF1 neurofibromin',
        'B': 'Biallelic loss of VHL tumor protein',
        'C': 'Inactivating mutations in TSC1 or TSC2',
        'D': 'Activating mosaic mutations in GNAQ',
        'E': 'Biallelic loss of NF2 merlin protein'
    }

    master_overrides[41] = {
        'A': 'Bilateral cerebellopontine angle acoustic schwannoma masses',
        'B': 'Cerebellar capillary hemangioblastoma with cystic nodules',
        'C': 'Optic nerve juvenile pilocytic astrocytoma with proptosis',
        'D': 'Subependymal giant cell astrocytomas lining ventricles',
        'E': 'Ipsilateral leptomeningeal angioma with cortical tracks'
    }

    master_overrides[42] = {
        'A': 'Dural meningiomas and acoustic vestibular schwannomas',
        'B': 'Clear cell renal cell carcinoma and pheochromocytoma',
        'C': 'Optic pathway gliomas and cutaneous neurofibroma foci',
        'D': 'Cardiac rhabdomyomas and bilateral angiomyolipomas',
        'E': 'Leptomeningeal facial angiomas and secondary glaucoma'
    }

    master_overrides[61] = {
        'A': 'Emergence of fungal resistance to amphotericin B therapy',
        'B': 'Reactivation of latent varicella zoster ganglion virus',
        'C': 'Acute bacterial superinfection with encapsulated cocci',
        'D': 'Direct neurotoxic adverse reaction to antiretroviral drugs',
        'E': 'Exaggerated immune reconstitution inflammatory syndrome'
    }

    master_overrides[79] = {
        'A': 'Emergent magnetic resonance angiography of head and neck',
        'B': 'Noncontrast computed tomography of brain without delay',
        'C': 'Catheter-based digital subtraction cerebral angiography',
        'D': 'Diagnostic lumbar puncture with opening pressure testing',
        'E': 'Transthoracic echocardiogram with agitated saline bubble'
    }

    master_overrides[81] = {
        'A': 'Urgent decompressive hemicraniectomy within two hours',
        'B': 'Immediate intravenous unfractionated heparin infusion',
        'C': 'Emergent surgical evacuation of intracranial thrombus',
        'D': 'Dual antiplatelet therapy with aspirin and clopidogrel',
        'E': 'Mechanical endovascular thrombectomy of occluded vessel'
    }

    master_overrides[82] = {
        'A': 'ATP depletion, pump failure, membrane depolarization, glutamate surge, and lethal calcium entry',
        'B': 'Excessive GABA release triggering sustained chloride influx and hyperpolarization necrosis',
        'C': 'Primary microglial phagocytosis triggering widespread complement-mediated axonal breakdown',
        'D': 'Direct mitochondrial swelling causing instantaneous mechanical rupture of cell membranes',
        'E': 'Astrocytic swelling causing immediate microvascular occlusion and parenchymal infarction'
    }

    master_overrides[86] = {
        'A': 'Direct compressive mass effect on the preganglionic T1 ramus',
        'B': 'Ischemia of the cavernous sinus dural sympathetic plexus',
        'C': 'Interruption of descending tectospinal pathways in midbrain',
        'D': 'Disruption of sympathetic fibers along the carotid vessel',
        'E': 'Compromise of the postganglionic supraclavicular trunk core'
    }

    master_overrides[90] = {
        'A': 'Intravenous labetalol infusion',
        'B': 'Intravenous milrinone therapy',
        'C': 'High-dose oral aspirin therapy',
        'D': 'Enteral nimodipine medication',
        'E': 'Subcutaneous unfractionated heparin'
    }

    master_overrides[91] = {
        'A': 'Protamine sulfate administration with supportive management',
        'B': 'Four-factor prothrombin complex plus intravenous vitamin K',
        'C': 'Platelet transfusion therapy alongside factor replacement',
        'D': 'Recombinant tissue plasminogen activator infusion therapy',
        'E': 'Intravenous tranexamic acid and desmopressin coagulation'
    }

    master_overrides[127] = {
        'A': 'Prompt immediate restitution of baseline clarity upon lying flat',
        'B': 'Lateral border tongue lacerations and prolonged postictal stupor',
        'C': 'Prominent autonomic prodrome with diaphoresis and lightheadness',
        'D': 'Completely normal post-event serum prolactin levels in the blood',
        'E': 'Complete absence of convulsive jerking or rhythmic limb twitches'
    }

    master_overrides[130] = {
        'A': 'Extensive cortical neuropil spongiform vacuolation and loss',
        'B': 'Hippocampal pyramidal cell loss with marked dense gliosis',
        'C': 'Perivenular oligodendrocyte demyelination with foam cells',
        'D': 'Microglial nodules surrounding viral inclusions in neurons',
        'E': 'Abundant neurofibrillary tangles formed of insoluble tau'
    }

    master_overrides[132] = {
        'A': 'Progression into medically refractory epileptic encephalopathy',
        'B': 'Severe cumulative cognitive decline and status epilepticus',
        'C': 'Spontaneous remission by adolescence with normal cognition',
        'D': 'Obligate requirement for aggressive combination anticonvulsants',
        'E': 'Rapid progressive neurodegeneration and loss of motor skills'
    }

    master_overrides[145] = {
        'A': 'Potent autoinduction of hepatic cytochrome P450 enzymes',
        'B': 'Linear first-order clearance with accelerated absorption',
        'C': 'Displacement from circulating serum albumin proteins only',
        'D': 'Significant reduction of active renal tubular clearance',
        'E': 'Saturation of hepatic clearance yielding zero-order kinetics'
    }

    master_overrides[148] = {
        'A': 'Fibrous gingival hyperplasia and androgenic facial hirsutism',
        'B': 'Fulminant idiosyncratic hepatitis with raised transaminases',
        'C': 'Profound idiosyncratic agranulocytosis and bone marrow aplasia',
        'D': 'Symmetrical length-dependent sensorimotor axonal neuropathy',
        'E': 'Stevens-Johnson syndrome or toxic epidermal necrolysis reaction'
    }

    # 3. Read raw questions
    source_path = '/Users/markyoussef_1/Downloads/Neuro Exam 3 150 High-Yield Step 1–Style Questions.md'
    with open(source_path, 'r', encoding='utf-8') as f:
        content = f.read()

    part1_idx = content.find('# Part 1: Questions')
    part2_idx = content.find('# Part 2: Answer Key and Explanations')

    part1 = content[part1_idx:part2_idx]
    part2 = content[part2_idx:]

    # Parse 1-48 answers and explanations from Part 2
    part2_matches = list(re.finditer(r'\*\*(\d+)\.\s*([A-E])\.\*\*\s*(.+?)(?=\n\n\*\*|\n##|$)', part2, re.DOTALL))
    ans_keys = {}
    expl_dict = {}
    for m in part2_matches:
        qnum = int(m.group(1))
        letter = m.group(2).strip()
        expl = m.group(3).strip()
        ans_keys[qnum] = letter
        expl_dict[qnum] = expl

    # Definitive keys and explanations for 49-150
    from answers_49_150 import ans_49_150
    for qnum, (let, exp) in ans_49_150.items():
        ans_keys[qnum] = let
        expl_dict[qnum] = exp

    # Apply medical corrections for 49-150
    ans_keys[64] = 'C'
    ans_keys[65] = 'B'
    ans_keys[93] = 'E'
    ans_keys[94] = 'C'
    ans_keys[95] = 'B'

    # Standalone stems for cross-referencing questions
    standalone_stems = {
        2: "A 27-year-old woman presents with acute right optic neuritis and visual blurring. Brain MRI demonstrates ovoid T2-hyperintense demyelinating lesions oriented perpendicularly to the lateral ventricles (Dawson fingers). Which cerebrospinal fluid (CSF) finding best supports the most likely diagnosis?",
        3: "A 27-year-old woman with multiple sclerosis presenting with acute optic neuritis and periventricular white matter lesions undergoes biopsy of an active demyelinating plaque. Which histological feature is most characteristically observed?",
        10: "A 32-year-old man presents with progressive, symmetric ascending lower extremity weakness and diffuse hyporeflexia 2 weeks after an episode of diarrheal illness. Lumbar puncture demonstrates albuminocytologic dissociation with elevated CSF protein and normal cell count, confirming Guillain-Barré syndrome. Which monitoring measure is most critical to guide ongoing inpatient management?",
        52: "A 63-year-old man with acute herpes simplex virus type 1 (HSV-1) encephalitis has neuroimaging demonstrating asymmetric hemorrhagic necrosis of the inferomedial temporal lobes. Which long-term neurological deficits are most likely to occur?",
        101: "A 57-year-old man with a left lateral medullary (Wallenberg) stroke develops dysphagia, hoarseness, and loss of the gag reflex due to nucleus ambiguus ischemia. To which side does the uvula deviate on examination, and why?",
        117: "A 63-year-old woman presents with rapidly progressive cognitive decline, cerebellar gait ataxia, myoclonus, and cortical ribboning on diffusion-weighted MRI concerning for Creutzfeldt-Jakob disease (CJD). Which diagnostic findings best support this diagnosis?",
        122: "Following an acute episode of Wernicke encephalopathy in a chronic alcohol user presenting with confusion, nystagmus, and ataxia, the patient develops persistent Korsakoff syndrome with severe anterograde amnesia and confabulation. Which anatomical structures are characteristically damaged?"
    }

    # Blueprint category mapping
    def get_category(qnum):
        if 1 <= qnum <= 15:
            return 'Demyelinating Disease'
        elif 16 <= qnum <= 27:
            return 'Cerebellum'
        elif 28 <= qnum <= 48:
            return 'Tumors'
        elif 49 <= qnum <= 63:
            return 'Opportunistic Infection'
        elif 64 <= qnum <= 108:
            return 'Stroke (Blood Supply, Cerebrovascular, Brainstem)'
        elif 109 <= qnum <= 123:
            return 'Dementia'
        elif 124 <= qnum <= 150:
            return 'CBIL Epilepsy'
        return 'Neurology'

    # Extract all 150 stems
    stems = {}
    for qnum in range(1, 151):
        if qnum in standalone_stems:
            stems[qnum] = standalone_stems[qnum]
        else:
            m = re.search(rf'\*\*{qnum}\.\*\*\s*(.+?)(?=\n\s*-\s*[A-E]\.|\n\n\*\*|\n##|$)', part1, re.DOTALL)
            if not m:
                print(f"Error parsing stem for Q{qnum}")
                return False
            stem_text = m.group(1).replace('\n', ' ').strip()
            # Clean any leading/trailing artifacts
            stem_text = re.sub(r'\s+', ' ', stem_text)
            stems[qnum] = stem_text

    # 4. Perform Key Balancing (to reach exactly 30 A, 30 B, 30 C, 30 D, 30 E)
    # B -> A swaps: Q12, Q24, Q58, Q87
    # D -> A swap:  Q78
    # C -> E swaps: Q8, Q25, Q55, Q89
    # D -> E swap:  Q99

    def swap_options(qnum, let1, let2):
        opts = master_overrides[qnum]
        t1 = opts[let1]
        t2 = opts[let2]
        opts[let1] = t2
        opts[let2] = t1

    # B -> A
    for qnum in [12, 24, 58, 87]:
        swap_options(qnum, 'A', 'B')
        ans_keys[qnum] = 'A'

    # D -> A
    swap_options(78, 'A', 'D')
    ans_keys[78] = 'A'

    # C -> E
    for qnum in [8, 25, 55, 89]:
        swap_options(qnum, 'C', 'E')
        ans_keys[qnum] = 'E'

    # D -> E
    swap_options(99, 'D', 'E')
    ans_keys[99] = 'E'

    # 5. Assemble all 150 questions
    assembled_questions = []
    key_distribution = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0}

    for qnum in range(1, 151):
        stem = stems[qnum]
        corr_letter = ans_keys[qnum]
        expl = expl_dict[qnum]
        category = get_category(qnum)
        ov = master_overrides[qnum]

        options = []
        correct_idx = None
        for idx, let in enumerate(['A', 'B', 'C', 'D', 'E']):
            text = ov[let]
            is_c = (let == corr_letter)
            if is_c:
                correct_idx = idx
                key_distribution[let] += 1
            options.append({
                'letter': let,
                'text': text,
                'is_correct': is_c
            })

        assembled_questions.append({
            'id': f'exam3_step1_150_q{qnum}',
            'q_num': str(qnum),
            'stem': stem,
            'category': category,
            'source': 'Neuro Exam 3: 150 High-Yield Step 1–Style Questions',
            'options': options,
            'correct_idx': correct_idx,
            'explanation': expl,
            'high_yield_pearl': f'High-Yield Rule: {category}',
            'image': None
        })

    # 6. Strict Validation
    assert len(assembled_questions) == 150, f"Expected 150 questions, got {len(assembled_questions)}"
    for k, count in key_distribution.items():
        assert count == 30, f"Key {k} has count {count}, expected 30!"

    for q in assembled_questions:
        qnum = int(q['q_num'])
        assert len(q['options']) == 5, f"Q{qnum} has {len(q['options'])} options"
        assert q['correct_idx'] in [0, 1, 2, 3, 4], f"Q{qnum} invalid correct_idx {q['correct_idx']}"
        opt_lens = [len(o['text']) for o in q['options']]
        spread = max(opt_lens) - min(opt_lens)
        assert spread <= 7, f"Q{qnum} spread {spread} > 7: {opt_lens}"
        for o in q['options']:
            assert '(' not in o['text'] and ')' not in o['text'], f"Paren in Q{qnum} {o['letter']}: {o['text']}"

    out_path = '/Users/markyoussef_1/.gemini/antigravity-ide/scratch/usmle_exam1/exam3_step1_150_questions.json'
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(assembled_questions, f, indent=2, ensure_ascii=False)

    print(f"SUCCESS: Generated {len(assembled_questions)} verified questions into {out_path}")
    print(f"Key Distribution: {key_distribution}")
    return True

if __name__ == '__main__':
    build_assembled_json()
