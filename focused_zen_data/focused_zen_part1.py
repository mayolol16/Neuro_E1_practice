# focused_zen_part1.py
# 80 Board-Style USMLE Step 1 Questions directly aligned with
# "Copy of Long NeuroPsych Exam 1 Study Guide.docx"
# Topics 1-4 (20 Questions each, IDs FZ_Q001 to FZ_Q080)

focused_questions_part1 = [
    # =========================================================================
    # TOPIC 1: Central Nervous System Anatomy (FZ_Q001 - FZ_Q020)
    # =========================================================================
    {
        "id": "FZ_Q001",
        "question_number": 1,
        "category": "Central Nervous System Anatomy",
        "stem": "A 58-year-old man with a history of long-standing hypertension presents to the emergency department with sudden-onset weakness. Physical examination reveals dense paralysis of the left face, left arm, and left leg, accompanied by loss of vibration, proprioception, and pinprick sensation over the entire left side of the body. There are no visual field deficits, language abnormalities, or cranial nerve palsies other than a central lower facial droop. A non-contrast head CT reveals a small, focal lacunar infarct. Which of the following anatomical structures is most likely affected?",
        "options": [
            {"text": "Anterior limb of the internal capsule", "is_correct": False},
            {"text": "Genu of the internal capsule", "is_correct": False},
            {"text": "Posterior limb of the internal capsule", "is_correct": True},
            {"text": "Ventral posteromedial (VPM) nucleus of the thalamus", "is_correct": False},
            {"text": "Medial lemniscus in the caudal medulla", "is_correct": False}
        ],
        "explanation": "Correct Answer: C. Posterior limb of the internal capsule.\n\nThe posterior limb of the internal capsule contains descending corticospinal motor tracts (conveying voluntary motor control to the contralateral body) and ascending third-order sensory fibers projecting from the thalamus (VPL/VPM) to the primary somatosensory cortex. A lacunar infarct in the posterior limb produces a dense contralateral combined sensorimotor stroke affecting the face, arm, and leg equally.\n\n• Option A is incorrect: The anterior limb conveys frontopontine tracts and thalamocortical limbic projections involved in emotional and cognitive processing.\n• Option B is incorrect: The genu carries corticobulbar fibers innervating cranial nerve motor nuclei; a lesion causes isolated contralateral lower facial and hypoglossal weakness without hemibody sensory loss.\n• Option D is incorrect: The VPM nucleus relays facial sensation only, not the whole hemibody.\n• Option E is incorrect: A caudal medullary medial lemniscus lesion produces contralateral loss of vibration and proprioception, sparing corticospinal motor pathways and pinprick sensation."
    },
    {
        "id": "FZ_Q002",
        "question_number": 2,
        "category": "Central Nervous System Anatomy",
        "stem": "A 62-year-old woman is brought to the emergency department 1 hour after the sudden onset of vertigo, severe nausea, and difficulty swallowing. Neurological examination reveals right-sided facial loss of pain and temperature sensation, left-sided body loss of pain and temperature sensation, right-sided Horner syndrome (ptosis, miosis, anhidrosis), hoarseness, loss of the gag reflex on the right, and severe right-sided limb ataxia. Occlusion of which of the following arteries is the most likely cause of this patient's presentation?",
        "options": [
            {"text": "Anterior spinal artery (ASA)", "is_correct": False},
            {"text": "Anterior inferior cerebellar artery (AICA)", "is_correct": False},
            {"text": "Posterior inferior cerebellar artery (PICA)", "is_correct": True},
            {"text": "Superior cerebellar artery (SCA)", "is_correct": False},
            {"text": "Posterior cerebral artery (PCA)", "is_correct": False}
        ],
        "explanation": "Correct Answer: C. Posterior inferior cerebellar artery (PICA).\n\nThis patient presents with Wallenberg syndrome (lateral medullary syndrome), classic for occlusion of the PICA or vertebral artery. The clinical findings map directly to lateral medullary structures:\n• Nucleus ambiguus (CN IX, X): Dysphagia, hoarseness, decreased gag reflex, uvula deviation.\n• Spinal trigeminal nucleus/tract: Ipsilateral facial loss of pain and temperature.\n• Spinothalamic tract: Contralateral body loss of pain and temperature.\n• Descending sympathetic fibers: Ipsilateral Horner syndrome (ptosis, miosis, anhidrosis).\n• Inferior cerebellar peduncle: Ipsilateral limb ataxia.\n• Vestibular nuclei: Vertigo, nystagmus, nausea, vomiting.\n\n• Option A is incorrect: Medial medullary syndrome (ASA occlusion) manifests with contralateral hemiparesis, contralateral DCML sensory loss, and ipsilateral tongue deviation.\n• Option B is incorrect: AICA occlusion causes lateral pontine syndrome, uniquely marked by ipsilateral facial paralysis (CN VII) and sensorineural hearing loss (CN VIII)."
    },
    {
        "id": "FZ_Q003",
        "question_number": 3,
        "category": "Central Nervous System Anatomy",
        "stem": "A 71-year-old man presents with sudden-onset weakness in his right leg and urinary incontinence. On physical examination, he has 1/5 motor strength in his right lower extremity with a positive Babinski sign, while his right upper extremity exhibits 4+/5 strength. He also has marked sensory loss to pinprick and vibration over the right foot and leg, but normal sensation over the right face and arm. Which of the following cerebral arteries is most likely occluded?",
        "options": [
            {"text": "Left anterior cerebral artery (ACA)", "is_correct": True},
            {"text": "Left middle cerebral artery (MCA)", "is_correct": False},
            {"text": "Left posterior cerebral artery (PCA)", "is_correct": False},
            {"text": "Right anterior choroidal artery", "is_correct": False},
            {"text": "Right lenticulostriate artery", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Left anterior cerebral artery (ACA).\n\nThe anterior cerebral artery (ACA) supplies the medial surface of the frontal and parietal lobes, which corresponds to the lower extremity representation on the motor and sensory homunculi. Infarction of the ACA causes contralateral motor and sensory deficits affecting the leg and foot far more severely than the arm and face, often accompanied by frontal lobe signs such as urinary incontinence, abulia, and primitive reflexes.\n\n• Option B is incorrect: MCA occlusion damages the lateral convexity of the hemisphere, resulting in contralateral face and arm weakness greater than leg weakness, along with aphasia or hemineglect.\n• Option C is incorrect: PCA infarction causes contralateral homonymous hemianopia with macular sparing.\n• Options D and E are incorrect: Lenticulostriate and anterior choroidal infarcts damage the internal capsule, causing dense, proportionate weakness of the face, arm, and leg equally."
    },
    {
        "id": "FZ_Q004",
        "question_number": 4,
        "category": "Central Nervous System Anatomy",
        "stem": "A 23-year-old professional hockey player is struck on the side of the head by a puck. He suffers a brief period of concussion followed by complete lucidity. Three hours later, he complains of an excruciating headache and rapidly becomes lethargic. An unenhanced head CT reveals a biconvex, lentiform hyperdense collection that does not cross cranial suture lines. Fracturing of which of the following skull landmarks is most closely associated with this vascular injury?",
        "options": [
            {"text": "Cribriform plate of the ethmoid bone", "is_correct": False},
            {"text": "Pterion", "is_correct": True},
            {"text": "Foramen spinosum", "is_correct": False},
            {"text": "Inion (external occipital protuberance)", "is_correct": False},
            {"text": "Mastoid process of the temporal bone", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. Pterion.\n\nThis patient has an epidural hematoma. The pterion is the junction of four skull bones: frontal, parietal, temporal, and greater wing of the sphenoid. It is the thinnest part of the calvarium. Deep to the pterion lies the anterior branch of the middle meningeal artery (a branch of the maxillary artery). Fractures at this site lacerate the artery, resulting in arterial bleeding that strips the periosteal dura from the skull, creating a classic biconvex (lens-shaped) hematoma bounded by cranial suture lines.\n\n• Option A is incorrect: Cribriform plate fracture tears olfactory fila (anosmia) and meninges (CSF rhinorrhea).\n• Option C is incorrect: The foramen spinosum transmits the middle meningeal artery into the cranial vault, but calvarial impact fractures the pterion overlying the artery's calvarial branches.\n• Option D is incorrect: The inion lies in the midline occipital bone overlying the torcular Herophili."
    },
    {
        "id": "FZ_Q005",
        "question_number": 5,
        "category": "Central Nervous System Anatomy",
        "stem": "A 45-year-old woman presents to the clinic with diplopia when walking down stairs and reading books. On examination, when she is asked to look downward and inward toward her nose with the left eye, she experiences vertical diplopia. She tilts her head toward her right shoulder to compensate. Which of the following cranial nerves is impaired, and where does it emerge from the brainstem?",
        "options": [
            {"text": "Trochlear nerve (CN IV); dorsal midbrain inferior to the inferior colliculi", "is_correct": True},
            {"text": "Oculomotor nerve (CN III); interpeduncular fossa of the ventral midbrain", "is_correct": False},
            {"text": "Abducens nerve (CN VI); pontomedullary junction", "is_correct": False},
            {"text": "Trochlear nerve (CN IV); ventrolateral pons", "is_correct": False},
            {"text": "Oculomotor nerve (CN III); dorsal midbrain superior to the superior colliculi", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Trochlear nerve (CN IV); dorsal midbrain inferior to the inferior colliculi.\n\nThe trochlear nerve (CN IV) innervates the superior oblique muscle, which depresses the adducted eye and intorts the globe. Lesions cause vertical diplopia that is most prominent when walking downstairs or reading (gazing downward and inward). Patients tilt their head away from the affected side (compensatory contralateral tilt) to extort the normal eye and align visual axes. Anatomically, CN IV is unique because it is the only cranial nerve that exits from the dorsal (posterior) surface of the brainstem, just caudal to the inferior colliculi.\n\n• Option B is incorrect: CN III emerges ventrally from the interpeduncular fossa; lesions cause ptosis, a 'down-and-out' pupil, and mydriasis.\n• Option C is incorrect: CN VI emerges ventrally at the pontomedullary junction and innervates the lateral rectus (abduction).\n• Options D and E are incorrect: CN IV does not exit ventrally, and CN III does not exit dorsally."
    },
    {
        "id": "FZ_Q006",
        "question_number": 6,
        "category": "Central Nervous System Anatomy",
        "stem": "A 68-year-old man presents with acute-onset right-sided hemiballismus, characterized by involuntary, high-amplitude, violent, flinging movements of his right arm and leg. A head MRI reveals a discrete ischemic stroke in the deep subcortical brain. Degeneration or acute infarction of which of the following structures is most specifically responsible for this movement disorder?",
        "options": [
            {"text": "Caudate nucleus", "is_correct": False},
            {"text": "Putamen", "is_correct": False},
            {"text": "Subthalamic nucleus of Luys", "is_correct": True},
            {"text": "Globus pallidus internus (GPi)", "is_correct": False},
            {"text": "Substantia nigra pars reticulata", "is_correct": False}
        ],
        "explanation": "Correct Answer: C. Subthalamic nucleus of Luys.\n\nHemiballismus consists of rapid, involuntary, violent flinging movements of the contralateral limbs. It is caused by an acute lesion (usually a lacunar stroke from lenticulostriate or posterior cerebral perforators) in the contralateral subthalamic nucleus (STN). In the indirect pathway of the basal ganglia, the STN provides excitatory glutamatergic drive to the globus pallidus internus (GPi). Loss of STN excitation disinhibits the motor thalamus (VA/VL), leading to hyperkinetic motor cortical output.\n\n• Option A is incorrect: Caudate atrophy occurs in Huntington disease, causing generalized chorea, psychiatric changes, and executive dysfunction.\n• Option B is incorrect: Putaminal lesions are seen in Wilson disease and dystonia.\n• Option D is incorrect: Increased (not decreased) GPi output produces the bradykinesia and rigidity of Parkinson disease."
    },
    {
        "id": "FZ_Q007",
        "question_number": 7,
        "category": "Central Nervous System Anatomy",
        "stem": "A 34-year-old woman with relapsing-remitting multiple sclerosis presents with horizontal diplopia during lateral gaze. On neurological examination, when she attempts to look to the left, her left eye abducts fully with horizontal nystagmus, but her right eye fails to adduct past the midline. However, when tested for near vision convergence, both eyes adduct symmetrically and constrict normally. This patient's deficit is localized to which of the following brainstem white matter tracts?",
        "options": [
            {"text": "Central tegmental tract", "is_correct": False},
            {"text": "Medial longitudinal fasciculus (MLF)", "is_correct": True},
            {"text": "Lateral lemniscus", "is_correct": False},
            {"text": "Spinothalamic tract", "is_correct": False},
            {"text": "Superior cerebellar peduncle", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. Medial longitudinal fasciculus (MLF).\n\nThis patient exhibits right internuclear ophthalmoplegia (INO). The medial longitudinal fasciculus (MLF) is a heavily myelinated brainstem tract that coordinates conjugate horizontal eye movements by transmitting signals from the contralateral abducens nucleus (CN VI in the pons) to the ipsilateral oculomotor nucleus (medial rectus subnucleus of CN III in the midbrain). Impaired right adduction on left conjugate gaze indicates a lesion of the right MLF. Convergence is spared because it is mediated by cortical inputs directly to CN III that bypass the MLF.\n\n• Option A is incorrect: The central tegmental tract connects the red nucleus to the inferior olivary nucleus; damage causes palatal myoclonus.\n• Option B is incorrect: The lateral lemniscus carries auditory information from the cochlear nuclei to the inferior colliculus.\n• Option E is incorrect: The superior cerebellar peduncle carries dentatorubrothalamic fibers."
    },
    {
        "id": "FZ_Q008",
        "question_number": 8,
        "category": "Central Nervous System Anatomy",
        "stem": "A 54-year-old man presents with hoarseness, difficulty swallowing solid foods, and weakness shrugging his right shoulder. On physical examination, the uvula deviates to the left upon phonation, and the gag reflex is absent on the right. When asked to turn his head to the left against resistance, there is noticeable weakness of the right sternocleidomastoid muscle. Sensation to the posterior third of the tongue is absent. A tumor compressing which of the following skull base foramina would explain all of these findings?",
        "options": [
            {"text": "Foramen ovale", "is_correct": False},
            {"text": "Foramen rotundum", "is_correct": False},
            {"text": "Internal acoustic meatus", "is_correct": False},
            {"text": "Jugular foramen", "is_correct": True},
            {"text": "Hypoglossal canal", "is_correct": False}
        ],
        "explanation": "Correct Answer: D. Jugular foramen.\n\nThis patient has Vernet syndrome (jugular foramen syndrome), caused by compression of cranial nerves IX, X, and XI as they exit the skull base through the jugular foramen:\n• CN IX (Glossopharyngeal): Loss of sensation on the posterior 1/3 of the tongue, loss of afferent limb of the gag reflex.\n• CN X (Vagus): Uvula deviation to the contralateral (left) side, dysphagia, hoarseness, loss of efferent gag reflex.\n• CN XI (Accessory): Weakness of the right sternocleidomastoid (causing difficulty turning the head to the left) and trapezius (shoulder droop).\n\n• Option A is incorrect: The foramen ovale transmits CN V3, the lesser petrosal nerve, and accessory meningeal artery.\n• Option B is incorrect: The foramen rotundum transmits CN V2.\n• Option C is incorrect: The internal acoustic meatus transmits CN VII and CN VIII.\n• Option E is incorrect: The hypoglossal canal transmits CN XII (tongue deviation)."
    },
    {
        "id": "FZ_Q009",
        "question_number": 9,
        "category": "Central Nervous System Anatomy",
        "stem": "A 74-year-old woman is brought to the neurology clinic by her family because she can no longer communicate effectively. While her speech is effortless, melodious, and fluent, her sentences make no sense and consist of nonsensical neologisms and word substitutions (word salad). When given written and spoken commands, she cannot comprehend or follow them. She also cannot repeat simple phrases. A lesion in which of the following cortical areas supplied by the middle cerebral artery is responsible?",
        "options": [
            {"text": "Brodmann areas 44 and 45 in the inferior frontal gyrus", "is_correct": False},
            {"text": "Brodmann area 22 in the posterior superior temporal gyrus", "is_correct": True},
            {"text": "Brodmann area 4 in the precentral gyrus", "is_correct": False},
            {"text": "Brodmann areas 3, 1, and 2 in the postcentral gyrus", "is_correct": False},
            {"text": "Brodmann area 39 in the angular gyrus", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. Brodmann area 22 in the posterior superior temporal gyrus.\n\nThis patient has Wernicke (receptive/sensory/fluent) aphasia, characterized by impaired comprehension, intact speech fluency, and impaired repetition. Wernicke area corresponds to Brodmann area 22 in the posterior part of the superior temporal gyrus of the dominant hemisphere (supplied by the inferior division of the middle cerebral artery).\n\n• Option A is incorrect: Broca area corresponds to Brodmann areas 44 and 45 in the inferior frontal gyrus; lesions produce non-fluent, halting, agrammatic speech with preserved comprehension.\n• Option C is incorrect: Brodmann area 4 is the primary motor cortex in the precentral gyrus.\n• Option E is incorrect: Brodmann area 39 is the angular gyrus; lesions in the dominant hemisphere produce Gerstmann syndrome (agraphia, acalculia, finger agnosia, left-right disorientation)."
    },
    {
        "id": "FZ_Q010",
        "question_number": 10,
        "category": "Central Nervous System Anatomy",
        "stem": "A 66-year-old chronic alcoholic man presents with progressive ataxia and frequent falls. On physical examination, he demonstrates a wide-based, staggering, unsteady gait and marked titubation (bobbing of the trunk and head). However, when seated with his trunk supported, he performs rapid alternating movements, finger-to-nose testing, and heel-to-shin testing smoothly and without intention tremor or dysmetria. Neuropathology in this patient is most likely localized to which of the following regions?",
        "options": [
            {"text": "Cerebellar vermis", "is_correct": True},
            {"text": "Lateral cerebellar hemispheres", "is_correct": False},
            {"text": "Flocculonodular lobe", "is_correct": False},
            {"text": "Dentate nucleus", "is_correct": False},
            {"text": "Subthalamic nucleus", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Cerebellar vermis.\n\nThe cerebellar vermis is the midline zone of the cerebellum that coordinates the vestibulospinal and reticulospinal tracts, controlling axial balance, truncal stability, and gait. Chronic alcoholism and thiamine deficiency selectively cause atrophy of the anterior vermis, resulting in severe truncal ataxia, wide-based gait, and titubation, while sparing appendicular coordination of the limbs.\n\n• Options B and D are incorrect: The lateral cerebellar hemispheres and dentate nuclei coordinate voluntary appendicular limb movements; lesions cause dysmetria, intention tremor, and dysdiadochokinesia of the ipsilateral limbs.\n• Option C is incorrect: The flocculonodular lobe (vestibulocerebellum) controls eye movements and vestibular balance; lesions cause nystagmus, vertigo, and truncal instability."
    },
    {
        "id": "FZ_Q011",
        "question_number": 11,
        "category": "Central Nervous System Anatomy",
        "stem": "A 52-year-old man presents with right visual field loss. Visual field testing reveals a right homonymous hemianopia with complete macular sparing. An MRI of the brain confirms an ischemic stroke in the occipital lobe. Which of the following cerebral arteries was most likely occluded, and which collateral vessel preserves macular vision?",
        "options": [
            {"text": "Left PCA occluded; collateral supply from the left MCA", "is_correct": True},
            {"text": "Left MCA occluded; collateral supply from the left ACA", "is_correct": False},
            {"text": "Right PCA occluded; collateral supply from the right MCA", "is_correct": False},
            {"text": "Left anterior choroidal artery occluded; collateral supply from the left PCA", "is_correct": False},
            {"text": "Right ophthalmic artery occluded; collateral supply from the facial artery", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Left PCA occluded; collateral supply from the left MCA.\n\nInfarction of the left primary visual cortex (Brodmann area 17) in the occipital lobe produces contralateral (right) homonymous hemianopia. The visual cortex is supplied by the posterior cerebral artery (PCA). Macular sparing occurs because the occipital pole (which represents the macula) possesses dual collateral blood supply from both the terminal branches of the PCA and the middle cerebral artery (MCA).\n\n• Option B is incorrect: MCA occlusion damages optic radiations (Meyer loop or parietal radiations), causing quadrantanopias without macular sparing.\n• Option C is incorrect: A right PCA infarction causes left homonymous hemianopia.\n• Option D is incorrect: Anterior choroidal artery occlusion causes homonymous hemianopia without macular sparing."
    },
    {
        "id": "FZ_Q012",
        "question_number": 12,
        "category": "Central Nervous System Anatomy",
        "stem": "A 41-year-old woman is admitted to the intensive care unit with bacterial sphenoid sinusitis complicated by cavernous sinus thrombosis. On physical examination, her right eye is fixed in mid-position and cannot abduct laterally on command. When evaluating which structure is earliest affected, the physician recalls the neuroanatomy of the cavernous sinus. Which of the following cranial nerves courses freely through the interior venous lumen of the cavernous sinus alongside the internal carotid artery?",
        "options": [
            {"text": "Oculomotor nerve (CN III)", "is_correct": False},
            {"text": "Trochlear nerve (CN IV)", "is_correct": False},
            {"text": "Ophthalmic nerve (CN V1)", "is_correct": False},
            {"text": "Maxillary nerve (CN V2)", "is_correct": False},
            {"text": "Abducens nerve (CN VI)", "is_correct": True}
        ],
        "explanation": "Correct Answer: E. Abducens nerve (CN VI).\n\nThe cavernous sinus contains neurovascular structures arranged into two anatomical groups:\n• Embedded within the lateral dural wall (from superior to inferior): CN III (Oculomotor), CN IV (Trochlear), CN V1 (Ophthalmic), and CN V2 (Maxillary).\n• Free within the interior venous lumen of the sinus: Internal carotid artery and CN VI (Abducens nerve).\nBecause CN VI floats directly within the venous blood of the sinus immediately adjacent to the internal carotid artery, it is the most vulnerable nerve to early compression from thrombosis, carotid cavernous fistulas, or cavernous internal carotid aneurysms, leading to isolated lateral rectus palsy (failure of abduction).\n\n• Options A, B, C, and D are incorrect: CN III, IV, V1, and V2 are embedded within the protective fibrous lateral wall of the cavernous sinus."
    },
    {
        "id": "FZ_Q013",
        "question_number": 13,
        "category": "Central Nervous System Anatomy",
        "stem": "A 22-year-old man survives a high-speed motorcycle crash resulting in multiple basilar skull fractures. Physical examination reveals clear, watery fluid dripping from his right nostril that tests positive for beta-2 transferrin. He also reports complete loss of his sense of smell. Shearing of delicate unmyelinated nerve fibers passing through which of the following skull base structures is the direct cause of this patient's anosmia?",
        "options": [
            {"text": "Cribriform plate of the ethmoid bone", "is_correct": True},
            {"text": "Optic canal of the sphenoid bone", "is_correct": False},
            {"text": "Superior orbital fissure", "is_correct": False},
            {"text": "Foramen lacerum", "is_correct": False},
            {"text": "Stylomastoid foramen", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Cribriform plate of the ethmoid bone.\n\nThe olfactory nerve (CN I) consists of primary sensory axons that pass from the olfactory neuroepithelium through the perforations of the cribriform plate of the ethmoid bone to synapse in the olfactory bulb. Fracture of the cribriform plate tears these delicate fila olfactoria and tears the underlying dura and arachnoid, resulting in permanent anosmia and CSF rhinorrhea (confirmed by beta-2 transferrin).\n\n• Option B is incorrect: The optic canal transmits CN II and the ophthalmic artery.\n• Option C is incorrect: The superior orbital fissure transmits CN III, IV, V1, and VI.\n• Option D is incorrect: The foramen lacerum is occluded by fibrocartilage in vivo.\n• Option E is incorrect: The stylomastoid foramen transmits the motor trunk of CN VII."
    },
    {
        "id": "FZ_Q014",
        "question_number": 14,
        "category": "Central Nervous System Anatomy",
        "stem": "A 60-year-old man with poorly controlled hypertension experiences an acute brainstem stroke. Physical examination demonstrates an ipsilateral flaccid paralysis of the tongue that deviates to the right upon protrusion, contralateral loss of vibration and position sense in the limbs, and contralateral spastic hemiparesis. Occlusion of which of the following arterial vessels produces this clinical triad of medial medullary syndrome?",
        "options": [
            {"text": "Posterior inferior cerebellar artery (PICA)", "is_correct": False},
            {"text": "Anterior spinal artery (ASA)", "is_correct": True},
            {"text": "Anterior inferior cerebellar artery (AICA)", "is_correct": False},
            {"text": "Basilar artery paramedian branches", "is_correct": False},
            {"text": "Labyrinthine artery", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. Anterior spinal artery (ASA).\n\nThis patient presents with medial medullary syndrome (Dejerine syndrome), caused by occlusion of the anterior spinal artery (ASA) or vertebral artery paramedian branches. The syndrome damages three medial medullary structures:\n1. Hypoglossal nucleus and CN XII fibers: Ipsilateral flaccid tongue paralysis with deviation toward the side of the lesion (right).\n2. Pyramids (corticospinal tract): Contralateral spastic hemiparesis.\n3. Medial lemniscus: Contralateral loss of vibration, conscious proprioception, and fine touch.\nPain and temperature sensation is spared because the spinothalamic tract is located laterally.\n\n• Option A is incorrect: PICA occlusion causes lateral medullary (Wallenberg) syndrome.\n• Option C is incorrect: AICA occlusion causes lateral pontine syndrome.\n• Option D is incorrect: Basilar artery paramedian branches supply the medial pons (causing abducens palsy and contralateral hemiparesis)."
    },
    {
        "id": "FZ_Q015",
        "question_number": 15,
        "category": "Central Nervous System Anatomy",
        "stem": "A 35-year-old man undergoes resection of an acoustic neuroma (vestibular schwannoma) located at the cerebellopontine angle. Postoperatively, he exhibits complete paralysis of all muscles of facial expression on the right side, loss of taste on the anterior two-thirds of the tongue, and hyperacusis (extreme sensitivity to loud sounds). Which of the following cranial nerves was injured during the procedure, and what structure normally dampens loud sounds?",
        "options": [
            {"text": "Trigeminal nerve (CN V3); tensor tympani", "is_correct": False},
            {"text": "Facial nerve (CN VII); stapedius", "is_correct": True},
            {"text": "Glossopharyngeal nerve (CN IX); stylopharyngeus", "is_correct": False},
            {"text": "Vagus nerve (CN X); levator veli palatini", "is_correct": False},
            {"text": "Accessory nerve (CN XI); sternocleidomastoid", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. Facial nerve (CN VII); stapedius.\n\nThe facial nerve (CN VII) emerges at the cerebellopontine angle adjacent to CN VIII. Injury causes peripheral lower motor neuron facial paralysis affecting both the upper and lower face. Branches of CN VII include:\n• Nerve to the stapedius: The stapedius muscle dampens excessive vibrations of the stapes against the oval window in response to loud sounds; denervation causes hyperacusis.\n• Chorda tympani: Transmits taste from the anterior 2/3 of the tongue and parasympathetic fibers to the submandibular and sublingual salivary glands.\n• Greater petrosal nerve: Parasympathetic innervation to the lacrimal gland.\n\n• Option A is incorrect: CN V3 innervates the tensor tympani, but its lesion does not cause facial paralysis or taste loss on the anterior 2/3 of the tongue."
    },
    {
        "id": "FZ_Q016",
        "question_number": 16,
        "category": "Central Nervous System Anatomy",
        "stem": "A 77-year-old man with memory loss undergoes brain MRI as part of a dementia workup. The radiologist notes severe, selective bilateral atrophy of the hippocampus and the primary white matter tract that projects from the subiculum of the hippocampus to the mammillary bodies of the hypothalamus. Disruption of this tract impairs the consolidation of new declarative memories. Which of the following structures is being described?",
        "options": [
            {"text": "Anterior commissure", "is_correct": False},
            {"text": "Corpus callosum", "is_correct": False},
            {"text": "Fornix", "is_correct": True},
            {"text": "Stria terminalis", "is_correct": False},
            {"text": "Uncinate fasciculus", "is_correct": False}
        ],
        "explanation": "Correct Answer: C. Fornix.\n\nThe fornix is a C-shaped bundle of white matter fibers that serves as the principal efferent projection tract of the hippocampal formation in the Papez circuit. It connects the hippocampus and subiculum to the mammillary bodies of the hypothalamus and the anterior thalamic nucleus. Bilateral transection or degeneration of the fornix impairs the Papez circuit, producing profound anterograde amnesia and inability to consolidate new declarative memories.\n\n• Option A is incorrect: The anterior commissure connects the anterior temporal lobes and amygdalae.\n• Option B is incorrect: The corpus callosum connects the bilateral neocortical hemispheres.\n• Option D is incorrect: The stria terminalis is the primary efferent tract of the amygdala projecting to the hypothalamus and septal area."
    },
    {
        "id": "FZ_Q017",
        "question_number": 17,
        "category": "Central Nervous System Anatomy",
        "stem": "A 48-year-old woman presents to the clinic with unsteadiness and difficulty walking. Neurological testing demonstrates that she has an absent right patellar reflex and an absent right Achilles tendon reflex, with profound loss of vibratory sensation in her right lower extremity. Her motor strength and pinprick sensation are completely normal. Where are the primary cell bodies of the sensory neurons responsible for transmitting this vibratory input located?",
        "options": [
            {"text": "Ventral horn of the spinal cord", "is_correct": False},
            {"text": "Dorsal horn substantia gelatinosa", "is_correct": False},
            {"text": "Dorsal root ganglion (DRG)", "is_correct": True},
            {"text": "Nucleus gracilis in the medulla", "is_correct": False},
            {"text": "Ventral posterolateral (VPL) nucleus of the thalamus", "is_correct": False}
        ],
        "explanation": "Correct Answer: C. Dorsal root ganglion (DRG).\n\nFirst-order sensory neurons of the dorsal column-medial lemniscal (DCML) pathway (which convey vibration, fine touch, and conscious proprioception) are pseudounipolar neurons whose cell bodies reside in the dorsal root ganglion (DRG). Their peripheral processes innervate encapsulated mechanoreceptors (such as Pacinian corpuscles for vibration), while their central processes enter the spinal cord and ascend ipsilaterally in the dorsal funiculus (fasciculus gracilis and cuneatus) without synapsing in the spinal cord.\n\n• Option A is incorrect: The ventral horn contains somatic lower motor neuron cell bodies.\n• Option B is incorrect: The substantia gelatinosa (Lamina II) contains second-order neurons for the pain and temperature pathway.\n• Option D is incorrect: Nucleus gracilis contains second-order neurons of the DCML pathway in the medulla.\n• Option E is incorrect: The VPL nucleus of the thalamus contains third-order sensory neurons."
    },
    {
        "id": "FZ_Q018",
        "question_number": 18,
        "category": "Central Nervous System Anatomy",
        "stem": "A 56-year-old woman suffers a subarachnoid hemorrhage. Catheter angiography demonstrates a ruptured berry aneurysm located at the junction of the internal carotid artery and the posterior communicating artery (PComA). Which of the following cranial nerve abnormalities is the most characteristic clinical sign of compression by an aneurysm at this specific anatomical location?",
        "options": [
            {"text": "Ipsilateral mydriasis and ptosis with a 'down-and-out' eye", "is_correct": True},
            {"text": "Contralateral loss of abduction with horizontal diplopia", "is_correct": False},
            {"text": "Ipsilateral facial numbness in the V1 distribution", "is_correct": False},
            {"text": "Ipsilateral facial paralysis including forehead weakness", "is_correct": False},
            {"text": "Bitemporal hemianopia", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Ipsilateral mydriasis and ptosis with a 'down-and-out' eye.\n\nThe oculomotor nerve (CN III) emerges from the midbrain in the interpeduncular fossa and passes directly between the posterior cerebral artery (PCA) and the superior cerebellar artery (SCA), running immediately adjacent to the posterior communicating artery (PComA). An aneurysm of the PComA compresses the superficial parasympathetic fibers of CN III first (causing a sluggish or fixed dilated 'blown' pupil / mydriasis), followed by somatic motor fibers (causing ptosis and a 'down-and-out' globe from unopposed action of the superior oblique and lateral rectus).\n\n• Option B is incorrect: CN VI compression causes failure of abduction, associated with cavernous sinus or elevated ICP, not isolated PComA aneurysms.\n• Option C is incorrect: V1 runs in the lateral wall of the cavernous sinus.\n• Option E is incorrect: Bitemporal hemianopia is caused by anterior communicating artery (AComA) aneurysms or pituitary macroadenomas compressing the optic chiasm."
    },
    {
        "id": "FZ_Q019",
        "question_number": 19,
        "category": "Central Nervous System Anatomy",
        "stem": "A 30-year-old woman presents to the clinic with bilateral lower extremity weakness and numbness. Magnetic resonance imaging reveals active demyelinating plaques in the corticospinal tracts and dorsal columns of the cervical spinal cord. In which of the following regions of the medulla oblongata do approximately 85% to 90% of the descending lateral corticospinal tract fibers decussate across the midline?",
        "options": [
            {"text": "Rostral medulla at the level of the open fourth ventricle", "is_correct": False},
            {"text": "Caudal medulla at the junction with the spinal cord", "is_correct": True},
            {"text": "Inferior olivary nucleus", "is_correct": False},
            {"text": "Pontomedullary junction", "is_correct": False},
            {"text": "Crus cerebri of the midbrain", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. Caudal medulla at the junction with the spinal cord.\n\nThe lateral corticospinal tract descends from the motor cortex through the corona radiata, posterior limb of the internal capsule, cerebral peduncle (crus cerebri), and basilar pons into the medullary pyramids. At the caudal medulla (immediately superior to the spinomedullary junction), approximately 85% to 90% of these fibers cross the midline at the pyramidal decussation to form the lateral corticospinal tract in the contralateral lateral funiculus of the spinal cord.\n\n• Option A is incorrect: The rostral medulla features the open 4th ventricle and prominent inferior olives; decussation occurs caudally at the closed medulla.\n• Option C is incorrect: The inferior olive relays climbing fibers to the contralateral cerebellum.\n• Option E is incorrect: The crus cerebri is in the ventral midbrain, where corticospinal fibers are ipsilateral and have not yet decussated."
    },
    {
        "id": "FZ_Q020",
        "question_number": 20,
        "category": "Central Nervous System Anatomy",
        "stem": "A 63-year-old man who underwent resection of a meningioma presents with difficulty tasting food. Detailed cranial nerve examination reveals loss of general sensation and taste on the posterior one-third of the tongue, as well as an absent afferent gag reflex on the left side. Sensation and taste on the anterior two-thirds of his tongue are completely normal. Which of the following cranial nerves is responsible for both general somatic sensation and special visceral taste sensation on the posterior one-third of the tongue?",
        "options": [
            {"text": "Trigeminal nerve (CN V3)", "is_correct": False},
            {"text": "Facial nerve (CN VII)", "is_correct": False},
            {"text": "Glossopharyngeal nerve (CN IX)", "is_correct": True},
            {"text": "Vagus nerve (CN X)", "is_correct": False},
            {"text": "Hypoglossal nerve (CN XII)", "is_correct": False}
        ],
        "explanation": "Correct Answer: C. Glossopharyngeal nerve (CN IX).\n\nThe tongue receives dual sensory innervation:\n• Anterior 2/3 of tongue: General somatic sensation is mediated by the lingual nerve (branch of CN V3); special taste sensation is mediated by the chorda tympani (branch of CN VII).\n• Posterior 1/3 of tongue: BOTH general somatic sensation AND special taste sensation are mediated by the glossopharyngeal nerve (CN IX).\n• Root of tongue / epiglottis: General sensation and taste are mediated by the vagus nerve (CN X).\n• Motor innervation: All intrinsic and extrinsic tongue muscles (except palatoglossus, CN X) are innervated by the hypoglossal nerve (CN XII).\n\n• Options A and B are incorrect: CN V3 and CN VII innervate the anterior 2/3 of the tongue only."
    },

    # =========================================================================
    # TOPIC 2: Central Nervous System Development (FZ_Q021 - FZ_Q040)
    # =========================================================================
    {
        "id": "FZ_Q021",
        "question_number": 21,
        "category": "Central Nervous System Development",
        "stem": "A 28-year-old primigravida presents for routine prenatal screening at 16 weeks of gestation. Maternal serum alpha-fetoprotein (MSAFP) is markedly elevated. A follow-up amniocentesis demonstrates elevated levels of both alpha-fetoprotein and acetylcholinesterase (AChE) in the amniotic fluid. High-resolution ultrasound reveals absence of the calvarium and cerebral hemispheres, with preservation of the brainstem and facial structures. Failure of which of the following embryological processes is responsible for this condition?",
        "options": [
            {"text": "Closure of the caudal neuropore on Day 27–28", "is_correct": False},
            {"text": "Closure of the rostral (cranial) neuropore on Day 25", "is_correct": True},
            {"text": "Migration of cranial neural crest cells into the pharyngeal arches", "is_correct": False},
            {"text": "Cleavage of the prosencephalon into two hemispheres", "is_correct": False},
            {"text": "Radial migration of neuroblasts from the subventricular zone", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. Closure of the rostral (cranial) neuropore on Day 25.\n\nAnencephaly is an open neural tube defect caused by failure of the rostral (anterior/cranial) neuropore to close on approximately Day 25 of embryogenesis. Exposure of developing neural tissue to amniotic fluid leads to necrosis and failure of the forebrain and calvarium to develop. The open defect allows fetal CSF and tissue to transudate into amniotic fluid, causing elevated amniotic alpha-fetoprotein (AFP) and elevated acetylcholinesterase (AChE), the latter of which confirms an open neural tube defect.\n\n• Option A is incorrect: Failure of the caudal neuropore to close on Day 27–28 causes spina bifida / myelomeningocele.\n• Option C is incorrect: Defective cranial neural crest migration causes craniofacial dysmorphisms and DiGeorge syndrome.\n• Option D is incorrect: Failure of prosencephalon cleavage causes holoprosencephaly."
    },
    {
        "id": "FZ_Q022",
        "question_number": 22,
        "category": "Central Nervous System Development",
        "stem": "A healthy 1-month-old infant is brought to the pediatrician for a well-child checkup. Physical examination reveals a small tuft of dark coarse hair overlying the lower lumbar spine at the L5-S1 level. Neurological examination is completely normal, with brisk, symmetric lower extremity movements and intact anal sphincter tone. Prenatal screening showed a normal maternal serum alpha-fetoprotein. Which of the following is the most likely diagnosis?",
        "options": [
            {"text": "Spina bifida occulta", "is_correct": True},
            {"text": "Meningocele", "is_correct": False},
            {"text": "Myelomeningocele", "is_correct": False},
            {"text": "Myeloschisis", "is_correct": False},
            {"text": "Chiari II malformation", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Spina bifida occulta.\n\nSpina bifida occulta is the mildest form of neural tube defect, characterized by failure of the posterior bony vertebral arches to fuse (usually at L5-S1) while the overlying skin remains intact. The spinal cord and meninges are anatomically normal, and patients are typically asymptomatic with normal neurological examinations. Cutaneous markers such as a localized tuft of hair, skin dimple, hemangioma, or subcutaneous lipoma are common. Maternal serum AFP is normal because the defect is closed and skin-covered.\n\n• Option B is incorrect: Meningocele involves herniation of the meninges and CSF through a bony vertebral defect, forming a skin-covered or open cystic sac.\n• Option C is incorrect: Myelomeningocele involves herniation of both meninges and the spinal cord/nerve roots, resulting in motor, sensory, and sphincter deficits.\n• Option D is incorrect: Myeloschisis is a severe, completely open defect where the neural plate failed to elevate and fold, leaving exposed neural placode on the back."
    },
    {
        "id": "FZ_Q023",
        "question_number": 23,
        "category": "Central Nervous System Development",
        "stem": "A newborn delivered at 38 weeks of gestation is evaluated for a large, cystic lumbar mass that transilluminates. Examination demonstrates complete flaccid paraplegia of the lower limbs and an absent anal wink reflex. A sagittal brain MRI demonstrates downward displacement of both the cerebellar vermis and tonsils into the foramen magnum, associated with elongation of the brainstem and hydrocephalus secondary to aqueductal stenosis. Which of the following congenital malformations is present?",
        "options": [
            {"text": "Chiari I malformation", "is_correct": False},
            {"text": "Chiari II (Arnold-Chiari) malformation", "is_correct": True},
            {"text": "Dandy-Walker malformation", "is_correct": False},
            {"text": "Holoprosencephaly", "is_correct": False},
            {"text": "Lissencephaly", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. Chiari II (Arnold-Chiari) malformation.\n\nChiari II malformation is characterized by downward herniation of both the cerebellar vermis and tonsils through the foramen magnum into the upper cervical canal. This crowding obstructs CSF flow, kinking the brainstem and causing aqueductal stenosis and obstructive hydrocephalus. Chiari II malformation is almost universally associated with a lumbosacral myelomeningocele (herniation of spinal cord and meninges).\n\n• Option A is incorrect: Chiari I malformation involves herniation of cerebellar tonsils only (>5 mm below foramen magnum); it typically presents in adulthood with headaches and neck pain, and is associated with syringomyelia, NOT myelomeningocele.\n• Option C is incorrect: Dandy-Walker malformation is characterized by agenesis of the cerebellar vermis, cystic dilation of the 4th ventricle, and an enlarged posterior fossa."
    },
    {
        "id": "FZ_Q024",
        "question_number": 24,
        "category": "Central Nervous System Development",
        "stem": "An infant presents with macrocephaly, delayed developmental milestones, and spastic diplegia. Brain MRI reveals marked agenesis of the cerebellar vermis, massive cystic enlargement of the fourth ventricle filling the posterior fossa, and upward displacement of the tentorium cerebelli and torcular Herophili. Which of the following is the most likely diagnosis?",
        "options": [
            {"text": "Chiari II malformation", "is_correct": False},
            {"text": "Dandy-Walker malformation", "is_correct": True},
            {"text": "Holoprosencephaly", "is_correct": False},
            {"text": "Lissencephaly type 1", "is_correct": False},
            {"text": "Periventricular leukomalacia", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. Dandy-Walker malformation.\n\nDandy-Walker malformation is a congenital posterior fossa anomaly characterized by the classic diagnostic triad:\n1. Complete or partial agenesis of the cerebellar vermis.\n2. Cystic dilation of the fourth ventricle.\n3. Enlarged posterior cranial fossa with elevated tentorium cerebelli.\nThis malformation leads to non-communicating hydrocephalus, macrocephaly, motor delays, and cerebellar ataxia.\n\n• Option A is incorrect: Chiari II has a small, crowded posterior fossa with downward tonsillar/vermian herniation and myelomeningocele.\n• Option C is incorrect: Holoprosencephaly is failure of the forebrain to cleave.\n• Option D is incorrect: Lissencephaly ('smooth brain') is a disorder of neuronal migration."
    },
    {
        "id": "FZ_Q025",
        "question_number": 25,
        "category": "Central Nervous System Development",
        "stem": "A full-term infant is born with severe craniofacial dysmorphisms, including hypotelorism, a flat single-nostril proboscis, and a midline cleft lip and palate. Magnetic resonance imaging reveals a single, monoventricular brain without separation of the cerebral hemispheres into left and right sides. Mutations in which of the following embryological signaling pathways, or which chromosomal aneuploidy, is most strongly associated with this disorder?",
        "options": [
            {"text": "Sonic Hedgehog (SHH) signaling pathway; Trisomy 13 (Patau syndrome)", "is_correct": True},
            {"text": "Fibroblast Growth Factor Receptor 3 (FGFR3); Achondroplasia", "is_correct": False},
            {"text": "Wnt signaling pathway; Trisomy 21 (Down syndrome)", "is_correct": False},
            {"text": "Bone Morphogenetic Protein (BMP); Turner syndrome", "is_correct": False},
            {"text": "Notch-Delta signaling; Fragile X syndrome", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Sonic Hedgehog (SHH) signaling pathway; Trisomy 13 (Patau syndrome).\n\nThis infant has holoprosencephaly, caused by failure of the prosencephalon (forebrain) to cleave into two cerebral hemispheres along the midline during weeks 5 to 6 of development. It is strongly linked to mutations in the Sonic Hedgehog (SHH) pathway (which orchestrates ventral midline patterning of the brain and face) and Trisomy 13 (Patau syndrome). Phenotypes range from cyclopia and proboscis in severe forms to mild midline anomalies like a single central maxillary incisor or hypotelorism.\n\n• Option B is incorrect: FGFR3 mutations cause achondroplasia and thanatophoric dysplasia.\n• Options C and D are incorrect: Wnt and BMP regulate dorsal neural tube patterning (alar plate), not ventral prosencephalic cleavage."
    },
    {
        "id": "FZ_Q026",
        "question_number": 26,
        "category": "Central Nervous System Development",
        "stem": "During human embryological development, the primary brain vesicles subdivide into five secondary vesicles. Which of the following secondary brain vesicles gives rise to the thalamus, hypothalamus, epithalamus (pineal gland), and the optic cups/retina?",
        "options": [
            {"text": "Telencephalon", "is_correct": False},
            {"text": "Diencephalon", "is_correct": True},
            {"text": "Mesencephalon", "is_correct": False},
            {"text": "Metencephalon", "is_correct": False},
            {"text": "Myelencephalon", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. Diencephalon.\n\nEmbryological derivations of secondary brain vesicles:\n• Prosencephalon (Forebrain) divides into:\n  1. Telencephalon: Cerebral hemispheres, basal ganglia, hippocampus, lateral ventricles.\n  2. Diencephalon: Thalamus, hypothalamus, epithalamus (pineal gland), optic vesicles/retina, neurohypophysis, 3rd ventricle.\n• Mesencephalon (Midbrain): Midbrain, cerebral aqueduct of Sylvius.\n• Rhombencephalon (Hindbrain) divides into:\n  1. Metencephalon: Pons, cerebellum, upper 4th ventricle.\n  2. Myelencephalon: Medulla oblongata, lower 4th ventricle."
    },
    {
        "id": "FZ_Q027",
        "question_number": 27,
        "category": "Central Nervous System Development",
        "stem": "Neural crest cells represent a pluripotent population of migratory cells that originate at the margins of the neural folds. Which of the following groups of cells or tissues is entirely derived from neural crest cells?",
        "options": [
            {"text": "Ventral horn motor neurons and astrocytes", "is_correct": False},
            {"text": "Oligodendrocytes and ependymal cells", "is_correct": False},
            {"text": "Dorsal root ganglia, Schwann cells, and adrenal chromaffin cells", "is_correct": True},
            {"text": "Microglia and cerebellar Purkinje cells", "is_correct": False},
            {"text": "Pyramidal neurons of the cerebral cortex", "is_correct": False}
        ],
        "explanation": "Correct Answer: C. Dorsal root ganglia, Schwann cells, and adrenal chromaffin cells.\n\nNeural crest derivatives include ('MOTEL PASS'):\n• Melanocytes\n• Odontoblasts\n• Tracheal cartilage\n• Enterochromaffin cells\n• Laryngeal cartilage\n• Parafollicular (C) cells of thyroid\n• Adrenal medulla (chromaffin cells)\n• Schwann cells\n• Spiral (aorticopulmonary) septum\n• Sympathetic chain, dorsal root ganglia, cranial nerve sensory ganglia, and arachnoid/pia mater.\n\n• Options A, B, and E are incorrect: Ventral horn motor neurons, cortical pyramidal neurons, oligodendrocytes, ependymal cells, and astrocytes are derived from the neuroectoderm of the neural tube.\n• Option D is incorrect: Microglia are mesodermal in origin (monocyte/macrophage lineage)."
    },
    {
        "id": "FZ_Q028",
        "question_number": 28,
        "category": "Central Nervous System Development",
        "stem": "Public health agencies recommend periconceptional supplementation with 400 mcg of folic acid daily for all women of childbearing age to prevent neural tube defects. At the biochemical level, folate is converted to tetrahydrofolate (THF), which serves as an essential cofactor for which of the following metabolic pathways required for rapid neuroepithelial cell division during primary neurulation?",
        "options": [
            {"text": "One-carbon transfer for purine and thymidylate (dTMP) synthesis", "is_correct": True},
            {"text": "Fatty acid beta-oxidation in the mitochondrial matrix", "is_correct": False},
            {"text": "Oxidative phosphorylation via complex IV of the electron transport chain", "is_correct": False},
            {"text": "Glycogen breakdown via glycogen phosphorylase", "is_correct": False},
            {"text": "Conversion of dopamine to norepinephrine via dopamine beta-hydroxylase", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. One-carbon transfer for purine and thymidylate (dTMP) synthesis.\n\nFolic acid (vitamin B9) is reduced to tetrahydrofolate (THF), which acts as a carrier of one-carbon units necessary for the de novo synthesis of purines and thymidylate (dTMP via thymidylate synthase). Rapidly proliferating neuroepithelial cells during the 3rd and 4th weeks of embryogenesis depend on high rates of DNA replication for neural fold elevation, apposition, and fusion. Folate deficiency impairs DNA synthesis, arresting neurulation and resulting in anencephaly or spina bifida."
    },
    {
        "id": "FZ_Q029",
        "question_number": 29,
        "category": "Central Nervous System Development",
        "stem": "A 26-year-old woman presents with suboccipital headaches exacerbated by coughing and bending forward. Neurological examination reveals bilateral loss of pain and temperature sensation in a 'cape-like' distribution across her neck and shoulders, while vibratory sensation and motor strength in her arms remain intact. A cervical spine MRI demonstrates a fluid-filled cavity (syrinx) within the central cord and herniation of the cerebellar tonsils 8 mm below the foramen magnum. Which of the following is the most likely diagnosis?",
        "options": [
            {"text": "Chiari I malformation with syringomyelia", "is_correct": True},
            {"text": "Chiari II malformation with myelomeningocele", "is_correct": False},
            {"text": "Dandy-Walker malformation", "is_correct": False},
            {"text": "Normal pressure hydrocephalus", "is_correct": False},
            {"text": "Holoprosencephaly", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Chiari I malformation with syringomyelia.\n\nChiari I malformation is defined by downward displacement of the cerebellar tonsils alone (>5 mm below the foramen magnum). It often remains asymptomatic until early adulthood, presenting with suboccipital cough-induced headaches and cerebellar ataxia. Over 50% of cases are associated with syringomyelia (a fluid-filled cavity within the central spinal canal, most commonly cervical). The syrinx selectively compresses the decussating fibers of the anterior white commissure, producing bilateral loss of pain and temperature in a 'cape-like' dermatomal distribution while sparing dorsal column touch/vibration.\n\n• Option B is incorrect: Chiari II involves both tonsils and vermis herniation and is linked to lumbosacral myelomeningocele in infants."
    },
    {
        "id": "FZ_Q030",
        "question_number": 30,
        "category": "Central Nervous System Development",
        "stem": "An infant with profound developmental delay and intractable infantile spasms undergoes neuroimaging. The MRI reveals a completely smooth cerebral surface lacking normal sulci and gyri (agyria), along with a markedly thickened, four-layered cerebral cortex. Disruption of which of the following cellular processes during gestational weeks 12 to 24 is responsible for this condition (lissencephaly)?",
        "options": [
            {"text": "Closure of the rostral neuropore", "is_correct": False},
            {"text": "Radial migration of neuroblasts along radial glial scaffolds", "is_correct": True},
            {"text": "Differentiation of the alar plate into the dorsal horn", "is_correct": False},
            {"text": "Myelination of peripheral nerves by Schwann cells", "is_correct": False},
            {"text": "Apoptosis of redundant motor neurons in the ventral horn", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. Radial migration of neuroblasts along radial glial scaffolds.\n\nLissencephaly ('smooth brain') is a severe malformation of cortical development caused by arrest of neuronal radial migration between weeks 12 and 24 of gestation. Developing neuroblasts generated in the periventricular germinal zone normally migrate outward toward the pial surface along radial glial fibers to form the normal 6-layered neocortex ('inside-out' development). Genetic mutations in microtubule-associated proteins (e.g., LIS1, DCX/doublecortin) disrupt radial migration, producing a smooth cortex lacking gyri and a disorganized 4-layered cortex."
    },
    {
        "id": "FZ_Q031",
        "question_number": 31,
        "category": "Central Nervous System Development",
        "stem": "In the developing spinal cord, the longitudinal groove known as the sulcus limitans divides the mantle zone into two functional regions: the dorsolateral alar plate and the ventrolateral basal plate. Which of the following adult spinal cord structures develops directly from the alar plate under the influence of Bone Morphogenetic Proteins (BMPs)?",
        "options": [
            {"text": "Somatic motor neurons of the ventral horn", "is_correct": False},
            {"text": "Autonomic motor neurons of the intermediolateral horn (T1-L2)", "is_correct": False},
            {"text": "Sensory relay neurons and interneurons of the dorsal horn", "is_correct": True},
            {"text": "Dorsal root ganglion sensory cell bodies", "is_correct": False},
            {"text": "Skeletal muscle myocytes", "is_correct": False}
        ],
        "explanation": "Correct Answer: C. Sensory relay neurons and interneurons of the dorsal horn.\n\nThe sulcus limitans separates the developing mantle layer into:\n• Alar plate (dorsal): Regulated by dorsal signaling molecules (BMPs and Wnt); gives rise to sensory neurons and interneurons of the dorsal horn.\n• Basal plate (ventral): Regulated by ventral signaling from the notochord and floor plate (Sonic Hedgehog / SHH); gives rise to somatic motor neurons (ventral horn) and sympathetic visceral motor neurons (intermediolateral horn).\n\n• Option D is incorrect: Dorsal root ganglion cell bodies arise from neural crest cells, not the alar plate of the neural tube."
    },
    {
        "id": "FZ_Q032",
        "question_number": 32,
        "category": "Central Nervous System Development",
        "stem": "A newborn is delivered with microcephaly, sensorineural deafness, dense bilateral cataracts, and a harsh continuous machine-like murmur heard best at the left infraclavicular area (patent ductus arteriosus). The mother had an unimmunized pregnancy complicated by a low-grade fever and a fine pink maculopapular rash during the first trimester. Which of the following infectious agents is responsible for this congenital constellation?",
        "options": [
            {"text": "Toxoplasma gondii", "is_correct": False},
            {"text": "Cytomegalovirus (CMV)", "is_correct": False},
            {"text": "Rubella virus", "is_correct": True},
            {"text": "Herpes simplex virus 2 (HSV-2)", "is_correct": False},
            {"text": "Zika virus", "is_correct": False}
        ],
        "explanation": "Correct Answer: C. Rubella virus.\n\nCongenital rubella syndrome produces the classic clinical triad of:\n1. Sensorineural deafness (most common)\n2. Ocular defects (cataracts, retinopathy, microphthalmia)\n3. Cardiac anomalies (patent ductus arteriosus [PDA], pulmonary artery stenosis)\nInfected infants may also exhibit microcephaly, developmental delay, and purpuric 'blueberry muffin' skin lesions.\n\n• Option A is incorrect: Congenital Toxoplasmosis triad is chorioretinitis, hydrocephalus, and diffuse intracranial calcifications.\n• Option B is incorrect: Congenital CMV manifests with periventricular calcifications, sensorineural hearing loss, and petechiae."
    },
    {
        "id": "FZ_Q033",
        "question_number": 33,
        "category": "Central Nervous System Development",
        "stem": "Anatomists observe that in an 8-week-old human fetus, the spinal cord extends throughout the entire length of the vertebral canal, with coccygeal nerves exiting horizontally. However, in a normal adult, the spinal cord terminates at the L1-L2 vertebral level as the conus medullaris. Which of the following developmental mechanisms accounts for this apparent rostral 'ascent' of the spinal cord?",
        "options": [
            {"text": "Apoptosis and resorption of the distal five sacral spinal cord segments", "is_correct": False},
            {"text": "Differential elongation of the bony vertebral column relative to the spinal cord", "is_correct": True},
            {"text": "Upward traction exerted by the enlarging cerebellum and brainstem", "is_correct": False},
            {"text": "Failure of caudal neuropore closure leading to cord shortening", "is_correct": False},
            {"text": "Involution of the dural sac below the thoracic level", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. Differential elongation of the bony vertebral column relative to the spinal cord.\n\nDuring embryogenesis, the spinal cord and vertebral column are initially of equal length. During later fetal development and childhood, the bony vertebral column and dura mater grow much more rapidly than the spinal cord. Consequently, the caudal tip of the spinal cord (conus medullaris) shifts relatively rostrally: ending at the L3 level at birth and at the L1-L2 vertebral disc space in adults. This differential growth pulls the lumbar and sacral nerve roots into an elongated sheaf of roots (the cauda equina) within the lumbar cistern."
    },
    {
        "id": "FZ_Q034",
        "question_number": 34,
        "category": "Central Nervous System Development",
        "stem": "A 9-month-old infant of Ashkenazi Jewish descent is brought to the clinic for developmental regression. Over the past 3 months, he has lost the ability to sit up and roll over. On examination, he exhibits generalized hypotonia, hyperacusis (exaggerated startle response to sound), and a bright cherry-red spot in the macula of both eyes. The liver and spleen are not palpable. A deficiency of which of the following lysosomal enzymes, and accumulation of which substrate, explains this condition?",
        "options": [
            {"text": "Sphingomyelinase; Sphingomyelin", "is_correct": False},
            {"text": "Hexosaminidase A; GM2 ganglioside", "is_correct": True},
            {"text": "Glucocerebrosidase; Glucocerebroside", "is_correct": False},
            {"text": "Galactocerebrosidase; Galactocerebroside", "is_correct": False},
            {"text": "Arylsulfatase A; Cerebroside sulfate", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. Hexosaminidase A; GM2 ganglioside.\n\nTay-Sachs disease is an autosomal recessive lysosomal storage disease caused by a deficiency of Hexosaminidase A, leading to toxic accumulation of GM2 ganglioside in neuronal lysosomes (demonstrating characteristic 'onion-skin' lamellar lysosomal inclusions on electron microscopy). Clinical hallmarks:\n• Progressive neurodegeneration and loss of motor milestones\n• Hyperacusis (exaggerated acoustic startle response)\n• Macular cherry-red spot (caused by lipid accumulation in retinal ganglion cells surrounding the fovea)\n• ABSENCE of hepatosplenomegaly (distinguishing it from Niemann-Pick disease).\n\n• Option A is incorrect: Niemann-Pick disease is caused by sphingomyelinase deficiency and presents with a macular cherry-red spot PLUS hepatosplenomegaly and foam cells on histology."
    },
    {
        "id": "FZ_Q035",
        "question_number": 35,
        "category": "Central Nervous System Development",
        "stem": "A 10-month-old child presents with progressive motor regression and failure to thrive. Physical examination reveals massive hepatosplenomegaly, severe hypotonia, and a cherry-red macular spot on fundoscopic examination. Bone marrow biopsy demonstrates lipid-laden foamy histiocytes. Which of the following lysosomal storage enzymes is deficient in this patient?",
        "options": [
            {"text": "Sphingomyelinase (Niemann-Pick disease)", "is_correct": True},
            {"text": "Hexosaminidase A (Tay-Sachs disease)", "is_correct": False},
            {"text": "Glucocerebrosidase (Gaucher disease)", "is_correct": False},
            {"text": "Alpha-L-iduronidase (Hurler syndrome)", "is_correct": False},
            {"text": "Galactocerebrosidase (Krabbe disease)", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Sphingomyelinase (Niemann-Pick disease).\n\nNiemann-Pick disease (Type A) is an autosomal recessive lysosomal storage disease caused by deficiency of acid sphingomyelinase, resulting in accumulation of sphingomyelin. It presents in infancy with:\n• Neurodegeneration and loss of motor skills\n• Macular cherry-red spot\n• Massive hepatosplenomegaly (due to reticuloendothelial accumulation)\n• Foam cells (lipid-laden foamy macrophages) on bone marrow biopsy.\nThis is distinguished from Tay-Sachs disease by the presence of prominent hepatosplenomegaly.\n\n• Option C is incorrect: Gaucher disease features hepatosplenomegaly and bone crises with crumpled tissue-paper macrophages, but NO cherry-red spot."
    },
    {
        "id": "FZ_Q036",
        "question_number": 36,
        "category": "Central Nervous System Development",
        "stem": "A 5-year-old boy presents with progressive bone pain, recurrent fractures, and pancytopenia. Abdominal examination reveals marked splenomegaly. Bone marrow aspirate reveals numerous enlarged, lipid-laden macrophages with a cytoplasm that resembles 'wrinkled tissue paper' or 'crumpled silk.' Which of the following lysosomal storage diseases is characterized by this finding?",
        "options": [
            {"text": "Gaucher disease", "is_correct": True},
            {"text": "Tay-Sachs disease", "is_correct": False},
            {"text": "Niemann-Pick disease", "is_correct": False},
            {"text": "Metachromatic leukodystrophy", "is_correct": False},
            {"text": "Krabbe disease", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Gaucher disease.\n\nGaucher disease is the most common lysosomal storage disease, caused by an autosomal recessive deficiency of beta-glucocerebrosidase (acid beta-glucosidase), leading to accumulation of glucocerebroside. Clinical features:\n• Hepatosplenomegaly (painless, massive)\n• Pancytopenia (anemia, thrombocytopenia) due to splenic sequestration and marrow infiltration\n• Bone crises, osteonecrosis of the femoral head, and Erlenmeyer flask bone deformities\n• Histopathology: Gaucher cells, which are lipid-laden macrophages with striated cytoplasm resembling 'wrinkled tissue paper' or 'crumpled silk.'\n\n• Option D is incorrect: Metachromatic leukodystrophy is caused by arylsulfatase A deficiency, resulting in central/peripheral demyelination without bone crises.\n• Option E is incorrect: Krabbe disease features galactocerebrosidase deficiency and globoid cells."
    },
    {
        "id": "FZ_Q037",
        "question_number": 37,
        "category": "Central Nervous System Development",
        "stem": "A 1-year-old child presents with progressive spasticity, irritability, optic atrophy, and loss of developmental milestones. Brain MRI demonstrates diffuse, symmetrical loss of myelin in the cerebral white matter. Brain biopsy reveals globoid, multinucleated cells clustered in perivascular spaces of the white matter. Deficiency of which of the following enzymes is responsible for Krabbe disease?",
        "options": [
            {"text": "Galactocerebrosidase (galactosylceramidase)", "is_correct": True},
            {"text": "Arylsulfatase A", "is_correct": False},
            {"text": "Alpha-galactosidase A", "is_correct": False},
            {"text": "Sphingomyelinase", "is_correct": False},
            {"text": "Hexosaminidase B", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Galactocerebrosidase (galactosylceramidase).\n\nKrabbe disease (globoid cell leukodystrophy) is an autosomal recessive lysosomal storage disease caused by deficiency of galactocerebrosidase (galactosylceramidase), resulting in the accumulation of galactocerebroside and toxic psychosine in oligodendrocytes. Pathological hallmark:\n• Destruction of myelin (severe dysmyelinating leukodystrophy)\n• Accumulation of multinucleated, phagocytic 'globoid cells' surrounding blood vessels in white matter\n• Clinical features: progressive peripheral neuropathy, spasticity, optic atrophy, developmental arrest, and death by age 2.\n\n• Option B is incorrect: Arylsulfatase A deficiency causes metachromatic leukodystrophy (cerebroside sulfate accumulation).\n• Option C is incorrect: Alpha-galactosidase A deficiency causes Fabry disease (angiokeratomas, neuropathic pain, renal/cardiac failure)."
    },
    {
        "id": "FZ_Q038",
        "question_number": 38,
        "category": "Central Nervous System Development",
        "stem": "A 4-year-old boy presents with progressive difficulty walking, frequent falls, and cognitive decline. Nerve conduction studies demonstrate markedly slowed motor conduction velocities consistent with demyelinating sensorimotor polyneuropathy. Sural nerve biopsy reveals brown-staining metachromatic granules within Schwann cells and macrophages when stained with cresyl violet or toluidine blue. Deficiency of which of the following enzymes causes this condition?",
        "options": [
            {"text": "Arylsulfatase A", "is_correct": True},
            {"text": "Hexosaminidase A", "is_correct": False},
            {"text": "Alpha-L-iduronidase", "is_correct": False},
            {"text": "Iduronate-2-sulfatase", "is_correct": False},
            {"text": "Sphingomyelinase", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Arylsulfatase A.\n\nMetachromatic leukodystrophy is an autosomal recessive lysosomal storage disorder caused by deficiency of arylsulfatase A, resulting in the toxic accumulation of sulfatides (galactosyl sulfatide / cerebroside sulfate) in oligodendrocytes and Schwann cells. This causes diffuse central and peripheral demyelination, leading to progressive ataxia, spasticity, and dementia. Sulfatides shift the absorption spectrum of dyes such as cresyl violet, producing characteristic brown-gold 'metachromasia' on histological staining.\n\n• Options C and D are incorrect: Mucopolysaccharidoses (Hurler and Hunter syndromes) involve alpha-L-iduronidase and iduronate-2-sulfatase, accumulating heparan and dermatan sulfate."
    },
    {
        "id": "FZ_Q039",
        "question_number": 39,
        "category": "Central Nervous System Development",
        "stem": "A newborn with micrognathia, low-set ears, and a cleft palate develops hypocalcemic tetany on day 2 of life. Echocardiogram demonstrates tetralogy of Fallot. Flow cytometry reveals an absolute absence of mature T lymphocytes. This patient's syndrome (DiGeorge syndrome, 22q11.2 deletion) results from defective migration of which of the following embryological cell types into the third and fourth pharyngeal pouches?",
        "options": [
            {"text": "Neural crest cells", "is_correct": True},
            {"text": "Endodermal epithelial cells", "is_correct": False},
            {"text": "Lateral plate mesoderm", "is_correct": False},
            {"text": "Paraxial somites", "is_correct": False},
            {"text": "Neuroepithelial tube cells", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Neural crest cells.\n\nDiGeorge syndrome (22q11.2 deletion syndrome) results from defective migration of cranial neural crest cells into the 3rd and 4th pharyngeal pouches and pharyngeal arches. This causes:\n• Thymic aplasia: Absence of thymic shadow on chest X-ray, leading to severe T-cell immunodeficiency and recurrent viral/fungal infections.\n• Parathyroid hypoplasia: Hypocalcemia causing neonatal tetany, seizures, or carpopedal spasms.\n• Conotruncal cardiac defects: Tetralogy of Fallot, truncus arteriosus, interrupted aortic arch.\n• Craniofacial dysmorphisms: Micrognathia, low-set malformed ears, cleft palate.\n\n• Options B, C, and D are incorrect: The primary embryological defect is failure of neural crest cell migration into the pharyngeal apparatus."
    },
    {
        "id": "FZ_Q040",
        "question_number": 40,
        "category": "Central Nervous System Development",
        "stem": "A 19-year-old woman with refractory epilepsy undergoes brain MRI. The scan demonstrates multiple small, smooth, rounded nodules of gray matter lining the lateral walls of both lateral ventricles, protruding into the ventricular lumen. These ectopic gray matter nodules are isointense to normal cerebral cortex on all pulse sequences. This developmental disorder (periventricular nodular heterotopia) is caused by failure of which of the following neuroembryological processes?",
        "options": [
            {"text": "Failure of neuroblasts to initiate radial migration away from the ventricular zone", "is_correct": True},
            {"text": "Failure of anterior neuropore closure during primary neurulation", "is_correct": False},
            {"text": "Defective cleavage of the embryonic telencephalon along the midline", "is_correct": False},
            {"text": "Excessive apoptosis of neuroblasts in the subplate zone", "is_correct": False},
            {"text": "Failure of secondary neurulation in the caudal eminence", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Failure of neuroblasts to initiate radial migration away from the ventricular zone.\n\nPeriventricular nodular heterotopia (often X-linked dominant due to mutations in the filamin A / FLNA gene) is a disorder of neuronal migration. During cortical development, neuroblasts are born in the periventricular germinal zone and must migrate radially outward along radial glial fibers to reach the cortical plate. In periventricular heterotopia, subsets of neurons fail to initiate migration and remain arrested as ectopic nodules of normal-appearing gray matter along the ventricular lining, which act as epileptogenic foci.\n\n• Option B is incorrect: Failure of neuropore closure causes anencephaly or spina bifida.\n• Option C is incorrect: Defective telencephalic cleavage causes holoprosencephaly.\n• Option E is incorrect: Defective secondary neurulation produces closed caudal spinal dysraphism."
    },

    # =========================================================================
    # TOPIC 3: Neurotransmitters and Action Potentials (FZ_Q041 - FZ_Q060)
    # =========================================================================
    {
        "id": "FZ_Q041",
        "question_number": 41,
        "category": "Neurotransmitters and Action Potentials",
        "stem": "In a resting human neuron, the resting membrane potential settles at approximately -70 mV. While the electrogenic Na+/K+ ATPase pumps 3 Na+ ions out of the cell for every 2 K+ ions pumped in, which of the following membrane channels is the primary determinant of this resting negative electrical potential?",
        "options": [
            {"text": "Voltage-gated sodium channels", "is_correct": False},
            {"text": "Non-gated (constitutively open) potassium leak channels", "is_correct": True},
            {"text": "Ligand-gated nicotinic acetylcholine channels", "is_correct": False},
            {"text": "Voltage-gated L-type calcium channels", "is_correct": False},
            {"text": "GABA-A chloride channels", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. Non-gated (constitutively open) potassium leak channels.\n\nThe resting membrane potential of a neuron (typically -70 mV) is primarily determined by high resting membrane permeability to K+ ions via constitutively open, non-gated K+ leak channels (such as two-pore domain K2P channels). Because the resting membrane is approximately 25 to 100 times more permeable to K+ than to Na+, the membrane potential settles close to the equilibrium potential for potassium (EK ≈ -90 mV), as predicted by the Goldman-Hodgkin-Katz equation. The Na+/K+ ATPase maintains the chemical concentration gradients.\n\n• Option A is incorrect: Voltage-gated Na+ channels open during the rapid depolarizing phase of the action potential.\n• Option C is incorrect: Nicotinic channels open only in the presence of acetylcholine."
    },
    {
        "id": "FZ_Q042",
        "question_number": 42,
        "category": "Neurotransmitters and Action Potentials",
        "stem": "A 32-year-old traveler consumes fugu (pufferfish) at an unlicensed coastal market. Within 45 minutes, he experiences intense perioral paresthesias, numbness of the tongue, nausea, and ascending flaccid paralysis of his limbs. Physical examination reveals intact mental status, absent deep tendon reflexes, and shallow respirations. Tetrodotoxin is confirmed as the causative agent. By which of the following molecular mechanisms does this toxin prevent action potential generation?",
        "options": [
            {"text": "Selective blockade of voltage-gated sodium channels", "is_correct": True},
            {"text": "Inhibition of delayed rectifier voltage-gated potassium channels", "is_correct": False},
            {"text": "Blockade of presynaptic P/Q-type voltage-gated calcium channels", "is_correct": False},
            {"text": "Cleavage of the SNARE protein synaptobrevin", "is_correct": False},
            {"text": "Irreversible inhibition of acetylcholinesterase", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Selective blockade of voltage-gated sodium channels.\n\nTetrodotoxin (found in pufferfish/fugu) and saxitoxin (found in 'red tide' dinoflagellates) bind with nanomolar affinity to site 1 on the extracellular pore of voltage-gated Na+ channels (Nav) in nerves and skeletal muscle. This physically blocks Na+ influx, completely arresting action potential upstroke and conduction. Patients experience perioral tingling, motor weakness, hyporeflexia, and death from respiratory paralysis, with completely preserved consciousness.\n\n• Option B is incorrect: K+ channel blockers (e.g., 4-aminopyridine, tetraethylammonium) prolong action potential duration.\n• Option C is incorrect: P/Q-type Ca2+ channels are blocked by Lambert-Eaton autoantibodies or omega-agatoxin.\n• Option D is incorrect: Synaptobrevin is cleaved by tetanus toxin and botulinum toxin B, D, F, G."
    },
    {
        "id": "FZ_Q043",
        "question_number": 43,
        "category": "Neurotransmitters and Action Potentials",
        "stem": "During the repolarization phase of a neuronal action potential, an axon cannot generate another action potential regardless of the strength or duration of the depolarizing electrical stimulus. Which of the following states of the voltage-gated sodium channel is responsible for this absolute refractory period?",
        "options": [
            {"text": "Activation (m) gates are closed, inactivation (h) gates are open", "is_correct": False},
            {"text": "Activation (m) gates are open, inactivation (h) gates are open", "is_correct": False},
            {"text": "Inactivation (h) gates are closed", "is_correct": True},
            {"text": "Voltage-gated potassium channels are deactivated", "is_correct": False},
            {"text": "Sodium/potassium ATPase is dephosphorylated", "is_correct": False}
        ],
        "explanation": "Correct Answer: C. Inactivation (h) gates are closed.\n\nVoltage-gated Na+ channels exist in three functional states controlled by two distinct gates:\n1. Resting (closed): Activation (m) gate is closed; inactivation (h) gate is open. The channel is closed but excitable.\n2. Activated (open): Both m and h gates are open. Occurs upon depolarization to threshold.\n3. Inactivated: The slow inactivation (h) gate closes shortly after depolarization. Because the h gate is closed, the channel cannot be opened by any depolarizing stimulus. This state defines the absolute refractory period. The channel must repolarize toward resting potential to reset ('de-inactivate') the h gate before it can open again."
    },
    {
        "id": "FZ_Q044",
        "question_number": 44,
        "category": "Neurotransmitters and Action Potentials",
        "stem": "A 45-year-old dentist prepares to perform an incision and drainage on a tense, acidic mandibular abscess. She injects 2% lidocaine locally around the inflamed tissue. However, despite adequate dosing, the patient continues to experience sharp pain during the incision. Which of the following physicochemical properties explains why local anesthetics have markedly reduced efficacy in infected, inflamed tissues?",
        "options": [
            {"text": "Low extracellular pH shifts the anesthetic to its uncharged lipophilic form, speeding its entry", "is_correct": False},
            {"text": "Low extracellular pH shifts the anesthetic to its charged (protonated) hydrophilic form, impairing membrane penetration", "is_correct": True},
            {"text": "Inflammation activates tissue esterases that instantly degrade all amide local anesthetics", "is_correct": False},
            {"text": "Acidosis irreversibly blocks the intracellular binding site of voltage-gated sodium channels", "is_correct": False},
            {"text": "Vasoconstriction caused by acidosis rapidly washes the anesthetic out of the tissue", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. Low extracellular pH shifts the anesthetic to its charged (protonated) hydrophilic form, impairing membrane penetration.\n\nLocal anesthetics are weak bases (pKa 8.0-9.0). To cross the neuronal lipid bilayer, they must exist in their uncharged, non-ionized lipophilic form (B). Once inside the axoplasm, the drug becomes protonated to its charged form (BH+), which binds to the inner pore of the voltage-gated Na+ channel to block conduction. In infected tissues, extracellular acidosis (pH < 6.0) shifts the equilibrium (Henderson-Hasselbalch equation) toward the ionized, protonated form (BH+). Because ionized molecules cannot readily diffuse across cell membranes, insufficient drug enters the axon, leading to failed anesthesia.\n\n• Option A is incorrect: Acidic pH protonates the base, increasing the charged fraction, not the uncharged fraction.\n• Option C is incorrect: Amide anesthetics are metabolized by hepatic CYP450 enzymes, not tissue esterases."
    },
    {
        "id": "FZ_Q045",
        "question_number": 45,
        "category": "Neurotransmitters and Action Potentials",
        "stem": "A 38-year-old woman with chronic tuberculosis is prescribed an antimicrobial regimen including isoniazid. Four weeks into therapy, she develops recurrent generalized tonic-clonic seizures that are refractory to standard anticonvulsant therapy. Laboratory evaluation confirms marked deficiency of active pyridoxal phosphate (vitamin B6). The patient's neuronal hyperexcitability and seizures result from impaired synthesis of which of the following inhibitory neurotransmitters?",
        "options": [
            {"text": "Glycine", "is_correct": False},
            {"text": "Gamma-aminobutyric acid (GABA)", "is_correct": True},
            {"text": "Glutamate", "is_correct": False},
            {"text": "Dopamine", "is_correct": False},
            {"text": "Serotonin", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. Gamma-aminobutyric acid (GABA).\n\nGABA is the primary inhibitory neurotransmitter of the brain. It is synthesized from glutamate via the enzyme glutamic acid decarboxylase (GAD), which strictly requires pyridoxal phosphate (PLP, the active form of vitamin B6) as a cofactor. Isoniazid inhibits pyridoxine phosphokinase and forms inactive complexes with pyridoxine, depleting B6. Reduced GAD activity decreases brain GABA levels, leading to loss of central inhibition, neuronal hyperexcitability, and refractory seizures (treated with IV pyridoxine).\n\n• Option A is incorrect: Glycine is the primary inhibitory neurotransmitter in the spinal cord, synthesized from serine.\n• Option C is incorrect: Glutamate is excitatory; its synthesis does not depend on GAD."
    },
    {
        "id": "FZ_Q046",
        "question_number": 46,
        "category": "Neurotransmitters and Action Potentials",
        "stem": "A 24-year-old man presents to the emergency department with acute severe panic and agitation. He is administered IV lorazepam. Within minutes, his anxiety resolves and he becomes calm and drowsy. Lorazepam binds allosterically to the GABA-A receptor complex. Which of the following biophysical actions directly mediates the inhibitory effect of benzodiazepines?",
        "options": [
            {"text": "Increases the duration of chloride channel opening", "is_correct": False},
            {"text": "Increases the frequency of chloride channel opening", "is_correct": True},
            {"text": "Directly gates the open state of the channel in the complete absence of GABA", "is_correct": False},
            {"text": "Promotes potassium efflux via Gi-protein-coupled metabotropic receptors", "is_correct": False},
            {"text": "Blocks presynaptic reuptake of GABA via GAT-1 transporters", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. Increases the frequency of chloride channel opening.\n\nThe GABA-A receptor is an ionotropic, ligand-gated chloride channel composed of five subunits. \n• Benzodiazepines (e.g., lorazepam, diazepam) bind to an allosteric regulatory site and facilitate GABA binding, increasing the FREQUENCY of chloride channel opening in the presence of GABA ('Frenzodiazepines'). Influx of Cl- hyperpolarizes the membrane, inhibiting action potential generation.\n• Barbiturates (e.g., phenobarbital), in contrast, increase the DURATION of chloride channel opening ('BarbiDURATes') and at high doses can directly open the channel even without GABA, explaining their higher risk of fatal respiratory depression.\n\n• Option D is incorrect: Potassium efflux via Gi is mediated by GABA-B metabotropic receptors (e.g., baclofen)."
    },
    {
        "id": "FZ_Q047",
        "question_number": 47,
        "category": "Neurotransmitters and Action Potentials",
        "stem": "A neurobiologist studying hippocampal synaptic plasticity observes that low-frequency stimulation produces basal transmission, whereas high-frequency tetanic stimulation triggers long-term potentiation (LTP). LTP induction strictly requires the removal of an extracellular magnesium ion (Mg2+) that physically blocks which of the following postsynaptic glutamate receptors at resting membrane potentials?",
        "options": [
            {"text": "AMPA receptor", "is_correct": False},
            {"text": "Kainate receptor", "is_correct": False},
            {"text": "NMDA receptor", "is_correct": True},
            {"text": "Group I metabotropic glutamate receptor (mGluR1)", "is_correct": False},
            {"text": "GABA-B receptor", "is_correct": False}
        ],
        "explanation": "Correct Answer: C. NMDA receptor.\n\nThe NMDA (N-methyl-D-aspartate) receptor is a ligand-gated, calcium-permeable ionotropic glutamate receptor. At resting membrane potentials (-70 mV), extracellular Mg2+ physically blocks the channel pore. When adjacent AMPA receptors are activated by glutamate, the resulting Na+ influx depolarizes the postsynaptic membrane. This membrane depolarization expels the Mg2+ plug ('voltage-dependent unblock'). Glutamate and its co-agonist glycine can then open the unblocked NMDA channel, allowing high Ca2+ influx that activates CaMKII and PKC, leading to AMPA receptor insertion and long-term potentiation (LTP).\n\n• Option A is incorrect: AMPA receptors are non-selective cation channels (Na+/K+) that are not blocked by Mg2+ at resting potentials."
    },
    {
        "id": "FZ_Q048",
        "question_number": 48,
        "category": "Neurotransmitters and Action Potentials",
        "stem": "A 50-year-old woman with severe depression refractory to multiple medications is started on the non-selective monoamine oxidase inhibitor (MAOI) tranylcypromine. Two weeks later, she attends a wine and cheese party and consumes aged cheddar and chianti. Within 45 minutes, she develops a severe occipital throbbing headache, palpitations, and a blood pressure of 210/120 mmHg. Tyramine accumulation induced massive displacement and release of which of the following neurotransmitters?",
        "options": [
            {"text": "Serotonin", "is_correct": False},
            {"text": "Norepinephrine", "is_correct": True},
            {"text": "Acetylcholine", "is_correct": False},
            {"text": "GABA", "is_correct": False},
            {"text": "Glycine", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. Norepinephrine.\n\nThis patient is experiencing the 'cheese reaction' (hypertensive crisis) caused by combining a non-selective MAOI with tyramine-rich foods (aged cheeses, red wine, cured meats). Dietary tyramine is normally degraded by intestinal and hepatic monoamine oxidase A (MAO-A). When MAO-A is inhibited, tyramine enters the systemic circulation and is transported into sympathetic nerve terminals via the norepinephrine transporter (NET). Tyramine displaces stored norepinephrine from synaptic vesicles into the synaptic cleft, resulting in massive stimulation of alpha-1 and beta-1 adrenergic receptors, causing severe vasoconstriction and hypertensive crisis.\n\n• Option A is incorrect: Combining MAOIs with serotonergic drugs (SSRIs, tramadol) causes Serotonin Syndrome, but tyramine specifically displaces stored catecholamines (norepinephrine)."
    },
    {
        "id": "FZ_Q049",
        "question_number": 49,
        "category": "Neurotransmitters and Action Potentials",
        "stem": "In the biosynthetic pathway of catecholamines in the central nervous system, what is the rate-limiting enzyme responsible for converting L-tyrosine into L-DOPA, and which essential cofactor does it require?",
        "options": [
            {"text": "DOPA decarboxylase; Pyridoxal phosphate (Vitamin B6)", "is_correct": False},
            {"text": "Tyrosine hydroxylase; Tetrahydrobiopterin (BH4)", "is_correct": True},
            {"text": "Dopamine beta-hydroxylase; Ascorbic acid (Vitamin C)", "is_correct": False},
            {"text": "Phenylethanolamine N-methyltransferase (PNMT); S-adenosylmethionine (SAM)", "is_correct": False},
            {"text": "Tryptophan hydroxylase; Tetrahydrofolate (THF)", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. Tyrosine hydroxylase; Tetrahydrobiopterin (BH4).\n\nCatecholamine synthesis pathway:\n1. Tyrosine → L-DOPA via Tyrosine hydroxylase (RATE-LIMITING step; requires tetrahydrobiopterin / BH4 and molecular oxygen).\n2. L-DOPA → Dopamine via DOPA decarboxylase (requires vitamin B6 / pyridoxal phosphate).\n3. Dopamine → Norepinephrine via Dopamine beta-hydroxylase (requires vitamin C / ascorbic acid and copper).\n4. Norepinephrine → Epinephrine via PNMT (requires SAM; stimulated by cortisol in adrenal medulla).\n\n• Option A is incorrect: DOPA decarboxylase is downstream and is not rate-limiting.\n• Option C is incorrect: Dopamine beta-hydroxylase converts dopamine to norepinephrine."
    },
    {
        "id": "FZ_Q050",
        "question_number": 50,
        "category": "Neurotransmitters and Action Potentials",
        "stem": "A 28-year-old woman presents to the clinic with severe mood disturbances, sleep dysregulation, and impulsive behavior. Neurological evaluation highlights the role of serotonergic pathways in modulating mood and affect. Where are the primary cell bodies of serotonin-producing projection neurons in the central nervous system concentrated, and what amino acid is the initial precursor?",
        "options": [
            {"text": "Locus coeruleus in the dorsal rostral pons; Tyrosine", "is_correct": False},
            {"text": "Raphe nuclei of the brainstem; Tryptophan", "is_correct": True},
            {"text": "Substantia nigra pars compacta; Phenylalanine", "is_correct": False},
            {"text": "Nucleus basalis of Meynert; Choline", "is_correct": False},
            {"text": "Tuberomammillary nucleus of the hypothalamus; Histidine", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. Raphe nuclei of the brainstem; Tryptophan.\n\nSerotonin (5-hydroxytryptamine / 5-HT) is synthesized predominantly in the median and dorsal raphe nuclei located throughout the brainstem (midbrain, pons, and medulla). The biosynthetic precursor is the essential amino acid tryptophan:\n1. Tryptophan → 5-hydroxytryptophan via Tryptophan hydroxylase (rate-limiting, requires BH4).\n2. 5-hydroxytryptophan → Serotonin via Aromatic L-amino acid decarboxylase (requires vitamin B6).\n\n• Option A is incorrect: The locus coeruleus synthesizes norepinephrine from tyrosine.\n• Option C is incorrect: The substantia nigra synthesizes dopamine.\n• Option D is incorrect: The nucleus basalis of Meynert synthesizes acetylcholine."
    },
    {
        "id": "FZ_Q051",
        "question_number": 51,
        "category": "Neurotransmitters and Action Potentials",
        "stem": "An elderly patient with memory impairment is diagnosed with Alzheimer disease and started on donepezil. Post-mortem studies of Alzheimer disease consistently demonstrate a marked loss of cholinergic projection neurons in the basal forebrain that normally project diffusely to the neocortex and hippocampus. Degeneration of which of the following specific nuclei is primarily responsible for this profound central acetylcholine deficiency?",
        "options": [
            {"text": "Locus coeruleus", "is_correct": False},
            {"text": "Nucleus basalis of Meynert", "is_correct": True},
            {"text": "Ventral tegmental area (VTA)", "is_correct": False},
            {"text": "Pedunculopontine nucleus", "is_correct": False},
            {"text": "Fastigial nucleus", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. Nucleus basalis of Meynert.\n\nThe nucleus basalis of Meynert (located in the substantia innominata of the basal forebrain) provides widespread cholinergic innervation to the cerebral cortex, amygdala, and hippocampus. Profound loss of these cholinergic neurons and reduced choline acetyltransferase (ChAT) activity are consistent hallmarks of Alzheimer disease, providing the pharmacological rationale for acetylcholinesterase inhibitors (donepezil, rivastigmine, galantamine).\n\n• Option A is incorrect: The locus coeruleus is noradrenergic.\n• Option C is incorrect: The VTA is dopaminergic (mesolimbic/mesocortical pathways).\n• Option D is incorrect: The pedunculopontine nucleus regulates brainstem locomotion."
    },
    {
        "id": "FZ_Q052",
        "question_number": 52,
        "category": "Neurotransmitters and Action Potentials",
        "stem": "A 7-year-old boy steps on a rusty nail while playing in an abandoned shed. Ten days later, he develops trismus (lockjaw), painful sustained facial contractions (risus sardonicus), and involuntary back arching spasms (opisthotonos) triggered by light and noise. Tetanus toxin (tetanospasmin) produced by Clostridium tetani is suspected. By which of the following mechanisms does this toxin produce spastic paralysis?",
        "options": [
            {"text": "Cleaves synaptobrevin (VAMP) in inhibitory interneurons (Renshaw cells), preventing glycine and GABA release", "is_correct": True},
            {"text": "Cleaves SNAP-25 in somatic motor nerve terminals, preventing acetylcholine release", "is_correct": False},
            {"text": "Directly antagonizes postsynaptic nicotinic receptors on skeletal muscle endplates", "is_correct": False},
            {"text": "Blocks voltage-gated calcium channels on presynaptic autonomic nerves", "is_correct": False},
            {"text": "Inactivates acetylcholinesterase at the neuromuscular junction", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Cleaves synaptobrevin (VAMP) in inhibitory interneurons (Renshaw cells), preventing glycine and GABA release.\n\nTetanus toxin (tetanospasmin) enters motor nerve terminals and undergoes retrograde axonal transport to the spinal cord. It crosses synapses into inhibitory interneurons (Renshaw cells) in the spinal cord and brainstem. There, its zinc-metalloprotease light chain cleaves the SNARE protein synaptobrevin (VAMP-2), preventing vesicle fusion and exocytosis of the inhibitory neurotransmitters glycine and GABA. Loss of inhibitory drive disinhibits alpha motor neurons, causing uncontrolled muscle contraction, trismus, and tetanic spasms (spastic paralysis).\n\n• Option B is incorrect: Botulinum toxin (serotypes A and E) cleaves SNAP-25 in peripheral motor nerve endings, blocking ACh release and producing FLACCID paralysis."
    },
    {
        "id": "FZ_Q053",
        "question_number": 53,
        "category": "Neurotransmitters and Action Potentials",
        "stem": "During chemical synaptic transmission, the arrival of an action potential at the presynaptic nerve terminal triggers vesicle exocytosis and neurotransmitter release into the synaptic cleft. Which of the following critical intracellular events couples membrane depolarization to the fusion of synaptic vesicles with the presynaptic active zone?",
        "options": [
            {"text": "Efflux of potassium ions through delayed rectifier channels", "is_correct": False},
            {"text": "Influx of calcium ions through voltage-gated calcium channels", "is_correct": True},
            {"text": "Influx of chloride ions through ionotropic GABA channels", "is_correct": False},
            {"text": "Phosphorylation of the Na+/K+ ATPase by protein kinase A", "is_correct": False},
            {"text": "Hydrolysis of cyclic GMP by phosphodiesterase 5", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. Influx of calcium ions through voltage-gated calcium channels.\n\nWhen a depolarizing action potential reaches the presynaptic bouton, it opens presynaptic voltage-gated Ca2+ channels (P/Q-type and N-type). The resulting rapid influx of Ca2+ down its steep electrochemical gradient binds to synaptotagmin, the calcium sensor on synaptic vesicle membranes. Calcium-bound synaptotagmin interacts with SNARE core complexes (synaptobrevin, syntaxin, SNAP-25), driving vesicle fusion with the presynaptic plasma membrane and pore opening to release neurotransmitter.\n\n• Options A, C, and D are incorrect: Intracellular Ca2+ influx is the universal, obligate signal coupling electrical depolarization to synaptic vesicle exocytosis."
    },
    {
        "id": "FZ_Q054",
        "question_number": 54,
        "category": "Neurotransmitters and Action Potentials",
        "stem": "A neuropathologist examines a brain biopsy from the margin of a chronic cerebral infarct. Immunohistochemical staining demonstrates an intense proliferation of star-shaped glial cells that are strongly immunoreactive for Glial Fibrillary Acidic Protein (GFAP). Under normal physiological conditions, which of the following is a primary function of these astrocytes in the central nervous system?",
        "options": [
            {"text": "Formation of myelin sheaths around multiple central axons", "is_correct": False},
            {"text": "Buffering of extracellular potassium and uptake/recycling of synaptic glutamate", "is_correct": True},
            {"text": "Immune surveillance and phagocytosis of cellular debris", "is_correct": False},
            {"text": "Production of cerebrospinal fluid via modified choroid plexuses", "is_correct": False},
            {"text": "Conduction of saltatory action potentials", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. Buffering of extracellular potassium and uptake/recycling of synaptic glutamate.\n\nAstrocytes are the most abundant glial cells in the CNS and express GFAP intermediate filaments. Major functions include:\n1. Extracellular K+ spatial buffering to maintain neuronal excitability.\n2. Uptake of synaptic glutamate via excitatory amino acid transporters (EAATs), converting it to glutamine via glutamine synthetase (the glutamate-glutamine cycle) to prevent excitotoxicity.\n3. Induction and maintenance of the blood-brain barrier via astrocyte end-feet (podocytes).\n4. Glycogen storage and lactate provision to neurons.\n5. Formation of a 'glial scar' (astrogliosis/gliosis) following CNS injury.\n\n• Option A is incorrect: Oligodendrocytes form CNS myelin.\n• Option C is incorrect: Microglia perform phagocytosis and immune surveillance.\n• Option D is incorrect: Ependymal cells line the ventricles and form choroid plexus epithelium."
    },
    {
        "id": "FZ_Q055",
        "question_number": 55,
        "category": "Neurotransmitters and Action Potentials",
        "stem": "A 36-year-old woman with a history of HIV infection presents with progressive cognitive slowing and behavioral changes. Autopsy reveals diffuse microglial nodules and multinucleated giant cells within the subcortical white matter and basal ganglia (HIV-associated dementia). From which of the following embryological germ layers do microglial cells originate?",
        "options": [
            {"text": "Neuroectoderm of the neural tube", "is_correct": False},
            {"text": "Neural crest cells", "is_correct": False},
            {"text": "Mesoderm (mesenchymal monocyte/macrophage lineage)", "is_correct": True},
            {"text": "Surface ectoderm", "is_correct": False},
            {"text": "Endoderm", "is_correct": False}
        ],
        "explanation": "Correct Answer: C. Mesoderm (mesenchymal monocyte/macrophage lineage).\n\nUnlike all other central nervous system cells (neurons, astrocytes, oligodendrocytes, and ependymal cells, which are derived from neuroectoderm), microglia originate from the embryonic mesoderm. Specifically, they arise from primitive macrophage precursors in the yolk sac that migrate into the developing neural tube during early embryogenesis. Microglia serve as resident CNS macrophages. In HIV-associated dementia, HIV enters the brain via infected monocytes/macrophages and infects microglia, forming characteristic multinucleated giant cells.\n\n• Options A and B are incorrect: Neuroectoderm gives rise to neurons, astrocytes, oligodendrocytes, and ependyma; neural crest gives rise to Schwann cells and PNS ganglia."
    },
    {
        "id": "FZ_Q056",
        "question_number": 56,
        "category": "Neurotransmitters and Action Potentials",
        "stem": "A 29-year-old woman presents with sudden, brief, shock-like sensations radiating down her spine into her legs upon flexing her neck forward (Lhermitte sign). An MRI reveals multiple hyperintense periventricular and spinal cord lesions on T2/FLAIR sequences. Her condition is characterized by autoimmune destruction of central myelin. Which of the following glial cells produces myelin sheaths for multiple axons in the central nervous system, and what is its histological appearance?",
        "options": [
            {"text": "Schwann cell; elongated spindle-shaped nucleus", "is_correct": False},
            {"text": "Oligodendrocyte; round nucleus with clear halo ('fried egg' appearance)", "is_correct": True},
            {"text": "Astrocyte; star-shaped cell with GFAP filaments", "is_correct": False},
            {"text": "Microglia; elongated rod-shaped nucleus", "is_correct": False},
            {"text": "Ependymal cell; ciliated cuboidal-to-columnar epithelium", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. Oligodendrocyte; round nucleus with clear halo ('fried egg' appearance).\n\nOligodendrocytes are neuroectoderm-derived glial cells that produce and maintain myelin sheaths in the central nervous system. A single oligodendrocyte can extend processes to myelinate segments of up to 30 to 50 separate axons. On routine histological sections, oligodendrocytes display a rounded, dark nucleus surrounded by a clear cytoplasmic halo (often described as a 'fried egg' appearance). They are the target of autoimmune demyelination in multiple sclerosis.\n\n• Option A is incorrect: Schwann cells myelinate a single internode of a single axon in the peripheral nervous system and are derived from neural crest cells."
    },
    {
        "id": "FZ_Q057",
        "question_number": 57,
        "category": "Neurotransmitters and Action Potentials",
        "stem": "Under resting conditions, the brain consumes approximately 20% of the body's total glucose and oxygen despite representing only 2% of total body mass. During periods of prolonged fasting or starvation lasting longer than 48 to 72 hours, which of the following circulating substrates crosses the blood-brain barrier via monocarboxylate transporters to provide the majority of the brain's energy needs?",
        "options": [
            {"text": "Free fatty acids (palmitate)", "is_correct": False},
            {"text": "Ketone bodies (beta-hydroxybutyrate and acetoacetate)", "is_correct": True},
            {"text": "Branched-chain amino acids (leucine, isoleucine)", "is_correct": False},
            {"text": "Lactate from skeletal muscle glycolysis", "is_correct": False},
            {"text": "Glycerol from triglyceride hydrolysis", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. Ketone bodies (beta-hydroxybutyrate and acetoacetate).\n\nUnder normal well-fed conditions, the brain is an obligate consumer of D-glucose (transported across the BBB by GLUT1 and into neurons by GLUT3). However, during prolonged fasting or starvation (>48-72 hours), hepatic glycogen stores are depleted. The liver oxidizes fatty acids to generate ketone bodies (beta-hydroxybutyrate and acetoacetate). These water-soluble ketone bodies cross the blood-brain barrier via monocarboxylate transporters (MCT1) and are converted in neurons into acetyl-CoA, providing up to 60-70% of the brain's ATP and sparing muscle protein from gluconeogenesis.\n\n• Option A is incorrect: Long-chain free fatty acids cannot cross the blood-brain barrier in significant quantities to meet metabolic demand."
    },
    {
        "id": "FZ_Q058",
        "question_number": 58,
        "category": "Neurotransmitters and Action Potentials",
        "stem": "A 42-year-old man presents with painful muscle spasms and stiffness. Laboratory evaluation confirms the presence of high-titer autoantibodies against glutamic acid decarboxylase (anti-GAD antibodies), establishing a diagnosis of Stiff-Person syndrome. Physiologically, GAD catalyzes the decarboxylation of which of the following excitatory amino acids to produce the central nervous system's primary inhibitory neurotransmitter?",
        "options": [
            {"text": "Glutamate", "is_correct": True},
            {"text": "Aspartate", "is_correct": False},
            {"text": "Glycine", "is_correct": False},
            {"text": "Tyrosine", "is_correct": False},
            {"text": "Glutamine", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Glutamate.\n\nGlutamic acid decarboxylase (GAD) catalyzes the conversion of the excitatory neurotransmitter L-glutamate into gamma-aminobutyric acid (GABA), the major inhibitory neurotransmitter in the CNS. Autoantibodies against GAD (seen in Stiff-Person syndrome and type 1 diabetes) decrease GABA synthesis in inhibitory interneurons, leading to continuous involuntary motor unit firing, painful muscular rigidity, and spasms, particularly in axial and proximal limb muscles.\n\n• Option B is incorrect: Aspartate is an excitatory amino acid that acts on NMDA receptors.\n• Option E is incorrect: Glutamine is converted to glutamate by glutaminase in presynaptic terminals."
    },
    {
        "id": "FZ_Q059",
        "question_number": 59,
        "category": "Neurotransmitters and Action Potentials",
        "stem": "A 60-year-old man with advanced Parkinson disease is treated with a combination of carbidopa and levodopa. Carbidopa is co-administered because it acts as a peripheral inhibitor of which of the following enzymes, thereby increasing the bioavailability of levodopa across the blood-brain barrier and minimizing peripheral side effects?",
        "options": [
            {"text": "Tyrosine hydroxylase", "is_correct": False},
            {"text": "DOPA decarboxylase (Aromatic L-amino acid decarboxylase)", "is_correct": True},
            {"text": "Dopamine beta-hydroxylase", "is_correct": False},
            {"text": "Monoamine oxidase B (MAO-B)", "is_correct": False},
            {"text": "Catechol-O-methyltransferase (COMT)", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. DOPA decarboxylase (Aromatic L-amino acid decarboxylase).\n\nLevodopa (L-DOPA) crosses the blood-brain barrier via large neutral amino acid transporters, whereas dopamine itself cannot cross the BBB. If levodopa is administered alone, >95% is rapidly converted into dopamine in the peripheral circulation by peripheral DOPA decarboxylase, causing severe peripheral side effects (nausea, vomiting via area postrema stimulation, orthostatic hypotension, arrhythmias) with minimal drug reaching the brain. Carbidopa is a peripheral DOPA decarboxylase inhibitor that does not cross the BBB. Co-administering carbidopa blocks peripheral conversion, increasing brain bioavailability of levodopa and drastically reducing nausea.\n\n• Option D is incorrect: Selegiline and rasagiline inhibit MAO-B.\n• Option E is incorrect: Entacapone inhibits peripheral COMT."
    },
    {
        "id": "FZ_Q060",
        "question_number": 60,
        "category": "Neurotransmitters and Action Potentials",
        "stem": "In the chemical synapse, neurotransmitters are cleared from the synaptic cleft by enzymatic degradation, glial uptake, or presynaptic reuptake. Which of the following neurotransmitters is cleared primarily via rapid extracellular enzymatic degradation directly within the synaptic cleft, rather than by reuptake via Na+-coupled plasma membrane transporters?",
        "options": [
            {"text": "Acetylcholine", "is_correct": True},
            {"text": "Dopamine", "is_correct": False},
            {"text": "Norepinephrine", "is_correct": False},
            {"text": "Serotonin", "is_correct": False},
            {"text": "Glutamate", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Acetylcholine.\n\nUnlike biogenic amines (dopamine, norepinephrine, serotonin) and amino acid transmitters (glutamate, GABA), which rely primarily on secondary active Na+-coupled reuptake transporters (DAT, NET, SERT, EAAT, GAT) to terminate synaptic signaling, acetylcholine is rapidly hydrolyzed directly within the synaptic cleft by the enzyme Acetylcholinesterase (AChE). AChE cleaves acetylcholine into acetate and choline in sub-millisecond timescales. Free choline is then taken back up into the presynaptic terminal via high-affinity choline transporters (ChT) to synthesize new ACh.\n\n• Options B, C, and D are incorrect: Biogenic amines are cleared predominantly via presynaptic reuptake transporters."
    },

    # =========================================================================
    # TOPIC 4: Ventricular System (FZ_Q061 - FZ_Q080)
    # =========================================================================
    {
        "id": "FZ_Q061",
        "question_number": 61,
        "category": "Ventricular System",
        "stem": "A 74-year-old man is brought to the clinic by his family because of progressive gait unsteadiness, forgetfulness, and urinary urgency over the past 4 months. His family notes that his feet appear 'stuck to the floor' when he walks (magnetic gait), and he recently suffered multiple urinary accidents. Mental status examination shows psychomotor slowing and impaired recall. An unenhanced brain MRI reveals marked, symmetrical enlargement of the lateral and third ventricles out of proportion to mild cerebral cortical sulcal enlargement. Opening pressure on lumbar puncture is 140 mm H2O (normal). Which of the following is the most likely diagnosis?",
        "options": [
            {"text": "Alzheimer disease", "is_correct": False},
            {"text": "Idiopathic intracranial hypertension (pseudotumor cerebri)", "is_correct": False},
            {"text": "Normal pressure hydrocephalus (NPH)", "is_correct": True},
            {"text": "Progressive supranuclear palsy", "is_correct": False},
            {"text": "Aqueductal stenosis", "is_correct": False}
        ],
        "explanation": "Correct Answer: C. Normal pressure hydrocephalus (NPH).\n\nNormal pressure hydrocephalus (NPH) is a form of communicating hydrocephalus characterized by the classic clinical triad:\n1. Gait disturbance: Magnetic, apraxic, wide-based, shuffling gait ('wobbly') — usually the earliest and most prominent symptom.\n2. Urinary incontinence: Detrusor instability and urge incontinence ('wet').\n3. Cognitive impairment: Subcortical dementia with psychomotor slowing, apathy, and impaired executive function ('wacky').\nNeuroimaging shows ventriculomegaly out of proportion to sulcal enlargement. Lumbar puncture demonstrates normal opening pressure (typically 100-200 mm H2O). A large-volume CSF tap test (30-50 mL removed) produces transient improvement in gait, predicting positive long-term response to ventriculoperitoneal (VP) shunting.\n\n• Option A is incorrect: Alzheimer disease causes prominent early episodic memory loss and hydrocephalus ex vacuo (ventricles enlarged secondary to cortical atrophy).\n• Option B is incorrect: Pseudotumor cerebri presents with headache, papilledema, and elevated opening pressure (>250 mm H2O) in young obese females."
    },
    {
        "id": "FZ_Q062",
        "question_number": 62,
        "category": "Ventricular System",
        "stem": "Cerebrospinal fluid (CSF) is continually produced at a rate of approximately 500 mL/day by modified ependymal cells of the choroid plexus. Which of the following anatomical channels provides the normal direct pathway for CSF to flow from the paired lateral ventricles into the midline third ventricle?",
        "options": [
            {"text": "Interventricular foramen of Monro", "is_correct": True},
            {"text": "Cerebral aqueduct of Sylvius", "is_correct": False},
            {"text": "Foramen of Luschka", "is_correct": False},
            {"text": "Foramen of Magendie", "is_correct": False},
            {"text": "Central canal of the spinal cord", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Interventricular foramen of Monro.\n\nCSF flow pathway:\n1. Produced by the choroid plexus within the lateral, third, and fourth ventricles.\n2. Lateral ventricles → Interventricular foramen of Monro → Third ventricle.\n3. Third ventricle → Cerebral aqueduct of Sylvius (in the midbrain) → Fourth ventricle.\n4. Fourth ventricle → Lateral foramina of Luschka (2) and median foramen of Magendie (1) → Subarachnoid space (cisterna magna and basal cisterns).\n5. Subarachnoid space → Arachnoid villi / granulations → Venous drainage into the superior sagittal sinus.\n\n• Option B is incorrect: The cerebral aqueduct connects the 3rd and 4th ventricles.\n• Options C and D are incorrect: The foramina of Luschka (Lateral) and Magendie (Median) drain the 4th ventricle into the subarachnoid space."
    },
    {
        "id": "FZ_Q063",
        "question_number": 63,
        "category": "Ventricular System",
        "stem": "A 16-year-old boy presents with progressive morning headaches, vomiting, and visual disturbances. On examination, he exhibits Parinaud syndrome, characterized by upward gaze paralysis, convergence-retraction nystagmus on attempted upward gaze, and light-near dissociation of the pupils. Neuroimaging reveals a mass in the pineal region compressing the dorsal midbrain. Obstruction of which of the following ventricular structures by this mass causes the patient's non-communicating hydrocephalus?",
        "options": [
            {"text": "Foramen of Monro", "is_correct": False},
            {"text": "Cerebral aqueduct of Sylvius", "is_correct": True},
            {"text": "Foramen of Luschka", "is_correct": False},
            {"text": "Foramen of Magendie", "is_correct": False},
            {"text": "Fourth ventricle outlet", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. Cerebral aqueduct of Sylvius.\n\nPineal gland tumors (e.g., germinoma, pineoblastoma) compress the dorsal midbrain tectum (superior colliculi and pretectal area), causing Parinaud syndrome (vertical gaze palsy, convergence-retraction nystagmus, light-near pupillary dissociation). Directly anterior to the tectum lies the slender cerebral aqueduct of Sylvius (which connects the third and fourth ventricles). Compression of the aqueduct results in obstructive (non-communicating) hydrocephalus with marked upstream dilation of the lateral and third ventricles.\n\n• Option A is incorrect: Obstruction of the foramen of Monro dilates only the lateral ventricles.\n• Options C and D are incorrect: The foramina of Luschka and Magendie are located in the caudal fourth ventricle in the medulla."
    },
    {
        "id": "FZ_Q064",
        "question_number": 64,
        "category": "Ventricular System",
        "stem": "The blood-brain barrier (BBB) strictly regulates the entry of polar molecules, proteins, and pathogens into the central nervous system parenchyma. Which of the following cellular components forms the primary physical seal responsible for the high electrical resistance and restricted paracellular permeability of the blood-brain barrier?",
        "options": [
            {"text": "Astrocyte end-feet (podocytes) surrounding the capillaries", "is_correct": False},
            {"text": "Non-fenestrated brain capillary endothelial cells joined by tight junctions (claudins and occludins)", "is_correct": True},
            {"text": "Pericytes embedded in the capillary basement membrane", "is_correct": False},
            {"text": "Pial cells forming the glia limitans", "is_correct": False},
            {"text": "Ependymal cells lining the cerebral ventricles", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. Non-fenestrated brain capillary endothelial cells joined by tight junctions (claudins and occludins).\n\nThe anatomical foundation of the blood-brain barrier consists of specialized, non-fenestrated capillary endothelial cells joined by continuous, complex intercellular tight junctions (composed of transmembrane proteins including claudins, occludin, and junctional adhesion molecules). These tight junctions abolish paracellular aqueous pores, forcing solutes to pass transcellularly based on lipid solubility or specific carrier-mediated transport mechanisms.\n\n• Option A is incorrect: Astrocyte foot processes encase the capillary and secrete signaling factors (such as TGF-beta) that induce and maintain the tight junctions, but they do not form the physical barrier itself.\n• Option C is incorrect: Pericytes regulate capillary blood flow and vascular stability."
    },
    {
        "id": "FZ_Q065",
        "question_number": 65,
        "category": "Ventricular System",
        "stem": "A 52-year-old woman undergoing chemotherapy for breast cancer experiences severe nausea and emesis within 30 minutes of receiving IV cisplatin. Cisplatin circulates in the bloodstream and triggers vomiting by activating dopamine D2 and neurokinin-1 receptors in the chemoreceptor trigger zone (area postrema). In which of the following locations is the area postrema situated, and why can circulating polar toxins access it directly?",
        "options": [
            {"text": "Caudal floor of the fourth ventricle; it is a circumventricular organ lacking a blood-brain barrier", "is_correct": True},
            {"text": "Anterior wall of the third ventricle; it is protected by tight junction ependyma", "is_correct": False},
            {"text": "Medial temporal lobe; it possesses fenestrated choroid arteries", "is_correct": False},
            {"text": "Interpeduncular fossa; it contains non-fenestrated capillaries", "is_correct": False},
            {"text": "Tectum of the midbrain; it has specialized GLUT1 transporters", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Caudal floor of the fourth ventricle; it is a circumventricular organ lacking a blood-brain barrier.\n\nThe area postrema is located in the caudal floor of the fourth ventricle at the dorsal margin of the medulla (adjacent to the obex and nucleus tractus solitarius). It is a circumventricular organ, meaning its capillary endothelial cells are fenestrated and lack a blood-brain barrier. This specialized anatomy allows the area postrema to act as the chemoreceptor trigger zone (CTZ), directly sampling systemic blood and emetogenic toxins (e.g., chemotherapeutic agents like cisplatin) to trigger the vomiting reflex.\n\n• Options B, C, D, and E are incorrect: The area postrema is located in the dorsal medulla (fourth ventricle floor) and lacks a BBB."
    },
    {
        "id": "FZ_Q066",
        "question_number": 66,
        "category": "Ventricular System",
        "stem": "A 68-year-old man who survived severe pneumococcal meningitis 3 months ago presents with progressive lethargy, headache, and cognitive slowing. A head CT demonstrates marked, symmetrical enlargement of all four ventricles (lateral, third, and fourth) with effacement of cortical sulci. Lumbar puncture demonstrates an elevated opening pressure of 280 mm H2O with normal glucose and protein. Which of the following pathophysiological mechanisms is responsible for this communicating hydrocephalus?",
        "options": [
            {"text": "Obstruction of the cerebral aqueduct by glial scabbing", "is_correct": False},
            {"text": "Fibrotic scarring and obliteration of the arachnoid villi/granulations impairing CSF reabsorption", "is_correct": True},
            {"text": "Hypersecretion of CSF by a choroid plexus papilloma", "is_correct": False},
            {"text": "Herniation of cerebellar tonsils through the foramen magnum", "is_correct": False},
            {"text": "Primary overproduction of endolymph within the inner ear", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. Fibrotic scarring and obliteration of the arachnoid villi/granulations impairing CSF reabsorption.\n\nCommunicating (non-obstructive) hydrocephalus occurs when CSF flow between the ventricles is unobstructed, but CSF reabsorption into the superior sagittal sinus is impaired. The most common cause is scarring, inflammation, and fibrotic occlusion of the arachnoid villi (granulations) following bacterial meningitis or subarachnoid hemorrhage. Because CSF cannot be reabsorbed, pressure increases and all four ventricles dilate symmetrically.\n\n• Option A is incorrect: Aqueductal stenosis causes non-communicating hydrocephalus with enlargement of the lateral and 3rd ventricles but a normal/small 4th ventricle.\n• Option C is incorrect: Choroid plexus papillomas cause communicating hydrocephalus via CSF hypersecretion, but are rare tumors typically seen in young children."
    },
    {
        "id": "FZ_Q067",
        "question_number": 67,
        "category": "Ventricular System",
        "stem": "A 35-year-old woman presents with severe headaches that occur exclusively when she bends forward or changes posture, accompanied by sudden 'drop attacks' (falling to the ground without loss of consciousness). Brain MRI reveals a smooth, round, well-demarcated cystic lesion attached to the roof of the third ventricle immediately adjacent to the interventricular foramen of Monro. Which of the following is the most likely diagnosis?",
        "options": [
            {"text": "Colloid cyst of the third ventricle", "is_correct": True},
            {"text": "Pineoblastoma", "is_correct": False},
            {"text": "Ependymoma of the fourth ventricle", "is_correct": False},
            {"text": "Craniopharyngioma", "is_correct": False},
            {"text": "Pilocytic astrocytoma", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Colloid cyst of the third ventricle.\n\nA colloid cyst is a benign, epithelial-lined cyst located in the anterior-superior aspect of the third ventricle, at the foramen of Monro. Because of its location, changes in head position can cause the cyst to act as a ball-valve, acutely obstructing CSF drainage from both lateral ventricles. This produces paroxysmal, position-dependent headaches, nausea, sudden acute hydrocephalus, and sudden drop attacks (syncope/falling without warning). Complete obstruction can cause rapid herniation and sudden death.\n\n• Option B is incorrect: Pineoblastomas arise in the pineal gland compressing the cerebral aqueduct.\n• Option C is incorrect: Ependymomas typically arise from the floor of the 4th ventricle in children.\n• Option D is incorrect: Craniopharyngiomas are suprasellar calcified masses arising from Rathke pouch remnants."
    },
    {
        "id": "FZ_Q068",
        "question_number": 68,
        "category": "Ventricular System",
        "stem": "A 55-year-old man with a large right-sided middle cerebral artery territory infarction develops massive brain edema and elevated intracranial pressure. Over the next 6 hours, his right pupil becomes fixed and dilated at 7 mm, his right eyelid droops, and he develops left-sided hemiplegia. An urgent CT reveals herniation of the medial temporal lobe over the free edge of the tentorium cerebelli. Compression of which of the following nerves and vessels is characteristic of this uncal herniation?",
        "options": [
            {"text": "Ipsilateral CN III and ipsilateral posterior cerebral artery (PCA)", "is_correct": True},
            {"text": "Contralateral CN VI and contralateral anterior cerebral artery (ACA)", "is_correct": False},
            {"text": "Ipsilateral CN VII and ipsilateral anterior inferior cerebellar artery (AICA)", "is_correct": False},
            {"text": "Bilateral CN XII and anterior spinal artery (ASA)", "is_correct": False},
            {"text": "Optic chiasm and internal carotid artery (ICA)", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Ipsilateral CN III and ipsilateral posterior cerebral artery (PCA).\n\nUncal herniation (transtentorial herniation) occurs when the medial temporal lobe (uncus) herniates downward across the tentorial notch. Classic features:\n1. Compression of ipsilateral CN III: Early parasympathetic fiber compression causes a fixed, dilated pupil ('blown pupil'), followed by ptosis and down-and-out deviation.\n2. Compression of ipsilateral PCA: Causes ischemia of the ipsilateral occipital cortex and contralateral homonymous hemianopia.\n3. Compression of ipsilateral cerebral peduncle (crus cerebri): Produces contralateral hemiparesis.\n4. Kernohan notch phenomenon: If the uncus pushes the midbrain across to compress the contralateral cerebral peduncle against the opposite tentorium, it produces paradoxical ipsilateral hemiparesis (a false-localizing sign).\n5. Duret hemorrhages: Caudally displaced midbrain tears paramedian basilar perforating arteries, causing fatal brainstem hemorrhages."
    },
    {
        "id": "FZ_Q069",
        "question_number": 69,
        "category": "Ventricular System",
        "stem": "During neurosurgical intensive care monitoring of a patient with severe traumatic brain injury, an intracranial pressure (ICP) monitor records a sustained pressure of 32 mmHg (normal <15 mmHg). Simultaneously, the patient's blood pressure rises to 195/105 mmHg, his pulse drops to 44 beats/min, and his breathing pattern becomes Cheyne-Stokes. This physiological response (Cushing triad) indicates impending fatal brain herniation. Which of the following represents the classic components of the Cushing triad?",
        "options": [
            {"text": "Hypertension (with widened pulse pressure), bradycardia, and irregular/depressed respirations", "is_correct": True},
            {"text": "Hypotension, tachycardia, and tachypnea", "is_correct": False},
            {"text": "Hypertension, tachycardia, and hyperthermia", "is_correct": False},
            {"text": "Hypotension, bradycardia, and Cheyne-Stokes respirations", "is_correct": False},
            {"text": "Hypothermia, tachycardia, and pupillary dilation", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Hypertension (with widened pulse pressure), bradycardia, and irregular/depressed respirations.\n\nThe Cushing triad is a late, life-threatening physiological response to severely elevated intracranial pressure (ICP) with impending brainstem herniation. Mechanism:\n1. Cerebral ischemia: Severely elevated ICP reduces cerebral perfusion pressure (CPP = MAP - ICP). Brainstem ischemia triggers a massive sympathetic surge.\n2. Hypertension with widened pulse pressure: Alpha-1 activation causes intense vasoconstriction to raise MAP and preserve cerebral perfusion.\n3. Bradycardia: Severe hypertension stimulates carotid sinus baroreceptors, triggering vagal parasympathetic activation that slows heart rate.\n4. Respiratory depression / irregularity: Direct compression of medullary respiratory centers results in irregular, slow, or Cheyne-Stokes respirations.\n\n• Option B is incorrect: Hypotension and tachycardia characterize hypovolemic or septic shock."
    },
    {
        "id": "FZ_Q070",
        "question_number": 67,
        "category": "Ventricular System",
        "stem": "A 44-year-old man with a massive right frontal glioblastoma develops subfalcine herniation. On non-contrast head CT, the cingulate gyrus is noted to have herniated beneath the free lower edge of the falx cerebri from right to left. Which of the following arterial vessels is most vulnerable to vascular compression against the falx cerebri, potentially leading to infarction of the medial frontal cortex and contralateral lower limb paralysis?",
        "options": [
            {"text": "Anterior cerebral artery (ACA)", "is_correct": True},
            {"text": "Middle cerebral artery (MCA)", "is_correct": False},
            {"text": "Posterior cerebral artery (PCA)", "is_correct": False},
            {"text": "Superior cerebellar artery (SCA)", "is_correct": False},
            {"text": "Basilar artery", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Anterior cerebral artery (ACA).\n\nSubfalcine (cingulate) herniation occurs when an expanding unilateral mass in the frontal or parietal lobe pushes the cingulate gyrus medially beneath the rigid, fibrous falx cerebri across the midline. This shifts the midline and compresses the ipsilateral (or occasionally bilateral) anterior cerebral artery (ACA) against the falx. Compression results in ACA territory infarction, causing contralateral lower extremity weakness, sensory loss, and abulia.\n\n• Option B is incorrect: The MCA courses laterally in the sylvian fissure and is not compressed against the falx.\n• Option C is incorrect: The PCA is compressed during uncal herniation across the tentorial edge."
    },
    {
        "id": "FZ_Q071",
        "question_number": 71,
        "category": "Ventricular System",
        "stem": "An 82-year-old woman with severe, advanced Alzheimer disease dies of aspiration pneumonia. At autopsy, neuropathology reveals diffuse cerebral cortical atrophy with prominent widening of cortical sulci and massive, compensatory enlargement of the lateral and third ventricles. Review of her medical records confirms that multiple lumbar punctures performed during life demonstrated normal opening pressures (120-140 mm H2O). Which of the following terms correctly classifies this compensatory ventricular enlargement?",
        "options": [
            {"text": "Hydrocephalus ex vacuo", "is_correct": True},
            {"text": "Obstructive hydrocephalus", "is_correct": False},
            {"text": "Normal pressure hydrocephalus", "is_correct": False},
            {"text": "Communicating hydrocephalus", "is_correct": False},
            {"text": "Pseudotumor cerebri", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Hydrocephalus ex vacuo.\n\nHydrocephalus ex vacuo is not a true disorder of CSF dynamics, but rather compensatory enlargement of the cerebral ventricles secondary to diffuse brain parenchymal loss and neuronal atrophy. It is seen in neurodegenerative disorders such as Alzheimer disease, Huntington disease, Pick disease, and advanced HIV-associated dementia. As brain volume shrinks, the ventricles passively dilate to fill the vacant space. Intracranial pressure and opening pressure remain completely normal.\n\n• Option C is incorrect: Normal pressure hydrocephalus (NPH) features ventriculomegaly out of proportion to sulcal enlargement and presents with the classic triad of gait ataxia, urinary incontinence, and dementia."
    },
    {
        "id": "FZ_Q072",
        "question_number": 72,
        "category": "Ventricular System",
        "stem": "A 2-year-old child presents with vomiting, irritability, and ataxia. Brain MRI demonstrates an ependymoma arising from the floor of the fourth ventricle. Histological examination confirms that the tumor is composed of ependymal cells. What is the normal physiological function and cell lineage of non-neoplastic ependymal cells lining the ventricular system?",
        "options": [
            {"text": "Ciliated neuroepithelial cells that line the ventricles and form the secretory epithelium of the choroid plexus", "is_correct": True},
            {"text": "Mesenchymal cells that phagocytose cellular debris", "is_correct": False},
            {"text": "Neural crest-derived cells that myelinate the cranial nerves", "is_correct": False},
            {"text": "Perivascular cells that secrete collagen type IV into the basement membrane", "is_correct": False},
            {"text": "Endothelial cells joined by zonula occludens tight junctions", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Ciliated neuroepithelial cells that line the ventricles and form the secretory epithelium of the choroid plexus.\n\nEpendymal cells are derived from the neuroectoderm of the neural tube. They form a single-layered, ciliated cuboidal-to-columnar epithelium that lines the cerebral ventricles and the central canal of the spinal cord. Apical cilia beat synchronously to facilitate the circulation of CSF. Specialized ependymal cells joined by tight junctions wrap around vascular capillary tufts to form the choroid plexus, which actively secretes CSF into the ventricular lumen.\n\n• Option B is incorrect: Mesenchymal phagocytes are microglia.\n• Option C is incorrect: Schwann cells are neural crest-derived."
    },
    {
        "id": "FZ_Q073",
        "question_number": 73,
        "category": "Ventricular System",
        "stem": "A 31-year-old woman presents to the clinic with severe, intractable nausea and vomiting during the 8th week of pregnancy (hyperemesis gravidarum). When considering antiemetic therapy, the physician notes that the vomiting reflex is integrated by the chemoreceptor trigger zone and nucleus tractus solitarius. Which of the following circumventricular organs acts as the body's primary osmosensory detector, stimulating thirst and vasopressin (ADH) release in response to elevated plasma hyperosmolality?",
        "options": [
            {"text": "Area postrema", "is_correct": False},
            {"text": "Organum vasculosum of the lamina terminalis (OVLT)", "is_correct": True},
            {"text": "Pineal gland", "is_correct": False},
            {"text": "Median eminence", "is_correct": False},
            {"text": "Posterior pituitary (neurohypophysis)", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. Organum vasculosum of the lamina terminalis (OVLT).\n\nThe organum vasculosum of the lamina terminalis (OVLT) and the subfornical organ (SFO) are sensory circumventricular organs that lack a blood-brain barrier. The OVLT contains specialized osmoreceptor neurons that directly sense changes in systemic plasma osmolality. When plasma osmolality rises (e.g., dehydration), the OVLT projects to the supraoptic and paraventricular nuclei of the hypothalamus to stimulate antidiuretic hormone (ADH/vasopressin) release, as well as to the lateral hypothalamus to trigger conscious thirst and water-seeking behavior.\n\n• Option A is incorrect: The area postrema is the emetic chemoreceptor trigger zone.\n• Option C is incorrect: The pineal gland secretes melatonin.\n• Option E is incorrect: The posterior pituitary stores and releases ADH and oxytocin into systemic circulation."
    },
    {
        "id": "FZ_Q074",
        "question_number": 74,
        "category": "Ventricular System",
        "stem": "A 4-month-old infant is evaluated for progressive macrocephaly and sunset eyes (bilateral downward gaze preference). Transfontanelle ultrasound and MRI demonstrate marked dilation of both lateral ventricles and the third ventricle, with a completely normal-sized, non-dilated fourth ventricle. Which of the following conditions is the most common cause of congenital non-communicating hydrocephalus in infants exhibiting this specific imaging pattern?",
        "options": [
            {"text": "Congenital stenosis of the cerebral aqueduct of Sylvius", "is_correct": True},
            {"text": "Atresia of the foramina of Luschka and Magendie", "is_correct": False},
            {"text": "Agenesis of the corpus callosum", "is_correct": False},
            {"text": "Choroid plexus papilloma", "is_correct": False},
            {"text": "Arachnoid granulation agenesis", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Congenital stenosis of the cerebral aqueduct of Sylvius.\n\nAqueductal stenosis is the most common cause of congenital non-communicating (obstructive) hydrocephalus in infants. Because the narrow cerebral aqueduct of Sylvius in the midbrain is obstructed, CSF flow from the third ventricle into the fourth ventricle is blocked. This results in progressive upstream dilation of the lateral ventricles and third ventricle, while the fourth ventricle downstream remains normal or small in caliber. It can be caused by congenital web-like narrowing (X-linked L1CAM mutations) or secondary to intrauterine infections (toxoplasmosis, CMV).\n\n• Option B is incorrect: Atresia of the foramina of Luschka and Magendie causes Dandy-Walker malformation with massive dilation of the fourth ventricle."
    },
    {
        "id": "FZ_Q075",
        "question_number": 75,
        "category": "Ventricular System",
        "stem": "A 19-year-old college student presents with acute confusion, fever, and neck stiffness. The resident prepares to perform an immediate diagnostic lumbar puncture. However, the attending physician pauses the procedure to examine the fundi for papilledema and to review a newly obtained non-contrast head CT, which shows diffuse cerebral edema with bilateral effacement of the basal cisterns. Why is performing a lumbar puncture strictly contraindicated in patients with mass effect or severely elevated intracranial pressure?",
        "options": [
            {"text": "Sudden reduction of lumbar CSF pressure creates a downward pressure gradient that precipitates fatal brainstem or tonsillar herniation", "is_correct": True},
            {"text": "The needle will introduce bacteria into the sterile ventricular system", "is_correct": False},
            {"text": "It triggers acute malignant hyperthermia via ryanodine receptor activation", "is_correct": False},
            {"text": "It leads to acute communicating hydrocephalus via choroid plexus hypersecretion", "is_correct": False},
            {"text": "It induces widespread cortical spreading depression and stroke", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Sudden reduction of lumbar CSF pressure creates a downward pressure gradient that precipitates fatal brainstem or tonsillar herniation.\n\nIn the presence of mass effect or elevated intracranial pressure, the brain parenchyma is under high downward pressure. Removing CSF from the lumbar subarachnoid space lowers hydrostatic pressure in the spinal canal, creating a steep downward pressure gradient. This gradient rapidly pulls the cerebellar tonsils downward through the foramen magnum (tonsillar herniation) or the temporal uncus through the tentorium (uncal herniation), compressing the medulla oblongata and causing immediate respiratory arrest and death. Therefore, a head CT must be obtained prior to LP whenever red-flag signs of high ICP or focal neurological deficits are present.\n\n• Options B, C, D, and E do not represent the mechanism of herniation risk."
    },
    {
        "id": "FZ_Q076",
        "question_number": 76,
        "category": "Ventricular System",
        "stem": "A 26-year-old obese woman (BMI 36 kg/m2) presents with bilateral throbbing headaches, transient visual obscurations when standing, and pulsatile tinnitus ('whooshing' sounds in her ears). Fundoscopic examination reveals bilateral severe papilledema. An unenhanced brain MRI is normal except for an empty sella and flattening of the posterior globes. Lumbar puncture demonstrates an elevated opening pressure of 340 mm H2O (normal <200) with completely normal CSF cell count, protein, and glucose. Which of the following is the first-line medical therapy for idiopathic intracranial hypertension (pseudotumor cerebri)?",
        "options": [
            {"text": "Acetazolamide", "is_correct": True},
            {"text": "Mannitol", "is_correct": False},
            {"text": "Furosemide", "is_correct": False},
            {"text": "Dexamethasone", "is_correct": False},
            {"text": "Donepezil", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Acetazolamide.\n\nIdiopathic intracranial hypertension (pseudotumor cerebri) typically affects young, obese women of childbearing age (associated with tetracyclines, vitamin A toxicity, isotretinoin). It presents with headaches, pulsatile tinnitus, CN VI palsies, and bilateral papilledema, with elevated opening pressure on LP (>250 mm H2O) but normal CSF chemistry. First-line medical therapy is Acetazolamide (a carbonic anhydrase inhibitor). In the choroid plexus, carbonic anhydrase generates bicarbonate ions necessary for CSF fluid transport; acetazolamide inhibits this enzyme, reducing CSF production and lowering ICP. Weight loss is also advised.\n\n• Option B is incorrect: IV mannitol is reserved for acute intracranial hypertension in ICU/trauma settings.\n• Option D is incorrect: Glucocorticoids do not treat pseudotumor cerebri and cause weight gain."
    },
    {
        "id": "FZ_Q077",
        "question_number": 77,
        "category": "Ventricular System",
        "stem": "Anatomists describe the roof, floor, and lateral boundaries of the fourth ventricle. Which of the following brainstem structures forms the ventral floor of the fourth ventricle (the rhomboid fossa)?",
        "options": [
            {"text": "Dorsal surface of the pons and open rostral medulla", "is_correct": True},
            {"text": "Ventral surface of the midbrain crus cerebri", "is_correct": False},
            {"text": "Superior medullary velum and vermis", "is_correct": False},
            {"text": "Inferior colliculi and pineal gland", "is_correct": False},
            {"text": "Interpeduncular fossa", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Dorsal surface of the pons and open rostral medulla.\n\nThe fourth ventricle is a diamond-shaped cavity located between the brainstem and the cerebellum. Its ventral floor (rhomboid fossa) is formed by the dorsal surface of the pons (rostral half) and the dorsal surface of the open rostral medulla (caudal half). The roof of the fourth ventricle is formed by the superior medullary velum rostrally and the inferior medullary velum/choroid plexus/cerebellar vermis caudally.\n\n• Option B is incorrect: The ventral surface of the midbrain crus cerebri faces anteriorly, away from the ventricles.\n• Option C is incorrect: The superior medullary velum forms the roof, not the floor."
    },
    {
        "id": "FZ_Q078",
        "question_number": 78,
        "category": "Ventricular System",
        "stem": "A 7-year-old child presents with morning nausea, vomiting, and gait ataxia. Contrast MRI of the brain demonstrates an intensely enhancing mass arising from the lateral ventricle choroid plexus. Biopsy confirms a choroid plexus papilloma. In addition to causing hydrocephalus by direct mass effect, this tumor is famous for causing communicating hydrocephalus through which of the following mechanisms?",
        "options": [
            {"text": "Marked hypersecretion of cerebrospinal fluid exceeding the reabsorptive capacity of the arachnoid villi", "is_correct": True},
            {"text": "Direct destruction of the internal carotid artery", "is_correct": False},
            {"text": "Autoimmune demyelination of the medial longitudinal fasciculus", "is_correct": False},
            {"text": "Severe cerebral vasoconstriction reducing brain perfusion", "is_correct": False},
            {"text": "Infiltration of the pineal gland suppressing melatonin synthesis", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Marked hypersecretion of cerebrospinal fluid exceeding the reabsorptive capacity of the arachnoid villi.\n\nChoroid plexus papillomas are benign intraventricular neuroepithelial neoplasms derived from choroid plexus epithelial cells (most common in the lateral ventricles in children and the 4th ventricle in adults). They are one of the few true causes of hydrocephalus due to CSF overproduction. The neoplastic choroid plexus secretes copious volumes of CSF that overwhelm the physiological reabsorptive capacity of normal arachnoid villi, resulting in communicating hydrocephalus.\n\n• Options B, C, D, and E do not describe the pathophysiology of choroid plexus papillomas."
    },
    {
        "id": "FZ_Q079",
        "question_number": 79,
        "category": "Ventricular System",
        "stem": "In the subarachnoid space, cerebrospinal fluid circulates over the cerebral convexities before being filtered back into the venous circulation. Through which of the following histological structures does CSF pass to enter the superior sagittal sinus, functioning as one-way pressure-dependent valves?",
        "options": [
            {"text": "Arachnoid villi (granulations)", "is_correct": True},
            {"text": "Virchow-Robin perivascular spaces", "is_correct": False},
            {"text": "Choroid plexus tight junctions", "is_correct": False},
            {"text": "Bridging cortical veins", "is_correct": False},
            {"text": "Pia mater fenestrations", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Arachnoid villi (granulations).\n\nArachnoid villi (macroscopic aggregations are known as arachnoid granulations or Pacchionian bodies) are outpocketings of the arachnoid mater that herniate through the meningeal dura into the superior sagittal sinus and its lateral lacunae. They function as passive, one-way pressure-dependent valves: when CSF pressure in the subarachnoid space exceeds venous sinus pressure (by 2-5 mmHg), open transcellular tubules and pores allow bulk flow of CSF into the venous blood, while preventing retrograde reflux of blood into the subarachnoid space.\n\n• Option B is incorrect: Virchow-Robin spaces are perivascular channels surrounding penetrating arterioles in the brain parenchyma.\n• Option D is incorrect: Bridging veins drain venous blood from the cortex into the superior sagittal sinus and can tear to cause subdural hematomas."
    },
    {
        "id": "FZ_Q080",
        "question_number": 80,
        "category": "Ventricular System",
        "stem": "A 59-year-old man with a history of hypertension suffers an acute intracerebral hemorrhage in the right basal ganglia with mass effect. On day 2, his neurological status deteriorates acutely: both pupils become fixed in midposition (5 mm), he exhibits decerebrate (extensor) posturing in response to noxious stimuli, and his respirations become rapid and shallow. Neuroimaging demonstrates central (transtentorial) herniation. Downward displacement of which of the following structures across the tentorial incisura defines central herniation?",
        "options": [
            {"text": "Cerebellar tonsils through the foramen magnum", "is_correct": False},
            {"text": "Bilateral cerebral hemispheres and diencephalon downward through the tentorial notch", "is_correct": True},
            {"text": "Cingulate gyrus beneath the falx cerebri", "is_correct": False},
            {"text": "Uncus of the temporal lobe over the tentorial edge", "is_correct": False},
            {"text": "Medulla oblongata upward through the tentorial notch", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. Bilateral cerebral hemispheres and diencephalon downward through the tentorial notch.\n\nCentral (transtentorial) herniation occurs when bilateral supratentorial mass lesions or diffuse cerebral edema force the diencephalon (thalamus and hypothalamus) and midbrain downward through the tentorial notch. This causes rostral-to-caudal brainstem compression:\n• Diencephalic stage: Small reactive pupils, Cheyne-Stokes respirations, decorticate posturing.\n• Midbrain/upper pontine stage: Midposition fixed pupils, hyperventilation, decerebrate (extensor) posturing.\n• Lower pontine/medullary stage: Flaccid paralysis, absent brainstem reflexes, terminal respiratory arrest.\n\n• Option A is incorrect: Downward herniation of cerebellar tonsils through the foramen magnum is tonsillar herniation.\n• Option C is incorrect: Cingulate gyrus displacement is subfalcine herniation.\n• Option D is incorrect: Unilateral temporal uncus herniation is uncal herniation."
    }
]
