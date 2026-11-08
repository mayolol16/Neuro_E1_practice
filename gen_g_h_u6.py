import json
from test_gen_structure import check_q

u6_questions = [
    {
        "id": "exam3_g_h_u6_q1",
        "category": "Unit 06: Blood Supply",
        "subcategory": "Cerebral Artery Syndromes",
        "question_type": "clinical_vignette",
        "stem": "A 69-year-old woman presents with sudden-onset left-sided weakness. Physical examination reveals dense flaccid paralysis (0/5) and complete loss of pinprick and vibration sensation in her left lower extremity, but only mild clumsiness (4+/5) with normal sensation in her left face and upper extremity. She exhibits marked abulia and urinary incontinence. Occlusion of which cerebral artery accounts for this somatotopic pattern of motor and sensory loss?",
        "options": [
            {"label": "A", "text": "Right anterior cerebral artery supplying the medial paracentral lobule", "is_correct": True},
            {"label": "B", "text": "Right middle cerebral artery supplying the lateral motor precentral cortex", "is_correct": False},
            {"label": "C", "text": "Right posterior cerebral artery supplying the primary calcarine fissure", "is_correct": False},
            {"label": "D", "text": "Right anterior choroidal artery supplying the posterior limb of capsule", "is_correct": False},
            {"label": "E", "text": "Right recurrent artery of Heubner supplying the anterior limb of capsule", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "The anterior cerebral artery (ACA) supplies the medial surface of the frontal and parietal lobes, including the medial aspect of the primary motor and somatosensory cortices (the paracentral lobule). Because the motor and sensory homunculi represent the lower extremity and perineum along this medial surface, ACA infarction selectively causes contralateral lower extremity paralysis, sensory loss, and frontal urinary incontinence, sparing the face and arm (represented laterally along MCA territory).",
        "high_yield_takeaway": "Anterior cerebral artery (ACA) stroke causes contralateral lower extremity motor and sensory loss, urinary incontinence, and abulia, sparing the face and arm."
    },
    {
        "id": "exam3_g_h_u6_q2",
        "category": "Unit 06: Blood Supply",
        "subcategory": "Cerebral Artery Syndromes",
        "question_type": "clinical_vignette",
        "stem": "A 71-year-old right-handed man presents with acute difficulty communicating. His speech is non-fluent, slow, telegraphic, and effortful, but his auditory comprehension is intact and he follows complex multi-step commands. On physical examination, he has a dense right lower facial droop and right upper extremity hemiparesis (2/5 strength) with preserved lower extremity strength (5/5). What specific arterial branch has been occluded?",
        "options": [
            {"label": "A", "text": "Superior division of the left middle cerebral artery", "is_correct": True},
            {"label": "B", "text": "Inferior division of the left middle cerebral artery", "is_correct": False},
            {"label": "C", "text": "Main trunk of the left anterior cerebral artery", "is_correct": False},
            {"label": "D", "text": "Cortical branches of the left posterior cerebral artery", "is_correct": False},
            {"label": "E", "text": "Perforating branches of the left anterior choroidal artery", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "The middle cerebral artery (MCA) bifurcates into superior and inferior divisions. The superior division supplies the frontal lobe convexity, including Broca area (pars opercularis/triangularis in the inferior frontal gyrus) and the motor cortex for the face and arm. Occlusion of the dominant superior MCA division produces expressive (Broca) non-fluent aphasia combined with contralateral face and arm weakness, while comprehension is preserved.",
        "high_yield_takeaway": "Superior division MCA stroke causes Broca (expressive/non-fluent) aphasia with contralateral face and arm weakness, sparing comprehension."
    },
    {
        "id": "exam3_g_h_u6_q3",
        "category": "Unit 06: Blood Supply",
        "subcategory": "Cerebral Artery Syndromes",
        "question_type": "clinical_vignette",
        "stem": "A 67-year-old woman is evaluated for acute spatial disorientation. She fails to acknowledge people standing on her left side, draws a clock face with all twelve numbers crowded into the right hemispace, and vehemently disowns her paralyzed left arm (anosognosia). Visual field examination reveals a left homonymous superior quadrantanopia ('pie in the sky'). What arterial division and neural pathway have been infarcted?",
        "options": [
            {"label": "A", "text": "Inferior division of the right MCA damaging Meyer loop in the temporal lobe", "is_correct": True},
            {"label": "B", "text": "Superior division of the right MCA damaging the frontoparietal operculum", "is_correct": False},
            {"label": "C", "text": "Anterior cerebral artery damaging the dorsal supplementary motor cortex", "is_correct": False},
            {"label": "D", "text": "Posterior cerebral artery damaging the dorsal optic radiations in parietal lobe", "is_correct": False},
            {"label": "E", "text": "Anterior choroidal artery damaging the optic chiasm at the skull base", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "The non-dominant (typically right) MCA inferior division supplies the posterior temporal and inferior parietal lobes. Damage to the non-dominant parietal cortex produces severe contralateral spatial hemineglect and anosognosia. Concomitant injury to Meyer loop (the ventral optic radiation arching through the temporal lobe around the lateral ventricle) produces a contralateral homonymous superior quadrantanopia ('pie in the sky').",
        "high_yield_takeaway": "Right inferior MCA division stroke produces left hemispatial neglect, anosognosia, and left superior quadrantanopia (Meyer loop damage)."
    },
    {
        "id": "exam3_g_h_u6_q4",
        "category": "Unit 06: Blood Supply",
        "subcategory": "Lacunar Stroke Syndromes",
        "question_type": "clinical_vignette",
        "stem": "A 62-year-old man with a twenty-year history of poorly controlled hypertension develops sudden right-sided weakness. Neurological examination reveals complete, symmetrical motor hemiparesis equally affecting his right face, arm, and leg (3/5 strength throughout) with brisk reflexes and a right extensor plantar sign. Sensation to all modalities, visual fields, and language are completely intact. What microvascular pathology in which deep brain structure is responsible for this classic pure motor stroke?",
        "options": [
            {"label": "A", "text": "Lipohyalinosis of lenticulostriate arteries in the posterior limb of capsule", "is_correct": True},
            {"label": "B", "text": "Atheroembolism of anterior choroidal artery to the lateral geniculate nucleus", "is_correct": False},
            {"label": "C", "text": "Charcot-Bouchard microaneurysm rupture within the medial thalamic nucleus", "is_correct": False},
            {"label": "D", "text": "Fibrinoid necrosis of basilar circumferential branches in the dorsal pons", "is_correct": False},
            {"label": "E", "text": "Thromboembolism of the Heubner artery into the anterior internal capsule", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "Pure motor hemiparesis is the most common lacunar stroke syndrome (>50%), resulting from ischemic infarction of the posterior limb of the internal capsule (carrying descending corticospinal and corticobulbar fibers). The underlying microvascular pathology is lipohyalinosis and microatheroma of the deep penetrating lenticulostriate branches of the middle cerebral artery, driven by chronic systemic hypertension.",
        "high_yield_takeaway": "Pure motor lacunar stroke is caused by lipohyalinosis of lenticulostriate arteries, selectively damaging the posterior limb of the internal capsule."
    },
    {
        "id": "exam3_g_h_u6_q5",
        "category": "Unit 06: Blood Supply",
        "subcategory": "Anterior Choroidal Artery",
        "question_type": "clinical_vignette",
        "stem": "A 58-year-old man presents with sudden left-sided weakness, dense left hemisensory loss to pinprick and proprioception, and a complete left homonymous hemianopia with macular involvement. Pupillary light reflexes are normal. Diffusion MRI demonstrates an ischemic stroke involving the posterior limb of the internal capsule, optic tract, and lateral geniculate nucleus. What specific vessel, arising directly from the internal carotid artery, has undergone occlusion?",
        "options": [
            {"label": "A", "text": "Right anterior choroidal artery supplying the retrolenticular capsule", "is_correct": True},
            {"label": "B", "text": "Right posterior communicating artery supplying the hypothalamic sulcus", "is_correct": False},
            {"label": "C", "text": "Right medial striate artery of Heubner supplying the caudate nucleus", "is_correct": False},
            {"label": "D", "text": "Right thalamoperforating artery supplying the anterior ventral thalamus", "is_correct": False},
            {"label": "E", "text": "Right ophthalmic artery supplying the intraorbital central retinal artery", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "The anterior choroidal artery arises directly from the internal carotid artery. It supplies the posterior limb and retrolenticular part of the internal capsule, the lateral geniculate nucleus (LGN), and the optic tract. Occlusion produces the classic anterior choroidal artery stroke triad: contralateral hemiparesis (corticospinal fibers), contralateral hemisensory loss (thalamocortical projections), and contralateral homonymous hemianopia (LGN/optic tract).",
        "high_yield_takeaway": "Anterior choroidal artery stroke produces a classic triad: contralateral hemiparesis, hemisensory loss, and homonymous hemianopia (capsule + LGN/optic tract)."
    },
    {
        "id": "exam3_g_h_u6_q6",
        "category": "Unit 06: Blood Supply",
        "subcategory": "PCA Syndromes",
        "question_type": "clinical_vignette",
        "stem": "A 65-year-old man with atrial fibrillation presents with sudden visual loss on his left side. Visual field testing confirms a complete left homonymous hemianopia; however, formal perimetry demonstrates that central visual acuity across the central five degrees of the visual field remains completely intact at 20/20 (macular sparing). What physiological vascular collateral accounts for the preservation of central vision following this posterior cerebral artery infarct?",
        "options": [
            {"label": "A", "text": "Dual blood supply to the occipital pole provided by terminal middle cerebral branches", "is_correct": True},
            {"label": "B", "text": "Retrograde flow through anterior communicating artery to the calcarine cortex", "is_correct": False},
            {"label": "C", "text": "Anastomotic supply from the superior cerebellar artery across tentorium cerebelli", "is_correct": False},
            {"label": "D", "text": "Persistent embryologic trigeminal artery supplying the striate visual center", "is_correct": False},
            {"label": "E", "text": "Reciprocal collateral branches from the anterior choroidal capillary plexus", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "The primary visual cortex along the calcarine sulcus is supplied by the calcarine branch of the posterior cerebral artery (PCA). However, the representation of the macula at the occipital pole has dual vascular collateral supply from terminal branches of the middle cerebral artery (MCA). Thus, embolic occlusion of the PCA produces homonymous hemianopia with macular sparing because MCA collateral flow preserves the occipital pole.",
        "high_yield_takeaway": "PCA calcarine stroke produces homonymous hemianopia with macular sparing due to collateral perfusion of the occipital pole by the middle cerebral artery."
    },
    {
        "id": "exam3_g_h_u6_q7",
        "category": "Unit 06: Blood Supply",
        "subcategory": "Disconnection Syndromes",
        "question_type": "clinical_vignette",
        "stem": "A 64-year-old man is evaluated following an ischemic stroke. When given a printed book, he cannot read a single sentence or letter. However, when given a pen and paper, he writes a coherent, grammatically flawless paragraph describing his family; immediately thereafter, he is totally unable to read what he has just written. Which two neuroanatomical structures were infarcted to produce this classic disconnection syndrome (alexia without agraphia)?",
        "options": [
            {"label": "A", "text": "Left primary visual cortex and the splenium of the corpus callosum", "is_correct": True},
            {"label": "B", "text": "Left angular gyrus and the arcuate fasciculus white matter tract", "is_correct": False},
            {"label": "C", "text": "Left inferior temporal gyrus and the uncinate fasciculus fibers", "is_correct": False},
            {"label": "D", "text": "Right visual cortex and the genu of the anterior corpus callosum", "is_correct": False},
            {"label": "E", "text": "Bilateral superior temporal gyri and the transverse auditory radiation", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "Alexia without agraphia (pure word blindness) is a classic disconnection syndrome caused by a left posterior cerebral artery (PCA) infarction involving both the left primary visual cortex and the splenium of the corpus callosum. The left visual field is processed by the intact right visual cortex, but visual information cannot cross to the left hemisphere language areas (angular gyrus) because the splenium is destroyed. Writing remains intact because the left angular gyrus and motor cortex are spared.",
        "high_yield_takeaway": "Alexia without agraphia results from left PCA infarction damaging the left visual cortex and the splenium of the corpus callosum."
    },
    {
        "id": "exam3_g_h_u6_q8",
        "category": "Unit 06: Blood Supply",
        "subcategory": "Thalamic Stroke Syndromes",
        "question_type": "clinical_vignette",
        "stem": "A 60-year-old man who suffered an ischemic lacunar stroke in his left posterolateral thalamus initially presented with contralateral hemianesthesia. Three months later, he presents with excruciating, burning, intractable pain over his right arm, trunk, and leg. Physical examination reveals that even the light touch of a cotton swab or a cool breeze elicits unbearable pain (allodynia and hyperpathia). What vascular perforator branches supplied the thalamic nucleus that underwent infarction?",
        "options": [
            {"label": "A", "text": "Thalamogeniculate perforating branches of the posterior cerebral artery", "is_correct": True},
            {"label": "B", "text": "Lenticulostriate branches of the proximal middle cerebral artery", "is_correct": False},
            {"label": "C", "text": "Anterior communicating artery perforators supplying the optic chiasm", "is_correct": False},
            {"label": "D", "text": "Paramedian basilar perforators supplying the dorsal pontine tegmentum", "is_correct": False},
            {"label": "E", "text": "Anterior spinal artery branches supplying the medial medullary pyramid", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "Dejerine-Roussy syndrome (thalamic pain syndrome) occurs weeks to months after an ischemic stroke involving the ventral posterolateral (VPL) and ventral posteromedial (VPM) nuclei of the thalamus, which are supplied by the thalamogeniculate perforating branches of the posterior cerebral artery (PCA). After initial contralateral sensory loss, central sensitization and loss of thalamic gating cause severe, paroxysmal, burning neuropathic pain and allodynia.",
        "high_yield_takeaway": "Dejerine-Roussy syndrome (central post-stroke pain) occurs after thalamogeniculate PCA stroke damaging the VPL/VPM sensory thalamic nuclei."
    },
    {
        "id": "exam3_g_h_u6_q9",
        "category": "Unit 06: Blood Supply",
        "subcategory": "Watershed Infarctions",
        "question_type": "clinical_vignette",
        "stem": "A 73-year-old man undergoes emergency repair of a ruptured abdominal aortic aneurysm complicated by massive hemorrhage and profound intraoperative hypotension (mean arterial pressure below 45 mmHg for fifty minutes). Upon emergence from anesthesia, he has severe bilateral proximal shoulder and hip weakness (1/5 strength) with preserved distal hand grip (5/5) and foot dorsiflexion (5/5), resembling a 'man-in-a-barrel.' What hemodynamic and neurovascular mechanism produced this presentation?",
        "options": [
            {"label": "A", "text": "Bilateral cortical watershed ischemia between the anterior and middle cerebral arteries", "is_correct": True},
            {"label": "B", "text": "Embolic occlusion of the basilar artery summit causing top-of-the-basilar syndrome", "is_correct": False},
            {"label": "C", "text": "Thrombosis of the anterior spinal artery at the level of the conus medullaris", "is_correct": False},
            {"label": "D", "text": "Acute watershed infarction between the superior and inferior cerebellar territories", "is_correct": False},
            {"label": "E", "text": "Bilateral internal carotid artery dissections with total hemispheric infarctions", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "Watershed (border zone) infarcts occur at the most distal junctions between major arterial vascular territories during severe systemic hypoperfusion (e.g., cardiac arrest, hemorrhagic shock). The anterior cortical border zone lies between the ACA and MCA territories over the high convexity motor cortex, which somatotopically controls the proximal upper and lower extremities (trunk, shoulders, thighs). Bilateral ischemia here causes 'man-in-a-barrel' syndrome: severe proximal bibrachial weakness with preserved distal hand function.",
        "high_yield_takeaway": "'Man-in-a-barrel' syndrome is caused by bilateral watershed infarction between ACA and MCA territories during profound systemic hypotension."
    },
    {
        "id": "exam3_g_h_u6_q10",
        "category": "Unit 06: Blood Supply",
        "subcategory": "Brainstem Stroke Syndromes",
        "question_type": "clinical_vignette",
        "stem": "A 57-year-old man presents with acute vertigo, intractable nausea, severe dysphagia, and hoarseness. Neurological examination reveals left Horner syndrome (ptosis, miosis, anhidrosis), loss of pain and temperature on the left face and right body, left cerebellar limb ataxia, and an absent left gag reflex with the uvula deviating to the right. Motor strength is 5/5 bilaterally, and dorsal column sensation is intact. What artery has occluded, and damage to which cranial nerve nucleus produces his dysphagia and hoarseness?",
        "options": [
            {"label": "A", "text": "Posterior inferior cerebellar artery; nucleus ambiguus (cranial nerves IX and X)", "is_correct": True},
            {"label": "B", "text": "Anterior inferior cerebellar artery; facial motor nucleus (cranial nerve VII)", "is_correct": False},
            {"label": "C", "text": "Anterior spinal artery; hypoglossal motor nucleus (cranial nerve XII)", "is_correct": False},
            {"label": "D", "text": "Superior cerebellar artery; motor nucleus of the trigeminal nerve (cranial nerve V)", "is_correct": False},
            {"label": "E", "text": "Paramedian basilar branches; abducens motor nucleus (cranial nerve VI)", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "This is lateral medullary (Wallenberg) syndrome, caused by occlusion of the posterior inferior cerebellar artery (PICA) or vertebral artery. Key features include: nucleus ambiguus damage (CN IX and X) causing dysphagia, hoarseness, and loss of gag reflex; spinal trigeminal nucleus (ipsilateral facial pain/temp); spinothalamic tract (contralateral body pain/temp); inferior cerebellar peduncle (ipsilateral ataxia); and descending sympathetic tract (ipsilateral Horner syndrome). Motor strength is completely spared because corticospinal tracts lie ventrally in the medial medulla.",
        "high_yield_takeaway": "Wallenberg syndrome (PICA occlusion) impairs the nucleus ambiguus, causing dysphagia, hoarseness, and absent gag reflex, with 'crossed' thermoanalgesia and Horner syndrome."
    },
    {
        "id": "exam3_g_h_u6_q11",
        "category": "Unit 06: Blood Supply",
        "subcategory": "Brainstem Stroke Syndromes",
        "question_type": "clinical_vignette",
        "stem": "A 63-year-old man presents with acute right-sided hemiparesis sparing his face. Examination shows 0/5 strength in the right arm and leg with a right Babinski sign, loss of vibration and joint position sense on the right side of his body, and flaccid atrophy of the left side of his tongue, which deviates to the left upon protrusion. Pain and temperature sensation are preserved bilaterally. Which vessel is occluded in this classic medial medullary syndrome?",
        "options": [
            {"label": "A", "text": "Paramedian branches of the anterior spinal artery in the anterior medulla", "is_correct": True},
            {"label": "B", "text": "Circumferential branches of the posterior inferior cerebellar artery", "is_correct": False},
            {"label": "C", "text": "Labyrinthine internal auditory branch of the anterior inferior cerebellar artery", "is_correct": False},
            {"label": "D", "text": "Paramedian perforating branches of the rostral basilar artery trunk", "is_correct": False},
            {"label": "E", "text": "Posterior communicating artery supplying the ventral diencephalon", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "Medial medullary (Dejerine) syndrome is caused by occlusion of the anterior spinal artery (ASA) or vertebral artery paramedian branches. The ischemic territory involves: 1) the medullary pyramid (contralateral hemiparesis of limbs, sparing face), 2) the medial lemniscus (contralateral loss of vibration and proprioception), and 3) the exiting hypoglossal nerve (CN XII) fibers/nucleus, causing ipsilateral tongue weakness with deviation toward the side of the lesion ('lick the lesion').",
        "high_yield_takeaway": "Medial medullary syndrome (anterior spinal artery stroke) presents with contralateral hemiparesis, contralateral proprioception loss, and ipsilateral tongue deviation."
    },
    {
        "id": "exam3_g_h_u6_q12",
        "category": "Unit 06: Blood Supply",
        "subcategory": "Brainstem Stroke Syndromes",
        "question_type": "clinical_vignette",
        "stem": "A 66-year-old man presents with sudden double vision and right-sided hemiplegia. On examination, his left eye is resting in a 'down-and-out' position with complete ptosis and a dilated, unreactive pupil (complete left third nerve palsy). His right arm and leg demonstrate flaccid paralysis (0/5 strength) with hyperreflexia and an extensor plantar response. Which arterial branch and midbrain structures were damaged to produce this Weber syndrome?",
        "options": [
            {"label": "A", "text": "Paramedian PCA branches injuring the crus cerebri and fascicles of CN III", "is_correct": True},
            {"label": "B", "text": "Quadrigeminal artery branches injuring the inferior colliculus and CN IV", "is_correct": False},
            {"label": "C", "text": "Short circumferential basilar branches injuring the medial lemniscus and CN VI", "is_correct": False},
            {"label": "D", "text": "Anterior choroidal artery branches injuring the optic tract and CN II", "is_correct": False},
            {"label": "E", "text": "Superior cerebellar artery branches injuring the red nucleus and CN V", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "Weber syndrome (superior alternating hemiplegia) is a ventral midbrain syndrome caused by occlusion of paramedian branches of the posterior cerebral artery (PCA) or basilar bifurcation. The infarct damages the cerebral peduncle / crus cerebri (corticospinal and corticobulbar tracts, causing contralateral hemiplegia and contralateral lower facial droop) and exiting fascicles of the oculomotor nerve (CN III, causing ipsilateral 'down-and-out' pupil-dilated third nerve palsy).",
        "high_yield_takeaway": "Weber syndrome is caused by a ventral midbrain PCA stroke, presenting with ipsilateral CN III palsy and contralateral hemiplegia."
    },
    {
        "id": "exam3_g_h_u6_q13",
        "category": "Unit 06: Blood Supply",
        "subcategory": "Brainstem Stroke Syndromes",
        "question_type": "clinical_vignette",
        "stem": "A 54-year-old woman presents with acute vertigo, vomiting, right-sided peripheral facial paralysis involving her forehead and lower face, right sensorineural hearing loss, right Horner syndrome, right appendicular limb ataxia, and loss of pain and temperature on her right face and left body. What distinct clinical findings conclusively differentiate this lateral pontine syndrome from a lateral medullary syndrome?",
        "options": [
            {"label": "A", "text": "Ipsilateral peripheral facial palsy and sensorineural hearing loss", "is_correct": True},
            {"label": "B", "text": "Severe dysphagia, dysarthria, and deviation of the uvula away from the lesion", "is_correct": False},
            {"label": "C", "text": "Contralateral loss of vibration and joint position sense in the limbs", "is_correct": False},
            {"label": "D", "text": "Ipsilateral deviation of the tongue with muscular atrophy and fasciculations", "is_correct": False},
            {"label": "E", "text": "Contralateral flaccid hemiparesis sparing the upper and lower face", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "Lateral pontine syndrome is caused by occlusion of the anterior inferior cerebellar artery (AICA), whereas lateral medullary syndrome is caused by PICA. Both share Horner syndrome, cerebellar ataxia, and crossed pain/temperature loss. The crucial distinguishing features of AICA (pons) are damage to the facial nucleus (CN VII: ipsilateral full-face paralysis) and cochlear nuclei/internal auditory artery (CN VIII: ipsilateral sensorineural deafness). In contrast, PICA (medulla) damages nucleus ambiguus (CN IX/X: hoarseness, dysphagia).",
        "high_yield_takeaway": "AICA (lateral pontine) stroke features ipsilateral facial paralysis and hearing loss; PICA (lateral medullary) stroke features hoarseness, dysphagia, and no facial paralysis."
    },
    {
        "id": "exam3_g_h_u6_q14",
        "category": "Unit 06: Blood Supply",
        "subcategory": "Basilar Artery Syndromes",
        "question_type": "clinical_vignette",
        "stem": "A 49-year-old man who experiences acute basilar artery thrombosis develops total quadriplegia, aphonia, and bilateral horizontal gaze paralysis. However, he is fully conscious, perfectly alert, and able to reliably communicate complex thoughts by blinking his upper eyelids and making voluntary vertical saccades. Why are consciousness and vertical ocular movements preserved despite extensive infarction of the ventral basis pontis ('locked-in' syndrome)?",
        "options": [
            {"label": "A", "text": "Midbrain reticular activating system and rostral CN III/IV centers are spared", "is_correct": True},
            {"label": "B", "text": "Horizontal saccade centers in the caudal pontine reticular formation are spared", "is_correct": False},
            {"label": "C", "text": "Descending corticospinal tracts receive retrograde supply from anterior spinal artery", "is_correct": False},
            {"label": "D", "text": "Medullary olive maintains tonic compensatory activation of cranial motor nuclei", "is_correct": False},
            {"label": "E", "text": "Basal ganglia striosomes autonomously control cognitive processing and alertness", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "Locked-in syndrome results from bilateral ventral pontine infarction (basis pontis), transecting descending corticospinal and corticobulbar fibers, and destroying bilateral abducens nuclei/PPRF (loss of horizontal gaze). Patients cannot move limbs, speak, or look horizontally. However, consciousness (ascending reticular activating system in the dorsal midbrain) and vertical eye movements/eyelid opening (CN III/IV and rostral interstitial nucleus of MLF in the midbrain) are preserved because the midbrain receives rostral collateral perfusion from the posterior cerebral arteries.",
        "high_yield_takeaway": "Locked-in syndrome spares consciousness (midbrain reticular activating system) and vertical eye movements (midbrain CN III/riMLF) despite bilateral pontine base destruction."
    },
    {
        "id": "exam3_g_h_u6_q15",
        "category": "Unit 06: Blood Supply",
        "subcategory": "Dural Venous Sinuses",
        "question_type": "clinical_vignette",
        "stem": "A 25-year-old man who squeezed an infected furuncle in his nasolabial fold develops high fever, periorbital edema, proptosis, and an inability to abduct his right eye beyond the midline. High-resolution contrast MRI confirms septic cavernous sinus thrombosis. Why is the abducens nerve (cranial nerve VI) typically the first and most severely damaged cranial nerve in cavernous sinus thrombosis?",
        "options": [
            {"label": "A", "text": "It traverses freely through the central venous lumen alongside the internal carotid artery", "is_correct": True},
            {"label": "B", "text": "It is protected within a fibrous sheath in the rigid lateral dural wall", "is_correct": False},
            {"label": "C", "text": "It receives precarious arterial microvascular supply from the ophthalmic artery", "is_correct": False},
            {"label": "D", "text": "It exits the skull base through the superior orbital fissure outside the annulus", "is_correct": False},
            {"label": "E", "text": "It carries primary parasympathetic fibers exquisitely sensitive to tissue hypoxia", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "The cavernous sinus is a unique venous structure. Cranial nerves III, IV, V1, and V2 are embedded within the protective fibrous dural tissue of the lateral wall. In contrast, the abducens nerve (CN VI) runs freely suspended inside the central cavernous sinus venous lumen, directly adjacent to the cavernous portion of the internal carotid artery. Consequently, CN VI is the earliest and most vulnerable structure injured during cavernous sinus inflammation or thrombosis.",
        "high_yield_takeaway": "The abducens nerve (CN VI) runs freely inside the central cavernous sinus lumen (not the lateral wall), making it most vulnerable to cavernous sinus thrombosis."
    },
    {
        "id": "exam3_g_h_u6_q16",
        "category": "Unit 06: Blood Supply",
        "subcategory": "Cerebral Venous Thrombosis",
        "question_type": "clinical_vignette",
        "stem": "A 28-year-old postpartum woman on oral contraceptives presents with worsening diffuse headache, bilateral papilledema, bilateral lower extremity weakness, and focal motor seizures. Contrast-enhanced CT venogram demonstrates non-filling of the posterior superior sagittal sinus surrounded by enhancing collateral dural channels ('empty delta sign'). What hemodynamic cascade causes parenchymal infarction and hemorrhage in cerebral venous sinus thrombosis?",
        "options": [
            {"label": "A", "text": "Elevated retrograde venous capillary pressure causing vasogenic edema and hemorrhage", "is_correct": True},
            {"label": "B", "text": "Primary arterial vasoconstriction mediated by excessive endothelin-1 secretion", "is_correct": False},
            {"label": "C", "text": "Direct rupture of high-pressure Charcot-Bouchard microaneurysms in basal ganglia", "is_correct": False},
            {"label": "D", "text": "Obstruction of the foramen of Monro causing acute bilateral non-communicating hydrocephalus", "is_correct": False},
            {"label": "E", "text": "Retrograde embolization of venous thrombi across a patent foramen ovale", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "Superior sagittal sinus thrombosis blocks the primary cerebral venous drainage pathway. Occlusion leads to severe retrograde venous and capillary hypertension, disruption of the blood-brain barrier (vasogenic edema), decreased cerebral perfusion pressure (cytotoxic edema), and eventually venous capillary rupture producing hemorrhagic venous infarction, typically in parasagittal convexities (bilateral leg weakness/seizures). Contrast CT shows the pathognomonic 'empty delta sign'.",
        "high_yield_takeaway": "Superior sagittal sinus thrombosis ('empty delta sign') causes severe venous hypertension, cerebral edema, and bilateral parasagittal hemorrhagic venous infarcts."
    },
    {
        "id": "exam3_g_h_u6_q17",
        "category": "Unit 06: Blood Supply",
        "subcategory": "Spinal Cord Vascular Anatomy",
        "question_type": "clinical_vignette",
        "stem": "A 68-year-old man undergoes surgical repair of an extensive descending thoracoabdominal aortic aneurysm. Post-operatively, he awakens with flaccid paraplegia (0/5 strength in both lower extremities), loss of pinprick and temperature sensation below the T10 dermatome, and acute urinary retention. However, his vibration and joint position sense remain completely intact bilaterally. Compromise of which radicular artery during aortic cross-clamping produced this anterior spinal artery syndrome?",
        "options": [
            {"label": "A", "text": "Great anterior radiculomedullary artery of Adamkiewicz originating from lower intercostals", "is_correct": True},
            {"label": "B", "text": "Posterior spinal arteries arising directly from the posterior inferior cerebellar arteries", "is_correct": False},
            {"label": "C", "text": "Vertebral artery ascending branches entering the transverse foramina of cervical vertebrae", "is_correct": False},
            {"label": "D", "text": "Internal iliac lateral sacral branches supplying the pelvic cauda equina nerve roots", "is_correct": False},
            {"label": "E", "text": "Ascending cervical radicular branches emerging from the thyrocervical trunk", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "The anterior spinal artery (ASA) supplies the anterior two-thirds of the spinal cord (anterior horns, corticospinal tracts, and spinothalamic tracts). In the lower thoracic and lumbar cord, the ASA relies heavily on the artery of Adamkiewicz (great anterior radiculomedullary artery), which typically arises from a left intercostal or lumbar artery between T9 and T12. Loss of this artery during thoracoabdominal aortic surgery causes anterior cord syndrome: paraplegia, loss of pain/temperature, and autonomic dysfunction, with complete sparing of the posterior dorsal columns.",
        "high_yield_takeaway": "Anterior spinal artery syndrome during aortic surgery results from ischemia to the artery of Adamkiewicz, causing bilateral paraplegia and thermoanalgesia with preserved dorsal columns."
    },
    {
        "id": "exam3_g_h_u6_q18",
        "category": "Unit 06: Blood Supply",
        "subcategory": "Carotid Artery Disease",
        "question_type": "clinical_vignette",
        "stem": "A 67-year-old woman with carotid atherosclerosis experiences sudden, painless loss of vision in her left eye, describing a 'dark shade or curtain descending from above' that leaves her completely blind for five minutes before spontaneously lifting. Immediate funduscopic examination reveals a bright, glistening, yellowish refractive crystal lodged at a bifurcation of a retinal arteriole (Hollenhorst plaque). Which arterial branch gave rise to the central retinal artery carrying this microembolus?",
        "options": [
            {"label": "A", "text": "Ophthalmic artery arising as the first intradural branch of internal carotid artery", "is_correct": True},
            {"label": "B", "text": "Superficial temporal artery arising from the bifurcation of external carotid artery", "is_correct": False},
            {"label": "C", "text": "Middle meningeal artery entering the skull base through the foramen spinosum", "is_correct": False},
            {"label": "D", "text": "Anterior cerebral artery arising from the internal carotid terminal bifurcation", "is_correct": False},
            {"label": "E", "text": "Internal maxillary artery passing through the pterygopalatine fossa", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "Amaurosis fugax (transient monocular vision loss) is a classic manifestation of internal carotid artery (ICA) stenosis. Microemboli (cholesterol plaques/Hollenhorst plaques or platelet-fibrin thrombi) dislodge from the carotid bifurcation and travel through the ICA into its first major intradural branch, the ophthalmic artery, and lodge in the central retinal artery or its branches, causing transient retinal ischemia.",
        "high_yield_takeaway": "Amaurosis fugax is transient monocular visual loss caused by microemboli (Hollenhorst plaques) traveling via the internal carotid artery to the ophthalmic and central retinal arteries."
    },
    {
        "id": "exam3_g_h_u6_q19",
        "category": "Unit 06: Blood Supply",
        "subcategory": "Brainstem Stroke Syndromes",
        "question_type": "clinical_vignette",
        "stem": "A 61-year-old man presents with acute double vision and weakness. Neurological examination reveals complete left-sided peripheral facial weakness involving the upper and lower face (cranial nerve VII), inability to abduct the left eye beyond the midline (cranial nerve VI), and dense contralateral right-sided hemiplegia (corticospinal tract). Sensation across all modalities is completely preserved. What alternating ventral brainstem stroke syndrome does this constellation represent?",
        "options": [
            {"label": "A", "text": "Millard-Gubler syndrome caused by an ischemic infarct in the ventrolateral pons", "is_correct": True},
            {"label": "B", "text": "Wallenberg syndrome caused by an ischemic infarct in the dorsolateral medulla", "is_correct": False},
            {"label": "C", "text": "Weber syndrome caused by an ischemic infarct in the ventral midbrain peduncle", "is_correct": False},
            {"label": "D", "text": "Benedikt syndrome caused by an ischemic infarct in the dorsal midbrain tegmentum", "is_correct": False},
            {"label": "E", "text": "Foville syndrome caused by an ischemic infarct in the dorsal rostral midbrain", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "Millard-Gubler syndrome (ventral pontine syndrome) is an alternating hemiplegia caused by occlusion of circumferential or paramedian branches of the basilar artery. The lesion affects the ventral caudal pons, damaging: 1) exiting fibers of CN VI (ipsilateral lateral rectus palsy), 2) exiting fibers of CN VII (ipsilateral peripheral facial palsy), and 3) the corticospinal tract (contralateral hemiplegia). Sensory tracts (spinothalamic, medial lemniscus) lie more dorsally and are spared.",
        "high_yield_takeaway": "Millard-Gubler syndrome (ventral pontine stroke) presents with ipsilateral CN VI and CN VII palsies and contralateral hemiplegia, sparing sensation."
    },
    {
        "id": "exam3_g_h_u6_q20",
        "category": "Unit 06: Blood Supply",
        "subcategory": "Vascular Malformations",
        "question_type": "clinical_vignette",
        "stem": "A 55-year-old woman presents with persistent pulsatile tinnitus described as a 'heartbeat in the ear', severe retro-orbital headache, and progressive redness and proptosis of her left eye. A loud vascular bruit is auscultated over her left mastoid and temporal bones. Catheter cerebral angiography confirms a direct pathological arteriovenous shunt between branches of the external carotid artery and the transverse-sigmoid dural sinus without an intervening capillary bed. What is the fundamental hemodynamic driver of her clinical symptoms?",
        "options": [
            {"label": "A", "text": "High-pressure arterial inflow causing retrograde hypertension within the dural venous system", "is_correct": True},
            {"label": "B", "text": "Hypoperfusion of the inner ear cochlea from systemic arterial steal through the shunt", "is_correct": False},
            {"label": "C", "text": "Severe intracranial hypotension from continuous cerebrospinal fluid leak into the sinus", "is_correct": False},
            {"label": "D", "text": "Compression of the cochlear nerve by a cavernous internal carotid artery pseudoaneurysm", "is_correct": False},
            {"label": "E", "text": "Occlusion of the internal jugular vein by an extrinsic parapharyngeal paraganglioma", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "A dural arteriovenous fistula (dAVF) is an acquired vascular malformation where meningeal arteries (e.g., branches of external carotid) shunt high-pressure arterial blood directly into a dural venous sinus (most commonly the transverse, sigmoid, or cavernous sinus). Pulsatile tinnitus results from turbulent high-flow shunting near the temporal bone. Retrograde venous hypertension engorges cortical and orbital veins, carrying a high risk of intracranial hemorrhage and ophthalmic venous stasis.",
        "high_yield_takeaway": "Dural arteriovenous fistulas shunt high-pressure arterial blood into dural sinuses, causing pulsatile tinnitus, retro-orbital pain, and retrograde venous hypertension."
    }
]

if __name__ == "__main__":
    for q in u6_questions:
        check_q(q)
    print("gen_g_h_u6.py: All 20 questions passed validation!")
