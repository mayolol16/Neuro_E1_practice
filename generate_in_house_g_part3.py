# Part 3: Questions 94 to 150 (Brainstem Stroke: 15 Qs, Dementia: 15 Qs, CBIL Epilepsy: 27 Qs)

def get_part3_questions():
    qs = []

    # =========================================================================
    # UNIT 8: STROKE - BRAINSTEM STROKE & ALTERNATING HEMIPLEGIAS (15 Qs: Q94 - Q108, 10%)
    # =========================================================================

    # Q94
    qs.append({
        "id": "exam3_in_house_like_g_q94",
        "q_num": "94",
        "stem": "A 59-year-old man presents with acute vertigo, nausea, vomiting, severe dysphagia, and hoarseness. Neurological examination reveals right-sided Horner syndrome (ptosis, miosis, anhidrosis), loss of pain and temperature on the right side of his face, loss of pain and temperature on the left side of his body, right cerebellar limb dysmetria, and a diminished right gag reflex with the uvula deviating to the left. Motor strength in all four extremities is 5/5. Occlusion of which of the following vessels is responsible?",
        "category": "Stroke (Blood Supply, Cerebrovascular, Brainstem)",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Anterior inferior cerebellar artery vascular trunk"},
            {"letter": "B", "is_correct": True, "text": "Posterior inferior cerebellar artery arterial branch"},
            {"letter": "C", "is_correct": False, "text": "Paramedian penetrating branches of the basilar"},
            {"letter": "D", "is_correct": False, "text": "Anterior spinal artery paramedian vascular trunk"},
            {"letter": "E", "is_correct": False, "text": "Superior cerebellar artery lateral branch vessels"}
        ],
        "correct_idx": 1,
        "explanation": "Lateral medullary (Wallenberg) syndrome is caused by occlusion of the posterior inferior cerebellar artery (PICA) or its parent vertebral artery. Classic structures damaged include: nucleus ambiguus (CN IX, X: dysphagia, hoarseness, decreased gag, uvula deviation away from lesion), vestibular nuclei (vertigo, nystagmus), spinal trigeminal nucleus (ipsilateral facial pain/temp loss), spinothalamic tract (contralateral body pain/temp loss), inferior cerebellar peduncle (ipsilateral ataxia), and descending sympathetics (ipsilateral Horner syndrome). Notably, the corticospinal tract is medial and completely spared, so motor strength is 5/5.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Wallenberg syndrome (PICA) features dysphagia/hoarseness (nucleus ambiguus), crossed pain/temperature loss, Horner syndrome, and ataxia; extremity motor strength is completely spared.",
        "image": None
    })

    # Q95
    qs.append({
        "id": "exam3_in_house_like_g_q95",
        "q_num": "95",
        "stem": "A 66-year-old man presents with acute left-sided weakness. Neurological examination reveals right-sided flaccid tongue paralysis; on protrusion, the tongue deviates to the right side with fasciculations. He exhibits left spastic hemiparesis with an extensor plantar response on the left, and loss of vibration sense, proprioception, and light touch on the left side of his body. Pain and temperature sensation are preserved bilaterally. Which of the following arterial vessels was occluded to produce this clinical syndrome?",
        "category": "Stroke (Blood Supply, Cerebrovascular, Brainstem)",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Posterior inferior cerebellar artery vascular trunk"},
            {"letter": "B", "is_correct": True, "text": "Anterior spinal artery paramedian medullary branch"},
            {"letter": "C", "is_correct": False, "text": "Anterior inferior cerebellar artery caudal branches"},
            {"letter": "D", "is_correct": False, "text": "Superior cerebellar artery rostral brainstem supply"},
            {"letter": "E", "is_correct": False, "text": "Posterior cerebral artery penetrating calcarine"}
        ],
        "correct_idx": 1,
        "explanation": "Medial medullary (Dejerine) syndrome is caused by occlusion of the anterior spinal artery (ASA) or paramedian branches of the vertebral artery. It damages three structures in the anterior medial medulla: the hypoglossal nerve fibers/nucleus (ipsilateral LMN tongue weakness; tongue deviates toward lesion), the corticospinal tract in the pyramid (contralateral spastic hemiparesis), and the medial lemniscus (contralateral loss of vibration and proprioception). Spinothalamic pain and temperature tracts are lateral and spared.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Medial medullary syndrome (ASA) damages the hypoglossal nerve (tongue deviates toward lesion), pyramid (contralateral hemiparesis), and medial lemniscus (contralateral proprioception loss).",
        "image": None
    })

    # Q96
    qs.append({
        "id": "exam3_in_house_like_g_q96",
        "q_num": "96",
        "stem": "A 61-year-old woman presents with acute vertigo, vomiting, right-sided facial weakness, and profound right-sided hearing loss. Physical examination demonstrates complete paralysis of the entire right face (involving both the forehead and lower face), hyperacusis in the right ear, loss of taste on the anterior two-thirds of the tongue on the right, right corneal reflex absence, right cerebellar limb dysmetria, and loss of pain and temperature on the left body. Occlusion of which of the following vessels is the cause?",
        "category": "Stroke (Blood Supply, Cerebrovascular, Brainstem)",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Posterior inferior cerebellar artery vascular branch"},
            {"letter": "B", "is_correct": True, "text": "Anterior inferior cerebellar artery arterial trunk"},
            {"letter": "C", "is_correct": False, "text": "Superior cerebellar artery rostral branch vessels"},
            {"letter": "D", "is_correct": False, "text": "Anterior spinal artery paramedian medullary trunk"},
            {"letter": "E", "is_correct": False, "text": "Posterior cerebral artery penetrating deep supply"}
        ],
        "correct_idx": 1,
        "explanation": "Lateral inferior pontine syndrome is caused by occlusion of the anterior inferior cerebellar artery (AICA). It presents similarly to lateral medullary syndrome (ataxia, Horner syndrome, crossed pain/temp loss), but is uniquely distinguished by involvement of cranial nerves VII and VIII: ipsilateral peripheral facial motor paralysis (CN VII nucleus/nerve: complete upper and lower face palsy), loss of taste on the anterior two-thirds of the tongue, and sensorineural hearing loss with tinnitus (CN VIII / internal auditory artery).",
        "high_yield_pearl": "High-Yield Clinical Pearl: AICA lateral pontine stroke causes ipsilateral facial paralysis (CN VII) and hearing loss (CN VIII), distinguishing it from PICA (which affects CN IX/X with dysphagia/hoarseness).",
        "image": None
    })

    # Q97
    qs.append({
        "id": "exam3_in_house_like_g_q97",
        "q_num": "97",
        "stem": "A 70-year-old man presents with acute double vision and left-sided weakness. Neurological examination reveals that when asked to look to the right, his right eye cannot abduct, while his left eye adducts normally. On left gaze and vertical gaze, eye movements are normal. He demonstrates left spastic hemiparesis and decreased vibration sense over the left upper and lower extremities. Sensation over the face is intact. An acute ischemic infarction in which of the following regions accounts for this presentation?",
        "category": "Stroke (Blood Supply, Cerebrovascular, Brainstem)",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Right dorsolateral tegmentum of the rostral medulla"},
            {"letter": "B", "is_correct": True, "text": "Right paramedian basis and tegmentum of caudal pons"},
            {"letter": "C", "is_correct": False, "text": "Left ventrolateral crus cerebri of the midbrain"},
            {"letter": "D", "is_correct": False, "text": "Right dorsolateral pretectum of the dorsal midbrain"},
            {"letter": "E", "is_correct": False, "text": "Left posterior limb of the internal capsule tract"}
        ],
        "correct_idx": 1,
        "explanation": "Medial inferior pontine syndrome is caused by occlusion of paramedian branches of the basilar artery. It damages three structures: the abducens nerve or nucleus (ipsilateral lateral rectus palsy with failure of abduction), the descending corticospinal tract in the basis pontis (contralateral spastic hemiparesis), and the medial lemniscus (contralateral loss of vibration and proprioception).",
        "high_yield_pearl": "High-Yield Clinical Pearl: Medial pontine syndrome (paramedian basilar branches) causes ipsilateral abducens (CN VI) palsy and contralateral hemiparesis and medial lemniscus proprioception loss.",
        "image": None
    })

    # Q98
    qs.append({
        "id": "exam3_in_house_like_g_q98",
        "q_num": "98",
        "stem": "A 74-year-old man presents with acute diplopia and left-sided weakness. Neurological examination reveals that the right eye is positioned \"down and out\" at rest, with complete right upper eyelid ptosis and a dilated right pupil that is unreactive to direct light. Examination of the left side reveals dense left spastic hemiplegia and a left lower facial droop. He cannot protrude the left corner of his mouth, but forehead wrinkling is symmetric. Occlusion of penetrating branches of which of the following vessels is responsible?",
        "category": "Stroke (Blood Supply, Cerebrovascular, Brainstem)",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Superior cerebellar artery rostral brainstem branch"},
            {"letter": "B", "is_correct": True, "text": "Posterior cerebral artery paramedian midbrain supply"},
            {"letter": "C", "is_correct": False, "text": "Anterior inferior cerebellar artery caudal branches"},
            {"letter": "D", "is_correct": False, "text": "Anterior choroidal artery lateral temporal branches"},
            {"letter": "E", "is_correct": False, "text": "Posterior inferior cerebellar artery medullary trunk"}
        ],
        "correct_idx": 1,
        "explanation": "Weber syndrome (ventral midbrain syndrome) is caused by occlusion of paramedian penetrating branches of the posterior cerebral artery (PCA). The lesion damages the exiting oculomotor nerve fascicles (CN III: ipsilateral ptosis, dilated fixed pupil, and \"down and out\" resting gaze) and the adjacent crus cerebri / cerebral peduncle (contralateral spastic hemiplegia via corticospinal tracts, and contralateral lower facial weakness via corticobulbar fibers).",
        "high_yield_pearl": "High-Yield Clinical Pearl: Weber syndrome (paramedian PCA) damages ventral midbrain: ipsilateral CN III palsy (\"down and out\" eye, mydriasis, ptosis) + contralateral spastic hemiplegia (cerebral peduncle).",
        "image": None
    })

    # Q99
    qs.append({
        "id": "exam3_in_house_like_g_q99",
        "q_num": "99",
        "stem": "A 76-year-old woman with chronic atrial fibrillation who discontinued her anticoagulation presents with acute double vision and limb tremor. Examination shows a dilated, fixed right pupil with ptosis and \"down and out\" eye deviation on the right. She exhibits loss of tactile sensation over the left face and left body. She has normal 5/5 strength bilaterally, but exhibits an irregular, coarse intention tremor and prominent dysmetria in both her left arm and left leg. Which of the following midbrain syndromes is present?",
        "category": "Stroke (Blood Supply, Cerebrovascular, Brainstem)",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Weber syndrome involving the ventral cerebral peduncle"},
            {"letter": "B", "is_correct": True, "text": "Benedikt syndrome involving the midbrain tegmentum"},
            {"letter": "C", "is_correct": False, "text": "Millard-Gubler syndrome involving the caudal pons"},
            {"letter": "D", "is_correct": False, "text": "Wallenberg syndrome involving the lateral medulla"},
            {"letter": "E", "is_correct": False, "text": "Dejerine syndrome involving the anterior medial medulla"}
        ],
        "correct_idx": 1,
        "explanation": "Benedikt syndrome (paramedian midbrain tegmentum syndrome) is caused by occlusion of penetrating branches of the PCA. The lesion damages CN III fascicles (ipsilateral CN III palsy), the medial lemniscus and ventral trigeminothalamic tract (contralateral sensory loss of body and face), and the red nucleus and adjacent superior cerebellar peduncle fibers (dentatorubrothalamic tract). Because superior cerebellar peduncle fibers cross before entering the red nucleus, damage produces contralateral intention tremor, ataxia, and choreoathetosis affecting both the arm and leg.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Benedikt syndrome (PCA midbrain tegmentum) features ipsilateral CN III palsy, contralateral sensory loss, and contralateral limb ataxia/tremor (red nucleus and superior cerebellar peduncle).",
        "image": None
    })

    # Q100
    qs.append({
        "id": "exam3_in_house_like_g_q100",
        "q_num": "100",
        "stem": "A 68-year-old man presents with acute diplopia and unsteadiness. Examination shows right-sided ptosis, a dilated right pupil, and right eye resting in a \"down and out\" position. He exhibits prominent intention tremor, dysmetria, and ataxia in the left upper extremity. Muscle strength is 5/5 bilaterally, with no corticospinal hyperreflexia or Babinski sign, and sensory examination is entirely normal. Which of the following midbrain structures was damaged to cause his isolated contralateral limb ataxia?",
        "category": "Stroke (Blood Supply, Cerebrovascular, Brainstem)",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Ventral crus cerebri containing corticospinal motor tracts"},
            {"letter": "B", "is_correct": True, "text": "Red nucleus and fibers of the superior cerebellar peduncle"},
            {"letter": "C", "is_correct": False, "text": "Substantia nigra pars compacta dopaminergic neuron cluster"},
            {"letter": "D", "is_correct": False, "text": "Medial lemniscus carrying contralateral proprioceptive input"},
            {"letter": "E", "is_correct": False, "text": "Spinal trigeminal nucleus and tract pain relay pathway"}
        ],
        "correct_idx": 1,
        "explanation": "Claude syndrome is a midbrain tegmental stroke caused by occlusion of branches of the PCA. It is characterized by an ipsilateral CN III palsy combined with contralateral cerebellar ataxia and intention tremor, WITHOUT significant corticospinal hemiparesis (which spares the crus cerebri, distinguishing it from Weber syndrome) and without prominent sensory loss. The contralateral limb ataxia is caused by infarction of the red nucleus and crossing fibers of the superior cerebellar peduncle.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Claude syndrome is a midbrain tegmental stroke causing ipsilateral CN III palsy and contralateral ataxia/tremor (red nucleus/superior cerebellar peduncle) with spared motor strength.",
        "image": None
    })

    # Q101
    qs.append({
        "id": "exam3_in_house_like_g_q101",
        "q_num": "101",
        "stem": "A 56-year-old man with severe basilar artery atherosclerosis suffers an acute brainstem stroke. On examination, he is completely quadriplegic and aphonic. He cannot move his face, speak, or swallow. However, his eyes are open, his sleep-wake cycles are normal, and he is able to answer complex yes/no questions accurately by blinking and moving his eyes vertically. Electroencephalography confirms normal awake rhythms. Which of the following structures was selectively spared in this patient?",
        "category": "Stroke (Blood Supply, Cerebrovascular, Brainstem)",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Bilateral descending corticospinal motor fiber tracts"},
            {"letter": "B", "is_correct": True, "text": "Tegmental ascending reticular activating system and CN III"},
            {"letter": "C", "is_correct": False, "text": "Bilateral descending corticobulbar motor fiber pathways"},
            {"letter": "D", "is_correct": False, "text": "Bilateral pontine abducens cranial nerve nuclei pathways"},
            {"letter": "E", "is_correct": False, "text": "Bilateral facial motor cranial nerve nuclei pathways"}
        ],
        "correct_idx": 1,
        "explanation": "Locked-in syndrome is caused by bilateral ventral pontine infarction (basis pontis), usually secondary to basilar artery thrombosis. It destroys the bilateral descending corticospinal tracts (causing complete quadriplegia) and corticobulbar tracts (causing aphonia and bilateral lower cranial nerve motor paralysis). Consciousness is preserved because the dorsal pontine tegmentum and the ascending reticular activating system (ARAS) are spared. Vertical eye movements and blinking are preserved because they are controlled by rostral midbrain centers (CN III and IV) and the Edinger-Westphal nucleus.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Locked-in syndrome (bilateral basis pontis basilar stroke) causes quadriplegia and aphonia; consciousness (ARAS) and vertical eye movements/blinking (midbrain CN III/IV) are spared.",
        "image": None
    })

    # Q102
    qs.append({
        "id": "exam3_in_house_like_g_q102",
        "q_num": "102",
        "stem": "A 64-year-old man presents with acute double vision, right-sided facial weakness, and left-sided hemiparesis. Physical examination reveals complete paralysis of the entire right side of the face (both forehead and lower face), failure of the right eye to abduct on attempted right gaze, and 2/5 spastic weakness with hyperreflexia and an extensor plantar response in the left arm and leg. Sensation is normal. Which of the following alternating brainstem syndromes does this patient display?",
        "category": "Stroke (Blood Supply, Cerebrovascular, Brainstem)",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Wallenberg syndrome of the lateral medullary region"},
            {"letter": "B", "is_correct": True, "text": "Millard-Gubler syndrome of the ventrolateral caudal pons"},
            {"letter": "C", "is_correct": False, "text": "Weber syndrome of the ventromedial rostral midbrain"},
            {"letter": "D", "is_correct": False, "text": "Benedikt syndrome of the midbrain tegmental nucleus"},
            {"letter": "E", "is_correct": False, "text": "Dejerine syndrome of the medial anterior medulla"}
        ],
        "correct_idx": 1,
        "explanation": "Millard-Gubler syndrome (ventral caudal pontine syndrome) is caused by infarction of the ventrolateral caudal pons (paramedian/circumferential branches of the basilar artery). It affects the exiting fascicles of the abducens nerve (CN VI: ipsilateral lateral rectus palsy/inability to abduct), the facial nerve (CN VII: ipsilateral complete facial palsy of Bell type), and the uncrossed descending corticospinal tract (contralateral spastic hemiplegia).",
        "high_yield_pearl": "High-Yield Clinical Pearl: Millard-Gubler syndrome (ventral caudal pons) features ipsilateral CN VI and CN VII palsies combined with contralateral spastic hemiplegia (corticospinal tract).",
        "image": None
    })

    # Q103
    qs.append({
        "id": "exam3_in_house_like_g_q103",
        "q_num": "103",
        "stem": "A 69-year-old man presents with acute right facial paralysis and left-sided hemiparesis. On neuro-ophthalmologic examination, he displays a complete conjugate gaze palsy when attempting to look to the right: neither the right eye can abduct nor can the left eye adduct on attempted rightward horizontal gaze. Leftward gaze, vertical gaze, and pupillary reflexes are normal. He also exhibits right-sided peripheral facial palsy and left hemiplegia. An infarction in which of the following structures causes this conjugate gaze palsy?",
        "category": "Stroke (Blood Supply, Cerebrovascular, Brainstem)",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Right frontal eye field within prefrontal cortex region"},
            {"letter": "B", "is_correct": True, "text": "Right paramedian pontine reticular formation or nucleus"},
            {"letter": "C", "is_correct": False, "text": "Left medial longitudinal fasciculus brainstem pathway"},
            {"letter": "D", "is_correct": False, "text": "Right oculomotor cranial nerve nucleus in dorsal midbrain"},
            {"letter": "E", "is_correct": False, "text": "Left trochlear cranial nerve nucleus in caudal midbrain"}
        ],
        "correct_idx": 1,
        "explanation": "Foville syndrome is an inferior dorsal pontine syndrome caused by infarction involving the abducens nucleus (or adjacent paramedian pontine reticular formation / PPRF), the facial nerve fascicle, and the corticospinal tract. Because the abducens nucleus contains both abducens motor neurons (to the ipsilateral lateral rectus) and interneurons that cross via the MLF to the contralateral CN III subnucleus, a nuclear lesion causes a complete ipsilateral conjugate horizontal gaze palsy (neither eye can look toward the side of the lesion).",
        "high_yield_pearl": "High-Yield Clinical Pearl: A lesion of the abducens nucleus or PPRF causes an ipsilateral conjugate gaze palsy; combined with CN VII palsy and contralateral hemiparesis, this defines Foville syndrome.",
        "image": None
    })

    # Q104
    qs.append({
        "id": "exam3_in_house_like_g_q104",
        "q_num": "104",
        "stem": "A 16-year-old boy presents with progressive headaches and visual disturbances. Examination reveals paralysis of upward conjugate gaze, bilateral upper eyelid retraction (Collier sign), and convergence-retraction nystagmus on attempted upward gaze. Pupillary examination reveals that both pupils constrict briskly to accommodation when focusing on a near object, but fail to constrict in response to bright light. MRI demonstrates a 2.5-cm mass compressing the dorsal midbrain. Which of the following neoplasms is most likely?",
        "category": "Stroke (Blood Supply, Cerebrovascular, Brainstem)",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Infratentorial cerebellar capillary hemangioblastoma"},
            {"letter": "B", "is_correct": True, "text": "Pineal region germinoma compressing the dorsal pretectum"},
            {"letter": "C", "is_correct": False, "text": "Pituitary anterior lobe prolactin-secreting adenoma"},
            {"letter": "D", "is_correct": False, "text": "Craniopharyngioma derived from surface Rathke pouch"},
            {"letter": "E", "is_correct": False, "text": "Ependymoma arising from floor of fourth ventricle"}
        ],
        "correct_idx": 1,
        "explanation": "This patient presents with Parinaud syndrome (dorsal midbrain syndrome), caused by extrinsic compression of the dorsal midbrain pretectal area and superior colliculi, most commonly by a pineal gland mass (such as a germinoma or pineocytoma) or aqueductal stenosis. Cardinal features include paralysis of upward conjugate gaze, pseudo-Argyll Robertson pupils (light-near dissociation: react to accommodation but not light), convergence-retraction nystagmus, and Collier sign (eyelid retraction).",
        "high_yield_pearl": "High-Yield Clinical Pearl: Parinaud syndrome (pineal tumor compressing dorsal midbrain) causes upward gaze palsy, light-near dissociation pupils, and convergence-retraction nystagmus.",
        "image": None
    })

    # Q105
    qs.append({
        "id": "exam3_in_house_like_g_q105",
        "q_num": "105",
        "stem": "A 27-year-old woman presents with horizontal double vision. When she attempts to look to the left, her right eye fails to adduct past the midline, while her left eye abducts fully but displays coarse horizontal nystagmus. When she attempts to look to the right, her eye movements are completely normal. Convergence is tested by bringing an object close to her nose, and both eyes adduct symmetrically with pupillary constriction. An isolated lesion in which of the following neural pathways accounts for this presentation?",
        "category": "Stroke (Blood Supply, Cerebrovascular, Brainstem)",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Left paramedian pontine reticular formation pathway"},
            {"letter": "B", "is_correct": True, "text": "Right medial longitudinal fasciculus brainstem tract"},
            {"letter": "C", "is_correct": False, "text": "Left abducens cranial nerve trunk in cavernous sinus"},
            {"letter": "D", "is_correct": False, "text": "Right oculomotor cranial nerve branch in the orbit"},
            {"letter": "E", "is_correct": False, "text": "Right frontal eye field within cerebral frontal lobe"}
        ],
        "correct_idx": 1,
        "explanation": "Internuclear ophthalmoplegia (INO) is caused by a lesion of the medial longitudinal fasciculus (MLF), which connects the contralateral abducens nucleus (PPRF) to the ipsilateral oculomotor subnucleus for the medial rectus. On attempted horizontal gaze, the eye on the side of the MLF lesion fails to adduct, while the contralateral abducting eye exhibits horizontal nystagmus. Convergence remains completely intact because the vergence pathway bypasses the MLF. Bilateral INO is pathognomonic for multiple sclerosis.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Internuclear ophthalmoplegia (INO) is caused by an MLF lesion; the ipsilateral eye fails to adduct on lateral gaze while the abducting eye has nystagmus; convergence is preserved.",
        "image": None
    })

    # Q106
    qs.append({
        "id": "exam3_in_house_like_g_q106",
        "q_num": "106",
        "stem": "A 51-year-old man presents with complex gaze abnormalities following a pontine stroke. Examination reveals that on attempted gaze to the right, neither eye moves (complete right horizontal gaze palsy). On attempted gaze to the left, the right eye fails to adduct past midline, while the left eye abducts with horizontal nystagmus. Vertical eye movements and pupillary reflexes are normal. This \"one-and-a-half syndrome\" results from a combined lesion involving which of the following structures?",
        "category": "Stroke (Blood Supply, Cerebrovascular, Brainstem)",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Bilateral medial longitudinal fasciculi in dorsal midbrain"},
            {"letter": "B", "is_correct": True, "text": "Right abducens nucleus and adjacent right MLF pathway"},
            {"letter": "C", "is_correct": False, "text": "Left abducens nucleus and adjacent left MLF tract"},
            {"letter": "D", "is_correct": False, "text": "Bilateral paramedian pontine reticular formation nuclei"},
            {"letter": "E", "is_correct": False, "text": "Right oculomotor nucleus and right trochlear nerve trunk"}
        ],
        "correct_idx": 1,
        "explanation": "The \"one-and-a-half syndrome\" is caused by a unilateral lesion involving both the abducens nucleus (or PPRF) AND the adjacent ipsilateral medial longitudinal fasciculus (MLF) on the same side. The abducens nucleus lesion produces a complete conjugate gaze palsy toward the lesion side (the \"one\"), while the MLF lesion impairs adduction of the ipsilateral eye when looking in the opposite direction (the \"half\"). The only preserved horizontal movement is abduction of the contralateral eye.",
        "high_yield_pearl": "High-Yield Clinical Pearl: One-and-a-half syndrome is caused by a unilateral lesion of the abducens nucleus (or PPRF) plus the ipsilateral MLF; only abduction of the contralateral eye remains.",
        "image": None
    })

    # Q107
    qs.append({
        "id": "exam3_in_house_like_g_q107",
        "q_num": "107",
        "stem": "A 67-year-old man with a prosthetic mitral valve develops sudden coma, pupillary asymmetry, and bilateral visual loss. Emergency brain MRI demonstrates acute ischemic infarctions involving the bilateral paramedian thalami, the rostral midbrain tegmentum, and the bilateral medial occipital lobes. Embolic occlusion at which of the following vascular locations accounts for this widespread rostral posterior circulation infarction?",
        "category": "Stroke (Blood Supply, Cerebrovascular, Brainstem)",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Origin of the posterior inferior cerebellar arteries"},
            {"letter": "B", "is_correct": True, "text": "Distal bifurcation apex of the basilar artery trunk"},
            {"letter": "C", "is_correct": False, "text": "Origin of the anterior inferior cerebellar arteries"},
            {"letter": "D", "is_correct": False, "text": "Confluence of both vertebral arteries into basilar"},
            {"letter": "E", "is_correct": False, "text": "Bifurcation of the internal carotid into ACA and MCA"}
        ],
        "correct_idx": 1,
        "explanation": "\"Top-of-the-basilar\" syndrome is caused by embolic occlusion at the rostral bifurcation of the basilar artery apex. Because the basilar apex gives rise to the superior cerebellar arteries, posterior cerebral arteries, and paramedian mesencephalic/thalamic perforators, occlusion results in ischemia of the rostral midbrain, bilateral thalami, and bilateral occipitotemporal lobes. Cardinal manifestations include coma, pupillary abnormalities, oculomotor palsies, visual hallucinations, and cortical blindness.",
        "high_yield_pearl": "High-Yield Clinical Pearl: \"Top-of-the-basilar\" syndrome involves embolic occlusion of the basilar apex, causing bilateral midbrain, thalamic, and occipital infarcts with coma and visual/pupillary defects.",
        "image": None
    })

    # Q108
    qs.append({
        "id": "exam3_in_house_like_g_q108",
        "q_num": "108",
        "stem": "A 42-year-old woman is evaluated for brain death following a severe anoxic brain injury. Cold caloric (oculovestibular) testing is performed by irrigating the right external auditory canal with ice-cold water while keeping the head elevated at 30 degrees. In a comatose patient with an intact, functional brainstem, which of the following ocular responses is normally observed?",
        "category": "Stroke (Blood Supply, Cerebrovascular, Brainstem)",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Complete absence of any ocular movement bilaterally"},
            {"letter": "B", "is_correct": True, "text": "Sustained slow tonic deviation of both eyes to right"},
            {"letter": "C", "is_correct": False, "text": "Sustained slow tonic deviation of both eyes to left"},
            {"letter": "D", "is_correct": False, "text": "Rapid saccadic deviation of both eyes toward the left"},
            {"letter": "E", "is_correct": False, "text": "Conjugate upward gaze deviation with eyelid flutter"}
        ],
        "correct_idx": 1,
        "explanation": "Cold water caloric testing evaluates the vestibulocochlear nerve (CN VIII), vestibular nuclei, MLF, and abducens/oculomotor nuclei (CN VI, III). In an alert awake patient, cold water induces slow tonic deviation toward the irrigated ear followed by fast corrective saccades away (COWS: Cold Opposite, Warm Same). However, in a comatose patient with an INTACT brainstem, the cortical corrective saccades are lost, resulting in sustained slow conjugate deviation toward the cold-irrigated ear. Absence of any eye deviation indicates brainstem death.",
        "high_yield_pearl": "High-Yield Clinical Pearl: In a comatose patient with intact brainstem reflexes, cold caloric irrigation produces slow tonic conjugate deviation toward the cold ear; complete absence of movement indicates brain death.",
        "image": None
    })

    # =========================================================================
    # UNIT 9: DEMENTIA & NEURODEGENERATIVE COGNITIVE DISORDERS (15 Qs: Q109 - Q123, 10%)
    # =========================================================================

    # Q109
    qs.append({
        "id": "exam3_in_house_like_g_q109",
        "q_num": "109",
        "stem": "A 74-year-old woman presents with progressive memory loss and disorientation over 3 years. Postmortem histopathology of the cerebral cortex reveals spherical extracellular deposits containing amyloid-beta peptide surrounded by dystrophic neurites, and flame-shaped intracellular neurofibrillary tangles. The intracellular neurofibrillary tangles are primarily composed of which of the following abnormally modified proteins?",
        "category": "Dementia",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Aggregated alpha-synuclein with ubiquitin tags"},
            {"letter": "B", "is_correct": True, "text": "Hyperphosphorylated microtubule-associated tau protein"},
            {"letter": "C", "is_correct": False, "text": "Misfolded prion protein in beta-pleated conformation"},
            {"letter": "D", "is_correct": False, "text": "Polyglutamine repeat expansion huntingtin protein"},
            {"letter": "E", "is_correct": False, "text": "Transactive response DNA-binding protein 43 aggregates"}
        ],
        "correct_idx": 1,
        "explanation": "Alzheimer disease is characterized by two cardinal neuropathologic hallmarks: extracellular senile (neuritic) plaques composed of cleaved amyloid-beta (Abeta42) peptide aggregates, and intracellular neurofibrillary tangles (NFTs) composed of hyperphosphorylated tau protein. Tau normally stabilizes axonal microtubules; when hyperphosphorylated, it detaches from microtubules and aggregates into insoluble paired helical filaments, causing microtubule collapse and neuronal death.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Alzheimer disease pathology features extracellular Abeta plaques and intracellular neurofibrillary tangles composed of hyperphosphorylated tau protein.",
        "image": None
    })

    # Q110
    qs.append({
        "id": "exam3_in_house_like_g_q110",
        "q_num": "110",
        "stem": "A 45-year-old woman with a family history of early-onset dementia in her mother and maternal grandfather presents with progressive memory impairment and executive dysfunction. Genetic analysis confirms a missense mutation in the presenilin-1 (PSEN1) gene on chromosome 14. Which of the following enzymatic complexes is altered by this pathogenic mutation, leading to accelerated production of neurotoxic amyloid-beta 42 peptides?",
        "category": "Dementia",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Alpha-secretase shedding non-amyloidogenic peptide"},
            {"letter": "B", "is_correct": True, "text": "Gamma-secretase transmembrane intramembrane protease"},
            {"letter": "C", "is_correct": False, "text": "Beta-secretase aspartyl protease cleavage complex"},
            {"letter": "D", "is_correct": False, "text": "Neprilysin zinc-dependent metalloprotease enzyme"},
            {"letter": "E", "is_correct": False, "text": "Insulin-degrading enzyme clearance protein complex"}
        ],
        "correct_idx": 1,
        "explanation": "Early-onset familial Alzheimer disease (<60 years) is caused by autosomal dominant mutations in amyloid precursor protein (APP on chr 21), presenilin-1 (PSEN1 on chr 14, most common cause), or presenilin-2 (PSEN2 on chr 1). Presenilins form the catalytic core of the gamma-secretase complex. Mutations in PSEN1 alter gamma-secretase cleavage of APP, favoring the generation of longer, highly fibrillogenic, and neurotoxic Abeta42 peptides.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Early-onset familial AD is caused by mutations in APP (chr 21), PSEN1 (chr 14, gamma-secretase), or PSEN2 (chr 1). Late-onset AD is associated with the ApoE epsilon-4 allele.",
        "image": None
    })

    # Q111
    qs.append({
        "id": "exam3_in_house_like_g_q111",
        "q_num": "111",
        "stem": "A 72-year-old woman with mild Alzheimer disease is started on donepezil to slow the progression of her cognitive symptoms. The physician explains that this medication improves cognitive function by enhancing cholinergic neurotransmission across the cerebral cortex. Atrophy and degeneration of which of the following subcortical nuclei is the primary anatomical source of the profound cholinergic deficit in Alzheimer disease?",
        "category": "Dementia",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Substantia nigra pars compacta in the rostral midbrain"},
            {"letter": "B", "is_correct": True, "text": "Basal nucleus of Meynert in the anterior basal forebrain"},
            {"letter": "C", "is_correct": False, "text": "Locus coeruleus in the dorsal rostral pons tegmentum"},
            {"letter": "D", "is_correct": False, "text": "Dorsal raphe nucleus in the midline midbrain brainstem"},
            {"letter": "E", "is_correct": False, "text": "Ventral tegmental area in the paramedian midbrain"}
        ],
        "correct_idx": 1,
        "explanation": "The most striking neurochemical disturbance in Alzheimer disease is a marked deficiency of acetylcholine. The anatomical basis of this deficit is the selective degeneration and atrophy of cholinergic neurons in the basal nucleus of Meynert (substantia innominata) in the basal forebrain, which provides widespread cholinergic projections to the neocortex and hippocampus. Cholinesterase inhibitors (donepezil, rivastigmine, galantamine) reversibly inhibit acetylcholinesterase, prolonging acetylcholine availability in the synaptic cleft.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Alzheimer disease causes selective degeneration of cholinergic neurons in the basal nucleus of Meynert; treat with cholinesterase inhibitors (donepezil, rivastigmine, galantamine).",
        "image": None
    })

    # Q112
    qs.append({
        "id": "exam3_in_house_like_g_q112",
        "q_num": "112",
        "stem": "A 71-year-old man presents with progressive cognitive fluctuations, daytime sleepiness, and episodes where he vividly sees small children and animals playing in his living room that are not present. Physical examination reveals resting tremor, cogwheel rigidity, and bradykinesia. After being prescribed haloperidol for his hallucinations, he experiences life-threatening rigidity, extreme hyperthermia, and autonomic collapse. Which of the following is the diagnosis?",
        "category": "Dementia",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Creutzfeldt-Jakob prion spongiform encephalopathy"},
            {"letter": "B", "is_correct": True, "text": "Dementia with Lewy bodies with neuroleptic sensitivity"},
            {"letter": "C", "is_correct": False, "text": "Frontotemporal lobar degeneration behavioral variant"},
            {"letter": "D", "is_correct": False, "text": "Normal pressure hydrocephalus with gait apraxia"},
            {"letter": "E", "is_correct": False, "text": "Progressive supranuclear palsy with vertical gaze palsy"}
        ],
        "correct_idx": 1,
        "explanation": "Dementia with Lewy bodies (DLB) presents with the classic tetrad: fluctuating cognition, recurrent detailed visual hallucinations, spontaneous parkinsonism (rigidity, tremor, bradykinesia), and REM sleep behavior disorder. Patients with DLB have exquisite neuroleptic sensitivity; exposure to typical antipsychotics (e.g., haloperidol) can precipitate irreversible parkinsonism, impaired consciousness, or neuroleptic malignant syndrome.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Dementia with Lewy bodies presents with visual hallucinations, fluctuating cognition, parkinsonism, and extreme neuroleptic sensitivity; avoid typical antipsychotics.",
        "image": None
    })

    # Q113
    qs.append({
        "id": "exam3_in_house_like_g_q113",
        "q_num": "113",
        "stem": "A 73-year-old man with a 2-year history of visual hallucinations, progressive cognitive decline, and mild parkinsonian rigidity dies of aspiration pneumonia. Histopathologic examination of the cerebral cortex, substantia nigra, and locus coeruleus reveals round, eosinophilic intracytoplasmic neuronal inclusions surrounded by a pale halo. Immunohistochemical staining confirms these inclusions are primarily composed of which of the following aggregated proteins?",
        "category": "Dementia",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Hyperphosphorylated tau protein in paired filaments"},
            {"letter": "B", "is_correct": True, "text": "Alpha-synuclein protein forming Lewy body inclusions"},
            {"letter": "C", "is_correct": False, "text": "Amyloid-beta 42 protein forming extracellular plaques"},
            {"letter": "D", "is_correct": False, "text": "Prion protein scrapie conformation in cortical neuropil"},
            {"letter": "E", "is_correct": False, "text": "TDP-43 transactive response DNA-binding inclusions"}
        ],
        "correct_idx": 1,
        "explanation": "Lewy bodies are round, eosinophilic, intracytoplasmic neuronal inclusions with a dense core and a pale peripheral halo. They are composed of insoluble aggregates of alpha-synuclein (often co-aggregated with ubiquitin). In Parkinson disease, Lewy bodies are localized primarily to the substantia nigra pars compacta, whereas in Dementia with Lewy bodies (DLB), they are diffusely distributed throughout the cerebral cortex and limbic system as well as the brainstem.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Lewy bodies are intracytoplasmic eosinophilic inclusions composed of alpha-synuclein; in DLB they are widespread across cortical and subcortical neurons.",
        "image": None
    })

    # Q114
    qs.append({
        "id": "exam3_in_house_like_g_q114",
        "q_num": "114",
        "stem": "A 54-year-old man is brought by his wife due to profound personality changes over 18 months. Previously a polite accountant, he has become socially disinhibited, makes inappropriate sexual remarks, lacks empathy, and compulsively gorges on candy and sweets. Neurological testing shows preserved visuospatial skills and intact memory recall. Brain MRI reveals marked asymmetric atrophy of the anterior frontal and temporal lobes with \"knife-blade\" gyri. Which of the following conditions is most likely?",
        "category": "Dementia",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Sporadic late-onset Alzheimer neurodegenerative disease"},
            {"letter": "B", "is_correct": True, "text": "Frontotemporal lobar degeneration behavioral variant"},
            {"letter": "C", "is_correct": False, "text": "Subacute spongiform encephalopathy prion disease"},
            {"letter": "D", "is_correct": False, "text": "Multi-infarct vascular dementia with stepwise course"},
            {"letter": "E", "is_correct": False, "text": "Dementia with Lewy bodies with motor parkinsonism"}
        ],
        "correct_idx": 1,
        "explanation": "Frontotemporal lobar degeneration (FTLD / Pick disease) is the most common cause of early-onset dementia in individuals under 65 years. The behavioral variant (bvFTLD) is characterized by early and prominent social disinhibition, apathy, loss of empathy, hyperorality (compulsive overeating of sweets), and stereotyped/perseverative behaviors, with relative sparing of memory and visuospatial orientation early in the course. Gross pathology reveals severe frontal and temporal atrophy with \"knife-blade\" thinning of gyri.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Frontotemporal dementia (<65 yo) presents with personality change, social disinhibition, and hyperorality with spared memory; MRI shows marked frontal/temporal \"knife-edge\" atrophy.",
        "image": None
    })

    # Q115
    qs.append({
        "id": "exam3_in_house_like_g_q115",
        "q_num": "115",
        "stem": "A 75-year-old man with a history of severe hypertension, diabetes, and smoking presents with progressive cognitive impairment. His daughter reports that his functional decline has occurred in a distinct stepwise pattern, with sudden drops in mental clarity following transient episodes of focal arm weakness. Examination demonstrates pseudobulbar affect, brisk deep tendon reflexes, and bilateral extensor plantar responses. Brain MRI demonstrates extensive periventricular white matter hyperintensities and multifocal lacunar infarcts. What is the diagnosis?",
        "category": "Dementia",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Frontotemporal lobar degeneration behavioral variant"},
            {"letter": "B", "is_correct": True, "text": "Vascular dementia secondary to cerebrovascular disease"},
            {"letter": "C", "is_correct": False, "text": "Dementia with Lewy bodies with autonomic instability"},
            {"letter": "D", "is_correct": False, "text": "Creutzfeldt-Jakob disease with rapidly progressive course"},
            {"letter": "E", "is_correct": False, "text": "Normal pressure hydrocephalus with gait apraxia"}
        ],
        "correct_idx": 1,
        "explanation": "Vascular dementia (multi-infarct dementia / Binswanger disease) is the second most common cause of dementia. It characteristically displays a stepwise cognitive decline temporally linked to acute cerebrovascular events or progressive microvascular ischemic damage. Neurologic examination typically reveals focal pyramidal signs (hyperreflexia, Babinski sign, pseudobulbar palsy). Neuroimaging demonstrates multifocal cortical/lacunar infarcts and prominent diffuse periventricular leukoaraiosis.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Vascular dementia features stepwise cognitive decline linked to stroke events, focal pyramidal deficits, and multifocal infarcts or extensive leukoaraiosis on MRI.",
        "image": None
    })

    # Q116
    qs.append({
        "id": "exam3_in_house_like_g_q116",
        "q_num": "116",
        "stem": "A 63-year-old woman presents with rapidly progressive cognitive decline, confusion, and gait ataxia over 6 weeks. Physical examination reveals prominent myoclonic jerking of both upper extremities triggered by sudden loud noises (startle myoclonus). EEG demonstrates periodic synchronous biphasic sharp-wave complexes. Brain MRI shows hyperintensity in the cortical ribbon and basal ganglia. Cerebrospinal fluid is positive for 14-3-3 protein. Which of the following neuropathologic processes underlies this fatal condition?",
        "category": "Dementia",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Autoimmune demyelination of central white matter tracts"},
            {"letter": "B", "is_correct": True, "text": "Spongiform vacuolation of gray matter by misfolded prions"},
            {"letter": "C", "is_correct": False, "text": "Widespread perivascular infiltration by CD8+ T lymphocytes"},
            {"letter": "D", "is_correct": False, "text": "Hydrocephalus ex vacuo caused by selective Meynert loss"},
            {"letter": "E", "is_correct": False, "text": "Degeneration of nigrostriatal dopaminergic projections"}
        ],
        "correct_idx": 1,
        "explanation": "Creutzfeldt-Jakob disease (CJD) is a transmissible spongiform encephalopathy caused by conversion of normal prion protein (PrP-c, alpha-helical) into an abnormal, protease-resistant beta-pleated conformation (PrP-sc). Hallmark features include rapidly progressive dementia leading to death in months, startle-induced myoclonus, ataxia, periodic sharp-wave complexes on EEG, cortical ribboning on MRI, and positive CSF 14-3-3 protein. Neuropathology demonstrates spongiform vacuolation of the cerebral cortex.",
        "high_yield_pearl": "High-Yield Clinical Pearl: CJD presents with rapidly progressive dementia, startle myoclonus, EEG periodic sharp waves, cortical ribboning, positive CSF 14-3-3 protein, and cortical spongiform vacuolation.",
        "image": None
    })

    # Q117
    qs.append({
        "id": "exam3_in_house_like_g_q117",
        "q_num": "117",
        "stem": "A 76-year-old man presents with progressive difficulty walking over 6 months. His family notes he takes short, slow, shuffling steps as if his \"feet are glued to the floor\" (magnetic gait). Over the past 2 months, he has developed memory problems and new-onset urinary urgency and incontinence. Brain MRI shows symmetrical ventricular enlargement out of proportion to cerebral sulcal enlargement. Which of the following is the most appropriate initial diagnostic and therapeutic intervention?",
        "category": "Dementia",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Administration of high-dose intravenous methylprednisolone"},
            {"letter": "B", "is_correct": True, "text": "High-volume lumbar puncture spinal tap drainage test"},
            {"letter": "C", "is_correct": False, "text": "Oral carbidopa-levodopa dopaminergic challenge testing"},
            {"letter": "D", "is_correct": False, "text": "Emergency bilateral subthalamic deep brain stimulation"},
            {"letter": "E", "is_correct": False, "text": "Daily oral donepezil acetylcholinesterase therapy"}
        ],
        "correct_idx": 1,
        "explanation": "Normal pressure hydrocephalus (NPH) presents with the classic triad: gait disturbance (\"magnetic gait\", apraxic, wide-based, slow - typically the first and most prominent symptom), cognitive slowing/dementia, and urinary incontinence (\"wet, wacky, and wobbly\"). It is caused by impaired CSF resorption through arachnoid granulations. Removal of 30-50 mL of CSF via a high-volume lumbar puncture (Miller Fisher tap test) produces objective improvement in gait, confirming the diagnosis and predicting success with ventriculoperitoneal (VP) shunting.",
        "high_yield_pearl": "High-Yield Clinical Pearl: NPH presents with gait apraxia (\"magnetic\"), dementia, and urinary incontinence with ventriculomegaly; diagnosis confirmed by gait improvement after high-volume LP tap test; treat with VP shunt.",
        "image": None
    })

    # Q118
    qs.append({
        "id": "exam3_in_house_like_g_q118",
        "q_num": "118",
        "stem": "A 50-year-old man with severe alcohol use disorder is brought to the emergency department confused and lethargic. Neurological examination reveals bilateral horizontal nystagmus, bilateral lateral rectus palsies, and a wide-based, unsteady, slow gait. Which of the following is the most critical immediate intervention to prevent permanent neurological disability in this patient?",
        "category": "Dementia",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Administration of 50% intravenous dextrose infusion first"},
            {"letter": "B", "is_correct": True, "text": "Intravenous thiamine administration prior to glucose"},
            {"letter": "C", "is_correct": False, "text": "Intravenous haloperidol therapy for acute delirium"},
            {"letter": "D", "is_correct": False, "text": "High-volume therapeutic lumbar puncture drainage"},
            {"letter": "E", "is_correct": False, "text": "Oral chlordiazepoxide therapy for alcohol withdrawal"}
        ],
        "correct_idx": 1,
        "explanation": "Wernicke encephalopathy is caused by thiamine (vitamin B1) deficiency, classically seen in chronic alcohol use disorder. It is defined by the acute clinical triad of encephalopathy/confusion, ophthalmoplegia/nystagmus, and gait ataxia. Thiamine is a required cofactor for glucose metabolism enzymes (pyruvate dehydrogenase, alpha-ketoglutarate dehydrogenase, transketolase). Administering glucose BEFORE thiamine can acutely deplete residual thiamine stores, precipitating permanent brainstem/diencephalic damage and Korsakoff syndrome. Always give IV thiamine before glucose.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Wernicke encephalopathy presents with confusion, ataxia, and ophthalmoplegia due to B1 deficiency; always administer intravenous thiamine BEFORE intravenous glucose.",
        "image": None
    })

    # Q119
    qs.append({
        "id": "exam3_in_house_like_g_q119",
        "q_num": "119",
        "stem": "A 56-year-old man with chronic alcohol dependence who experienced an untreated episode of Wernicke encephalopathy 6 months ago is evaluated for persistent memory dysfunction. He demonstrates severe anterograde amnesia and cannot recall what he ate for breakfast. When asked how he spent his morning, he cheerfully fabricates an elaborate, detailed story about flying a helicopter to meet the mayor, entirely unaware that he is inventing the account. Bilateral necrosis and petechial hemorrhages in which of the following structures is pathognomonic for this syndrome?",
        "category": "Dementia",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Caudate nucleus and putamen of the basal ganglia"},
            {"letter": "B", "is_correct": True, "text": "Mammillary bodies and dorsomedial thalamic nuclei"},
            {"letter": "C", "is_correct": False, "text": "Dentate nucleus and superior cerebellar peduncles"},
            {"letter": "D", "is_correct": False, "text": "Substantia nigra pars compacta and subthalamic"},
            {"letter": "E", "is_correct": False, "text": "Nucleus accumbens and ventral tegmental area"},
        ],
        "correct_idx": 1,
        "explanation": "Korsakoff syndrome is a chronic, largely irreversible neurocognitive disorder that develops as a sequel to untreated or inadequately treated Wernicke encephalopathy. Cardinal features include dense anterograde and retrograde amnesia, confabulation (inventing memories without intent to deceive), and lack of insight. Neuropathology characteristically reveals bilateral petechial hemorrhages, necrosis, and hemosiderin deposition in the mammillary bodies and the dorsomedial nuclei of the thalamus.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Korsakoff syndrome features irreversible anterograde amnesia and confabulation caused by thiamine deficiency; pathology reveals bilateral mammillary body and thalamic necrosis.",
        "image": None
    })

    # Q120
    qs.append({
        "id": "exam3_in_house_like_g_q120",
        "q_num": "120",
        "stem": "Patient H.M. underwent bilateral surgical resection of the medial temporal lobes, including the hippocampi and amygdalae, for intractable epilepsy. Following surgery, he developed complete anterograde amnesia, unable to form new episodic or semantic memories. However, when trained on a mirror-tracing motor task, his performance improved steadily over successive days at a normal rate, despite having no conscious memory of having ever seen the apparatus before. Which of the following memory systems was intact in this patient?",
        "category": "Dementia",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Episodic autobiographical declarative memory system"},
            {"letter": "B", "is_correct": True, "text": "Procedural non-declarative motor skill memory system"},
            {"letter": "C", "is_correct": False, "text": "Semantic factual declarative knowledge memory system"},
            {"letter": "D", "is_correct": False, "text": "Anterograde long-term explicit conscious memory"},
            {"letter": "E", "is_correct": False, "text": "Short-term consolidation of verbal episodic memories"}
        ],
        "correct_idx": 1,
        "explanation": "Memory is categorized into declarative (explicit: episodic autobiographical events and semantic factual knowledge) and non-declarative (implicit: procedural motor skills, habits, and classical conditioning). Declarative memory consolidation depends on the medial temporal lobes and hippocampi. Non-declarative procedural motor memory (e.g., mirror-tracing, riding a bicycle) depends on the basal ganglia (striatum), cerebellum, and supplementary motor cortex. H.M. had intact procedural memory despite profound anterograde declarative amnesia.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Medial temporal lobes/hippocampi consolidate declarative (episodic/semantic) memory. Procedural motor memory (non-declarative) relies on the basal ganglia and cerebellum.",
        "image": None
    })

    # Q121
    qs.append({
        "id": "exam3_in_house_like_g_q121",
        "q_num": "121",
        "stem": "The Papez circuit is a fundamental anatomical pathway of the limbic system that interconnects the hippocampus with subcortical and cortical structures involved in emotional processing and memory consolidation. In this circuit, efferent axonal projections originate in the hippocampus, travel through the fornix, and synapse in which of the following structures before activity is relayed to the anterior nucleus of the thalamus?",
        "category": "Dementia",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Centromedian nucleus of the intralaminar thalamus"},
            {"letter": "B", "is_correct": True, "text": "Mammillary bodies via the postcommissural fornix"},
            {"letter": "C", "is_correct": False, "text": "Cingulate gyrus via the cingulum white matter tract"},
            {"letter": "D", "is_correct": False, "text": "Entorhinal cortex via the perforant white pathway"},
            {"letter": "E", "is_correct": False, "text": "Nucleus accumbens via the stria terminalis bundle"}
        ],
        "correct_idx": 1,
        "explanation": "The classic Papez circuit flows in an orderly loop: Hippocampus -> via the Fornix -> Mammillary bodies -> via the Mammillothalamic tract -> Anterior nucleus of the thalamus -> via internal capsule projections -> Cingulate gyrus -> via the Cingulum bundle -> Entorhinal cortex (parahippocampal gyrus) -> via the Perforant pathway -> returning to the Hippocampus.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Papez circuit sequence: Hippocampus -> Fornix -> Mammillary bodies -> Mammillothalamic tract -> Anterior thalamus -> Cingulate gyrus -> Entorhinal cortex -> Hippocampus.",
        "image": None
    })

    # Q122
    qs.append({
        "id": "exam3_in_house_like_g_q122",
        "q_num": "122",
        "stem": "A 34-year-old man recovering from severe herpes simplex virus encephalitis exhibits dramatic behavioral changes. He demonstrates a complete lack of fear or anger when confronted with threatening situations, places inappropriate non-food objects into his mouth to explore them (hyperorality), displays intense hypersexuality with inappropriate sexual advances, and exhibits visual agnosia. Bilateral damage to which of the following anatomical structures is responsible for this constellation of symptoms?",
        "category": "Dementia",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Ventromedial hypothalamic satiety center nuclei"},
            {"letter": "B", "is_correct": True, "text": "Amygdala and adjacent anterior temporal lobar cortex"},
            {"letter": "C", "is_correct": False, "text": "Dorsolateral prefrontal executive cognitive cortex"},
            {"letter": "D", "is_correct": False, "text": "Mammillary bodies and anterior thalamic nuclei"},
            {"letter": "E", "is_correct": False, "text": "Septal nuclei and anterior cingulate gyrus cortex"}
        ],
        "correct_idx": 1,
        "explanation": "Klüver-Bucy syndrome results from bilateral destruction of the anterior temporal lobes, specifically the amygdalae. Cardinal manifestations include: placidity/docility (loss of normal fear and aggression responses), hyperorality (exploring objects with the mouth), hypersexuality, psychic blindness (visual agnosia: inability to recognize objects by sight), and hyperphagia/bulimia. HSV-1 encephalitis is the classic etiology in humans due to its tropism for temporal lobe cortex.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Klüver-Bucy syndrome is caused by bilateral amygdala damage (e.g., HSV-1); features docility (loss of fear), hyperorality, hypersexuality, and visual agnosia.",
        "image": None
    })

    # Q123
    qs.append({
        "id": "exam3_in_house_like_g_q123",
        "q_num": "123",
        "stem": "A neurobiology researcher is investigating the neural circuitry of motivation, positive reinforcement, and substance use disorders. She demonstrates that rewarding stimuli (such as food, sex, and drugs of abuse like cocaine and opioids) cause a robust surge in extracellular neurotransmitter levels within the nucleus accumbens. Neurons projecting from which of the following brainstem regions provide the primary dopaminergic input to the nucleus accumbens in this mesolimbic pathway?",
        "category": "Dementia",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Substantia nigra pars compacta of the midbrain"},
            {"letter": "B", "is_correct": True, "text": "Ventral tegmental area of the ventral midbrain"},
            {"letter": "C", "is_correct": False, "text": "Locus coeruleus of the dorsal rostral pons tegmentum"},
            {"letter": "D", "is_correct": False, "text": "Dorsal raphe nucleus of the central brainstem"},
            {"letter": "E", "is_correct": False, "text": "Basal nucleus of Meynert of the basal forebrain"}
        ],
        "correct_idx": 1,
        "explanation": "The mesolimbic reward pathway consists of dopaminergic neurons in the ventral tegmental area (VTA) of the midbrain projecting to the nucleus accumbens (in the ventral striatum). This pathway is the principal neural circuit governing motivation, drive, incentive salience, and positive reinforcement. Natural rewards as well as addictive substances trigger dopamine release in the nucleus accumbens, reinforcing substance-seeking behavior.",
        "high_yield_pearl": "High-Yield Clinical Pearl: The mesolimbic reward circuit consists of dopaminergic projections from the ventral tegmental area (VTA) to the nucleus accumbens, driving motivation and addiction.",
        "image": None
    })

    # =========================================================================
    # UNIT 5: CBIL: EPILEPSY & SEIZURE DISORDERS (27 Qs: Q124 - Q150, 18%)
    # =========================================================================

    # Q124
    qs.append({
        "id": "exam3_in_house_like_g_q124",
        "q_num": "124",
        "stem": "A 23-year-old woman is evaluated following a seizure. Her roommate reports that the patient experienced an initial rising epigastric sensation, followed by 90 seconds of blank staring, lip smacking, and fumbling with her buttons. She was unresponsive to questions during the event and had 15 minutes of confusion afterward. According to the International League Against Epilepsy (ILAE) classification, which of the following terms describes this seizure?",
        "category": "CBIL Epilepsy",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Focal aware motor seizure with jacksonian march"},
            {"letter": "B", "is_correct": True, "text": "Focal impaired awareness seizure with automatisms"},
            {"letter": "C", "is_correct": False, "text": "Generalized typical absence seizure without aura"},
            {"letter": "D", "is_correct": False, "text": "Generalized myoclonic seizure with consciousness"},
            {"letter": "E", "is_correct": False, "text": "Generalized atonic drop attack seizure episode"}
        ],
        "correct_idx": 1,
        "explanation": "Under the 2017 ILAE classification, seizures originating within networks limited to one cerebral hemisphere are classified as focal. When awareness of self and environment is compromised at any point during the seizure, it is designated a \"focal impaired awareness seizure.\" Characteristic features of temporal lobe origin include an epigastric rising aura, staring, automatisms (manual fumbling, lip smacking/chewing), and postictal confusion.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Focal impaired awareness seizures originate in one hemisphere (commonly temporal), feature auras, automatisms (lip smacking), and postictal confusion.",
        "image": None
    })

    # Q125
    qs.append({
        "id": "exam3_in_house_like_g_q125",
        "q_num": "125",
        "stem": "A 28-year-old man presents with pharmacoresistant focal epilepsy. His seizures begin with an aura of intense déjà vu and an unpleasant metallic taste, followed by impaired awareness, right-hand dystonic posturing, and left-hand repetitive automatisms. High-resolution brain MRI demonstrates unilateral volume loss and T2/FLAIR hyperintensity in the hippocampus. Which of the following histopathologic processes is characteristically observed in surgical resection specimens of this lesion?",
        "category": "CBIL Epilepsy",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Perivascular cuffing by CD4+ and CD8+ lymphocytes"},
            {"letter": "B", "is_correct": True, "text": "Selective neuronal loss with dense fibrillary astrogliosis"},
            {"letter": "C", "is_correct": False, "text": "Extracellular amyloid-beta neuritic plaque deposition"},
            {"letter": "D", "is_correct": False, "text": "Spongiform vacuolation within gray matter neuropil"},
            {"letter": "E", "is_correct": False, "text": "Intracytoplasmic inclusions composed of alpha-synuclein"}
        ],
        "correct_idx": 1,
        "explanation": "Mesial temporal sclerosis (hippocampal sclerosis) is the most common pathology found in adults with drug-resistant temporal lobe epilepsy. Neuroimaging shows hippocampal atrophy and hyperintensity on T2/FLAIR. Histopathology demonstrates selective pyramidal neuronal loss in the CA1 and CA4 subfields of the hippocampus and dentate gyrus, accompanied by dense fibrillary astrogliosis. Anterior temporal lobectomy provides seizure freedom in >70-80% of refractory cases.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Mesial temporal sclerosis (hippocampal sclerosis) is the leading cause of refractory temporal lobe epilepsy; pathology shows hippocampal pyramidal cell loss and astrogliosis.",
        "image": None
    })

    # Q126
    qs.append({
        "id": "exam3_in_house_like_g_q126",
        "q_num": "126",
        "stem": "An 8-year-old girl is brought by her parents because her teacher noticed multiple brief episodes each day where she suddenly stops talking, stares blankly into space for 5 to 10 seconds, and exhibits eyelid fluttering. She immediately resumes her previous activity without any confusion. In the clinic, hyperventilation for 3 minutes triggers an identical episode. Routine electroencephalography demonstrates generalized 3-Hz spike-and-wave discharges. Which of the following is the first-line medication?",
        "category": "CBIL Epilepsy",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Carbamazepine sodium channel blocker therapy"},
            {"letter": "B", "is_correct": True, "text": "Ethosuximide calcium channel blocker therapy"},
            {"letter": "C", "is_correct": False, "text": "Phenytoin sodium channel blocker pharmacotherapy"},
            {"letter": "D", "is_correct": False, "text": "Phenobarbital barbiturate GABA receptor therapy"},
            {"letter": "E", "is_correct": False, "text": "Gabapentin calcium channel alpha-2-delta therapy"}
        ],
        "correct_idx": 1,
        "explanation": "Typical absence (petit mal) seizures present in childhood with frequent, brief (5-10 second) staring spells, eyelid fluttering, immediate recovery of consciousness, and NO postictal confusion. They are characteristically provoked by hyperventilation. The EEG is pathognomonic: generalized, symmetric, synchronous 3-Hz spike-and-wave discharges. Ethosuximide is the first-line pharmacotherapy for isolated absence seizures due to its high efficacy and favorable safety profile.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Absence seizures feature brief staring spells with NO postictal period and 3-Hz spike-wave complexes on EEG triggered by hyperventilation; ethosuximide is first-line.",
        "image": None
    })

    # Q127
    qs.append({
        "id": "exam3_in_house_like_g_q127",
        "q_num": "127",
        "stem": "An 8-year-old boy with newly diagnosed absence epilepsy is prescribed ethosuximide. The pediatric neurologist explains to the parents that the medication works by blocking a specific class of ion channels in thalamocortical relay neurons, thereby suppressing the synchronized rhythmic oscillatory burst discharges that generate absence seizures. Which of the following ion channels is the specific pharmacological target of ethosuximide?",
        "category": "CBIL Epilepsy",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "High-voltage-activated P/Q-type calcium channels"},
            {"letter": "B", "is_correct": True, "text": "Low-voltage-activated T-type calcium channels"},
            {"letter": "C", "is_correct": False, "text": "Voltage-gated fast-inactivating sodium channels"},
            {"letter": "D", "is_correct": False, "text": "Inwardly rectifying potassium channel complexes"},
            {"letter": "E", "is_correct": False, "text": "Ligand-gated chloride channels of GABA-A complex"}
        ],
        "correct_idx": 1,
        "explanation": "Ethosuximide exerts its antiepileptic effect by selectively blocking low-voltage-activated T-type calcium channels in thalamic relay neurons. Thalamic T-type calcium currents are responsible for generating the rhythmic, oscillatory burst firing between the thalamus and cortex that produces the characteristic 3-Hz spike-and-wave discharges of absence seizures.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Ethosuximide selectively blocks low-voltage T-type calcium channels in thalamic relay neurons, disrupting the 3-Hz spike-and-wave rhythm of absence seizures.",
        "image": None
    })

    # Q128
    qs.append({
        "id": "exam3_in_house_like_g_q128",
        "q_num": "128",
        "stem": "A 16-year-old boy presents after experiencing a generalized tonic-clonic seizure that occurred 30 minutes after waking up on a Saturday morning following a night of sleep deprivation. On further questioning, he reveals that for the past year, he has had frequent brief, involuntary \"shock-like\" jerks of both arms in the morning, which have caused him to drop his phone and spill orange juice. Interictal EEG demonstrates generalized 4- to 6-Hz polyspike-and-wave discharges. Which of the following is the drug of choice?",
        "category": "CBIL Epilepsy",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Carbamazepine narrow-spectrum sodium channel drug"},
            {"letter": "B", "is_correct": True, "text": "Valproic acid broad-spectrum antiepileptic drug"},
            {"letter": "C", "is_correct": False, "text": "Phenytoin narrow-spectrum sodium channel agent"},
            {"letter": "D", "is_correct": False, "text": "Gabapentin calcium alpha-2-delta subunit ligand"},
            {"letter": "E", "is_correct": False, "text": "Vigabatrin GABA transaminase inhibitor medication"}
        ],
        "correct_idx": 1,
        "explanation": "Juvenile myoclonic epilepsy (JME / Janz syndrome) is an idiopathic generalized epilepsy presenting in adolescence. Cardinal features include bilateral morning myoclonic jerks (dropping objects after waking), generalized tonic-clonic seizures, and occasional absence seizures, typically provoked by sleep deprivation and alcohol. EEG shows generalized 4-6 Hz polyspike-and-wave complexes. Valproic acid (broad-spectrum) is the first-line medication of choice in males; narrow-spectrum sodium channel blockers (carbamazepine, phenytoin) can worsen myoclonic seizures.",
        "high_yield_pearl": "High-Yield Clinical Pearl: JME presents with morning myoclonic jerks and tonic-clonic seizures provoked by sleep loss; EEG shows 4-6 Hz polyspike-waves; valproate is first-line; carbamazepine/phenytoin worsen JME.",
        "image": None
    })

    # Q129
    qs.append({
        "id": "exam3_in_house_like_g_q129",
        "q_num": "129",
        "stem": "A 17-year-old male with generalized epilepsy who recently started valproic acid therapy presents to the emergency department with severe epigastric abdominal pain radiating to his back, accompanied by nausea and persistent vomiting. Physical examination reveals marked epigastric tenderness with guarding. Serum lipase is markedly elevated at 1,450 U/L (normal <60 U/L). Which of the following sets of adverse effects is specifically associated with valproate therapy?",
        "category": "CBIL Epilepsy",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Aplastic anemia, agranulocytosis, and hyponatremia"},
            {"letter": "B", "is_correct": True, "text": "Hepatotoxicity, acute pancreatitis, and neural tube defects"},
            {"letter": "C", "is_correct": False, "text": "Gingival hyperplasia, hirsutism, and osteomalacia"},
            {"letter": "D", "is_correct": False, "text": "Irreversible concentric peripheral visual field loss"},
            {"letter": "E", "is_correct": False, "text": "Nephrolithiasis, hypohidrosis, and angle-closure glaucoma"}
        ],
        "correct_idx": 1,
        "explanation": "Valproic acid (divalproex sodium) is a broad-spectrum antiepileptic agent that blocks voltage-gated Na+ channels, blocks T-type Ca2+ channels, and elevates GABA levels. Notable black box warnings and severe adverse effects include: fatal hepatotoxicity (highest in children <2 years), acute hemorrhagic pancreatitis (as seen here), weight gain, alopecia, hyperammonemia, and high teratogenicity causing neural tube defects (spina bifida).",
        "high_yield_pearl": "High-Yield Clinical Pearl: Valproic acid black box warnings: fatal hepatotoxicity, acute pancreatitis, and high teratogenicity (neural tube defects). Also causes weight gain and tremor.",
        "image": None
    })

    # Q130
    qs.append({
        "id": "exam3_in_house_like_g_q130",
        "q_num": "130",
        "stem": "A 35-year-old man is brought to the emergency department actively convulsing with continuous generalized tonic-clonic motor activity that has lasted for 12 minutes without interruption. Capillary blood glucose is 115 mg/dL. He has had continuous airway management and high-flow oxygen. According to standard clinical guidelines for the management of status epilepticus, which of the following is the most appropriate first-line pharmacotherapeutic agent?",
        "category": "CBIL Epilepsy",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Intravenous levetiracetam non-sedating antiepileptic"},
            {"letter": "B", "is_correct": True, "text": "Intravenous lorazepam benzodiazepine receptor agonist"},
            {"letter": "C", "is_correct": False, "text": "Intravenous fosphenytoin sodium channel blocker agent"},
            {"letter": "D", "is_correct": False, "text": "Intravenous sodium valproate broad-spectrum agent"},
            {"letter": "E", "is_correct": False, "text": "Intravenous continuous propofol general anesthetic"}
        ],
        "correct_idx": 1,
        "explanation": "Status epilepticus is defined as >=5 minutes of continuous clinical/electrographic seizure activity, or >=2 discrete seizures without complete recovery of consciousness between events. First-line therapy (emergent phase, 5-20 min) is an intravenous benzodiazepine (IV lorazepam 0.1 mg/kg or IV diazepam; or IM midazolam if no IV access). If seizures continue beyond 20 minutes, second-line urgent therapy is an IV non-sedating AED (levetiracetam, fosphenytoin, or valproate).",
        "high_yield_pearl": "High-Yield Clinical Pearl: Status epilepticus (>5 min) stepwise protocol: 1st line = IV lorazepam (or IM midazolam); 2nd line = IV levetiracetam, fosphenytoin, or valproate; 3rd line = general anesthesia.",
        "image": None
    })

    # Q131
    qs.append({
        "id": "exam3_in_house_like_g_q131",
        "q_num": "131",
        "stem": "Benzodiazepines (such as lorazepam and diazepam) and barbiturates (such as phenobarbital) are both allosteric modulators of the ionotropic GABA-A receptor complex, enhancing chloride conductance and hyperpolarizing neuronal membranes. Which of the following electrophysiologic mechanisms correctly contrasts the primary action of benzodiazepines with that of barbiturates at this receptor?",
        "category": "CBIL Epilepsy",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Benzodiazepines prolong duration; barbiturates increase frequency"},
            {"letter": "B", "is_correct": True, "text": "Benzodiazepines increase frequency; barbiturates prolong duration"},
            {"letter": "C", "is_correct": False, "text": "Benzodiazepines block reuptake; barbiturates block degradation"},
            {"letter": "D", "is_correct": False, "text": "Benzodiazepines open potassium; barbiturates open chloride"},
            {"letter": "E", "is_correct": False, "text": "Benzodiazepines close sodium; barbiturates open calcium"}
        ],
        "correct_idx": 1,
        "explanation": "Both benzodiazepines and barbiturates bind distinct allosteric sites on the GABA-A receptor-chloride channel complex. The classic distinction is: \"Frenzodiazepines increase Frequency of channel opening\" (shift dose-response curve to the left), whereas \"BarbiDURATes increase DURATION of channel opening\" (and at high doses can directly gate chloride channels even in the absence of GABA, accounting for their greater risk of fatal respiratory depression).",
        "high_yield_pearl": "High-Yield Clinical Pearl: Benzodiazepines increase the FREQUENCY of GABA-A chloride channel opening; Barbiturates increase the DURATION of opening (and directly open channels at high doses).",
        "image": None
    })

    # Q132
    qs.append({
        "id": "exam3_in_house_like_g_q132",
        "q_num": "132",
        "stem": "A 32-year-old man with focal epilepsy has been taking phenytoin for 2 years. On routine dental examination, his dentist observes extensive, firm, pink, non-tender nodular overgrowth of the gingiva that covers more than half of his mandibular and maxillary incisors. Platelet count and coagulation profile are completely normal. Which of the following mechanisms is responsible for this patient's gingival enlargement?",
        "category": "CBIL Epilepsy",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Microvascular capillary proliferation induced by VEGF"},
            {"letter": "B", "is_correct": True, "text": "Increased platelet-derived growth factor stimulating fibroblasts"},
            {"letter": "C", "is_correct": False, "text": "Autoimmune immune complex vasculitis of gingival margin"},
            {"letter": "D", "is_correct": False, "text": "Chronic granulomatous inflammation from oral spirochetes"},
            {"letter": "E", "is_correct": False, "text": "Excessive collagen breakdown caused by metalloproteinases"}
        ],
        "correct_idx": 1,
        "explanation": "Gingival hyperplasia occurs in ~50% of patients receiving chronic phenytoin therapy. Phenytoin increases the secretion of platelet-derived growth factor (PDGF) by gingival fibroblasts and macrophages. When exposed to PDGF, gingival fibroblasts proliferate and produce excessive amounts of extracellular collagen matrix, resulting in benign nodular gingival overgrowth. Good oral hygiene and drug discontinuation (or switching to another AED) typically reverse the condition.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Phenytoin causes gingival hyperplasia mediated by PDGF-driven fibroblast proliferation and collagen synthesis. Also causes hirsutism, ataxia, and folate deficiency.",
        "image": None
    })

    # Q133
    qs.append({
        "id": "exam3_in_house_like_g_q133",
        "q_num": "133",
        "stem": "A 54-year-old woman with trigeminal neuralgia is started on carbamazepine. Six weeks later, she presents with severe sore throat, oral mucosal ulcerations, and fever. Complete blood count demonstrates a white blood cell count of 1,200/uL with an absolute neutrophil count of 180/uL (normal 1,500-8,000/uL), hemoglobin 12.8 g/dL, and platelets 185,000/uL. Which of the following adverse hematologic reactions to carbamazepine is this patient experiencing?",
        "category": "CBIL Epilepsy",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Immune thrombocytopenic purpura with megakaryocytes"},
            {"letter": "B", "is_correct": True, "text": "Dose-independent idiosyncratic severe agranulocytosis"},
            {"letter": "C", "is_correct": False, "text": "Autoimmune Coombs-positive hemolytic anemia reaction"},
            {"letter": "D", "is_correct": False, "text": "Megaloblastic macrocytic anemia from folate deficiency"},
            {"letter": "E", "is_correct": False, "text": "Polycythemia vera with erythroid hyperplasia expansion"}
        ],
        "correct_idx": 1,
        "explanation": "Carbamazepine is a first-line agent for focal seizures and the drug of choice for trigeminal neuralgia. It can cause dangerous hematologic toxicities, including benign transient leukopenia, but also severe idiosyncratic agranulocytosis (severe neutropenia <500/uL presenting with fever, sore throat, and mouth ulcers) and fatal aplastic anemia. Other significant carbamazepine adverse effects include SIADH (hyponatremia), Stevens-Johnson syndrome, and hepatic CYP450 autoinduction.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Carbamazepine adverse effects: agranulocytosis/aplastic anemia, SIADH (hyponatremia), Stevens-Johnson syndrome (HLA-B*1502), and potent CYP450 enzyme induction.",
        "image": None
    })

    # Q134
    qs.append({
        "id": "exam3_in_house_like_g_q134",
        "q_num": "134",
        "stem": "A 26-year-old woman with focal epilepsy is initiated on lamotrigine monotherapy. The neurologist emphasizes that the medication must be titrated upward very slowly over a period of 6 to 8 weeks according to a strict dosing schedule. Which of the following life-threatening adverse reactions is specifically prevented by adhering to this slow dosage titration protocol?",
        "category": "CBIL Epilepsy",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Acute hemorrhagic pancreatitis with pancreatic necrosis"},
            {"letter": "B", "is_correct": True, "text": "Stevens-Johnson syndrome and toxic epidermal necrolysis"},
            {"letter": "C", "is_correct": False, "text": "Fulminant hepatic necrosis with acute liver failure"},
            {"letter": "D", "is_correct": False, "text": "Irreversible bilateral concentric visual field constriction"},
            {"letter": "E", "is_correct": False, "text": "Acute angle-closure glaucoma with visual field loss"}
        ],
        "correct_idx": 1,
        "explanation": "Lamotrigine blocks voltage-gated Na+ channels and inhibits excitatory glutamate release. The most feared adverse effect is a severe, life-threatening hypersensitivity cutaneous reaction, including Stevens-Johnson syndrome (SJS) and toxic epidermal necrolysis (TEN). The risk is strongly correlated with rapid initial dose escalation or high starting doses. Slow titration over several weeks drastically reduces the incidence of severe skin rashes. Adding valproate inhibits lamotrigine metabolism, doubling its half-life and requiring a 50% dose reduction.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Lamotrigine requires slow dose titration to prevent life-threatening Stevens-Johnson syndrome (SJS/TEN); valproate inhibits lamotrigine metabolism, markedly increasing SJS risk.",
        "image": None
    })

    # Q135
    qs.append({
        "id": "exam3_in_house_like_g_q135",
        "q_num": "135",
        "stem": "A 29-year-old man with newly diagnosed focal impaired awareness seizures is started on levetiracetam. He achieves excellent seizure freedom, but 3 weeks later his partner reports that he has become uncharacteristically irritable, aggressive, hostile, and depressed. He has no prior psychiatric history. Which of the following cellular structures is the primary pharmacological binding target of levetiracetam?",
        "category": "CBIL Epilepsy",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Alpha-2-delta subunit of voltage-gated calcium channels"},
            {"letter": "B", "is_correct": True, "text": "Synaptic vesicle glycoprotein SV2A in axon terminals"},
            {"letter": "C", "is_correct": False, "text": "GABA transporter GAT-1 in perisynaptic glial membranes"},
            {"letter": "D", "is_correct": False, "text": "Fast-inactivating voltage-gated sodium channel alpha"},
            {"letter": "E", "is_correct": False, "text": "GABA transaminase enzyme within mitochondrial matrix"}
        ],
        "correct_idx": 1,
        "explanation": "Levetiracetam (Keppra) has a unique mechanism of action: it binds selectively to synaptic vesicle protein 2A (SV2A) on presynaptic vesicle membranes, inhibiting exocytosis of excitatory neurotransmitters (such as glutamate). It is broad-spectrum, effective for focal and generalized seizures, and has no hepatic CYP450 interactions (renal clearance). Its major clinically significant adverse effects are behavioral and psychiatric, including irritability, hostility, anxiety, agitation, and depression.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Levetiracetam binds synaptic vesicle protein SV2A to inhibit neurotransmitter exocytosis; lacks CYP interactions, but can cause irritability, aggression, and depression.",
        "image": None
    })

    # Q136
    qs.append({
        "id": "exam3_in_house_like_g_q136",
        "q_num": "136",
        "stem": "A 31-year-old woman with epilepsy and chronic migraine headaches is started on topiramate. At her 3-month follow-up, she has lost 12 pounds, but complains of mental fog, word-finding difficulty, and slowed thinking (\"Dopamax\" effect). She also reports an episode of sudden right flank pain and hematuria, with ultrasound confirming a calcium phosphate renal stone. Which of the following pharmacological properties of topiramate contributes to nephrolithiasis?",
        "category": "CBIL Epilepsy",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Potent induction of hepatic cytochrome P450 isoenzymes"},
            {"letter": "B", "is_correct": True, "text": "Inhibition of renal tubular carbonic anhydrase activity"},
            {"letter": "C", "is_correct": False, "text": "Blockade of presynaptic T-type calcium ion channels"},
            {"letter": "D", "is_correct": False, "text": "Direct agonism of postsynaptic AMPA glutamate receptors"},
            {"letter": "E", "is_correct": False, "text": "Irreversible inhibition of mitochondrial GABA transaminase"}
        ],
        "correct_idx": 1,
        "explanation": "Topiramate is a multifaceted broad-spectrum AED that blocks Na+ channels, potentiates GABA-A receptors, and antagonizes AMPA receptors. It also acts as a weak carbonic anhydrase inhibitor. In the kidneys, carbonic anhydrase inhibition decreases bicarbonate reabsorption, leading to metabolic acidosis, alkalinization of the urine, and hypocitraturia, which strongly promotes precipitation of calcium phosphate kidney stones (nephrolithiasis). Other side effects include cognitive slowing (\"Dopamax\"), weight loss, and acute angle-closure glaucoma.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Topiramate causes cognitive slowing (\"Dopamax\"), weight loss, and kidney stones (due to carbonic anhydrase inhibition alkalinizing urine). Also causes acute glaucoma.",
        "image": None
    })

    # Q137
    qs.append({
        "id": "exam3_in_house_like_g_q137",
        "q_num": "137",
        "stem": "A 9-month-old infant with tuberous sclerosis presents with clusters of sudden flexion spasms of the neck, trunk, and extremities (infantile spasms / West syndrome). Hypsarrhythmia is confirmed on EEG. The pediatric neurologist prescribes vigabatrin, which is particularly effective for infantile spasms in tuberous sclerosis. Which of the following permanent, irreversible adverse effects requires regular ophthalmologic visual field surveillance with this drug?",
        "category": "CBIL Epilepsy",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Bilateral posterior subcapsular cataract opacification"},
            {"letter": "B", "is_correct": True, "text": "Concentric bilateral peripheral visual field constriction"},
            {"letter": "C", "is_correct": False, "text": "Ischemic anterior optic neuropathy with altitudinal loss"},
            {"letter": "D", "is_correct": False, "text": "Central scotoma from macular pigmentary degeneration"},
            {"letter": "E", "is_correct": False, "text": "Severe persistent corneal verticillata microdeposits"}
        ],
        "correct_idx": 1,
        "explanation": "Vigabatrin is an irreversible inhibitor of GABA transaminase (GABA-T), the enzyme responsible for catabolizing GABA, thereby increasing brain GABA concentrations. It is first-line for infantile spasms associated with tuberous sclerosis. However, vigabatrin carries a black box warning for permanent, irreversible concentric peripheral visual field constriction (retinal toxicity occurring in 30-40% of patients), necessitating baseline and periodic perimetry testing.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Vigabatrin irreversibly inhibits GABA transaminase; used for infantile spasms in tuberous sclerosis; causes permanent irreversible concentric visual field constriction.",
        "image": None
    })

    # Q138
    qs.append({
        "id": "exam3_in_house_like_g_q138",
        "q_num": "138",
        "stem": "A 58-year-old man with diabetic peripheral neuropathy and adjunctive therapy for focal seizures is prescribed gabapentin. He asks how this medication works, noting that despite its chemical name resembling GABA, his doctor mentioned it does not bind directly to GABA receptors. Which of the following is the primary cellular mechanism of action of gabapentin and pregabalin?",
        "category": "CBIL Epilepsy",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Direct allosteric agonism of postsynaptic GABA-A chloride"},
            {"letter": "B", "is_correct": True, "text": "Binding to the alpha-2-delta subunit of calcium channels"},
            {"letter": "C", "is_correct": False, "text": "Inhibition of presynaptic GAT-1 GABA reuptake proteins"},
            {"letter": "D", "is_correct": False, "text": "Inactivation of fast-inactivating voltage-gated sodium"},
            {"letter": "E", "is_correct": False, "text": "Irreversible inhibition of mitochondrial GABA transaminase"}
        ],
        "correct_idx": 1,
        "explanation": "Gabapentin and pregabalin are structural analogues of GABA, but they do NOT bind to GABA-A or GABA-B receptors, nor do they alter GABA metabolism or uptake. Instead, they bind with high affinity to the auxiliary alpha-2-delta subunit of presynaptic voltage-gated calcium channels. This decreases presynaptic calcium influx in response to action potentials, reducing the release of excitatory neurotransmitters (such as glutamate, substance P, and norepinephrine). They are used for focal seizures and neuropathic pain.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Gabapentin and pregabalin bind the alpha-2-delta subunit of voltage-gated Ca2+ channels, decreasing excitatory neurotransmitter release; effective for focal seizures and neuropathic pain.",
        "image": None
    })

    # Q139
    qs.append({
        "id": "exam3_in_house_like_g_q139",
        "q_num": "139",
        "stem": "A 38-year-old man with refractory focal epilepsy is evaluated for adjunctive antiepileptic therapy. The neurologist selects tiagabine. Which of the following specific cellular mechanisms mediates the therapeutic anticonvulsant activity of tiagabine?",
        "category": "CBIL Epilepsy",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Irreversible inhibition of mitochondrial GABA transaminase"},
            {"letter": "B", "is_correct": True, "text": "Inhibition of GAT-1 presynaptic and glial GABA reuptake"},
            {"letter": "C", "is_correct": False, "text": "Allosteric modulation of the postsynaptic GABA-A chloride"},
            {"letter": "D", "is_correct": False, "text": "Selective blockade of low-voltage T-type calcium pores"},
            {"letter": "E", "is_correct": False, "text": "Enhancement of slow inactivation of voltage sodium pores"}
        ],
        "correct_idx": 1,
        "explanation": "Tiagabine is an antiepileptic drug that selectively inhibits GABA transporter 1 (GAT-1), the primary transporter responsible for reuptake of GABA from the synaptic cleft into presynaptic neurons and surrounding glial cells. By blocking reuptake, tiagabine prolongs the synaptic dwell time of GABA and potentiates inhibitory postsynaptic currents.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Tiagabine increases synaptic GABA by inhibiting the GAT-1 GABA reuptake transporter. Vigabatrin inhibits GABA transaminase (degradation).",
        "image": None
    })

    # Q140
    qs.append({
        "id": "exam3_in_house_like_g_q140",
        "q_num": "140",
        "stem": "A 25-year-old woman with a history of generalized epilepsy visits her neurologist for preconception counseling. She is currently taking valproic acid. The physician strongly recommends transitioning to an alternative antiepileptic agent before attempting to conceive because valproate carries the highest teratogenic risk among all antiseizure medications. Which of the following congenital malformations is most specifically linked to in utero valproate exposure?",
        "category": "CBIL Epilepsy",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Ebstein anomaly of tricuspid valve with atrialization"},
            {"letter": "B", "is_correct": True, "text": "Neural tube defects including lumbar myelomeningocele"},
            {"letter": "C", "is_correct": False, "text": "Bilateral renal agenesis with severe oligohydramnios"},
            {"letter": "D", "is_correct": False, "text": "Phocomelia of upper limbs with flipper-like hands"},
            {"letter": "E", "is_correct": False, "text": "Transposition of the great arteries cyanotic heart"}
        ],
        "correct_idx": 1,
        "explanation": "Valproic acid is Pregnancy Category D and is the most teratogenic antiepileptic medication. In utero exposure, especially during the first trimester when the neural tube closes (days 21-28 post-conception), is associated with a 1-2% risk of neural tube defects (spina bifida aperta, myelomeningocele; a 10- to 20-fold increase over the general population). It also causes facial clefts, congenital heart defects, and impaired cognitive development. Lamotrigine and levetiracetam have lower teratogenic risk and are preferred in women of childbearing potential, along with high-dose folic acid (4 mg/day).",
        "high_yield_pearl": "High-Yield Clinical Pearl: Valproic acid has the highest teratogenic risk among AEDs, causing neural tube defects (spina bifida); lamotrigine and levetiracetam are preferred lower-risk options in pregnancy.",
        "image": None
    })

    # Q141
    qs.append({
        "id": "exam3_in_house_like_g_q141",
        "q_num": "141",
        "stem": "A 22-year-old woman with focal epilepsy taking combination ethinyl estradiol-norgestimate oral contraceptive pills is started on an antiseizure medication. Three months later, she presents with unexpected breakthrough vaginal bleeding and a positive urine pregnancy test. Which of the following antiseizure medications was most likely prescribed, leading to accelerated hepatic metabolism and contraceptive failure?",
        "category": "CBIL Epilepsy",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Sodium valproate cytochrome P450 inhibitor medication"},
            {"letter": "B", "is_correct": True, "text": "Carbamazepine cytochrome P450 enzyme-inducing agent"},
            {"letter": "C", "is_correct": False, "text": "Levetiracetam non-hepatic renally excreted medication"},
            {"letter": "D", "is_correct": False, "text": "Gabapentin non-metabolized renally excreted compound"},
            {"letter": "E", "is_correct": False, "text": "Lacosamide minimally interacting amino acid derivative"}
        ],
        "correct_idx": 1,
        "explanation": "Enzyme-inducing antiseizure medications (carbamazepine, phenytoin, phenobarbital, primidone, and high-dose topiramate) induce hepatic cytochrome P450 enzymes (specifically CYP3A4). This accelerates the metabolic clearance of estrogen and progestin components of combined oral contraceptives, leading to decreased plasma steroid levels, breakthrough bleeding, and unintended pregnancy. Non-inducing AEDs (levetiracetam, valproate, gabapentin, lacosamide) do not reduce oral contraceptive efficacy.",
        "high_yield_pearl": "High-Yield Clinical Pearl: CYP450 inducers (carbamazepine, phenytoin, phenobarbital) accelerate oral contraceptive metabolism, causing contraceptive failure. Levetiracetam and valproate do not induce CYP450.",
        "image": None
    })

    # Q142
    qs.append({
        "id": "exam3_in_house_like_g_q142",
        "q_num": "142",
        "stem": "A 34-year-old man presents to the clinic after experiencing a generalized tonic-clonic seizure while at home. Six months ago, he experienced a similar unprovoked generalized seizure. Brain MRI with contrast is normal, and routine interictal EEG is unremarkable. Which of the following is the most appropriate management recommendation regarding antiepileptic drug therapy for this patient?",
        "category": "CBIL Epilepsy",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Withhold pharmacotherapy until a third seizure occurs"},
            {"letter": "B", "is_correct": True, "text": "Initiate long-term maintenance antiepileptic drug therapy"},
            {"letter": "C", "is_correct": False, "text": "Perform emergency bilateral anterior temporal lobectomy"},
            {"letter": "D", "is_correct": False, "text": "Prescribe rescue rectal diazepam monotherapy without daily AED"},
            {"letter": "E", "is_correct": False, "text": "Implant a vagus nerve stimulation pulse generator unit"}
        ],
        "correct_idx": 1,
        "explanation": "Following a single unprovoked seizure with normal neuroimaging and EEG, the 2-year recurrence risk is approximately 30-40%, so daily AED maintenance is often deferred. However, following a SECOND unprovoked seizure, the risk of recurrence rises steeply to 80-90%. By definition, two unprovoked seizures occurring >24 hours apart fulfills the diagnostic criteria for epilepsy, and initiation of long-term maintenance antiepileptic monotherapy is universally recommended.",
        "high_yield_pearl": "High-Yield Clinical Pearl: After a single unprovoked seizure, recurrence risk is 30-40%; after a SECOND unprovoked seizure, recurrence risk jumps to 80-90%, establishing the clear indication to start daily AED therapy.",
        "image": None
    })

    # Q143
    qs.append({
        "id": "exam3_in_house_like_g_q143",
        "q_num": "143",
        "stem": "A 24-year-old man collapses in a shopping mall and is brought to the emergency department. The emergency team must distinguish whether the transient loss of consciousness was an epileptic seizure or vasovagal syncope. Which of the following clinical features, if present, is most highly specific for an epileptic generalized tonic-clonic seizure rather than syncope?",
        "category": "CBIL Epilepsy",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Brief lightheadedness and diaphoresis prior to collapse"},
            {"letter": "B", "is_correct": True, "text": "Laceration of the lateral border of the tongue blade"},
            {"letter": "C", "is_correct": False, "text": "Immediate return to full alertness upon awakening recumbent"},
            {"letter": "D", "is_correct": False, "text": "Presence of a few brief multifocal myoclonic limb jerks"},
            {"letter": "E", "is_correct": False, "text": "Pale, cool, clammy skin observed during the episode"}
        ],
        "correct_idx": 1,
        "explanation": "Laceration of the lateral border of the tongue is highly specific (>99%) for a generalized tonic-clonic epileptic seizure. In contrast, tip-of-the-tongue biting can occasionally occur during syncope or falls. Other features favoring seizure over syncope include: distinct auras, prolonged tonic-clonic contractions (>30-60 sec), urinary incontinence, and prolonged postictal confusion/somnolence (15-30+ min). Syncope typically features a prodrome of diaphoresis/tunnel vision and immediate recovery upon lying flat.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Lateral tongue laceration is highly specific for epileptic generalized tonic-clonic seizure. Syncope typically features immediate recovery of orientation upon assuming recumbency.",
        "image": None
    })

    # Q144
    qs.append({
        "id": "exam3_in_house_like_g_q144",
        "q_num": "144",
        "stem": "A 2-year-old boy is brought to the emergency department by his frantic parents after experiencing a generalized tonic-clonic seizure that lasted 3 minutes. His temperature is 39.4 C (103.0 F). Rapid viral testing is positive for human herpesvirus 6 (roseola). On examination 30 minutes after arrival, he is playful, fully alert, and has a normal neurological examination with supple neck. He has had no prior seizures. Which of the following is the most appropriate management strategy for this child?",
        "category": "CBIL Epilepsy",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Initiation of daily oral levetiracetam maintenance therapy"},
            {"letter": "B", "is_correct": True, "text": "Parental reassurance and symptomatic antipyretic comfort"},
            {"letter": "C", "is_correct": False, "text": "Immediate lumbar puncture and empiric ceftriaxone therapy"},
            {"letter": "D", "is_correct": False, "text": "Daily oral phenobarbital maintenance therapy for one year"},
            {"letter": "E", "is_correct": False, "text": "Emergency head CT followed by continuous video-EEG study"}
        ],
        "correct_idx": 1,
        "explanation": "This child experienced a simple febrile seizure, defined as a generalized seizure lasting <15 minutes, occurring only once in a 24-hour period in a child aged 6 months to 5 years, with a fever and without evidence of intracranial infection or baseline neurological deficit. Simple febrile seizures carry an excellent prognosis with no increased risk of intellectual disability and only a minor (<2-3%) risk of future epilepsy. Daily maintenance AED therapy is NOT indicated; management consists of parental education and antipyretics for comfort.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Simple febrile seizures (<15 min, generalized, once in 24 hr, normal baseline) are benign; manage with parental reassurance and antipyretics; daily AEDs are contraindicated.",
        "image": None
    })

    # Q145
    qs.append({
        "id": "exam3_in_house_like_g_q145",
        "q_num": "145",
        "stem": "A 48-year-old man with severe chronic alcohol dependence is admitted to the hospital with acute pancreatitis. Thirty-six hours after his last drink, he experiences two witnessed generalized tonic-clonic seizures in rapid succession. Neurological examination between seizures shows tremulousness, diaphoresis, tachycardia (118/min), and coarse hand tremor. Which of the following neurochemical alterations explains the emergence of seizures during acute alcohol withdrawal?",
        "category": "CBIL Epilepsy",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Upregulation of GABA-A and downregulation of NMDA pores"},
            {"letter": "B", "is_correct": True, "text": "Downregulation of GABA-A and upregulation of NMDA pores"},
            {"letter": "C", "is_correct": False, "text": "Excessive central dopamine release in nucleus accumbens"},
            {"letter": "D", "is_correct": False, "text": "Depletion of brainstem acetylcholine from Meynert loss"},
            {"letter": "E", "is_correct": False, "text": "Complete blockade of voltage-gated sodium channel pores"}
        ],
        "correct_idx": 1,
        "explanation": "Chronic alcohol consumption enhances inhibitory GABA-A receptor function and inhibits excitatory NMDA glutamate receptors. To maintain homeostasis, the brain chronically downregulates GABA-A receptors and upregulates NMDA receptors. When alcohol is abruptly removed, the loss of exogenous GABAergic facilitation unmasks this baseline imbalance: reduced GABAergic inhibition combined with unopposed glutamate excitotoxicity via upregulated NMDA receptors leads to autonomic hyperactivity, tremors, and withdrawal seizures (typically 12-48 hours post-cessation). Treat with benzodiazepines.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Alcohol withdrawal seizures (12-48 hr post-cessation) result from chronic GABA-A downregulation and NMDA upregulation; treat with benzodiazepines (lorazepam, diazepam).",
        "image": None
    })

    # Q146
    qs.append({
        "id": "exam3_in_house_like_g_q146",
        "q_num": "146",
        "stem": "A 30-year-old woman with focal epilepsy has continued to experience disabling focal impaired awareness seizures despite compliant trials of maximal tolerated doses of lamotrigine monotherapy, levetiracetam monotherapy, and combination carbamazepine plus lacosamide. She meets the formal ILAE definition for drug-resistant (refractory) epilepsy. Which of the following is the most appropriate next step in the clinical management of this patient?",
        "category": "CBIL Epilepsy",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Trial of lifelong high-dose phenobarbital monotherapy"},
            {"letter": "B", "is_correct": True, "text": "Referral to an epilepsy center for presurgical evaluation"},
            {"letter": "C", "is_correct": False, "text": "Discontinuation of all medications as trials have failed"},
            {"letter": "D", "is_correct": False, "text": "Institution of a strict low-carbohydrate Atkins diet alone"},
            {"letter": "E", "is_correct": False, "text": "Reassurance that medical management will eventually work"}
        ],
        "correct_idx": 1,
        "explanation": "Drug-resistant (refractory) epilepsy is defined as failure of adequate trials of TWO tolerated and appropriately chosen and used antiepileptic drug schedules (as monotherapies or in combination) to achieve sustained seizure freedom. When a patient fails two AEDs, the probability of achieving seizure freedom with a third medication drops to <5%. The standard next step is referral to a comprehensive epilepsy center for video-EEG monitoring and evaluation for surgical resection (such as anterior temporal lobectomy).",
        "high_yield_pearl": "High-Yield Clinical Pearl: Refractory epilepsy is failure of 2 appropriate AED trials; likelihood of medical cure is <5%; refer to a comprehensive epilepsy center for surgical evaluation.",
        "image": None
    })

    # Q147
    qs.append({
        "id": "exam3_in_house_like_g_q147",
        "q_num": "147",
        "stem": "A 27-year-old woman with epilepsy and obesity (BMI 34 kg/m2) is concerned about medication-induced weight changes when selecting an antiepileptic drug. Which of the following antiepileptic agents is NOT associated with weight gain, and instead characteristically causes significant anorexia and weight loss?",
        "category": "CBIL Epilepsy",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Sodium valproate broad-spectrum antiepileptic drug"},
            {"letter": "B", "is_correct": True, "text": "Topiramate broad-spectrum antiepileptic medication"},
            {"letter": "C", "is_correct": False, "text": "Carbamazepine narrow-spectrum sodium channel drug"},
            {"letter": "D", "is_correct": False, "text": "Gabapentin calcium alpha-2-delta subunit ligand"},
            {"letter": "E", "is_correct": False, "text": "Pregabalin calcium channel alpha-2-delta ligand"}
        ],
        "correct_idx": 1,
        "explanation": "Weight changes are common adverse effects of antiepileptic medications. Agents commonly associated with substantial weight gain include valproate, carbamazepine, gabapentin, and pregabalin. In contrast, topiramate and zonisamide characteristically produce appetite suppression (anorexia) and significant weight loss. Levetiracetam, lamotrigine, and lacosamide are generally weight-neutral.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Topiramate and zonisamide cause anorexia and weight loss; valproate, carbamazepine, and gabapentin/pregabalin cause weight gain; lamotrigine/levetiracetam are weight neutral.",
        "image": None
    })

    # Q148
    qs.append({
        "id": "exam3_in_house_like_g_q148",
        "q_num": "148",
        "stem": "A 24-year-old college student is diagnosed with new-onset epilepsy following two unprovoked seizures and is started on levetiracetam. During the initial clinical counseling session, the physician discusses essential lifestyle modifications, legal restrictions, and safety precautions. Which of the following interventions is NOT appropriate to discuss during this initial counseling conversation?",
        "category": "CBIL Epilepsy",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Statutory motor vehicle driving restrictions and suspension"},
            {"letter": "B", "is_correct": True, "text": "Immediate evaluation for curative epilepsy neurosurgery"},
            {"letter": "C", "is_correct": False, "text": "Workplace and water safety, including avoiding alone bathing"},
            {"letter": "D", "is_correct": False, "text": "Avoidance of recreational sleep deprivation and heavy alcohol"},
            {"letter": "E", "is_correct": False, "text": "Calcium and vitamin D bone health supplementation guidance"}
        ],
        "correct_idx": 1,
        "explanation": "Initial counseling for newly diagnosed epilepsy must address immediate practical safety concerns: driving restrictions (statutory driving suspension, typically 3-12 months seizure-free), water safety (showering instead of bathing alone, avoiding unsupervised swimming), workplace safety (avoiding heights/heavy machinery), sleep hygiene and alcohol avoidance (common triggers), and bone health. In contrast, epilepsy surgery is reserved for medically refractory epilepsy (failure of >=2 AEDs) and is NOT part of the initial conversation for a newly diagnosed patient.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Initial epilepsy counseling covers driving restrictions, water/workplace safety, and seizure triggers. Epilepsy surgery is reserved for patients who fail >=2 AED trials.",
        "image": None
    })

    # Q149
    qs.append({
        "id": "exam3_in_house_like_g_q149",
        "q_num": "149",
        "stem": "A 44-year-old man with refractory focal impaired awareness seizures is prescribed lacosamide as adjunctive therapy. Unlike traditional sodium channel blockers (such as phenytoin and carbamazepine) that modulate fast inactivation, lacosamide exerts its primary therapeutic effect through which of the following novel electrophysiological mechanisms?",
        "category": "CBIL Epilepsy",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Irreversible inhibition of mitochondrial GABA transaminase"},
            {"letter": "B", "is_correct": True, "text": "Selective enhancement of slow inactivation of sodium pores"},
            {"letter": "C", "is_correct": False, "text": "Direct opening of postsynaptic ligand-gated chloride pores"},
            {"letter": "D", "is_correct": False, "text": "Selective blockade of low-voltage T-type calcium channels"},
            {"letter": "E", "is_correct": False, "text": "Irreversible blockade of presynaptic SV2A vesicle proteins"}
        ],
        "correct_idx": 1,
        "explanation": "Lacosamide is a functionalized amino acid that has a unique mechanism of action: it selectively enhances the SLOW inactivation of voltage-gated sodium channels without altering physiological fast inactivation. This action selectively terminates sustained, repetitive neuronal burst firing characteristic of epileptic foci while sparing normal physiological action potential propagation. It has minimal drug interactions and is available in oral and IV formulations.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Lacosamide selectively enhances the SLOW inactivation of voltage-gated sodium channels, unlike phenytoin/carbamazepine which modulate fast inactivation.",
        "image": None
    })

    # Q150
    qs.append({
        "id": "exam3_in_house_like_g_q150",
        "q_num": "150",
        "stem": "A 72-year-old man presents with a new-onset focal motor seizure involving rhythmic clonic jerking of his right hand that spread to his right arm over 2 minutes, followed by 10 minutes of postictal confusion. He has no prior personal or family history of seizures. Routine laboratory testing and toxicology screens are unremarkable. In this elderly age demographic, which of the following is the single most common underlying etiology for new-onset seizures?",
        "category": "CBIL Epilepsy",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Congenital cortical brain malformations and heterotopias"},
            {"letter": "B", "is_correct": True, "text": "Cerebrovascular disease including past ischemic stroke"},
            {"letter": "C", "is_correct": False, "text": "Idiopathic genetic channelopathy epilepsy syndromes"},
            {"letter": "D", "is_correct": False, "text": "Perinatal intraventricular hemorrhage hypoxic injury"},
            {"letter": "E", "is_correct": False, "text": "Inborn errors of metabolism affecting amino acid cycles"}
        ],
        "correct_idx": 1,
        "explanation": "Etiologies of new-onset seizures vary dramatically across the lifespan: in neonates/infants, common causes are perinatal hypoxia, congenital malformations, and metabolic disorders; in children, febrile seizures, genetic epilepsies, and infections predominate; in young adults (15-35 years), head trauma, recreational drug/alcohol use, and brain tumors are frequent; in elderly adults (>65 years), cerebrovascular disease (ischemic and hemorrhagic strokes, remote stroke encephalomalacia) is by far the #1 cause, accounting for 30-50% of all new-onset seizures.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Cerebrovascular disease (stroke) is the #1 single cause of new-onset seizures in adults over 65 years. In young adults, trauma and tumors predominate; in children, genetic and febrile causes.",
        "image": None
    })

    return qs

if __name__ == '__main__':
    qs = get_part3_questions()
    print(f"Generated {len(qs)} questions for Part 3 (Q94 - Q150).")
