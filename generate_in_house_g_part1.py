# Part 1: Questions 1 to 48 (Demyelinating: 15 Qs, Cerebellum: 12 Qs, Tumors: 21 Qs)
import json

def get_part1_questions():
    qs = []

    # =========================================================================
    # UNIT 1: DEMYELINATING DISEASES (15 Questions: Q1 - Q15, 10%)
    # =========================================================================

    # Q1
    qs.append({
        "id": "exam3_in_house_like_g_q1",
        "q_num": "1",
        "stem": "A 28-year-old woman presents with painful visual blurring in her left eye and painful ocular movement over 3 days. Examination shows visual acuity of 20/100 in the left eye, decreased color desaturation, and a left relative afferent pupillary defect. Funduscopic examination shows a normal optic disc. MRI demonstrates hyperintensity of the left optic nerve and multiple periventricular white matter T2/FLAIR hyperintensities oriented perpendicularly to the lateral ventricles. Which of the following is the most appropriate acute pharmacotherapy for this patient's presentation?",
        "category": "Demyelinating Disease",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Subcutaneous interferon beta-1a therapy"},
            {"letter": "B", "is_correct": False, "text": "Subcutaneous glatiramer acetate therapy"},
            {"letter": "C", "is_correct": True, "text": "Intravenous methylprednisolone therapy"},
            {"letter": "D", "is_correct": False, "text": "Intravenous immune globulin infusion"},
            {"letter": "E", "is_correct": False, "text": "Therapeutic plasma exchange treatment"}
        ],
        "correct_idx": 2,
        "explanation": "This patient presents with acute optic neuritis in the setting of multiple sclerosis (MS) with typical Dawson fingers (periventricular demyelinating plaques perpendicular to the ventricles along medullary venules). First-line therapy for acute MS relapses is high-dose intravenous methylprednisolone (1000 mg daily for 3-5 days) to accelerate functional recovery. Interferon-beta and glatiramer are disease-modifying therapies for chronic maintenance, not acute relapse abortive therapy.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Acute multiple sclerosis relapses (including acute optic neuritis) are treated with high-dose intravenous methylprednisolone. Disease-modifying agents are for chronic relapse prevention.",
        "image": None
    })

    # Q2
    qs.append({
        "id": "exam3_in_house_like_g_q2",
        "q_num": "2",
        "stem": "A 32-year-old woman with relapsing-remitting multiple sclerosis undergoes diagnostic lumbar puncture during an initial clinical workup. Which of the following cerebrospinal fluid (CSF) profiles is most characteristically observed in patients with this condition?",
        "category": "Demyelinating Disease",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Marked neutrophilic pleocytosis with severe hypoglycorrhachia"},
            {"letter": "B", "is_correct": False, "text": "Albuminocytologic dissociation with completely normal IgG index"},
            {"letter": "C", "is_correct": True, "text": "Oligoclonal bands on electrophoresis with elevated IgG index"},
            {"letter": "D", "is_correct": False, "text": "Marked eosinophilic pleocytosis with high opening pressure"},
            {"letter": "E", "is_correct": False, "text": "Xanthochromia with persistently elevated erythrocyte counts"}
        ],
        "correct_idx": 2,
        "explanation": "The classic CSF finding in multiple sclerosis (>90% of cases) is the presence of two or more oligoclonal IgG bands (OCBs) on agarose gel electrophoresis that are absent in paired serum, reflecting intrathecal IgG synthesis, accompanied by an elevated CSF IgG index and elevated myelin basic protein. Albuminocytologic dissociation is characteristic of Guillain-Barré syndrome.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Multiple sclerosis CSF demonstrates oligoclonal IgG bands and elevated IgG index/myelin basic protein with mild lymphocytic pleocytosis (<50 cells/uL) and normal glucose.",
        "image": None
    })

    # Q3
    qs.append({
        "id": "exam3_in_house_like_g_q3",
        "q_num": "3",
        "stem": "A 25-year-old woman with multiple sclerosis presents with diplopia on horizontal gaze. Examination reveals that upon attempted left lateral gaze, the right eye fails to adduct past the midline, while the left eye abducts with horizontal monocular nystagmus. Convergence remains completely intact. Which of the following central nervous system pathways is damaged?",
        "category": "Demyelinating Disease",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Right paramedian pontine reticular formation"},
            {"letter": "B", "is_correct": False, "text": "Left abducens cranial nerve somatic motor nucleus"},
            {"letter": "C", "is_correct": False, "text": "Right oculomotor cranial nerve visceral motor nucleus"},
            {"letter": "D", "is_correct": True, "text": "Right medial longitudinal fasciculus pathway"},
            {"letter": "E", "is_correct": False, "text": "Left cortical frontal eye field motor center"}
        ],
        "correct_idx": 3,
        "explanation": "This patient has right internuclear ophthalmoplegia (INO), a hallmark of demyelinating disease in young adults. The medial longitudinal fasciculus (MLF) coordinates conjugate horizontal gaze by transmitting signals from the abducens nucleus (pons) to the contralateral oculomotor nucleus (midbrain). A right MLF lesion impairs right eye adduction on leftward gaze with nystagmus of the abducting left eye. Convergence is mediated by separate cortical pathways bypassing the MLF and remains intact.",
        "high_yield_pearl": "High-Yield Clinical Pearl: INO is caused by demyelination of the MLF. The affected MLF side corresponds to the eye that cannot adduct. Bilateral INO is virtually pathognomonic for multiple sclerosis.",
        "image": None
    })

    # Q4
    qs.append({
        "id": "exam3_in_house_like_g_q4",
        "q_num": "4",
        "stem": "A 34-year-old woman with multiple sclerosis reports that taking a hot shower or exercising vigorously causes transient blurring of vision and profound subjective limb weakness that completely resolves within 30 minutes of cooling down. Which of the following pathophysiological mechanisms best explains this phenomenon?",
        "category": "Demyelinating Disease",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Acute acceleration of autoimmune axonal transection"},
            {"letter": "B", "is_correct": True, "text": "Temperature-dependent conduction block in demyelinated axons"},
            {"letter": "C", "is_correct": False, "text": "Transient vasoconstriction of deep cerebral microvessels"},
            {"letter": "D", "is_correct": False, "text": "Reversible breakdown of the central blood-brain barrier"},
            {"letter": "E", "is_correct": False, "text": "Exaggerated peripheral neuromuscular junction fatigue"}
        ],
        "correct_idx": 1,
        "explanation": "This clinical presentation represents Uhthoff phenomenon, characterized by reversible worsening of pre-existing neurological deficits in MS upon elevated core body temperature. Demyelinated axons have a depleted safety factor for action potential transmission; increased temperature increases potassium conductance and speeds sodium channel inactivation, causing temporary conduction block across demyelinated segments.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Uhthoff phenomenon is a heat-induced reversible conduction block in demyelinated axons, not a true disease relapse.",
        "image": None
    })

    # Q5
    qs.append({
        "id": "exam3_in_house_like_g_q5",
        "q_num": "5",
        "stem": "A 36-year-old woman presents with severe bilateral vision loss and paraparesis with urinary retention over 48 hours. Brain MRI is normal, but spinal cord MRI demonstrates a contiguous T2 hyperintensity extending from C2 to T6 (4 contiguous vertebral segments). Serum testing is positive for autoantibodies directed against aquaporin-4 (AQP4). Which of the following cellular structures is the primary target of these autoantibodies?",
        "category": "Demyelinating Disease",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Myelin sheaths formed by central oligodendrocytes"},
            {"letter": "B", "is_correct": False, "text": "Voltage-gated potassium channels at nodes of Ranvier"},
            {"letter": "C", "is_correct": True, "text": "Water channels on astrocytic foot processes"},
            {"letter": "D", "is_correct": False, "text": "Peripheral myelin protein 22 on Schwann cells"},
            {"letter": "E", "is_correct": False, "text": "Postsynaptic nicotinic acetylcholine receptors"}
        ],
        "correct_idx": 2,
        "explanation": "Neuromyelitis optica (NMO / Devic disease) is an inflammatory CNS disorder characterized by severe optic neuritis and longitudinally extensive transverse myelitis (LETM, spanning >=3 vertebral segments). It is mediated by pathogenic IgG antibodies targeting aquaporin-4 (AQP4) water channels located predominantly on astrocytic end-feet, leading to complement-mediated astrocyte destruction and secondary demyelination.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Neuromyelitis optica targets aquaporin-4 on astrocyte foot processes (an astrocytopathy), unlike MS which directly targets oligodendrocyte myelin.",
        "image": None
    })

    # Q6
    qs.append({
        "id": "exam3_in_house_like_g_q6",
        "q_num": "6",
        "stem": "A 30-year-old man presents with progressive symmetric leg weakness and tingling in his toes 3 weeks following a diarrheal illness caused by Campylobacter jejuni. Examination reveals bilateral lower extremity weakness (3/5), absent patellar and Achilles deep tendon reflexes, and mild distal sensory loss. Which of the following immunopathologic mechanisms is directly responsible for this patient's illness?",
        "category": "Demyelinating Disease",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Direct persistent bacterial invasion of peripheral nerve sheaths"},
            {"letter": "B", "is_correct": False, "text": "Bacterial exotoxin-mediated destruction of anterior horn cells"},
            {"letter": "C", "is_correct": True, "text": "Cross-reactive antibodies targeting peripheral gangliosides"},
            {"letter": "D", "is_correct": False, "text": "Autoantibody-mediated blockade of presynaptic calcium channels"},
            {"letter": "E", "is_correct": False, "text": "CD8+ cytotoxic T-cell destruction of central oligodendrocytes"}
        ],
        "correct_idx": 2,
        "explanation": "Guillain-Barré syndrome (acute inflammatory demyelinating polyradiculoneuropathy, AIDP) classically follows Campylobacter jejuni enteritis. Pathogenesis involves molecular mimicry: lipooligosaccharides (LOS) in the Campylobacter bacterial outer wall resemble peripheral nerve gangliosides (e.g. GM1, GD1a). The humoral response produces cross-reactive autoantibodies that trigger complement activation, macrophage infiltration, and demyelination of peripheral nerves and nerve roots.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Guillain-Barré syndrome involves molecular mimicry between Campylobacter jejuni lipooligosaccharides and human gangliosides (GM1/GD1a), causing ascending flaccid paralysis and areflexia.",
        "image": None
    })

    # Q7
    qs.append({
        "id": "exam3_in_house_like_g_q7",
        "q_num": "7",
        "stem": "A 42-year-old man is admitted to the intensive care unit with Guillain-Barré syndrome and rapidly ascending flaccid quadriparesis. On hospital day 4, his vital signs demonstrate wide fluctuations: heart rate ranges from 45 to 135 bpm, and blood pressure swings from 85/50 to 190/110 mmHg with marked facial diaphoresis. Which of the following is the most likely underlying cause of these hemodynamic findings?",
        "category": "Demyelinating Disease",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Undetected adrenal pheochromocytoma crisis"},
            {"letter": "B", "is_correct": False, "text": "Fulminant secondary hospital-acquired septic shock"},
            {"letter": "C", "is_correct": False, "text": "Acute massive pulmonary thromboembolism"},
            {"letter": "D", "is_correct": True, "text": "Autonomic neuropathy from demyelination"},
            {"letter": "E", "is_correct": False, "text": "Acute coronary syndrome with cardiogenic shock"}
        ],
        "correct_idx": 3,
        "explanation": "Autonomic dysfunction (dysautonomia) occurs in up to 65% of hospitalized Guillain-Barré syndrome patients due to inflammatory demyelination of autonomic fibers (sympathetic and parasympathetic). Manifestations include sinus tachycardia, labile hypertension/hypotension, bradyarrhythmias (even asystole), and diaphoresis. It is a major cause of mortality requiring continuous cardiac monitoring.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Dysautonomia in Guillain-Barré syndrome is caused by autonomic fiber demyelination and requires vigilant hemodynamic monitoring in the ICU.",
        "image": None
    })

    # Q8
    qs.append({
        "id": "exam3_in_house_like_g_q8",
        "q_num": "8",
        "stem": "A 14-year-old boy presents with progressive walking difficulty, frequent tripping, and high foot arches. Physical examination shows bilateral pes cavus deformities, hammer toes, atrophy of the peroneal muscles giving a 'stork leg' appearance, and generalized hyporeflexia. Nerve conduction velocity of the peroneal nerve is markedly slowed (22 m/s; normal >40 m/s). Genetic analysis reveals a duplication on chromosome 17p11.2. Which of the following proteins is affected by this genetic defect?",
        "category": "Demyelinating Disease",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Survival motor neuron protein 1"},
            {"letter": "B", "is_correct": False, "text": "Mitochondrial iron chaperone frataxin"},
            {"letter": "C", "is_correct": True, "text": "Peripheral myelin protein 22"},
            {"letter": "D", "is_correct": False, "text": "Neurofibromin GTPase-activating protein"},
            {"letter": "E", "is_correct": False, "text": "Voltage-gated potassium channel Kv1.1"}
        ],
        "correct_idx": 2,
        "explanation": "This patient has Charcot-Marie-Tooth disease type 1A (CMT1A), the most common hereditary motor and sensory neuropathy. It is caused by an autosomal dominant duplication of the PMP22 gene on chromosome 17p11.2 encoding peripheral myelin protein 22. Overexpression leads to abnormal peripheral myelination, onion-bulb formation on nerve biopsy, distal limb wasting, pes cavus, hammer toes, and marked slowing of motor nerve conduction velocities.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Charcot-Marie-Tooth disease 1A is caused by PMP22 duplication on chromosome 17, presenting with pes cavus, stork legs, and slowed nerve conduction velocities.",
        "image": None
    })

    # Q9
    qs.append({
        "id": "exam3_in_house_like_g_q9",
        "q_num": "9",
        "stem": "A 52-year-old man with a history of alcohol use disorder is admitted for severe hyponatremia (serum sodium 104 mEq/L). Over the next 24 hours, his serum sodium is rapidly corrected to 132 mEq/L using 3% hypertonic saline. Three days later, he develops acute spastic quadriplegia, pseudobulbar palsy with dysarthria and dysphagia, and impaired horizontal eye movements, but remains awake and alert. Which of the following is the primary neuropathologic mechanism of this patient's condition?",
        "category": "Demyelinating Disease",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Acute thrombosis of the anterior spinal artery"},
            {"letter": "B", "is_correct": True, "text": "Osmotic demyelination of the central basis pontis"},
            {"letter": "C", "is_correct": False, "text": "Cerebral edema secondary to acute hyponatremia"},
            {"letter": "D", "is_correct": False, "text": "Excitotoxic hemorrhagic necrosis of mammillary bodies"},
            {"letter": "E", "is_correct": False, "text": "Diffuse microglial nodule encephalitic formation"}
        ],
        "correct_idx": 1,
        "explanation": "Rapid correction of chronic severe hyponatremia (>10-12 mEq/L in 24 hours) leads to osmotic demyelination syndrome (formerly central pontine myelinolysis). During chronic hyponatremia, pontine brain cells extrude organic osmolytes to prevent swelling; rapid hypertonic fluid administration causes brain dehydration, oligodendrocyte shrinkage, blood-brain barrier disruption, and non-inflammatory demyelination of the basis pontis (corticospinal and corticobulbar tracts), resulting in locked-in syndrome.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Rapid correction of hyponatremia causes central pontine myelinolysis ('from low to high, your pons will die'). Correct sodium slowly (<=8-10 mEq/L per 24 hours).",
        "image": None
    })

    # Q10
    qs.append({
        "id": "exam3_in_house_like_g_q10",
        "q_num": "10",
        "stem": "A 48-year-old woman with relapsing-remitting multiple sclerosis is treated with natalizumab. Two years into therapy, she develops progressive cognitive impairment, left hemiparesis, and homonymous hemianopia. Brain MRI shows multifocal asymmetric T2/FLAIR hyperintensities in subcortical white matter without mass effect or enhancement. CSF PCR is positive for JC virus DNA. Which of the following cellular populations is selectively destroyed by this virus?",
        "category": "Demyelinating Disease",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Perivascular central nervous system microglia"},
            {"letter": "B", "is_correct": False, "text": "Pyramidal neurons in neocortical layers III and V"},
            {"letter": "C", "is_correct": True, "text": "Myelin-producing central oligodendrocytes"},
            {"letter": "D", "is_correct": False, "text": "Myelin-producing peripheral Schwann cells"},
            {"letter": "E", "is_correct": False, "text": "Astrocytic end-feet maintaining the barrier"}
        ],
        "correct_idx": 2,
        "explanation": "Progressive multifocal leukoencephalopathy (PML) is caused by reactivation of the JC polyomavirus in immunosuppressed individuals, including those receiving natalizumab (which blocks alpha-4 integrin and prevents lymphocyte homing to the CNS). The JC virus selectively infects and lytically destroys oligodendrocytes, leading to widespread CNS demyelination. Histology shows enlarged oligodendrocytes with ground-glass viral inclusions and bizarre giant astrocytes.",
        "high_yield_pearl": "High-Yield Clinical Pearl: PML is caused by JC virus infection of oligodendrocytes in patients treated with natalizumab or immunosuppression, producing non-enhancing white matter demyelination.",
        "image": None
    })

    # Q11
    qs.append({
        "id": "exam3_in_house_like_g_q11",
        "q_num": "11",
        "stem": "A 9-year-old boy presents with progressive lethargy, confusion, ataxia, and left-sided hemiparesis 10 days after a mild febrile illness and rash from varicella. Brain MRI reveals widespread, bilateral, poorly demarcated T2 hyperintensities in the subcortical white matter, brainstem, and cerebellar peduncles with patchy enhancement. CSF examination demonstrates mild lymphocytic pleocytosis and elevated protein with absent oligoclonal bands. The patient improves dramatically following a course of high-dose corticosteroids. Which of the following is the most likely diagnosis?",
        "category": "Demyelinating Disease",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Primary progressive multiple sclerosis"},
            {"letter": "B", "is_correct": True, "text": "Acute disseminated encephalomyelitis"},
            {"letter": "C", "is_correct": False, "text": "Progressive multifocal leukoencephalopathy"},
            {"letter": "D", "is_correct": False, "text": "Subacute sclerosing panencephalitis"},
            {"letter": "E", "is_correct": False, "text": "Adrenoleukodystrophy peroxisomal disease"}
        ],
        "correct_idx": 1,
        "explanation": "Acute disseminated encephalomyelitis (ADEM) is a monophasic post-infectious demyelinating syndrome that occurs predominantly in children following viral illnesses (e.g. varicella, measles, mumps) or vaccinations. Unlike multiple sclerosis, ADEM is typically accompanied by acute encephalopathy (confusion, lethargy), multifocal neurological deficits, bilateral symmetric or asymmetric white matter lesions, and absence of CSF oligoclonal bands. It responds rapidly to high-dose corticosteroids.",
        "high_yield_pearl": "High-Yield Clinical Pearl: ADEM is a monophasic post-viral encephalomyelitis in pediatric patients presenting with acute encephalopathy and multifocal CNS deficits, responding well to IV steroids.",
        "image": None
    })

    # Q12
    qs.append({
        "id": "exam3_in_house_like_g_q12",
        "q_num": "12",
        "stem": "A 31-year-old woman with multiple sclerosis notes an electric shock-like sensation that shoots down her spine and radiates into her extremities whenever she flexes her neck forward to look at her phone. Which of the following is the most likely anatomic site of demyelination responsible for this symptom?",
        "category": "Demyelinating Disease",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Anterior corticospinal motor tracts in lumbar cord"},
            {"letter": "B", "is_correct": True, "text": "Cervical dorsal columns of the spinal cord"},
            {"letter": "C", "is_correct": False, "text": "Medial longitudinal fasciculus in rostral midbrain"},
            {"letter": "D", "is_correct": False, "text": "Bilateral calcarine cortices in the occipital pole"},
            {"letter": "E", "is_correct": False, "text": "Ventral posterolateral nuclei of the thalamus"}
        ],
        "correct_idx": 1,
        "explanation": "This patient is describing Lhermitte sign (barber chair phenomenon), characterized by sudden paroxysmal electric shock-like sensations radiating down the spine into the limbs upon neck flexion. It is caused by mechanical stretching of demyelinated, hypersensitive sensory axons within the posterior/dorsal columns of the cervical spinal cord.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Lhermitte sign reflects demyelination in the cervical dorsal columns, producing an electric shock sensation upon neck flexion.",
        "image": None
    })

    # Q13
    qs.append({
        "id": "exam3_in_house_like_g_q13",
        "q_num": "13",
        "stem": "A 29-year-old woman presents with weakness and numbness in her left leg that began 1 week ago. Neurological examination reveals left lower extremity spasticity, hyperreflexia, and an extensor plantar response. MRI of the brain and spine reveals two contrast-enhancing T2 lesions in the periventricular white matter and one non-enhancing lesion in the cervical spinal cord. Which of the following diagnostic criteria concepts in multiple sclerosis is fulfilled by these neuroimaging findings?",
        "category": "Demyelinating Disease",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Selective involvement of peripheral nerve roots only"},
            {"letter": "B", "is_correct": True, "text": "Dissemination in both space and time on MRI"},
            {"letter": "C", "is_correct": False, "text": "Presence of acute longitudinally extensive myelitis"},
            {"letter": "D", "is_correct": False, "text": "Monophasic disease course without recurrent attacks"},
            {"letter": "E", "is_correct": False, "text": "Sparing of the central blood-brain barrier pathways"}
        ],
        "correct_idx": 1,
        "explanation": "According to the McDonald criteria for multiple sclerosis, a definitive diagnosis requires demonstrating dissemination in space (DIS: lesions in >=2 typical CNS locations: periventricular, juxtacortical/cortical, infratentorial, or spinal cord) and dissemination in time (DIT). DIT can be demonstrated on a single baseline MRI scan by the simultaneous presence of at least one asymptomatic gadolinium-enhancing lesion (active/new) and at least one non-enhancing lesion (older).",
        "high_yield_pearl": "High-Yield Clinical Pearl: MS diagnosis requires dissemination in space and time. A single MRI demonstrating simultaneous enhancing and non-enhancing lesions fulfills dissemination in time.",
        "image": None
    })

    # Q14
    qs.append({
        "id": "exam3_in_house_like_g_q14",
        "q_num": "14",
        "stem": "A 37-year-old man presents with progressive lower extremity weakness 2 weeks after an episode of gastroenteritis. Cerebrospinal fluid analysis demonstrates an opening pressure of 140 mm H2O, WBC count of 2/uL (normal 0-5), glucose of 65 mg/dL (normal 45-80), and total protein of 165 mg/dL (normal 15-45). Which of the following terms describes this classic diagnostic laboratory pattern?",
        "category": "Demyelinating Disease",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Pleocytosis with marked hypoglycorrhachia"},
            {"letter": "B", "is_correct": False, "text": "Elevated myelin basic protein index only"},
            {"letter": "C", "is_correct": True, "text": "Albuminocytologic dissociation pattern"},
            {"letter": "D", "is_correct": False, "text": "Intrathecal oligoclonal IgG band isolation"},
            {"letter": "E", "is_correct": False, "text": "Xanthochromic non-clearing erythrocyte state"}
        ],
        "correct_idx": 2,
        "explanation": "Albuminocytologic dissociation refers to markedly elevated CSF protein (>100-200 mg/dL) with normal or near-normal cell counts (<5-10 WBC/uL). This finding is classic for Guillain-Barré syndrome (AIDP), typically appearing after the first week of symptoms. It reflects extensive inflammatory transudation and protein leakage from spinal nerve roots into the subarachnoid space without meningeal infiltration.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Albuminocytologic dissociation (high CSF protein with normal WBC count) is the hallmark laboratory finding of Guillain-Barré syndrome.",
        "image": None
    })

    # Q15
    qs.append({
        "id": "exam3_in_house_like_g_q15",
        "q_num": "15",
        "stem": "A 54-year-old man with a 15-year history of relapsing-remitting multiple sclerosis has noted no discrete new attacks over the past 3 years. However, he describes an insidious, steady worsening of his walking ability, progressive bilateral lower extremity spasticity, and worsening urge incontinence. Which of the following clinical subtypes of multiple sclerosis does this patient now manifest?",
        "category": "Demyelinating Disease",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Primary progressive multiple sclerosis"},
            {"letter": "B", "is_correct": True, "text": "Secondary progressive multiple sclerosis"},
            {"letter": "C", "is_correct": False, "text": "Relapsing-remitting multiple sclerosis"},
            {"letter": "D", "is_correct": False, "text": "Clinically isolated demyelinating syndrome"},
            {"letter": "E", "is_correct": False, "text": "Fulminant Marburg acute multiple sclerosis"}
        ],
        "correct_idx": 1,
        "explanation": "This patient has transitioned to secondary progressive multiple sclerosis (SPMS). In untreated RRMS, approximately 50-60% of patients transition within 10-15 years to SPMS, characterized by gradual, steady accumulation of neurological disability without clear acute relapses or periods of remission. Primary progressive MS (PPMS) displays steady progression from initial disease onset without an antecedent relapsing-remitting phase.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Secondary progressive MS is defined by steady neurodegenerative disability progression following an initial relapsing-remitting course.",
        "image": None
    })

    # =========================================================================
    # UNIT 2: CEREBELLUM (12 Questions: Q16 - Q27, 8%)
    # =========================================================================

    # Q16
    qs.append({
        "id": "exam3_in_house_like_g_q16",
        "q_num": "16",
        "stem": "A 56-year-old man with a 25-year history of severe alcohol dependence presents with a slow, wide-based, unsteady gait. On examination, he staggers while walking and is unable to perform tandem gait. However, rapid alternating movements and finger-to-nose testing of both upper extremities are completely normal, and speech is fluent without dysarthria. Which of the following cerebellar regions is selectively damaged in this patient?",
        "category": "Cerebellum",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Left lateral cerebellar hemisphere neocortex"},
            {"letter": "B", "is_correct": True, "text": "Anterior cerebellar vermis and spinocerebellum"},
            {"letter": "C", "is_correct": False, "text": "Bilateral dentate nuclei in deep white matter"},
            {"letter": "D", "is_correct": False, "text": "Flocculonodular lobe vestibulocerebellum"},
            {"letter": "E", "is_correct": False, "text": "Bilateral superior cerebellar peduncle tracts"}
        ],
        "correct_idx": 1,
        "explanation": "Chronic alcohol neurotoxicity paired with thiamine deficiency causes selective atrophy and Purkinje cell loss in the anterior superior cerebellar vermis (spinocerebellum). Because the vermis coordinates trunk and lower extremity movements, patients present with severe truncal and gait ataxia ('drunken sailor gait'). The lateral cerebellar hemispheres (cerebrocerebellum), which coordinate fine appendicular upper extremity movements, are spared, preserving finger-to-nose testing.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Alcoholic cerebellar degeneration selectively affects the anterior superior vermis, causing lower extremity/gait ataxia with spared upper extremity coordination.",
        "image": None
    })

    # Q17
    qs.append({
        "id": "exam3_in_house_like_g_q17",
        "q_num": "17",
        "stem": "A 62-year-old man develops acute right-sided clumsiness following a posterior fossa stroke. Examination shows dysmetria on right finger-to-nose testing, dysdiadochokinesia on right rapid alternating movements, and a prominent right action tremor that worsens as his finger approaches the target. Gait is relatively preserved. Which of the following structures is the primary site of pathology?",
        "category": "Cerebellum",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Midline cerebellar vermis and fastigial nucleus"},
            {"letter": "B", "is_correct": True, "text": "Right lateral cerebellar hemisphere neocortex"},
            {"letter": "C", "is_correct": False, "text": "Left lateral cerebellar hemisphere neocortex"},
            {"letter": "D", "is_correct": False, "text": "Contralateral red nucleus in the rostral midbrain"},
            {"letter": "E", "is_correct": False, "text": "Cervical spinal cord dorsal column pathways"}
        ],
        "correct_idx": 1,
        "explanation": "Lesions of the lateral cerebellar hemisphere (cerebrocerebellum) affect the planning and execution of fine appendicular movements, producing ipsilateral limb ataxia, dysmetria (past-pointing), dysdiadochokinesia (impaired rapid alternating movements), and intention tremor. Because cerebellar pathways cross twice before reaching the periphery (decussation of the superior cerebellar peduncle, then pyramidal decussation), cerebellar hemisphere deficits are always IPSILATERAL to the lesion.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Lateral cerebellar hemisphere lesions cause IPSILATERAL appendicular ataxia, intention tremor, and dysmetria ('cerebellar signs are ipsilateral').",
        "image": None
    })

    # Q18
    qs.append({
        "id": "exam3_in_house_like_g_q18",
        "q_num": "18",
        "stem": "A neuroscientist is studying cerebellar cortical microcircuitry. Which of the following neuronal populations provides the sole excitatory output from the cerebellar cortex to the deep cerebellar nuclei?",
        "category": "Cerebellum",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Inhibitory Purkinje cells utilizing GABA"},
            {"letter": "B", "is_correct": False, "text": "Inhibitory Golgi cells in the granular layer"},
            {"letter": "C", "is_correct": True, "text": "No cells; Purkinje output is purely inhibitory"},
            {"letter": "D", "is_correct": False, "text": "Excitatory granule cells utilizing glutamate"},
            {"letter": "E", "is_correct": False, "text": "Inhibitory stellate cells in molecular layer"}
        ],
        "correct_idx": 2,
        "explanation": "A fundamental rule of cerebellar neuroanatomy: Purkinje cells are the SOLE output neurons of the cerebellar cortex, and their projections to the deep cerebellar nuclei are PURELY INHIBITORY, utilizing the neurotransmitter GABA. The deep cerebellar nuclei, in turn, provide the excitatory (glutamatergic) output of the cerebellum to the thalamus, red nucleus, and vestibular nuclei. Granule cells are excitatory to Purkinje cells via parallel fibers, but they do NOT leave the cortex.",
        "high_yield_pearl": "High-Yield Clinical Pearl: All output from the cerebellar cortex is mediated by Purkinje cells, which are exclusively INHIBITORY (GABAergic) to the deep cerebellar nuclei.",
        "image": None
    })

    # Q19
    qs.append({
        "id": "exam3_in_house_like_g_q19",
        "q_num": "19",
        "stem": "A 6-year-old boy presents with progressive morning vomiting, headaches, and a profound wide-based gait ataxia with truncal instability. When sitting unsupported on the examination table, he exhibits prominent oscillations of his trunk (titubation). Neuroimaging reveals a midline medulloblastoma compressing the roof of the fourth ventricle. Which of the following deep cerebellar nuclei is primarily involved in coordinating this balance and axial posture?",
        "category": "Cerebellum",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Dentate nucleus in lateral white matter"},
            {"letter": "B", "is_correct": False, "text": "Emboliform nucleus in intermediate zone"},
            {"letter": "C", "is_correct": True, "text": "Fastigial nucleus in midline cerebellum"},
            {"letter": "D", "is_correct": False, "text": "Globose nucleus in intermediate zone"},
            {"letter": "E", "is_correct": False, "text": "Red nucleus in the rostral midbrain"}
        ],
        "correct_idx": 2,
        "explanation": "The deep cerebellar nuclei from medial to lateral can be remembered by the mnemonic 'Don't Eat Greasy Foods' (Dentate, Emboliform, Globose, Fastigial). The most medial nucleus is the fastigial nucleus, which receives projections from the vermis and vestibulocerebellum/flocculonodular lobe and projects to vestibular nuclei and reticular formation to regulate axial balance, truncal stability, and eye movements.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Deep cerebellar nuclei: Fastigial (medial, vermis/vestibular, axial balance) -> Interposed [Globose + Emboliform] (intermediate, distal limb tone) -> Dentate (lateral, motor planning).",
        "image": None
    })

    # Q20
    qs.append({
        "id": "exam3_in_house_like_g_q20",
        "q_num": "20",
        "stem": "Which of the following afferent fiber systems entering the cerebellum originates exclusively in the contralateral inferior olivary nucleus, traverses the inferior cerebellar peduncle, and forms powerful, direct excitatory synapses onto the dendritic tree of a single Purkinje cell?",
        "category": "Cerebellum",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Mossy fibers originating in the pontine nuclei"},
            {"letter": "B", "is_correct": False, "text": "Parallel fibers derived from cerebellar granule cells"},
            {"letter": "C", "is_correct": True, "text": "Climbing fibers from inferior olivary nucleus"},
            {"letter": "D", "is_correct": False, "text": "Spinocerebellar tract fibers from spinal cord"},
            {"letter": "E", "is_correct": False, "text": "Vestibulocerebellar fibers from Scarpa ganglion"}
        ],
        "correct_idx": 2,
        "explanation": "Cerebellar afferents consist of climbing fibers and mossy fibers. Climbing fibers arise EXCLUSIVELY from the contralateral inferior olivary nucleus, ascend through the inferior cerebellar peduncle, and wrap directly around the dendritic tree of Purkinje cells. A single climbing fiber forms multiple synapses with one Purkinje cell, eliciting massive, prolonged 'complex spikes' that trigger motor learning and long-term depression (LTD). Mossy fibers synapse on granule cells.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Climbing fibers arise solely from the contralateral inferior olive, directly synapse on Purkinje cells, and generate complex spikes crucial for motor learning.",
        "image": None
    })

    # Q21
    qs.append({
        "id": "exam3_in_house_like_g_q21",
        "q_num": "21",
        "stem": "A 16-year-old boy presents with progressive unsteadiness, frequent stumbling, and slurred speech. Examination reveals pes cavus, hammer toes, severe loss of vibration and position sense in the lower extremities, absent ankle and patellar reflexes, bilateral extensor plantar responses, and dysmetria. An electrocardiogram shows T-wave inversions and concentric left ventricular hypertrophy. Genetic testing confirms an abnormal trinucleotide repeat expansion. Which of the following repeat sequences and genes is responsible?",
        "category": "Cerebellum",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "CAG repeat expansion in huntingtin gene"},
            {"letter": "B", "is_correct": False, "text": "CTG repeat expansion in myotonin kinase gene"},
            {"letter": "C", "is_correct": True, "text": "GAA repeat expansion in frataxin gene"},
            {"letter": "D", "is_correct": False, "text": "CGG repeat expansion in FMR1 promotor gene"},
            {"letter": "E", "is_correct": False, "text": "CCTG repeat expansion in zinc finger gene"}
        ],
        "correct_idx": 2,
        "explanation": "Friedreich ataxia is an autosomal recessive neurodegenerative disease caused by an unstable GAA trinucleotide repeat expansion in intron 1 of the FXN gene (chromosome 9q13) encoding frataxin, a mitochondrial iron-binding protein. Frataxin deficiency leads to mitochondrial iron overload, defective iron-sulfur cluster assembly, and oxidative cellular damage. Key pathology: dorsal columns (vibration/proprioception loss), spinocerebellar tracts (ataxia), corticospinal tracts (spastic weakness), and dorsal root ganglia (hyporeflexia). Hypertrophic cardiomyopathy is the leading cause of death.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Friedreich ataxia is an autosomal recessive GAA repeat disorder on chromosome 9 (FXN gene) presenting with ataxia, loss of DTRs, vibration loss, pes cavus, and hypertrophic cardiomyopathy.",
        "image": None
    })

    # Q22
    qs.append({
        "id": "exam3_in_house_like_g_q22",
        "q_num": "22",
        "stem": "A 45-year-old man presents with progressive gait instability. Neurological examination reveals a broad-based gait. When asked to stand with feet together and eyes open, he maintains balance steadily. However, immediately upon closing his eyes, he begins to sway markedly and loses balance, requiring examiner support. Which of the following pathways is damaged in this patient?",
        "category": "Cerebellum",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Midline cerebellar vermis spinocerebellar neocortex"},
            {"letter": "B", "is_correct": True, "text": "Ascending dorsal columns in the spinal cord"},
            {"letter": "C", "is_correct": False, "text": "Descending lateral corticospinal motor tracts"},
            {"letter": "D", "is_correct": False, "text": "Vestibulocerebellar flocculonodular pathways"},
            {"letter": "E", "is_correct": False, "text": "Dentatorubrothalamic superior peduncle fibers"}
        ],
        "correct_idx": 1,
        "explanation": "A positive Romberg sign (loss of balance upon eye closure) indicates SENSORY ataxia, resulting from disruption of the conscious proprioceptive pathway in the ascending dorsal columns (fasciculus gracilis/cuneatus) or large-fiber peripheral sensory neuropathy. Equilibrium requires 2 of 3 sensory inputs: vision, proprioception, and vestibular function. With impaired proprioception, the patient compensates using vision; closing the eyes eliminates visual compensation. In contrast, cerebellar ataxia causes unsteadiness with eyes OPEN and closed.",
        "high_yield_pearl": "High-Yield Clinical Pearl: A positive Romberg sign indicates sensory ataxia due to dorsal column proprioceptive loss. Cerebellar ataxia causes instability with eyes open AND closed (negative Romberg).",
        "image": None
    })

    # Q23
    qs.append({
        "id": "exam3_in_house_like_g_q23",
        "q_num": "23",
        "stem": "A 68-year-old woman presents with persistent, slow, irregular, slurred speech where words are broken into individual syllables with inappropriate pauses and variable explosive loudness. Neurological examination confirms scanning dysarthria and appendicular ataxia of the left upper extremity. Which of the following mechanisms best explains this speech disturbance?",
        "category": "Cerebellum",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Impaired motor planning of speech in Broca area"},
            {"letter": "B", "is_correct": False, "text": "Language comprehension deficit in Wernicke area"},
            {"letter": "C", "is_correct": True, "text": "Asynergy and incoordination of speech musculature"},
            {"letter": "D", "is_correct": False, "text": "Flaccid paralysis of the hypoglossal nerve fibers"},
            {"letter": "E", "is_correct": False, "text": "Mechanical disruption of the laryngeal vocal cords"}
        ],
        "correct_idx": 2,
        "explanation": "Scanning (ataxic) dysarthria is a characteristic manifestation of cerebellar dysfunction (particularly lesions involving the lateral hemispheres and paravermal regions). It is not an aphasia (which is a cognitive language disorder), but rather a neuromuscular incoordination (asynergy and dysmetria) of the respiratory, laryngeal, and articulatory muscles, resulting in slurred speech broken into explosive, irregular syllables.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Scanning speech in cerebellar disease is an ataxic motor coordination defect of articulatory and phonatory muscles, distinct from cortical aphasia.",
        "image": None
    })

    # Q24
    qs.append({
        "id": "exam3_in_house_like_g_q24",
        "q_num": "24",
        "stem": "Which of the following cerebellar peduncles carries the primary outflow from the dentate nucleus to the contralateral ventral lateral (VL) nucleus of the thalamus and contralateral red nucleus, and undergoes decussation in the caudal midbrain?",
        "category": "Cerebellum",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Inferior cerebellar peduncle tract"},
            {"letter": "B", "is_correct": False, "text": "Middle cerebellar peduncle tract"},
            {"letter": "C", "is_correct": True, "text": "Superior cerebellar peduncle tract"},
            {"letter": "D", "is_correct": False, "text": "Stria medullaris of the thalamus"},
            {"letter": "E", "is_correct": False, "text": "Medial longitudinal fasciculus tract"}
        ],
        "correct_idx": 2,
        "explanation": "The superior cerebellar peduncle (brachium conjunctivum) is the main EFFERENT pathway of the cerebellum. It carries axons originating in the deep cerebellar nuclei (predominantly the dentate nucleus) that ascend, decussate in the caudal midbrain tegmentum (decussation of the superior cerebellar peduncle), and project to the contralateral red nucleus (rubrospinal tract) and the contralateral ventral lateral (VL) nucleus of the thalamus (dentatorubrothalamic tract).",
        "high_yield_pearl": "High-Yield Clinical Pearl: The superior cerebellar peduncle is the primary cerebellar efferent pathway, carrying dentatorubrothalamic fibers that decussate in the midbrain.",
        "image": None
    })

    # Q25
    qs.append({
        "id": "exam3_in_house_like_g_q25",
        "q_num": "25",
        "stem": "A 28-year-old woman presents with subacute progressive cerebellar ataxia, coarse downbeat nystagmus, and dysarthria. Brain MRI shows profound cerebellar cortical atrophy without parenchymal mass lesions. Comprehensive workup reveals an occult ovarian teratoma and high-titer serum autoantibodies targeting Purkinje cells. Which of the following paraneoplastic antibodies is most characteristically associated with this presentation?",
        "category": "Cerebellum",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Anti-Hu autoantibodies against neuronal nuclei"},
            {"letter": "B", "is_correct": True, "text": "Anti-Yo autoantibodies against Purkinje cells"},
            {"letter": "C", "is_correct": False, "text": "Anti-aquaporin-4 autoantibodies on astrocytes"},
            {"letter": "D", "is_correct": False, "text": "Anti-voltage gated calcium channel autoantibodies"},
            {"letter": "E", "is_correct": False, "text": "Anti-acetylcholine receptor autoantibodies"}
        ],
        "correct_idx": 1,
        "explanation": "Paraneoplastic cerebellar degeneration (PCD) is an immune-mediated syndrome characterized by subacute cerebellar ataxia, dysarthria, and nystagmus due to extensive autoimmune destruction of cerebellar Purkinje cells. Anti-Yo (anti-Purkinje cell cytoplasmic antibody type 1 / PCA-1) is the classic paraneoplastic antibody in women with breast or gynecologic (ovarian/uterine) malignancies.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Paraneoplastic cerebellar degeneration in women with ovarian or breast cancer is linked to Anti-Yo antibodies targeting cerebellar Purkinje cells.",
        "image": None
    })

    # Q26
    qs.append({
        "id": "exam3_in_house_like_g_q26",
        "q_num": "26",
        "stem": "A 33-year-old woman presents with occipital headaches that worsen noticeably during coughing, sneezing, and straining. Neurological examination reveals bilateral limb ataxia and horizontal nystagmus. Sagittal T1 MRI of the brain demonstrates herniation of the cerebellar tonsils 7 mm below the horizontal plane of the foramen magnum into the upper cervical spinal canal. Which of the following is the most likely diagnosis?",
        "category": "Cerebellum",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Dandy-Walker congenital cystic malformation"},
            {"letter": "B", "is_correct": True, "text": "Chiari type I cerebellar tonsillar malformation"},
            {"letter": "C", "is_correct": False, "text": "Chiari type II congenital myelomeningocele"},
            {"letter": "D", "is_correct": False, "text": "Joubert syndrome with molar tooth brainstem"},
            {"letter": "E", "is_correct": False, "text": "Normal pressure chronic adult hydrocephalus"}
        ],
        "correct_idx": 1,
        "explanation": "Chiari type I malformation is characterized by downward herniation of the cerebellar tonsils (>5 mm) through the foramen magnum into the upper cervical spinal canal. Unlike Chiari II (which involves tonsillar and vermian herniation and is associated with lumbar myelomeningocele in infants), Chiari I typically presents in adulthood with occipital headaches exacerbated by Valsalva maneuvers (coughing, straining), cerebellar ataxia, and is frequently associated with syringomyelia.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Chiari I malformation involves downward tonsillar herniation (>5 mm) through the foramen magnum, presenting in young adults with Valsalva-induced occipital headaches and syringomyelia.",
        "image": None
    })

    # Q27
    qs.append({
        "id": "exam3_in_house_like_g_q27",
        "q_num": "27",
        "stem": "A 71-year-old man with hypertension experiences an acute ischemic stroke. Examination reveals that the patient has left-sided limb ataxia and dysmetria, along with severe left-sided spastic hemiparesis. Brain MRI demonstrates an acute lacunar infarction within the left posterior limb of the internal capsule. Which of the following terms best describes this clinical lacunar syndrome?",
        "category": "Cerebellum",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Pure motor hemiparesis lacunar syndrome"},
            {"letter": "B", "is_correct": False, "text": "Pure sensory thalamic stroke syndrome"},
            {"letter": "C", "is_correct": True, "text": "Ataxic hemiparesis lacunar stroke syndrome"},
            {"letter": "D", "is_correct": False, "text": "Clumsy hand-dysarthria stroke syndrome"},
            {"letter": "E", "is_correct": False, "text": "Wallenberg lateral medullary stroke syndrome"}
        ],
        "correct_idx": 2,
        "explanation": "Ataxic hemiparesis is one of the classic lacunar stroke syndromes caused by microatheroma or lipohyalinosis of penetrating arterioles. It features a combination of cerebellar ataxia and motor weakness on the SAME side of the body. Classic anatomical localizations include the posterior limb of the internal capsule, the basis pontis (disrupting corticospinal and frontopontine fibers), or the corona radiata.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Ataxic hemiparesis is a classic lacunar syndrome combining ipsilateral weakness and ataxia, localized to the posterior limb of internal capsule or basis pontis.",
        "image": None
    })

    # =========================================================================
    # UNIT 3: TUMORS & NEUROCUTANEOUS SYNDROMES (21 Questions: Q28 - Q48, 14%)
    # =========================================================================

    # Q28
    qs.append({
        "id": "exam3_in_house_like_g_q28",
        "q_num": "28",
        "stem": "A 58-year-old man presents with progressive headaches, cognitive slowing, and a new-onset generalized tonic-clonic seizure. Contrast-enhanced brain MRI reveals a large, heterogeneously ring-enhancing mass in the deep frontal white matter that crosses the corpus callosum into the contralateral hemisphere with marked central necrosis and surrounding vasogenic edema. Histopathological biopsy demonstrates pseudopalisading necrosis and florid microvascular endothelial proliferation. Which of the following is the most likely diagnosis?",
        "category": "Tumors",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Cerebellar pilocytic low-grade astrocytoma"},
            {"letter": "B", "is_correct": True, "text": "Glioblastoma multiforme WHO grade IV tumor"},
            {"letter": "C", "is_correct": False, "text": "Oligodendroglioma with 1p/19q codeletion"},
            {"letter": "D", "is_correct": False, "text": "Primary central nervous system lymphoma"},
            {"letter": "E", "is_correct": False, "text": "Dural-based extra-axial fibrous meningioma"}
        ],
        "correct_idx": 1,
        "explanation": "Glioblastoma (WHO Grade IV astrocytoma) is the most common and aggressive primary malignant brain tumor in adults. Classic imaging features include a solitary, heterogeneously ring-enhancing supratentorial mass with central necrosis that frequently crosses the corpus callosum ('butterfly glioma'). Diagnostic histopathologic hallmarks are pseudopalisading pleomorphic tumor cells lining areas of central necrosis and microvascular (glomeruloid) proliferation. Cells are strongly GFAP-positive.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Glioblastoma is a high-grade supratentorial malignancy characterized by butterfly crossing of the corpus callosum, pseudopalisading necrosis, and microvascular proliferation.",
        "image": None
    })

    # Q29
    qs.append({
        "id": "exam3_in_house_like_g_q29",
        "q_num": "29",
        "stem": "An 8-year-old girl presents with progressive headaches, morning vomiting, and gait unsteadiness over 2 months. Brain MRI reveals a well-circumscribed cystic mass in the left cerebellar hemisphere with an intensely contrast-enhancing mural nodule. The patient undergoes gross total surgical resection. Histopathology shows a biphasic tumor with compact fibrillary zones containing corkscrew-shaped eosinophilic Rosenthal fibers and eosinophilic granular bodies. Which of the following is the most likely diagnosis and WHO grade?",
        "category": "Tumors",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Medulloblastoma; WHO grade IV malignancy"},
            {"letter": "B", "is_correct": True, "text": "Pilocytic astrocytoma; WHO grade I neoplasm"},
            {"letter": "C", "is_correct": False, "text": "Ependymoma; WHO grade II ventricular tumor"},
            {"letter": "D", "is_correct": False, "text": "Glioblastoma; WHO grade IV malignant tumor"},
            {"letter": "E", "is_correct": False, "text": "Atypical teratoid rhabdoid tumor grade IV"}
        ],
        "correct_idx": 1,
        "explanation": "Pilocytic astrocytoma (WHO Grade I) is the most common primary brain tumor in children. Typically located in the cerebellar hemispheres, its classic neuroimaging appearance is a cystic mass with an enhancing mural nodule. Histopathology confirms a biphasic pattern composed of piloid (hair-like) astrocytes, Rosenthal fibers (eosinophilic corkscrew intracytoplasmic inclusions containing alphaB-crystallin and ubiquitin), and eosinophilic granular bodies. Prognosis following surgical resection is excellent (>90% 10-year survival).",
        "high_yield_pearl": "High-Yield Clinical Pearl: Pilocytic astrocytoma is a benign (Grade I) pediatric cerebellar tumor featuring a cystic cavity with an enhancing mural nodule and Rosenthal fibers.",
        "image": None
    })

    # Q30
    qs.append({
        "id": "exam3_in_house_like_g_q30",
        "q_num": "30",
        "stem": "A 5-year-old boy presents with ataxia, vomiting, and lethargy. Brain MRI demonstrates a solid, contrast-enhancing mass in the midline cerebellar vermis compressing the fourth ventricle and causing obstructive hydrocephalus. Staging neuroaxis spine MRI shows linear nodular leptomeningeal enhancement along the cauda equina ('drop metastases'). Histopathological biopsy demonstrates sheets of small, hyperchromatic blue cells with scant cytoplasm forming Homer Wright rosettes. Which of the following is the most likely tumor?",
        "category": "Tumors",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Pilocytic astrocytoma with Rosenthal fibers"},
            {"letter": "B", "is_correct": True, "text": "Medulloblastoma small round blue cell tumor"},
            {"letter": "C", "is_correct": False, "text": "Ependymoma with true ependymal rosettes"},
            {"letter": "D", "is_correct": False, "text": "Craniopharyngioma with calcified wet keratin"},
            {"letter": "E", "is_correct": False, "text": "Capillary hemangioblastoma stromal tumor"}
        ],
        "correct_idx": 1,
        "explanation": "Medulloblastoma (WHO Grade IV) is the most common malignant pediatric brain tumor. It arises in the posterior fossa from primitive neuroectodermal cells in the cerebellar vermis (roof of fourth ventricle). Histology reveals sheets of densely packed small round blue cells with high nuclear-to-cytoplasmic ratios, frequent mitoses, and Homer Wright rosettes (tumor cells surrounding a central neuropil core). It frequently disseminates through CSF pathways ('drop metastases' to cauda equina). It is radiosensitive.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Medulloblastoma is a highly malignant cerebellar vermis tumor in children featuring small round blue cells, Homer Wright rosettes, and CSF drop metastases.",
        "image": None
    })

    # Q31
    qs.append({
        "id": "exam3_in_house_like_g_q31",
        "q_num": "31",
        "stem": "A 7-year-old girl presents with progressive headaches and projectile vomiting. MRI reveals a mass arising from the floor of the fourth ventricle that extends out through the foramina of Luschka and Magendie ('plastic' molding appearance). Histopathologic examination shows tumor cells surrounding blood vessels with clear intervening fibrillary zones, forming perivascular pseudorosettes and true ependymal rosettes. Electron microscopy reveals blepharoplasts (ciliary basal bodies). Which of the following is the most likely diagnosis?",
        "category": "Tumors",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Pilocytic astrocytoma of the cerebellum"},
            {"letter": "B", "is_correct": False, "text": "Medulloblastoma of the cerebellar vermis"},
            {"letter": "C", "is_correct": True, "text": "Ependymoma of the fourth ventricular floor"},
            {"letter": "D", "is_correct": False, "text": "Choroid plexus benign papillary papilloma"},
            {"letter": "E", "is_correct": False, "text": "Subependymal giant cell astrocytoma tumor"}
        ],
        "correct_idx": 2,
        "explanation": "Ependymoma arises from ependymal cells lining the ventricular system, most commonly the fourth ventricle in children. Ependymomas demonstrate a distinctive tendency to 'mold' and squeeze through ventricular exit foramina (foramina of Luschka and Magendie) into the subarachnoid space. Histological hallmarks are perivascular pseudorosettes (tumor cells arrayed around central blood vessels) and true ependymal rosettes. Blepharoplasts (basal bodies of cilia) are seen on electron microscopy.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Ependymoma arises in the fourth ventricle floor, displays plastic molding into ventricular foramina, and features perivascular pseudorosettes with blepharoplasts.",
        "image": None
    })

    # Q32
    qs.append({
        "id": "exam3_in_house_like_g_q32",
        "q_num": "32",
        "stem": "A 40-year-old man presents with new-onset generalized seizures. Head CT reveals a calcified, well-circumscribed mass in the frontal lobe cortex and subcortical white matter. Biopsy demonstrates uniform, sheets of cells with round, central nuclei surrounded by clear cytoplasmic halos ('fried-egg' appearance) embedded in a dense network of branching, anastomosing capillaries ('chicken-wire' pattern). Molecular genetic testing confirms combined 1p and 19q chromosomal arm codeletions. Which of the following is the most likely tumor?",
        "category": "Tumors",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Glioblastoma multiforme WHO grade IV tumor"},
            {"letter": "B", "is_correct": False, "text": "Pilocytic astrocytoma with Rosenthal fibers"},
            {"letter": "C", "is_correct": True, "text": "Oligodendroglioma with 1p/19q codeletion"},
            {"letter": "D", "is_correct": False, "text": "Primary central nervous system lymphoma"},
            {"letter": "E", "is_correct": False, "text": "Dural-based extra-axial fibrous meningioma"}
        ],
        "correct_idx": 2,
        "explanation": "Oligodendroglioma (WHO Grade II or III) is a slow-growing adult glial neoplasm typically located in the frontal lobes that frequently calcifies (visible on CT) and presents with seizures. Classic histology shows 'fried-egg' cells (round regular nuclei with clear halos caused by delayed formalin fixation) and a delicate 'chicken-wire' capillary network. The diagnostic molecular hallmark is complete codeletion of chromosomal arms 1p and 19q (1p/19q codeletion), which predicts superior response to alkylating chemotherapy (PCV / temozolomide).",
        "high_yield_pearl": "High-Yield Clinical Pearl: Oligodendroglioma features frontal lobe calcification, 'fried-egg' cells, 'chicken-wire' capillaries, and 1p/19q codeletion conferring chemosensitivity.",
        "image": None
    })

    # Q33
    qs.append({
        "id": "exam3_in_house_like_g_q33",
        "q_num": "33",
        "stem": "A 52-year-old woman presents with progressive headaches and localized focal seizures affecting her left arm. Brain MRI reveals a well-circumscribed, extra-axial, homogeneously contrast-enhancing mass abutting the right parasagittal dura with an adjacent hyperostosis of the overlying calvarium and a distinct 'dural tail'. Biopsy demonstrates spindle cells arranged in concentric whorled patterns and numerous calcified laminated psammoma bodies. Which of the following is the most likely diagnosis?",
        "category": "Tumors",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Supratentorial high-grade glioblastoma"},
            {"letter": "B", "is_correct": True, "text": "Dural-based benign transitional meningioma"},
            {"letter": "C", "is_correct": False, "text": "Cerebellopontine vestibular schwannoma"},
            {"letter": "D", "is_correct": False, "text": "Metastatic papillary adenocarcinoma"},
            {"letter": "E", "is_correct": False, "text": "Subependymal giant cell astrocytoma"}
        ],
        "correct_idx": 1,
        "explanation": "Meningioma is the most common primary non-glial brain tumor in adults, occurring most often in middle-aged women. Arising from arachnoid cap cells, it is an extra-axial, dural-based mass that demonstrates intense homogeneous enhancement with a pathognomonic 'dural tail' and may cause hyperostosis of adjacent bone. Histology reveals whorled fascicles of meningothelial cells and concentric laminated calcifications called psammoma bodies. They frequently express estrogen and progesterone receptors.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Meningioma is a benign, extra-axial, dural-based tumor with a 'dural tail', whorled cellular pattern, and calcified psammoma bodies on histology.",
        "image": None
    })

    # Q34
    qs.append({
        "id": "exam3_in_house_like_g_q34",
        "q_num": "34",
        "stem": "A 49-year-old woman presents with progressive unilateral right-sided hearing loss, continuous high-pitched tinnitus, and intermittent unsteadiness over 18 months. Physical examination confirms right-sided sensorineural hearing loss and diminished corneal sensation on the right. Contrast MRI demonstrates an intensely enhancing mass centered at the right cerebellopontine angle with widening of the internal acoustic meatus. Histopathology reveals alternating cellular Antoni A areas with Verocay bodies and hypocellular Antoni B areas, with strong S100 positivity. Which of the following is the most likely diagnosis?",
        "category": "Tumors",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Cerebellar capillary hemangioblastoma"},
            {"letter": "B", "is_correct": True, "text": "Vestibular schwannoma acoustic neuroma"},
            {"letter": "C", "is_correct": False, "text": "Posterior fossa transitional meningioma"},
            {"letter": "D", "is_correct": False, "text": "Epidermoid cyst of the cerebellopontine angle"},
            {"letter": "E", "is_correct": False, "text": "Metastatic melanoma to the petrous temporal bone"}
        ],
        "correct_idx": 1,
        "explanation": "Vestibular schwannoma (acoustic neuroma) arises from Schwann cells of the vestibular branch of cranial nerve VIII at the cerebellopontine angle (CPA). Presentation involves progressive unilateral sensorineural hearing loss, tinnitus, and vertigo, followed by facial numbness due to compression of adjacent CN V. Histopathology shows a biphasic pattern: dense Antoni A areas containing palisading nuclei around fibrillary processes (Verocay bodies) and loose myxoid Antoni B areas. Cells are strongly S100 positive (neural crest origin).",
        "high_yield_pearl": "High-Yield Clinical Pearl: Vestibular schwannoma arises at the CPA from CN VIII, causing unilateral hearing loss and tinnitus, featuring biphasic Antoni A/B histology with S100 positivity.",
        "image": None
    })

    # Q35
    qs.append({
        "id": "exam3_in_house_like_g_q35",
        "q_num": "35",
        "stem": "A 10-year-old boy presents with growth retardation, polyuria, and progressive vision impairment. Visual field testing reveals bitemporal hemianopia. Skull radiographs and CT show a calcified, suprasellar cystic mass with peripheral ring calcification abutting the optic chiasm. Fluid aspirated from the mass resembles dark, turbid 'motor oil' containing glistening cholesterol crystals. Histopathology shows nests of palisading squamous epithelium with wet keratin. From which of the following embryological structures is this tumor derived?",
        "category": "Tumors",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Neural crest cells of the branchial arches"},
            {"letter": "B", "is_correct": True, "text": "Rathke pouch surface ectoderm remnants"},
            {"letter": "C", "is_correct": False, "text": "Neuroectoderm of the optic cup and chiasm"},
            {"letter": "D", "is_correct": False, "text": "Floor of the third ventricle infundibulum"},
            {"letter": "E", "is_correct": False, "text": "Mesodermal dural lining of sella turcica"}
        ],
        "correct_idx": 1,
        "explanation": "Craniopharyngioma is a benign suprasellar pediatric neoplasm derived from remnants of Rathke pouch (an upward invagination of oral surface ectoderm that normally forms the anterior pituitary / adenohypophysis). Compression of the optic chiasm causes bitemporal hemianopia; compression of the pituitary stalk causes endocrinopathies. Characteristic gross pathology is turbid, brown-yellow 'machine/motor oil' cyst fluid rich in cholesterol crystals. Histology displays adamantinomatous squamous epithelium with lamellar 'wet keratin'. Calcifications on CT are classic.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Craniopharyngioma arises from Rathke pouch ectodermal remnants, features 'motor oil' fluid with cholesterol crystals, and causes bitemporal hemianopia in children.",
        "image": None
    })

    # Q36
    qs.append({
        "id": "exam3_in_house_like_g_q36",
        "q_num": "36",
        "stem": "A 36-year-old man with AIDS (CD4 count 45/uL) presents with confusion, memory loss, and a right-sided hemiparesis. Brain MRI demonstrates a solitary, 3.5-cm periventricular contrast-enhancing mass in the left deep parietal lobe with subependymal extension. PCR of the cerebrospinal fluid reveals positive Epstein-Barr virus (EBV) DNA. Biopsy demonstrates a high-grade neoplasm composed of large atypical lymphocytes expressing CD20. Which of the following is the most likely diagnosis?",
        "category": "Tumors",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Cerebral toxoplasmosis parasitic abscess"},
            {"letter": "B", "is_correct": True, "text": "Primary central nervous system lymphoma"},
            {"letter": "C", "is_correct": False, "text": "Progressive multifocal leukoencephalopathy"},
            {"letter": "D", "is_correct": False, "text": "Glioblastoma multiforme malignant astrocytoma"},
            {"letter": "E", "is_correct": False, "text": "Cryptococcal gelatigenous pseudocyst lesion"}
        ],
        "correct_idx": 1,
        "explanation": "Primary central nervous system lymphoma (PCNSL) is a high-grade non-Hodgkin B-cell lymphoma (diffuse large B-cell lymphoma, CD20+) strongly linked to Epstein-Barr virus (EBV) in immunocompromised patients (AIDS, organ transplant). In contrast to toxoplasmosis (which usually produces multiple ring-enhancing lesions in the basal ganglia), PCNSL is characteristically a solitary, deeply situated periventricular lesion with subependymal spread and positive CSF EBV PCR.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Primary CNS lymphoma in AIDS patients is a periventricular B-cell (CD20+) neoplasm driven by EBV, presenting with solitary or multiple enhancing lesions.",
        "image": None
    })

    # Q37
    qs.append({
        "id": "exam3_in_house_like_g_q37",
        "q_num": "37",
        "stem": "A 31-year-old man with von Hippel-Lindau disease presents with headache and unsteadiness. Laboratory evaluation reveals a hematocrit of 58% (normal 40-52%) with elevated serum erythropoietin levels. Contrast-enhanced brain MRI demonstrates a highly vascular, intensely enhancing cystic lesion with a hypervascular mural nodule in the right cerebellar hemisphere. Histopathology reveals lipid-rich, vacuolated, foamy stromal cells intertwined within an extensive, thin-walled capillary network. Which of the following is the most likely tumor?",
        "category": "Tumors",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Pilocytic astrocytoma of the cerebellum"},
            {"letter": "B", "is_correct": True, "text": "Capillary hemangioblastoma cerebellar tumor"},
            {"letter": "C", "is_correct": False, "text": "Medulloblastoma small round blue cell tumor"},
            {"letter": "D", "is_correct": False, "text": "Oligodendroglioma with 1p/19q codeletion"},
            {"letter": "E", "is_correct": False, "text": "Clear cell renal cell carcinoma metastasis"}
        ],
        "correct_idx": 1,
        "explanation": "Capillary hemangioblastoma is a benign, highly vascular posterior fossa neoplasm occurring sporadically or as part of von Hippel-Lindau (VHL) disease (deletion/mutation of VHL tumor suppressor on chromosome 3p). The tumor cells produce erythropoietin, leading to secondary polycythemia. Histology reveals large, lipid-rich, vacuolated foamy stromal cells and a dense meshwork of thin-walled capillary vessels.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Cerebellar hemangioblastoma in VHL disease produces erythropoietin causing polycythemia, featuring foamy lipid-rich stromal cells and abundant capillaries.",
        "image": None
    })

    # Q38
    qs.append({
        "id": "exam3_in_house_like_g_q38",
        "q_num": "38",
        "stem": "A 64-year-old man with a 40 pack-year smoking history presents with progressive headache, confusion, and new left-sided weakness. Contrast MRI of the brain demonstrates multiple discrete, well-circumscribed, ring-enhancing spherical lesions localized precisely at the gray-white matter junctions of both cerebral hemispheres, accompanied by extensive surrounding vasogenic edema. Which of the following is the most likely etiology of these intracranial lesions?",
        "category": "Tumors",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Primary multifocal glioblastoma multiforme"},
            {"letter": "B", "is_correct": True, "text": "Metastatic carcinoma from primary lung cancer"},
            {"letter": "C", "is_correct": False, "text": "Multiple subependymal giant cell astrocytomas"},
            {"letter": "D", "is_correct": False, "text": "Progressive multifocal leukoencephalopathy"},
            {"letter": "E", "is_correct": False, "text": "Multiple intracranial transitional meningiomas"}
        ],
        "correct_idx": 1,
        "explanation": "Metastatic brain tumors are the most common intracranial neoplasms in adults, outnumbering primary tumors by far. They classically present as multiple, well-circumscribed, round, contrast-enhancing masses at the gray-white junction (where microvasculature narrows, trapping hematogenous tumor emboli) with marked surrounding finger-like vasogenic edema. The most common primary site is lung cancer (small cell or non-small cell), followed by breast, melanoma, renal cell, and colorectal carcinoma.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Brain metastases are the most common adult brain tumors; multiple well-circumscribed lesions at the gray-white junction with severe vasogenic edema most often originate from the lung.",
        "image": None
    })

    # Q39
    qs.append({
        "id": "exam3_in_house_like_g_q39",
        "q_num": "39",
        "stem": "An 11-year-old boy is brought for evaluation of learning difficulties. Physical examination reveals eight smooth-bordered, light-brown hyperpigmented macules measuring >15 mm on his trunk, bilateral axillary freckling (Crowe sign), multiple soft subcutaneous cutaneous nodules, and multiple small, raised, pigmented hamartomas on the iris (Lisch nodules). Visual testing reveals decreased visual acuity in the right eye secondary to an optic nerve glioma. An autosomal dominant mutation in a tumor suppressor gene on chromosome 17q is confirmed. Which of the following is the normal function of the protein encoded by this gene?",
        "category": "Tumors",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Degradation of hypoxia-inducible factor 1"},
            {"letter": "B", "is_correct": True, "text": "Inactivation of active Ras GTPase signaling"},
            {"letter": "C", "is_correct": False, "text": "Inhibition of the mammalian target of rapamycin"},
            {"letter": "D", "is_correct": False, "text": "Contact-dependent suppression of Schwann cells"},
            {"letter": "E", "is_correct": False, "text": "Phosphorylation of retinoblastoma protein"}
        ],
        "correct_idx": 1,
        "explanation": "Neurofibromatosis type 1 (NF1 / von Recklinghausen disease) is caused by autosomal dominant mutations in the NF1 tumor suppressor gene on chromosome 17q11.2, which encodes neurofibromin. Neurofibromin functions as a GTPase-activating protein (GAP) that hydrolyzes active Ras-GTP into inactive Ras-GDP, negatively regulating the p21-Ras MAPK cell proliferation pathway. Loss of neurofibromin leads to constitutive Ras activation, resulting in café-au-lait macules, neurofibromas, Lisch nodules, and optic pathway gliomas.",
        "high_yield_pearl": "High-Yield Clinical Pearl: NF1 encodes neurofibromin on chromosome 17, which functions as a Ras-GAP; loss of function causes constitutive Ras activation and multisystem neural crest tumors.",
        "image": None
    })

    # Q40
    qs.append({
        "id": "exam3_in_house_like_g_q40",
        "q_num": "40",
        "stem": "A 23-year-old man presents with progressive bilateral hearing loss and tinnitus. Contrast-enhanced MRI reveals bilateral enhancing masses in the cerebellopontine angles causing internal acoustic canal widening, consistent with bilateral vestibular schwannomas. Additional neuroimaging reveals two separate thoracic spinal dural-based meningiomas. Which of the following genes and chromosomal loci is mutated in this condition?",
        "category": "Tumors",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "NF1 tumor suppressor gene on chromosome 17q"},
            {"letter": "B", "is_correct": True, "text": "NF2 tumor suppressor gene on chromosome 22q"},
            {"letter": "C", "is_correct": False, "text": "TSC1 tumor suppressor gene on chromosome 9q"},
            {"letter": "D", "is_correct": False, "text": "VHL tumor suppressor gene on chromosome 3p"},
            {"letter": "E", "is_correct": False, "text": "GNAQ guanine nucleotide gene on chromosome 9q"}
        ],
        "correct_idx": 1,
        "explanation": "Neurofibromatosis type 2 (NF2) is an autosomal dominant syndrome caused by mutations in the NF2 tumor suppressor gene on chromosome 22q12.2, which encodes merlin (schwannomin), a cytoskeletal protein that mediates contact inhibition. Bilateral vestibular schwannomas are virtually pathognomonic. Patients are also predisposed to multiple meningiomas, spinal ependymomas, and juvenile posterior subcapsular cataracts (remember mnemonic: 'NF2 affects chromosome 22, causes 2 acoustic neuromas, and causes 2 major tumor types: Schwannomas and Meningiomas').",
        "high_yield_pearl": "High-Yield Clinical Pearl: NF2 involves merlin on chromosome 22q; bilateral vestibular schwannomas and multiple meningiomas are the hallmark.",
        "image": None
    })

    # Q41
    qs.append({
        "id": "exam3_in_house_like_g_q41",
        "q_num": "41",
        "stem": "A 16-year-old boy presents with longstanding epilepsy and cognitive impairment. Physical examination reveals hypopigmented ash-leaf macules on his trunk, a leathery, pebbly plaque on his lumbosacral region (shagreen patch), and multiple red-brown angiofibromas over his malar face. Brain MRI demonstrates multiple calcified nodules protruding into the lateral ventricles resembling 'candle gutterings'. A biopsy of an enlarging periventricular mass near the foramen of Monro confirms a subependymal giant cell astrocytoma (SEGA). Which of the following intracellular signaling pathways is constitutively hyperactivated in this disorder?",
        "category": "Tumors",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Wnt-beta-catenin nuclear transcription signaling"},
            {"letter": "B", "is_correct": False, "text": "Constitutive Ras-mitogen activated protein kinase"},
            {"letter": "C", "is_correct": True, "text": "Mammalian target of rapamycin kinase pathway"},
            {"letter": "D", "is_correct": False, "text": "Hypoxia-inducible factor alpha transcription"},
            {"letter": "E", "is_correct": False, "text": "Cyclin-dependent kinase inhibitor 2A pathway"}
        ],
        "correct_idx": 2,
        "explanation": "Tuberous sclerosis complex (TSC) is caused by autosomal dominant mutations in either TSC1 (hamartin, chromosome 9q34) or TSC2 (tuberin, chromosome 16p13). Hamartin and tuberin normally form a heterodimer complex that acts as a GTPase-activating protein for Rheb, thereby INHIBITING the mammalian target of rapamycin (mTOR) signaling cascade. Inactivation of TSC1 or TSC2 leads to constitutive mTOR hyperactivation, driving unregulated cell growth and hamartomas (cortical tubers, subependymal nodules, SEGA, cardiac rhabdomyomas, renal angiomyolipomas). mTOR inhibitors (everolimus, sirolimus) are targeted therapies.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Tuberous sclerosis involves TSC1 (hamartin) or TSC2 (tuberin) mutations leading to uncontrolled mTOR pathway hyperactivation, treated with mTOR inhibitors.",
        "image": None
    })

    # Q42
    qs.append({
        "id": "exam3_in_house_like_g_q42",
        "q_num": "42",
        "stem": "A 6-month-old infant presents with focal motor seizures. Physical examination reveals a large, dark purple, unilateral cutaneous vascular malformation over the forehead and upper eyelid in the ophthalmic (V1) distribution of the trigeminal nerve (port-wine stain / nevus flammeus). Noncontrast head CT reveals ipsilateral leptomeningeal angiomatosis with gyriform, calcified 'tram-track' cortical calcifications underlying the angioma. Which of the following is the underlying genetic mechanism of this syndrome?",
        "category": "Tumors",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Autosomal dominant germline mutation in TSC2"},
            {"letter": "B", "is_correct": True, "text": "Non-inherited somatic mosaic GNAQ gene mutation"},
            {"letter": "C", "is_correct": False, "text": "Autosomal recessive trinucleotide GAA expansion"},
            {"letter": "D", "is_correct": False, "text": "X-linked dominant mutation in the MECP2 gene"},
            {"letter": "E", "is_correct": False, "text": "Germline loss-of-function mutation in VHL gene"}
        ],
        "correct_idx": 1,
        "explanation": "Sturge-Weber syndrome (encephalotrigeminal angiomatosis) is a congenital neurocutaneous disorder that is NON-inherited, caused by a postzygotic, somatic mosaic activating mutation in the GNAQ gene (encoding a G-protein alpha-q subunit). Manifestations include a unilateral cutaneous facial capillary vascular malformation (port-wine stain / nevus flammeus in V1/V2 distribution), ipsilateral leptomeningeal angiomatosis, cortical 'tram-track' gyriform calcifications, intractable seizures, intellectual disability, and early-onset glaucoma.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Sturge-Weber syndrome is non-inherited (somatic mosaic GNAQ mutation), featuring port-wine stain in V1 distribution, leptomeningeal angioma, and tram-track calcifications.",
        "image": None
    })

    # Q43
    qs.append({
        "id": "exam3_in_house_like_g_q43",
        "q_num": "43",
        "stem": "A 15-year-old boy presents with headaches and double vision. Neuro-ophthalmologic examination reveals impaired upward vertical gaze, bilateral pupillary light-near dissociation (pupils constrict normally during convergence but fail to constrict to direct light), convergence-retraction nystagmus on attempted upward gaze, and bilateral eyelid retraction (Collier sign). Neuroimaging reveals a contrast-enhancing mass in the pineal region compressing the dorsal midbrain. Which of the following anatomical structures is directly compressed to produce this clinical triad?",
        "category": "Tumors",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Ventral basis pontis and corticospinal tracts"},
            {"letter": "B", "is_correct": True, "text": "Dorsal midbrain pretectum and superior colliculi"},
            {"letter": "C", "is_correct": False, "text": "Anterior inferior cerebellum and vermian lobule"},
            {"letter": "D", "is_correct": False, "text": "Caudal medulla olive and solitary tract nuclei"},
            {"letter": "E", "is_correct": False, "text": "Sellar pituitary fossa and anterior optic chiasm"}
        ],
        "correct_idx": 1,
        "explanation": "This patient has Parinaud syndrome (dorsal midbrain syndrome), caused by compression of the dorsal midbrain tectum/pretectal area and superior colliculi, classically by a pineal region neoplasm (germinoma or pineocytoma) or obstructive hydrocephalus. The syndrome consists of: (1) upward vertical gaze palsy, (2) pupillary light-near dissociation (pretectal light reflex fibers damaged, Edinger-Westphal convergence spared), and (3) convergence-retraction nystagmus and bilateral lid retraction.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Parinaud syndrome results from pineal mass compression of the dorsal midbrain tectum/pretectum, causing upward gaze palsy and light-near pupillary dissociation.",
        "image": None
    })

    # Q44
    qs.append({
        "id": "exam3_in_house_like_g_q44",
        "q_num": "44",
        "stem": "A 28-year-old woman presents with amenorrhea and bilateral galactorrhea. Visual field testing reveals bitemporal hemianopia. Brain MRI confirms a 2.2-cm intrasellar mass with suprasellar extension compressing the optic chiasm. Serum prolactin is markedly elevated at 280 ng/mL (normal <25 ng/mL). Which of the following medications is the most appropriate initial pharmacological therapy for this patient?",
        "category": "Tumors",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Somatostatin receptor analog octreotide"},
            {"letter": "B", "is_correct": True, "text": "Dopamine D2 receptor agonist cabergoline"},
            {"letter": "C", "is_correct": False, "text": "Glucocorticoid receptor antagonist mifepristone"},
            {"letter": "D", "is_correct": False, "text": "Growth hormone receptor antagonist pegvisomant"},
            {"letter": "E", "is_correct": False, "text": "GnRH receptor antagonist leuprolide depot"}
        ],
        "correct_idx": 1,
        "explanation": "Prolactinoma is the most common functional pituitary neuroendocrine tumor. In premenopausal women, hyperprolactinemia causes amenorrhea, galactorrhea, and infertility; macroadenomas (>10 mm) compress the optic chiasm producing bitemporal hemianopia. Because hypothalamic dopamine provides tonic physiologic inhibition of lactotroph prolactin secretion, first-line therapy for prolactinomas (even macroprolactinomas with visual deficits!) is medical management with dopamine D2 receptor agonists (cabergoline or bromocriptine), which reliably shrink the tumor and normalize prolactin levels.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Prolactinomas are treated primarily with dopamine agonists (cabergoline/bromocriptine) to inhibit secretion and shrink tumor size; surgery is reserved for refractory cases.",
        "image": None
    })

    # Q45
    qs.append({
        "id": "exam3_in_house_like_g_q45",
        "q_num": "45",
        "stem": "A 55-year-old woman with a large right frontoparietal glioblastoma suddenly becomes stuporous. On examination, her right pupil is 7 mm, fixed, and completely unreactive to direct light, while the left pupil is 3 mm and reactive. She demonstrates left-sided spastic hemiplegia and an extensor plantar response on the left. Which of the following intracranial herniation syndromes is occurring in this patient?",
        "category": "Tumors",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Subfalcine herniation under the cerebral falx"},
            {"letter": "B", "is_correct": True, "text": "Uncal transtentorial herniation of temporal lobe"},
            {"letter": "C", "is_correct": False, "text": "Tonsillar herniation into the foramen magnum"},
            {"letter": "D", "is_correct": False, "text": "Upward trans-cerebellar herniation of posterior vermis"},
            {"letter": "E", "is_correct": False, "text": "Trans-calvarial external brain tissue herniation"}
        ],
        "correct_idx": 1,
        "explanation": "Uncal (transtentorial) herniation occurs when an expanding supratentorial lateral mass forces the uncus of the medial temporal lobe medially and downward over the tentorium cerebelli. Compression of the ipsilateral oculomotor nerve (CN III) parasympathetic fibers causes ipsilateral pupil dilation and loss of light reflex ('blown pupil'). Compression of the ipsilateral cerebral peduncle (corticospinal tract) causes contralateral hemiplegia. Compression of the posterior cerebral artery (PCA) can cause ipsilateral occipital infarction.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Uncal herniation causes ipsilateral blown pupil (CN III compression) and contralateral hemiparesis (cerebral peduncle compression); Duret hemorrhages can follow.",
        "image": None
    })

    # Q46
    qs.append({
        "id": "exam3_in_house_like_g_q46",
        "q_num": "46",
        "stem": "A 55-year-old woman with an expanding intracranial mass experiences acute uncal transtentorial herniation with ipsilateral pupillary dilation and contralateral hemiparesis. Several hours later, she experiences rapid neurological deterioration into coma with decerebrate posturing. Autopsy reveals secondary linear flame-shaped midbrain and upper pontine parenchymal hemorrhages caused by downward displacement and caudal stretching of penetrating paramedian basilar arterial branches. Which of the following eponyms designates these fatal brainstem hemorrhages?",
        "category": "Tumors",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Charcot-Bouchard microaneurysmal ruptures"},
            {"letter": "B", "is_correct": True, "text": "Duret hemorrhages of the brainstem tegmentum"},
            {"letter": "C", "is_correct": False, "text": "Kernohan notch false localizing contusions"},
            {"letter": "D", "is_correct": False, "text": "Spicer-Russell vascular angiomatous lesions"},
            {"letter": "E", "is_correct": False, "text": "Binswanger subcortical lacunar hemorrhages"}
        ],
        "correct_idx": 1,
        "explanation": "Duret hemorrhages are secondary linear or flame-shaped hemorrhages in the midline paramedian tegmentum of the midbrain and upper pons. They result from downward axial displacement of the brainstem caused by central or uncal transtentorial herniation, which stretches and tears the penetrating paramedian arterial branches of the basilar artery. They are typically fatal.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Duret hemorrhages are secondary brainstem hemorrhages in the pons/midbrain caused by shearing of paramedian basilar perforators during transtentorial herniation.",
        "image": None
    })

    # Q47
    qs.append({
        "id": "exam3_in_house_like_g_q47",
        "q_num": "47",
        "stem": "A 62-year-old man presents with progressive headaches and left hemiparesis. Brain MRI reveals a right frontal glioblastoma surrounded by extensive, finger-like T2/FLAIR hyperintensity in the cerebral white matter that spares the overlying cerebral cortex. Intravenous administration of dexamethasone produces rapid, marked clinical improvement within 24 hours. Which of the following forms of cerebral edema was present in this patient?",
        "category": "Tumors",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Cytotoxic intracellular astrocytic edema"},
            {"letter": "B", "is_correct": True, "text": "Vasogenic extracellular white matter edema"},
            {"letter": "C", "is_correct": False, "text": "Interstitial transependymal CSF hydrocephalic edema"},
            {"letter": "D", "is_correct": False, "text": "Osmotic hypo-osmolar hyperhydration edema"},
            {"letter": "E", "is_correct": False, "text": "Hydrostatic post-reperfusion hyperemic edema"}
        ],
        "correct_idx": 1,
        "explanation": "Vasogenic cerebral edema is caused by disruption of the blood-brain barrier (tight junctions between endothelial cells), allowing fluid and plasma proteins to transudate into the extracellular space. It selectively tracks along white matter tracts (finger-like distribution on FLAIR) while sparing cortical gray matter. It is characteristically seen surrounding brain tumors, metastases, and abscesses, and responds dramatically to high-dose corticosteroids (dexamethasone), which restore endothelial tight junction integrity. Cytotoxic edema (intracellular swelling from ATP depletion in stroke) does NOT respond to steroids.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Vasogenic edema involves blood-brain barrier breakdown around tumors/abscesses, spreads in white matter, and responds to dexamethasone. Cytotoxic edema in stroke does not.",
        "image": None
    })

    # Q48
    qs.append({
        "id": "exam3_in_house_like_g_q48",
        "q_num": "48",
        "stem": "A 14-year-old girl with neurofibromatosis type 1 is undergoing annual surveillance. Slit-lamp biomicroscopy of the eyes reveals bilateral, multiple, well-demarcated, dome-shaped, tan-brown hamartomas on the anterior surface of the iris stroma that do not interfere with vision. Which of the following is the specific designation for these iris lesions?",
        "category": "Tumors",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Kayser-Fleischer peripheral copper rings"},
            {"letter": "B", "is_correct": True, "text": "Lisch nodules of melanocytic hamartomas"},
            {"letter": "C", "is_correct": False, "text": "Brushfield spots of the iris periphery"},
            {"letter": "D", "is_correct": False, "text": "Ash-leaf hypopigmented retinal spots"},
            {"letter": "E", "is_correct": False, "text": "Horner syndrome sympathetic iris changes"}
        ],
        "correct_idx": 1,
        "explanation": "Lisch nodules are benign melanocytic hamartomas of the iris stroma that appear as small, yellow-to-brown, dome-shaped papules on slit-lamp examination. They are present in >90% of adult patients with neurofibromatosis type 1 (NF1) and represent one of the cardinal diagnostic criteria. They are absent in NF2.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Lisch nodules are pigmented iris hamartomas pathognomonic for Neurofibromatosis type 1 (NF1); they do not occur in NF2.",
        "image": None
    })

    return qs

if __name__ == '__main__':
    qs = get_part1_questions()
    print(f"Generated {len(qs)} questions for Part 1 (Q1 - Q48).")
