# -*- coding: utf-8 -*-
# inhouse_section3.py
# Section 3: Somatosensory & Trigeminal Systems
# Covers:
# - Somatosensory DCML (Tactile Receptors, Axon Diameters, 3-Neuron Pathway, Romberg, Agnosias)
# - Somatosensory ALS (Nociception vs Pain, Spinothalamic Pathway, Referred Cardiac Pain, Lesion Sidedness)
# - Trigeminal Pathway (Facial Touch vs Pain/Temp, Corneal Reflex, Jaw-Jerk Reflex, VPM)
# - Pain Mechanisms (Peripheral vs Central Sensitization, Allodynia vs Hyperalgesia, Paresthesia vs Dysesthesia)
# - Spinal Cord Syndromes (Brown-Séquard, Syringomyelia, Tabes Dorsalis, Vitamin B12 SCD)
# - Radiculopathies & Neuropathies (C6, C7, L5, S1, Carpal Tunnel, NCS Demyelinating vs Axonal, CRPS)

questions_section3 = [
    # ==========================================
    # DCML PATHWAY & TACTILE RECEPTORS
    # ==========================================
    {
        "id": "IH_Q106",
        "question_number": 106,
        "category": "In House: Somatosensory DCML Pathway",
        "stem": "A 24-year-old blind student reads a passage written in Braille by rapidly gliding her fingertips across raised dots on paper. Which of the following cutaneous mechanoreceptors possesses a small receptive field and slow adaptation rate, providing the high spatial resolution necessary to discriminate fine shapes, edges, and braille characters?",
        "options": [
            {"text": "Pacinian corpuscles", "is_correct": False},
            {"text": "Meissner corpuscles", "is_correct": False},
            {"text": "Merkel discs (complexes)", "is_correct": True},
            {"text": "Ruffini endings", "is_correct": False},
            {"text": "Free nerve endings", "is_correct": False}
        ],
        "explanation": "Correct Answer: C. Merkel discs (complexes).\n\nCutaneous mechanoreceptors are classified by receptive field size and adaptation rate:\n1. Merkel Discs: Located in the basal epidermal layer (stratum basale) of glabrous (hairless) and hairy skin; have SMALL receptive fields with distinct borders and are SLOWLY ADAPTING. They fire continuously to sustained static pressure and provide the highest spatial resolution (0.5 mm), making them uniquely suited for resolving fine tactile details, points, edges, shapes, and Braille reading.\n2. Meissner Corpuscles: Located in dermal papillae of glabrous skin; have SMALL receptive fields and are RAPIDLY ADAPTING. They detect low-frequency vibration (flutter, 30–50 Hz), slip detection, and grip control.\n3. Pacinian Corpuscles: Located deep in the dermis and subcutaneous tissue; have LARGE receptive fields with indistinct borders and are RAPIDLY ADAPTING (onion-like lamellae). They detect high-frequency vibration (200–300 Hz) and transient mechanical taps.\n4. Ruffini Endings: Located deep in the dermis; have LARGE receptive fields and are SLOWLY ADAPTING. They respond to lateral skin stretch, joint movement, and finger position.\n\n• Options A, B, D, and E do not match the specific high-resolution, slow-adapting properties of Merkel discs."
    },
    {
        "id": "IH_Q107",
        "question_number": 107,
        "category": "In House: Somatosensory DCML Pathway",
        "stem": "An electrophysiologist records sensory action potentials from human peripheral nerves. She isolates four distinct nerve fiber groups: Ia, A-beta, A-delta, and C fibers. Which of the following pairings correctly matches the nerve fiber type with its diameter, myelination status, and physiological sensory modality?",
        "options": [
            {"text": "C fibers: Largest diameter, heavily myelinated; transmit conscious proprioception from muscle spindles", "is_correct": False},
            {"text": "A-delta fibers: Unmyelinated, slowest conduction velocity (0.5-2 m/s); transmit warm temperature and itch", "is_correct": False},
            {"text": "A-beta fibers: Medium-to-large diameter, heavily myelinated; transmit tactile sensations (fine touch, vibration, pressure) from encapsulated mechanoreceptors", "is_correct": True},
            {"text": "Ia fibers: Smallest diameter, unmyelinated; transmit dull aching visceral pain", "is_correct": False},
            {"text": "A-beta fibers: Unmyelinated; transmit reflex flexor withdrawal pain", "is_correct": False}
        ],
        "explanation": "Correct Answer: C. A-beta fibers: Medium-to-large diameter, heavily myelinated; transmit tactile sensations (fine touch, vibration, pressure) from encapsulated mechanoreceptors.\n\nPeripheral nerve fiber classification based on diameter and myelination correlates directly with conduction velocity and sensory modality:\n1. Group A-alpha / Ia & Ib fibers: Largest diameter (12–20 μm), heavily myelinated, fastest conduction (70–120 m/s); convey proprioceptive afferents from muscle spindles (Ia) and Golgi tendon organs (Ib).\n2. Group A-beta / II fibers: Medium-to-large diameter (6–12 μm), heavily myelinated, rapid conduction (30–70 m/s); convey light touch, discriminative touch, vibration, and pressure from encapsulated cutaneous mechanoreceptors (Meissner, Pacinian, Merkel, Ruffini).\n3. Group A-delta / III fibers: Small diameter (1–5 μm), thinly myelinated, moderate conduction (12–30 m/s); convey fast, sharp, well-localized 'first pain' and cold temperature.\n4. Group C / IV fibers: Smallest diameter (0.2–1.5 μm), completely UNMYELINATED, slowest conduction (0.5–2.0 m/s); convey slow, dull, burning, aching 'second pain', warm temperature, and itch.\n\n• Options A, B, D, and E incorrectly describe fiber sizes and modalities."
    },
    {
        "id": "IH_Q108",
        "question_number": 108,
        "category": "In House: Somatosensory DCML Pathway",
        "stem": "A 56-year-old man presents with progressive sensory loss. Neurological examination reveals complete loss of vibratory sensation and two-point discrimination over his right lower extremity up to the right iliac crest (T10 dermatome). Vibratory and light touch sensation in both upper extremities and the left lower extremity are intact. In which tract of the spinal cord is this patient's lesion localized?",
        "options": [
            {"text": "Right fasciculus cuneatus", "is_correct": False},
            {"text": "Right fasciculus gracilis", "is_correct": True},
            {"text": "Left fasciculus gracilis", "is_correct": False},
            {"text": "Right lateral spinothalamic tract", "is_correct": False},
            {"text": "Left anterior spinothalamic tract", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. Right fasciculus gracilis.\n\nThe Dorsal Column-Medial Lemniscal (DCML) pathway conveys conscious proprioception, vibratory sense, and fine discriminative touch. Primary afferents enter the spinal cord via the dorsal roots and ascend IPSILATERALLY in the dorsal funiculus without decussating in the spinal cord:\n1. Fasciculus Gracilis: Occupies the MEDIAL dorsal column throughout the entire spinal cord; carries fibers originating from the lower extremities and lower trunk (below T6, sacral, lumbar, and lower thoracic levels).\n2. Fasciculus Cuneatus: Occupies the LATERAL dorsal column; present only at and above spinal cord level T6; carries fibers originating from the upper trunk, upper extremities, and neck (cervical and upper thoracic levels).\nBecause dorsal column fibers do not cross until the lower medulla (at the sensory decussation of internal arcuate fibers), a lesion of the right fasciculus gracilis produces an IPSILATERAL loss of vibration, proprioception, and fine touch in the right lower extremity.\n\n• Option A is incorrect: Fasciculus cuneatus carries upper extremity sensation (T6 and above).\n• Option C is incorrect: Left fasciculus gracilis would cause left lower extremity loss.\n• Option D is incorrect: Right spinothalamic tract lesion causes contralateral (left-sided) loss of pain and temperature.\n• Option E is incorrect: Anterior spinothalamic tract conveys crude touch."
    },
    {
        "id": "IH_Q109",
        "question_number": 109,
        "category": "In House: Somatosensory DCML Pathway",
        "stem": "During an anatomy practical exam, a student traces the entire 3-neuron chain of the dorsal column-medial lemniscal (DCML) pathway from the right great toe to the cerebral cortex. Where are the second-order neuronal cell bodies located, and where do their axons cross the midline?",
        "options": [
            {"text": "Dorsal root ganglion; cross at the anterior white commissure of the lumbar spinal cord", "is_correct": False},
            {"text": "Nucleus gracilis in the caudal medulla; cross as internal arcuate fibers to form the contralateral medial lemniscus", "is_correct": True},
            {"text": "Nucleus cuneatus in the rostral pons; cross in the trapezoid body", "is_correct": False},
            {"text": "Ventral posterolateral (VPL) nucleus of the thalamus; cross in the corpus callosum", "is_correct": False},
            {"text": "Substantia gelatinosa of the dorsal horn; cross at the pyramidal decussation", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. Nucleus gracilis in the caudal medulla; cross as internal arcuate fibers to form the contralateral medial lemniscus.\n\nThe DCML pathway consists of a strict 3-neuron chain:\n1. First-order neuron: Pseudounipolar cell body in the ipsilateral dorsal root ganglion (DRG); peripheral process innervates mechanoreceptors; central process enters the spinal cord and ascends ipsilaterally in the dorsal column (fasciculus gracilis for lower body, cuneatus for upper body) without synapsing.\n2. Second-order neuron: Cell bodies are located in the dorsal column nuclei (Nucleus Gracilis and Nucleus Cuneatus) in the dorsal caudal medulla. Axons of these second-order neurons emerge and sweep ventromedially as the INTERNAL ARCUATE FIBERS, decussating across the midline in the sensory decussation to form the contralateral MEDIAL LEMNISCUS. The medial lemniscus ascends through the medulla, pons, and midbrain.\n3. Third-order neuron: Cell bodies in the Ventral Posterolateral (VPL) nucleus of the thalamus. Axons travel through the posterior limb of the internal capsule to synapse in the primary somatosensory cortex (postcentral gyrus, Brodmann 3, 1, 2).\n\n• Options A, C, D, and E disrupt the correct anatomical locations and crossings of the 3-neuron chain."
    },
    {
        "id": "IH_Q110",
        "question_number": 110,
        "category": "In House: Somatosensory DCML Pathway",
        "stem": "A 39-year-old man presents with progressive gait instability. On examination, when asked to stand with his feet close together and his eyes open, he stands steadily without swaying. However, immediately upon closing his eyes, he sways violently and falls toward his left side unless caught by the examiner (positive Romberg test). Which of the following sensory systems is dysfunctional in this patient, and why does eye closure precipitate his unsteadiness?",
        "options": [
            {"text": "Cerebellar vermis; vision triggers cerebellar nystagmus", "is_correct": False},
            {"text": "Conscious proprioceptive system (dorsal columns / large-fiber peripheral nerves); upright balance requires at least 2 of 3 sensory inputs (vision, proprioception, vestibular), so closing the eyes eliminates visual compensation when proprioception is already lost", "is_correct": True},
            {"text": "Lateral spinothalamic tract; loss of cutaneous temperature sensation blunts foot reflexes", "is_correct": False},
            {"text": "Lateral corticospinal tract; closing the eyes interrupts voluntary motor drive", "is_correct": False},
            {"text": "Basal ganglia; closing the eyes halts dopamine release in the striatum", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. Conscious proprioceptive system (dorsal columns / large-fiber peripheral nerves); upright balance requires at least 2 of 3 sensory inputs (vision, proprioception, vestibular), so closing the eyes eliminates visual compensation when proprioception is already lost.\n\nMaintaining upright equilibrium requires harmonious integration of at least 2 of 3 sensory modalities: (1) Vision, (2) Proprioception (joint position sense conveyed by dorsal columns and large peripheral sensory fibers), and (3) Vestibular apparatus. The Romberg test distinguishes sensory ataxia from cerebellar ataxia:\n- In SENSORY ATAXIA (e.g., tabes dorsalis, vitamin B12 deficiency, peripheral sensory neuropathy): Proprioceptive feedback is defective. When the patient's eyes are open, vision successfully compensates for the lost proprioception, allowing stable standing. When the patient closes their eyes, visual compensation is removed, leaving only the vestibular system, which is insufficient to maintain balance, causing the patient to sway and fall (POSITIVE Romberg sign).\n- In CEREBELLAR ATAXIA (e.g., cerebellar vermis midline lesion, alcohol toxicity): Balance and coordination processing are impaired at the central motor coordinator level. The patient is unsteady and sways with eyes open AND with eyes closed (NEGATIVE Romberg test; cerebellar ataxia is present regardless of vision).\n\n• Option A is incorrect: Midline cerebellar vermian lesions cause ataxia with eyes open as well as closed.\n• Options C, D, and E do not explain the physiological mechanism of Romberg's test."
    },
    {
        "id": "IH_Q111",
        "question_number": 111,
        "category": "In House: Somatosensory & Cortical Syndromes",
        "stem": "A 64-year-old woman is evaluated following a right middle cerebral artery ischemic stroke affecting the right parietal lobe. On examination, when a key or coin is placed into her left hand with her eyes closed, she can feel that an object is present, but is completely unable to identify what the object is by touch alone (astereognosis). She is also unable to identify numbers traced on her left palm (agraphesthesia). However, primary light touch and two-point discrimination thresholds on her fingertips are only minimally decreased. Damage to which cortical area accounts for this tactile agnosia?",
        "options": [
            {"text": "Primary motor cortex (precentral gyrus)", "is_correct": False},
            {"text": "Secondary somatosensory cortex and somatosensory association cortex (parietal operculum and superior parietal lobule, Brodmann areas 5 and 7)", "is_correct": True},
            {"text": "Frontal eye field (Brodmann area 8)", "is_correct": False},
            {"text": "Broca expressive speech area (Brodmann areas 44 and 45)", "is_correct": False},
            {"text": "Primary auditory cortex (transverse temporal gyri of Heschl)", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. Secondary somatosensory cortex and somatosensory association cortex (parietal operculum and superior parietal lobule, Brodmann areas 5 and 7).\n\nTactile agnosia is the inability to recognize objects by touch in the absence of a primary sensory deficit (intact basic light touch). Key types include:\n1. Astereognosis: Inability to identify common three-dimensional objects (e.g., key, paperclip, coin) placed in the hand by manipulation with eyes closed.\n2. Agraphesthesia: Inability to recognize letters or numbers traced on the skin of the palm.\nThese complex higher-order discriminative tactile functions require the Somatosensory Association Cortex located in the parietal lobe (Brodmann areas 5 and 7 in the superior parietal lobule, as well as the secondary somatosensory cortex S2 in the parietal operculum). A lesion in the contralateral parietal association cortex destroys the integration of sensory submodalities (texture, weight, contour, temperature) into a coherent mental object representation.\n\n• Option A is incorrect: Precentral gyrus is primary motor cortex (Brodmann 4); damage causes hemiplegia.\n• Option C is incorrect: Frontal eye field coordinates voluntary saccadic eye movements.\n• Option D is incorrect: Broca area governs motor speech output.\n• Option E is incorrect: Transverse gyri of Heschl mediate primary auditory reception."
    },

    # ==========================================
    # ANTEROLATERAL SYSTEM (ALS) & REFERRED PAIN
    # ==========================================
    {
        "id": "IH_Q112",
        "question_number": 112,
        "category": "In House: Somatosensory ALS Pathway",
        "stem": "A 58-year-old man presents to the emergency department with severe, crushing substernal chest pressure radiating down the medial aspect of his left arm and forearm to the fourth and fifth digits, accompanied by diaphoresis and nausea. An ECG confirms an acute inferior ST-elevation myocardial infarction (STEMI). What is the physiological mechanism explaining why cardiac ischemia refers pain to the left arm (referred pain)?",
        "options": [
            {"text": "Direct compression of the left brachial plexus by the enlarged left ventricle", "is_correct": False},
            {"text": "The convergence-projection hypothesis: visceral nociceptive afferents from the heart enter the spinal cord at T1-T4/T5 levels and synapse on the same second-order projection neurons in the dorsal horn as somatic nociceptive afferents from the left arm and chest", "is_correct": True},
            {"text": "Retrograde axonal transport of cardiac troponin into the median nerve", "is_correct": False},
            {"text": "Spasm of the left subclavian artery causing ischemic myopathy in the forearm", "is_correct": False},
            {"text": "Direct communication between cardiac vagal fibers and the radial nerve in the neck", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. The convergence-projection hypothesis: visceral nociceptive afferents from the heart enter the spinal cord at T1-T4/T5 levels and synapse on the same second-order projection neurons in the dorsal horn as somatic nociceptive afferents from the left arm and chest.\n\nReferred pain occurs when visceral pain is perceived as originating from a somatic dermatome. The established neurobiological explanation is the Convergence-Projection Hypothesis:\n1. Visceral nociceptive afferents from the ischemic myocardium travel retrogradely along cardiac sympathetic nerves to enter the dorsal horn of the upper thoracic spinal cord (T1–T4/T5 segments).\n2. In the dorsal horn, these visceral afferents converge onto the SAME second-order spinothalamic projection neurons that receive somatic nociceptive inputs from the T1–T4 dermatomes (which cover the medial aspect of the left arm, axilla, and chest wall).\n3. Because visceral nociception is rarely activated compared to somatic inputs, the cerebral somatosensory cortex has learned to interpret excitation of these second-order spinothalamic neurons as originating from the somatic dermatome (the left arm and chest), rather than from the heart.\n\n• Option A is incorrect: The heart does not physically compress the brachial plexus.\n• Option C is incorrect: Troponin does not undergo retrograde axonal transport to cause pain.\n• Option D is incorrect: Subclavian artery spasm is not the mechanism of cardiac angina.\n• Option E is incorrect: Cardiac pain is conveyed by sympathetic afferents to T1-T4, not vagal-radial connections."
    },
    {
        "id": "IH_Q113",
        "question_number": 113,
        "category": "In House: Somatosensory ALS Pathway",
        "stem": "A 35-year-old woman is evaluated after a diving accident that caused a focal traumatic lesion localized strictly to the right anterolateral system (ALS / spinothalamic tract) at the level of the C7 spinal cord segment. On neurological examination, what type of sensory deficit and in what bodily distribution will this patient exhibit?",
        "options": [
            {"text": "Ipsilateral (right-sided) loss of vibration and fine touch from C7 downward", "is_correct": False},
            {"text": "Contralateral (left-sided) loss of pain and temperature sensation beginning approximately 1 to 2 segments below the lesion (from T1 downward)", "is_correct": True},
            {"text": "Bilateral loss of pain and temperature restricted to the C7 dermatome only", "is_correct": False},
            {"text": "Contralateral (left-sided) loss of proprioception and vibration over the entire left side of the body", "is_correct": False},
            {"text": "Ipsilateral (right-sided) loss of pain and temperature over the entire right upper limb only", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. Contralateral (left-sided) loss of pain and temperature sensation beginning approximately 1 to 2 segments below the lesion (from T1 downward).\n\nThe Anterolateral System (ALS / Spinothalamic tract) conveys pain and temperature sensations. The pathway is organized as follows:\n1. First-order fibers enter the dorsal horn via the tract of Lissauer (ascending or descending 1–2 segments before synapsing).\n2. Second-order neurons in the dorsal horn (laminae I and V) send axons that decussate obliquely across the anterior white commissure over 1 to 2 spinal segments to enter the contralateral anterolateral funiculus.\n3. The crossed fibers ascend through the spinal cord, brainstem, to the VPL thalamus.\nConsequently, an interruption of the right ALS at spinal segment C7 destroys second-order fibers that originated from the LEFT side of the body that crossed 1–2 segments below the lesion. Therefore, the clinical deficit is a CONTRALATERAL (left-sided) loss of pain and temperature sensation beginning 1 to 2 segments below the lesion level (i.e., beginning around T1/T2 dermatome and extending down through the rest of the left body and lower extremity).\n\n• Option A is incorrect: Vibration and fine touch are conveyed by the dorsal columns, which travel ipsilaterally.\n• Option C is incorrect: Bilateral segmental cape-like loss characterizes syringomyelia, which transects crossing fibers in the midline anterior white commissure.\n• Option D is incorrect: Proprioception is DCML, not ALS.\n• Option E is incorrect: ALS conveys contralateral sensation, not ipsilateral."
    },
    {
        "id": "IH_Q114",
        "question_number": 114,
        "category": "In House: Somatosensory ALS Pathway",
        "stem": "When a person accidentally steps barefoot on a sharp tack, two distinct temporal sensations of pain are felt: an immediate, sharp, well-localized pain followed seconds later by a persistent, dull, burning, poorly localized ache. What peripheral axon types and central ascending pathways mediate this dual sensation of 'fast pain' versus 'slow pain'?",
        "options": [
            {"text": "Fast pain is mediated by C fibers via the spinoreticular tract; slow pain is mediated by A-delta fibers via the neospinothalamic tract", "is_correct": False},
            {"text": "Fast pain is mediated by thinly myelinated A-delta fibers projecting via the neospinothalamic tract to the VPL thalamus and SI cortex; slow pain is mediated by unmyelinated C fibers projecting via paleospinothalamic, spinoreticular, and spinomesencephalic tracts to medial thalamus and limbic structures", "is_correct": True},
            {"text": "Both fast and slow pain are mediated by A-beta fibers synapsing in the nucleus gracilis", "is_correct": False},
            {"text": "Fast pain is generated in the dorsal horn; slow pain is generated in the motor end plate", "is_correct": False},
            {"text": "Fast pain uses acetylcholine as its neurotransmitter; slow pain exclusively uses glycine", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. Fast pain is mediated by thinly myelinated A-delta fibers projecting via the neospinothalamic tract to the VPL thalamus and SI cortex; slow pain is mediated by unmyelinated C fibers projecting via paleospinothalamic, spinoreticular, and spinomesencephalic tracts to medial thalamus and limbic structures.\n\nNociceptive signaling features dual temporal and anatomical pathways:\n1. Fast (First) Pain: Transmitted by thinly myelinated A-delta fibers (conduction velocity 12–30 m/s) releasing glutamate. They synapse in laminae I and V of the dorsal horn, decussate, and ascend in the lateral spinothalamic tract (neospinothalamic tract) to the Ventral Posterolateral (VPL) nucleus of the thalamus, projecting directly to the primary somatosensory cortex (SI). This pathway mediates the sensory-discriminative aspects of pain: precise location, sharp quality, onset, and intensity.\n2. Slow (Second) Pain: Transmitted by slowly conducting, unmyelinated C fibers (conduction velocity 0.5–2 m/s) releasing glutamate and substance P. They synapse in substantia gelatinosa (lamina II), decussate, and project via the paleospinothalamic, spinoreticular, and spinomesencephalic (spinotectal) tracts to the reticular activating system (arousal), periaqueductal gray (pain modulation), medial thalamic nuclei, insula, and anterior cingulate cortex. This pathway mediates the affective, emotional, motivational, and autonomic suffering of pain.\n\n• Option A is incorrect: It reverses the fiber types and tracts.\n• Option C is incorrect: A-beta fibers carry light touch, not noxious pain.\n• Option D is incorrect: Pain is initiated by peripheral free nerve endings, not the motor end plate.\n• Option E is incorrect: Primary nociceptive transmitters are glutamate, substance P, and CGRP, not acetylcholine or glycine."
    },
    {
        "id": "IH_Q115",
        "question_number": 115,
        "category": "In House: Somatosensory & Spinal Cord",
        "stem": "A 42-year-old woman is brought to the emergency department after sustaining a knife wound to the right side of her neck at the C5 vertebral level. Neurological examination reveals:\n- Complete loss of vibration, proprioception, and light touch in the right arm and right leg below the lesion.\n- Right-sided spastic hemiparesis with hyperreflexia and an extensor plantar response (positive Babinski sign) in the right lower extremity.\n- Complete loss of pain and temperature sensation on the left side of her body from the C7 dermatome downward.\n- Complete flaccid weakness, muscle fasciculations, and loss of all sensation in the right C5 dermatome.\nWhat spinal cord syndrome is represented by this classic clinical presentation?",
        "options": [
            {"text": "Central cord syndrome", "is_correct": False},
            {"text": "Anterior spinal artery syndrome", "is_correct": False},
            {"text": "Brown-Séquard syndrome (spinal cord hemisection)", "is_correct": True},
            {"text": "Posterior cord syndrome", "is_correct": False},
            {"text": "Cauda equina syndrome", "is_correct": False}
        ],
        "explanation": "Correct Answer: C. Brown-Séquard syndrome (spinal cord hemisection).\n\nBrown-Séquard syndrome results from hemisection of the spinal cord (most commonly from penetrating knife or gunshot trauma, lateral disc herniation, or demyelinating plaque). The anatomical basis of its findings includes:\n1. Ipsilateral loss of proprioception, vibration, and fine touch below the lesion: Destruction of the uncrossed dorsal columns (fasciculus gracilis and cuneatus) on the side of the lesion.\n2. Ipsilateral spastic paralysis below the lesion: Interruption of the descending lateral corticospinal tract, producing Upper Motor Neuron (UMN) signs (spasticity, hyperreflexia, Babinski sign) on the same side because corticospinal fibers had already decussated in the caudal medulla.\n3. Contralateral loss of pain and temperature sensation beginning 1–2 segments below the lesion: Interruption of the ascending spinothalamic tract (ALS), which carries pain/temperature fibers that crossed from the opposite side 1–2 segments below.\n4. Ipsilateral complete sensory loss and Lower Motor Neuron (LMN) flaccid paralysis at the exact level of the lesion: Destruction of entering dorsal root fibers and anterior horn motor neurons in that specific spinal segment.\n\n• Option A is incorrect: Central cord syndrome (e.g., hyperextension in cervical spondylosis or syringomyelia) preferentially affects upper extremity motor/sensory function over lower extremities.\n• Option B is incorrect: Anterior spinal artery syndrome spares the dorsal columns (proprioception intact bilaterally) and causes bilateral motor paralysis and bilateral pain/temperature loss.\n• Option D is incorrect: Posterior cord syndrome causes isolated bilateral loss of vibration and proprioception.\n• Option E is incorrect: Cauda equina syndrome affects lumbosacral nerve roots causing saddle anesthesia, bowel/bladder incontinence, and flaccid leg weakness."
    },

    # ==========================================
    # TRIGEMINAL SYSTEM & CRANIAL REFLEXES
    # ==========================================
    {
        "id": "IH_Q116",
        "question_number": 116,
        "category": "In House: Trigeminal Somatosensory Pathway",
        "stem": "A 52-year-old woman is evaluated for right facial numbness following a lateral pontine ischemic stroke. Testing demonstrates loss of light touch, fine vibration, and two-point discrimination on the right side of her forehead, cheek, and chin, while facial pain and temperature sensations remain preserved. Where is the principal synaptic relay for facial discriminative tactile sensation located in the brainstem?",
        "options": [
            {"text": "Spinal trigeminal nucleus in the medulla", "is_correct": False},
            {"text": "Chief (Principal) sensory trigeminal nucleus in the mid-pons", "is_correct": True},
            {"text": "Mesencephalic trigeminal nucleus in the midbrain", "is_correct": False},
            {"text": "Trigeminal motor nucleus in the caudal pons", "is_correct": False},
            {"text": "Nucleus ambiguus in the rostral medulla", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. Chief (Principal) sensory trigeminal nucleus in the mid-pons.\n\nThe trigeminal sensory system possesses three distinct nuclei spanning the entire brainstem, each specialized for distinct sensory submodalities:\n1. Chief (Principal) Sensory Trigeminal Nucleus: Located in the dorsolateral tegmentum of the MID-PONS at the entry point of the trigeminal nerve. It receives primary large-myelinated afferents for DISCRIMINATIVE TOUCH, pressure, and vibration from the face (analogous to the dorsal column nuclei for the body). Its second-order axons cross the midline to form the anterior trigeminothalamic tract (and uncrossed posterior tract) projecting to the Ventral Posteromedial (VPM) nucleus of the thalamus.\n2. Spinal Trigeminal Nucleus: Extends from the caudal pons down through the entire medulla into the upper cervical spinal cord (C2-C3). It receives thinly myelinated and unmyelinated fibers descending in the spinal trigeminal tract conveying PAIN, TEMPERATURE, and crude touch from the face (analogous to the spinal cord substantia gelatinosa/dorsal horn).\n3. Mesencephalic Trigeminal Nucleus: Located in the lateral midbrain tegmentum; contains primary pseudounipolar cell bodies conveying PROPRIOCEPTION from muscles of mastication and periodontal ligaments.\n\n• Option A is incorrect: The spinal trigeminal nucleus mediates facial pain and temperature, not fine touch.\n• Option C is incorrect: The mesencephalic nucleus conveys proprioception.\n• Option D is incorrect: The trigeminal motor nucleus innervates muscles of mastication.\n• Option E is incorrect: Nucleus ambiguus provides branchiomotor innervation to CN IX, X, XI."
    },
    {
        "id": "IH_Q117",
        "question_number": 117,
        "category": "In House: Trigeminal Somatosensory Pathway",
        "stem": "During a neurological examination, the physician gently touches the right cornea of an unconscious patient with a wisp of sterile cotton. The patient immediately blinks with both the right and left eyes (normal direct and consensual corneal reflex). What cranial nerves and central brainstem connections mediate the afferent and efferent limbs of this reflex?",
        "options": [
            {"text": "Afferent: Optic nerve (CN II); Efferent: Oculomotor nerve (CN III)", "is_correct": False},
            {"text": "Afferent: Ophthalmic division of Trigeminal nerve (CN V1); Efferent: Facial nerve (CN VII) bilateral orbicularis oculi innervation", "is_correct": True},
            {"text": "Afferent: Maxillary division of Trigeminal nerve (CN V2); Efferent: Abducens nerve (CN VI)", "is_correct": False},
            {"text": "Afferent: Facial nerve (CN VII); Efferent: Trigeminal nerve (CN V3)", "is_correct": False},
            {"text": "Afferent: Vestibulocochlear nerve (CN VIII); Efferent: Trochlear nerve (CN IV)", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. Afferent: Ophthalmic division of Trigeminal nerve (CN V1); Efferent: Facial nerve (CN VII) bilateral orbicularis oculi innervation.\n\nThe corneal reflex tests the integrity of both the trigeminal and facial cranial nerves as well as the brainstem:\n1. Afferent Limb: Free nerve endings in the cornea transmit sensory signals via the nasociliary branch of the Ophthalmic division of the Trigeminal nerve (CN V1). Fibers enter the mid-pons and descend to synapse in the spinal trigeminal nucleus (and principal sensory nucleus).\n2. Central Connections: Interneurons in the trigeminal sensory nuclei project BILATERALLY via the reticular formation to the motor nuclei of the Facial nerve (CN VII) in the caudal pontine tegmentum.\n3. Efferent Limb: Lower motor neurons of the Facial nerve (CN VII) travel via the temporal and zygomatic branches to innervate the Orbicularis Oculi muscles bilaterally, producing simultaneous contraction of the stimulated eye (direct blink) and the opposite eye (consensual blink).\n\n• Option A is incorrect: CN II and CN III mediate the pupillary light reflex, not the corneal touch reflex.\n• Option C is incorrect: The cornea is innervated by V1 (ophthalmic), not V2 (maxillary), and CN VI abducts the eye.\n• Option D is incorrect: Trigeminal is afferent and facial is efferent, not vice versa.\n• Option E is incorrect: CN VIII and CN IV do not mediate the corneal blink reflex."
    },
    {
        "id": "IH_Q118",
        "question_number": 118,
        "category": "In House: Trigeminal Somatosensory Pathway",
        "stem": "A neurologist taps the chin of a 72-year-old patient with a reflex hammer while the patient's mouth is held slightly open. The patient exhibits an exaggerated, brisk, clonus-like upward snap of the mandible (hyperactive jaw-jerk reflex). What unique anatomical feature distinguishes the primary afferent neurons of this reflex from all other primary somatic sensory neurons in the human body, and what does a hyperactive reflex indicate?",
        "options": [
            {"text": "Their cell bodies reside inside the central nervous system within the Mesencephalic Trigeminal Nucleus; a hyperactive reflex indicates a bilateral Upper Motor Neuron lesion above the mid-pons", "is_correct": True},
            {"text": "Their cell bodies reside in the sympathetic chain ganglia; indicates peripheral trigeminal nerve transection", "is_correct": False},
            {"text": "Their axons do not utilize myelin sheaths; indicates acute myasthenia gravis", "is_correct": False},
            {"text": "Their dendrites lack mechanoreceptors; indicates cerebellar hemisphere infarct", "is_correct": False},
            {"text": "They synapse directly in the cerebral cortex without thalamic relay; indicates normal aging", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Their cell bodies reside inside the central nervous system within the Mesencephalic Trigeminal Nucleus; a hyperactive reflex indicates a bilateral Upper Motor Neuron lesion above the mid-pons.\n\nThe jaw-jerk (masseter) reflex is a monosynaptic stretch reflex of the trigeminal system:\n1. Anatomical Uniqueness: In all other sensory pathways, primary sensory pseudounipolar cell bodies are located in peripheral ganglia (DRG or cranial nerve ganglia like the trigeminal/Gasserian ganglion). The Mesencephalic Trigeminal Nucleus is the SOLE exception in the entire nervous system: it consists of primary sensory pseudounipolar cell bodies that failed to migrate out into the periphery during neural crest development, remaining embedded INSIDE the CNS in the lateral midbrain tegmentum. They receive muscle spindle proprioceptive inputs from the masseter and temporalis muscles.\n2. Reflex Arc: The central processes of these mesencephalic neurons project directly and monosynaptically to the Trigeminal Motor Nucleus in the mid-pons, which sends motor axons via CN V3 to contract the masseter muscle.\n3. Clinical Significance: The normal jaw-jerk reflex is minimal or absent. A brisk, hyperactive jaw jerk is a definitive Upper Motor Neuron (UMN) sign indicating bilateral disruption of descending corticobulbar inhibitory fibers located ABOVE the mid-pons (e.g., pseudobulbar palsy, ALS, bilateral internal capsule strokes, or multiple sclerosis).\n\n• Options B, C, D, and E represent incorrect anatomical descriptions and clinical interpretations."
    },
    {
        "id": "IH_Q119",
        "question_number": 119,
        "category": "In House: Pain Mechanisms & Sensitization",
        "stem": "A 54-year-old woman is evaluated in a specialized pain clinic 4 months after suffering a severe scaphoid and radial head fracture that has radiographically healed. Despite normal bone alignment, she complains of severe, burning, throbbing pain in her right hand. When the examiner lightly brushes the skin of her dorsal hand with a soft camel-hair paintbrush, she wincing in agony and pulls her hand away, describing the light brush as feeling like a blowtorch. What neurobiological term defines this perception of an innocuous, non-noxious stimulus as severe pain, and what underlying central mechanism is responsible?",
        "options": [
            {"text": "Hyperpathia; loss of peripheral unmyelinated C fibers", "is_correct": False},
            {"text": "Allodynia; central sensitization involving dorsal horn NMDA receptor activation ('wind-up') and recruitment of low-threshold A-beta mechanoreceptor inputs into nociceptive pain-signaling pathways", "is_correct": True},
            {"text": "Hyperalgesia; decreased synthesis of dynorphin in the raphe nuclei", "is_correct": False},
            {"text": "Paresthesia; focal demyelination of motor axons in the carpal tunnel", "is_correct": False},
            {"text": "Anesthesia dolorosa; surgical transection of the thalamic reticular nucleus", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. Allodynia; central sensitization involving dorsal horn NMDA receptor activation ('wind-up') and recruitment of low-threshold A-beta mechanoreceptor inputs into nociceptive pain-signaling pathways.\n\nPain neurobiology recognizes key distinctions in altered sensory processing:\n1. Allodynia: The perception of pain evoked by an ordinarily innocuous, non-painful stimulus (such as a light touch with cotton, gentle brushing, clothing, or a light breeze). In healthy conditions, light touch is transmitted by low-threshold myelinated A-beta fibers to non-pain circuits. Following tissue injury, chronic inflammation, or nerve damage, repetitive C-fiber firing releases glutamate and substance P in the spinal dorsal horn, removing the Mg2+ block from postsynaptic NMDA receptors. This induces 'central sensitization' (long-term potentiation of dorsal horn wide dynamic range [WDR] neurons). Due to this heightened excitability and sprouting, low-threshold A-beta touch inputs now directly excite nociceptive projection neurons, resulting in light touch being perceived as excruciating pain (Allodynia).\n2. Hyperalgesia: An exaggerated, prolonged painful response to a stimulus that is normally painful (e.g., a mild pinprick feels like a deep stab wound).\n3. Paresthesia: An abnormal spontaneous sensation (tingling, pins-and-needles) that is not inherently painful.\n4. Dysesthesia: An unpleasant, abnormal sensation (burning, electric shocks), either spontaneous or evoked.\n\n• Option A is incorrect: Hyperpathia is an abnormally painful reaction to a repetitive stimulus, often with raised threshold.\n• Option C is incorrect: Hyperalgesia refers to increased sensitivity to already painful stimuli, not light touch.\n• Option D is incorrect: Paresthesia is non-painful tingling.\n• Option E is incorrect: Anesthesia dolorosa is pain in an area that is completely numb to all sensation."
    },
    {
        "id": "IH_Q120",
        "question_number": 120,
        "category": "In House: Spinal Cord & Neuropathies",
        "stem": "A 48-year-old man presents with progressive numbness in both feet, difficulty walking in the dark, and erectile dysfunction. On examination, he has absent ankle and knee reflexes, impaired vibratory sensation at the toes and ankles, and a broad-based, unsteady gait where he forcefully slaps his feet against the floor with each step ('stamping gait'). Serum RPR and VDRL are positive, and CSF VDRL is reactive. Which anatomical structures are selectively degenerated in Tabes Dorsalis, and how does it differ from Vitamin B12 deficiency (Subacute Combined Degeneration)?",
        "options": [
            {"text": "Tabes dorsalis causes demyelination of the anterior horn cells; B12 deficiency affects the cerebral cortex", "is_correct": False},
            {"text": "Tabes dorsalis selectively destroys the large-diameter sensory fibers of the dorsal roots and dorsal columns (fasciculus gracilis), causing sensory ataxia with absent reflexes (hyporeflexia); Vitamin B12 deficiency destroys the dorsal columns PLUS the lateral corticospinal tracts, causing sensory ataxia accompanied by upper motor neuron signs (spasticity, hyperreflexia, extensor plantars)", "is_correct": True},
            {"text": "Tabes dorsalis destroys the lateral spinothalamic tracts bilaterally; B12 deficiency selectively destroys the autonomic sympathetic chain", "is_correct": False},
            {"text": "Both conditions present with identical spastic paraparesis, hyperreflexia, and clonus", "is_correct": False},
            {"text": "Tabes dorsalis is characterized by microcytic hypochromic anemia, while B12 deficiency causes normocytic anemia", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. Tabes dorsalis selectively destroys the large-diameter sensory fibers of the dorsal roots and dorsal columns (fasciculus gracilis), causing sensory ataxia with absent reflexes (hyporeflexia); Vitamin B12 deficiency destroys the dorsal columns PLUS the lateral corticospinal tracts, causing sensory ataxia accompanied by upper motor neuron signs (spasticity, hyperreflexia, extensor plantars).\n\nDifferentiating neurosyphilitic Tabes Dorsalis from Vitamin B12 deficiency (Subacute Combined Degeneration, SCD) is a fundamental board topic:\n1. Tabes Dorsalis (Tertiary Syphilis): Treponema pallidum causes chronic dorsal root ganglionitis with selective degeneration and demyelination of the dorsal roots and dorsal columns (primarily fasciculus gracilis, producing 'locomotor ataxia'). Because sensory afferent reflex arcs are interrupted, patients display: absent deep tendon reflexes (hyporeflexia/areflexia), sensory ataxia with a high-stepping/stamping gait (slapping feet to generate auditory cues), positive Romberg sign, impaired vibration/proprioception, lancinating 'lightning' pains, and Argyll Robertson pupils. Motor strength and corticospinal tracts are INTACT.\n2. Subacute Combined Degeneration (Vitamin B12 deficiency): Demyelination affects TWO major tracts: (a) Dorsal columns (causing vibratory/proprioceptive loss and sensory ataxia, identical to tabes), AND (b) Lateral corticospinal tracts (causing spastic paraparesis, hyperreflexia, and positive Babinski sign). The presence of Upper Motor Neuron (UMN) signs (spasticity, brisk knee jerks, extensor plantars) definitively distinguishes B12 deficiency from Tabes dorsalis. In addition, B12 deficiency causes megaloblastic macrocytic anemia with hypersegmented neutrophils.\n\n• Options A, C, D, and E represent incorrect tract distributions and clinical signs."
    },

    # ==========================================
    # RADICULOPATHIES, NEUROPATHIES & EMG/NCS
    # ==========================================
    {
        "id": "IH_Q121",
        "question_number": 121,
        "category": "In House: Radiculopathies & Spine",
        "stem": "A 33-year-old construction worker experiences acute lower back pain while lifting a heavy crate. The pain radiates down the posterolateral aspect of his left thigh and calf, extending into the lateral border of his left foot and fifth toe. On examination, he has sensory loss along the lateral aspect of the foot and sole. Strength testing reveals weakness of foot plantarflexion (gastrocnemius/soleus complex, difficulty walking on toes). The left Achilles tendon reflex (ankle jerk) is completely absent, while the patellar reflex is 2+ and symmetric. Which spinal nerve root is compressed, and which intervertebral disc is most likely herniated?",
        "options": [
            {"text": "L4 nerve root; L3-L4 disc herniation", "is_correct": False},
            {"text": "L5 nerve root; L4-L5 disc herniation", "is_correct": False},
            {"text": "S1 nerve root; L5-S1 posterolateral disc herniation", "is_correct": True},
            {"text": "S2 nerve root; S1-S2 disc herniation", "is_correct": False},
            {"text": "C7 nerve root; C6-C7 disc herniation", "is_correct": False}
        ],
        "explanation": "Correct Answer: C. S1 nerve root; L5-S1 posterolateral disc herniation.\n\nIn the lumbar spine, nerve roots exit BELOW their correspondingly numbered vertebrae (e.g., L4 root exits beneath L4 vertebra). However, because lumbar roots cross the intervertebral disc space before exiting through the neural foramen, a typical posterolateral disc herniation compresses the traversing nerve root (the root of the vertebra BELOW the disc). Therefore, an L5-S1 posterolateral disc herniation compresses the traversing S1 nerve root:\n1. S1 Radiculopathy Hallmarks:\n   - Pain/Sensory loss: Radiates down posterior thigh/calf to the lateral foot, sole, and 5th digit.\n   - Motor weakness: Plantarflexion of the foot and toes (gastrocnemius/soleus complex; inability to walk on tiptoes).\n   - Reflex: Diminished or absent Achilles tendon reflex (ankle jerk, mediated by S1/S2).\n2. Contrast with L5 Radiculopathy (L4-L5 herniation):\n   - Pain/Sensory loss: Radiates down lateral calf to the dorsum of the foot and great toe.\n   - Motor weakness: Foot dorsiflexion and great toe extension (extensor hallucis longus, tibialis anterior; difficulty walking on heels).\n   - Reflex: No easily elicited reflex (normal Achilles reflex).\n3. Contrast with L4 Radiculopathy (L3-L4 herniation):\n   - Pain/Sensory loss: Anterior thigh and medial leg.\n   - Motor weakness: Knee extension (quadriceps).\n   - Reflex: Diminished patellar tendon reflex (knee jerk, mediated by L3/L4).\n\n• Options A, B, D, and E represent incorrect root, motor, and reflex correlations."
    },
    {
        "id": "IH_Q122",
        "question_number": 122,
        "category": "In House: Radiculopathies & Spine",
        "stem": "A 45-year-old office worker presents with neck pain radiating into his right shoulder, lateral forearm, and into the thumb and index finger. Neurological examination reveals reduced pinprick and vibratory sensation over the right thumb and lateral forearm. Strength testing demonstrates 3/5 weakness of elbow flexion and wrist extension. The right biceps and brachioradialis reflexes are absent (0), while the right triceps reflex is 2+. Compression of which spinal nerve root is responsible for these findings?",
        "options": [
            {"text": "C5 nerve root", "is_correct": False},
            {"text": "C6 nerve root", "is_correct": True},
            {"text": "C7 nerve root", "is_correct": False},
            {"text": "C8 nerve root", "is_correct": False},
            {"text": "T1 nerve root", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. C6 nerve root.\n\nIn the cervical spine, there are 8 cervical spinal nerves but only 7 cervical vertebrae; spinal roots C1 through C7 exit ABOVE their correspondingly numbered vertebrae (e.g., C6 root exits between C5 and C6 vertebrae), while root C8 exits between C7 and T1. A C5-C6 disc herniation compresses the C6 root:\n1. C6 Radiculopathy Hallmarks:\n   - Pain/Sensory loss: Neck/shoulder radiating down the lateral arm, lateral forearm, and into the THUMB and index finger (dermatome C6).\n   - Motor weakness: Biceps brachii (elbow flexion) and wrist extensors (extensor carpi radialis longus/brevis).\n   - Reflex: Diminished or absent Biceps and Brachioradialis reflexes (mediated by C5-C6).\n2. Contrast with C7 Radiculopathy (C6-C7 herniation):\n   - Sensory loss: Middle finger (digit 3).\n   - Motor weakness: Triceps (elbow extension), wrist flexors, finger extensors.\n   - Reflex: Diminished Triceps reflex (mediated by C7-C8).\n3. Contrast with C8 Radiculopathy (C7-T1 herniation):\n   - Sensory loss: Medial forearm, ring finger, and little finger (digits 4 and 5).\n   - Motor weakness: Finger flexors and intrinsic hand muscles (interossei).\n   - Reflex: Finger flexor reflex.\n\n• Options A, C, D, and E do not match the thumb sensory loss, wrist extensor weakness, and biceps/brachioradialis reflex loss."
    },
    {
        "id": "IH_Q123",
        "question_number": 123,
        "category": "In House: Neuropathies & Electrodiagnosis",
        "stem": "A 52-year-old woman presents with numbness, tingling, and burning pain in her right hand that frequently awakens her at night. Physical examination reveals sensory loss localized to the palmar surfaces of digits 1, 2, 3, and the radial half of digit 4, with complete sparing of the hypothenar eminence and digit 5. Tapping over the volar wrist reproduces electric sensations into the thumb and index finger (positive Tinel sign), and flexing the wrists for 60 seconds reproduces her symptoms (positive Phalen test). How does the sensory distribution of this median nerve entrapment (carpal tunnel syndrome) differentiate it from a C6 radiculopathy?",
        "options": [
            {"text": "Carpal tunnel syndrome affects the entire lateral forearm up to the biceps, while C6 radiculopathy is confined to the fingers", "is_correct": False},
            {"text": "Carpal tunnel syndrome affects the palmar aspect of the first 3.5 digits while sparing the thenar eminence (palmar cutaneous branch exits proximal to the carpal tunnel) and sparing the forearm; C6 radiculopathy involves the entire C6 dermatome (lateral arm, lateral forearm, and thumb) and causes a depressed biceps/brachioradialis reflex", "is_correct": True},
            {"text": "Carpal tunnel syndrome causes an absent triceps reflex, while C6 radiculopathy does not", "is_correct": False},
            {"text": "Both conditions cause identical forearm sensory loss and absent Achilles reflexes", "is_correct": False},
            {"text": "Carpal tunnel syndrome causes weakness of elbow extension, while C6 radiculopathy causes wrist drop", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. Carpal tunnel syndrome affects the palmar aspect of the first 3.5 digits while sparing the thenar eminence (palmar cutaneous branch exits proximal to the carpal tunnel) and sparing the forearm; C6 radiculopathy involves the entire C6 dermatome (lateral arm, lateral forearm, and thumb) and causes a depressed biceps/brachioradialis reflex.\n\nDistinguishing peripheral mononeuropathy from spinal radiculopathy is essential in clinical neurology:\n1. Carpal Tunnel Syndrome (Median Nerve Entrapment at Flexor Retinaculum):\n   - Sensory loss: Confined strictly to the peripheral cutaneous territory of the median nerve in the hand: palmar surface of digits 1, 2, 3, and the radial half of digit 4. Crucially, sensation over the proximal thenar eminence is SPARED because the palmar cutaneous branch of the median nerve branches proximal to the flexor retinaculum and travels superficially above the carpal tunnel. Sensation on the forearm is completely normal. Deep tendon reflexes are unaffected.\n2. C6 Radiculopathy (Cervical Nerve Root Compression):\n   - Sensory loss: Follows the C6 DERMATOME: extends along the lateral aspect of the arm, lateral forearm, and thumb. Sensation over the forearm IS abnormal. Motor weakness involves elbow flexors (biceps) and wrist extensors. The biceps and brachioradialis reflexes are characteristically depressed or absent.\n\n• Options A, C, D, and E represent incorrect anatomical and reflex distributions."
    },
    {
        "id": "IH_Q124",
        "question_number": 124,
        "category": "In House: Neuropathies & Electrodiagnosis",
        "stem": "A neurologist performs Nerve Conduction Studies (NCS) and Electromyography (EMG) on two patients with muscle weakness. Patient A exhibits markedly prolonged distal latencies, dramatically slowed Nerve Conduction Velocities (NCV < 30 m/s; normal > 50 m/s), and conduction block across the elbow. Patient B exhibits normal NCV and normal distal latencies, but severely reduced Compound Muscle Action Potential (CMAP) and Sensory Nerve Action Potential (SNAP) amplitudes. On needle EMG, Patient B displays abundant fibrillations and positive sharp waves at rest. What pathological processes differentiate Patient A from Patient B?",
        "options": [
            {"text": "Patient A has an axonal neuropathy; Patient B has a demyelinating neuropathy", "is_correct": False},
            {"text": "Patient A has a demyelinating neuropathy (pathology of Schwann cells/myelin causing slowed saltatory conduction and conduction block); Patient B has an axonal neuropathy (loss/degeneration of axons causing reduced response amplitudes and denervation fibrillations on EMG)", "is_correct": True},
            {"text": "Patient A has myasthenia gravis; Patient B has botulism", "is_correct": False},
            {"text": "Both patients have primary muscle disease (polymyositis)", "is_correct": False},
            {"text": "Patient A has upper motor neuron disease; Patient B has neuromuscular junction fatigue", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. Patient A has a demyelinating neuropathy (pathology of Schwann cells/myelin causing slowed saltatory conduction and conduction block); Patient B has an axonal neuropathy (loss/degeneration of axons causing reduced response amplitudes and denervation fibrillations on EMG).\n\nElectrodiagnosis cleanly differentiates demyelinating from axonal neuropathies:\n1. Demyelinating Neuropathy (e.g., Guillain-Barré syndrome / AIDP, Charcot-Marie-Tooth 1, CIDP):\n   - Primary defect: Loss or disruption of myelin sheaths surrounding intact axons.\n   - NCS findings: Marked SLOWING of conduction velocity (<70–80% of lower limit of normal), markedly prolonged distal latencies, prolonged F-wave latencies, temporal dispersion, and CONDUCTION BLOCK (a significant drop in CMAP amplitude when stimulating proximally compared to distally due to focal failure of saltatory conduction).\n2. Axonal Neuropathy (e.g., diabetic distal symmetric polyneuropathy, toxic/chemotherapy-induced neuropathy, Charcot-Marie-Tooth 2):\n   - Primary defect: Degeneration and dropout of individual axon cylinders.\n   - NCS findings: Marked REDUCTION in CMAP and SNAP AMPLITUDES (proportional to the number of lost axons); conduction velocity and distal latencies remain normal or only mildly slowed in the surviving intact axons.\n   - Needle EMG: Displays active denervation potentials at rest: FIBRILLATIONS and POSITIVE SHARP WAVES (spontaneous action potentials of individual denervated muscle fibers that have become hypersensitive to acetylcholine following loss of lower motor neuron axon innervation).\n\n• Option A is incorrect: It reverses the classic electrodiagnostic definitions.\n• Option C is incorrect: NMJ disorders are tested with repetitive stimulation, not standard NCS conduction velocity slowing.\n• Option D is incorrect: Myopathies show small, short-duration, polyphasic motor unit potentials on EMG with normal sensory NCS.\n• Option E is incorrect: UMN lesions have normal NCS and normal EMG without fibrillations."
    },
    {
        "id": "IH_Q125",
        "question_number": 125,
        "category": "In House: Neuropathies & Electrodiagnosis",
        "stem": "On a needle electromyography (EMG) examination, what physiological and structural differences distinguish 'fibrillations' from 'fasciculations'?",
        "options": [
            {"text": "Fasciculations represent spontaneous firing of single denervated muscle fibers that are invisible to the naked eye; fibrillations are twitches of entire motor units visible on the skin", "is_correct": False},
            {"text": "Fibrillations represent spontaneous, rhythmic action potentials of single isolated denervated muscle fibers (invisible to the naked eye, detected only by needle EMG); fasciculations represent spontaneous, involuntary discharges of an entire motor unit (an alpha motor neuron and all its innervated muscle fibers) that produce visible twitches beneath the skin", "is_correct": True},
            {"text": "Fibrillations occur only in central nervous system lesions; fasciculations occur only in sensory nerve roots", "is_correct": False},
            {"text": "Both represent synchronized contractions of entire muscle bellies triggered by cardiac pacemakers", "is_correct": False},
            {"text": "Fibrillations are recorded with surface electrodes; fasciculations can only be recorded with intracranial depth electrodes", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. Fibrillations represent spontaneous, rhythmic action potentials of single isolated denervated muscle fibers (invisible to the naked eye, detected only by needle EMG); fasciculations represent spontaneous, involuntary discharges of an entire motor unit (an alpha motor neuron and all its innervated muscle fibers) that produce visible twitches beneath the skin.\n\nDifferentiating spontaneous muscle discharges is a favorite high-yield distinction:\n1. Fibrillations (and Positive Sharp Waves):\n   - Origin: Individual single muscle fibers.\n   - Mechanism: When an axon degenerates, the denervated muscle fiber becomes unstable and develops acetylcholine hypersensitivity across its entire sarcolemma, spontaneously firing regular action potentials (1–50 Hz).\n   - Clinical visibility: Completely INVISIBLE to the naked eye beneath intact skin (too small to move skin). Detected exclusively as spontaneous electrical activity on needle EMG.\n   - Clinical meaning: Definitive evidence of active, ongoing lower motor neuron axonal denervation or severe necrotizing myopathy.\n2. Fasciculations:\n   - Origin: An entire MOTOR UNIT (one lower motor neuron cell body or axon and the hundreds of muscle fibers it innervates).\n   - Mechanism: Spontaneous, irregular depolarizing discharge of a sick or irritable lower motor neuron soma or proximal axon, synchronously activating all muscle fibers in that unit.\n   - Clinical visibility: VISIBLE beneath the skin as brief, spontaneous, coarse, flickering muscle twitches (without moving the joint).\n   - Clinical meaning: Seen in ALS, progressive spinal muscular atrophy, radiculopathy, as well as benign states (fatigue, caffeine, anxiety).\n\n• Options A, C, D, and E represent incorrect electrophysiological definitions."
    }
]

questions_section3.extend([
    {'category': 'In House: Radiculopathies & Neuropathies',
 'explanation': 'Correct Answer: B. Common fibular (peroneal) nerve at the fibular neck; the tibialis posterior muscle '
                '(responsible for foot inversion) is innervated by the tibial nerve (L5 root), so intact inversion '
                'confirms a peripheral fibular nerve lesion rather than an L5 radiculopathy (which would impair both '
                'dorsiflexion AND inversion).\n'
                '\n'
                'Differentiating a Common Fibular (Peroneal) Neuropathy from an L5 Radiculopathy is one of the '
                'highest-yield clinical pearls in neurology:\n'
                '1. Common Fibular Nerve Compression: The nerve winds superficially around the lateral aspect of the '
                'fibular neck, making it exceptionally vulnerable to trauma, tight casts, or prolonged leg crossing. '
                'It bifurcates into:\n'
                '   - Deep fibular nerve: innervates foot dorsiflexors (tibialis anterior, extensor digitorum longus, '
                'extensor hallucis longus) and provides sensation to the first dorsal web space between toes 1 and 2.\n'
                '   - Superficial fibular nerve: innervates foot everters (fibularis longus and brevis) and provides '
                'sensation to the anterolateral lower leg and dorsum of the foot.\n'
                "   Consequently, damage at the fibular neck causes 'foot drop', loss of dorsiflexion, loss of "
                'eversion, and numbness over the lateral leg and foot dorsum.\n'
                '2. The Key Differentiating Maneuver: FOOT INVERSION. Foot inversion is driven primarily by the '
                'Tibialis Posterior muscle. The tibialis posterior is innervated by the TIBIAL NERVE (not the fibular '
                'nerve), although its roots are L4-L5. Therefore:\n'
                '   - In Common Fibular Neuropathy: Foot inversion is completely PRESERVED.\n'
                '   - In L5 Radiculopathy: Foot inversion is IMPAIRED (along with dorsiflexion, eversion, and hip '
                'abduction via gluteus medius).\n'
                '\n'
                '• Options A, C, D, and E represent incorrect nerve localizations and muscle mechanics.',
 'id': 'IH_Q126_sec3',
 'id_clean': 'IH_Q141',
 'options': [{'is_correct': False,
              'text': 'Tibial nerve at the popliteal fossa; tibial nerve innervates the gastrocnemius'},
             {'is_correct': True,
              'text': 'Common fibular (peroneal) nerve at the fibular neck; the tibialis posterior muscle (responsible '
                      'for foot inversion) is innervated by the tibial nerve (L5 root), so intact inversion confirms a '
                      'peripheral fibular nerve lesion rather than an L5 radiculopathy (which would impair both '
                      'dorsiflexion AND inversion)'},
             {'is_correct': False,
              'text': 'Femoral nerve at the inguinal canal; femoral nerve controls the patellar reflex'},
             {'is_correct': False,
              'text': 'Obturator nerve in the obturator canal; obturator nerve controls hip adduction'},
             {'is_correct': False, 'text': 'Superficial fibular nerve in the foot; deep fibular nerve is spared'}],
 'question_number': 141,
 'stem': 'A 45-year-old man trips and falls while running, striking his right knee against a concrete curb. He '
         'presents with an inability to lift his right foot (foot drop) and drags his toes while walking, adopting an '
         "exaggerated high-stepping gait ('steppage gait') to prevent his foot from catching the ground. On "
         'examination, he has weakness of right foot dorsiflexion and foot eversion. Inversion of the foot (tibialis '
         'posterior) is completely intact. Sensory testing reveals numbness over the anterolateral lower leg and the '
         'dorsum of the foot. Where is the lesion located, and how does intact foot inversion distinguish this nerve '
         'injury from an L5 radiculopathy?'},
    {'category': 'In House: Trigeminal Somatosensory Pathway',
 'explanation': 'Correct Answer: B. Trigeminal Neuralgia (Tic Douloureux); Superior Cerebellar Artery (SCA); '
                'first-line medical therapy is Carbamazepine.\n'
                '\n'
                'Trigeminal Neuralgia (Tic Douloureux) is a classic cranial nerve disorder:\n'
                '1. Presentation: Paroxysmal, intense, stabbing, electric shock-like, unilateral facial pain '
                'restricted to one or more divisions of CN V (most commonly V2 [maxillary] or V3 [mandibular]; V1 is '
                'involved in <5%). Attacks last from seconds to 2 minutes. The pain is triggered by innocuous '
                "mechanical stimuli on cutaneous 'trigger zones' (shaving, washing face, chewing, talking, brushing "
                'teeth). Physical and sensory examinations are strictly normal.\n'
                '2. Pathophysiology: Pulsatile neurovascular compression of the trigeminal sensory nerve root at its '
                'root entry zone into the pons—most commonly by an aberrant loop of the Superior Cerebellar Artery '
                "(SCA, in ~75-80% of cases)—causes focal demyelination, ephaptic cross-talk ('short-circuiting') "
                'between non-noxious A-beta fibers and nociceptive pain fibers, and central sensitization of the '
                'spinal trigeminal nucleus.\n'
                '3. First-line Medical Treatment: Carbamazepine (or oxcarbazepine). It inhibits voltage-gated sodium '
                'channels, reducing repetitive high-frequency neuronal firing. Patients must be monitored for side '
                'effects: agranulocytosis/aplastic anemia, hyponatremia (SIADH), ataxia, hepatotoxicity, and '
                'Stevens-Johnson syndrome (especially in patients with the HLA-B*1502 allele).\n'
                '4. Surgical Treatment: Microvascular decompression (Jannetta procedure), moving the offending '
                'arterial loop away from the nerve with a Teflon felt spacer.\n'
                '\n'
                '• Option A is incorrect: Atypical facial pain is constant and burning.\n'
                '• Option C is incorrect: Postherpetic neuralgia follows a dermatomal zoster rash.\n'
                '• Option D is incorrect: Cluster headache features autonomic symptoms (rhinorrhea, lacrimation).\n'
                '• Option E is incorrect: GCA features elevated ESR and jaw claudication in patients >50.',
 'id': 'IH_Q142',
 'options': [{'is_correct': False, 'text': 'Atypical facial pain; basilar artery; treat with high-dose prednisone'},
             {'is_correct': True,
              'text': 'Trigeminal Neuralgia (Tic Douloureux); Superior Cerebellar Artery (SCA); first-line medical '
                      'therapy is Carbamazepine'},
             {'is_correct': False,
              'text': 'Postherpetic neuralgia; posterior inferior cerebellar artery; treat with acyclovir'},
             {'is_correct': False, 'text': 'Cluster headache; internal carotid artery; treat with verapamil'},
             {'is_correct': False,
              'text': 'Giant cell arteritis; superficial temporal artery; treat with methotrexate'}],
 'question_number': 142,
 'stem': 'A 58-year-old woman presents with paroxysms of excruciating, sharp, electric-shock-like pain shooting across '
         'her right cheek and upper jaw. Each attack lasts only 5 to 15 seconds, but recurs hundreds of times a day. '
         'Attacks are triggered by trivial mechanical stimuli such as brushing her teeth, applying makeup, chewing, or '
         'even a light breeze against her cheek. Neurological examination reveals no sensory deficits or cranial nerve '
         'abnormalities between attacks. High-resolution brain MRI with constructive interference in steady-state '
         '(CISS) sequences reveals neurovascular compression of the right trigeminal nerve root entry zone by an '
         'aberrant arterial loop. What is the diagnosis, what vessel is most commonly implicated, and what is the '
         'first-line medical therapy?'},
    {'category': 'In House: Pain Mechanisms & Sensitization',
 'explanation': 'Correct Answer: B. They activate enkephalinergic inhibitory interneurons that release endogenous '
                'opioids (enkephalins) to presynaptically inhibit calcium influx and neurotransmitter release from '
                'primary afferents, and postsynaptically hyperpolarize second-order spinothalamic projection neurons.\n'
                '\n'
                'The Descending Pain Modulatory System provides powerful endogenous analgesia:\n'
                '1. Brainstem Centers: The Periaqueductal Gray (PAG) in the midbrain integrates inputs from the '
                'amygdala, hypothalamus, and frontal cortex. PAG neurons project to the Rostral Ventromedial Medulla '
                '(RVM, primarily the Nucleus Raphe Magnus) and the Locus Coeruleus.\n'
                '2. Descending Tracts: Serotonergic axons from the nucleus raphe magnus and noradrenergic axons from '
                'the locus coeruleus descend in the dorsolateral funiculus of the spinal cord to terminate in the '
                'superficial dorsal horn (substantia gelatinosa, lamina II).\n'
                '3. Spinal Mechanism: These descending projections synapse on local Enkephalinergic Inhibitory '
                'Interneurons, stimulating them to release endogenous opioid peptides (Met-enkephalin, '
                'Leu-enkephalin). Enkephalins bind to presynaptic and postsynaptic mu- and delta-opioid receptors:\n'
                '   - Presynaptically: Close voltage-gated Ca2+ channels on incoming primary nociceptive C-fiber '
                'terminals, inhibiting release of glutamate, substance P, and CGRP.\n'
                '   - Postsynaptically: Open G-protein-coupled inwardly rectifying K+ channels (GIRK), hyperpolarizing '
                'second-order spinothalamic projection neurons away from firing threshold.\n'
                "This process represents the physiological basis for the 'Gate Control Theory' of pain and explains "
                'the analgesic efficacy of exogenous opioids.\n'
                '\n'
                '• Options A, C, D, and E represent incorrect cellular mechanisms.',
 'id': 'IH_Q143',
 'options': [{'is_correct': False, 'text': 'They directly stimulate substance P release from primary C-fibers'},
             {'is_correct': True,
              'text': 'They activate enkephalinergic inhibitory interneurons that release endogenous opioids '
                      '(enkephalins) to presynaptically inhibit calcium influx and neurotransmitter release from '
                      'primary afferents, and postsynaptically hyperpolarize second-order spinothalamic projection '
                      'neurons'},
             {'is_correct': False, 'text': 'They induce apoptosis of second-order spinothalamic neurons'},
             {'is_correct': False, 'text': 'They permanently destroy NMDA receptors in the spinal cord'},
             {'is_correct': False, 'text': 'They block sodium channels in the postcentral gyrus'}],
 'question_number': 143,
 'stem': 'The central nervous system possesses an intrinsic descending analgesia system capable of suppressing '
         'incoming nociceptive signals at the level of the spinal cord dorsal horn. Activation of the Periaqueductal '
         'Gray (PAG) in the midbrain leads to activation of serotonergic neurons in the Rostral Ventromedial Medulla '
         '(RVM / nucleus raphe magnus) and noradrenergic neurons in the locus coeruleus. What is the terminal '
         'mechanism in the substantia gelatinosa (lamina II) of the dorsal horn by which descending fibers inhibit '
         'nociceptive transmission?'},
    {'category': 'In House: Spinal Cord Syndromes',
 'explanation': 'Correct Answer: B. Anterior spinal artery (ASA), supplied in the lower thoracic region by the Great '
                'Radicular Artery of Adamkiewicz; infarction of the anterior two-thirds of the spinal cord (sparing '
                'the posterior columns supplied by paired posterior spinal arteries).\n'
                '\n'
                'Anterior Spinal Artery (ASA) Syndrome is a devastating complication of aortic surgery, severe '
                'hypotension, or atherosclerosis:\n'
                '1. Vascular Anatomy: The single Anterior Spinal Artery (ASA) supplies the anterior two-thirds of the '
                'spinal cord (anterior horns, lateral corticospinal tracts, anterolateral spinothalamic tracts, '
                'autonomic lateral horns). In the lower thoracic and lumbar regions, the ASA relies critically on '
                'radicular feeding vessels originating from intercostal/lumbar aortic branches, most prominently the '
                'Great Radicular Artery of Adamkiewicz (arteria radicularis magna, typically arising on the left at '
                'T9–T12). Cross-clamping or sacrificing these aortic branches during aneurysm repair causes acute '
                'spinal cord ischemia.\n'
                '2. Clinical Deficits:\n'
                '   - Bilateral loss of motor function below the lesion (paraplegia): due to bilateral lateral '
                'corticospinal tract infarction (initially flaccid with areflexia from spinal shock, evolving into '
                'spasticity with hyperreflexia and Babinski signs).\n'
                '   - Bilateral loss of pain and temperature below the lesion: due to bilateral spinothalamic tract '
                '(ALS) infarction.\n'
                '   - Autonomic dysfunction: urinary retention and bowel incontinence due to descending autonomic '
                'pathway destruction.\n'
                '3. The Definitive Dissociation (Sensory Dissociation): The POSTERIOR COLUMNS (fasciculus gracilis and '
                'cuneatus) occupy the posterior one-third of the cord and are supplied by the PAIRED POSTERIOR SPINAL '
                'ARTERIES. Therefore, vibratory sense, conscious proprioception, and fine touch are COMPLETELY '
                'PRESERVED bilaterally! This clinical picture—bilateral motor paralysis and pain/temperature loss with '
                'preserved proprioception/vibration—is pathognomonic for ASA infarction.\n'
                '\n'
                '• Option A is incorrect: Posterior spinal artery infarction would destroy proprioception and '
                'vibration while sparing motor function and pain/temp.\n'
                '• Options C, D, and E represent cerebral/brainstem vascular territories.',
 'id': 'IH_Q144',
 'options': [{'is_correct': False, 'text': 'Bilateral posterior spinal arteries; dorsal columns'},
             {'is_correct': True,
              'text': 'Anterior spinal artery (ASA), supplied in the lower thoracic region by the Great Radicular '
                      'Artery of Adamkiewicz; infarction of the anterior two-thirds of the spinal cord (sparing the '
                      'posterior columns supplied by paired posterior spinal arteries)'},
             {'is_correct': False, 'text': 'Vertebral artery thrombosis; medial medulla'},
             {'is_correct': False, 'text': 'Internal carotid artery; anterior choroidal artery territory'},
             {'is_correct': False, 'text': 'Superior cerebellar artery; pontine tegmentum'}],
 'question_number': 144,
 'stem': 'A 66-year-old man undergoes surgical repair of an extensive thoracoabdominal aortic aneurysm involving '
         'placement of a cross-clamp across the descending aorta for 45 minutes. Upon awakening from anesthesia, he is '
         'found to have complete flaccid paralysis of both lower extremities with bilateral loss of pain and '
         'temperature sensation below the T8 level, accompanied by acute urinary retention. Surprisingly, vibratory '
         'sensation, joint position sense (proprioception), and two-point discrimination remain entirely normal '
         'bilaterally in both lower extremities. What vascular territory and spinal cord structures were infarcted?'},
    {'category': 'In House: Spinal Cord Syndromes',
 'explanation': 'Correct Answer: B. Central Cord Syndrome; hyperextension forces buckle the ligamentum flavum, '
                'compressing the central cervical cord where corticospinal tract fibers destined for the upper '
                'extremities (arms/hands) are located medially, while fibers destined for the lower extremities '
                '(legs/feet) are located peripherally/laterally.\n'
                '\n'
                'Central Cord Syndrome is the most common incomplete spinal cord injury syndrome:\n'
                '1. Mechanism: Typically occurs in elderly individuals with pre-existing cervical spondylosis and '
                'canal stenosis who suffer a hyperextension neck injury (e.g., fall with forehead impact). The '
                'hyperextension pinches the cord between anterior osteophytes and the buckled posterior ligamentum '
                'flavum, creating central hemorrhagic contusion and ischemia centered around the central canal.\n'
                '2. Somatotopic Organization of the Corticospinal Tract:\n'
                '   - In the descending lateral corticospinal tract, fibers are arranged with a distinct laminated '
                'somatotopy: cervical/upper extremity fibers (hands, arms) are located MEDIALLY (centrally), while '
                'thoracic, lumbar, and sacral/lower extremity fibers (legs, feet) are located LATERAL (peripherally).\n'
                '3. Clinical Pattern: An expanding central lesion selectively disrupts the centrally located medial '
                'corticospinal fibers and central spinal gray matter (anterior horn motor neurons supplying the upper '
                'limbs), causing dense motor weakness and sensory loss in the UPPER EXTREMITIES (especially distal '
                "hands) with relative SPARING of the LOWER EXTREMITIES. Patients present with 'man-in-a-barrel' "
                'weakness (inability to lift or move arms, but able to move legs and walk).\n'
                '\n'
                '• Option A is incorrect: Brown-Séquard syndrome features hemicord deficits with contralateral pain '
                'loss and ipsilateral motor/proprioceptive loss.\n'
                '• Option C is incorrect: ASA syndrome causes dense lower extremity paraplegia.\n'
                '• Option D is incorrect: GBS causes ascending symmetric lower-to-upper paralysis.\n'
                '• Option E is incorrect: MG causes fatigable ocular/bulbar weakness.',
 'id': 'IH_Q145',
 'options': [{'is_correct': False, 'text': 'Brown-Séquard syndrome; hemisection of the lumbar cord'},
             {'is_correct': True,
              'text': 'Central Cord Syndrome; hyperextension forces buckle the ligamentum flavum, compressing the '
                      'central cervical cord where corticospinal tract fibers destined for the upper extremities '
                      '(arms/hands) are located medially, while fibers destined for the lower extremities (legs/feet) '
                      'are located peripherally/laterally'},
             {'is_correct': False,
              'text': 'Anterior spinal artery thrombosis; complete transection of the lumbar conus'},
             {'is_correct': False, 'text': 'Guillain-Barré syndrome; peripheral demyelinating polyneuropathy'},
             {'is_correct': False, 'text': 'Myasthenia gravis; postsynaptic receptor degradation'}],
 'question_number': 145,
 'stem': 'A 70-year-old man with cervical spine osteoarthritis trips and strikes his forehead against a table, causing '
         'sudden, forceful hyperextension of his neck. In the emergency department, he is alert and oriented. '
         'Neurological examination reveals severe flaccid weakness, muscle wasting, and sensory loss in both upper '
         'extremities (hands, forearms, and arms), whereas his lower extremities show only mild weakness, brisk knee '
         'reflexes, and intact sensory perception. What is the diagnosis, and why are the upper extremities affected '
         'substantially more than the lower extremities?'},
])

if __name__ == "__main__":
    print(f"Section 3 Question Count: {len(questions_section3)}")
    ids = [q["id"] for q in questions_section3]
    assert len(ids) == len(set(ids)), "Duplicate IDs found!"
    print("Section 3 validated successfully!")
