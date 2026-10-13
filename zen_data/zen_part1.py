# zen_part1.py - Topics 1 to 4 (80 Questions total)
import json

part1_questions = [
    # =========================================================================
    # 1. CENTRAL NERVOUS SYSTEM ANATOMY (20 Questions: Q1 - Q20)
    # =========================================================================
    {
        "q_num": "CNS-01",
        "category": "Central Nervous System Anatomy",
        "stem": "A 68-year-old man with a history of poorly controlled hypertension presents to the emergency department with acute-onset right-sided hemiparesis and right-sided hemisensory loss. Physical examination demonstrates 2/5 strength in both the right upper and lower extremities, with hyperreflexia and an extensor plantar response on the right. Sensation to pinprick, light touch, and vibration is markedly diminished on the entire right side of the body. Cranial nerve examination reveals right lower facial drooping with forehead sparing and deviation of the tongue to the right on protrusion. Non-contrast CT of the head reveals a small, focal lacunar infarct. Damage to which of the following structures is most likely responsible for this patient's combined motor and sensory presentation?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Anterior limb of the internal capsule"},
            {"letter": "B", "is_correct": False, "text": "Genu of the internal capsule"},
            {"letter": "C", "is_correct": True, "text": "Posterior limb of the internal capsule"},
            {"letter": "D", "is_correct": False, "text": "Medial lemniscus in the caudal medulla"},
            {"letter": "E", "is_correct": False, "text": "Ventral posteromedial nucleus of the thalamus"}
        ],
        "explanation": "Correct Answer: C. Posterior limb of the internal capsule.\n\nThe posterior limb of the internal capsule contains both descending corticospinal motor tracts (conveying voluntary motor control to the contralateral body) and ascending third-order sensory fibers from the thalamus to the primary somatosensory cortex (VPL/VPM projections). A lacunar infarct in the posterior limb causes pure motor hemiparesis or combined sensorimotor deficits affecting the contralateral face, arm, and leg equally.\n\n• Option A is incorrect: The anterior limb conveys frontopontine fibers and thalamocortical connections involved in cognitive and limbic circuits, not main motor or sensory pathways.\n• Option B is incorrect: The genu carries corticobulbar fibers innervating cranial nerve motor nuclei; a lesion here produces primarily contralateral lower facial and hypoglossal weakness without hemibody sensory loss.\n• Option D is incorrect: A medial lemniscus lesion in the caudal medulla produces contralateral loss of vibration and proprioception, but spares motor tracts and pinprick/temperature sensation.\n• Option E is incorrect: The VPM nucleus relays sensory information from the face (trigeminal pathway), not the hemibody."
    },
    {
        "q_num": "CNS-02",
        "category": "Central Nervous System Anatomy",
        "stem": "A 62-year-old woman presents with sudden onset of severe vertigo, nausea, and unsteady gait. Neurological examination reveals right-sided Horner syndrome (ptosis, miosis, anhidrosis), loss of pain and temperature sensation on the right side of her face and the left side of her body, dysphagia, hoarseness, and right-sided limb ataxia. Motor strength is 5/5 in all extremities. An occlusion of which of the following blood vessels is the most likely cause of this patient's symptoms?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Anterior spinal artery"},
            {"letter": "B", "is_correct": False, "text": "Basilar artery paramedian branches"},
            {"letter": "C", "is_correct": True, "text": "Posterior inferior cerebellar artery (PICA)"},
            {"letter": "D", "is_correct": False, "text": "Superior cerebellar artery (SCA)"},
            {"letter": "E", "is_correct": False, "text": "Anterior inferior cerebellar artery (AICA)"}
        ],
        "explanation": "Correct Answer: C. Posterior inferior cerebellar artery (PICA).\n\nThis patient presents with Wallenberg syndrome (lateral medullary syndrome), caused by occlusion of the PICA or vertebral artery. The classic findings are:\n• Nucleus ambiguus (CN IX, X, XI): Dysphagia, hoarseness, decreased gag reflex.\n• Vestibular nuclei: Vertigo, nystagmus, vomiting.\n• Spinal trigeminal nucleus & tract: Ipsilateral facial pain/temperature loss.\n• Spinothalamic tract: Contralateral body pain/temperature loss.\n• Descending sympathetic fibers: Ipsilateral Horner syndrome.\n• Inferior cerebellar peduncle: Ipsilateral cerebellar ataxia.\n\n• Option A is incorrect: Occlusion of the anterior spinal artery causes medial medullary syndrome (contralateral hemiparesis, contralateral DCML sensory loss, and ipsilateral tongue deviation).\n• Option E is incorrect: AICA infarction causes lateral pontine syndrome, uniquely characterized by ipsilateral facial paralysis (CN VII) and hearing loss (CN VIII)."
    },
    {
        "q_num": "CNS-03",
        "category": "Central Nervous System Anatomy",
        "stem": "A 55-year-old man who underwent clipping of a ruptured anterior communicating artery aneurysm is noted to have significant short-term memory impairment and confabulation. An MRI reveals bilateral ischemic necrosis of the anterior medial temporal lobes and the fornix. The fornix serves as a major efferent projection tract connecting which of the following pairs of anatomical structures?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Amygdala to the septal nuclei"},
            {"letter": "B", "is_correct": True, "text": "Hippocampus to the mammillary bodies"},
            {"letter": "C", "is_correct": False, "text": "Substantia nigra to the striatum"},
            {"letter": "D", "is_correct": False, "text": "Locus coeruleus to the cingulate cortex"},
            {"letter": "E", "is_correct": False, "text": "Cerebellum to the red nucleus"}
        ],
        "explanation": "Correct Answer: B. Hippocampus to the mammillary bodies.\n\nThe fornix is a C-shaped white matter bundle that serves as the principal output tract of the hippocampus in the limbic system (Papez circuit). It projects from the subiculum and hippocampus to the mammillary bodies of the hypothalamus and the anterior thalamic nucleus. Disruption of the fornix causes dense anterograde amnesia and inability to consolidate new declarative memories.\n\n• Option A is incorrect: The stria terminalis and ventral amygdalofugal pathway connect the amygdala to the hypothalamus and septal nuclei.\n• Option C is incorrect: The nigrostriatal pathway connects the substantia nigra pars compacta to the caudate and putamen.\n• Option E is incorrect: The superior cerebellar peduncle (dentatorubrothalamic tract) connects the deep cerebellar nuclei to the red nucleus."
    },
    {
        "q_num": "CNS-04",
        "category": "Central Nervous System Anatomy",
        "stem": "A 71-year-old man with long-standing atrial fibrillation develops acute weakness of his left lower extremity. On examination, strength in the left leg is 1/5, while strength in the left arm and face is 5/5. There is loss of cortical sensory modalities (graphesthesia and stereognosis) in the left foot and leg. He exhibits primitive reflexes (grasp reflex) and urinary incontinence. Occlusion of which cerebral artery is most consistent with this clinical picture?",
        "options": [
            {"letter": "A", "is_correct": True, "text": "Right anterior cerebral artery (ACA)"},
            {"letter": "B", "is_correct": False, "text": "Right middle cerebral artery (MCA) superior division"},
            {"letter": "C", "is_correct": False, "text": "Right posterior cerebral artery (PCA)"},
            {"letter": "D", "is_correct": False, "text": "Right lenticulostriate artery"},
            {"letter": "E", "is_correct": False, "text": "Right anterior choroidal artery"}
        ],
        "explanation": "Correct Answer: A. Right anterior cerebral artery (ACA).\n\nThe ACA supplies the medial surface of the frontal and parietal lobes, which corresponds to the lower extremity representation on the motor and sensory homunculi. Occlusion leads to contralateral motor and sensory deficits predominantly affecting the leg and foot, along with frontal lobe signs such as urinary incontinence, abulia, and primitive reflexes.\n\n• Option B is incorrect: MCA infarcts affect the lateral convexity, causing contralateral face and arm weakness greater than leg weakness, as well as aphasia (dominant hemisphere) or hemineglect (non-dominant hemisphere).\n• Option C is incorrect: PCA infarcts supply the occipital lobe and inferior temporal lobe, producing contralateral homonymous hemianopia with macular sparing.\n• Option D is incorrect: Lenticulostriate infarcts affect the posterior limb of the internal capsule, causing dense contralateral weakness affecting the face, arm, and leg equally."
    },
    {
        "q_num": "CNS-05",
        "category": "Central Nervous System Anatomy",
        "stem": "A 45-year-old woman is evaluated for resting tremor, bradykinesia, and cogwheel rigidity. Degeneration of dopaminergic neurons in the substantia nigra pars compacta leads to decreased dopamine stimulation of the striatum. In the indirect pathway of the basal ganglia, decreased dopamine binding to D2 receptors results in which of the following alterations in neural activity?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Decreased inhibition of the internal globus pallidus (GPi)"},
            {"letter": "B", "is_correct": False, "text": "Inhibition of the subthalamic nucleus (STN)"},
            {"letter": "C", "is_correct": True, "text": "Increased excitation of the internal globus pallidus (GPi) by the subthalamic nucleus"},
            {"letter": "D", "is_correct": False, "text": "Disinhibition of the ventral anterior/ventrolateral (VA/VL) thalamus"},
            {"letter": "E", "is_correct": False, "text": "Increased dopamine release in the motor cortex"}
        ],
        "explanation": "Correct Answer: C. Increased excitation of the internal globus pallidus (GPi) by the subthalamic nucleus.\n\nIn the indirect pathway:\n1. Striatal neurons expressing inhibitory D2 receptors project to the globus pallidus externus (GPe) via GABA.\n2. Loss of dopamine disinhibits (activates) these striatal D2 neurons, leading to excessive GABAergic inhibition of the GPe.\n3. Because the GPe is inhibited, it fails to inhibit the subthalamic nucleus (STN).\n4. The STN becomes hyperactive and fires excitatory glutamatergic signals to the globus pallidus internus (GPi).\n5. Hyperactive GPi sends excessive inhibitory GABA to the thalamus (VA/VL), decreasing motor cortex excitation and causing bradykinesia.\n\n• Options A and D are incorrect: The thalamus is excessively inhibited, not disinhibited.\n• Option B is incorrect: The STN is disinhibited (hyperactive), not inhibited."
    },
    {
        "q_num": "CNS-06",
        "category": "Central Nervous System Anatomy",
        "stem": "A 23-year-old professional boxer presents with double vision when walking down stairs. On physical examination, he tilts his head to the left to compensate for vertical diplopia. When looking straight ahead, his right eye is slightly extorted and elevated. Examination confirms right superior oblique muscle palsy. The axons of the cranial nerve innervating this muscle exit the brainstem in which of the following locations?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Ventral midbrain medial to the cerebral peduncles"},
            {"letter": "B", "is_correct": True, "text": "Dorsal midbrain inferior to the inferior colliculi"},
            {"letter": "C", "is_correct": False, "text": "Cerebellopontine angle"},
            {"letter": "D", "is_correct": False, "text": "Preolivary sulcus of the medulla"},
            {"letter": "E", "is_correct": False, "text": "Ventral pontomedullary junction"}
        ],
        "explanation": "Correct Answer: B. Dorsal midbrain inferior to the inferior colliculi.\n\nThe trochlear nerve (CN IV) innervates the superior oblique muscle (which depresses and intorts the eye, particularly in adduction). CN IV has two unique anatomical characteristics:\n1. It is the only cranial nerve that exits from the dorsal (posterior) surface of the brainstem (just caudal to the inferior colliculi).\n2. Its fibers decussate within the anterior medullary velum before exiting, meaning the right CN IV nucleus innervates the left superior oblique muscle, but the exiting nerve supplies the ipsilateral eye once outside the brainstem.\n\n• Option A is incorrect: The oculomotor nerve (CN III) emerges ventrally from the interpeduncular fossa of the midbrain.\n• Option D is incorrect: The hypoglossal nerve (CN XII) emerges from the preolivary sulcus of the medulla.\n• Option E is incorrect: The abducens nerve (CN VI) emerges ventrally at the pontomedullary junction."
    },
    {
        "q_num": "CNS-07",
        "category": "Central Nervous System Anatomy",
        "stem": "A 34-year-old woman with multiple sclerosis presents with impaired horizontal gaze. When asked to look to the left, her left eye abducts with fine horizontal nystagmus, but her right eye fails to adduct past the midline. When tested for convergence, however, both eyes adduct symmetrically and pupils constrict normally. This patient's deficit is due to a demyelinating lesion involving which of the following brainstem tracts?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Central tegmental tract"},
            {"letter": "B", "is_correct": False, "text": "Lateral lemniscus"},
            {"letter": "C", "is_correct": True, "text": "Medial longitudinal fasciculus (MLF)"},
            {"letter": "D", "is_correct": False, "text": "Medial lemniscus"},
            {"letter": "E", "is_correct": False, "text": "Spinothalamic tract"}
        ],
        "explanation": "Correct Answer: C. Medial longitudinal fasciculus (MLF).\n\nThis patient exhibits internuclear ophthalmoplegia (INO), a classic manifestation of multiple sclerosis involving the MLF. The MLF is a heavily myelinated brainstem pathway that coordinates conjugate horizontal eye movements by transmitting signals from the contralateral abducens nucleus (CN VI) in the pons to the ipsilateral oculomotor nucleus (CN III, medial rectus subnucleus) in the midbrain. \n• Impaired right adduction on left lateral gaze indicates a right MLF lesion.\n• Convergence is preserved because it is mediated by cortical pathways projecting directly to the pretectal area and CN III nuclei without relying on the MLF.\n\n• Option A is incorrect: The central tegmental tract connects the red nucleus to the inferior olivary nucleus; lesions cause palatal myoclonus.\n• Option B is incorrect: The lateral lemniscus carries auditory information from the cochlear nuclei to the inferior colliculus."
    },
    {
        "q_num": "CNS-08",
        "category": "Central Nervous System Anatomy",
        "stem": "An 80-year-old man presents with progressive memory loss and disorientation. Neuropathological evaluation at autopsy reveals marked atrophy of the nucleus basalis of Meynert. This nucleus is located in the basal forebrain and serves as the major site of synthesis for which of the following neurotransmitters?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Dopamine"},
            {"letter": "B", "is_correct": False, "text": "Norepinephrine"},
            {"letter": "C", "is_correct": False, "text": "Serotonin"},
            {"letter": "D", "is_correct": True, "text": "Acetylcholine"},
            {"letter": "E", "is_correct": False, "text": "Gamma-aminobutyric acid (GABA)"}
        ],
        "explanation": "Correct Answer: D. Acetylcholine.\n\nThe nucleus basalis of Meynert (located in the substantia innominata of the basal forebrain) contains the primary cholinergic projection neurons that innervate the neocortex and hippocampus. Profound loss of these cholinergic neurons is a hallmark of Alzheimer disease, providing the biochemical basis for treatment with acetylcholinesterase inhibitors (donepezil, rivastigmine, galantamine).\n\n• Option A is incorrect: Dopamine is synthesized predominantly in the substantia nigra pars compacta and ventral tegmental area (VTA).\n• Option B is incorrect: Norepinephrine is synthesized in the locus coeruleus in the dorsal rostral pons.\n• Option C is incorrect: Serotonin is synthesized in the raphe nuclei of the brainstem."
    },
    {
        "q_num": "CNS-09",
        "category": "Central Nervous System Anatomy",
        "stem": "A 54-year-old man presents with progressive difficulty walking. Physical examination reveals broad-based gait ataxia, marked truncal instability, and titubation of the trunk. However, rapid alternating movements of the hands (dysdiadochokinesia) and finger-to-nose testing are performed smoothly and accurately without tremor. Which region of the cerebellum is most likely damaged in this patient?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Lateral cerebellar hemisphere"},
            {"letter": "B", "is_correct": True, "text": "Cerebellar vermis"},
            {"letter": "C", "is_correct": False, "text": "Dentate nucleus"},
            {"letter": "D", "is_correct": False, "text": "Superior cerebellar peduncle"},
            {"letter": "E", "is_correct": False, "text": "Posterior lobe lateral zone"}
        ],
        "explanation": "Correct Answer: B. Cerebellar vermis.\n\nThe cerebellar vermis forms the midline zone of the cerebellum and projects via the fastigial nucleus to the vestibular nuclei and reticulospinal tracts (vestibulospinal and reticulospinal pathways), controlling axial and truncal stability. \n• Midline vermis lesions (common in chronic alcoholism causing thiamine deficiency and anterior vermian atrophy) result in truncal ataxia, broad-based staggering gait, and titubation, while sparing appendicular coordination.\n• Lateral hemisphere lesions (affecting the cerebrocerebellum and dentate nucleus) cause appendicular ataxia, dysmetria, intention tremor, and dysdiadochokinesia of the ipsilateral limbs."
    },
    {
        "q_num": "CNS-10",
        "category": "Central Nervous System Anatomy",
        "stem": "A 60-year-old woman is admitted after an ischemic stroke. On neurological examination, she speaks fluently at a normal rate with normal melody, but her speech is devoid of meaning and full of neologisms ('word salad'). She is completely unable to follow spoken commands or repeat short phrases ('no ifs, ands, or buts'). Which Brodmann area and anatomical location corresponds to the damaged cortical region?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Brodmann area 44/45 in the inferior frontal gyrus"},
            {"letter": "B", "is_correct": True, "text": "Brodmann area 22 in the superior temporal gyrus"},
            {"letter": "C", "is_correct": False, "text": "Brodmann area 4 in the precentral gyrus"},
            {"letter": "D", "is_correct": False, "text": "Brodmann area 17 in the occipital pole"},
            {"letter": "E", "is_correct": False, "text": "Brodmann area 39 in the angular gyrus"}
        ],
        "explanation": "Correct Answer: B. Brodmann area 22 in the superior temporal gyrus.\n\nThis patient exhibits Wernicke (receptive/fluent) aphasia, characterized by impaired comprehension, intact fluency, and impaired repetition. Wernicke area corresponds to Brodmann area 22 in the posterior part of the superior temporal gyrus of the dominant (usually left) hemisphere, supplied by the inferior division of the middle cerebral artery (MCA).\n\n• Option A is incorrect: Brodmann areas 44 and 45 represent Broca area in the inferior frontal gyrus; lesions cause non-fluent expressive aphasia with preserved comprehension.\n• Option C is incorrect: Brodmann area 4 is the primary motor cortex in the precentral gyrus.\n• Option E is incorrect: Brodmann area 39 is the angular gyrus; lesions in the dominant hemisphere cause Gerstmann syndrome (agraphia, acalculia, finger agnosia, left-right disorientation)."
    },
    {
        "q_num": "CNS-11",
        "category": "Central Nervous System Anatomy",
        "stem": "A 50-year-old man presents with sudden loss of vision on the left side. Visual field testing reveals left homonymous hemianopia with macular sparing. Pupillary light reflexes are equal and reactive bilaterally. An ischemic lesion in which of the following vascular territories accounts for this finding?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Right anterior choroidal artery"},
            {"letter": "B", "is_correct": False, "text": "Right middle cerebral artery inferior division"},
            {"letter": "C", "is_correct": True, "text": "Right posterior cerebral artery (PCA)"},
            {"letter": "D", "is_correct": False, "text": "Right ophthalmic artery"},
            {"letter": "E", "is_correct": False, "text": "Anterior communicating artery"}
        ],
        "explanation": "Correct Answer: C. Right posterior cerebral artery (PCA).\n\nOcclusion of the PCA causes ischemia of the occipital cortex (primary visual cortex, Brodmann area 17). Damage to the right primary visual cortex leads to contralateral (left) homonymous hemianopia. Macular sparing occurs because the macular representation at the occipital pole receives dual collateral blood supply from both the PCA and the MCA.\n\n• Option A is incorrect: Anterior choroidal artery occlusion damages the posterior limb of the internal capsule and optic tract/LGN, causing homonymous hemianopia without macular sparing.\n• Option B is incorrect: MCA inferior division damages Meyer loop in the temporal lobe, producing superior quadrantanopia ('pie in the sky').\n• Option D is incorrect: Ophthalmic artery occlusion causes monocular blindness."
    },
    {
        "q_num": "CNS-12",
        "category": "Central Nervous System Anatomy",
        "stem": "A 28-year-old man involved in a motorcycle collision strikes his forehead on the steering wheel. A non-contrast head CT demonstrates fracture of the cribriform plate of the ethmoid bone with clear rhinorrhea. Testing the discharge confirms it is cerebrospinal fluid (positive for beta-2 transferrin). Which of the following cranial nerves is most vulnerable to transection in this injury?",
        "options": [
            {"letter": "A", "is_correct": True, "text": "Cranial nerve I"},
            {"letter": "B", "is_correct": False, "text": "Cranial nerve II"},
            {"letter": "C", "is_correct": False, "text": "Cranial nerve III"},
            {"letter": "D", "is_correct": False, "text": "Cranial nerve V (ophthalmic division)"},
            {"letter": "E", "is_correct": False, "text": "Cranial nerve VII"}
        ],
        "explanation": "Correct Answer: A. Cranial nerve I.\n\nThe olfactory nerve (CN I) consists of non-myelinated primary olfactory axons that traverse the multiple perforations of the cribriform plate of the ethmoid bone to synapse in the olfactory bulb. Cribriform plate fractures frequently shear these delicate fila olfactoria, leading to tearing of the underlying meninges (causing CSF rhinorrhea) and permanent anosmia (loss of smell).\n\n• Option B is incorrect: CN II traverses the optic canal in the sphenoid bone.\n• Options C and D are incorrect: CN III and CN V1 exit the skull through the superior orbital fissure.\n• Option E is incorrect: CN VII exits via the internal acoustic meatus and stylomastoid foramen."
    },
    {
        "q_num": "CNS-13",
        "category": "Central Nervous System Anatomy",
        "stem": "A 48-year-old man presents with progressive spastic paraparesis. Physical examination shows bilateral lower extremity weakness with hyperactive patellar reflexes and sustained ankle clonus. An MRI demonstrates compression of the lateral funiculus of the thoracic spinal cord. The descending axons responsible for voluntary motor control within this tract decussate at which anatomical level?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Midbrain tegmentum"},
            {"letter": "B", "is_correct": False, "text": "Upper rostral pons"},
            {"letter": "C", "is_correct": True, "text": "Caudal medulla (pyramidal decussation)"},
            {"letter": "D", "is_correct": False, "text": "Anterior white commissure of the spinal cord"},
            {"letter": "E", "is_correct": False, "text": "Ventral tegmental decussation"}
        ],
        "explanation": "Correct Answer: C. Caudal medulla (pyramidal decussation).\n\nThe lateral corticospinal tract arises from upper motor neurons in the primary motor cortex (Brodmann area 4), descends through the corona radiata, posterior limb of the internal capsule, middle 3/5 of the cerebral peduncle (crus cerebri), and basilar pons. At the medullary pyramids in the caudal medulla, approximately 85-90% of the fibers cross the midline at the pyramidal decussation to descend in the contralateral lateral funiculus of the spinal cord.\n\n• Option D is incorrect: The anterior white commissure is where second-order spinothalamic axons cross 1-2 segments above their entry level."
    },
    {
        "q_num": "CNS-14",
        "category": "Central Nervous System Anatomy",
        "stem": "A 73-year-old woman is brought to the clinic by her daughter due to progressive behavioral changes. The patient has become hyperoral (frequently placing non-food objects in her mouth), inappropriately placid with loss of normal fear responses, and exhibits hypersexuality and visual agnosia. MRI shows prominent bilateral anterior temporal lobe atrophy. These findings are most characteristic of injury to which limbic structure?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Cingulate gyrus"},
            {"letter": "B", "is_correct": True, "text": "Amygdala"},
            {"letter": "C", "is_correct": False, "text": "Septal nuclei"},
            {"letter": "D", "is_correct": False, "text": "Mammillary bodies"},
            {"letter": "E", "is_correct": False, "text": "Anterior thalamic nucleus"}
        ],
        "explanation": "Correct Answer: B. Amygdala.\n\nThis patient exhibits Klüver-Bucy syndrome, caused by bilateral lesions of the amygdala and anterior temporal lobes (commonly due to herpes simplex encephalitis, trauma, or frontotemporal lobar degeneration). Clinical features include hyperorality, hypersexuality, docility/placidity, psychic blindness (visual agnosia), and hyperphagia.\n\n• Option A is incorrect: Cingulate gyrus lesions result in akinetic mutism or apathy.\n• Option D is incorrect: Bilateral mammillary body necrosis occurs in Wernicke-Korsakoff syndrome, characterized by ophthalmoplegia, ataxia, confusion, and confabulation."
    },
    {
        "q_num": "CNS-15",
        "category": "Central Nervous System Anatomy",
        "stem": "A neurosurgeon is planning a transsphenoidal resection of a pituitary macroadenoma that has expanded laterally into the cavernous sinus. Which of the following anatomical structures passes through the center of the cavernous sinus alongside the internal carotid artery, making it the most susceptible to compressive injury from an intrasinus pathology?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Oculomotor nerve (CN III)"},
            {"letter": "B", "is_correct": False, "text": "Trochlear nerve (CN IV)"},
            {"letter": "C", "is_correct": False, "text": "Ophthalmic division of the trigeminal nerve (CN V1)"},
            {"letter": "D", "is_correct": False, "text": "Maxillary division of the trigeminal nerve (CN V2)"},
            {"letter": "E", "is_correct": True, "text": "Abducens nerve (CN VI)"}
        ],
        "explanation": "Correct Answer: E. Abducens nerve (CN VI).\n\nThe cavernous sinus contains neurovascular structures either embedded within its lateral dural wall or coursing freely through its venous lumen:\n• Lateral wall: CN III, CN IV, CN V1, and CN V2 (superior to inferior).\n• Free inside sinus center: Internal carotid artery and CN VI.\nBecause CN VI floats directly within the sinus lumen adjacent to the carotid artery, it is the most vulnerable nerve to early compression from carotid cavernous fistulas, aneurysms, or pituitory expansion into the sinus, causing isolated lateral rectus palsy (inability to abduct the eye)."
    },
    {
        "q_num": "CNS-16",
        "category": "Central Nervous System Anatomy",
        "stem": "A 66-year-old man presents with uncontrollable, violent, flinging movements of his left arm and leg (hemiballismus). A non-contrast head CT reveals a small hypertensive intraparenchymal hemorrhage in the diencephalon. The lesion is located in a lens-shaped nucleus that uses glutamate to excite the internal globus pallidus. Which nucleus is damaged?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Caudate nucleus"},
            {"letter": "B", "is_correct": False, "text": "Putamen"},
            {"letter": "C", "is_correct": True, "text": "Subthalamic nucleus of Luys"},
            {"letter": "D", "is_correct": False, "text": "Substantia nigra pars reticulata"},
            {"letter": "E", "is_correct": False, "text": "Ventral lateral nucleus of the thalamus"}
        ],
        "explanation": "Correct Answer: C. Subthalamic nucleus of Luys.\n\nHemiballismus consists of sudden, wild, flailing movements of the contralateral limbs. It is caused by a lesion (most often a lacunar stroke) of the contralateral subthalamic nucleus (STN). The STN normally provides excitatory (glutamatergic) drive to the globus pallidus internus (GPi). Loss of STN function decreases GPi output, leading to disinhibition of the motor thalamus (VA/VL) and excessive cortical motor excitation.\n\n• Option A is incorrect: Caudate degeneration causes chorea in Huntington disease.\n• Option B is incorrect: Putamen lesions cause dystonia or parkinsonian features."
    },
    {
        "q_num": "CNS-17",
        "category": "Central Nervous System Anatomy",
        "stem": "A 29-year-old man presents with right-sided facial weakness. When asked to smile, the right side of his mouth does not move. When asked to close his eyes tightly or wrinkle his forehead, the right eye remains partially open and the right forehead does not wrinkle. He also reports hyperacusis in his right ear and loss of taste on the anterior two-thirds of his tongue. Which of the following cranial nerves is affected, and where did the lesion occur?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Left primary motor cortex"},
            {"letter": "B", "is_correct": False, "text": "Left internal capsule genu"},
            {"letter": "C", "is_correct": True, "text": "Right cranial nerve VII peripheral to the brainstem"},
            {"letter": "D", "is_correct": False, "text": "Right cranial nerve V3 peripheral branch"},
            {"letter": "E", "is_correct": False, "text": "Left facial motor nucleus in the pons"}
        ],
        "explanation": "Correct Answer: C. Right cranial nerve VII peripheral to the brainstem.\n\nThis patient has Bell palsy (lower motor neuron lesion of CN VII):\n• Forehead involvement distinguishes LMN from UMN lesions because the upper facial nucleus receives bilateral corticobulbar innervation; an UMN lesion (cortex or internal capsule) spares the forehead, while a LMN lesion paralyzes the entire ipsilateral face (both upper and lower).\n• Associated symptoms: Stapedius muscle paralysis causes hyperacusis; chorda tympani involvement causes loss of taste on the anterior 2/3 of the tongue and reduced submandibular/sublingual salivation.\n\n• Options A and B are incorrect: UMN lesions spare forehead wrinkling.\n• Option E is incorrect: A left pontine lesion would cause left-sided facial weakness, not right-sided."
    },
    {
        "q_num": "CNS-18",
        "category": "Central Nervous System Anatomy",
        "stem": "A 70-year-old man presents with right-sided resting tremor, rigidity, and gait impairment. He is prescribed levodopa/carbidopa. Histological examination of the brainstem in patients with this disorder demonstrates loss of neuromelanin-pigmented neurons containing alpha-synuclein-positive eosinophilic inclusions (Lewy bodies). In which anatomical structure are these pigmented neurons located?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Red nucleus"},
            {"letter": "B", "is_correct": True, "text": "Substantia nigra pars compacta"},
            {"letter": "C", "is_correct": False, "text": "Periaqueductal gray"},
            {"letter": "D", "is_correct": False, "text": "Inferior olivary nucleus"},
            {"letter": "E", "is_correct": False, "text": "Dentate nucleus"}
        ],
        "explanation": "Correct Answer: B. Substantia nigra pars compacta.\n\nParkinson disease is characterized neuropathologically by the loss of dopaminergic neurons in the substantia nigra pars compacta (located in the midbrain). These neurons normally contain dark neuromelanin pigment (derived from dopamine oxidation). Surviving neurons exhibit intracellular round, eosinophilic Lewy bodies composed of aggregated alpha-synuclein.\n\n• Option A is incorrect: The red nucleus is involved in rubrospinal motor coordination.\n• Option C is incorrect: The periaqueductal gray regulates descending pain modulation.\n• Option D is incorrect: The inferior olive projects climbing fibers to Purkinje cells in the cerebellum."
    },
    {
        "q_num": "CNS-19",
        "category": "Central Nervous System Anatomy",
        "stem": "A 58-year-old woman is found to have an intracranial meningioma compressing the jugular foramen on the right side. On physical examination, which of the following deficits would be expected in this patient?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Loss of corneal reflex and facial sensation"},
            {"letter": "B", "is_correct": True, "text": "Loss of gag reflex and weakness turning head to the left"},
            {"letter": "C", "is_correct": False, "text": "Deviation of the tongue to the right on protrusion"},
            {"letter": "D", "is_correct": False, "text": "Inability to abduct the right eye"},
            {"letter": "E", "is_correct": False, "text": "Right-sided facial paralysis and hearing loss"}
        ],
        "explanation": "Correct Answer: B. Loss of gag reflex and weakness turning head to the left.\n\nThe jugular foramen transmits cranial nerves IX (glossopharyngeal), X (vagus), and XI (accessory), as well as the internal jugular vein (Vernet syndrome):\n• CN IX lesion: Loss of afferent gag reflex, loss of sensation/taste on posterior 1/3 of tongue.\n• CN X lesion: Loss of efferent gag reflex, uvula deviation away from the lesion, hoarseness.\n• CN XI lesion: Weakness of ipsilateral sternocleidomastoid (causing difficulty turning the head to the contralateral / left side) and trapezius (shoulder droop).\n\n• Option C is incorrect: CN XII exits via the hypoglossal canal.\n• Option D is incorrect: CN VI exits via the superior orbital fissure.\n• Option E is incorrect: CN VII and VIII traverse the internal acoustic meatus."
    },
    {
        "q_num": "CNS-20",
        "category": "Central Nervous System Anatomy",
        "stem": "A 65-year-old man undergoes an endovascular repair of a thoracoabdominal aortic aneurysm. Postoperatively, he is unable to move his legs and has lost sensation to pinprick and temperature bilaterally below the level of T10. However, conscious proprioception, two-point discrimination, and vibration sensation in both lower extremities remain completely normal. Which spinal cord vascular territory was compromised during the aortic cross-clamping?",
        "options": [
            {"letter": "A", "is_correct": True, "text": "Anterior spinal artery (artery of Adamkiewicz)"},
            {"letter": "B", "is_correct": False, "text": "Posterior spinal arteries"},
            {"letter": "C", "is_correct": False, "text": "Posterior cerebral artery"},
            {"letter": "D", "is_correct": False, "text": "Basilar artery"},
            {"letter": "E", "is_correct": False, "text": "Vertebral artery paramedian branch"}
        ],
        "explanation": "Correct Answer: A. Anterior spinal artery (artery of Adamkiewicz).\n\nThis patient has anterior spinal artery syndrome (Beck syndrome), a feared complication of thoracic aortic surgery. The anterior spinal artery supplies the anterior 2/3 of the spinal cord (lateral corticospinal tracts, spinothalamic tracts, and anterior horn motor neurons). Infarction causes bilateral spastic paraplegia and loss of pain/temperature below the lesion. The posterior columns (dorsal columns: vibration and proprioception) are spared because they receive separate arterial perfusion from the paired posterior spinal arteries."
    },

    # =========================================================================
    # 2. CENTRAL NERVOUS SYSTEM DEVELOPMENT (20 Questions: Q21 - Q40)
    # =========================================================================
    {
        "q_num": "DEV-01",
        "category": "Central Nervous System Development",
        "stem": "A 24-year-old primigravida at 16 weeks gestation undergoes routine prenatal screening. Maternal serum alpha-fetoprotein (MSAFP) is found to be significantly elevated (3.2 multiples of the median). High-resolution ultrasound reveals a failure of the rostral neuropore to close, with absence of the calvarium and cerebral hemispheres. Which of the following amniotic fluid biomarkers would be elevated alongside alpha-fetoprotein in this neural tube defect?",
        "options": [
            {"letter": "A", "is_correct": True, "text": "Acetylcholinesterase"},
            {"letter": "B", "is_correct": False, "text": "Alkaline phosphatase"},
            {"letter": "C", "is_correct": False, "text": "Creatine kinase-BB"},
            {"letter": "D", "is_correct": False, "text": "Beta-human chorionic gonadotropin"},
            {"letter": "E", "is_correct": False, "text": "Unconjugated estriol"}
        ],
        "explanation": "Correct Answer: A. Acetylcholinesterase.\n\nFailure of the rostral (cranial) neuropore to close during the 4th week of development results in anencephaly (meroencephaly). When the neural tube fails to close, fetal cerebrospinal fluid and neural tissue are exposed directly to the amniotic cavity, allowing large amounts of alpha-fetoprotein (AFP) and acetylcholinesterase (AChE) to transudate into the amniotic fluid. Detecting elevated AChE in amniotic fluid confirms an open neural tube defect.\n\n• Option D is incorrect: Elevated hCG is associated with trisomy 21 (Down syndrome), not neural tube defects.\n• Option E is incorrect: Estriol is decreased in trisomies 18 and 21."
    },
    {
        "q_num": "DEV-02",
        "category": "Central Nervous System Development",
        "stem": "A newborn male is examined in the nursery. Physical examination reveals a hairy patch and a small cutaneous dimple over the lower lumbar spine at L5-S1. The infant moves both lower extremities vigorously with normal muscle tone and intact anal wink reflex. A sagittal MRI demonstrates failure of the posterior vertebral arches to fuse, but the spinal cord, nerve roots, and meninges remain entirely within the spinal canal. Which of the following is the diagnosis?",
        "options": [
            {"letter": "A", "is_correct": True, "text": "Spina bifida occulta"},
            {"letter": "B", "is_correct": False, "text": "Meningocele"},
            {"letter": "C", "is_correct": False, "text": "Meningomyelocele"},
            {"letter": "D", "is_correct": False, "text": "Myeloschisis"},
            {"letter": "E", "is_correct": False, "text": "Caudal regression syndrome"}
        ],
        "explanation": "Correct Answer: A. Spina bifida occulta.\n\nSpina bifida occulta is the mildest form of neural tube defect, characterized by failure of the bony vertebral arches to fuse posteriorly (usually at L5-S1) with an intact overlying skin surface. The dura mater and spinal cord remain completely inside the vertebral canal without herniation. Cutaneous markers include a tuft of hair, skin dimple, hemangioma, or lipoma at the level of the defect. MSAFP levels are typically normal because the defect is closed.\n\n• Option B is incorrect: Meningocele involves herniation of the meninges (dura and arachnoid) through the bony defect, containing CSF but no neural tissue.\n• Option C is incorrect: Meningomyelocele involves herniation of both meninges and spinal cord/nerve roots.\n• Option D is incorrect: Myeloschisis is the most severe open defect where the neural plate failed to fold entirely, leaving exposed neural tissue."
    },
    {
        "q_num": "DEV-03",
        "category": "Central Nervous System Development",
        "stem": "An infant girl born to a 19-year-old mother who received no prenatal care presents with a large sac-like mass protruding from the lumbosacral region containing meninges and malformed spinal cord tissue. Physical examination reveals flaccid paralysis of the lower extremities and urinary dribbling. Brain MRI reveals herniation of the cerebellar vermis and tonsils through the foramen magnum into the cervical canal, accompanied by non-communicating hydrocephalus. Which congenital malformation is present?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Chiari I malformation"},
            {"letter": "B", "is_correct": True, "text": "Chiari II (Arnold-Chiari) malformation"},
            {"letter": "C", "is_correct": False, "text": "Dandy-Walker malformation"},
            {"letter": "D", "is_correct": False, "text": "Holoprosencephaly"},
            {"letter": "E", "is_correct": False, "text": "Schizencephaly"}
        ],
        "explanation": "Correct Answer: B. Chiari II (Arnold-Chiari) malformation.\n\nChiari II malformation is characterized by downward herniation of both the cerebellar vermis and tonsils into the foramen magnum, causing compression of the medulla and aqueductal stenosis (leading to hydrocephalus). It is almost universally associated with a lumbosacral myelomeningocele.\n\n• Option A is incorrect: Chiari I malformation is defined by herniation of cerebellar tonsils only (>5 mm below foramen magnum); it typically presents in adulthood with headaches and neck pain, and is associated with syringomyelia, NOT myelomeningocele.\n• Option C is incorrect: Dandy-Walker malformation is characterized by agenesis of the cerebellar vermis and cystic expansion of the 4th ventricle."
    },
    {
        "q_num": "DEV-04",
        "category": "Central Nervous System Development",
        "stem": "A 3-month-old infant is evaluated for rapidly increasing head circumference (macrocephaly). Neurological examination shows irritability, down-gaze preference ('setting-sun' sign), and developmental delay. Head CT demonstrates complete agenesis of the cerebellar vermis with massive cystic dilation of the fourth ventricle filling the posterior fossa, and an enlarged posterior fossa with elevated tentorium. Which of the following is the diagnosis?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Chiari I malformation"},
            {"letter": "B", "is_correct": False, "text": "Chiari II malformation"},
            {"letter": "C", "is_correct": True, "text": "Dandy-Walker malformation"},
            {"letter": "D", "is_correct": False, "text": "Lissencephaly"},
            {"letter": "E", "is_correct": False, "text": "Holoprosencephaly"}
        ],
        "explanation": "Correct Answer: C. Dandy-Walker malformation.\n\nDandy-Walker malformation is a congenital anomaly of the posterior fossa characterized by the classic triad:\n1. Complete or partial agenesis of the cerebellar vermis.\n2. Cystic dilation of the fourth ventricle.\n3. Enlarged posterior fossa with elevation of the tentorium cerebelli and torcular Herophili.\nThis leads to non-communicating hydrocephalus, macrocephaly, and motor delays.\n\n• Option D is incorrect: Lissencephaly ('smooth brain') is a neuronal migration disorder leading to an absence of gyri and sulci.\n• Option E is incorrect: Holoprosencephaly is failure of the prosencephalon to divide into two cerebral hemispheres."
    },
    {
        "q_num": "DEV-05",
        "category": "Central Nervous System Development",
        "stem": "A female newborn is born with severe craniofacial dysmorphism including hypotelorism, a flat nasal bridge, a single central incisor, and a midline cleft lip and palate. Cranial ultrasound reveals a single large monoventricle with fusion of the frontal lobes and basal ganglia, and absence of the falx cerebri. A mutation in which of the following signaling pathways is most frequently implicated in this disorder?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Wnt/beta-catenin signaling"},
            {"letter": "B", "is_correct": True, "text": "Sonic hedgehog (SHH) signaling"},
            {"letter": "C", "is_correct": False, "text": "Notch receptor signaling"},
            {"letter": "D", "is_correct": False, "text": "Fibroblast growth factor receptor 3 (FGFR3)"},
            {"letter": "E", "is_correct": False, "text": "Homeobox (HOX) gene clusters"}
        ],
        "explanation": "Correct Answer: B. Sonic hedgehog (SHH) signaling.\n\nThis infant has holoprosencephaly, a developmental malformation caused by failure of the prosencephalon (forebrain) to cleave into two cerebral hemispheres along the midline (weeks 5-6). It is strongly associated with mutations in the Sonic Hedgehog (SHH) gene pathway or trisomy 13 (Patau syndrome). Severe forms manifest as cyclopia and proboscis; milder forms show midline facial abnormalities such as cleft lip/palate, hypotelorism, or a single central maxillary incisor.\n\n• Option D is incorrect: FGFR3 mutations cause achondroplasia and thanatophoric dysplasia."
    },
    {
        "q_num": "DEV-06",
        "category": "Central Nervous System Development",
        "stem": "During early embryogenesis, the primary brain vesicles differentiate into five secondary brain vesicles. The diencephalon develops from the prosencephalon. Which of the following adult neurological structures is embryologically derived from the diencephalon?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Cerebral cortex and hippocampus"},
            {"letter": "B", "is_correct": True, "text": "Thalamus, hypothalamus, and optic vesicles/retina"},
            {"letter": "C", "is_correct": False, "text": "Cerebral peduncles and tectum"},
            {"letter": "D", "is_correct": False, "text": "Pons and cerebellum"},
            {"letter": "E", "is_correct": False, "text": "Medulla oblongata"}
        ],
        "explanation": "Correct Answer: B. Thalamus, hypothalamus, and optic vesicles/retina.\n\nEmbryological derivatives of secondary vesicles:\n• Telencephalon (from prosencephalon): Cerebral hemispheres, basal ganglia, hippocampus, lateral ventricles.\n• Diencephalon (from prosencephalon): Thalamus, hypothalamus, epithalamus (pineal gland), optic vesicles, neurohypophysis, 3rd ventricle.\n• Mesencephalon: Midbrain, cerebral aqueduct.\n• Metencephalon (from rhombencephalon): Pons, cerebellum, upper 4th ventricle.\n• Myelencephalon (from rhombencephalon): Medulla oblongata, lower 4th ventricle."
    },
    {
        "q_num": "DEV-07",
        "category": "Central Nervous System Development",
        "stem": "Neural crest cells undergo epithelial-to-mesenchymal transition and migrate extensively throughout the embryo to give rise to a diverse array of non-neuronal and neuronal tissues. Which of the following structures is derived from the neural crest?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Motor neurons of the spinal cord ventral horn"},
            {"letter": "B", "is_correct": False, "text": "Oligodendrocytes of the cerebral white matter"},
            {"letter": "C", "is_correct": True, "text": "Schwann cells and dorsal root ganglia"},
            {"letter": "D", "is_correct": False, "text": "Astrocytes forming the blood-brain barrier"},
            {"letter": "E", "is_correct": False, "text": "Microglia of the brain parenchyma"}
        ],
        "explanation": "Correct Answer: C. Schwann cells and dorsal root ganglia.\n\nNeural crest derivatives ('MOTEL PASS'):\n• Melanocytes\n• Odontoblasts\n• Tracheal cartilage\n• Enterochromaffin cells\n• Laryngeal cartilage\n• Parafollicular (C) cells of thyroid\n• Adrenal medulla (chromaffin cells)\n• Schwann cells\n• Spiral septum (aorticopulmonary septum)\n• Sympathetic and sensory (dorsal root) ganglia, pia and arachnoid mater.\n\n• Options A, B, and D are incorrect: Ventral horn motor neurons, oligodendrocytes, and astrocytes are derived from the neuroectoderm of the neural tube.\n• Option E is incorrect: Microglia are mesodermal in origin (monocyte/macrophage lineage)."
    },
    {
        "q_num": "DEV-08",
        "category": "Central Nervous System Development",
        "stem": "A 26-year-old woman presents to her obstetrician for preconception counseling. She has a history of type 1 diabetes mellitus and is planning to become pregnant. To reduce the risk of congenital neural tube defects in her offspring, the physician prescribes oral folic acid supplementation. Folic acid promotes neural tube closure primarily by serving as a cofactor for which of the following biochemical processes?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Lipid peroxidation inhibition"},
            {"letter": "B", "is_correct": True, "text": "One-carbon metabolism for purine and thymidylate synthesis"},
            {"letter": "C", "is_correct": False, "text": "Collagen proline hydroxylation"},
            {"letter": "D", "is_correct": False, "text": "Glycogen synthesis and branching"},
            {"letter": "E", "is_correct": False, "text": "Oxidative phosphorylation in the mitochondrial matrix"}
        ],
        "explanation": "Correct Answer: B. One-carbon metabolism for purine and thymidylate synthesis.\n\nFolate (vitamin B9) is converted to tetrahydrofolate (THF), which serves as a one-carbon carrier essential for the synthesis of purines and thymidylate (dTMP) via thymidylate synthase. Rapidly dividing neuroepithelial cells during the 3rd and 4th weeks of gestation require high rates of DNA synthesis for neural fold elevation and fusion. Folate deficiency disrupts this rapid cell proliferation, leading to failure of neuropore closure."
    },
    {
        "q_num": "DEV-09",
        "category": "Central Nervous System Development",
        "stem": "A 32-year-old woman presents with progressive bilateral loss of pain and temperature sensation across her shoulders and upper arms ('cape-like' distribution). Light touch, proprioception, and vibration sensation are completely preserved. A spinal MRI reveals an expanding cystic cavity located within the central cervical spinal cord (C5-T1). What embryological failure or anomaly is most frequently associated with the development of this condition?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Failure of the rostral neuropore to close"},
            {"letter": "B", "is_correct": True, "text": "Chiari I malformation with cerebellar tonsillar ectopia"},
            {"letter": "C", "is_correct": False, "text": "Agenesis of the corpus callosum"},
            {"letter": "D", "is_correct": False, "text": "Failure of radial glia migration in the neocortex"},
            {"letter": "E", "is_correct": False, "text": "Failure of ventral horn motor neuron apoptosis"}
        ],
        "explanation": "Correct Answer: B. Chiari I malformation with cerebellar tonsillar ectopia.\n\nThis patient has syringomyelia, a fluid-filled cavity (syrinx) within the central canal of the spinal cord (most commonly cervical). It selectively damages the anterior white commissure crossing fibers of the spinothalamic tract, producing bilateral loss of pain and temperature sensation in a 'cape-like' distribution over the shoulders and arms. More than 50% of syringomyelia cases are associated with Chiari I malformation, in which cerebellar tonsillar ectopia (>5 mm below the foramen magnum) obstructs normal CSF flow at the craniocervical junction."
    },
    {
        "q_num": "DEV-10",
        "category": "Central Nervous System Development",
        "stem": "An infant is diagnosed with lissencephaly (agyria). MRI of the brain reveals an abnormally smooth cerebral cortical surface, markedly reduced sulcation, and a thickened four-layered cortex (rather than the normal six layers). The pathogenesis of this congenital malformation involves a disruption in which of the following neurodevelopmental processes?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Neuroepithelial cell induction by the notochord"},
            {"letter": "B", "is_correct": True, "text": "Radial migration of neuroblasts along radial glia"},
            {"letter": "C", "is_correct": False, "text": "Axonal pruning during synaptic refinement"},
            {"letter": "D", "is_correct": False, "text": "Oligodendrocyte precursor myelination"},
            {"letter": "E", "is_correct": False, "text": "Spinal cord ventral horn motor neuron differentiation"}
        ],
        "explanation": "Correct Answer: B. Radial migration of neuroblasts along radial glia.\n\nLissencephaly ('smooth brain') is a severe malformation of cortical development caused by defective neuronal migration during weeks 12-24 of gestation. Developing neuroblasts normally migrate from the periventricular germinal matrix outwards toward the pial surface along scaffolds provided by radial glial cells. Mutations in genes regulating the microtubule cytoskeleton (such as LIS1 and DCX/doublecortin) disrupt radial migration, resulting in a smooth cortex with few or no sulci and a thickened, disorganized 4-layered cortex."
    },
    {
        "q_num": "DEV-11",
        "category": "Central Nervous System Development",
        "stem": "During spinal cord development, the mantle layer of the neural tube is divided into dorsal and ventral regions by a longitudinal groove on the inner surface called the sulcus limitans. Which of the following functional cell groups develops from the alar plate located dorsal to the sulcus limitans?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Alpha motor neurons of the ventral horn"},
            {"letter": "B", "is_correct": True, "text": "Sensory neurons and interneurons of the dorsal horn"},
            {"letter": "C", "is_correct": False, "text": "Preganglionic sympathetic neurons of the intermediolateral cell column"},
            {"letter": "D", "is_correct": False, "text": "Parasympathetic preganglionic neurons in the sacral cord"},
            {"letter": "E", "is_correct": False, "text": "Dorsal root ganglion pseudounipolar neurons"}
        ],
        "explanation": "Correct Answer: B. Sensory neurons and interneurons of the dorsal horn.\n\nThe sulcus limitans separates the mantle zone into:\n• Alar plate (dorsal): Regulated by bone morphogenetic proteins (BMPs) and Wnt; gives rise to sensory relay neurons and interneurons of the dorsal horn.\n• Basal plate (ventral): Regulated by Sonic hedgehog (SHH) from the notochord and floor plate; gives rise to somatic motor neurons (ventral horn) and visceral autonomic motor neurons (intermediolateral horn).\n\n• Option E is incorrect: Dorsal root ganglion neurons arise from the neural crest, not the alar plate."
    },
    {
        "q_num": "DEV-12",
        "category": "Central Nervous System Development",
        "stem": "A full-term male infant is born with a caudal midline mass. Neurological examination reveals lower extremity clubfoot, flaccid paraplegia, and absent sphincter tone. Spinal ultrasound reveals myelomeningocele. At what gestational age does the caudal neuropore normally complete its closure during human embryogenesis?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Day 14"},
            {"letter": "B", "is_correct": False, "text": "Day 21"},
            {"letter": "C", "is_correct": False, "text": "Day 25"},
            {"letter": "D", "is_correct": True, "text": "Day 27–28"},
            {"letter": "E", "is_correct": False, "text": "Day 42"}
        ],
        "explanation": "Correct Answer: D. Day 27–28.\n\nNeurulation timing:\n• Neural folds begin to fuse along the midline around Day 20–21.\n• Rostral (cranial/anterior) neuropore closes on approximately Day 25 (failure results in anencephaly/encephalocele).\n• Caudal (posterior) neuropore closes approximately 2 days later, on Day 27–28 (week 4) (failure results in spina bifida / myelomeningocele)."
    },
    {
        "q_num": "DEV-13",
        "category": "Central Nervous System Development",
        "stem": "A 16-year-old boy presents with progressive clumsiness and hand weakness. MRI of the brain reveals the cerebellar tonsils extending 8 mm below the level of the foramen magnum into the upper cervical canal. No hydrocephalus or myelomeningocele is present, but a small syrinx is noted at C6-T1. Which of the following is the most appropriate diagnosis?",
        "options": [
            {"letter": "A", "is_correct": True, "text": "Chiari I malformation"},
            {"letter": "B", "is_correct": False, "text": "Chiari II malformation"},
            {"letter": "C", "is_correct": False, "text": "Dandy-Walker variant"},
            {"letter": "D", "is_correct": False, "text": "Klippel-Feil syndrome"},
            {"letter": "E", "is_correct": False, "text": "Tethered cord syndrome"}
        ],
        "explanation": "Correct Answer: A. Chiari I malformation.\n\nChiari I malformation is defined by herniation of the cerebellar tonsils alone (>5 mm) through the foramen magnum into the cervical canal. It is often asymptomatic in childhood and presents in adolescence or adulthood with suboccipital headaches (worsened by Valsalva, coughing, or bending forward), ataxia, and symptoms of an associated cervical syrinx (syringomyelia). It is NOT associated with myelomeningocele (which defines Chiari II)."
    },
    {
        "q_num": "DEV-14",
        "category": "Central Nervous System Development",
        "stem": "An autopsy performed on a stillborn infant with cyclopia and a proboscis reveals complete failure of forebrain separation. Genetic analysis reveals trisomy 13 (Patau syndrome). The embryological structure whose failure to cleave resulted in this pathology normally gives rise to which two secondary brain vesicles?",
        "options": [
            {"letter": "A", "is_correct": True, "text": "Telencephalon and Diencephalon"},
            {"letter": "B", "is_correct": False, "text": "Metencephalon and Myelencephalon"},
            {"letter": "C", "is_correct": False, "text": "Mesencephalon and Metencephalon"},
            {"letter": "D", "is_correct": False, "text": "Prosencephalon and Rhombencephalon"},
            {"letter": "E", "is_correct": False, "text": "Diencephalon and Mesencephalon"}
        ],
        "explanation": "Correct Answer: A. Telencephalon and Diencephalon.\n\nHoloprosencephaly is the failure of the primary forebrain vesicle (the prosencephalon) to divide into its two secondary vesicles—the telencephalon (cerebral hemispheres) and diencephalon (thalamus/hypothalamus). Normally, this division occurs during the 5th and 6th weeks of embryogenesis."
    },
    {
        "q_num": "DEV-15",
        "category": "Central Nervous System Development",
        "stem": "A 4-year-old child presents with intellectual disability and severe refractory seizures. Cranial MRI reveals periventricular nodular heterotopia (abnormal clumps of neurons lining the lateral ventricular walls). This condition represents an arrest in which stage of neurodevelopment?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Primary neurulation"},
            {"letter": "B", "is_correct": True, "text": "Neuronal migration"},
            {"letter": "C", "is_correct": False, "text": "Synaptic pruning"},
            {"letter": "D", "is_correct": False, "text": "Myelination"},
            {"letter": "E", "is_correct": False, "text": "Vesicle formation"}
        ],
        "explanation": "Correct Answer: B. Neuronal migration.\n\nPeriventricular nodular heterotopia (often caused by mutations in the filamin A / FLNA gene) is a disorder of neuronal migration. Neuroblasts generated in the periventricular germinal zone fail to initiate or complete their migration along radial glial fibers to the cortical plate, remaining trapped as ectopic nodules of gray matter along the ventricular walls, which frequently act as epileptogenic foci."
    },
    {
        "q_num": "DEV-16",
        "category": "Central Nervous System Development",
        "stem": "During early spinal cord development, the adult spinal cord terminates at approximately the L1-L2 vertebral level in adults, whereas at early fetal development (month 3), the spinal cord extends the entire length of the vertebral canal. What embryological mechanism accounts for this apparent 'ascent' of the spinal cord?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Progressive apoptosis of coccygeal spinal cord segments"},
            {"letter": "B", "is_correct": True, "text": "Differential elongation of the vertebral column compared to the spinal cord"},
            {"letter": "C", "is_correct": False, "text": "Rostral migration of the conus medullaris into the cervical spine"},
            {"letter": "D", "is_correct": False, "text": "Shortening of the spinal nerve roots"},
            {"letter": "E", "is_correct": False, "text": "Infolding of the caudal neuropore"}
        ],
        "explanation": "Correct Answer: B. Differential elongation of the vertebral column compared to the spinal cord.\n\nIn early fetal life, the spinal cord and vertebral column are of equal length, and spinal nerves exit horizontally through their corresponding intervertebral foramina. During later fetal and postnatal development, the vertebral column and dura mater grow significantly faster than the spinal cord. Consequently, the caudal end of the spinal cord (conus medullaris) shifts relatively rostrally: terminating at S1 at birth and at L1-L2 in adults. This differential growth also creates the cauda equina and lumbar cistern."
    },
    {
        "q_num": "DEV-17",
        "category": "Central Nervous System Development",
        "stem": "A female newborn is born with microcephaly, bilateral sensorineural hearing loss, chorioretinitis, patent ductus arteriosus, and cataracts. Maternal serology during pregnancy was positive for a togavirus. Which of the following viral agents is responsible for this constellation of congenital CNS and systemic anomalies?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Cytomegalovirus"},
            {"letter": "B", "is_correct": False, "text": "Toxoplasma gondii"},
            {"letter": "C", "is_correct": True, "text": "Rubella virus"},
            {"letter": "D", "is_correct": False, "text": "Zika virus"},
            {"letter": "E", "is_correct": False, "text": "Herpes simplex virus-2"}
        ],
        "explanation": "Correct Answer: C. Rubella virus.\n\nCongenital rubella syndrome (caused by Rubella virus, an enveloped, positive-sense single-stranded RNA togavirus) produces the classic triad of:\n1. Sensorineural deafness\n2. Cataracts (and retinopathy)\n3. Cardiac anomalies (patent ductus arteriosus, pulmonary artery stenosis)\nMicrocephaly, intellectual disability, and 'blueberry muffin' purpuric skin lesions are also characteristic.\n\n• Option A is incorrect: CMV (herpesvirus, dsDNA) causes periventricular calcifications, chorioretinitis, and sensorineural hearing loss.\n• Option B is incorrect: Toxoplasma causes diffuse intracerebral calcifications, chorioretinitis, and hydrocephalus."
    },
    {
        "q_num": "DEV-18",
        "category": "Central Nervous System Development",
        "stem": "The cerebral aqueduct of Sylvius connects the third ventricle to the fourth ventricle. From which embryonic brain vesicle does the cerebral aqueduct originate?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Telencephalon"},
            {"letter": "B", "is_correct": False, "text": "Diencephalon"},
            {"letter": "C", "is_correct": True, "text": "Mesencephalon"},
            {"letter": "D", "is_correct": False, "text": "Metencephalon"},
            {"letter": "E", "is_correct": False, "text": "Myelencephalon"}
        ],
        "explanation": "Correct Answer: C. Mesencephalon.\n\nThe mesencephalon (midbrain) remains undivided as a single primary vesicle. Its internal cavity narrows considerably during fetal development to form the slender cerebral aqueduct (aqueduct of Sylvius), which connects the third ventricle (diencephalon) with the fourth ventricle (rhombencephalon)."
    },
    {
        "q_num": "DEV-19",
        "category": "Central Nervous System Development",
        "stem": "A 2-day-old infant is found to have low-set ears, micrognathia, a small cleft palate, and a truncus arteriosus on echocardiogram. Fluorescent in situ hybridization (FISH) confirms a microdeletion on chromosome 22q11.2 (DiGeorge syndrome). Defective migration of which embryonic cell population is responsible for this condition?",
        "options": [
            {"letter": "A", "is_correct": True, "text": "Neural crest cells into the 3rd and 4th pharyngeal pouches"},
            {"letter": "B", "is_correct": False, "text": "Endodermal cells into the thyroid diverticulum"},
            {"letter": "C", "is_correct": False, "text": "Lateral plate mesoderm into the pericardial cavity"},
            {"letter": "D", "is_correct": False, "text": "Ectodermal placodes into the otic vesicle"},
            {"letter": "E", "is_correct": False, "text": "Neuroepithelial cells into the alar plate"}
        ],
        "explanation": "Correct Answer: A. Neural crest cells into the 3rd and 4th pharyngeal pouches.\n\nDiGeorge syndrome (22q11.2 deletion syndrome) results from defective migration of cranial neural crest cells into the 3rd and 4th pharyngeal pouches. This causes:\n• Agenesis/hypoplasia of parathyroid glands (hypocalcemia, tetany)\n• Thymic aplasia (T-cell immunodeficiency)\n• Conotruncal cardiac defects (tetralogy of Fallot, truncus arteriosus, interrupted aortic arch)\n• Craniofacial dysmorphisms (cleft palate, low-set ears)."
    },
    {
        "q_num": "DEV-20",
        "category": "Central Nervous System Development",
        "stem": "An infant girl born with a lumbar myelomeningocele undergoes surgical repair. Postoperatively, she is at high risk for developing non-communicating hydrocephalus. Aqueductal stenosis in patients with Chiari II malformation is primarily due to which mechanical process?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Fibrous obliteration of arachnoid granulations"},
            {"letter": "B", "is_correct": True, "text": "Downward traction and crowding of the brainstem in the narrow posterior fossa"},
            {"letter": "C", "is_correct": False, "text": "Hypersecretion of CSF by the choroid plexus"},
            {"letter": "D", "is_correct": False, "text": "Agenesis of the foramen of Magendie"},
            {"letter": "E", "is_correct": False, "text": "Thrombosis of the superior sagittal sinus"}
        ],
        "explanation": "Correct Answer: B. Downward traction and crowding of the brainstem in the narrow posterior fossa.\n\nIn Chiari II malformation, tethering and downward displacement of the brainstem through an abnormally small, crowded posterior fossa causes compression, elongation, and kinking of the brainstem (medulla and midbrain), which compresses and occludes the narrow cerebral aqueduct of Sylvius, resulting in obstructive (non-communicating) hydrocephalus."
    },

    # =========================================================================
    # 3. NEUROTRANSMITTERS AND ACTION POTENTIALS (20 Questions: Q41 - Q60)
    # =========================================================================
    {
        "q_num": "NT-01",
        "category": "Neurotransmitters and Action Potentials",
        "stem": "A neurophysiologist measures the electrical properties of an isolated mammalian axon. The resting membrane potential is recorded at -70 mV. Which of the following ion channels is primarily responsible for establishing and maintaining this resting membrane potential close to the potassium equilibrium potential?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Voltage-gated sodium channels"},
            {"letter": "B", "is_correct": True, "text": "Non-gated (leak) potassium channels"},
            {"letter": "C", "is_correct": False, "text": "Voltage-gated calcium channels"},
            {"letter": "D", "is_correct": False, "text": "Ligand-gated chloride channels"},
            {"letter": "E", "is_correct": False, "text": "Mechanically-gated cation channels"}
        ],
        "explanation": "Correct Answer: B. Non-gated (leak) potassium channels.\n\nThe resting membrane potential (typically -70 mV in neurons) is primarily determined by high resting permeability to K+ ions via constitutively open, non-gated K+ leak channels (such as K2P two-pore domain channels). Because the resting membrane is approximately 25-100 times more permeable to K+ than to Na+, the membrane potential settles close to the equilibrium potential for K+ (EK ≈ -90 mV), as described by the Goldman-Hodgkin-Katz equation. The Na+/K+ ATPase electrogenically pumps 3 Na+ out for every 2 K+ in, maintaining the concentration gradients."
    },
    {
        "q_num": "NT-02",
        "category": "Neurotransmitters and Action Potentials",
        "stem": "During an action potential in a peripheral motor axon, the rapid upstroke (depolarization phase) shifts the membrane potential from threshold (-55 mV) toward +35 mV. This rapid depolarization is primarily driven by which of the following events?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Efflux of potassium ions through delayed rectifier channels"},
            {"letter": "B", "is_correct": True, "text": "Influx of sodium ions through voltage-gated sodium channels"},
            {"letter": "C", "is_correct": False, "text": "Influx of calcium ions through L-type calcium channels"},
            {"letter": "D", "is_correct": False, "text": "Efflux of chloride ions through GABA-A receptors"},
            {"letter": "E", "is_correct": False, "text": "Active extrusion of sodium ions by Na+/K+ ATPase"}
        ],
        "explanation": "Correct Answer: B. Influx of sodium ions through voltage-gated sodium channels.\n\nWhen a depolarizing stimulus reaches threshold (typically around -55 mV), activation (m) gates of voltage-gated Na+ channels rapidly open. This causes a massive influx of Na+ down both its concentration and electrical gradients, driving the membrane potential toward the sodium equilibrium potential (ENa ≈ +60 mV)."
    },
    {
        "q_num": "NT-03",
        "category": "Neurotransmitters and Action Potentials",
        "stem": "A 34-year-old chef at a Japanese restaurant develops perioral paresthesias, nausea, vomiting, and progressive muscle paralysis with diaphragmatic weakness within 30 minutes of tasting poorly prepared fugu (pufferfish). The toxin responsible for his condition (tetrodotoxin) impairs action potential propagation by which mechanism?",
        "options": [
            {"letter": "A", "is_correct": True, "text": "Binding to and blocking voltage-gated sodium channels"},
            {"letter": "B", "is_correct": False, "text": "Preventing inactivation of voltage-gated sodium channels"},
            {"letter": "C", "is_correct": False, "text": "Irreversibly blocking voltage-gated potassium channels"},
            {"letter": "D", "is_correct": False, "text": "Inhibiting acetylcholinesterase at the neuromuscular junction"},
            {"letter": "E", "is_correct": False, "text": "Cleaving synaptobrevin to block acetylcholine exocytosis"}
        ],
        "explanation": "Correct Answer: A. Binding to and blocking voltage-gated sodium channels.\n\nTetrodotoxin (found in pufferfish/fugu) and saxitoxin (found in 'red tide' dinoflagellates) bind with high affinity to site 1 on the extracellular pore of voltage-gated Na+ channels in nerves and cardiac/skeletal muscle. This completely prevents Na+ influx, halting action potential generation and conduction. Symptoms include perioral tingling, loss of reflexes, ascending flaccid paralysis, and death from respiratory failure, while consciousness remains intact."
    },
    {
        "q_num": "NT-04",
        "category": "Neurotransmitters and Action Potentials",
        "stem": "A neurophysiologist investigates the absolute refractory period in a squid giant axon. During this phase, it is impossible to elicit a second action potential, regardless of the stimulus intensity. What state of the voltage-gated sodium channels accounts for the absolute refractory period?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Activation gates are closed, and inactivation gates are open"},
            {"letter": "B", "is_correct": False, "text": "Both activation and inactivation gates are fully open"},
            {"letter": "C", "is_correct": True, "text": "Inactivation gates are closed"},
            {"letter": "D", "is_correct": False, "text": "Sodium channels have been internalized by endocytosis"},
            {"letter": "E", "is_correct": False, "text": "Channels are phosphorylated by protein kinase A"}
        ],
        "explanation": "Correct Answer: C. Inactivation gates are closed.\n\nVoltage-gated Na+ channels have two gates:\n1. Activation (m) gate: Opens rapidly upon depolarization.\n2. Inactivation (h) gate: Closes slowly after depolarization.\nDuring the peak and repolarization phase of the action potential, the inactivation gates are closed ('inactivated state'). Until the membrane repolarizes sufficiently to allow these inactivation gates to reopen ('de-inactivation'), no stimulus can open the channel to generate another action potential. This period of inexcitable Na+ channels defines the absolute refractory period."
    },
    {
        "q_num": "NT-05",
        "category": "Neurotransmitters and Action Potentials",
        "stem": "In the central nervous system, glutamate is the primary excitatory neurotransmitter, while GABA is the primary inhibitory neurotransmitter. Which enzyme catalyzes the decarboxylation of glutamate to form GABA, and which vitamin serves as its essential cofactor?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Choline acetyltransferase; Vitamin B1 (thiamine)"},
            {"letter": "B", "is_correct": True, "text": "Glutamic acid decarboxylase (GAD); Vitamin B6 (pyridoxine)"},
            {"letter": "C", "is_correct": False, "text": "Tyrosine hydroxylase; Vitamin B12 (cobalamin)"},
            {"letter": "D", "is_correct": False, "text": "Tryptophan hydroxylase; Vitamin B3 (niacin)"},
            {"letter": "E", "is_correct": False, "text": "DOPA decarboxylase; Vitamin C (ascorbate)"}
        ],
        "explanation": "Correct Answer: B. Glutamic acid decarboxylase (GAD); Vitamin B6 (pyridoxine).\n\nGABA (gamma-aminobutyric acid) is synthesized from glutamate via the enzyme glutamic acid decarboxylase (GAD). GAD strictly requires pyridoxal phosphate (PLP, active vitamin B6) as a cofactor. Vitamin B6 deficiency (e.g., from isoniazid therapy for tuberculosis) leads to decreased GABA synthesis, causing neuronal hyperexcitability and refractory seizures. Antibodies against GAD are found in Type 1 diabetes and Stiff-Person syndrome."
    },
    {
        "q_num": "NT-06",
        "category": "Neurotransmitters and Action Potentials",
        "stem": "A 42-year-old woman is admitted for acute anxiety and panic disorder. She is prescribed lorazepam. Benzodiazepines produce their therapeutic sedative and anxiolytic effects by binding to which receptor and causing which ionic change?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "GABA-B receptor; increased potassium efflux"},
            {"letter": "B", "is_correct": True, "text": "GABA-A receptor; increased frequency of chloride channel opening"},
            {"letter": "C", "is_correct": False, "text": "GABA-A receptor; increased duration of chloride channel opening"},
            {"letter": "D", "is_correct": False, "text": "NMDA receptor; decreased calcium influx"},
            {"letter": "E", "is_correct": False, "text": "5-HT1A receptor; decreased adenylyl cyclase activity"}
        ],
        "explanation": "Correct Answer: B. GABA-A receptor; increased frequency of chloride channel opening.\n\n• Benzodiazepines bind allosterically to the GABA-A receptor (an ionotropic ligand-gated chloride channel) and increase the FREQUENCY of chloride channel opening in the presence of GABA.\n• In contrast, Barbiturates increase the DURATION of chloride channel opening (Option C) and at high doses can directly gate the channel even in the absence of GABA, explaining their higher risk of lethal respiratory depression."
    },
    {
        "q_num": "NT-07",
        "category": "Neurotransmitters and Action Potentials",
        "stem": "A 22-year-old man taking an antidepressant medication for major depressive disorder attends a party where he consumes aged cheese and red wine. Two hours later, he presents to the emergency room with severe throbbing headache, diaphoresis, palpitations, and a blood pressure of 210/120 mm Hg. This hypertensive crisis occurs due to displacement and release of which neurotransmitter?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Acetylcholine"},
            {"letter": "B", "is_correct": False, "text": "Serotonin"},
            {"letter": "C", "is_correct": True, "text": "Norepinephrine"},
            {"letter": "D", "is_correct": False, "text": "GABA"},
            {"letter": "E", "is_correct": False, "text": "Glycine"}
        ],
        "explanation": "Correct Answer: C. Norepinephrine.\n\nThis patient is taking a monoamine oxidase inhibitor (MAOI, e.g., phenelzine, tranylcypromine, selegiline) and experienced the 'cheese reaction.' Dietary tyramine (abundant in aged cheeses, cured meats, and draft beer) is normally degraded by intestinal and hepatic MAO-A. When MAO-A is inhibited, tyramine enters the systemic circulation and is taken up into sympathetic nerve terminals via the norepinephrine transporter (NET). Tyramine displaces stored norepinephrine from synaptic vesicles into the synaptic cleft, causing massive alpha-1 and beta-1 receptor activation, severe vasoconstriction, and hypertensive crisis."
    },
    {
        "q_num": "NT-08",
        "category": "Neurotransmitters and Action Potentials",
        "stem": "In the biosynthesis of catecholamines, the rate-limiting step in the conversion of L-tyrosine to epinephrine is catalyzed by which enzyme?",
        "options": [
            {"letter": "A", "is_correct": True, "text": "Tyrosine hydroxylase"},
            {"letter": "B", "is_correct": False, "text": "DOPA decarboxylase"},
            {"letter": "C", "is_correct": False, "text": "Dopamine beta-hydroxylase"},
            {"letter": "D", "is_correct": False, "text": "Phenylethanolamine N-methyltransferase (PNMT)"},
            {"letter": "E", "is_correct": False, "text": "Catechol-O-methyltransferase (COMT)"}
        ],
        "explanation": "Correct Answer: A. Tyrosine hydroxylase.\n\nCatecholamine synthesis pathway:\n1. Tyrosine → L-DOPA via Tyrosine hydroxylase (rate-limiting step, requires tetrahydrobiopterin / BH4).\n2. L-DOPA → Dopamine via DOPA decarboxylase (requires vitamin B6).\n3. Dopamine → Norepinephrine via Dopamine beta-hydroxylase (requires vitamin C and copper).\n4. Norepinephrine → Epinephrine via PNMT (requires SAM; stimulated by cortisol from adrenal cortex)."
    },
    {
        "q_num": "NT-09",
        "category": "Neurotransmitters and Action Potentials",
        "stem": "Which of the following neurotransmitter receptors is an ionotropic receptor that conducts both sodium and calcium ions upon activation, is blocked by extracellular magnesium ions at resting membrane potentials, and plays a central role in long-term potentiation (LTP) and synaptic plasticity?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "AMPA receptor"},
            {"letter": "B", "is_correct": False, "text": "Kainate receptor"},
            {"letter": "C", "is_correct": True, "text": "NMDA receptor"},
            {"letter": "D", "is_correct": False, "text": "Metabotropic glutamate receptor 1 (mGluR1)"},
            {"letter": "E", "is_correct": False, "text": "GABA-B receptor"}
        ],
        "explanation": "Correct Answer: C. NMDA receptor.\n\nThe NMDA (N-methyl-D-aspartate) receptor is an ionotropic glutamate receptor with unique properties:\n• At resting membrane potentials (-70 mV), its pore is physically blocked by an extracellular Mg2+ ion.\n• When the postsynaptic membrane is depolarized (typically via adjacent AMPA receptor activation), the Mg2+ plug is expelled.\n• Once glutamate and its co-agonist glycine bind to the unblocked receptor, it allows a high influx of Ca2+ (and Na+).\n• This Ca2+ influx activates calcium/calmodulin-dependent protein kinase II (CaMKII), triggering the insertion of additional AMPA receptors into the postsynaptic membrane, which underlies long-term potentiation (LTP) and memory formation."
    },
    {
        "q_num": "NT-10",
        "category": "Neurotransmitters and Action Potentials",
        "stem": "A 19-year-old college student presents with high fever, agitation, tremor, hyperreflexia, bilateral ankle clonus, and diarrhea. She recently started taking sertraline (an SSRI) for depression and took tramadol earlier today for a sprained ankle. Serotonin (5-hydroxytryptamine) is synthesized in which brainstem nuclei, and from which precursor amino acid?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Locus coeruleus; Tyrosine"},
            {"letter": "B", "is_correct": False, "text": "Substantia nigra; Phenylalanine"},
            {"letter": "C", "is_correct": True, "text": "Raphe nuclei; Tryptophan"},
            {"letter": "D", "is_correct": False, "text": "Nucleus basalis of Meynert; Choline"},
            {"letter": "E", "is_correct": False, "text": "Tuberomammillary nucleus; Histidine"}
        ],
        "explanation": "Correct Answer: C. Raphe nuclei; Tryptophan.\n\nSerotonin is synthesized primarily in the dorsal and median raphe nuclei of the brainstem (midbrain, pons, and medulla). The biosynthetic pathway starts with the essential amino acid tryptophan:\n1. Tryptophan → 5-hydroxytryptophan (via Tryptophan hydroxylase, requiring BH4).\n2. 5-hydroxytryptophan → 5-HT / Serotonin (via Aromatic L-amino acid decarboxylase / DOPA decarboxylase, requiring vitamin B6).\nCombining an SSRI with tramadol (which inhibits serotonin reuptake) can precipitate life-threatening Serotonin Syndrome (autonomic instability, neuromuscular hyperactivity/clonus, altered mental status)."
    },
    {
        "q_num": "NT-11",
        "category": "Neurotransmitters and Action Potentials",
        "stem": "Which of the following local anesthetics is classified as an amino ester, provides intrinsic vasoconstriction by blocking the reuptake of norepinephrine at sympathetic nerve endings, and is commonly used for topical anesthesia during nasal surgery?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Lidocaine"},
            {"letter": "B", "is_correct": False, "text": "Bupivacaine"},
            {"letter": "C", "is_correct": True, "text": "Cocaine"},
            {"letter": "D", "is_correct": False, "text": "Ropivacaine"},
            {"letter": "E", "is_correct": False, "text": "Procaine"}
        ],
        "explanation": "Correct Answer: C. Cocaine.\n\nLocal anesthetics block voltage-gated Na+ channels from the intracellular side of the membrane. They are classified into:\n• Esters: Cocaine, procaine, tetracaine, benzocaine (metabolized by plasma pseudocholinesterase).\n• Amides: Lidocaine, bupivacaine, mepivacaine, ropivacaine (contain two 'i's in their spelling; metabolized by hepatic CYP enzymes).\nCocaine is unique among local anesthetics because it also inhibits the presynaptic norepinephrine reuptake transporter (NET), causing local vasoconstriction that minimizes mucosal bleeding during ENT procedures."
    },
    {
        "q_num": "NT-12",
        "category": "Neurotransmitters and Action Potentials",
        "stem": "In myelinated axons, action potentials conduct significantly faster than in unmyelinated axons of identical diameter. This rapid conduction occurs through saltatory conduction. How does myelin alter the membrane's physical properties to accelerate conduction velocity?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Increases membrane capacitance and increases membrane resistance"},
            {"letter": "B", "is_correct": True, "text": "Decreases membrane capacitance and increases membrane resistance"},
            {"letter": "C", "is_correct": False, "text": "Increases membrane capacitance and decreases membrane resistance"},
            {"letter": "D", "is_correct": False, "text": "Decreases internal axial resistance along the axoplasm"},
            {"letter": "E", "is_correct": False, "text": "Increases the density of sodium channels along the internodes"}
        ],
        "explanation": "Correct Answer: B. Decreases membrane capacitance and increases membrane resistance.\n\nMyelin, formed by multiple concentric layers of oligodendrocyte (CNS) or Schwann cell (PNS) plasma membranes, acts as an electrical insulator:\n• Increases membrane resistance (Rm): Prevents current from leaking out across the internodal axolemma, dramatically increasing the length (space) constant (λ).\n• Decreases membrane capacitance (Cm): By increasing the thickness of the dielectric layer separating intra- and extracellular charges, less charge is stored on the membrane, dramatically decreasing the time constant (τ).\nThese changes allow electrotonic current to spread rapidly between the nodes of Ranvier, where voltage-gated Na+ channels are densely clustered (saltatory conduction)."
    },
    {
        "q_num": "NT-13",
        "category": "Neurotransmitters and Action Potentials",
        "stem": "A 5-year-old child ingest a garden plant containing strychnine, a lethal poison. Strychnine causes severe generalized muscle spasms, opisthotonos, and convulsions without loss of consciousness. Strychnine produces these symptoms by competitively antagonizing which inhibitory neurotransmitter receptor?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "GABA-A receptor"},
            {"letter": "B", "is_correct": False, "text": "GABA-B receptor"},
            {"letter": "C", "is_correct": True, "text": "Glycine receptor"},
            {"letter": "D", "is_correct": False, "text": "Nicotinic acetylcholine receptor"},
            {"letter": "E", "is_correct": False, "text": "Muscarinic M2 receptor"}
        ],
        "explanation": "Correct Answer: C. Glycine receptor.\n\nGlycine is the predominant inhibitory neurotransmitter in the spinal cord and brainstem (especially at Renshaw interneurons). It binds to ionotropic glycine receptors, opening chloride channels to cause postsynaptic hyperpolarization. Strychnine is a potent, selective competitive antagonist of the glycine receptor. By blocking glycine-mediated recurrent inhibition, motor neurons fire uncontrollably in response to minimal sensory stimuli, resulting in painful tetanic convulsions and asphyxiation."
    },
    {
        "q_num": "NT-14",
        "category": "Neurotransmitters and Action Potentials",
        "stem": "A 45-year-old man presents with progressive chorea, depression, and executive cognitive decline. Genetic testing reveals an expanded CAG trinucleotide repeat on chromosome 4. Neuropathology demonstrates marked atrophy of the caudate and putamen. In the early stages of Huntington disease, there is selective loss of striatal projection neurons utilizing which neurotransmitter?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Dopamine"},
            {"letter": "B", "is_correct": True, "text": "GABA"},
            {"letter": "C", "is_correct": False, "text": "Norepinephrine"},
            {"letter": "D", "is_correct": False, "text": "Serotonin"},
            {"letter": "E", "is_correct": False, "text": "Histamine"}
        ],
        "explanation": "Correct Answer: B. GABA.\n\nHuntington disease is an autosomal dominant neurodegenerative disorder characterized by loss of medium spiny neurons in the striatum (caudate nucleus > putamen). These neurons synthesize and release the inhibitory neurotransmitter GABA (and substance P/enkephalin). Loss of GABAergic striatal neurons projecting to the external globus pallidus (indirect pathway) leads to disinhibition of the thalamus and the classic hyperkinetic choreiform movements."
    },
    {
        "q_num": "NT-15",
        "category": "Neurotransmitters and Action Potentials",
        "stem": "A 26-year-old woman is stung by a black widow spider (Latrodectus mactans). Within an hour, she experiences severe generalized muscle cramps, abdominal rigidity, diaphoresis, and hypertension. The toxin alpha-latrotoxin produces these symptoms by which molecular mechanism at the presynaptic terminal?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Blocks voltage-gated calcium channels to prevent vesicle fusion"},
            {"letter": "B", "is_correct": True, "text": "Forms calcium-permeable membrane pores causing massive, uncontrolled acetylcholine release"},
            {"letter": "C", "is_correct": False, "text": "Irreversibly inhibits acetylcholinesterase"},
            {"letter": "D", "is_correct": False, "text": "Competitively blocks post-synaptic nicotinic receptors"},
            {"letter": "E", "is_correct": False, "text": "Cleaves SNAP-25 preventing SNARE complex assembly"}
        ],
        "explanation": "Correct Answer: B. Forms calcium-permeable membrane pores causing massive, uncontrolled acetylcholine release.\n\nAlpha-latrotoxin (from the black widow spider) binds to presynaptic receptors (latrophilin and neurexin) and inserts into the presynaptic membrane, forming non-specific cation pores. The resulting massive influx of Ca2+ triggers explosive, uncontrolled exocytosis of acetylcholine (and other neurotransmitters) at neuromuscular junctions and autonomic synapses, causing intense muscle contractions, abdominal wall rigidity, and autonomic overactivity."
    },
    {
        "q_num": "NT-16",
        "category": "Neurotransmitters and Action Potentials",
        "stem": "Action potentials in unmyelinated C-fibers conduct at approximately 0.5 to 2.0 m/s, whereas in myelinated A-alpha motor fibers, conduction reaches 80 to 120 m/s. According to cable theory, increasing which of the following parameters will increase the space (length) constant of a nerve fiber?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Increasing internal axoplasmic resistance (Ri)"},
            {"letter": "B", "is_correct": True, "text": "Increasing membrane resistance (Rm)"},
            {"letter": "C", "is_correct": False, "text": "Increasing membrane capacitance (Cm)"},
            {"letter": "D", "is_correct": False, "text": "Decreasing axon diameter"},
            {"letter": "E", "is_correct": False, "text": "Increasing extracellular fluid resistance"}
        ],
        "explanation": "Correct Answer: B. Increasing membrane resistance (Rm).\n\nThe space constant (length constant, λ) is mathematically defined as:\nλ = √(Rm / Ri)\nwhere Rm is membrane resistance and Ri is internal axial (axoplasmic) resistance. A larger λ means voltage changes decay less over distance, allowing current to spread further along the axon to trigger downstream action potentials.\n• Increasing Rm (via myelination) increases λ.\n• Increasing axon diameter decreases Ri, which also increases λ."
    },
    {
        "q_num": "NT-17",
        "category": "Neurotransmitters and Action Potentials",
        "stem": "Which of the following neurotransmitters is a retrograde gaseous neuromodulator that is synthesized on demand from L-arginine, diffuses across cell membranes without vesicular packaging, and activates soluble guanylyl cyclase in target cells to increase cyclic GMP levels?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Carbon monoxide"},
            {"letter": "B", "is_correct": True, "text": "Nitric oxide (NO)"},
            {"letter": "C", "is_correct": False, "text": "Hydrogen sulfide"},
            {"letter": "D", "is_correct": False, "text": "Endothelin-1"},
            {"letter": "E", "is_correct": False, "text": "Anandamide"}
        ],
        "explanation": "Correct Answer: B. Nitric oxide (NO).\n\nNitric oxide (NO) is synthesized from L-arginine, oxygen, and NADPH by neuronal nitric oxide synthase (nNOS), which is activated by Ca2+/calmodulin following NMDA receptor activation. Because it is a gas, NO is not stored in vesicles; it diffuses retrogradely from postsynaptic spines back to the presynaptic terminal. There, it activates soluble guanylyl cyclase (sGC) to produce cGMP, modulating presynaptic neurotransmitter release during long-term potentiation."
    },
    {
        "q_num": "NT-18",
        "category": "Neurotransmitters and Action Potentials",
        "stem": "A 30-year-old man undergoes electrophysiological nerve conduction testing. When a presynaptic neuron fires multiple action potentials in rapid succession at a single synapse, the individual excitatory postsynaptic potentials (EPSPs) summate to bring the axon hillock to threshold. This phenomenon is termed:",
        "options": [
            {"letter": "A", "is_correct": True, "text": "Temporal summation"},
            {"letter": "B", "is_correct": False, "text": "Spatial summation"},
            {"letter": "C", "is_correct": False, "text": "Long-term depression"},
            {"letter": "D", "is_correct": False, "text": "Post-tetanic potentiation"},
            {"letter": "E", "is_correct": False, "text": "Habituation"}
        ],
        "explanation": "Correct Answer: A. Temporal summation.\n\n• Temporal summation occurs when a single presynaptic terminal fires repeated action potentials in rapid succession, such that postsynaptic potentials generated before previous potentials have decayed summate over time.\n• Spatial summation (Option B) occurs when multiple distinct presynaptic terminals fire simultaneously at different dendritic locations, and their inputs combine across space at the axon hillock."
    },
    {
        "q_num": "NT-19",
        "category": "Neurotransmitters and Action Potentials",
        "stem": "The equilibrium potential for an ion across a biological membrane is calculated using the Nernst equation. If the extracellular potassium concentration is 4 mM and the intracellular potassium concentration is 140 mM at standard physiological temperature (37°C), the Nernst equilibrium potential for K+ (EK) is approximately:",
        "options": [
            {"letter": "A", "is_correct": False, "text": "+60 mV"},
            {"letter": "B", "is_correct": False, "text": "+120 mV"},
            {"letter": "C", "is_correct": False, "text": "0 mV"},
            {"letter": "D", "is_correct": True, "text": "-95 mV"},
            {"letter": "E", "is_correct": False, "text": "-30 mV"}
        ],
        "explanation": "Correct Answer: D. -95 mV.\n\nUsing the Nernst equation at 37°C:\nE_ion = (61.5 / z) * log10([ion]_out / [ion]_in)\nFor K+ (valence z = +1):\nEK = 61.5 * log10(4 / 140) = 61.5 * log10(0.0286) = 61.5 * (-1.544) ≈ -95 mV.\nBecause the resting membrane is predominantly permeable to K+, the resting membrane potential of excitable cells (-70 to -85 mV) lies closest to this value."
    },
    {
        "q_num": "NT-20",
        "category": "Neurotransmitters and Action Potentials",
        "stem": "A 28-year-old hiker in the Caribbean eats barracuda at a beach resort. Several hours later, he develops nausea, paresthesias, and a bizarre sensation where cold objects feel burning hot and hot objects feel cold (temperature reversal / cold allodynia). The toxin ciguatoxin causes these symptoms through which physiological effect on ion channels?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Competitive block of nicotinic receptors"},
            {"letter": "B", "is_correct": True, "text": "Opening voltage-gated sodium channels and keeping them open at resting potentials"},
            {"letter": "C", "is_correct": False, "text": "Selective blockage of delayed rectifier potassium channels"},
            {"letter": "D", "is_correct": False, "text": "Irreversible inhibition of the sodium-calcium exchanger"},
            {"letter": "E", "is_correct": False, "text": "Inactivation of calcium-activated potassium channels"}
        ],
        "explanation": "Correct Answer: B. Opening voltage-gated sodium channels and keeping them open at resting potentials.\n\nCiguatoxin (produced by Gambierdiscus toxicus dinoflagellates and bioaccumulated in reef fish like barracuda, grouper, and snapper) binds to voltage-gated Na+ channels, lowering the threshold of activation and preventing their inactivation. This causes persistent Na+ influx, continuous repetitive firing of axons, and classic temperature sensation reversal (cold allodynia)."
    },

    # =========================================================================
    # 4. VENTRICULAR SYSTEM (20 Questions: Q61 - Q80)
    # =========================================================================
    {
        "q_num": "VENT-01",
        "category": "Ventricular System",
        "stem": "A 74-year-old man is brought to the clinic by his family because of progressive difficulty walking over the past 6 months. His steps are slow, short, and shuffling, and he feels as if his feet are 'glued to the floor' (magnetic gait). Over the last 2 months, he has developed urinary urgency and incontinence, as well as forgetfulness and psychomotor slowing. MRI of the brain reveals marked symmetrical ventricular enlargement with minimal cortical sulcal enlargement. Which of the following is the most likely diagnosis?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Alzheimer disease"},
            {"letter": "B", "is_correct": True, "text": "Normal pressure hydrocephalus (NPH)"},
            {"letter": "C", "is_correct": False, "text": "Idiopathic intracranial hypertension"},
            {"letter": "D", "is_correct": False, "text": "Parkinson disease"},
            {"letter": "E", "is_correct": False, "text": "Progressive supranuclear palsy"}
        ],
        "explanation": "Correct Answer: B. Normal pressure hydrocephalus (NPH).\n\nNPH is characterized by the classic clinical triad of:\n1. Gait instability ('wobbly' - magnetic/apraxic gait)\n2. Urinary incontinence ('wet' - urgency progressing to incontinence)\n3. Cognitive impairment ('wacky' - subcortical psychomotor slowing and memory loss)\nNeuroimaging demonstrates ventricular enlargement out of proportion to cerebral sulcal enlargement. Lumbar puncture opening pressure is typically normal. It is caused by impaired CSF reabsorption across the arachnoid granulations into the superior sagittal sinus. A large-volume lumbar puncture (tap test) produces temporary symptomatic improvement and predicts positive response to ventriculoperitoneal (VP) shunting."
    },
    {
        "q_num": "VENT-02",
        "category": "Ventricular System",
        "stem": "A 27-year-old obese woman (BMI 36 kg/m²) presents with daily throbbing headaches that are worse upon awakening and exacerbated by coughing or bending forward. She describes brief episodes of visual darkening lasting several seconds ('transient visual obscurations') and pulsatile whooshing tinnitus in both ears. Fundoscopic examination reveals bilateral optic disc edema (papilledema). Cranial nerve examination shows impaired abduction of both eyes. Brain MRI with MR venography is completely normal with no mass, hydrocephalus, or venous sinus thrombosis. Which of the following lumbar puncture findings is expected in this patient?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Elevated white blood cell count with lymphocytic predominance"},
            {"letter": "B", "is_correct": False, "text": "Markedly elevated protein with xanthochromia"},
            {"letter": "C", "is_correct": True, "text": "Elevated opening pressure (>250 mm H2O) with normal CSF composition"},
            {"letter": "D", "is_correct": False, "text": "Decreased opening pressure (<60 mm H2O)"},
            {"letter": "E", "is_correct": False, "text": "Presence of oligoclonal IgG bands"}
        ],
        "explanation": "Correct Answer: C. Elevated opening pressure (>250 mm H2O) with normal CSF composition.\n\nThis patient has Idiopathic Intracranial Hypertension (IIH, pseudotumor cerebri). Typical demographics are young, overweight females of childbearing age. Symptoms include headache, papilledema, pulsatile tinnitus, and transient visual obscurations. Bilateral CN VI palsies occur as a 'false localizing sign' because the abducens nerve has a long intracranial course vulnerable to elevated ICP. Diagnosis requires elevated opening pressure on LP (>250 mm H2O in adults) with normal CSF analysis. First-line medical therapy is weight loss and acetazolamide (which inhibits choroid plexus carbonic anhydrase, reducing CSF production)."
    },
    {
        "q_num": "VENT-03",
        "category": "Ventricular System",
        "stem": "A 6-year-old boy presents with progressive morning headaches, vomiting, and ataxia. Brain MRI demonstrates an obstructing mass in the posterior fossa that has occluded the fourth ventricle, causing severe dilation of the third and lateral ventricles. Through which narrow anatomical structure does cerebrospinal fluid normally flow from the third ventricle to the fourth ventricle?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Interventricular foramen of Monro"},
            {"letter": "B", "is_correct": True, "text": "Cerebral aqueduct of Sylvius"},
            {"letter": "C", "is_correct": False, "text": "Lateral foramen of Luschka"},
            {"letter": "D", "is_correct": False, "text": "Median foramen of Magendie"},
            {"letter": "E", "is_correct": False, "text": "Arachnoid granulations"}
        ],
        "explanation": "Correct Answer: B. Cerebral aqueduct of Sylvius.\n\nNormal CSF circulation pathway:\n1. Lateral ventricles (produced by choroid plexus)\n2. Interventricular foramina of Monro → Third ventricle\n3. Cerebral aqueduct of Sylvius (in midbrain) → Fourth ventricle\n4. Foramina of Luschka (two lateral) and Foramen of Magendie (one midline) → Subarachnoid space (cisterna magna and basal cisterns)\n5. Arachnoid granulations / villi → Superior sagittal sinus (venous drainage)."
    },
    {
        "q_num": "VENT-04",
        "category": "Ventricular System",
        "stem": "A physician performs a diagnostic lumbar puncture on a 35-year-old man. The needle is inserted in the midline at the L3-L4 interspace with the patient in the lateral decubitus position. To enter the subarachnoid space and obtain CSF, the needle must pass through several anatomical layers. Which of the following represents the correct sequence of structures traversed from superficial to deep?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Skin → Supraspinous ligament → Interspinous ligament → Epidural space → Ligamentum flavum → Dura mater → Arachnoid mater"},
            {"letter": "B", "is_correct": True, "text": "Skin → Supraspinous ligament → Interspinous ligament → Ligamentum flavum → Epidural space → Dura mater → Arachnoid mater"},
            {"letter": "C", "is_correct": False, "text": "Skin → Ligamentum flavum → Supraspinous ligament → Dura mater → Arachnoid mater → Pia mater"},
            {"letter": "D", "is_correct": False, "text": "Skin → Supraspinous ligament → Ligamentum flavum → Subarachnoid space → Dura mater"},
            {"letter": "E", "is_correct": False, "text": "Skin → Interspinous ligament → Supraspinous ligament → Ligamentum flavum → Subdural space"}
        ],
        "explanation": "Correct Answer: B. Skin → Supraspinous ligament → Interspinous ligament → Ligamentum flavum → Epidural space → Dura mater → Arachnoid mater.\n\nLayers traversed during lumbar puncture from external to internal:\n1. Skin and subcutaneous tissue\n2. Supraspinous ligament (connecting tips of spinous processes)\n3. Interspinous ligament (between adjacent spinous processes)\n4. Ligamentum flavum (yellow ligament between laminae; produces a distinct 'pop')\n5. Epidural space (contains internal vertebral venous plexus and fat)\n6. Dura mater\n7. Arachnoid mater (second 'pop'; needle enters subarachnoid space containing CSF)\nNote: The pia mater lines the spinal cord/roots and is NOT pierced."
    },
    {
        "q_num": "VENT-05",
        "category": "Ventricular System",
        "stem": "Cerebrospinal fluid (CSF) is produced continuously at a rate of approximately 500 mL/day (0.35 mL/min) by specialized epithelial structures. Which of the following specialized cell types forms the choroid plexus and produces CSF?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Protoplasmic astrocytes with end-feet"},
            {"letter": "B", "is_correct": True, "text": "Modified ependymal cells with tight junctions"},
            {"letter": "C", "is_correct": False, "text": "Pericytes lining fenestrated capillaries"},
            {"letter": "D", "is_correct": False, "text": "Microglial cells of mesodermal origin"},
            {"letter": "E", "is_correct": False, "text": "Arachnoid cap cells of the meninges"}
        ],
        "explanation": "Correct Answer: B. Modified ependymal cells with tight junctions.\n\nThe choroid plexus is located within the lateral, third, and fourth ventricles. It consists of invaginated vascular fronds covered by a single layer of modified cuboidal-to-columnar ependymal cells joined by apical tight junctions (zonula occludens). These tight junctions form the blood-CSF barrier. Capillaries within the core are fenestrated, but the ependymal tight junctions strictly regulate the active secretion and ionic composition of CSF via Na+/K+ ATPases, carbonic anhydrase, and aquaporin-1 channels."
    },
    {
        "q_num": "VENT-06",
        "category": "Ventricular System",
        "stem": "A 45-year-old woman presents with severe headaches that occur exclusively when she stands up or sits upright, and resolve almost completely when she lies flat (orthostatic headache). She also reports neck stiffness, nausea, and muffled hearing. A brain MRI with gadolinium demonstrates diffuse, smooth, pachymeningeal (dural) enhancement without leptomeningeal involvement. What is the underlying pathophysiology of her headache?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Bacterial colonization of the leptomeninges"},
            {"letter": "B", "is_correct": True, "text": "Spontaneous cerebrospinal fluid leak causing intracranial hypotension"},
            {"letter": "C", "is_correct": False, "text": "Impaired CSF reabsorption at the superior sagittal sinus"},
            {"letter": "D", "is_correct": False, "text": "Dilation of cerebral arterioles from hypercapnia"},
            {"letter": "E", "is_correct": False, "text": "Obstruction of the foramen of Monro by a colloid cyst"}
        ],
        "explanation": "Correct Answer: B. Spontaneous cerebrospinal fluid leak causing intracranial hypotension.\n\nThis patient has Spontaneous Intracranial Hypotension (SIH), typically caused by a spontaneous dural tear or CSF leak in the spine (often thoracic). Key characteristics:\n• Postural / orthostatic headache (worse upright, relieved supine)\n• Diffuse, thick, smooth dural enhancement on brain MRI (due to compensatory venous engorgement according to the Monro-Kellie doctrine)\n• Subdural hygromas or downward sagging of the brainstem ('brain sag')\nTreatment includes bed rest, oral hydration, caffeine, and targeted epidural blood patch (EBP)."
    },
    {
        "q_num": "VENT-07",
        "category": "Ventricular System",
        "stem": "An adult patient with an acute change in mental status and signs of elevated intracranial pressure is evaluated in the neurointensive care unit. According to the Monro-Kellie hypothesis, the total volume inside the rigid, non-compliant adult cranial vault is fixed. The cranial cavity is occupied by which three physiological compartments?",
        "options": [
            {"letter": "A", "is_correct": True, "text": "Brain parenchyma, cerebrospinal fluid, and intravascular blood"},
            {"letter": "B", "is_correct": False, "text": "Brain parenchyma, skull bone, and dura mater"},
            {"letter": "C", "is_correct": False, "text": "Arterial blood, venous blood, and lymphatic fluid"},
            {"letter": "D", "is_correct": False, "text": "Extracellular fluid, intracellular fluid, and interstitial myelin"},
            {"letter": "E", "is_correct": False, "text": "Choroid plexus, ependyma, and subarachnoid cisterns"}
        ],
        "explanation": "Correct Answer: A. Brain parenchyma, cerebrospinal fluid, and intravascular blood.\n\nThe Monro-Kellie doctrine states that the rigid, non-expandable cranial vault has a fixed total volume composed of:\n1. Brain tissue (~80%, ~1400 mL)\n2. Cerebrospinal fluid (~10%, ~150 mL)\n3. Intravascular blood (~10%, ~150 mL)\nAn increase in the volume of one component (e.g., mass, hematoma, edema) must be compensated by an equal reduction in the volume of the others (primarily CSF displacement into the spinal thecal sac and venous blood extrusion into jugular veins). Once compensatory mechanisms are exhausted, intracranial pressure rises exponentially."
    },
    {
        "q_num": "VENT-08",
        "category": "Ventricular System",
        "stem": "A 38-year-old man presents with sudden, episodic 'drop attacks' (loss of postural tone and falling to the ground without loss of consciousness) that occur when he turns his head to the side. These attacks are preceded by severe paroxysmal bifrontal headaches. Brain MRI reveals a 1.5 cm smooth, hyperdense, spherical mass attached to the roof of the third ventricle. Which lesion is most likely present?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Craniopharyngioma"},
            {"letter": "B", "is_correct": True, "text": "Colloid cyst of the third ventricle"},
            {"letter": "C", "is_correct": False, "text": "Medulloblastoma"},
            {"letter": "D", "is_correct": False, "text": "Ependymoma of the fourth ventricle"},
            {"letter": "E", "is_correct": False, "text": "Meningioma of the sphenoid wing"}
        ],
        "explanation": "Correct Answer: B. Colloid cyst of the third ventricle.\n\nA colloid cyst is a benign, mucin-filled developmental cyst located at the anterior roof of the third ventricle, adjacent to the paired interventricular foramina of Monro. Positional head changes can cause the cyst to act as a ball-valve, suddenly occluding the foramina of Monro. This triggers acute obstructive hydrocephalus, manifesting as sudden severe positional headaches, nausea, drop attacks, and potentially fatal herniation."
    },
    {
        "q_num": "VENT-09",
        "category": "Ventricular System",
        "stem": "A 21-year-old woman recovers from severe pneumococcal meningitis. Three months later, she presents with progressive lethargy, headache, and gait instability. Brain MRI shows symmetrical dilation of the lateral, third, and fourth ventricles without any focal mass or stenosis of the cerebral aqueduct. What type of hydrocephalus has this patient developed?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Non-communicating (obstructive) hydrocephalus"},
            {"letter": "B", "is_correct": True, "text": "Communicating hydrocephalus"},
            {"letter": "C", "is_correct": False, "text": "Hydrocephalus ex vacuo"},
            {"letter": "D", "is_correct": False, "text": "Dandy-Walker hydrocephalus"},
            {"letter": "E", "is_correct": False, "text": "External hydrocephalus"}
        ],
        "explanation": "Correct Answer: B. Communicating hydrocephalus.\n\nCommunicating hydrocephalus occurs when there is unobstructed CSF flow throughout the ventricular system (all ventricles—lateral, third, and fourth—are symmetrically dilated), but CSF reabsorption at the arachnoid granulations is compromised. Post-meningitic or post-subarachnoid hemorrhage (SAH) inflammatory scarring and fibrosis of the arachnoid villi prevent normal resorption of CSF into the superior sagittal sinus."
    },
    {
        "q_num": "VENT-10",
        "category": "Ventricular System",
        "stem": "An 82-year-old woman with severe Alzheimer disease undergoes brain MRI. The scan demonstrates marked cerebral atrophy with pronounced thinning of cortical gyri, widening of sulci, and compensatory enlargement of both lateral ventricles. Her intracranial pressure is normal. This appearance is best described as:",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Normal pressure hydrocephalus"},
            {"letter": "B", "is_correct": False, "text": "Communicating hydrocephalus"},
            {"letter": "C", "is_correct": True, "text": "Hydrocephalus ex vacuo"},
            {"letter": "D", "is_correct": False, "text": "Aqueductal stenosis"},
            {"letter": "E", "is_correct": False, "text": "Idiopathic intracranial hypertension"}
        ],
        "explanation": "Correct Answer: C. Hydrocephalus ex vacuo.\n\nHydrocephalus ex vacuo is NOT true hydrocephalus (intracranial pressure is normal, and there is no obstruction or impairment of CSF dynamics). Instead, ventricular enlargement occurs as a passive, compensatory consequence of brain parenchyma volume loss (cerebral cortical atrophy in Alzheimer disease, frontotemporal dementia, Huntington disease, or Pick disease). The sulci and ventricles enlarge proportionally."
    },
    {
        "q_num": "VENT-11",
        "category": "Ventricular System",
        "stem": "Which of the following medications is a carbonic anhydrase inhibitor that reduces the rate of CSF production by the choroid plexus and is the preferred first-line pharmacological treatment for idiopathic intracranial hypertension (pseudotumor cerebri)?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Furosemide"},
            {"letter": "B", "is_correct": False, "text": "Mannitol"},
            {"letter": "C", "is_correct": True, "text": "Acetazolamide"},
            {"letter": "D", "is_correct": False, "text": "Spironolactone"},
            {"letter": "E", "is_correct": False, "text": "Hydrochlorothiazide"}
        ],
        "explanation": "Correct Answer: C. Acetazolamide.\n\nAcetazolamide inhibits carbonic anhydrase in the choroid plexus epithelial cells, which decreases bicarbonate and sodium transport into the ventricular lumen, reducing CSF secretion by up to 50%. It is the standard first-line medical therapy for idiopathic intracranial hypertension (IIH). Common adverse effects include distal paresthesias, metabolic acidosis, hypokalemia, and calcium phosphate kidney stones."
    },
    {
        "q_num": "VENT-12",
        "category": "Ventricular System",
        "stem": "A neurosurgeon places an external ventricular drain (EVD) to manage acute hydrocephalus. The catheter is inserted through a burr hole at Kocher's point (approximately 1 cm anterior to the coronal suture and 2-3 cm lateral to the midline). The tip of the catheter is directed toward which ventricular structure to achieve optimal CSF drainage?",
        "options": [
            {"letter": "A", "is_correct": True, "text": "Frontal horn of the lateral ventricle near the foramen of Monro"},
            {"letter": "B", "is_correct": False, "text": "Temporal horn of the lateral ventricle"},
            {"letter": "C", "is_correct": False, "text": "Occipital horn of the lateral ventricle"},
            {"letter": "D", "is_correct": False, "text": "Cerebral aqueduct"},
            {"letter": "E", "is_correct": False, "text": "Fourth ventricle median aperture"}
        ],
        "explanation": "Correct Answer: A. Frontal horn of the lateral ventricle near the foramen of Monro.\n\nAn external ventricular drain (ventriculostomy) is standardly placed through Kocher point into the frontal (anterior) horn of the ipsilateral lateral ventricle, with the tip positioned just anterior to the foramen of Monro. The frontal horn contains no choroid plexus (choroid plexus is located in the atrium/trigone, temporal horn, and body of the lateral ventricle, as well as the 3rd and 4th ventricles), which prevents the catheter tip from becoming occluded by choroid plexus tissue."
    },
    {
        "q_num": "VENT-13",
        "category": "Ventricular System",
        "stem": "In which of the following regions of the ventricular system is choroid plexus tissue completely absent?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Body of the lateral ventricle"},
            {"letter": "B", "is_correct": False, "text": "Temporal horn of the lateral ventricle"},
            {"letter": "C", "is_correct": True, "text": "Anterior (frontal) horn of the lateral ventricle"},
            {"letter": "D", "is_correct": False, "text": "Roof of the third ventricle"},
            {"letter": "E", "is_correct": False, "text": "Caudal roof of the fourth ventricle"}
        ],
        "explanation": "Correct Answer: C. Anterior (frontal) horn of the lateral ventricle.\n\nChoroid plexus is located in:\n• Body and temporal horn of the lateral ventricles\n• Atrium / trigone of the lateral ventricles\n• Roof of the 3rd ventricle\n• Caudal roof and lateral recesses of the 4th ventricle\nImportantly, choroid plexus is completely ABSENT from the anterior (frontal) horn and occipital (posterior) horn of the lateral ventricles, as well as the cerebral aqueduct."
    },
    {
        "q_num": "VENT-14",
        "category": "Ventricular System",
        "stem": "A 12-year-old girl presents with progressive headaches, papilledema, and Parinaud syndrome (dorsal midbrain syndrome: upward gaze palsy, convergence-retraction nystagmus, and light-near pupillary dissociation). An MRI reveals a pineal gland mass compressing the posterior midbrain. Compression of which ventricular structure by this pineal tumor produces non-communicating hydrocephalus?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Foramen of Monro"},
            {"letter": "B", "is_correct": True, "text": "Cerebral aqueduct of Sylvius"},
            {"letter": "C", "is_correct": False, "text": "Foramen of Luschka"},
            {"letter": "D", "is_correct": False, "text": "Foramen of Magendie"},
            {"letter": "E", "is_correct": False, "text": "Central canal of the spinal cord"}
        ],
        "explanation": "Correct Answer: B. Cerebral aqueduct of Sylvius.\n\nA pinealoma (such as a germinoma or pineocytoma) compresses the dorsal midbrain tegmentum (superior colliculi and pretectal nuclei), producing Parinaud syndrome (vertical gaze palsy, pseudo-Argyll Robertson pupils, convergence-retraction nystagmus). Ventral compression also occludes the adjacent cerebral aqueduct of Sylvius, resulting in acute obstructive (non-communicating) hydrocephalus of the lateral and third ventricles."
    },
    {
        "q_num": "VENT-15",
        "category": "Ventricular System",
        "stem": "The subarachnoid space expands into several large reservoirs around the base of the brain called subarachnoid cisterns. Which of the following cisterns is located between the inferior surface of the cerebellum and the dorsal surface of the medulla oblongata, directly receives CSF from the foramen of Magendie, and is the largest subarachnoid cistern in the posterior fossa?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Interpeduncular cistern"},
            {"letter": "B", "is_correct": False, "text": "Ambient cistern"},
            {"letter": "C", "is_correct": True, "text": "Cisterna magna (cerebellomedullary cistern)"},
            {"letter": "D", "is_correct": False, "text": "Quadrigeminal cistern"},
            {"letter": "E", "is_correct": False, "text": "Chiasmatic cistern"}
        ],
        "explanation": "Correct Answer: C. Cisterna magna (cerebellomedullary cistern).\n\nThe cisterna magna (cerebellomedullary cistern) is the largest cistern in the intracranial subarachnoid space, situated between the cerebellum and the dorsal medulla. CSF exits the fourth ventricle through the median aperture (foramen of Magendie) directly into the cisterna magna before circulating over the cerebral convexities and down the spinal subarachnoid space."
    },
    {
        "q_num": "VENT-16",
        "category": "Ventricular System",
        "stem": "A 52-year-old man presents with progressive confusion and a staggering gait following a severe bout of cryptococcal meningitis. A high-volume diagnostic lumbar puncture is performed. If the patient has communicating hydrocephalus, what change is expected in the ventricular system immediately following removal of 30-50 mL of CSF?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Complete collapse of the fourth ventricle with herniation"},
            {"letter": "B", "is_correct": True, "text": "Transient decompression with clinical improvement in gait and cognitive function"},
            {"letter": "C", "is_correct": False, "text": "Acute obstructive hydrocephalus from aqueductal kinking"},
            {"letter": "D", "is_correct": False, "text": "Immediate permanent resolution of all symptoms"},
            {"letter": "E", "is_correct": False, "text": "Paradoxical increase in CSF opening pressure"}
        ],
        "explanation": "Correct Answer: B. Transient decompression with clinical improvement in gait and cognitive function.\n\nIn communicating hydrocephalus (including normal pressure hydrocephalus), removal of 30-50 mL of CSF via a large-volume lumbar puncture (Miller Fisher spinal tap test) temporarily reduces ventricular pressure and improves periventricular white matter perfusion, resulting in rapid, transient improvement in gait velocity, balance, and cognitive psychomotor speed."
    },
    {
        "q_num": "VENT-17",
        "category": "Ventricular System",
        "stem": "A neonate is delivered at 38 weeks gestation with severe macrocephaly. Cranial ultrasound shows massive dilation of both lateral ventricles and the third ventricle, with a normal-sized fourth ventricle. What is the most common congenital cause of non-communicating hydrocephalus presenting in infancy with this ventricular configuration?",
        "options": [
            {"letter": "A", "is_correct": True, "text": "Congenital aqueductal stenosis (often X-linked L1CAM mutation)"},
            {"letter": "B", "is_correct": False, "text": "Arachnoid cyst of the middle cranial fossa"},
            {"letter": "C", "is_correct": False, "text": "Choroid plexus papilloma of the fourth ventricle"},
            {"letter": "D", "is_correct": False, "text": "Agenesis of the corpus callosum"},
            {"letter": "E", "is_correct": False, "text": "Thrombosis of the vein of Galen"}
        ],
        "explanation": "Correct Answer: A. Congenital aqueductal stenosis (often X-linked L1CAM mutation).\n\nCongenital aqueductal stenosis is the most common cause of congenital hydrocephalus. Because the cerebral aqueduct is the narrowest conduit in the ventricular system (normally ~1-2 mm in diameter), narrowing or fork-like occlusion blocks flow from the third to the fourth ventricle, causing upstream triventricular hydrocephalus (dilated lateral and third ventricles, with a normal or compressed fourth ventricle). It can occur sporadically, post-infection (mumps, CMV, toxoplasmosis), or as an X-linked recessive disorder (Bickers-Adams-Edwards syndrome, due to mutations in the L1CAM gene encoding a neural cell adhesion molecule)."
    },
    {
        "q_num": "VENT-18",
        "category": "Ventricular System",
        "stem": "Under physiological conditions, cerebrospinal fluid flows from the subarachnoid space into the superior sagittal sinus across arachnoid granulations. What physical mechanism drives this unidirectional bulk flow of CSF into the venous circulation?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Active ATP-dependent pinocytosis across endothelial cells"},
            {"letter": "B", "is_correct": True, "text": "Hydrostatic pressure gradient where CSF pressure exceeds dural venous sinus pressure"},
            {"letter": "C", "is_correct": False, "text": "Colloid oncotic pressure gradient established by high CSF albumin"},
            {"letter": "D", "is_correct": False, "text": "Osmotic pressure gradient driven by high CSF glucose"},
            {"letter": "E", "is_correct": False, "text": "Arterial pulsations of the internal carotid siphon"}
        ],
        "explanation": "Correct Answer: B. Hydrostatic pressure gradient where CSF pressure exceeds dural venous sinus pressure.\n\nCSF reabsorption across arachnoid granulations functions as a passive, pressure-dependent, one-way valve. Under normal conditions, subarachnoid CSF hydrostatic pressure (approximately 100-150 mm H2O) is higher than the venous pressure inside the superior sagittal sinus (approximately 50-80 mm H2O). This positive hydrostatic pressure gradient (ΔP ≈ 30-70 mm H2O) drives bulk transcellular fluid flow through giant vacuoles and endothelial pores into the sinus lumen. If sinus pressure exceeds CSF pressure, the tubules collapse, preventing retrograde blood flow into the CSF."
    },
    {
        "q_num": "VENT-19",
        "category": "Ventricular System",
        "stem": "A 4-year-old boy presents with progressive macrocephaly, vomiting, and ataxia. Brain MRI reveals an intraventricular cauliflower-like, well-circumscribed, highly vascular mass in the atrium of the left lateral ventricle. Biopsy confirms a choroid plexus papilloma. In addition to physical obstruction of the CSF pathways, by what other mechanism does this tumor produce hydrocephalus?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Destruction of ependymal ciliary transport"},
            {"letter": "B", "is_correct": True, "text": "Marked hypersecretion of cerebrospinal fluid exceeding resorptive capacity"},
            {"letter": "C", "is_correct": False, "text": "Compaction of the cerebral parenchyma into the spinal canal"},
            {"letter": "D", "is_correct": False, "text": "Infiltration of the subarachnoid space by mucinous fluid"},
            {"letter": "E", "is_correct": False, "text": "Thrombosis of the internal cerebral veins"}
        ],
        "explanation": "Correct Answer: B. Marked hypersecretion of cerebrospinal fluid exceeding resorptive capacity.\n\nChoroid plexus papilloma is a benign neuroepithelial tumor derived from choroid plexus epithelial cells, most commonly arising in the lateral ventricles in children (and 4th ventricle in adults). It is one of the rare etiologies of hydrocephalus caused by true CSF hypersecretion (producing CSF at rates far exceeding the normal 500 mL/day), overwhelming the resorptive capacity of arachnoid granulations in addition to causing physical ventricular outflow obstruction."
    },
    {
        "q_num": "VENT-20",
        "category": "Ventricular System",
        "stem": "Which of the following circumventricular organs is located along the wall of the third ventricle, possesses a deficient blood-brain barrier (fenestrated capillaries), and contains the area postrema in the dorsal medulla responsible for sensing emetic toxins in the bloodstream to trigger vomiting?",
        "options": [
            {"letter": "A", "is_correct": True, "text": "Area postrema"},
            {"letter": "B", "is_correct": False, "text": "Subfornical organ"},
            {"letter": "C", "is_correct": False, "text": "Organum vasculosum of the lamina terminalis (OVLT)"},
            {"letter": "D", "is_correct": False, "text": "Median eminence"},
            {"letter": "E", "is_correct": False, "text": "Posterior pituitary gland"}
        ],
        "explanation": "Correct Answer: A. Area postrema.\n\nCircumventricular organs (CVOs) have fenestrated capillaries lacking tight junctions, allowing them to sense blood-borne molecules or secrete neurohormones directly into the circulation:\n• Area postrema (caudal 4th ventricle): Chemoreceptor trigger zone (CTZ) that detects toxins/chemotherapeutics in blood and triggers vomiting.\n• Organum vasculosum of the lamina terminalis (OVLT, 3rd ventricle): Osmoreceptors that regulate thirst and fever (pyrogens trigger PGE2 here).\n• Subfornical organ (SFO): Responds to circulating angiotensin II to regulate drinking behavior and blood pressure."
    }
]

if __name__ == '__main__':
    print(f'Part 1 loaded successfully with {len(part1_questions)} questions.')
