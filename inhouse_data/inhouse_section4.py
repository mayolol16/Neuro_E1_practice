# -*- coding: utf-8 -*-
# inhouse_section4.py
# Section 4: Acute Neuro-Pathology & Critical Care
# Covers:
# - Headache Disorders (Migraine, Tension, Cluster, CGRP, Gepants, Triptans, MOH, Red Flags/GCA)
# - Traumatic Brain Injuries (Concussion, Contusion, DAI, GCS, Coma/RAS, Coup/Contrecoup)
# - Intracranial Hemorrhages (Epidural vs Subdural vs Subarachnoid, Anatomy, Lucid Interval)
# - Meningitis (Clinical Triad, Kernig/Brudzinski, CT before LP, CSF Analysis Table, Empiric Antibiotics, Listeria, N. meningitidis Prophylaxis)

questions_section4 = [
    # ==========================================
    # HEADACHE DISORDERS & PHARMACOLOGY
    # ==========================================
    {
        "id": "IH_Q126",
        "question_number": 126,
        "category": "In House: Headache Disorders",
        "stem": "A 28-year-old female accountant presents with recurrent headaches occurring 3 to 4 times per month for the past two years. The headaches are strictly unilateral, throbbing and pulsating in quality, of severe intensity, and worsen when she climbs stairs or walks. Each attack lasts 24 to 36 hours if untreated and is accompanied by intense nausea, vomiting, photophobia, and phonophobia. Neurological examination is entirely normal between attacks. Which of the following neuropeptides, released from perivascular trigeminal nerve endings in the meninges, plays a central role in driving neurogenic inflammation, vasodilation, and mast cell degranulation during these attacks?",
        "options": [
            {"text": "Calcitonin Gene-Related Peptide (CGRP)", "is_correct": True},
            {"text": "Neuropeptide Y (NPY)", "is_correct": False},
            {"text": "Somatostatin", "is_correct": False},
            {"text": "Enkephalin", "is_correct": False},
            {"text": "Gamma-aminobutyric acid (GABA)", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Calcitonin Gene-Related Peptide (CGRP).\n\nMigraine is a neurovascular disorder driven by dysfunction of brainstem sensory modulation and the trigeminovascular system:\n1. Cortical spreading depression (a wave of neuronal and glial depolarization traveling across the cortex) activates nociceptive afferents of the ophthalmic division of the trigeminal nerve (CN V1) innervating meningeal and dural blood vessels.\n2. When activated, these perivascular trigeminal sensory nerve terminals release potent vasoactive and inflammatory neuropeptides, most notably Calcitonin Gene-Related Peptide (CGRP), as well as substance P and neurokinin A.\n3. CGRP binds to CGRP receptors (composed of CLR and RAMP1) on smooth muscle cells of meningeal arteries, triggering profound vasodilation, plasma protein extravasation, and mast cell degranulation (neurogenic inflammation). CGRP also acts centrally in the spinal trigeminal nucleus and thalamus to enhance nociceptive transmission and sustain central sensitization.\n4. Small-molecule CGRP receptor antagonists (gepants: ubrogepant, rimegepant, atogepant) and monoclonal antibodies against CGRP or its receptor (erenumab, galcanezumab, fremanezumab, eptinezumab) are highly effective targeted therapies.\n\n• Option B is incorrect: NPY is a sympathetic cotransmitter and appetite stimulant.\n• Option C is incorrect: Somatostatin inhibits growth hormone and GI secretions.\n• Option D is incorrect: Enkephalins are endogenous opioids that inhibit, rather than cause, pain.\n• Option E is incorrect: GABA is the primary inhibitory neurotransmitter."
    },
    {
        "id": "IH_Q127",
        "question_number": 127,
        "category": "In House: Headache Disorders",
        "stem": "A 32-year-old woman with a history of episodic migraines presents to discuss acute treatment. Her physician prescribes sumatriptan. What is the receptor mechanism of action of triptans, and in which patient population are triptans strictly contraindicated due to their vascular properties?",
        "options": [
            {"text": "Competitive antagonism at dopamine D2 receptors; contraindicated in Parkinson disease", "is_correct": False},
            {"text": "Selective agonism at serotonin 5-HT1B and 5-HT1D receptors; contraindicated in patients with coronary artery disease, history of myocardial infarction, stroke, or uncontrolled hypertension", "is_correct": True},
            {"text": "Blockade of calcium channels; contraindicated in patients with heart block", "is_correct": False},
            {"text": "Direct inhibition of cyclooxygenase-2 (COX-2); contraindicated in peptic ulcer disease", "is_correct": False},
            {"text": "Agonism at mu-opioid receptors; contraindicated in substance use disorder", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. Selective agonism at serotonin 5-HT1B and 5-HT1D receptors; contraindicated in patients with coronary artery disease, history of myocardial infarction, stroke, or uncontrolled hypertension.\n\nTriptans (e.g., sumatriptan, rizatriptan, zolmitriptan) are first-line acute migraine-abortive medications that act as selective agonists at 5-HT1B and 5-HT1D serotonin receptors:\n1. 5-HT1B receptors are expressed on vascular smooth muscle of cranial and meningeal arteries; activation causes vasoconstriction of distended meningeal vessels.\n2. 5-HT1D receptors are presynaptic autoreceptors on trigeminal sensory nerve terminals; activation inhibits the presynaptic release of CGRP, substance P, and other inflammatory neuropeptides.\n3. Central 5-HT1D activation in the spinal trigeminal nucleus blocks ascending nociceptive transmission to the thalamus.\nContraindications: Because 5-HT1B receptors are also expressed on coronary arteries and peripheral vessels, triptans can cause coronary vasospasm. They are strictly contraindicated in patients with established coronary artery disease (CAD), previous myocardial infarction, Prinzmetal (variant) angina, ischemic stroke, transient ischemic attack (TIA), peripheral vascular disease, or uncontrolled severe hypertension.\n\n• Option A is incorrect: Antiemetics like metoclopramide block D2 receptors, not triptans.\n• Option C is incorrect: Calcium channel blockers (verapamil) prevent cluster headaches.\n• Option D is incorrect: NSAIDs inhibit COX enzymes.\n• Option E is incorrect: Triptans are not opioids."
    },
    {
        "id": "IH_Q128",
        "question_number": 128,
        "category": "In House: Headache Disorders",
        "stem": "A 38-year-old man presents with agonizing, piercing pain centered behind and around his right eye that began 45 minutes ago. He describes the pain as feeling like a 'hot poker being driven into my eye' and states he feels compelled to pace rapidly around the room ('suicide headache'). Physical examination during the attack reveals severe right-sided conjunctival injection, profuse tearing (lacrimation) from the right eye, right rhinorrhea, and partial right-sided ptosis and miosis. What is the most effective immediate first-line acute therapy to abort this attack in the emergency room?",
        "options": [
            {"text": "Oral acetaminophen with codeine", "is_correct": False},
            {"text": "High-flow 100% oxygen (12 to 15 L/min via a non-rebreather mask) and/or subcutaneous sumatriptan", "is_correct": True},
            {"text": "Intravenous morphine bolus", "is_correct": False},
            {"text": "Oral verapamil", "is_correct": False},
            {"text": "Carbamazepine", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. High-flow 100% oxygen (12 to 15 L/min via a non-rebreather mask) and/or subcutaneous sumatriptan.\n\nThis patient presents with a classic Cluster Headache, a primary headache belonging to the Trigeminal Autonomic Cephalalgias (TACs):\n- Clinical features: Severe or very severe, strictly unilateral orbital/supraorbital/temporal pain lasting 15 to 180 minutes. Attacks occur in cyclical 'clusters' (1 to 8 attacks per day for weeks to months, often waking the patient from REM sleep at the same time each night). Prominent ipsilateral cranial parasympathetic autonomic symptoms occur: conjunctival injection, lacrimation, nasal congestion, rhinorrhea, forehead sweating, and an incomplete Horner syndrome (ptosis and miosis due to sympathetic carotid plexus compression). Patients exhibit marked motor restlessness (pacing, rocking), contrasting with migraineurs who prefer to lie still in a dark room.\n- Acute Abortive Treatment: High-flow 100% normobaric oxygen (12–15 L/min via non-rebreather face mask for 15 minutes) aborts attacks in up to 80% of patients within 10–15 minutes by constricting cerebral vessels and suppressing trigeminal autonomic reflex circuits. Subcutaneous sumatriptan (6 mg) or intranasal zolmitriptan are also first-line acute agents (oral triptans are too slow).\n- Preventive Treatment: Verapamil is the drug of choice for maintenance prophylaxis (requires ECG monitoring for PR prolongation); lithium and high-dose galcanezumab are alternatives.\n\n• Option A is incorrect: Opioids are ineffective for cluster headaches and carry high addiction risk.\n• Option C is incorrect: Morphine does not terminate trigeminal autonomic cephalalgias.\n• Option D is incorrect: Verapamil is used for maintenance prevention, not immediate acute attack abortion.\n• Option E is incorrect: Carbamazepine is the first-line treatment for Trigeminal Neuralgia (tic douloureux)."
    },
    {
        "id": "IH_Q129",
        "question_number": 129,
        "category": "In House: Headache Disorders",
        "stem": "A 45-year-old woman with a 15-year history of episodic migraines presents with daily, continuous, dull, throbbing headaches that are present upon waking and persist all day. When asked about medication use, she admits to taking an over-the-counter combination analgesic containing acetaminophen, aspirin, and caffeine (Excedrin) 3 to 4 times every single day (over 25 days per month) for the past 6 months. She notes that the pills provide temporary relief for 2 hours, after which a severe headache returns with vengeance. What is the diagnosis, and what is the primary management strategy?",
        "options": [
            {"text": "Idiopathic intracranial hypertension; perform serial lumbar punctures", "is_correct": False},
            {"text": "Medication Overuse Headache (MOH / Rebound headache); educate the patient, discontinue/wean the overused acute medication, and initiate a prophylactic migraine preventive therapy", "is_correct": True},
            {"text": "Trigeminal neuralgia; initiate high-dose carbamazepine", "is_correct": False},
            {"text": "Temporal arteritis; initiate high-dose intravenous methylprednisolone", "is_correct": False},
            {"text": "Cluster headache; prescribe verapamil and 100% oxygen", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. Medication Overuse Headache (MOH / Rebound headache); educate the patient, discontinue/wean the overused acute medication, and initiate a prophylactic migraine preventive therapy.\n\nMedication Overuse Headache (MOH, previously termed 'rebound headache') is a secondary headache disorder defined by the International Classification of Headache Disorders (ICHD-3):\n1. Occurs in a patient with a pre-existing primary headache (most commonly migraine).\n2. Present on >=15 days per month for >3 months.\n3. Regular overuse of acute headache medications for >3 months: defined as taking simple analgesics (acetaminophen, NSAIDs) on >=15 days/month, or combination analgesics (containing caffeine, butalbital), triptans, ergots, or opioids on >=10 days/month.\n4. Pathophysiology: Chronic receptor down-regulation and central sensitization create a vicious cycle: as the acute medication wears off, withdrawal-mediated nociceptive firing triggers a rebound headache, prompting the patient to consume more medication.\n5. Management: The cornerstone of treatment is patient education and complete withdrawal/weaning of the offending acute medication, establishing a strict limit of acute therapy to <=2 days per week (<=8 days/month), using bridge therapy (e.g., short steroid taper or nerve blocks) if necessary, and initiating an effective preventive medication (e.g., topiramate, propranolol, or CGRP monoclonal antibodies).\n\n• Options A, C, D, and E represent unrelated diagnoses and incorrect treatments."
    },
    {
        "id": "IH_Q130",
        "question_number": 130,
        "category": "In House: Headache Disorders",
        "stem": "A 71-year-old woman presents to the clinic with a 3-week history of a new, severe, right-sided throbbing headache centered over her temple. She reports that combing her hair produces extreme tenderness across her scalp, and she experiences cramping, fatigue, and pain in her jaw muscles when chewing meat (jaw claudication). Yesterday, she experienced two transient episodes of complete visual loss in her right eye ('amaurosis fugax'). Physical examination reveals a tender, swollen, nodular, pulseless right superficial temporal artery. Laboratory evaluation shows an erythrocyte sedimentation rate (ESR) of 105 mm/hr (normal < 30 mm/hr) and C-reactive protein (CRP) of 42 mg/L. What is the most critical immediate step in clinical management?",
        "options": [
            {"text": "Schedule an elective temporal artery biopsy in 3 weeks before initiating any pharmacological therapy", "is_correct": False},
            {"text": "Immediately initiate high-dose systemic corticosteroids (e.g., oral prednisone 60 mg/day or IV methylprednisolone) without waiting for temporal artery biopsy results, to prevent irreversible bilateral blindness", "is_correct": True},
            {"text": "Prescribe oral sumatriptan and send the patient home with a headache diary", "is_correct": False},
            {"text": "Order a non-contrast head CT and perform an immediate lumbar puncture", "is_correct": False},
            {"text": "Start low-dose aspirin and schedule a carotid endarterectomy", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. Immediately initiate high-dose systemic corticosteroids (e.g., oral prednisone 60 mg/day or IV methylprednisolone) without waiting for temporal artery biopsy results, to prevent irreversible bilateral blindness.\n\nGiant Cell Arteritis (Temporal Arteritis) is a chronic granulomatous vasculitis of large- and medium-sized arteries, preferentially targeting branches of the external and internal carotid arteries (superficial temporal, ophthalmic, posterior ciliary, and vertebral arteries) in individuals older than 50 years (associated with Polymyalgia Rheumatica in ~50%):\n- Clinical features: New-onset headache (temple), prominent scalp tenderness (pain when brushing hair), jaw claudication (masseter ischemia during chewing, highest positive likelihood ratio), markedly elevated ESR (>50–100 mm/hr) and CRP, and amaurosis fugax.\n- Critical Urgency: Inflammation of the ophthalmic and posterior ciliary arteries can cause Anterior Ischemic Optic Neuropathy (AION), leading to sudden, irreversible blindness. Crucially, involvement of the contralateral eye can follow within 24 to 48 hours!\n- Management Rule: If Giant Cell Arteritis is strongly suspected, HIGH-DOSE SYSTEMIC CORTICOSTEROIDS must be initiated IMMEDIATELY. Diagnostic confirmation via temporal artery biopsy should be arranged, but biopsy must NEVER delay steroid administration (histopathological changes of granulomatous inflammation and multinucleated giant cells persist for up to 2–4 weeks after starting steroids).\n\n• Option A is incorrect: Delaying steroids pending biopsy risks permanent, bilateral blindness.\n• Option C is incorrect: Triptans are contraindicated and ineffective for arteritis.\n• Option D is incorrect: CT and LP are indicated for subarachnoid hemorrhage, not temporal arteritis.\n• Option E is incorrect: GCA is an inflammatory vasculitis requiring immunosuppression, not carotid stenosis surgery."
    },

    # ==========================================
    # TRAUMATIC BRAIN INJURY & HEMORRHAGES
    # ==========================================
    {
        "id": "IH_Q131",
        "question_number": 131,
        "category": "In House: Traumatic Brain Injuries",
        "stem": "A 12-year-old boy is struck on the right side of his head by an errant baseball bat near the temple. He loses consciousness for 1 minute, but regains awareness and appears entirely normal, answering questions lucidly and continuing to sit on the team bench for 2 hours (classic 'lucid interval'). Later that evening, he develops an explosive headache, repeated projectile vomiting, progressive lethargy, and a dilated, sluggish right pupil. Emergency non-contrast head CT reveals a hyperdense, biconvex (lens-shaped) extra-axial collection along the right temporoparietal convexity that does not cross cranial sutures. Which vascular structure was torn, and what anatomical feature restricts this hematoma from crossing suture lines?",
        "options": [
            {"text": "Bridging cortical veins; restricted by arachnoid trabeculae", "is_correct": False},
            {"text": "Middle meningeal artery; restricted because the periosteal dura mater is firmly adherent to the inner calvarial suture lines", "is_correct": True},
            {"text": "Aneurysm of the anterior communicating artery; restricted by the falx cerebri", "is_correct": False},
            {"text": "Internal carotid artery; restricted by the cavernous sinus", "is_correct": False},
            {"text": "Posterior inferior cerebellar artery; restricted by the foramen magnum", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. Middle meningeal artery; restricted because the periosteal dura mater is firmly adherent to the inner calvarial suture lines.\n\nAn Epidural Hematoma (EDH) classic board scenario:\n1. Mechanism: Blunt trauma to the pterion (the thin junction of the frontal, parietal, temporal, and sphenoid bones on the lateral skull) fractures the bone and lacerates the underlying Middle Meningeal Artery (a branch of the maxillary artery entering via the foramen spinosum).\n2. Clinical Course: High-pressure arterial bleeding strips the dura away from the skull table. Patients often experience a transient loss of consciousness followed by a classic 'LUCID INTERVAL' (lasting hours) where they seem neurologically intact, before rapid expansion of the arterial hematoma causes severe intracranial hypertension, uncal herniation (compressing CN III, producing an ipsilateral dilated 'blown' pupil and 'down-and-out' eye), coma, and death unless surgically evacuated via emergent craniotomy/burr hole.\n3. Radiographic Appearance: Biconvex (lenticular / lens-shaped) hyperdense collection. Because the periosteal layer of the dura is firmly stitched and adherent to the cranial sutures (coronal, lambdoid, sagittal), the hematoma CANNOT cross cranial suture lines. However, because it lies outside the dura, it CAN cross dural reflections like the falx cerebri and tentorium.\n\n• Option A is incorrect: Tearing of bridging veins causes subdural hematomas (crescent-shaped, crosses suture lines).\n• Option C is incorrect: Ruptured berry aneurysms cause subarachnoid hemorrhage.\n• Option D is incorrect: ICA rupture in the cavernous sinus causes a direct carotid-cavernous fistula.\n• Option E is incorrect: PICA rupture causes subarachnoid or intraventricular hemorrhage."
    },
    {
        "id": "IH_Q132",
        "question_number": 132,
        "category": "In House: Traumatic Brain Injuries",
        "stem": "An 82-year-old man with mild baseline dementia and chronic alcohol use is brought to the emergency department by his daughter because of fluctuating confusion, worsening memory, and an unsteady gait that have developed insidiously over the past 3 weeks. His daughter recalls that he bumped his head against a kitchen cabinet a month ago, but had no loss of consciousness at that time. Non-contrast head CT reveals a crescent-shaped, hypodense extra-axial fluid collection spreading across the entire left cerebral hemisphere, crossing both coronal and lambdoid suture lines, but bounded medially by the falx cerebri. What is the diagnosis, and which vessels are torn?",
        "options": [
            {"text": "Acute epidural hematoma; Middle meningeal artery", "is_correct": False},
            {"text": "Chronic subdural hematoma; Tearing of bridging cortical veins bridging the subdural space between the cerebral cortex and dural venous sinuses", "is_correct": True},
            {"text": "Subarachnoid hemorrhage; Rupture of a Charcot-Bouchard microaneurysm", "is_correct": False},
            {"text": "Intraventricular hemorrhage; Ependymal vein laceration", "is_correct": False},
            {"text": "Arteriovenous malformation; Middle cerebral artery", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. Chronic subdural hematoma; Tearing of bridging cortical veins bridging the subdural space between the cerebral cortex and dural venous sinuses.\n\nA Subdural Hematoma (SDH) features fundamentally distinct anatomy and epidemiology from an epidural hematoma:\n1. Pathophysiology: Results from tearing of Bridging Cortical Veins as they traverse the subdural space to drain into the superior sagittal sinus. In elderly patients and individuals with chronic alcohol use, age-related cerebral cortical atrophy enlarges the subarachnoid space and stretches these delicate bridging veins, making them exceedingly vulnerable to shear rupture even from minor, trivial head bumps.\n2. Clinical Presentation: Because bleeding originates from low-pressure venous structures, blood accumulates slowly. A Chronic Subdural Hematoma presents indolently over weeks or months with fluctuating drowsiness, progressive cognitive slowing, confusion, headache, and contralateral mild hemiparesis, frequently masquerading as worsening dementia or depression.\n3. Radiographic Appearance: Crescent-shaped (concave toward the brain), conforming to the hemispheric convexity. Because the subdural space is continuous over the cerebral hemispheres, an SDH freely CROSSES cranial suture lines. However, it CANNOT cross dural reflections (bounded medially by the falx cerebri and inferiorly by the tentorium cerebelli). On CT, acute blood is hyperdense (bright), subacute is isodense, and chronic blood (>3 weeks) is hypodense (dark).\n\n• Option A is incorrect: Epidural hematomas are biconvex, do not cross sutures, and result from middle meningeal artery rupture.\n• Option C is incorrect: Charcot-Bouchard aneurysms cause deep intraparenchymal basal ganglia hemorrhages in hypertension.\n• Option D is incorrect: Intraventricular hemorrhage is confined to the ventricular cavities.\n• Option E is incorrect: AVM rupture typically causes intraparenchymal or subarachnoid hemorrhage."
    },
    {
        "id": "IH_Q133",
        "question_number": 133,
        "category": "In House: Traumatic Brain Injuries",
        "stem": "A 22-year-old unrestrained driver is ejected through the windshield during a high-speed motor vehicle collision. Paramedics assess the patient at the scene and record the following findings on the Glasgow Coma Scale (GCS):\n- The patient opens his eyes only in response to painful sternal rub.\n- The patient utters only incomprehensible sounds (groans and moans) without recognizable words.\n- The patient exhibits decorticate (abnormal flexor) posturing in response to pain.\nWhat is this patient's total Glasgow Coma Scale score, and what does this score dictate regarding emergency airway management?",
        "options": [
            {"text": "GCS 11; stable for observation with non-rebreather oxygen mask", "is_correct": False},
            {"text": "GCS 8 (Eyes = 2, Verbal = 2, Motor = 3); indicates severe traumatic brain injury requiring immediate endotracheal intubation ('GCS <= 8, intubate')", "is_correct": True},
            {"text": "GCS 5; indicates irreversible brain death", "is_correct": False},
            {"text": "GCS 14; mild concussion with no airway risk", "is_correct": False},
            {"text": "GCS 3; minimum possible score indicating flaccid areflexia", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. GCS 8 (Eyes = 2, Verbal = 2, Motor = 3); indicates severe traumatic brain injury requiring immediate endotracheal intubation ('GCS <= 8, intubate').\n\nThe Glasgow Coma Scale (GCS) is the universally standard tool for assessing level of consciousness in acute brain injury (scores range from 3 to 15):\n1. Eye Opening (E, maximum 4):\n   - 4 = Spontaneous\n   - 3 = To voice / speech\n   - 2 = To pain (sternal rub / nailbed pressure) -> This patient = 2\n   - 1 = None\n2. Verbal Response (V, maximum 5):\n   - 5 = Oriented\n   - 4 = Confused\n   - 3 = Inappropriate words\n   - 2 = Incomprehensible sounds (groaning/moaning) -> This patient = 2\n   - 1 = None\n3. Motor Response (M, maximum 6):\n   - 6 = Obeys commands\n   - 5 = Localizes to pain\n   - 4 = Normal flexion / withdrawal to pain\n   - 3 = Abnormal flexion (decorticate posturing) -> This patient = 3\n   - 2 = Extension (decerebrate posturing)\n   - 1 = None (flaccid)\nTotal Score: E2 + V2 + M3 = 8.\nA GCS <= 8 defines SEVERE Traumatic Brain Injury and coma. At this level of depressed consciousness, protective airway reflexes (cough, gag) are lost, placing the patient at imminent risk for aspiration and asphyxiation. Emergency medicine dogma dictates: 'GCS of 8 or less, intubate!'.\n\n• Options A, C, D, and E represent incorrect score calculations and management guidelines."
    },
    {
        "id": "IH_Q134",
        "question_number": 134,
        "category": "In House: Traumatic Brain Injuries",
        "stem": "A 19-year-old passenger is involved in a severe rollover vehicle collision. She arrives in a deep coma (GCS 5) and remains comatose for two weeks. Initial non-contrast head CT on admission was reported as normal without evidence of mass effect, midline shift, or large hematomas. However, subsequent brain MRI reveals multiple punctate microhemorrhages and foci of restricted diffusion localized to the gray-white matter junction of the cerebral hemispheres and the splenium of the corpus callosum. Immunohistochemical staining on brain tissue sections demonstrates extensive accumulation of beta-amyloid precursor protein (beta-APP). What is the underlying pathology?",
        "options": [
            {"text": "Simple cerebral concussion", "is_correct": False},
            {"text": "Diffuse Axonal Injury (DAI) caused by rotational acceleration-deceleration shearing forces", "is_correct": True},
            {"text": "Fat embolism syndrome", "is_correct": False},
            {"text": "Carbon monoxide poisoning with globus pallidus necrosis", "is_correct": False},
            {"text": "Central pontine myelinolysis", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. Diffuse Axonal Injury (DAI) caused by rotational acceleration-deceleration shearing forces.\n\nDiffuse Axonal Injury (DAI) is one of the most common and devastating consequences of severe traumatic brain injury:\n1. Mechanism: Violent, high-velocity angular or rotational acceleration-deceleration forces subject brain regions of differing tissue density (specifically the interface between cortical gray matter and underlying subcortical white matter, the corpus callosum, and the dorsolateral upper brainstem) to severe tensile and shear stress.\n2. Cellular Pathophysiology: Axonal cytoskeletons (neurofilaments and microtubules) stretch and rupture, disrupting fast axonal transport. Organelles and transport proteins accumulate at the site of breakage, causing focal axonal swellings ('axonal varicosities' or 'retraction balls'). Immunohistochemical staining for Beta-Amyloid Precursor Protein (β-APP) or alpha-synuclein sensitively detects these damaged axons within hours of injury.\n3. Clinical Profile: Devastating clinical presentation (immediate, prolonged coma / vegetative state) in striking contrast to a seemingly unremarkable or minimally abnormal initial head CT (which may only reveal subtle punctate petechial microhemorrhages). Gradient echo (GRE) or susceptibility-weighted (SWI) MRI is the imaging modality of choice to visualize the microscopic axonal shear injuries.\n\n• Option A is incorrect: Concussions cause transient functional deficits without prolonged coma or focal microhemorrhages.\n• Option C is incorrect: Fat embolism syndrome occurs 24-72 hrs after long bone fractures, presenting with a petechial rash, hypoxemia, and neurological deficits.\n• Option D is incorrect: Carbon monoxide causes bilateral globus pallidus necrosis.\n• Option E is incorrect: Central pontine myelinolysis is caused by overly rapid correction of hyponatremia."
    },

    # ==========================================
    # MENINGITIS & CRITICAL CNS INFECTIONS
    # ==========================================
    {
        "id": "IH_Q135",
        "question_number": 135,
        "category": "In House: Meningitis & Infections",
        "stem": "An 18-year-old college freshman living in a crowded campus dormitory presents to the emergency department with high fever (103.5°F / 39.7°C), severe throbbing headache, photophobia, and extreme neck stiffness that developed over the past 6 hours. On examination, passive flexion of his neck causes involuntary, spontaneous flexion of his hips and knees (positive Brudzinski sign), and he cannot fully extend his knee when his hip is flexed to 90° due to severe pain (positive Kernig sign). He has a petechial and purpuric rash spreading across his lower extremities and trunk. Lumbar puncture reveals cloudy CSF with 4,500 WBC/mm³ (92% neutrophils), protein 340 mg/dL, and glucose 18 mg/dL (serum glucose 110 mg/dL). Gram stain reveals intracellular Gram-negative diplococci. What pathogen is responsible, and what chemoprophylaxis is recommended for his close dormitory contacts?",
        "options": [
            {"text": "Streptococcus pneumoniae; Prophylaxis with oral Amoxicillin", "is_correct": False},
            {"text": "Neisseria meningitidis; Prophylaxis with oral Rifampin (or single-dose Ciprofloxacin or intramuscular Ceftriaxone) for close contacts", "is_correct": True},
            {"text": "Listeria monocytogenes; Prophylaxis with oral Trimethoprim-sulfamethoxazole", "is_correct": False},
            {"text": "Haemophilus influenzae type b; Prophylaxis with oral Doxycycline", "is_correct": False},
            {"text": "Cryptococcus neoformans; Prophylaxis with oral Fluconazole", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. Neisseria meningitidis; Prophylaxis with oral Rifampin (or single-dose Ciprofloxacin or intramuscular Ceftriaxone) for close contacts.\n\nNeisseria meningitidis (Meningococcus) is the classic culprit for epidemic bacterial meningitis in adolescents, college students living in dormitories, and military recruits:\n1. Characteristics: Gram-negative, coffee-bean-shaped diplococci that ferment both glucose and maltose. It produces an antiphagocytic polysaccharide capsule and endotoxin (lipooligosaccharide, LOS). Shedding of LOS drives massive systemic cytokine release, causing petechial/purpuric skin lesions (purpura fulminans), DIC, and potential bilateral hemorrhagic adrenal necrosis (Waterhouse-Friderichsen syndrome with acute adrenal insufficiency and circulatory collapse).\n2. CSF Profile: Classic for acute bacterial meningitis: cloudy, elevated opening pressure, elevated neutrophils (>1000/mm³), high protein, and markedly decreased glucose (CSF:serum ratio < 0.4).\n3. Prophylaxis: Droplet transmission occurs via respiratory secretions. Chemoprophylaxis is MANDATORY for all close contacts (roommates, household members, daycare contacts, intimate partners, or healthcare workers directly exposed to oral secretions during intubation):\n   - First-line: Oral Rifampin (600 mg BID for 2 days; penetrates mucosal secretions and eradicates nasopharyngeal carriage; note: turns tears/urine orange and induces CYP450).\n   - Alternatives: Single-dose oral Ciprofloxacin (500 mg) or single-dose intramuscular Ceftriaxone (250 mg; safe in pregnancy).\n\n• Option A is incorrect: S. pneumoniae is a Gram-positive lancet-shaped diplococcus and does not require contact prophylaxis.\n• Option C is incorrect: Listeria is a Gram-positive tumbling motile rod.\n• Option D is incorrect: H. influenzae is a Gram-negative coccobacillus; prophylaxis for HiB is rifampin, but HiB is prevented by childhood vaccination.\n• Option E is incorrect: Cryptococcus is an encapsulated yeast seen in AIDS."
    },
    {
        "id": "IH_Q136",
        "question_number": 136,
        "category": "In House: Meningitis & Infections",
        "stem": "A 68-year-old man with a history of type 2 diabetes mellitus is brought to the emergency department with fever, confusion, and nuchal rigidity. The medical team initiates immediate empiric antibiotic therapy while preparing for diagnostic testing. In addition to vancomycin and ceftriaxone, which antibiotic MUST be added to the empiric regimen specifically for this patient because of his age (>50 years), and which pathogen does it cover?",
        "options": [
            {"text": "Azithromycin; to cover Mycoplasma pneumoniae", "is_correct": False},
            {"text": "Ampicillin; to cover Listeria monocytogenes", "is_correct": True},
            {"text": "Metronidazole; to cover Bacteroides fragilis", "is_correct": False},
            {"text": "Gentamicin; to cover Pseudomonas aeruginosa", "is_correct": False},
            {"text": "Acyclovir; to cover Cytomegalovirus", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. Ampicillin; to cover Listeria monocytogenes.\n\nEmpiric antimicrobial therapy for suspected acute bacterial meningitis is dictated by age-stratified epidemiology:\n1. Age 1 month to 50 years: Pathogens are Streptococcus pneumoniae and Neisseria meningitidis -> Empiric coverage is Vancomycin (covers penicillin- and cephalosporin-resistant S. pneumoniae) + 3rd generation cephalosporin (Ceftriaxone or Cefotaxime).\n2. Age > 50 years and Immunocompromised individuals (e.g., diabetics, cirrhotics, transplant recipients, lymphoma): In addition to S. pneumoniae and N. meningitidis, these patients have impaired cell-mediated immunity and are at high risk for Listeria monocytogenes (a foodborne Gram-positive facultative intracellular bacillus found in unpasteurized cheeses, cold cuts, and deli meats).\n3. Why Ampicillin is essential: Listeria monocytogenes possesses low-affinity penicillin-binding proteins (PBPs) that render it NATURALLY RESISTANT to ALL CEPHALOSPORINS (including ceftriaxone and cefotaxime!). Therefore, AMPICILLIN must be added to the empiric regimen (Vancomycin + Ceftriaxone + Ampicillin) whenever a patient is >50 years old, an infant <1 month old, pregnant, or immunocompromised.\n\n• Option A is incorrect: Azithromycin does not treat acute bacterial meningitis or Listeria.\n• Option C is incorrect: Metronidazole covers anaerobes in brain abscesses, but is not part of standard empiric meningitis regimens.\n• Option D is incorrect: Gentamicin is used with ampicillin in neonates, but ampicillin covers Listeria in elderly adults.\n• Option E is incorrect: Acyclovir covers HSV encephalitis, not bacterial meningitis."
    },
    {
        "id": "IH_Q137",
        "question_number": 137,
        "category": "In House: Meningitis & Infections",
        "stem": "A 45-year-old man presents with fever, stiff neck, and severe headache. In which of the following clinical scenarios must a non-contrast head CT scan be performed BEFORE performing a diagnostic lumbar puncture, to prevent precipitating fatal brainstem herniation?",
        "options": [
            {"text": "A patient with fever and neck stiffness who is fully awake, alert, oriented x 4, with normal pupillary reflexes and no focal deficits", "is_correct": False},
            {"text": "Presence of focal neurological deficits, new-onset seizures within 1 week, altered mental status / depressed consciousness, papilledema on funduscopy, or an immunocompromised state (e.g., advanced HIV)", "is_correct": True},
            {"text": "A patient with a mild maculopapular rash on the chest", "is_correct": False},
            {"text": "A patient with a positive Kernig sign and temperature of 101°F", "is_correct": False},
            {"text": "A patient who has previously taken oral ibuprofen 2 hours prior", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. Presence of focal neurological deficits, new-onset seizures within 1 week, altered mental status / depressed consciousness, papilledema on funduscopy, or an immunocompromised state (e.g., advanced HIV).\n\nPerforming a lumbar puncture in a patient with a space-occupying intracranial mass lesion (e.g., abscess, tumor, large hemorrhage) or severe cerebral edema can establish a steep rostral-caudal pressure gradient, precipitating fatal uncal or tonsillar herniation through the foramen magnum. Standard clinical guidelines dictate that a screening Head CT must precede LP ONLY if high-risk features for mass effect or elevated ICP are present (remember FAILS criteria):\n1. Focal neurological deficit (e.g., hemiparesis, visual field defect, dilated unreactive pupil)\n2. Altered mental status / depressed consciousness (GCS < 15, stupor, lethargy)\n3. Immunocompromised state (HIV/AIDS, solid organ transplant, immunosuppressive drugs)\n4. Loss of consciousness / New-onset seizure within the past week\n5. Papilledema on funduscopic examination\nCRITICAL MANAGEMENT RULE: If a head CT is required, DO NOT DELAY ANTIBIOTICS! Blood cultures must be drawn immediately, empiric antibiotics and dexamethasone administered STAT, and only THEN is the patient transported to CT, followed by lumbar puncture.\nIn the absence of these high-risk features (Option A), an LP can and should be performed immediately without a prior CT.\n\n• Options A, C, D, and E do not require a prior CT scan before LP."
    },
    {
        "id": "IH_Q138",
        "question_number": 138,
        "category": "In House: Meningitis & Infections",
        "stem": "A 55-year-old man undergoes lumbar puncture for suspected meningitis. The CSF results are displayed below:\n- Appearance: Turbid / cloudy\n- Opening pressure: 320 mm H2O (normal 70-200)\n- White blood cells: 3,800 /mm³ (88% polymorphonuclear neutrophils)\n- Protein: 280 mg/dL (normal 15-45)\n- Glucose: 16 mg/dL (normal 45-80; serum glucose 100 mg/dL; CSF:serum ratio = 0.16)\nGram stain demonstrates Gram-positive, lancet-shaped diplococci. Prior to or alongside the first dose of intravenous ceftriaxone and vancomycin, what adjunctive medication should be administered to reduce the risk of sensorineural hearing loss, neurological complications, and mortality?",
        "options": [
            {"text": "Intravenous Dexamethasone", "is_correct": True},
            {"text": "Intravenous Mannitol", "is_correct": False},
            {"text": "Oral Acetazolamide", "is_correct": False},
            {"text": "Intravenous Phenytoin", "is_correct": False},
            {"text": "Intravenous Heparin", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Intravenous Dexamethasone.\n\nThe patient has acute Streptococcus pneumoniae (pneumococcal) meningitis, confirmed by lancet-shaped Gram-positive diplococci and classic bacterial CSF findings (turbid, neutrophilic pleocytosis, high protein, markedly low glucose).\n- Rationale for Dexamethasone: When bactericidal antibiotics lyse bacteria in the subarachnoid space, massive amounts of bacterial cell wall components (peptidoglycan, teichoic acid, pneumolysin) are released, triggering an explosive inflammatory response in the meninges and subarachnoid space. This inflammatory cascade causes severe cerebral edema, increased ICP, cortical thrombophlebitis, and cochlear damage. Clinical trials demonstrate that administering adjunctive Dexamethasone (10 mg IV) prior to or concurrently with the first dose of antibiotics significantly dampens this cytokine surge, reducing the incidence of severe sensorineural hearing loss, long-term neurological sequelae, and overall mortality in pneumococcal meningitis.\n- Timing is critical: Steroids must be given BEFORE or WITH the first antibiotic dose; giving steroids after antibiotics have already lysed bacteria provides no clinical benefit.\n\n• Option B is incorrect: Mannitol treats acute herniation, not the primary inflammatory response in meningitis.\n• Option C is incorrect: Acetazolamide is for chronic pseudotumor cerebri, not acute bacterial meningitis.\n• Option D is incorrect: Prophylactic anticonvulsants are not routinely indicated unless clinical seizures occur.\n• Option E is incorrect: Anticoagulation is contraindicated due to the risk of hemorrhagic transformation."
    },
    {
        "id": "IH_Q139",
        "question_number": 139,
        "category": "In House: Meningitis & Infections",
        "stem": "A 21-year-old college student presents with mild fever (100.8°F / 38.2°C), headache, mild photophobia, and slight neck stiffness. Neurological examination is completely normal with no focal deficits. Lumbar puncture demonstrates:\n- Appearance: Clear, colorless\n- Opening pressure: 160 mm H2O (normal 70-200)\n- White blood cells: 180 /mm³ (95% lymphocytes, 5% neutrophils)\n- Protein: 65 mg/dL (mildly elevated; normal 15-45)\n- Glucose: 60 mg/dL (normal; serum glucose 95 mg/dL; CSF:serum ratio = 0.63)\n- Gram stain: No organisms seen\nWhat is the most likely diagnosis, and what viral family is the most common cause of this clinical presentation?",
        "options": [
            {"text": "Acute bacterial meningitis; Neisseria meningitidis", "is_correct": False},
            {"text": "Viral (aseptic) meningitis; Enteroviruses (Coxsackievirus, Echovirus)", "is_correct": True},
            {"text": "Fungal meningitis; Cryptococcus neoformans", "is_correct": False},
            {"text": "Tuberculous meningitis; Mycobacterium tuberculosis", "is_correct": False},
            {"text": "Neurosyphilis; Treponema pallidum", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. Viral (aseptic) meningitis; Enteroviruses (Coxsackievirus, Echovirus).\n\nThis patient exhibits the classic CSF profile of Viral (Aseptic) Meningitis:\n1. CSF Appearance: Clear or slightly opalescent.\n2. Opening Pressure: Normal to only mildly elevated (<200–250 mm H2O).\n3. Cell Count: Mildly to moderately elevated (typically 10–500 /mm³), with a predominant LYMPHOCYTIC pleocytosis (>80-90% lymphocytes; note: early in the first 24 hours, neutrophils may transiently predominate before rapidly converting to lymphocytes).\n4. Protein: Normal to only mildly elevated (50–100 mg/dL).\n5. Glucose: Completely NORMAL (CSF glucose > 40 mg/dL, CSF:serum glucose ratio > 0.6). Viruses do not consume glucose in the CSF.\nEtiology: Non-polio Enteroviruses (specifically Coxsackieviruses A and B, Echoviruses, and Enterovirus 71) account for >85–90% of all cases of viral meningitis in children and young adults, typically peaking in late summer and early autumn. Herpes simplex virus type 2 (HSV-2; Mollaret meningitis), varicella-zoster virus (VZV), and arboviruses are other recognized viral causes. Viral meningitis is typically self-limiting and managed with supportive care.\n\n• Option A is incorrect: Bacterial meningitis shows cloudy CSF, >1000 neutrophils, and very low glucose.\n• Option C is incorrect: Fungal meningitis exhibits elevated pressure, lymphocytes, elevated protein, and LOW glucose.\n• Option D is incorrect: TB meningitis exhibits very high protein (>150-500), low glucose, and fibrinous web formation.\n• Option E is incorrect: Neurosyphilis does not present with acute summer viral meningitis."
    },
    {
        "id": "IH_Q140",
        "question_number": 140,
        "category": "In House: Meningitis & Infections",
        "stem": "A 2-week-old newborn infant is evaluated in the neonatal intensive care unit for poor feeding, lethargy, hypothermia (temperature 96.2°F / 35.7°C), bulging anterior fontanelle, and irritability. Lumbar puncture confirms acute neonatal bacterial meningitis. Which of the following trios represents the most common bacterial etiologies of neonatal meningitis acquired during passage through the birth canal, and what is the recommended empiric antibiotic regimen?",
        "options": [
            {"text": "Streptococcus pneumoniae, Neisseria meningitidis, Haemophilus influenzae; Ceftriaxone + Vancomycin", "is_correct": False},
            {"text": "Group B Streptococcus (Streptococcus agalactiae), Escherichia coli (K1 capsular strain), and Listeria monocytogenes; Ampicillin + Gentamicin (or Ampicillin + Cefotaxime)", "is_correct": True},
            {"text": "Staphylococcus aureus, Pseudomonas aeruginosa, Enterococcus faecalis; Cefepime + Metronidazole", "is_correct": False},
            {"text": "Treponema pallidum, Toxoplasma gondii, Cytomegalovirus; Penicillin G + Pyrimethamine", "is_correct": False},
            {"text": "Clostridium tetani, Corynebacterium diphtheriae, Bordetella pertussis; DTaP vaccine immediately", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. Group B Streptococcus (Streptococcus agalactiae), Escherichia coli (K1 capsular strain), and Listeria monocytogenes; Ampicillin + Gentamicin (or Ampicillin + Cefotaxime).\n\nNeonatal meningitis (in infants <1 month of age) involves organisms colonizing the maternal vaginal tract and perineum:\n1. Top 3 Pathogens:\n   - Group B Streptococcus (S. agalactiae): The #1 most common cause (>50%); Gram-positive cocci in chains, narrow zone of beta-hemolysis, bacitracin resistant, CAMP test positive.\n   - Escherichia coli: The #2 cause (~20–30%), specifically strains expressing the K1 capsular polysaccharide antigen that resists complement and facilitates meningeal invasion.\n   - Listeria monocytogenes: Gram-positive motile rod transmitted transplacentally or via birth canal.\n2. Empiric Antimicrobial Regimen: Ampicillin + Gentamicin (or Ampicillin + Cefotaxime). Ampicillin covers Group B Strep and Listeria; Gentamicin or Cefotaxime provides potent synergy and gram-negative coverage against E. coli.\n(Note: Ceftriaxone is contraindicated in neonates because it displaces bilirubin from albumin, increasing the risk of kernicterus, and can precipitate with calcium in the gallbladder/biliary sludging).\n\n• Option A is incorrect: S. pneumoniae and N. meningitidis cause meningitis in older infants, children, and adults.\n• Option C is incorrect: S. aureus and Pseudomonas cause hospital-acquired/shunt infections.\n• Option D is incorrect: These are congenital TORCH infections.\n• Option E is incorrect: These cause tetanus, diphtheria, and whooping cough, not acute neonatal meningitis."
    }
]

questions_section4.extend([
    {'category': 'In House: Headache Disorders',
 'explanation': 'Correct Answer: B. Women with migraine with aura already possess an elevated baseline risk for '
                'ischemic stroke; exogenous estrogens produce a synergistic, markedly increased risk of ischemic '
                'stroke and thromboembolism.\n'
                '\n'
                'Migraine with Aura (classic migraine) is present in roughly 25–30% of migraine sufferers:\n'
                '1. Aura Criteria: Reversible focal neurological symptoms that spread gradually over >=5 minutes and '
                'last 5 to 60 minutes, most commonly visual (scintillating scotoma, fortification spectra, '
                'teichopsia), followed by sensory (unilateral spreading numbness/tingling), or speech/language '
                'disturbance, followed by the headache.\n'
                '2. Cardiovascular/Cerebrovascular Risk: Large epidemiological studies demonstrate that women who have '
                'Migraine WITH AURA have an independent 2- to 3-fold increased relative risk of ischemic stroke, as '
                'well as elevated risk of myocardial infarction. Migraine WITHOUT aura does not carry this elevated '
                'stroke risk.\n'
                '3. Contraindication: Exogenous estrogen (found in combined oral contraceptive pills, transdermal '
                'contraceptive patches, and vaginal rings) promotes hepatic synthesis of clotting factors (fibrinogen, '
                'factors VII, VIII, X) and decreases antithrombin III, inducing a prothrombotic state. Combining '
                'estrogen with migraine with aura produces a multiplicative, unacceptably high risk of arterial '
                'ischemic stroke. The CDC, WHO, and ACOG classify combined hormonal contraceptives as Medical '
                'Eligibility Criteria Category 4 (UNACCEPTABLE HEALTH RISK / STRICTLY CONTRAINDICATED) in women with '
                'migraine with aura. Safe contraceptive alternatives include progestin-only pills, levonorgestrel IUD, '
                'copper IUD, or subdermal etonogestrel implants.\n'
                '\n'
                '• Options A, C, D, and E represent incorrect mechanisms and false associations.',
 'id': 'IH_Q136_sec4',
 'id_clean': 'IH_Q146',
 'options': [{'is_correct': False, 'text': 'Estrogen causes immediate degradation of the blood-brain barrier'},
             {'is_correct': True,
              'text': 'Women with migraine with aura already possess an elevated baseline risk for ischemic stroke; '
                      'exogenous estrogens produce a synergistic, markedly increased risk of ischemic stroke and '
                      'thromboembolism'},
             {'is_correct': False, 'text': 'Estrogen directly blocks serotonin 5-HT1B receptors in cranial vessels'},
             {'is_correct': False, 'text': 'Combination pills provoke fatal status epilepticus in migraineurs'},
             {'is_correct': False, 'text': 'Progestins induce pituitary microadenomas specifically in migraineurs'}],
 'question_number': 146,
 'stem': 'A 26-year-old woman presents to her primary care physician requesting oral contraceptive pills for birth '
         'control. During her review of systems, she notes that 3 to 4 times a year she experiences a visual '
         "disturbance consisting of shimmering, jagged, zigzag lines ('fortification spectra') expanding across her "
         'right visual field over 20 minutes, followed by numbness spreading from her right hand up into her right '
         'face. As the visual and sensory symptoms resolve, she develops a severe, pulsating left-sided headache with '
         'nausea and photophobia lasting 24 hours. Why are combination estrogen-containing oral contraceptives '
         'strictly contraindicated in women who experience migraine with aura?'},
    {'category': 'In House: Headache Disorders',
 'explanation': 'Correct Answer: B. Weak inhibition of carbonic anhydrase isozymes (CA-II and CA-IV).\n'
                '\n'
                'Topiramate is a first-line anticonvulsant used for migraine prophylaxis (Level A evidence). It '
                'possesses multiple pharmacological actions: (1) Blocks voltage-gated Na+ channels, (2) Potentiates '
                'GABA-A receptor inhibitory currents, (3) Antagonizes AMPA/kainate glutamate receptors, and (4) Acts '
                'as a weak inhibitor of Carbonic Anhydrase (CA-II and CA-IV).\n'
                'Carbonic anhydrase inhibition accounts for several characteristic clinical adverse effects:\n'
                '- Paresthesias (numbness/tingling in fingers and toes): altered pH and sensory nerve electrolyte '
                'gradients.\n'
                '- Altered taste of carbonated soda (carbonic acid taste flat): inhibition of salivary/tongue carbonic '
                'anhydrase.\n'
                '- Non-anion gap metabolic acidosis: renal bicarbonate wasting (similar to acetazolamide).\n'
                '- Nephrolithiasis (kidney stones in ~1.5%): alkaline urine and hypocitraturia promote calcium '
                'phosphate stone precipitation.\n'
                'Other major topiramate side effects include cognitive slowing / memory blunting / word-finding '
                "difficulty (colloquially termed 'Dopamax'), weight loss (often considered a favorable side effect), "
                'acute angle-closure glaucoma, and teratogenicity (increased risk of oral clefts / cleft lip and '
                'palate in the first trimester).\n'
                '\n'
                '• Options A, C, D, and E do not account for carbonic anhydrase-mediated paresthesias or altered '
                'carbonation taste.',
 'id': 'IH_Q147',
 'options': [{'is_correct': False, 'text': 'Blockade of voltage-gated L-type calcium channels'},
             {'is_correct': True, 'text': 'Weak inhibition of carbonic anhydrase isozymes (CA-II and CA-IV)'},
             {'is_correct': False, 'text': 'Direct agonism at presynaptic dopamine D2 receptors'},
             {'is_correct': False, 'text': 'Irreversible inhibition of monoamine oxidase B'},
             {'is_correct': False, 'text': 'Competitive antagonism at histamine H1 receptors'}],
 'question_number': 147,
 'stem': 'A 34-year-old woman with a history of severe episodic migraines is started on topiramate for daily '
         'preventive therapy. At her 6-week follow-up, she reports significant reduction in headache frequency, but '
         'complains of tingling in her fingers and toes (paresthesias), trouble recalling common words during '
         "conversations ('word-finding difficulty'), decreased appetite with a 7-pound weight loss, and dysgeusia "
         "(carbonated beverages taste completely flat). Which of topiramate's multifaceted pharmacological mechanisms "
         'accounts for the tingling and flat taste of carbonated drinks?'},
    {'category': 'In House: Traumatic Brain Injuries',
 'explanation': 'Correct Answer: B. Perform a diagnostic lumbar puncture to evaluate for elevated red blood cells and '
                'xanthochromia in the CSF.\n'
                '\n'
                'Subarachnoid Hemorrhage (SAH) is the most critical secondary headache emergency, most commonly caused '
                'by rupture of a saccular (berry) aneurysm at the Circle of Willis (most frequently the anterior '
                'communicating artery, followed by the posterior communicating artery and middle cerebral artery '
                'bifurcation):\n'
                "- Clinical hallmark: 'Thunderclap' headache—a severe headache that reaches instantaneous or maximum "
                "peak intensity within 1 minute ('worst headache of life'), often during physical exertion or "
                'Valsalva, accompanied by neck stiffness (chemical meningismus).\n'
                '- Diagnostic Algorithm:\n'
                '  1. Step 1: Immediate NON-CONTRAST HEAD CT. Non-contrast CT is ~98-100% sensitive in the first 6 '
                'hours, but sensitivity drops rapidly over subsequent days (to 85% at 24 hours and <50% at 1 week) as '
                'extravasated blood is cleared or diluted by CSF.\n'
                '  2. Step 2: If the non-contrast CT is NEGATIVE (or equivocal) and clinical suspicion for SAH remains '
                'high, a LUMBAR PUNCTURE is MANDATORY!\n'
                '- CSF Findings in SAH:\n'
                '  - Persistent, non-clearing RBC count from tube 1 to tube 4 (distinguishing SAH from a traumatic '
                'tap, where RBC counts clear significantly by tube 4).\n'
                '  - XANTHOCHROMIA: A yellow, pink, or amber discoloration of the centrifuged CSF supernatant caused '
                'by the enzymatic degradation of red blood cell hemoglobin into oxyhemoglobin and bilirubin by tissue '
                'macrophages. Bilirubin formation requires at least 2 to 4 hours in vivo and peaks at 12 hours; its '
                'presence definitively confirms an intracranial subarachnoid bleed.\n'
                '\n'
                '• Option A is incorrect: Discharging a patient with an uninvestigated thunderclap headache risks '
                'fatal re-bleeding from a ruptured aneurysm.\n'
                '• Option C is incorrect: EEG does not detect subarachnoid hemorrhage.\n'
                '• Option D is incorrect: Analgesia alone without completing the SAH rule-out is malpractice.\n'
                '• Option E is incorrect: Acyclovir does not rule out aneurysmal subarachnoid hemorrhage.',
 'id': 'IH_Q148',
 'options': [{'is_correct': False,
              'text': 'Reassure the patient that serious pathology has been ruled out and discharge him on oral '
                      'ibuprofen'},
             {'is_correct': True,
              'text': 'Perform a diagnostic lumbar puncture to evaluate for elevated red blood cells and xanthochromia '
                      'in the CSF'},
             {'is_correct': False, 'text': 'Schedule an outpatient routine EEG in 4 weeks'},
             {'is_correct': False, 'text': 'Administer intramuscular ketorolac and reassess in 24 hours'},
             {'is_correct': False, 'text': 'Initiate empiric oral acyclovir for viral meningitis'}],
 'question_number': 148,
 'stem': 'A 48-year-old man presents to the emergency department after experiencing a sudden, explosive headache that '
         "reached maximum, unbearable intensity within 30 seconds while lifting a heavy weight ('worst headache of my "
         "life / thunderclap headache'). He has mild photophobia and neck stiffness, but is alert with a normal "
         'neurological exam without focal deficits. An immediate non-contrast head CT performed 4 hours after headache '
         'onset is reviewed by the attending radiologist and reported as completely normal with no intracranial blood '
         'seen. What is the mandatory next diagnostic step in management?'},
    {'category': 'In House: Traumatic Brain Injuries',
 'explanation': 'Correct Answer: B. Contrecoup contusion: as the skull decelerates upon impact, the inertia of the '
                'suspended brain causes it to rebound forcefully against the rough, irregular bony surfaces of the '
                'anterior cranial fossa and sphenoid wing opposite the point of impact.\n'
                '\n'
                'Cerebral contusions represent macroscopic bruising of the brain parenchyma involving the crests of '
                'gyri:\n'
                '1. Coup Injury: Occurs directly beneath the point of skull impact. It results from direct inbending '
                'of bone compressing the underlying cortex; common when a moving object strikes a stationary head '
                '(e.g., bat hitting head).\n'
                '2. Contrecoup Injury: Occurs on the brain surface directly OPPOSITE the site of cranial impact. It '
                'results when a moving head strikes a stationary, unyielding surface (e.g., fall backward onto the '
                'floor, MVA). Upon impact, the rigid skull abruptly halts, but the floating brain continues moving '
                'forward due to inertia, rebounding violently against the sharp, jagged internal bony ridges of the '
                'skull table.\n'
                '3. Vulnerable Sites: The floor of the anterior cranial fossa (orbital surface of the frontal lobes) '
                'and the sphenoid ridges / middle cranial fossa (crests and tips of the temporal poles) have '
                'irregular, sharp bony contours. Consequently, an occipital impact produces severe, devastating '
                'CONTRECOUP contusions of the frontal and temporal poles, whereas coup contusions under the smooth '
                'internal surface of the occipital bone are typically mild or absent.\n'
                '\n'
                '• Option A is incorrect: Coup occurs at the impact site, not opposite.\n'
                '• Option C is incorrect: Venous sinus thrombosis is not the mechanism of focal polar contusions.\n'
                '• Option D is incorrect: Fat embolism causes diffuse petechiae, not focal frontal/temporal '
                'contusions.\n'
                '• Option E is incorrect: Aneurysm rupture causes subarachnoid hemorrhage, not localized cortical '
                'polar contusions.',
 'id': 'IH_Q149',
 'options': [{'is_correct': False, 'text': 'Coup injury alone without brain motion'},
             {'is_correct': True,
              'text': 'Contrecoup contusion: as the skull decelerates upon impact, the inertia of the suspended brain '
                      'causes it to rebound forcefully against the rough, irregular bony surfaces of the anterior '
                      'cranial fossa and sphenoid wing opposite the point of impact'},
             {'is_correct': False, 'text': 'Selective thrombosis of the superior sagittal sinus'},
             {'is_correct': False, 'text': 'Embolization of bone marrow fat into the middle cerebral artery'},
             {'is_correct': False, 'text': 'Secondary rupture of a pre-existing basilar tip aneurysm'}],
 'question_number': 149,
 'stem': 'An 80-year-old pedestrian is struck from behind by a bicycle and falls backward, striking the occiput of his '
         'head forcefully against the asphalt pavement. At autopsy following his death 48 hours later, gross '
         'pathological examination reveals a small scalp laceration and linear fracture of the occipital bone at the '
         'site of impact. However, the most severe, hemorrhagic contusions and brain lacerations are discovered at the '
         'anterior tips of the frontal poles and the inferior-lateral surfaces of the temporal poles. What traumatic '
         'mechanism explains this disparity between the impact site and the location of maximum parenchymal injury?'},
    {'category': 'In House: Meningitis & Infections',
 'explanation': 'Correct Answer: B. Intravenous Liposomal Amphotericin B combined with oral Flucytosine for at least 2 '
                'weeks, followed by oral Fluconazole consolidation.\n'
                '\n'
                'Cryptococcal Meningitis is an opportunistic fungal infection caused by Cryptococcus neoformans (an '
                'environmental basidiomycete yeast found in pigeon droppings and soil), primarily affecting '
                'immunocompromised patients with CD4 counts < 100 cells/mm³:\n'
                '1. Pathological Features: Cryptococcus is a heavily encapsulated yeast with narrow-based budding. Its '
                'thick polysaccharide capsule (composed of glucuronoxylomannan) resists phagocytosis. India ink '
                'microscopy displays round yeast cells surrounded by wide, transparent halos (capsule excludes ink '
                'particles). Mucicarmine stains the capsule bright red. Detection of Cryptococcal Antigen (CrAg) via '
                'lateral flow assay or latex agglutination is >98% sensitive and specific.\n'
                '2. Clinical Management:\n'
                '   - Danger of Increased ICP: Capsular polysaccharide plugs the arachnoid villi, resulting in '
                'dangerously high CSF opening pressures (>250–350 mm H2O) that can cause optic nerve atrophy and '
                'sudden blindness. Serial therapeutic lumbar punctures are required to drain CSF and maintain opening '
                'pressure <200 mm H2O.\n'
                '   - Antifungal Protocol: Gold-standard induction therapy is Liposomal Amphotericin B (binds '
                'ergosterol, creating membrane pores) PLUS Flucytosine (5-FC, converted to 5-fluorouracil inside '
                'fungal cells by cytosine deaminase, blocking thymidylate synthase and DNA synthesis) for at least 2 '
                'weeks. Once clinical improvement and CSF sterilization occur, therapy transitions to high-dose oral '
                'Fluconazole for 8 weeks (consolidation), followed by low-dose Fluconazole maintenance until CD4 '
                'counts recover >100 cells/mm³ on antiretroviral therapy.\n'
                '\n'
                '• Option A is incorrect: Fluconazole monotherapy has unacceptably high induction mortality in '
                'cryptococcal meningitis.\n'
                '• Options C, D, and E represent antibacterial and antiviral regimens.',
 'id': 'IH_Q150',
 'options': [{'is_correct': False, 'text': 'Oral Fluconazole monotherapy for 10 days'},
             {'is_correct': True,
              'text': 'Intravenous Liposomal Amphotericin B combined with oral Flucytosine for at least 2 weeks, '
                      'followed by oral Fluconazole consolidation'},
             {'is_correct': False, 'text': 'Intravenous Ceftriaxone plus Vancomycin'},
             {'is_correct': False, 'text': 'Intravenous Acyclovir plus Ganciclovir'},
             {'is_correct': False, 'text': 'Intravenous Metronidazole plus Cefepime'}],
 'question_number': 150,
 'stem': 'A 38-year-old man with advanced, untreated HIV/AIDS (CD4 count 28 cells/mm³) presents with a 2-week history '
         'of dull, progressive headache, low-grade fever, malaise, and memory lapses. Physical examination reveals '
         'mild neck stiffness without focal neurological deficits. Non-contrast head CT is normal without mass effect '
         'or hydrocephalus. Lumbar puncture reveals a markedly elevated opening pressure of 360 mm H2O. CSF analysis '
         'reveals:\n'
         '- White blood cells: 95 /mm³ (90% lymphocytes)\n'
         '- Protein: 140 mg/dL\n'
         '- Glucose: 22 mg/dL (serum glucose 90 mg/dL)\n'
         'India ink preparation of the CSF reveals round budding yeast cells surrounded by wide, clear unstained '
         'halos. Latex agglutination for cryptococcal capsular antigen (CrAg) is strongly positive. What is the '
         'definitive initial antimicrobial induction regimen for this fungal meningitis?'},
])

if __name__ == "__main__":
    print(f"Section 4 Question Count: {len(questions_section4)}")
    ids = [q["id"] for q in questions_section4]
    assert len(ids) == len(set(ids)), "Duplicate IDs found!"
    print("Section 4 validated successfully!")
