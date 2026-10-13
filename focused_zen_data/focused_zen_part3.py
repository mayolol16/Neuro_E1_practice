# focused_zen_part3.py
# 80 Board-Style USMLE Step 1 Questions directly aligned with
# "Copy of Long NeuroPsych Exam 1 Study Guide.docx"
# Topics 9-12 (20 Questions each, IDs FZ_Q161 to FZ_Q240)

focused_questions_part3 = [
    # =========================================================================
    # TOPIC 9: Pain Pathway (FZ_Q161 - FZ_Q180)
    # =========================================================================
    {
        "id": "FZ_Q161",
        "question_number": 161,
        "category": "Pain Pathway",
        "stem": "A 22-year-old chef accidentally touches a scorching hot skillet. She experiences an immediate, sharp, well-localized sensation of intense pain, followed a few seconds later by a prolonged, poorly localized, throbbing and burning ache. Which of the following nerve fiber types mediates the initial, rapid 'first pain,' and which fiber mediates the subsequent, slow 'second pain'?",
        "options": [
            {"text": "A-delta fibers mediate first pain; C fibers mediate second pain", "is_correct": True},
            {"text": "A-alpha fibers mediate first pain; A-beta fibers mediate second pain", "is_correct": False},
            {"text": "C fibers mediate first pain; A-delta fibers mediate second pain", "is_correct": False},
            {"text": "A-beta fibers mediate first pain; C fibers mediate second pain", "is_correct": False},
            {"text": "B fibers mediate first pain; A-gamma fibers mediate second pain", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. A-delta fibers mediate first pain; C fibers mediate second pain.\n\nCutaneous nociceptive pain is conveyed by two distinct populations of primary sensory afferents:\n1. A-delta fibers: Medium-diameter, thinly myelinated fibers with moderate conduction velocity (5-30 m/s). They terminate in Rexed laminae I and V of the dorsal horn and mediate fast, sharp, pricking, well-localized 'first pain' (thermal and high-threshold mechanical nociception).\n2. C fibers: Small-diameter, unmyelinated fibers with slow conduction velocity (0.5-2 m/s). They terminate in Rexed lamina II (substantia gelatinosa) and release glutamate, Substance P, and CGRP. They mediate slow, burning, dull, aching, poorly localized 'second pain' (polymodal nociceptors).\n\n• Option B is incorrect: A-alpha and A-beta fibers convey proprioception and discriminative touch, not pain."
    },
    {
        "id": "FZ_Q162",
        "question_number": 162,
        "category": "Pain Pathway",
        "stem": "Primary sensory afferent fibers conveying pain and temperature enter the spinal cord via the lateral division of the dorsal root. Before synapsing with second-order projection neurons in the dorsal horn gray matter, these axons ascend or descend 1 to 2 spinal segments within which of the following white matter tracts?",
        "options": [
            {"text": "Dorsolateral tract of Lissauer", "is_correct": True},
            {"text": "Fasciculus gracilis", "is_correct": False},
            {"text": "Fasciculus cuneatus", "is_correct": False},
            {"text": "Anterior white commissure", "is_correct": False},
            {"text": "Rubrospinal tract", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Dorsolateral tract of Lissauer.\n\nUpon entering the dorsolateral aspect of the spinal cord, central processes of primary nociceptive neurons (A-delta and C fibers) divide into ascending and descending collateral branches that run within the tract of Lissauer (dorsolateral fasciculus). They travel 1 to 2 spinal segments rostrally or caudally before penetrating the dorsal horn to synapse on second-order neurons in Rexed laminae I (marginal zone), II (substantia gelatinosa), and V (nucleus proprius).\n\n• Option D is incorrect: The anterior white commissure is where second-order spinothalamic axons decussate across the midline."
    },
    {
        "id": "FZ_Q163",
        "question_number": 163,
        "category": "Pain Pathway",
        "stem": "In the anterolateral spinothalamic system, second-order projection neurons have their cell bodies in the dorsal horn. Where do their axons decussate across the midline to reach the contralateral anterolateral funiculus?",
        "options": [
            {"text": "Anterior white commissure, crossing obliquely 1 to 2 spinal cord levels above the level of entry", "is_correct": True},
            {"text": "Posterior gray commissure at the exact segment of entry", "is_correct": False},
            {"text": "Sensory decussation of the caudal medulla", "is_correct": False},
            {"text": "Tegmentum of the rostral midbrain", "is_correct": False},
            {"text": "Pyramidal decussation of the closed medulla", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Anterior white commissure, crossing obliquely 1 to 2 spinal cord levels above the level of entry.\n\nSecond-order axons of the anterolateral system (spinothalamic tract) originate from cell bodies in the dorsal horn (Rexed laminae I and V). They course ventromedially and decussate across the midline in the Anterior White Commissure, traveling obliquely upward over 1 to 2 spinal cord segments. After crossing, they ascend in the contralateral anterolateral funiculus to the brainstem and thalamus. Because of this 1-2 segment oblique crossing, a unilateral spinal cord lesion (e.g., Brown-Séquard syndrome) results in loss of pain and temperature on the contralateral side starting 1 to 2 dermatomes BELOW the anatomical level of the lesion."
    },
    {
        "id": "FZ_Q164",
        "question_number": 164,
        "category": "Pain Pathway",
        "stem": "A 54-year-old woman with chronic diabetic peripheral neuropathy rubs her sore feet with her hands, noticing that vigorous rubbing provides temporary relief from her burning pain. According to the Gate Control Theory of Pain proposed by Melzack and Wall, which of the following mechanisms explains why mechanical touch relieves nociceptive pain?",
        "options": [
            {"text": "Activation of large, myelinated A-beta fibers stimulates inhibitory interneurons in the substantia gelatinosa, which inhibit pain transmission from A-delta and C fibers", "is_correct": True},
            {"text": "Tactile rubbing activates descending pathways from the locus coeruleus that deplete acetylcholine in the ventral horn", "is_correct": False},
            {"text": "Mechanical stimulation irreversibly destroys substance P receptors on primary nociceptors", "is_correct": False},
            {"text": "Rubbing causes immediate endocytosis of all postsynaptic AMPA and NMDA receptors", "is_correct": False},
            {"text": "Tactile input hyperpolarizes Schwann cells, preventing saltatory conduction", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Activation of large, myelinated A-beta fibers stimulates inhibitory interneurons in the substantia gelatinosa, which inhibit pain transmission from A-delta and C fibers.\n\nAccording to the Gate Control Theory of Pain (Melzack & Wall):\n• Transmission of pain from primary A-delta and C fibers to second-order spinothalamic neurons in the dorsal horn is modulated by a 'neural gate' in Rexed lamina II (substantia gelatinosa).\n• Non-painful tactile mechanical stimulation activates large-diameter, myelinated A-beta fibers.\n• Collateral branches of these A-beta fibers excite inhibitory interneurons in the substantia gelatinosa.\n• These interneurons release GABA and enkephalin, presynaptically inhibiting neurotransmitter release from C fibers and postsynaptically hyperpolarizing second-order transmission cells, effectively 'closing the gate' to pain signaling.\nThis explains why rubbing a bumped elbow, massage therapy, and transcutaneous electrical nerve stimulation (TENS) provide analgesia."
    },
    {
        "id": "FZ_Q165",
        "question_number": 165,
        "category": "Pain Pathway",
        "stem": "The central nervous system possesses an intrinsic descending analgesia system that suppresses pain transmission at the level of the spinal dorsal horn. Stimulation of neurons in the periaqueductal gray (PAG) of the midbrain activates serotonergic neurons in which of the following brainstem nuclei to project descending inhibitory axons to the substantia gelatinosa?",
        "options": [
            {"text": "Nucleus raphe magnus in the rostral ventromedial medulla", "is_correct": True},
            {"text": "Substantia nigra pars compacta", "is_correct": False},
            {"text": "Inferior olivary nucleus", "is_correct": False},
            {"text": "Abducens nucleus", "is_correct": False},
            {"text": "Edinger-Westphal nucleus", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Nucleus raphe magnus in the rostral ventromedial medulla.\n\nThe descending pain modulation circuit:\n1. Neurons in the Periaqueductal Gray (PAG) of the midbrain receive inputs from the cortex, amygdala, and hypothalamus.\n2. Excitatory projections from the PAG project to the Rostral Ventromedial Medulla (RVM), specifically targeting the Nucleus Raphe Magnus (serotonergic, 5-HT) and the Locus Coeruleus (noradrenergic, NE) in the pons.\n3. Descending axons from the Nucleus Raphe Magnus travel down the dorsolateral funiculus to the spinal cord dorsal horn.\n4. Serotonin and norepinephrine release activates local enkephalin-containing inhibitory interneurons in Rexed lamina II (substantia gelatinosa).\n5. Enkephalins bind presynaptic and postsynaptic mu-opioid receptors, blocking substance P and glutamate release and hyperpolarizing second-order projection neurons."
    },
    {
        "id": "FZ_Q166",
        "question_number": 166,
        "category": "Pain Pathway",
        "stem": "A 58-year-old man presents with acute retrosternal chest tightness radiating down the medial aspect of his left arm into his little finger. Electrocardiogram confirms acute ST-elevation myocardial infarction. The patient's left arm pain is an example of referred visceral pain. According to the convergence-projection theory, which of the following neuroanatomical mechanisms explains why myocardial ischemia is perceived as somatic pain in the T1-T4 dermatomes?",
        "options": [
            {"text": "Visceral sensory afferents from the heart and somatic sensory afferents from the left arm converge onto the same second-order spinothalamic neurons in the T1-T4 dorsal horn", "is_correct": True},
            {"text": "Myocardial ischemia releases inflammatory cytokines that travel hematogenously to the brachial plexus", "is_correct": False},
            {"text": "The phrenic nerve carries parasympathetic motor fibers directly to the pectoralis major", "is_correct": False},
            {"text": "Cervical sympathetic ganglia send motor efferents that cause spasm of the ulnar artery", "is_correct": False},
            {"text": "Cardiac pain signals decussate in the corpus callosum instead of the spinal cord", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Visceral sensory afferents from the heart and somatic sensory afferents from the left arm converge onto the same second-order spinothalamic neurons in the T1-T4 dorsal horn.\n\nAccording to the Convergence-Projection Theory of referred pain:\n• Visceral organs have sparse sensory innervation and do not have separate dedicated pathways to the primary somatosensory cortex.\n• Visceral nociceptive afferents from the heart travel along sympathetic nerves and enter the upper thoracic spinal cord (segments T1 to T4).\n• In the dorsal horn, these visceral afferents converge and synapse onto the SAME second-order spinothalamic projection neurons that receive somatic nociceptive inputs from the T1-T4 dermatomes (which correspond to the precordial chest, axilla, and medial aspect of the left arm).\n• When the cerebral cortex receives signals from these second-order neurons, it projects the sensation to the more frequently stimulated somatic dermatome (the left arm and chest)."
    },
    {
        "id": "FZ_Q167",
        "question_number": 167,
        "category": "Pain Pathway",
        "stem": "A 45-year-old woman presents with severe right upper quadrant abdominal pain and fever. Ultrasound confirms acute cholecystitis with gallstones. In addition to right upper quadrant tenderness, she reports sharp pain localized to the tip of her right shoulder and inferior angle of her right scapula (Boas sign). Inflammation of the gallbladder irritating the under-surface of the diaphragm causes referred shoulder pain via which of the following nerves?",
        "options": [
            {"text": "Right phrenic nerve (C3, C4, C5)", "is_correct": True},
            {"text": "Right vagus nerve (CN X)", "is_correct": False},
            {"text": "Right greater splanchnic nerve (T5-T9)", "is_correct": False},
            {"text": "Right lateral cutaneous nerve of the thigh (L2-L3)", "is_correct": False},
            {"text": "Right sciatic nerve (L4-S3)", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Right phrenic nerve (C3, C4, C5).\n\nReferred shoulder pain from subdiaphragmatic irritation (Kehr sign for splenic rupture, or gallbladder inflammation in acute cholecystitis) is mediated by the phrenic nerve. The diaphragm receives sensory innervation from the phrenic nerve (roots C3, C4, C5; 'C3, 4, 5 keeps the diaphragm alive'). Sensory afferents enter the cervical spinal cord at C3-C5, converging onto second-order neurons that also receive somatic sensation from the supraclavicular nerves (C3-C4 dermatome over the shoulder tip). Irritation of the diaphragmatic peritoneum is therefore perceived as pain over the ipsilateral shoulder."
    },
    {
        "id": "FZ_Q168",
        "question_number": 168,
        "category": "Pain Pathway",
        "stem": "A 35-year-old woman presents to the clinic with severe sunburn across her shoulders. When her partner lightly drapes a soft cotton shirt over her sunburned skin, she recoils in agony, perceiving the light touch as excruciatingly painful. What clinical term describes the perception of a normally innocuous, non-painful stimulus as painful?",
        "options": [
            {"text": "Allodynia", "is_correct": True},
            {"text": "Hyperalgesia", "is_correct": False},
            {"text": "Hyperpathia", "is_correct": False},
            {"text": "Paresthesia", "is_correct": False},
            {"text": "Anesthesia dolorosa", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Allodynia.\n\nKey pain terminology:\n• Allodynia: Pain resulting from a stimulus that does not normally provoke pain (e.g., light touch of clothing or a gentle breeze on sunburned skin, or touching the face in trigeminal neuralgia). It reflects sensitization of central dorsal horn neurons (central sensitization) and phenotypic switching of low-threshold A-beta mechanoreceptors.\n• Hyperalgesia: An exaggerated or increased pain response to a stimulus that is normally painful (e.g., a mild pinprick on inflamed skin feeling like a knife stab).\n• Paresthesia: An abnormal spontaneous sensation (tingling, 'pins and needles') that is not unpleasant or painful.\n• Anesthesia dolorosa: Pain perceived in an area that is completely numb and anesthetic."
    },
    {
        "id": "FZ_Q169",
        "question_number": 169,
        "category": "Pain Pathway",
        "stem": "Following tissue injury, an 'inflammatory soup' of chemical mediators is released into the interstitial fluid surrounding peripheral nociceptive nerve terminals, sensitizing them and lowering their activation thresholds (primary peripheral sensitization). Which of the following inflammatory mediators directly binds and sensitizes the TRPV1 (transient receptor potential vanilloid 1) non-selective cation channel on unmyelinated C fibers?",
        "options": [
            {"text": "Protons (extracellular H+ ions), Bradykinin, and Prostaglandin E2 (PGE2)", "is_correct": True},
            {"text": "Acetylcholine and Dopamine", "is_correct": False},
            {"text": "Gamma-aminobutyric acid (GABA)", "is_correct": False},
            {"text": "Glycine and Taurine", "is_correct": False},
            {"text": "Thyroid stimulating hormone (TSH)", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Protons (extracellular H+ ions), Bradykinin, and Prostaglandin E2 (PGE2).\n\nTissue trauma, infection, and ischemia cause damaged cells, mast cells, platelets, and macrophages to release an 'inflammatory soup':\n• Bradykinin: Binds B2 Gq receptors, activating PKC to phosphorylate and lower the activation threshold of TRPV1.\n• Prostaglandins (PGE2, PGI2): Bind EP/IP Gs receptors, activating PKA to phosphorylate Na+ channels (Nav1.8) and TRPV1.\n• Protons (H+, tissue acidosis): Directly gate and open the TRPV1 pore at physiological temperatures.\n• Histamine, Serotonin, ATP, Nerve Growth Factor (NGF), and Substance P.\nTogether, these mediators dramatically lower the threshold of heat- and mechanosensitive nociceptors, producing primary hyperalgesia at the site of injury."
    },
    {
        "id": "FZ_Q170",
        "question_number": 170,
        "category": "Pain Pathway",
        "stem": "A 58-year-old man with poorly controlled type 2 diabetes mellitus presents with burning, shooting pain in both feet that is worse at night. Physical examination reveals a symmetrical 'stocking-glove' distribution of pinprick hyperalgesia and loss of 10-g monofilament tactile sensation. The physician prescribes a topical capsaicin cream (derived from chili peppers). What is the mechanism of action by which capsaicin relieves neuropathic pain?",
        "options": [
            {"text": "Initial activation of the TRPV1 receptor leads to sustained calcium influx, causing functional desensitization and depletion of substance P from nociceptive nerve terminals", "is_correct": True},
            {"text": "Irreversible blockade of voltage-gated potassium channels", "is_correct": False},
            {"text": "Selective competitive antagonism of mu-opioid receptors", "is_correct": False},
            {"text": "Direct inhibition of cycloxygenase-2 (COX-2) in endothelial cells", "is_correct": False},
            {"text": "Allosteric enhancement of GABA-A chloride channels", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Initial activation of the TRPV1 receptor leads to sustained calcium influx, causing functional desensitization and depletion of substance P from nociceptive nerve terminals.\n\nCapsaicin is a potent, selective agonist of the TRPV1 (Transient Receptor Potential Vanilloid 1) receptor, an ionotropic non-selective cation channel normally activated by noxious heat (>43°C) and protons on C and A-delta nociceptors.\n• Initial application: Causes opening of TRPV1, influx of Na+ and Ca2+, and intense burning pain, erythema, and itching.\n• Repeated application: Chronic, excessive Ca2+ influx leads to osmotic swelling, mitochondrial dysfunction, reversible retraction of epidermal nerve terminals, and prolonged DESENSITIZATION of nociceptors, accompanied by depletion of Substance P. This provides sustained analgesia in diabetic neuropathy and post-herpetic neuralgia."
    },
    {
        "id": "FZ_Q171",
        "question_number": 171,
        "category": "Pain Pathway",
        "stem": "A 60-year-old man with painful diabetic peripheral neuropathy is evaluated in the clinic. As discussed in CBIL Case 1, diabetic polyneuropathy results from chronic hyperglycemia. Which of the following biochemical pathways is responsible for intracellular sorbitol accumulation, osmotic stress, and depletion of NADPH in peripheral nerves?",
        "options": [
            {"text": "Polyol pathway (Aldose reductase converts glucose to sorbitol, consuming NADPH)", "is_correct": True},
            {"text": "Hexosamine pathway converting fructose-6-phosphate to UDP-GlcNAc", "is_correct": False},
            {"text": "Protein kinase C pathway activated by diacylglycerol", "is_correct": False},
            {"text": "Advanced glycation end-product (AGE) formation via non-enzymatic fructosamine", "is_correct": False},
            {"text": "Glycogen synthesis via glycogen synthase", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Polyol pathway (Aldose reductase converts glucose to sorbitol, consuming NADPH).\n\nIn diabetic neuropathy (CBIL Case 1):\n• Schwann cells and peripheral axons take up glucose via insulin-independent GLUT transporters. In chronic hyperglycemia, intracellular glucose saturates hexokinase and is shunted into the Polyol pathway.\n• Aldose reductase reduces glucose to Sorbitol, consuming NADPH.\n• Sorbitol dehydrogenase slowly oxidizes sorbitol to fructose, using NAD+.\nPathological consequences:\n1. Sorbitol is polar and cannot cross cell membranes; its accumulation generates intracellular hyperosmotic stress, drawing water in and causing Schwann cell swelling.\n2. Depletion of NADPH deprives Glutathione Reductase of the reducing equivalents needed to regenerate reduced glutathione (GSH), causing severe oxidative stress and free radical damage.\n3. Advanced Glycation End-products (AGEs) cross-link extracellular matrix proteins, leading to microvascular endoneurial ischemia."
    },
    {
        "id": "FZ_Q172",
        "question_number": 172,
        "category": "Pain Pathway",
        "stem": "A 55-year-old man with diabetic polyneuropathy is evaluated for severe nocturnal neuropathic foot pain. As outlined in CBIL Case 1, which of the following oral medications is considered first-line pharmacotherapy for painful diabetic neuropathy by binding to the alpha-2-delta auxiliary subunit of presynaptic voltage-gated calcium channels, thereby reducing excitatory neurotransmitter release?",
        "options": [
            {"text": "Pregabalin (or Gabapentin)", "is_correct": True},
            {"text": "Oxycodone", "is_correct": False},
            {"text": "Ibuprofen", "is_correct": False},
            {"text": "Acetaminophen", "is_correct": False},
            {"text": "Indomethacin", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Pregabalin (or Gabapentin).\n\nGabapentinoids (Pregabalin and Gabapentin) are first-line agents for neuropathic pain (diabetic polyneuropathy, post-herpetic neuralgia). Mechanism:\n• Despite structural resemblance to GABA, they do NOT bind GABA receptors or alter GABA metabolism.\n• Instead, they bind with high affinity to the alpha-2-delta-1 (α2δ-1) auxiliary subunit of presynaptic P/Q-type and N-type voltage-gated calcium channels (VGCCs) in the dorsal horn and brain.\n• This blocks Ca2+ influx during action potentials, dampening the presynaptic exocytosis of excitatory neurotransmitters (glutamate, substance P, CGRP, and norepinephrine).\nCommon side effects: Dizziness, somnolence, peripheral edema, and weight gain."
    },
    {
        "id": "FZ_Q173",
        "question_number": 173,
        "category": "Pain Pathway",
        "stem": "A 52-year-old woman with chronic neuropathic back pain is prescribed duloxetine, a serotonin-norepinephrine reuptake inhibitor (SNRI). As outlined in the pain management curriculum, why are SNRIs and tricyclic antidepressants (TCAs) effective in alleviating chronic neuropathic pain?",
        "options": [
            {"text": "They increase synaptic concentrations of serotonin and norepinephrine in the dorsal horn, enhancing the activity of descending inhibitory pain pathways", "is_correct": True},
            {"text": "They directly block postsynaptic AMPA receptors on primary motor neurons", "is_correct": False},
            {"text": "They irreversibly acetylate cyclooxygenase enzymes in peripheral tissues", "is_correct": False},
            {"text": "They deplete intracellular calcium stores from skeletal muscle sarcoplasmic reticulum", "is_correct": False},
            {"text": "They antagonize mu-opioid receptors to prevent tolerance", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. They increase synaptic concentrations of serotonin and norepinephrine in the dorsal horn, enhancing the activity of descending inhibitory pain pathways.\n\nSNRIs (duloxetine, venlafaxine) and TCAs (amitriptyline, nortriptyline) treat neuropathic pain by blocking the reuptake of Serotonin (via SERT) and Norepinephrine (via NET). In the dorsal horn of the spinal cord, descending inhibitory pain pathways originating in the periaqueductal gray, nucleus raphe magnus, and locus coeruleus release 5-HT and NE. By increasing synaptic levels of these monoamines in Rexed lamina II (substantia gelatinosa), these drugs activate inhibitory alpha-2 adrenergic and serotonergic receptors, which stimulate enkephalinergic interneurons to suppress nociceptive transmission."
    },
    {
        "id": "FZ_Q174",
        "question_number": 174,
        "category": "Pain Pathway",
        "stem": "Ascending axons in the anterolateral system diverge to target multiple brainstem and forebrain structures. Axons of the spinoreticular and spinolimbic tracts project to the reticular formation, intralaminar thalamic nuclei, amygdala, and anterior cingulate cortex. Which of the following dimensions of the pain experience is mediated by these spinolimbic projections?",
        "options": [
            {"text": "Affective-motivational and emotional suffering of pain", "is_correct": True},
            {"text": "Sensory-discriminative localization and intensity", "is_correct": False},
            {"text": "Two-point discrimination and vibratory threshold", "is_correct": False},
            {"text": "Monosynaptic myotatic deep tendon reflex", "is_correct": False},
            {"text": "Voluntary motor execution via the corticospinal tract", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Affective-motivational and emotional suffering of pain.\n\nThe pain pathway is divided into two distinct functional streams:\n1. Lateral pain system (Sensory-Discriminative): Spinothalamic tract → VPL nucleus of the thalamus → Primary somatosensory cortex (S1). Mediates spatial localization, intensity, duration, and quality of pain (e.g., 'sharp pain on the left index finger').\n2. Medial pain system (Affective-Motivational): Spinoreticular, spinomesencephalic, and spinolimbic tracts → Reticular formation, periaqueductal gray, intralaminar/mediodorsal thalamic nuclei → Insula, amygdala, and Anterior Cingulate Cortex (ACC). Mediates the unpleasantness, emotional anguish, suffering, autonomic arousal, and fear associated with pain."
    },
    {
        "id": "FZ_Q175",
        "question_number": 175,
        "category": "Pain Pathway",
        "stem": "A 48-year-old woman presents with severe burning pain across her right flank in a T8 dermatomal band 3 weeks after recovering from herpes zoster (shingles). Light brushing of a cotton wisp over the skin provokes intense, excruciating pain (allodynia). Central sensitization in the dorsal horn is suspected. At the molecular level, central sensitization and the 'wind-up' phenomenon in second-order nociceptive neurons are driven by continuous glutamate release activating which of the following postsynaptic receptors?",
        "options": [
            {"text": "NMDA receptors, leading to calcium influx and activation of protein kinase C (PKC)", "is_correct": True},
            {"text": "GABA-B receptors coupled to Gi proteins", "is_correct": False},
            {"text": "Nicotinic acetylcholine receptors", "is_correct": False},
            {"text": "Glycine receptors gating chloride influx", "is_correct": False},
            {"text": "D2 dopamine receptors", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. NMDA receptors, leading to calcium influx and activation of protein kinase C (PKC).\n\nCentral sensitization (the 'wind-up' phenomenon) is a state of sustained hyper-excitability of dorsal horn wide-dynamic-range neurons following repetitive C-fiber firing. Sustained release of glutamate and Substance P produces prolonged depolarization that expels the Mg2+ plug from postsynaptic NMDA receptors. Once unblocked, massive Ca2+ influx activates PKC, CaMKII, and nitric oxide synthase (NOS). This leads to phosphorylation of AMPA receptors (increasing their channel conductance) and trafficking of new AMPA receptors to the membrane, lowering the activation threshold so that even non-nociceptive tactile A-beta inputs can evoke pain (allodynia)."
    },
    {
        "id": "FZ_Q176",
        "question_number": 176,
        "category": "Pain Pathway",
        "stem": "A 24-year-old man presents with acute periumbilical abdominal pain, anorexia, and low-grade fever that began 8 hours ago. Over the next 4 hours, the pain shifts and localizes sharply to the right lower quadrant at McBurney point, accompanied by rebound tenderness and guarding. Which of the following explains why appendiceal pain shifts from dull periumbilical pain to sharp right lower quadrant pain?",
        "options": [
            {"text": "Initial visceral pain from appendiceal distension enters at T10 via sympathetic afferents (periumbilical); subsequent transmural inflammation irritates the parietal peritoneum, activating somatic sensory afferents (well-localized RLQ pain)", "is_correct": True},
            {"text": "The appendix migrates physically from the midline umbilicus into the right iliac fossa over 12 hours", "is_correct": False},
            {"text": "The phrenic nerve initially innervates the appendix before switching to the vagus nerve", "is_correct": False},
            {"text": "Initial inflammation irritates the dorsal columns, followed by spinothalamic activation", "is_correct": False},
            {"text": "Appendix pain shifts because of retrograde peristalsis through the ileocecal valve", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Initial visceral pain from appendiceal distension enters at T10 via sympathetic afferents (periumbilical); subsequent transmural inflammation irritates the parietal peritoneum, activating somatic sensory afferents (well-localized RLQ pain).\n\nThe classic shifting pain of acute appendicitis illustrates the difference between visceral and somatic pain:\n1. Visceral phase: Luminal obstruction causes ischemia and distension of the visceral appendiceal wall. Visceral sensory C fibers travel retrogradely with sympathetic splanchnic nerves to the T10 spinal cord level, presenting as dull, cramping, poorly localized periumbilical pain (T10 dermatome).\n2. Somatic phase: As transmural inflammation progresses, purulent exudate contacts the overlying parietal peritoneum of the anterior abdominal wall. The parietal peritoneum is innervated by somatic sensory fibers of spinal nerves (T12-L1). Somatic pain is sharp, excruciating, and precisely localized to McBurney point (right lower quadrant), accompanied by muscular guarding and rebound tenderness."
    },
    {
        "id": "FZ_Q177",
        "question_number": 177,
        "category": "Pain Pathway",
        "stem": "A 64-year-old man presents with diabetic polyneuropathy. As emphasized in CBIL Case 1, what simple, non-invasive screening test involves calculating the ratio of the systolic blood pressure at the ankle to the higher of the two brachial systolic pressures to evaluate for coexisting peripheral artery disease (PAD) in diabetic patients with neuropathy?",
        "options": [
            {"text": "Ankle-Brachial Index (ABI)", "is_correct": True},
            {"text": "Electromyography (EMG)", "is_correct": False},
            {"text": "Quantitative sensory testing (QST)", "is_correct": False},
            {"text": "Nerve conduction velocity (NCV)", "is_correct": False},
            {"text": "Sudomotor axon reflex test (QSART)", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Ankle-Brachial Index (ABI).\n\nAs outlined in CBIL Case 1 (Diabetic Neuropathy):\n• The Ankle-Brachial Index (ABI) is the premier screening tool for peripheral artery disease (PAD) in diabetic patients presenting with peripheral neuropathy.\n• It is calculated by dividing the highest ankle systolic pressure (dorsalis pedis or posterior tibial artery) by the higher of the two brachial systolic pressures.\n• Interpretation:\n  - Normal: 0.90 to 1.30\n  - Mild-to-moderate PAD (claudication): 0.41 to 0.90\n  - Severe PAD (critical limb ischemia, rest pain, tissue necrosis): ≤0.40\n  - Values >1.30 indicate calcified, non-compressible arteries (common in diabetics, requiring toe-brachial index testing)."
    },
    {
        "id": "FZ_Q178",
        "question_number": 178,
        "category": "Pain Pathway",
        "stem": "As part of comprehensive preventive counseling for diabetic patients with loss of protective sensation from diabetic polyneuropathy (CBIL Case 1), which of the following instructions is most critical to prevent the development of diabetic foot ulcers and secondary osteomyelitis?",
        "options": [
            {"text": "Perform daily visual foot inspections and never walk barefoot, wearing well-fitted supportive shoes", "is_correct": True},
            {"text": "Soak feet in hot water daily for 30 minutes to improve blood flow", "is_correct": False},
            {"text": "Walk barefoot on grass to stimulate mechanoreceptors", "is_correct": False},
            {"text": "Apply high-dose topical corticosteroids to the soles of the feet daily", "is_correct": False},
            {"text": "Trim calluses aggressively with a razor blade at home", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Perform daily visual foot inspections and never walk barefoot, wearing well-fitted supportive shoes.\n\nIn diabetic neuropathy (CBIL Case 1), loss of protective sensation (LOPS) prevents patients from sensing repetitive microtrauma, ill-fitting footwear, pebbles, or thermal burns. Key preventive guidelines:\n• Daily visual foot inspection (using a mirror if necessary) to detect cuts, blisters, erythema, or fungal infections early.\n• Never walk barefoot (even indoors) to prevent punctures and lacerations.\n• Wear properly fitted, cushioned shoes.\n• Avoid soaking feet in hot water (risk of severe burns due to thermal insensitivity).\n• Professional podiatric care for calluses and nail trimming."
    },
    {
        "id": "FZ_Q179",
        "question_number": 179,
        "category": "Pain Pathway",
        "stem": "Which of the following neuropeptides is co-released with glutamate from the central terminals of primary nociceptive C fibers in Rexed lamina II of the dorsal horn, binding to neurokinin-1 (NK-1) receptors to mediate slow, sustained postsynaptic depolarizations and neurogenic inflammation?",
        "options": [
            {"text": "Substance P", "is_correct": True},
            {"text": "Endorphin", "is_correct": False},
            {"text": "GABA", "is_correct": False},
            {"text": "Glycine", "is_correct": False},
            {"text": "Dopamine", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Substance P.\n\nSubstance P is an 11-amino acid neuropeptide belonging to the tachykinin family. It is synthesized by primary sensory C fibers and stored in dense-core vesicles. Upon noxious stimulation, Substance P is co-released with glutamate into the substantia gelatinosa (Rexed lamina II). It binds to Gq-coupled Neurokinin-1 (NK-1) receptors, producing slow, long-lasting postsynaptic depolarizations that enhance NMDA receptor opening and facilitate pain transmission. Peripherally, antidromic release of Substance P and CGRP causes vasodilation, plasma extravasation, and mast cell degranulation (neurogenic inflammation)."
    },
    {
        "id": "FZ_Q180",
        "question_number": 180,
        "category": "Pain Pathway",
        "stem": "A 32-year-old man presents with bilateral loss of pain and temperature sensation across his shoulders, arms, and upper chest, with preservation of vibration, proprioception, and motor strength. Spine MRI demonstrates an expanding fluid-filled syrinx within the central canal of the cervical spinal cord (syringomyelia). Which of the following anatomical structures is directly compressed by the enlarging syrinx to cause this bilateral 'cape-like' loss of pain and temperature?",
        "options": [
            {"text": "Anterior white commissure (decussating spinothalamic fibers)", "is_correct": True},
            {"text": "Fasciculus gracilis and cuneatus bilaterally", "is_correct": False},
            {"text": "Lateral corticospinal tracts bilaterally", "is_correct": False},
            {"text": "Dorsal root ganglia bilaterally", "is_correct": False},
            {"text": "Intermediolateral cell columns bilaterally", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Anterior white commissure (decussating spinothalamic fibers).\n\nSyringomyelia is a cystic cavitation (syrinx) within the central canal of the spinal cord (most commonly cervical C8-T1, frequently associated with Chiari I malformation). As the syrinx expands from the central canal, the first structures it compresses are the crossing second-order spinothalamic axons traversing the Anterior White Commissure immediately ventral to the central canal. This produces bilateral, symmetrical loss of pain and temperature sensation in a dermatomal 'cape-like' distribution over the neck, shoulders, and arms. The dorsal columns (located dorsally) and corticospinal tracts (located laterally) are spared early in the disease."
    },

    # =========================================================================
    # TOPIC 10: Trigeminal Pathway (FZ_Q181 - FZ_Q200)
    # =========================================================================
    {
        "id": "FZ_Q181",
        "question_number": 181,
        "category": "Trigeminal Pathway",
        "stem": "A 62-year-old woman presents to the clinic with paroxysmal episodes of severe, stabbing, electric shock-like pain on the right side of her face. The pain lasts 10 to 30 seconds and is triggered by brushing her teeth, chewing, or even a light breeze on her cheek. The pain is strictly confined to the right cheek, upper lip, and lateral nose (V2 distribution). Neurological examination is normal between episodes. Which of the following is the first-line pharmacotherapeutic agent of choice for trigeminal neuralgia?",
        "options": [
            {"text": "Carbamazepine", "is_correct": True},
            {"text": "Indomethacin", "is_correct": False},
            {"text": "Sumatriptan", "is_correct": False},
            {"text": "Acetaminophen", "is_correct": False},
            {"text": "Morphine", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Carbamazepine.\n\nTrigeminal neuralgia (Tic Douloureux) is characterized by sudden, unilateral, paroxysmal, lancinating, electric shock-like facial pain triggered by innocuous tactile stimuli (touching the face, chewing, wind). The first-line medication is Carbamazepine (or oxcarbazepine). Mechanism: Carbamazepine binds and stabilizes the inactivated state of voltage-gated sodium channels, preventing high-frequency repetitive firing in hyper-excitable, demyelinated trigeminal axons. \n• Important side effects: Aplastic anemia, agranulocytosis, SIADH (hyponatremia), ataxia, CYP3A4 auto-induction, and Stevens-Johnson syndrome (especially in patients with HLA-B*1502)."
    },
    {
        "id": "FZ_Q182",
        "question_number": 182,
        "category": "Trigeminal Pathway",
        "stem": "High-resolution 3D constructive interference in steady state (CISS) MRI is performed on a patient with classic trigeminal neuralgia. The scan reveals neurovascular compression of the trigeminal sensory root entry zone at the cerebellopontine angle by an aberrant arterial loop. Which of the following arteries is most frequently identified as the compressing vessel causing trigeminal neuralgia?",
        "options": [
            {"text": "Superior cerebellar artery (SCA)", "is_correct": True},
            {"text": "Anterior inferior cerebellar artery (AICA)", "is_correct": False},
            {"text": "Posterior inferior cerebellar artery (PICA)", "is_correct": False},
            {"text": "Anterior cerebral artery (ACA)", "is_correct": False},
            {"text": "Middle cerebral artery (MCA)", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Superior cerebellar artery (SCA).\n\nIn >80% to 90% of classic trigeminal neuralgia cases, the etiology is pulsatile neurovascular compression of the trigeminal nerve root entry zone (REZ) in the prepontine cistern. The offending vessel is most commonly an aberrant or ectatic loop of the Superior Cerebellar Artery (SCA), which branches from the rostral basilar artery and wraps around the upper pons. Chronic arterial pulsations cause focal mechanical demyelination and ephaptic transmission (cross-talk between low-threshold tactile fibers and unmyelinated nociceptive fibers). Surgical decompression (the Jannetta microvascular decompression procedure) lifts the SCA off the nerve."
    },
    {
        "id": "FZ_Q183",
        "question_number": 183,
        "category": "Trigeminal Pathway",
        "stem": "A 28-year-old woman presents with paroxysmal, lancinating electric shock-like facial pain affecting the left mandibular region (V3). Two months ago, she experienced transient optic neuritis in her right eye. Brain MRI reveals multiple hyperintense periventricular plaques and a focal demyelinating lesion at the trigeminal root entry zone in the left mid-pons. In a young adult presenting with bilateral or atypical trigeminal neuralgia, which of the following is the most likely underlying diagnosis?",
        "options": [
            {"text": "Multiple sclerosis", "is_correct": True},
            {"text": "Amyotrophic lateral sclerosis", "is_correct": False},
            {"text": "Parkinson disease", "is_correct": False},
            {"text": "Alzheimer disease", "is_correct": False},
            {"text": "Tabes dorsalis", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Multiple sclerosis.\n\nWhile classic trigeminal neuralgia in elderly patients is typically caused by vascular compression by the superior cerebellar artery, trigeminal neuralgia presenting in a young patient (<40 years old), or presenting bilaterally, is a classic harbinger of Multiple Sclerosis (MS). An autoimmune demyelinating plaque located at the trigeminal root entry zone within the pontine tegmentum disrupts axonal insulation, leading to spontaneous ectopic action potential generation and ephaptic cross-excitation."
    },
    {
        "id": "FZ_Q184",
        "question_number": 184,
        "category": "Trigeminal Pathway",
        "stem": "The trigeminal sensory nuclear complex extends throughout the entire brainstem into the upper cervical spinal cord. Which of the following trigeminal nuclei contains primary sensory pseudounipolar cell bodies that uniquely reside INSIDE the central nervous system (rather than in a peripheral sensory ganglion), conveying unconscious proprioception from the muscles of mastication?",
        "options": [
            {"text": "Mesencephalic nucleus of the trigeminal nerve", "is_correct": True},
            {"text": "Chief (principal) sensory nucleus of the trigeminal nerve", "is_correct": False},
            {"text": "Spinal trigeminal nucleus", "is_correct": False},
            {"text": "Trigeminal motor nucleus", "is_correct": False},
            {"text": "Nucleus ambiguus", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Mesencephalic nucleus of the trigeminal nerve.\n\nThe mesencephalic nucleus of the trigeminal nerve (located in the lateral midbrain tegmentum) is unique in neuroanatomy: it is the ONLY structure in the central nervous system that contains primary sensory pseudounipolar neuronal cell bodies (which normally reside in peripheral ganglia like the DRG or trigeminal ganglion). Embryologically, these are neural crest cells that failed to migrate out of the neural tube. They receive proprioceptive input from muscle spindles in the muscles of mastication and mechanoreceptors in periodontal ligaments, mediating bite-force regulation and the monosynaptic jaw jerk reflex."
    },
    {
        "id": "FZ_Q185",
        "question_number": 185,
        "category": "Trigeminal Pathway",
        "stem": "Which of the following nuclei in the brainstem trigeminal sensory complex is the direct analog to the spinal cord dorsal columns, receiving primary afferents that convey discriminative fine touch, vibration, and two-point discrimination from the face?",
        "options": [
            {"text": "Chief (principal) sensory nucleus of the trigeminal nerve (located in the mid-pons)", "is_correct": True},
            {"text": "Spinal trigeminal nucleus (subnucleus caudalis)", "is_correct": False},
            {"text": "Mesencephalic nucleus of the trigeminal nerve", "is_correct": False},
            {"text": "Trigeminal motor nucleus", "is_correct": False},
            {"text": "Edinger-Westphal nucleus", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Chief (principal) sensory nucleus of the trigeminal nerve (located in the mid-pons).\n\nThe Chief (principal) sensory nucleus of CN V is located in the mid-pons (lateral to the motor nucleus). It is the facial counterpart to the dorsal column nuclei (gracilis and cuneatus). Primary pseudounipolar cell bodies in the trigeminal (semilunar/Gasserian) ganglion send large myelinated A-beta fibers into the mid-pons to terminate in the principal sensory nucleus, conveying fine touch, pressure, and vibration. Second-order neurons decussate and ascend as the trigeminal lemniscus (ventral trigeminothalamic tract) to the VPM nucleus of the thalamus."
    },
    {
        "id": "FZ_Q186",
        "question_number": 186,
        "category": "Trigeminal Pathway",
        "stem": "A 59-year-old man presents with loss of pain and temperature sensation on the right side of his face. Touch and vibration on his face are completely intact. An MRI reveals a small infarction in the lateral medulla. Which of the following nuclei in the trigeminal complex extends caudally through the entire medulla into the upper cervical cord (C2-C3), functioning as the primary relay for facial pain and temperature?",
        "options": [
            {"text": "Spinal trigeminal nucleus (specifically subnucleus caudalis)", "is_correct": True},
            {"text": "Chief sensory nucleus", "is_correct": False},
            {"text": "Mesencephalic nucleus", "is_correct": False},
            {"text": "Trigeminal motor nucleus", "is_correct": False},
            {"text": "Hypoglossal nucleus", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Spinal trigeminal nucleus (specifically subnucleus caudalis).\n\nThe Spinal Trigeminal Nucleus extends from the mid-pons through the entire length of the medulla down into the dorsal horn of the upper cervical spinal cord (C2-C3). It is the facial counterpart to the anterolateral spinothalamic system. Primary pain and temperature fibers enter the pons, turn caudally, and descend in the Spinal Trigeminal Tract before synapsing in the spinal trigeminal nucleus. Subnucleus caudalis (in the caudal medulla) is the primary relay for pain and temperature and is continuous histologically with Rexed lamina II (substantia gelatinosa) of the cervical cord."
    },
    {
        "id": "FZ_Q187",
        "question_number": 187,
        "category": "Trigeminal Pathway",
        "stem": "In the central somatosensory pathways, second-order neurons conveying discriminative touch, pain, and temperature from the face ascend through the brainstem in the trigeminothalamic tracts. In which of the following specific thalamic nuclei do third-order sensory neurons representing the face terminate?",
        "options": [
            {"text": "Ventral posteromedial (VPM) nucleus", "is_correct": True},
            {"text": "Ventral posterolateral (VPL) nucleus", "is_correct": False},
            {"text": "Lateral geniculate nucleus (LGN)", "is_correct": False},
            {"text": "Medial geniculate nucleus (MGN)", "is_correct": False},
            {"text": "Anterior thalamic nucleus", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Ventral posteromedial (VPM) nucleus.\n\nThalamic somatosensory relays:\n• Ventral Posteromedial (VPM) nucleus: Relays ALL sensory inputs from the FACE and head (trigeminal lemniscus and ventral trigeminothalamic tract), as well as taste from the solitary nucleus ('VPM = Make-up on the Face'). Third-order axons project through the posterior limb of the internal capsule to the lateral face area of the postcentral gyrus.\n• Ventral Posterolateral (VPL) nucleus: Relays sensory inputs from the BODY and limbs (medial lemniscus and spinothalamic tract) ('VPL = Legs and body')."
    },
    {
        "id": "FZ_Q188",
        "question_number": 188,
        "category": "Trigeminal Pathway",
        "stem": "The trigeminal nerve (CN V) divides into three major sensory divisions before exiting the middle cranial fossa. Which of the following skull base foramina transmits the maxillary nerve (V2)?",
        "options": [
            {"text": "Foramen rotundum", "is_correct": True},
            {"text": "Superior orbital fissure", "is_correct": False},
            {"text": "Foramen ovale", "is_correct": False},
            {"text": "Foramen spinosum", "is_correct": False},
            {"text": "Jugular foramen", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Foramen rotundum.\n\nExit foramina of the three divisions of the trigeminal nerve (mnemonic: 'Standing Room Only'):\n• V1 (Ophthalmic division): Superior orbital fissure ('S')\n• V2 (Maxillary division): Foramen Rotundum ('R')\n• V3 (Mandibular division): Foramen Ovale ('O').\n\n• The foramen spinosum transmits the middle meningeal artery.\n• The jugular foramen transmits cranial nerves IX, X, and XI."
    },
    {
        "id": "FZ_Q189",
        "question_number": 189,
        "category": "Trigeminal Pathway",
        "stem": "A 45-year-old man undergoes surgical resection of a Schwannoma located in the foramen ovale. Which of the following anatomical structures passes through the foramen ovale and would be vulnerable to injury during this procedure?",
        "options": [
            {"text": "Mandibular nerve (CN V3) and motor root of the trigeminal nerve", "is_correct": True},
            {"text": "Maxillary nerve (CN V2)", "is_correct": False},
            {"text": "Ophthalmic nerve (CN V1)", "is_correct": False},
            {"text": "Internal carotid artery", "is_correct": False},
            {"text": "Middle meningeal artery", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Mandibular nerve (CN V3) and motor root of the trigeminal nerve.\n\nThe foramen ovale is an oval opening in the greater wing of the sphenoid bone. Structures passing through the foramen ovale (mnemonic: 'OVALE'):\n• O: Otic ganglion (situated immediately inferior to the foramen)\n• V: V3 (Mandibular nerve, including both sensory and motor roots)\n• A: Accessory meningeal artery\n• L: Lesser petrosal nerve (branch of CN IX carrying parasympathetics to the parotid)\n• E: Emissary veins.\nInjury to CN V3 causes sensory loss over the lower jaw/chin and paralysis of the muscles of mastication (masseter, temporalis, pterygoids)."
    },
    {
        "id": "FZ_Q190",
        "question_number": 190,
        "category": "Trigeminal Pathway",
        "stem": "The motor root of the mandibular nerve (CN V3) originates from the trigeminal motor nucleus in the mid-pons. In addition to innervating the four primary muscles of mastication (masseter, temporalis, medial pterygoid, and lateral pterygoid), the motor root of CN V3 innervates which of the following muscles?",
        "options": [
            {"text": "Tensor tympani, tensor veli palatini, mylohyoid, and anterior belly of the digastric", "is_correct": True},
            {"text": "Stapedius, posterior belly of the digastric, and stylohyoid", "is_correct": False},
            {"text": "Levator veli palatini and palatoglossus", "is_correct": False},
            {"text": "Stylopharyngeus", "is_correct": False},
            {"text": "Genioglossus and hyoglossus", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Tensor tympani, tensor veli palatini, mylohyoid, and anterior belly of the digastric.\n\nAll muscles derived from the first pharyngeal (mandibular) arch are innervated by the motor branch of the mandibular nerve (CN V3):\n• Four muscles of mastication: Masseter, temporalis, medial pterygoid, lateral pterygoid.\n• Mylohyoid and Anterior belly of the digastric (floor of the mouth).\n• Tensor tympani (dampens sound vibrations of the tympanic membrane).\n• Tensor veli palatini (tenses soft palate and opens Eustachian tube).\n\n• Option B is incorrect: Derived from the 2nd pharyngeal arch, innervated by CN VII.\n• Option C is incorrect: Innervated by CN X.\n• Option D is incorrect: Innervated by CN IX."
    },
    {
        "id": "FZ_Q191",
        "question_number": 191,
        "category": "Trigeminal Pathway",
        "stem": "During a coma examination, a physician touches a fine wisp of sterile cotton to the lateral cornea of the patient's right eye, observing an immediate, consensual bilateral blink. Which of the following cranial nerves provides the afferent sensory limb, and which provides the efferent motor limb, of the corneal reflex?",
        "options": [
            {"text": "Afferent: CN V1 (nasociliary branch of the ophthalmic nerve); Efferent: Bilateral CN VII (facial nerve)", "is_correct": True},
            {"text": "Afferent: CN II (optic nerve); Efferent: Bilateral CN III (oculomotor nerve)", "is_correct": False},
            {"text": "Afferent: CN V2; Efferent: CN V3", "is_correct": False},
            {"text": "Afferent: CN VII; Efferent: CN V1", "is_correct": False},
            {"text": "Afferent: CN VIII; Efferent: CN VI", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Afferent: CN V1 (nasociliary branch of the ophthalmic nerve); Efferent: Bilateral CN VII (facial nerve).\n\nThe corneal reflex arc:\n• Afferent limb: Touch on the cornea stimulates unmyelinated free nerve endings of the nasociliary branch of the ophthalmic nerve (CN V1). Fibers enter the mid-pons and descend to the spinal trigeminal nucleus.\n• Central interneurons: Relay bilaterally to the facial motor nuclei (CN VII) in the caudal pons.\n• Efferent limb: Both facial nerves (CN VII) fire, innervating the orbicularis oculi muscles to produce a direct blink in the touched eye and a consensual blink in the opposite eye."
    },
    {
        "id": "FZ_Q192",
        "question_number": 192,
        "category": "Trigeminal Pathway",
        "stem": "A neurologist taps the center of a patient's chin with a reflex hammer while the patient's mouth is held slightly open. In a normal individual, this produces a minimal or absent reflex. In a patient with bilateral upper motor neuron lesions (pseudobulbar palsy), however, this produces a brisk, hyperactive jaw jerk (masseter reflex). What is the neural circuit mediating this monosynaptic reflex?",
        "options": [
            {"text": "Afferent limb via CN V (mesencephalic nucleus); Efferent limb via CN V (trigeminal motor nucleus)", "is_correct": True},
            {"text": "Afferent limb via CN VII; Efferent limb via CN XII", "is_correct": False},
            {"text": "Afferent limb via CN IX; Efferent limb via CN X", "is_correct": False},
            {"text": "Afferent limb via CN V1; Efferent limb via CN VII", "is_correct": False},
            {"text": "Afferent limb via CN V2; Efferent limb via CN XI", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Afferent limb via CN V (mesencephalic nucleus); Efferent limb via CN V (trigeminal motor nucleus).\n\nThe jaw jerk reflex (masseter reflex) is a monosynaptic deep tendon reflex:\n• Afferent limb: Tapping the chin stretches muscle spindles in the masseter muscle. Proprioceptive afferents travel in the mandibular nerve (CN V3) to their primary cell bodies in the Mesencephalic nucleus of CN V.\n• Central synapse: Mesencephalic axons project monosynaptically to the adjacent Trigeminal Motor Nucleus in the mid-pons.\n• Efferent limb: Motor axons travel via CN V3 to contract the masseter and temporalis, closing the jaw.\nA hyperactive jaw jerk indicates bilateral upper motor neuron lesions above the mid-pons (e.g., ALS or pseudobulbar palsy)."
    },
    {
        "id": "FZ_Q193",
        "question_number": 193,
        "category": "Trigeminal Pathway",
        "stem": "A 66-year-old man presents with Wallenberg syndrome (lateral medullary syndrome) following occlusion of his right posterior inferior cerebellar artery (PICA). On sensory examination, he exhibits a 'crossed' or alternating pattern of analgesia: loss of pain and temperature on the right side of his face, but on the left side of his body. Which of the following two anatomical tracts were simultaneously infarcted in the right lateral medulla?",
        "options": [
            {"text": "Right spinal trigeminal nucleus/tract and right spinothalamic tract", "is_correct": True},
            {"text": "Right chief sensory nucleus and right medial lemniscus", "is_correct": False},
            {"text": "Left spinal trigeminal nucleus and left corticospinal tract", "is_correct": False},
            {"text": "Right mesencephalic nucleus and right medial longitudinal fasciculus", "is_correct": False},
            {"text": "Left trigeminal motor nucleus and right pyramids", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Right spinal trigeminal nucleus/tract and right spinothalamic tract.\n\nWallenberg syndrome (lateral medullary syndrome) characteristically produces 'crossed hemianalgesia':\n1. Ipsilateral facial pain and temperature loss: The spinal trigeminal nucleus and tract carry uncrossed primary pain/temperature afferents from the ipsilateral face. A right lateral medullary lesion causes right-sided facial loss.\n2. Contralateral body pain and temperature loss: The spinothalamic tract carries pain/temperature fibers that crossed in the spinal cord and ascend in the anterolateral medulla. A right lateral medullary lesion causes left-sided hemibody loss."
    },
    {
        "id": "FZ_Q194",
        "question_number": 194,
        "category": "Trigeminal Pathway",
        "stem": "A 50-year-old woman with a history of breast cancer presents with numbness over her chin and lower lip ('numb chin syndrome'). There is no facial motor weakness. Imaging reveals metastatic bone destruction of the mandible. Neuropathy of which of the following terminal branches of the mandibular nerve (CN V3) is responsible for isolated numbness of the chin?",
        "options": [
            {"text": "Mental nerve (terminal branch of the inferior alveolar nerve)", "is_correct": True},
            {"text": "Lingual nerve", "is_correct": False},
            {"text": "Auriculotemporal nerve", "is_correct": False},
            {"text": "Infraorbital nerve", "is_correct": False},
            {"text": "Supraorbital nerve", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Mental nerve (terminal branch of the inferior alveolar nerve).\n\n'Numb chin syndrome' (mental neuropathy) is a classic neurological red flag that often indicates mandibular metastasis from breast, prostate, or lung cancer. The mental nerve is the terminal cutaneous sensory branch of the inferior alveolar nerve (from CN V3). It exits the mandible through the mental foramen to provide somatic sensation to the lower lip and chin. Tumor infiltration or compression within the mandibular canal produces isolated numbness of the chin."
    },
    {
        "id": "FZ_Q195",
        "question_number": 195,
        "category": "Trigeminal Pathway",
        "stem": "A 23-year-old boxer receives a direct blow to the orbit, sustaining a 'blowout fracture' of the thin orbital floor (maxillary bone). He complains of numbness over his right cheek, upper lip, and right upper gingiva, and exhibits diplopia on upward gaze due to inferior rectus entrapment. Which of the following nerves coursing through the floor of the orbit was injured?",
        "options": [
            {"text": "Infraorbital nerve (branch of CN V2)", "is_correct": True},
            {"text": "Supraorbital nerve (branch of CN V1)", "is_correct": False},
            {"text": "Lacrimal nerve (branch of CN V1)", "is_correct": False},
            {"text": "Mental nerve (branch of CN V3)", "is_correct": False},
            {"text": "Zygomaticofacial nerve", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Infraorbital nerve (branch of CN V2).\n\nThe infraorbital nerve is the continuation of the maxillary nerve (CN V2). After passing through the inferior orbital fissure, it travels forward in the infraorbital groove and canal in the floor of the orbit (roof of the maxillary sinus) before emerging onto the face via the infraorbital foramen. In orbital blowout fractures, the fragile orbital floor fractures into the maxillary sinus, commonly injuring the infraorbital nerve and causing paresthesias and numbness of the ipsilateral lower eyelid, cheek, upper lip, and upper teeth."
    },
    {
        "id": "FZ_Q196",
        "question_number": 196,
        "category": "Trigeminal Pathway",
        "stem": "A 38-year-old woman presents with severe pain in front of her ear and temple while chewing, accompanied by clicking and popping of the jaw. She has tenderness over the temporomandibular joint (TMJ). Which of the following sensory branches of the mandibular nerve (CN V3) wraps around the neck of the mandible and the middle meningeal artery, providing sensory innervation to the TMJ, external auditory meatus, and temple?",
        "options": [
            {"text": "Auriculotemporal nerve", "is_correct": True},
            {"text": "Buccal nerve", "is_correct": False},
            {"text": "Inferior alveolar nerve", "is_correct": False},
            {"text": "Greater auricular nerve", "is_correct": False},
            {"text": "Chorda tympani", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Auriculotemporal nerve.\n\nThe auriculotemporal nerve arises from CN V3 by two roots that encircle the middle meningeal artery. It courses posteriorly around the neck of the mandible, passes deep to the parotid gland, and ascends across the zygomatic arch with the superficial temporal vessels. It provides sensory innervation to:\n1. The temporomandibular joint (TMJ)\n2. The anterior auricle and external acoustic meatus\n3. Cutaneous temple and scalp.\nIt also carries postganglionic parasympathetic secretomotor fibers from the otic ganglion to the parotid gland. Irritation in TMJ dysfunction produces severe temporal and preauricular headache."
    },
    {
        "id": "FZ_Q197",
        "question_number": 197,
        "category": "Trigeminal Pathway",
        "stem": "A 60-year-old man presents with acute shingles. He exhibits painful, grouped vesicles on an erythematous base distributed across his forehead, upper eyelid, and extending down to the tip and side of his nose (Hutchinson sign). The presence of vesicles on the tip of the nose indicates involvement of the nasociliary branch of CN V1, warning of high risk for which of the following serious complications?",
        "options": [
            {"text": "Herpes zoster ophthalmicus with corneal ulceration and blindness", "is_correct": True},
            {"text": "Otitis media with ossicular chain destruction", "is_correct": False},
            {"text": "Parotid gland necrosis", "is_correct": False},
            {"text": "Thyroid storm", "is_correct": False},
            {"text": "Suppurative submandibular sialadenitis", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Herpes zoster ophthalmicus with corneal ulceration and blindness.\n\nHerpes zoster ophthalmicus occurs when latent varicella-zoster virus (VZV) reactivates in the trigeminal (Gasserian) ganglion within the ophthalmic division (CN V1). The nasociliary branch of V1 innervates both the tip of the nose (via the external nasal branch) and the cornea/globe (via long and short ciliary nerves). Vesicles on the tip of the nose (positive Hutchinson sign) correlate strongly with ocular involvement (dendritic keratitis, corneal ulceration, anterior uveitis, and secondary glaucoma), requiring emergency ophthalmological evaluation and prompt antiviral therapy (oral valacyclovir) to prevent irreversible visual loss."
    },
    {
        "id": "FZ_Q198",
        "question_number": 198,
        "category": "Trigeminal Pathway",
        "stem": "During dental anesthesia for a mandibular molar extraction, an inferior alveolar nerve block is administered. If the needle is inserted too far posteriorly into the parotid gland capsule, which of the following cranial nerves can be inadvertently anesthetized, resulting in acute, transient unilateral facial droop?",
        "options": [
            {"text": "Facial nerve (CN VII motor branches)", "is_correct": True},
            {"text": "Glossopharyngeal nerve (CN IX)", "is_correct": False},
            {"text": "Hypoglossal nerve (CN XII)", "is_correct": False},
            {"text": "Accessory nerve (CN XI)", "is_correct": False},
            {"text": "Vagus nerve (CN X)", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Facial nerve (CN VII motor branches).\n\nThe inferior alveolar nerve block is injected into the pterygomandibular space near the mandibular foramen. The parotid gland wraps around the posterior border of the ramus of the mandible. Within the parotid gland parenchyma, the main trunk of the facial nerve (CN VII) divides into its five terminal motor branches (temporal, zygomatic, buccal, marginal mandibular, cervical). If local anesthetic is injected too far posteriorly, it infiltrates the parotid gland, anesthetizing CN VII and causing transient ipsilateral lower motor neuron facial paralysis (inability to close the eye, loss of nasolabial fold, mouth droop) that resolves as the anesthetic wears off."
    },
    {
        "id": "FZ_Q199",
        "question_number": 199,
        "category": "Trigeminal Pathway",
        "stem": "A 45-year-old woman presents with persistent left facial numbness. On physical examination, when she is asked to open her mouth wide and protrude her lower jaw, her mandible deviates visibly to the left side. Weakness of which of the following muscles innervated by the mandibular nerve (CN V3) causes the jaw to deviate toward the side of the lesion?",
        "options": [
            {"text": "Left lateral pterygoid muscle", "is_correct": True},
            {"text": "Right lateral pterygoid muscle", "is_correct": False},
            {"text": "Left masseter muscle", "is_correct": False},
            {"text": "Right temporalis muscle", "is_correct": False},
            {"text": "Left buccinator muscle", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Left lateral pterygoid muscle.\n\nThe lateral pterygoid muscle is the primary muscle responsible for protracting (pushing forward) and depressing the mandible. Each lateral pterygoid pushes the condyle of the mandible forward and medially toward the contralateral side. When both muscles contract symmetrically, the jaw protrudes in the midline. If there is a lower motor neuron lesion of the left CN V3, the left lateral pterygoid is paralyzed; the unopposed action of the normal right lateral pterygoid pushes the jaw forward and toward the weak (left) side. Thus, the mandible deviates TOWARD the side of the lesion ('the jaw deviates toward the injured nerve')."
    },
    {
        "id": "FZ_Q200",
        "question_number": 200,
        "category": "Trigeminal Pathway",
        "stem": "A 52-year-old man presents with episodic pain along the base of his tongue and deep ear canal that is triggered by swallowing cold liquids. Neurological testing reveals that general somatic sensation from the external auditory meatus and tympanic membrane is shared by several cranial nerves. Which of the following cranial nerves contributes sensory innervation to the external ear canal and ear drum?",
        "options": [
            {"text": "Cranial nerves V3, VII, IX, and X", "is_correct": True},
            {"text": "Cranial nerves I, II, III, and IV", "is_correct": False},
            {"text": "Cranial nerves VI and XII only", "is_correct": False},
            {"text": "Cranial nerves III and VIII only", "is_correct": False},
            {"text": "Cranial nerve XI only", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Cranial nerves V3, VII, IX, and X.\n\nThe external ear canal and tympanic membrane possess complex overlapping sensory innervation derived from four cranial nerves:\n1. CN V3 (Auriculotemporal nerve): Anterior wall of external acoustic meatus and anterior tympanic membrane.\n2. CN VII (Nervus intermedius): Concha of auricle and posterior wall of canal.\n3. CN IX (Tympanic nerve of Jacobson): Inner surface of tympanic membrane and middle ear cavity.\n4. CN X (Auricular branch of vagus / Arnold nerve): Posterior and inferior canal and posterior tympanic membrane (stimulation during ear cleaning can trigger reflex coughing or syncope via vagal stimulation)."
    },

    # =========================================================================
    # TOPIC 11: Anesthetic & NMJ Blocking Agents (FZ_Q201 - FZ_Q220)
    # =========================================================================
    {
        "id": "FZ_Q201",
        "question_number": 201,
        "category": "Anesthetic & NMJ Blocking Agents",
        "stem": "An anesthesiologist is evaluating five different inhaled general anesthetic gasses for an upcoming procedure. The Minimum Alveolar Concentration (MAC) values are: Anesthetic A (0.75%), Anesthetic B (1.2%), Anesthetic C (1.6%), Anesthetic D (6.0%), and Anesthetic E (105%). Which of these anesthetic agents has the highest potency?",
        "options": [
            {"text": "Anesthetic A (MAC 0.75%)", "is_correct": True},
            {"text": "Anesthetic B (MAC 1.2%)", "is_correct": False},
            {"text": "Anesthetic C (MAC 1.6%)", "is_correct": False},
            {"text": "Anesthetic D (MAC 6.0%)", "is_correct": False},
            {"text": "Anesthetic E (MAC 105%)", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Anesthetic A (MAC 0.75%).\n\nMinimum Alveolar Concentration (MAC) is defined as the alveolar concentration of an inhaled anesthetic at 1 atmosphere of pressure that prevents skeletal muscle movement in response to a standard noxious surgical stimulus (skin incision) in 50% of patients. \n• MAC is inversely proportional to POTENCY (Potency = 1/MAC).\n• An anesthetic with a low MAC (e.g., Halothane, MAC ~0.75%) requires only a tiny concentration in the lungs to produce surgical anesthesia, meaning it is extremely potent.\n• Conversely, an agent with a very high MAC (e.g., Nitrous Oxide, MAC ~105%) has very low potency and cannot produce general anesthesia alone at atmospheric pressure."
    },
    {
        "id": "FZ_Q202",
        "question_number": 202,
        "category": "Anesthetic & NMJ Blocking Agents",
        "stem": "In clinical pharmacology, the speed of induction (onset of anesthesia) and the speed of emergence (recovery) of an inhaled anesthetic are governed by its solubility in blood. Which of the following physical constants determines the rate at which alveolar partial pressure equilibrates with arterial blood and brain partial pressure?",
        "options": [
            {"text": "Blood:Gas partition coefficient (inversely proportional to induction speed)", "is_correct": True},
            {"text": "Oil:Gas partition coefficient (directly proportional to induction speed)", "is_correct": False},
            {"text": "Minimum Alveolar Concentration (MAC)", "is_correct": False},
            {"text": "Molecular weight of the anesthetic gas", "is_correct": False},
            {"text": "Renal clearance rate", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Blood:Gas partition coefficient (inversely proportional to induction speed).\n\nThe Blood:Gas partition coefficient is a measure of an inhaled anesthetic's solubility in blood:\n• Insoluble agents (LOW blood:gas partition coefficient, e.g., Nitrous Oxide [0.47], Desflurane [0.42]): Very little gas dissolves in the blood. Blood saturates rapidly, allowing alveolar and arterial partial pressures to rise swiftly. Brain partial pressure equilibrates rapidly, resulting in FAST induction and FAST emergence.\n• Soluble agents (HIGH blood:gas partition coefficient, e.g., Halothane [2.30], Isoflurane [1.40]): Large amounts of gas dissolve in the blood (acting like a sponge). Blood saturation is delayed, alveolar partial pressure rises slowly, and brain equilibration is sluggish, resulting in SLOW induction and SLOW emergence."
    },
    {
        "id": "FZ_Q203",
        "question_number": 203,
        "category": "Anesthetic & NMJ Blocking Agents",
        "stem": "A 22-year-old man undergoes emergency appendectomy under general anesthesia with halothane and succinylcholine. Thirty minutes into the procedure, the anesthesiologist notes acute masseter muscle rigidity, end-tidal carbon dioxide (EtCO2) rising from 38 to 85 mmHg, tachycardia of 145 beats/min, and core body temperature spiking to 41.2°C (106.2°F). Laboratory testing reveals severe hyperkalemia and acute metabolic acidosis. Mutations in which of the following genes is the most common cause of this life-threatening Malignant Hyperthermia?",
        "options": [
            {"text": "RYR1 gene encoding the skeletal muscle ryanodine receptor", "is_correct": True},
            {"text": "SCN4A gene encoding the skeletal muscle voltage-gated sodium channel", "is_correct": False},
            {"text": "DMD gene encoding dystrophin", "is_correct": False},
            {"text": "CACNA1A gene encoding the P/Q-type calcium channel", "is_correct": False},
            {"text": "ATP1A2 gene encoding the sodium-potassium pump", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. RYR1 gene encoding the skeletal muscle ryanodine receptor.\n\nMalignant Hyperthermia (MH) is a life-threatening pharmacogenetic disorder triggered by volatile inhaled anesthetics (halothane, isoflurane, sevoflurane, desflurane) or the depolarizing muscle relaxant succinylcholine. In >70% to 80% of families, it is inherited in an autosomal dominant pattern caused by mutations in the RYR1 gene (encoding the ryanodine receptor 1 channel on the sarcoplasmic reticulum) or CACNA1S (encoding the L-type calcium channel / DHPR). Triggering agents cause uncontrolled, continuous Ca2+ release from the sarcoplasmic reticulum into the myoplasm, driving sustained muscle contraction (masseter rigidity), hypermetabolism, massive heat production, hypercapnia, rhabdomyolysis, and hyperkalemia."
    },
    {
        "id": "FZ_Q204",
        "question_number": 204,
        "category": "Anesthetic & NMJ Blocking Agents",
        "stem": "In the management of the patient described above experiencing acute malignant hyperthermia, which of the following medications is the specific antidote that must be administered immediately intravenously to halt uncontrolled sarcoplasmic reticulum calcium release?",
        "options": [
            {"text": "Dantrolene", "is_correct": True},
            {"text": "Pralidoxime", "is_correct": False},
            {"text": "Neostigmine", "is_correct": False},
            {"text": "Atropine", "is_correct": False},
            {"text": "Flumazenil", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Dantrolene.\n\nIV Dantrolene is the specific, life-saving antidote for Malignant Hyperthermia (and neuroleptic malignant syndrome). Dantrolene acts as a direct Ryanodine Receptor (RyR1) antagonist, binding the channel and blocking Ca2+ release from the sarcoplasmic reticulum into the skeletal muscle cytoplasm. This uncouples excitation-contraction coupling, halting muscle rigidity, hypermetabolism, heat generation, and lactic acid production.\n\n• Protocol: Discontinue offending volatile anesthetics and succinylcholine, hyperventilate with 100% O2, administer IV dantrolene (2.5 mg/kg bolus), and actively cool the patient."
    },
    {
        "id": "FZ_Q205",
        "question_number": 205,
        "category": "Anesthetic & NMJ Blocking Agents",
        "stem": "A 45-year-old trauma patient with severe hypovolemic shock (blood pressure 75/40 mmHg, heart rate 130 beats/min) requires emergency rapid sequence intubation. The anesthesiologist selects etomidate as the IV induction agent because of its outstanding hemodynamic stability. However, which of the following endocrine side effects is a well-known risk of etomidate administration, particularly during continuous infusion?",
        "options": [
            {"text": "Reversible inhibition of 11-beta-hydroxylase, leading to primary adrenal insufficiency (suppression of cortisol and aldosterone)", "is_correct": True},
            {"text": "Inhibition of thyroid peroxidase, causing acute hypothyroidism", "is_correct": False},
            {"text": "Hypersecretion of prolactin causing acute gynecomastia", "is_correct": False},
            {"text": "Destruction of beta-islet cells causing permanent type 1 diabetes", "is_correct": False},
            {"text": "Massive release of parathyroid hormone causing hypercalcemic crisis", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Reversible inhibition of 11-beta-hydroxylase, leading to primary adrenal insufficiency (suppression of cortisol and aldosterone).\n\nEtomidate is an imidazole derivative that acts as a GABA-A receptor allosteric agonist. It is the induction agent of choice for hemodynamically unstable patients (septic shock, hypovolemia, trauma) because it preserves cardiac output, blood pressure, and systemic vascular resistance. However, etomidate contains an imidazole ring that reversibly inhibits 11-beta-hydroxylase (the mitochondrial enzyme that converts 11-deoxycortisol to cortisol and 11-deoxycorticosterone to corticosterone in the adrenal cortex). Even a single induction dose can cause transient adrenocortical suppression, and continuous infusions are contraindicated due to increased mortality from adrenal failure."
    },
    {
        "id": "FZ_Q206",
        "question_number": 206,
        "category": "Anesthetic & NMJ Blocking Agents",
        "stem": "A 25-year-old man undergoes procedural sedation for reduction of a dislocated shoulder using intravenous ketamine. He maintains spontaneous ventilation, but appears awake with his eyes open while completely unresponsive to pain ('dissociative anesthesia'). Ketamine is an antagonist at which of the following central nervous system receptors, and which adverse effect is common during emergence?",
        "options": [
            {"text": "NMDA receptor antagonist; emergence delirium and vivid hallucinations", "is_correct": True},
            {"text": "GABA-A receptor antagonist; status epilepticus", "is_correct": False},
            {"text": "Mu-opioid receptor antagonist; acute opioid withdrawal", "is_correct": False},
            {"text": "D2 dopamine receptor antagonist; acute dystonic reaction", "is_correct": False},
            {"text": "Alpha-2 adrenergic agonist; severe rebound hypertension", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. NMDA receptor antagonist; emergence delirium and vivid hallucinations.\n\nKetamine is an arylcyclohexylamine (chemically related to phencyclidine / PCP) that acts as a non-competitive antagonist of the NMDA glutamate receptor complex. It produces 'dissociative anesthesia' (patient appears awake with open eyes, slow nystagmic gaze, amnesia, catatonia, and profound analgesia). Key properties:\n• Cardiovascular stimulant: Stimulates central sympathetic outflow, increasing HR, BP, and cardiac output (beneficial in shock, harmful in uncontrolled HTN or ischemic heart disease).\n• Respiratory preservation: Minimal respiratory depression, potent bronchodilator (ideal for severe asthma).\n• Adverse effects: Increases intracranial pressure (ICP); during recovery, causes emergence delirium (vivid dreams, hallucinations, disorientation, agitation), which can be prevented by co-administering benzodiazepines (midazolam)."
    },
    {
        "id": "FZ_Q207",
        "question_number": 207,
        "category": "Anesthetic & NMJ Blocking Agents",
        "stem": "A 35-year-old woman is induced with intravenous propofol for an elective laparoscopic cholecystectomy. Within 30 seconds, she falls into a deep hypnotic state. However, if propofol is given as a single bolus without maintenance infusion, she will awaken completely within 8 to 10 minutes. Which of the following pharmacokinetic processes accounts for the rapid termination of propofol's anesthetic effect after a single IV bolus?",
        "options": [
            {"text": "Rapid redistribution of the drug from the highly perfused brain to less vascularized skeletal muscle and adipose tissue", "is_correct": True},
            {"text": "Ultra-rapid hepatic glucuronidation with 100% first-pass clearance", "is_correct": False},
            {"text": "Immediate exhalation through the alveolar membrane into expired air", "is_correct": False},
            {"text": "Enzymatic hydrolysis by plasma pseudocholinesterases in the blood", "is_correct": False},
            {"text": "Rapid renal tubular filtration and excretion in the urine", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Rapid redistribution of the drug from the highly perfused brain to less vascularized skeletal muscle and adipose tissue.\n\nPropofol (like thiopental) is highly lipophilic. Upon IV bolus administration, it distributes preferentially into vessel-rich organs with high blood flow (brain, heart, liver, kidneys), achieving peak brain concentration within 1 minute (rapid induction). Shortly thereafter, blood concentrations drop as the drug redistributes down concentration gradients into vessel-poor, larger-volume peripheral compartments (skeletal muscle, skin, adipose tissue). This rapid REDISTRIBUTION lowers brain concentrations below the threshold for hypnosis, causing the patient to awaken within 5 to 10 minutes. Hepatic metabolism is required for ultimate systemic elimination, but redistribution terminates the clinical hypnotic effect."
    },
    {
        "id": "FZ_Q208",
        "question_number": 208,
        "category": "Anesthetic & NMJ Blocking Agents",
        "stem": "A 60-year-old critically ill patient in the intensive care unit requires mechanical ventilation and sedation. The intensivist selects dexmedetomidine because it provides 'cooperative sedation' (the patient can be easily awakened to follow commands) without depressing respiratory drive. Dexmedetomidine exerts its sedative and hypnotic effects by selectively activating which of the following receptors?",
        "options": [
            {"text": "Alpha-2 adrenergic receptors in the locus coeruleus", "is_correct": True},
            {"text": "GABA-A receptors in the cerebral cortex", "is_correct": False},
            {"text": "Mu-opioid receptors in the periaqueductal gray", "is_correct": False},
            {"text": "5-HT1A serotonin receptors in the dorsal raphe nucleus", "is_correct": False},
            {"text": "H1 histamine receptors in the tuberomammillary nucleus", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Alpha-2 adrenergic receptors in the locus coeruleus.\n\nDexmedetomidine is a highly selective, centrally acting alpha-2 adrenergic receptor agonist (alpha-2:alpha-1 selectivity of 1600:1, compared to 220:1 for clonidine). It acts in the locus coeruleus of the dorsal pons, where it activates presynaptic Gi-coupled alpha-2 receptors to inhibit norepinephrine release. This produces sedation that closely mimics natural non-REM stage 3 sleep, termed 'cooperative sedation' (patients remain easily rousable). Crucially, dexmedetomidine produces minimal to no respiratory depression, making it ideal for weaning intubated ICU patients. Side effects: Bradycardia and hypotension."
    },
    {
        "id": "FZ_Q209",
        "question_number": 209,
        "category": "Anesthetic & NMJ Blocking Agents",
        "stem": "A 40-year-old man receives succinylcholine for rapid sequence intubation. Succinylcholine is a depolarizing neuromuscular blocker that acts as a nicotinic acetylcholine receptor agonist. How does the electrophysiological response to train-of-four (TOF) nerve stimulation differ between a Phase I block and a Phase II block produced by succinylcholine?",
        "options": [
            {"text": "Phase I block shows constant (equal) reduction in twitch height without fade (no post-tetanic facilitation); Phase II block exhibits progressive fade with post-tetanic facilitation", "is_correct": True},
            {"text": "Phase I block shows marked fade; Phase II block shows no fade", "is_correct": False},
            {"text": "Phase I block is reversed by neostigmine; Phase II block is worsened by neostigmine", "is_correct": False},
            {"text": "Phase I block is competitive; Phase II block is allosteric", "is_correct": False},
            {"text": "Phase I block occurs only after prolonged infusion; Phase II block occurs immediately", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Phase I block shows constant (equal) reduction in twitch height without fade (no post-tetanic facilitation); Phase II block exhibits progressive fade with post-tetanic facilitation.\n\nSuccinylcholine neuromuscular blockade:\n• Phase I Block (Depolarizing block): Succinylcholine persistently depolarizes the endplate. On train-of-four (TOF) stimulation, all four twitches are equally reduced in amplitude (NO fade, TOF ratio = 1.0). There is NO post-tetanic facilitation. Acetylcholinesterase inhibitors (neostigmine) PROLONG and worsen Phase I block because they increase synaptic ACh, adding to depolarization.\n• Phase II Block (Desensitization block): With prolonged exposure or high doses, the endplate repolarizes but nicotinic receptors become desensitized. The block now resembles a non-depolarizing block: marked TOF FADE is present, along with post-tetanic potentiation. Phase II block CAN be reversed by AChE inhibitors."
    },
    {
        "id": "FZ_Q210",
        "question_number": 210,
        "category": "Anesthetic & NMJ Blocking Agents",
        "stem": "A 28-year-old woman with severe third-degree burns over 45% of her body surface area sustained 3 weeks ago requires surgery for skin grafting. The surgical resident suggests using succinylcholine for endotracheal intubation, but the attending anesthesiologist firmly objects. Why is succinylcholine strictly contraindicated in patients with extensive burns, denervation injuries, or prolonged immobilization?",
        "options": [
            {"text": "Proliferation of extrajunctional nicotinic acetylcholine receptors across skeletal muscle sarcolemma leads to massive, life-threatening hyperkalemia and cardiac arrest", "is_correct": True},
            {"text": "Burn patients have hyperactive pseudocholinesterases that inactivate the drug within 1 second", "is_correct": False},
            {"text": "Succinylcholine precipitates acute rhabdomyolysis by destroying the Golgi tendon organ", "is_correct": False},
            {"text": "Burn patients have zero nicotinic receptors, making the drug ineffective", "is_correct": False},
            {"text": "It induces acute renal failure by precipitating in collecting tubules", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Proliferation of extrajunctional nicotinic acetylcholine receptors across skeletal muscle sarcolemma leads to massive, life-threatening hyperkalemia and cardiac arrest.\n\nSuccinylcholine is an AChR agonist that opens channels, allowing Na+ to enter and K+ to exit muscle cells. In normal individuals, serum K+ rises by only 0.5 mEq/L. However, in patients with severe burns, spinal cord transection, upper or lower motor neuron denervation, or prolonged immobilization (>48-72 hours post-injury):\n• Denervated or damaged muscle fibers upregulate extrajunctional nicotinic receptors (immature alpha-7 and embryonic gamma-containing nAChRs) across the ENTIRE surface of the sarcolemma (not just at the motor endplate).\n• When succinylcholine is administered, it opens millions of extrajunctional channels simultaneously across the entire body, causing a massive, catastrophic efflux of K+ into the circulation.\n• This precipitates acute lethal hyperkalemia (>8-10 mEq/L), ventricular fibrillation, and cardiac arrest."
    },
    {
        "id": "FZ_Q211",
        "question_number": 211,
        "category": "Anesthetic & NMJ Blocking Agents",
        "stem": "A 58-year-old man with end-stage renal disease (ESRD) on hemodialysis and decompensated cirrhosis with hepatic failure requires general anesthesia for surgery. The anesthesiologist chooses cisatracurium as the neuromuscular blocking agent because its clearance is completely independent of renal and hepatic function. By which of the following unique mechanisms is cisatracurium eliminated from the body?",
        "options": [
            {"text": "Spontaneous non-enzymatic chemical degradation in plasma and tissue at physiological pH and temperature (Hofmann elimination)", "is_correct": True},
            {"text": "Metabolism by hepatic cytochrome P450 3A4 enzymes", "is_correct": False},
            {"text": "Rapid glomerular filtration and active proximal tubular secretion", "is_correct": False},
            {"text": "Hydrolysis by plasma butyrylcholinesterase", "is_correct": False},
            {"text": "Exhalation through the pulmonary alveolar membrane", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Spontaneous non-enzymatic chemical degradation in plasma and tissue at physiological pH and temperature (Hofmann elimination).\n\nCisatracurium (and atracurium) are benzylisoquinolinium non-depolarizing neuromuscular blockers. They undergo Hofmann elimination, a spontaneous, non-enzymatic chemical breakdown in the blood and peripheral tissues that occurs naturally at physiological body temperature (37°C) and physiological pH (7.40) to form laudanosine and monoacrylate metabolites. Because its clearance depends neither on hepatic metabolism nor renal excretion, cisatracurium is the neuromuscular blocking drug of choice in patients with severe renal failure, liver failure, or multisystem organ dysfunction."
    },
    {
        "id": "FZ_Q212",
        "question_number": 212,
        "category": "Anesthetic & NMJ Blocking Agents",
        "stem": "At the conclusion of a surgical procedure under general anesthesia, a patient exhibits residual paralysis from rocuronium with a train-of-four (TOF) ratio of 0.4. Rather than using an acetylcholinesterase inhibitor and an antimuscarinic agent, the anesthesiologist administers sugammadex. What is the mechanism of action by which sugammadex reverses rocuronium neuromuscular blockade?",
        "options": [
            {"text": "It is a modified gamma-cyclodextrin that selectively encapsulates and chelates rocuronium in a 1:1 ratio in the plasma", "is_correct": True},
            {"text": "It acts as a direct competitive agonist at nicotinic acetylcholine receptors", "is_correct": False},
            {"text": "It irreversibly phosphorylates the active site of acetylcholinesterase", "is_correct": False},
            {"text": "It activates renal tubular secretion of rocuronium via organic cation transporters", "is_correct": False},
            {"text": "It stimulates presynaptic vesicular acetylcholine exocytosis", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. It is a modified gamma-cyclodextrin that selectively encapsulates and chelates rocuronium in a 1:1 ratio in the plasma.\n\nSugammadex is a modified gamma-cyclodextrin ring structured with a lipophilic core and a hydrophilic exterior. It acts as a selective relaxant binding agent: it binds with high affinity to the steroidal non-depolarizing NMBAs (rocuronium > vecuronium), encapsulating the drug in a 1:1 complex in plasma. This drastically lowers free rocuronium concentrations, creating a gradient that pulls rocuronium off nicotinic receptors back into the blood, achieving rapid, complete reversal within 2-3 minutes. Because it does not alter acetylcholinesterase, it does not require co-administration of antimuscarinic agents (atropine/glycopyrrolate) and avoids cholinergic side effects."
    },
    {
        "id": "FZ_Q213",
        "question_number": 213,
        "category": "Anesthetic & NMJ Blocking Agents",
        "stem": "A 30-year-old healthy man undergoes an uncomplicated elective procedure using succinylcholine for intubation. Two hours after surgery, he remains completely paralyzed, unable to breathe or move, requiring continued mechanical ventilation in the PACU. A dibucaine number test is performed, which shows a dibucaine inhibition number of 20% (normal >80%). This patient has a genetic deficiency of which of the following enzymes?",
        "options": [
            {"text": "Pseudocholinesterase (butyrylcholinesterase / plasma cholinesterase)", "is_correct": True},
            {"text": "Acetylcholinesterase in the synaptic cleft", "is_correct": False},
            {"text": "Choline acetyltransferase (ChAT)", "is_correct": False},
            {"text": "Cytochrome P450 2D6", "is_correct": False},
            {"text": "Glucose-6-phosphate dehydrogenase (G6PD)", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Pseudocholinesterase (butyrylcholinesterase / plasma cholinesterase).\n\nSuccinylcholine has a normally brief duration of action (5-10 minutes) because >90% of the IV dose is hydrolyzed in the plasma by Pseudocholinesterase (also known as Butyrylcholinesterase or plasma cholinesterase, synthesized by the liver) before reaching the neuromuscular junction. Individuals with atypical pseudocholinesterase (autosomal recessive BCHE gene variants) cannot metabolize succinylcholine or mivacurium, leading to prolonged apnea and flaccid paralysis lasting several hours. The dibucaine test differentiates normal from atypical enzyme: dibucaine inhibits normal pseudocholinesterase by >80% (dibucaine number >80), but inhibits atypical enzyme by only ~20%."
    },
    {
        "id": "FZ_Q214",
        "question_number": 214,
        "category": "Anesthetic & NMJ Blocking Agents",
        "stem": "Local anesthetics are classified chemically into esters and amides based on their intermediate chain linkage. Which of the following local anesthetics is an ester that is metabolized by plasma pseudocholinesterases into para-aminobenzoic acid (PABA), which can trigger severe allergic hypersensitivity reactions?",
        "options": [
            {"text": "Procaine (or Tetracaine / Benzocaine)", "is_correct": True},
            {"text": "Lidocaine", "is_correct": False},
            {"text": "Bupivacaine", "is_correct": False},
            {"text": "Ropivacaine", "is_correct": False},
            {"text": "Mepivacaine", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Procaine (or Tetracaine / Benzocaine).\n\nLocal anesthetics classification rule:\n• Amides have TWO 'i's in their generic name: L-i-doca-i-ne, Bup-i-vaca-i-ne, Rop-i-vaca-i-ne, Mep-i-vaca-i-ne, Pr-i-loca-i-ne. They are metabolized by hepatic CYP450 enzymes; true allergic reactions to amides are exceptionally rare.\n• Esters have ONE 'i' in their generic name: Proca-i-ne, Tetraca-i-ne, Benzoca-i-ne, Coca-i-ne, Chloroproca-i-ne. Esters are hydrolyzed in the blood by plasma pseudocholinesterases into para-aminobenzoic acid (PABA). PABA is an immunogenic hapten that can trigger IgE-mediated Type I anaphylactic or Type IV hypersensitivity allergic reactions."
    },
    {
        "id": "FZ_Q215",
        "question_number": 215,
        "category": "Anesthetic & NMJ Blocking Agents",
        "stem": "A 32-year-old pregnant woman receives an epidural infusion of bupivacaine during labor. Shortly after an accidental intravascular catheter migration and bolus injection, she experiences a metallic taste, tinnitus, and perioral numbness, followed immediately by severe refractory ventricular fibrillation and cardiovascular collapse. Which of the following treatments is the specific rescue lipid emulsion therapy for bupivacaine cardiotoxicity?",
        "options": [
            {"text": "Intravenous 20% lipid emulsion (Intralipid)", "is_correct": True},
            {"text": "Intravenous methylene blue", "is_correct": False},
            {"text": "Intravenous pralidoxime", "is_correct": False},
            {"text": "Intravenous flumazenil", "is_correct": False},
            {"text": "Intravenous calcium gluconate", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Intravenous 20% lipid emulsion (Intralipid).\n\nBupivacaine is an amide local anesthetic known for severe cardiotoxicity. It is highly lipophilic and dissociates very slowly from cardiac voltage-gated Na+ channels during diastole ('fast in, slow out'), leading to severe conduction block, intractable ventricular arrhythmias, and myocardial depression. The rescue treatment for local anesthetic systemic toxicity (LAST) is immediate administration of IV 20% lipid emulsion (Intralipid). Mechanisms of lipid rescue:\n• 'Lipid sink' phenomenon: The lipid emulsion creates an intravascular lipid phase that rapidly extracts and sequesters lipophilic bupivacaine from cardiac myocytes.\n• Metabolic activation: Lipids provide direct fatty acid energy substrate to the stunned myocardium."
    },
    {
        "id": "FZ_Q216",
        "question_number": 216,
        "category": "Anesthetic & NMJ Blocking Agents",
        "stem": "A 19-year-old college student presents to the emergency department with cyanosis and shortness of breath after using a topical benzocaine throat spray for severe pharyngitis. Pulse oximetry reveals an oxygen saturation of 85% that does not improve despite breathing 100% supplemental oxygen via a non-rebreather mask. Arterial blood gas draws dark, chocolate-brown colored blood. Co-oximetry reveals 35% methemoglobin. Which of the following is the specific antidote for benzocaine-induced methemoglobinemia?",
        "options": [
            {"text": "Methylene blue", "is_correct": True},
            {"text": "N-acetylcysteine", "is_correct": False},
            {"text": "Deferoxamine", "is_correct": False},
            {"text": "Dimercaprol", "is_correct": False},
            {"text": "Atropine", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Methylene blue.\n\nTopical oxidizing local anesthetics (especially benzocaine and prilocaine) oxidize the iron in hemoglobin from the normal ferrous state (Fe2+) to the ferric state (Fe3+), forming Methemoglobin. Hallmarks of methemoglobinemia:\n• Methemoglobin cannot bind oxygen, and it shifts the oxygen-hemoglobin dissociation curve to the left, impeding oxygen release to tissues.\n• Patients present with cyanosis, dyspnea, and headache.\n• Blood appears dark 'chocolate-brown' and does not turn red upon exposure to air.\n• Standard pulse oximetry reads ~85% regardless of true arterial PO2, and cyanosis is refractory to 100% O2.\n• Antidote: Intravenous METHYLENE BLUE (1-2 mg/kg), which acts as an electron acceptor for NADPH-methemoglobin reductase to reduce Fe3+ back to Fe2+."
    },
    {
        "id": "FZ_Q217",
        "question_number": 217,
        "category": "Anesthetic & NMJ Blocking Agents",
        "stem": "A dental surgeon injects 2% lidocaine with 1:100,000 epinephrine before a tooth extraction. What is the pharmacological rationale for co-administering epinephrine with local anesthetics?",
        "options": [
            {"text": "Epinephrine stimulates alpha-1 adrenergic receptors, producing local vasoconstriction that slows systemic absorption, prolongs duration of anesthesia, and reduces bleeding", "is_correct": True},
            {"text": "Epinephrine acts as an allosteric agonist at voltage-gated sodium channels", "is_correct": False},
            {"text": "Epinephrine lowers tissue pH to accelerate local anesthetic protonation", "is_correct": False},
            {"text": "Epinephrine inhibits plasma pseudocholinesterases", "is_correct": False},
            {"text": "Epinephrine blocks central NMDA receptors to induce procedural amnesia", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Epinephrine stimulates alpha-1 adrenergic receptors, producing local vasoconstriction that slows systemic absorption, prolongs duration of anesthesia, and reduces bleeding.\n\nEpinephrine is frequently combined with local anesthetics (e.g., lidocaine, bupivacaine). By stimulating vascular alpha-1 adrenergic receptors, it causes intense local arteriolar vasoconstriction. This achieves three clinical goals:\n1. Decreases systemic absorption of the local anesthetic, drastically reducing peak blood levels and risk of systemic toxicity (seizures, arrhythmias).\n2. Prolongs the duration of local anesthesia (by keeping the drug localized at the nerve).\n3. Minimizes local surgical bleeding.\nContraindication: Avoid injecting epinephrine into anatomical regions with terminal end-artery vascular supply (fingers, toes, tip of nose, ears, and penis) due to the risk of severe ischemic necrosis."
    },
    {
        "id": "FZ_Q218",
        "question_number": 218,
        "category": "Anesthetic & NMJ Blocking Agents",
        "stem": "When a local anesthetic is injected around a peripheral mixed nerve, different functional modalities are blocked at different rates. Which of the following sequences represents the typical clinical order of functional loss during local anesthetic nerve conduction blockade?",
        "options": [
            {"text": "Pain (small unmyelinated/thinly myelinated fibers) -> Temperature -> Touch -> Motor function (large myelinated fibers)", "is_correct": True},
            {"text": "Motor function -> Touch -> Temperature -> Pain", "is_correct": False},
            {"text": "Proprioception -> Motor -> Pain -> Autonomic", "is_correct": False},
            {"text": "Touch -> Pain -> Motor -> Temperature", "is_correct": False},
            {"text": "Motor and pain are blocked simultaneously with touch preserved", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Pain (small unmyelinated/thinly myelinated fibers) -> Temperature -> Touch -> Motor function (large myelinated fibers).\n\nSusceptibility of nerve fibers to local anesthetic blockade is determined by fiber diameter, presence of myelin, and firing frequency:\n• Small-diameter fibers are blocked more readily than large-diameter fibers.\n• Myelinated fibers are blocked more readily than unmyelinated fibers of the same diameter (because blocking 2 to 3 successive nodes of Ranvier halts saltatory conduction).\n• High-frequency firing nerves are blocked faster (use-dependence).\nTypical order of clinical sensory/motor loss:\nPain (small A-delta and C fibers) → Temperature → Touch/Pressure (A-beta fibers) → Skeletal motor function (large A-alpha fibers last). Recovery occurs in the exact reverse order."
    },
    {
        "id": "FZ_Q219",
        "question_number": 219,
        "category": "Anesthetic & NMJ Blocking Agents",
        "stem": "A 42-year-old woman develops fulminant hepatic failure 6 days after undergoing surgery under general anesthesia with halothane in another country. Autopsy reveals massive centrilobular hepatic necrosis, and laboratory testing reveals antibodies directed against trifluoroacetylated liver microsomal proteins. What is the mechanism of halothane hepatitis?",
        "options": [
            {"text": "Immune-mediated hypersensitivity reaction triggered by trifluoroacetylated liver proteins formed during hepatic metabolism of halothane", "is_correct": True},
            {"text": "Direct non-immunological necrosis of bile canaliculi by fluoride ions", "is_correct": False},
            {"text": "Overactivation of the ryanodine receptor in hepatocytes", "is_correct": False},
            {"text": "Inactivation of alpha-1 antitrypsin in the endoplasmic reticulum", "is_correct": False},
            {"text": "Occlusion of the hepatic veins (Budd-Chiari syndrome)", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Immune-mediated hypersensitivity reaction triggered by trifluoroacetylated liver proteins formed during hepatic metabolism of halothane.\n\nHalothane undergoes significant oxidative metabolism (~20-25%) by hepatic CYP2E1, forming a reactive trifluoroacetyl chloride intermediate. This reactive metabolite covalently binds to hepatic microsomal proteins, forming neoantigens. In genetically susceptible individuals (especially after repeated exposures), the immune system mounts a humoral and cell-mediated immune response against these trifluoroacetylated proteins, causing fulminant autoimmune hepatitis. Histopathology shows massive centrilobular hepatic necrosis, with high mortality (~50-80%). Modern volatile agents (desflurane, sevoflurane) undergo minimal metabolism (<0.02-2%) and rarely cause hepatitis."
    },
    {
        "id": "FZ_Q220",
        "question_number": 220,
        "category": "Anesthetic & NMJ Blocking Agents",
        "stem": "A patient with severe chronic obstructive pulmonary disease (COPD) is being ventilated. The physician wishes to administer an inhaled anesthetic but recalls that nitrous oxide (N2O) is contraindicated in certain clinical conditions. Which of the following physical properties explains why nitrous oxide rapidly expands closed, air-filled gas cavities (such as a pneumothorax, bowel obstruction, or middle ear surgery)?",
        "options": [
            {"text": "Nitrous oxide is 34 times more soluble in blood than nitrogen, diffusing into air-filled closed cavities faster than nitrogen can diffuse out", "is_correct": True},
            {"text": "Nitrous oxide reacts with oxygen to form nitric acid gas that occupies large volumes", "is_correct": False},
            {"text": "Nitrous oxide has a molecular weight lower than helium", "is_correct": False},
            {"text": "Nitrous oxide triggers massive carbon dioxide production by activating carbonic anhydrase", "is_correct": False},
            {"text": "Nitrous oxide causes severe pulmonary vasodilation that traps atmospheric air", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Nitrous oxide is 34 times more soluble in blood than nitrogen, diffusing into air-filled closed cavities faster than nitrogen can diffuse out.\n\nNitrous oxide (N2O) is approximately 34 times more soluble in blood than molecular nitrogen (N2). When a patient inhales N2O, large quantities of dissolved N2O in the bloodstream rapidly diffuse into any closed, air-containing gas cavity in the body. However, because nitrogen inside the cavity is poorly soluble in blood, it diffuses out into the circulation very slowly. This net influx of gas causes rapid expansion of volume or massive pressure elevation in closed spaces. Nitrous oxide is strictly contraindicated in pneumothorax, closed loop bowel obstruction, middle ear surgery, air embolism, and intraocular gas bubble procedures."
    },

    # =========================================================================
    # TOPIC 12: Headache (FZ_Q221 - FZ_Q240)
    # =========================================================================
    {
        "id": "FZ_Q221",
        "question_number": 221,
        "category": "Headache",
        "stem": "A 26-year-old woman presents with recurrent, unilateral, throbbing headaches that last 12 to 24 hours. The headache is preceded by 20 minutes of shimmering, zigzag visual lines (fortification spectra / scintillating scotoma) in her right visual field. During the headache, she experiences nausea, photophobia, and phonophobia, and prefers to rest in a dark, quiet room. At the neurobiological level, which of the following phenomena is responsible for the visual aura that precedes migraine attacks?",
        "options": [
            {"text": "Cortical spreading depression (CSD)", "is_correct": True},
            {"text": "Acute spasm of the ophthalmic artery causing retinal ischemia", "is_correct": False},
            {"text": "Dural venous sinus microthrombosis", "is_correct": False},
            {"text": "Transient occlusion of the basilar artery", "is_correct": False},
            {"text": "Hyperpolarization of cerebellar Purkinje cells", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Cortical spreading depression (CSD).\n\nMigraine with aura is mediated by Cortical Spreading Depression (CSD):\n• A self-propagating wave of slow cellular depolarization (traveling at 2-5 mm/min across the cerebral cortex, typically occipital), followed by prolonged neuronal and glial suppression.\n• The initial wave of depolarization triggers visual scintillating scotomas (aura), while the subsequent activation of meningeal trigeminal perivascular nerves stimulates the release of pro-inflammatory neuropeptides (CGRP, substance P), causing neurogenic vasodilation and throbbing headache."
    },
    {
        "id": "FZ_Q222",
        "question_number": 222,
        "category": "Headache",
        "stem": "During a severe acute migraine attack, activation of the trigeminovascular system causes the release of vasoactive neuropeptides from perivascular trigeminal nerve endings surrounding dural blood vessels. Which of the following potent vasodilatory neuropeptides is the primary driver of neurogenic inflammation in migraine, serving as the target for both monoclonal antibodies and gepants?",
        "options": [
            {"text": "Calcitonin Gene-Related Peptide (CGRP)", "is_correct": True},
            {"text": "Endothelin-1", "is_correct": False},
            {"text": "Angiotensin II", "is_correct": False},
            {"text": "Thromboxane A2", "is_correct": False},
            {"text": "Neuropeptide Y", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Calcitonin Gene-Related Peptide (CGRP).\n\nCalcitonin Gene-Related Peptide (CGRP) is a 37-amino acid neuropeptide synthesized in trigeminal ganglion sensory neurons. Upon activation of the trigeminovascular system, CGRP is released around meningeal blood vessels, where it produces intense cranial vasodilation, mast cell degranulation, and neurogenic plasma extravasation. Plasma CGRP levels spike during acute migraine attacks. Modern migraine therapeutics specifically target CGRP:\n• Small-molecule CGRP receptor antagonists (gepants: rimegepant, ubrogepant) for acute treatment.\n• Monoclonal antibodies against CGRP receptor (erenumab) or CGRP ligand (galcanezumab, fremanezumab) for migraine prevention."
    },
    {
        "id": "FZ_Q223",
        "question_number": 223,
        "category": "Headache",
        "stem": "A 34-year-old woman presents with severe migraine attacks. The physician considers prescribing sumatriptan for acute abortive therapy. Sumatriptan acts as an agonist at 5-HT1B and 5-HT1D receptors. Because of its pharmacological mechanism, sumatriptan is strictly contraindicated in patients with which of the following medical conditions?",
        "options": [
            {"text": "Coronary artery disease, Prinzmetal angina, or uncontrolled hypertension", "is_correct": True},
            {"text": "Chronic bronchial asthma", "is_correct": False},
            {"text": "Type 2 diabetes mellitus", "is_correct": False},
            {"text": "Osteoarthritis of the knees", "is_correct": False},
            {"text": "Chronic allergic rhinitis", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Coronary artery disease, Prinzmetal angina, or uncontrolled hypertension.\n\nTriptans (sumatriptan, zolmitriptan, rizatriptan) are selective 5-HT1B/1D receptor agonists used for acute moderate-to-severe migraine attacks:\n• 5-HT1B receptors are located on vascular smooth muscle of cranial blood vessels; activation causes vasoconstriction.\n• 5-HT1D receptors are located presynaptically on trigeminal nerve terminals; activation blocks the release of CGRP and substance P.\nBecause 5-HT1B receptors are also expressed on coronary arteries, triptans can cause coronary artery vasoconstriction and vasospasm. They are strictly contraindicated in patients with coronary artery disease, history of myocardial infarction, Prinzmetal (vasospastic) angina, uncontrolled hypertension, peripheral vascular disease, or basilar/hemiplegic migraine."
    },
    {
        "id": "FZ_Q224",
        "question_number": 224,
        "category": "Headache",
        "stem": "A 40-year-old man who smokes 1 pack of cigarettes daily presents with excruciating headaches that occur in cycles lasting 6 to 8 weeks every autumn. The pain is strictly unilateral, sharp, and centered behind his right eye ('ice-pick in the eye'). The attacks last 45 minutes and occur 2 to 3 times per day, characteristically awakening him from sleep at 2:00 AM. During attacks, he exhibits right-sided conjunctival injection, profuse lacrimation, rhinorrhea, and mild ptosis with miosis. He paces the room restlessly. Which of the following is the first-line acute abortive therapy for cluster headache?",
        "options": [
            {"text": "100% High-Flow Oxygen via non-rebreather face mask (and subcutaneous sumatriptan)", "is_correct": True},
            {"text": "Oral acetaminophen and caffeine", "is_correct": False},
            {"text": "Intramuscular ketorolac", "is_correct": False},
            {"text": "Oral amitriptyline", "is_correct": False},
            {"text": "Intravenous mannitol", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. 100% High-Flow Oxygen via non-rebreather face mask (and subcutaneous sumatriptan).\n\nCluster headache is a Trigeminal Autonomic Cephalalgia (TAC) predominantly affecting young-to-middle-aged male smokers. Hallmarks:\n• Severe, strictly unilateral retro-orbital pain ('suicide headache') lasting 15 to 180 minutes.\n• Circadian regularity (attacks occur at the exact same hour, often awakening patient during REM sleep due to hypothalamic activation).\n• Ipsilateral cranial autonomic symptoms (lacrimation, conjunctival injection, nasal congestion, partial Horner syndrome [ptosis/miosis]).\n• Marked motor agitation (patients pace, rock, or hit their head, unlike migraineurs who lie still in the dark).\nAcute first-line treatment: 100% High-Flow Oxygen (12-15 L/min via non-rebreather mask for 15 minutes) and subcutaneous Sumatriptan (6 mg). Prophylaxis: Verapamil is first-line."
    },
    {
        "id": "FZ_Q225",
        "question_number": 225,
        "category": "Headache",
        "stem": "In the patient described above with frequent episodic cluster headaches, which of the following medications is considered the first-line preventive (prophylactic) therapy of choice, requiring periodic baseline and follow-up electrocardiographic monitoring for PR prolongation?",
        "options": [
            {"text": "Verapamil", "is_correct": True},
            {"text": "Propranolol", "is_correct": False},
            {"text": "Amitriptyline", "is_correct": False},
            {"text": "Valproate", "is_correct": False},
            {"text": "Topiramate", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Verapamil.\n\nVerapamil (a non-dihydropyridine calcium channel blocker) is the first-line maintenance prophylactic drug for cluster headache. It prevents attacks by modulating hypothalamic calcium channels and stabilizing cranial vascular tone. Because high doses (240 to 960 mg/day) are required to cross the blood-brain barrier and achieve cluster prophylaxis, verapamil can cause bradycardia, AV block, and PR interval prolongation on ECG. A baseline ECG and routine follow-up ECGs are mandatory during dose titration."
    },
    {
        "id": "FZ_Q226",
        "question_number": 226,
        "category": "Headache",
        "stem": "A 30-year-old software engineer presents with frequent headaches at the end of long workdays. He describes the pain as a dull, constant, aching band-like pressure wrapping around both sides of his forehead and occiput ('tight headband'). The headache is of mild-to-moderate intensity, is not aggravated by climbing stairs, and is not accompanied by nausea, vomiting, or focal visual disturbances. Palpation of the pericranial muscles reveals tenderness. Which of the following is the most likely diagnosis?",
        "options": [
            {"text": "Tension-type headache", "is_correct": True},
            {"text": "Migraine without aura", "is_correct": False},
            {"text": "Cluster headache", "is_correct": False},
            {"text": "Idiopathic intracranial hypertension", "is_correct": False},
            {"text": "Temporal arteritis", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Tension-type headache.\n\nTension-type headache is the most common primary headache disorder (>70% lifetime prevalence). Diagnostic criteria:\n• Bilateral location (forehead, temples, or occiput).\n• Quality: Pressing or tightening (non-pulsatile), often described as a tight vise or band around the head.\n• Mild to moderate intensity (does not prohibit daily activities).\n• NOT aggravated by routine physical activity (walking, climbing stairs).\n• NO nausea or vomiting; no more than one of photophobia or phonophobia.\n• Associated with pericranial myofascial tenderness in the neck and shoulders.\nAcute treatment: NSAIDs (ibuprofen, naproxen) or acetaminophen. Prophylaxis: Amitriptyline (TCA) for chronic tension headaches (>15 days/month)."
    },
    {
        "id": "FZ_Q227",
        "question_number": 227,
        "category": "Headache",
        "stem": "A 72-year-old woman presents with severe, aching pain localized to her right temple over the past 2 weeks. She reports severe pain when brushing her hair (scalp tenderness) and fatigue in her jaw muscles when chewing meat (jaw claudication). Laboratory testing reveals an Erythrocyte Sedimentation Rate (ESR) of 105 mm/hr (normal <30) and C-reactive protein (CRP) of 45 mg/L. Which of the following is the most critical immediate management step to prevent permanent blindness?",
        "options": [
            {"text": "Immediate administration of high-dose systemic corticosteroids (prednisone or methylprednisolone) prior to performing a temporal artery biopsy", "is_correct": True},
            {"text": "Withhold all treatment until a 2 cm temporal artery biopsy is obtained and histologically confirmed", "is_correct": False},
            {"text": "Prescribe oral sumatriptan and high-flow oxygen", "is_correct": False},
            {"text": "Perform a diagnostic lumbar puncture to check opening pressure", "is_correct": False},
            {"text": "Administer intravenous mannitol and acetazolamide", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Immediate administration of high-dose systemic corticosteroids (prednisone or methylprednisolone) prior to performing a temporal artery biopsy.\n\nGiant Cell (Temporal) Arteritis is a granulomatous vasculitis affecting medium and large branches of the carotid artery in patients >50 years old (associated with polymyalgia rheumatica). Hallmarks:\n• New headache (typically unilateral temporal), scalp tenderness, jaw claudication, markedly elevated ESR and CRP.\n• Feared complication: Irreversible visual loss due to Anterior Ischemic Optic Neuropathy (AION) caused by occlusion of the ophthalmic artery and posterior ciliary arteries.\n• Management: Immediate high-dose systemic corticosteroids (prednisone 60 mg/day or IV methylprednisolone if visual symptoms are present) must be initiated IMMEDIATELY upon clinical suspicion. Never delay steroids to obtain a temporal artery biopsy, as biopsy findings remain diagnostic for up to 2-4 weeks after starting steroids."
    },
    {
        "id": "FZ_Q228",
        "question_number": 228,
        "category": "Headache",
        "stem": "A temporal artery biopsy is performed on a patient with suspected giant cell arteritis. Histopathological examination of the excised vessel wall confirms the diagnosis. Which of the following microscopic findings is characteristic of giant cell arteritis?",
        "options": [
            {"text": "Granulomatous inflammation of the tunica media with fragmentation of the internal elastic lamina and multinucleated giant cells", "is_correct": True},
            {"text": "Transmural necrotizing inflammation with fibrinoid necrosis and leukocytoclasia sparing the internal elastic lamina", "is_correct": False},
            {"text": "Extensive lipid-laden foam cells in the subendothelial space without inflammatory infiltrates", "is_correct": False},
            {"text": "Hyaline arteriolosclerosis with concentric onion-skinning", "is_correct": False},
            {"text": "Non-inflammatory fibromuscular dysplasia with alternating luminal narrowing", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Granulomatous inflammation of the tunica media with fragmentation of the internal elastic lamina and multinucleated giant cells.\n\nHistopathology of Giant Cell Arteritis:\n• Focal, segmental granulomatous inflammation centered on the internal elastic lamina of medium-to-large elastic and muscular arteries.\n• Infiltration of T cells and macrophages.\n• Fragmentation, duplication, and disruption of the internal elastic lamina.\n• Multinucleated giant cells (seen in ~75% of positive biopsies).\n• Intimal hyperplasia leading to luminal narrowing and distal ischemia.\nBecause the disease is segmental ('skip lesions'), a generous biopsy length (>2-3 cm) is required to avoid false negatives."
    },
    {
        "id": "FZ_Q229",
        "question_number": 229,
        "category": "Headache",
        "stem": "A 42-year-old woman with a history of episodic migraines presents with a daily, unremitting dull headache that is present upon awakening each morning. Over the past 6 months, she has been taking over-the-counter combination analgesics (acetaminophen-aspirin-caffeine) 5 days per week and sumatriptan 3 days per week. She notes that the medications provide brief relief for 3 to 4 hours, after which the headache rebounds with greater intensity. Which of the following is the definitive management of this medication overuse (rebound) headache?",
        "options": [
            {"text": "Complete withdrawal and discontinuation of all overused acute abortive medications and initiation of prophylactic migraine therapy", "is_correct": True},
            {"text": "Switching to daily long-acting oral opioid therapy", "is_correct": False},
            {"text": "Increasing the frequency of daily sumatriptan doses", "is_correct": False},
            {"text": "Performing daily therapeutic lumbar punctures", "is_correct": False},
            {"text": "Initiating high-dose oral acetazolamide indefinitely", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Complete withdrawal and discontinuation of all overused acute abortive medications and initiation of prophylactic migraine therapy.\n\nMedication Overuse Headache (MOH / Rebound Headache) occurs in patients with pre-existing primary headache disorders (migraine or tension headache) who excessively consume acute abortive medications:\n• Regular intake of simple analgesics (NSAIDs, acetaminophen) on ≥15 days/month, or triptans, opioids, ergotamines, or combination analgesics on ≥10 days/month for >3 months.\n• Manifests as a chronic daily headache present upon awakening, perpetuated by withdrawal between doses.\n• Management: Complete discontinuation/weaning of the offending acute medication (warning the patient of a transient withdrawal headache flare lasting 1-2 weeks), bridge therapy (steroid taper), and initiation of preventive migraine prophylaxis (topiramate, beta-blocker, or CGRP antibody)."
    },
    {
        "id": "FZ_Q230",
        "question_number": 230,
        "category": "Headache",
        "stem": "A 28-year-old woman with frequent, disabling migraines (6 attacks per month) is started on topiramate for migraine prevention. At a follow-up visit 2 months later, she reports substantial reduction in headache frequency, but complains of word-finding difficulties, cognitive slowing ('feeling foggy'), paresthesias in her fingers, and a 12-pound weight loss. Laboratory testing reveals mild metabolic acidosis and a newly diagnosed calcium phosphate renal stone. Which of the following mechanisms explains topiramate's adverse effect profile?",
        "options": [
            {"text": "Blockade of voltage-gated sodium channels, enhancement of GABA-A, antagonism of AMPA/kainate, and mild carbonic anhydrase inhibition", "is_correct": True},
            {"text": "Direct agonism of mu-opioid receptors and inhibition of acetylcholinesterase", "is_correct": False},
            {"text": "Selective antagonism of beta-1 adrenergic receptors in the sinoatrial node", "is_correct": False},
            {"text": "Irreversible inhibition of DOPA decarboxylase", "is_correct": False},
            {"text": "Competitive inhibition of dihydrofolate reductase", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Blockade of voltage-gated sodium channels, enhancement of GABA-A, antagonism of AMPA/kainate, and mild carbonic anhydrase inhibition.\n\nTopiramate is a broad-spectrum anticonvulsant and first-line migraine prophylactic drug. Mechanisms:\n1. Blocks voltage-gated Na+ channels.\n2. Potentiates GABA-A receptor chloride currents.\n3. Antagonizes AMPA/kainate glutamate receptors.\n4. Mild carbonic anhydrase inhibitor.\nAdverse effects:\n• Cognitive slowing, memory impairment, and word-finding difficulty (often called 'Dopamax').\n• Anorexia and significant weight loss.\n• Distal paresthesias (tingling in hands/feet).\n• Carbonic anhydrase inhibition causes metabolic acidosis (low bicarbonate) and alkalinizes the urine, increasing the risk of nephrolithiasis (calcium phosphate kidney stones).\n• Acute myopia and secondary angle-closure glaucoma."
    },
    {
        "id": "FZ_Q231",
        "question_number": 231,
        "category": "Headache",
        "stem": "A 24-year-old woman presents to the emergency department with a sudden, explosive headache that reached maximal intensity within 30 seconds of onset ('thunderclap headache'). Non-contrast head CT performed 4 hours after headache onset is completely normal. What is the mandatory next diagnostic step to definitively rule out a ruptured saccular aneurysm and subarachnoid hemorrhage?",
        "options": [
            {"text": "Lumbar puncture to evaluate for elevated opening pressure, persistent red blood cells, and xanthochromia", "is_correct": True},
            {"text": "Discharge home with an oral triptan and follow-up in 2 weeks", "is_correct": False},
            {"text": "Repeat non-contrast head CT in 24 hours", "is_correct": False},
            {"text": "Electroencephalogram (EEG)", "is_correct": False},
            {"text": "Carotid duplex ultrasound", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Lumbar puncture to evaluate for elevated opening pressure, persistent red blood cells, and xanthochromia.\n\nA thunderclap headache (peaking within <1 minute) is the classic hallmark of subarachnoid hemorrhage (SAH). While non-contrast head CT is >95-98% sensitive within the first 6 hours, sensitivity declines to ~85% at 24 hours and <50% at 1 week. If non-contrast CT is normal, a Lumbar Puncture is mandatory. In SAH, CSF analysis reveals elevated opening pressure, high RBC count that does NOT clear between collection tubes 1 and 4, and XANTHOCHROMIA (a pink or yellow supernatant caused by bilirubin from enzymatic breakdown of RBCs, detected via spectrophotometry 6-12 hours post-hemorrhage)."
    },
    {
        "id": "FZ_Q232",
        "question_number": 232,
        "category": "Headache",
        "stem": "Which of the following medications is a humanized monoclonal antibody that selectively binds to the Calcitonin Gene-Related Peptide (CGRP) RECEPTOR, rather than the CGRP ligand, administered as a monthly subcutaneous injection for the prevention of migraine?",
        "options": [
            {"text": "Erenumab", "is_correct": True},
            {"text": "Galcanezumab", "is_correct": False},
            {"text": "Fremanezumab", "is_correct": False},
            {"text": "Eptinezumab", "is_correct": False},
            {"text": "Rimegepant", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Erenumab.\n\nCGRP-targeted monoclonal antibodies for migraine prevention:\n• Erenumab is a fully human monoclonal antibody that selectively binds and blocks the CGRP RECEPTOR (calcRL/RAMP1 complex).\n• Galcanezumab, Fremanezumab, and Eptinezumab are monoclonal antibodies that bind directly to the circulating CGRP LIGAND itself.\n• Rimegepant and Ubrogepant are small-molecule oral CGRP receptor antagonists (gepants), not monoclonal antibodies."
    },
    {
        "id": "FZ_Q233",
        "question_number": 233,
        "category": "Headache",
        "stem": "A 32-year-old woman with severe migraine headaches cannot tolerate triptans due to coronary vasospasm and a history of myocardial infarction. The neurologist prescribes lasmiditan for acute treatment. Lasmiditan is a 'ditan' that selectively activates which of the following serotonin receptor subtypes, successfully aborting migraine without causing vasoconstriction of coronary or cerebral arteries?",
        "options": [
            {"text": "5-HT1F receptor", "is_correct": True},
            {"text": "5-HT1B receptor", "is_correct": False},
            {"text": "5-HT1D receptor", "is_correct": False},
            {"text": "5-HT2A receptor", "is_correct": False},
            {"text": "5-HT3 receptor", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. 5-HT1F receptor.\n\nLasmiditan is a high-affinity, selective 5-HT1F receptor agonist (a 'ditan'). Unlike triptans (which bind 5-HT1B and 5-HT1D receptors and produce vascular smooth muscle vasoconstriction), 5-HT1F receptors are located exclusively on central and peripheral trigeminal neurons and do NOT produce vasoconstriction. Activating 5-HT1F inhibits trigeminal calcitonin gene-related peptide (CGRP) release and blocks central pain transmission. Lasmiditan is FDA-approved for acute migraine abortive therapy in patients with cardiovascular disease, coronary artery disease, or uncontrolled hypertension."
    },
    {
        "id": "FZ_Q234",
        "question_number": 234,
        "category": "Headache",
        "stem": "A 48-year-old man presents with sharp, excruciating, unilateral headache attacks localized to the temple that occur 15 to 20 times per day, lasting 10 to 20 minutes each. The attacks are accompanied by ipsilateral conjunctival injection and rhinorrhea. He is treated with a 48-hour trial of oral indomethacin, which produces complete and rapid abolition of all headache attacks. Which of the following Trigeminal Autonomic Cephalalgias is defined by this absolute therapeutic response to indomethacin?",
        "options": [
            {"text": "Paroxysmal hemicrania", "is_correct": True},
            {"text": "Episodic cluster headache", "is_correct": False},
            {"text": "Tension-type headache", "is_correct": False},
            {"text": "Migraine with brainstem aura", "is_correct": False},
            {"text": "Temporal arteritis", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Paroxysmal hemicrania.\n\nParoxysmal hemicrania is a Trigeminal Autonomic Cephalalgia (TAC) with key differences from cluster headache:\n• Shorter duration: Attacks last 2 to 30 minutes (cluster attacks last 15-180 minutes).\n• Higher frequency: Occur >5 to 20 times per day (cluster attacks occur 1-8 times/day).\n• Female predominance (cluster has male predominance).\n• Hallmark diagnostic criterion: Complete, prompt, absolute response to therapeutic doses of Indomethacin (an NSAID), which is diagnostic ('indomethacin-responsive headache')."
    },
    {
        "id": "FZ_Q235",
        "question_number": 235,
        "category": "Headache",
        "stem": "A 21-year-old college student presents with throbbing headaches, nausea, and vomiting. He mentions that his mother and maternal uncle suffer from similar episodes that are accompanied by temporary unilateral hemiparesis and ataxia. Genetic sequencing reveals a missense mutation in the CACNA1A gene encoding the pore-forming alpha-1A subunit of neuronal Cav2.1 (P/Q-type) voltage-gated calcium channels. Which of the following is the diagnosis?",
        "options": [
            {"text": "Familial Hemiplegic Migraine type 1 (FHM1)", "is_correct": True},
            {"text": "Huntington disease", "is_correct": False},
            {"text": "Friedreich ataxia", "is_correct": False},
            {"text": "Spinocerebellar ataxia type 3", "is_correct": False},
            {"text": "Lambert-Eaton myasthenic syndrome", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Familial Hemiplegic Migraine type 1 (FHM1).\n\nFamilial Hemiplegic Migraine (FHM) is an autosomal dominant subtype of migraine with aura characterized by reversible motor weakness (hemiparesis) during the aura phase:\n• FHM1 (~50% of cases): Caused by gain-of-function mutations in CACNA1A (chromosome 19p), encoding the alpha-1A pore subunit of P/Q-type voltage-gated calcium channels (Cav2.1). Increased calcium influx causes excessive cortical glutamate release, lowering the threshold for cortical spreading depression.\n• FHM2: Mutations in ATP1A2 (alpha-2 subunit of Na+/K+ ATPase).\n• FHM3: Mutations in SCN1A (voltage-gated Na+ channel Nav1.1)."
    },
    {
        "id": "FZ_Q236",
        "question_number": 236,
        "category": "Headache",
        "stem": "A 35-year-old woman presents to the clinic with chronic daily headaches. In evaluating secondary headache disorders, the physician reviews the 'SNOOP' mnemonic for dangerous headache red flags. Which of the following clinical features represents a 'red flag' requiring emergent neuroimaging and lumbar puncture?",
        "options": [
            {"text": "Sudden onset 'thunderclap' headache, systemic symptoms (fever, weight loss), focal neurological deficits, or new headache in an immunocompromised patient", "is_correct": True},
            {"text": "Bilateral band-like pressure after 8 hours of computer work", "is_correct": False},
            {"text": "Unilateral throbbing headache that resolves after 2 hours of sleep in a dark room", "is_correct": False},
            {"text": "Headache that worsens with menstruation and improves with NSAIDs", "is_correct": False},
            {"text": "Pericranial muscle tightness that resolves with neck massage", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Sudden onset 'thunderclap' headache, systemic symptoms (fever, weight loss), focal neurological deficits, or new headache in an immunocompromised patient.\n\nThe 'SNOOP' mnemonic identifies red-flag headache symptoms requiring urgent neuroimaging (CT/MRI) and further workup:\n• S: Systemic symptoms (fever, weight loss, night sweats, malignancy) or Systemic disease (HIV, cancer, immunocompromised)\n• N: Neurological signs or symptoms (confusion, papilledema, focal deficits, seizures)\n• O: Onset is sudden (thunderclap headache peaking in <1 minute, suggestive of SAH)\n• O: Older age at onset (new headache onset after age 50, suggestive of temporal arteritis or tumor)\n• P: Pattern change or Positional headache (worse lying down / standing up, or triggered by Valsalva, coughing, or exercise)."
    },
    {
        "id": "FZ_Q237",
        "question_number": 237,
        "category": "Headache",
        "stem": "A 29-year-old woman presents with headaches that occur exclusively when standing up or sitting upright, resolving completely within 15 minutes of lying flat (orthostatic headache). She had an uncomplicated epidural catheter placed 3 days ago for labor analgesia. Physical examination is normal when supine. Which of the following conditions is the most likely cause of this postural headache?",
        "options": [
            {"text": "Low-pressure headache secondary to post-dural puncture CSF leak", "is_correct": True},
            {"text": "Idiopathic intracranial hypertension", "is_correct": False},
            {"text": "Acute bacterial meningitis", "is_correct": False},
            {"text": "Cerebral venous sinus thrombosis", "is_correct": False},
            {"text": "Tension-type headache", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Low-pressure headache secondary to post-dural puncture CSF leak.\n\nPost-dural puncture headache (PDPH / low-pressure headache) occurs when an accidental dural puncture during spinal or epidural anesthesia leads to persistent leakage of CSF into the epidural space. Hallmarks:\n• Orthostatic / postural headache: Excruciating bilateral throbbing headache within 15 minutes of standing or sitting upright, promptly relieved by lying supine.\n• Pathophysiology: Loss of CSF volume lowers intracranial pressure. In the upright position, the brain sags caudally within the skull, exerting painful traction on pain-sensitive meninges, anchoring veins, and cranial nerves (CN V, IX, X).\n• Treatment: Conservative (bed rest, hydration, caffeine); if refractory, an epidural blood patch (autologous blood injected into epidural space to clot and seal the dural hole) is curative."
    },
    {
        "id": "FZ_Q238",
        "question_number": 238,
        "category": "Headache",
        "stem": "A 23-year-old woman with a history of migraine with aura presents to her gynecologist requesting oral contraceptive pills. Why are combined estrogen-progestin oral contraceptive pills strictly contraindicated in women who experience migraine WITH aura?",
        "options": [
            {"text": "Markedly increased synergistic risk of ischemic stroke", "is_correct": True},
            {"text": "Estrogen irreversibly blocks central 5-HT1D receptors", "is_correct": False},
            {"text": "Progestins precipitate acute trigeminal neuralgia", "is_correct": False},
            {"text": "Oral contraceptives cause acute subarachnoid hemorrhage", "is_correct": False},
            {"text": "Combined pills trigger malignant hyperthermia", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Markedly increased synergistic risk of ischemic stroke.\n\nMigraine with aura is an independent risk factor for ischemic stroke (relative risk ~2.0 to 2.5). Combined estrogen-containing oral contraceptive pills (COCs) induce hepatic synthesis of clotting factors and increase the risk of venous and arterial thromboembolism. In women with migraine WITH aura, adding estrogen-containing contraceptives creates a multiplicative, synergistic increase in the risk of ischemic stroke (risk increases by 6- to 9-fold, and up to 30-fold if the patient also smokes). Therefore, combined hormonal contraceptives are contraindicated in women with migraine with aura (progestin-only pills, levonorgestrel IUD, or copper IUD are safe alternatives)."
    },
    {
        "id": "FZ_Q239",
        "question_number": 239,
        "category": "Headache",
        "stem": "A 40-year-old woman with chronic migraine (>15 headache days per month for >6 months) has failed trials of propranolol, topiramate, and amitriptyline. The neurologist recommends intramuscular injections of onabotulinumtoxinA (Botox) administered across 31 pericranial head and neck sites according to the PREEMPT protocol. What is the mechanism of action by which botulinum toxin prevents chronic migraine?",
        "options": [
            {"text": "Cleaves SNAP-25 in peripheral sensory nerve endings, inhibiting the release of CGRP, substance P, and glutamate from trigeminovascular afferents", "is_correct": True},
            {"text": "Directly blocks post-junctional nicotinic receptors on smooth muscle", "is_correct": False},
            {"text": "Inhibits the enzyme cyclooxygenase-1 in circulating platelets", "is_correct": False},
            {"text": "Stimulates GABA-A receptor chloride opening in the locus coeruleus", "is_correct": False},
            {"text": "Increases intracranial pressure to stabilize CSF dynamics", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Cleaves SNAP-25 in peripheral sensory nerve endings, inhibiting the release of CGRP, substance P, and glutamate from trigeminovascular afferents.\n\nOnabotulinumtoxinA is FDA-approved specifically for the prevention of CHRONIC migraine (≥15 headache days/month, with at least 8 being migrainous, for ≥3 months). Mechanism in migraine:\n• Botulinum toxin heavy chain binds to SV2 receptors on unmyelinated C-fiber and thinly myelinated A-delta trigeminal and cervical sensory nerve terminals in pericranial muscles.\n• The light chain enters the cytosol and cleaves SNAP-25, preventing vesicle fusion.\n• This blocks the peripheral exocytosis of inflammatory and nociceptive neurotransmitters (CGRP, Substance P, and glutamate), preventing peripheral sensitization and dampening the afferent signals that trigger central sensitization in the brainstem."
    },
    {
        "id": "FZ_Q240",
        "question_number": 240,
        "category": "Headache",
        "stem": "A 50-year-old man presents with chronic daily tension-type headaches that occur 20 days per month. He has been taking excessive doses of ibuprofen with minimal effect. The physician decides to start prophylactic pharmacotherapy. Which of the following medications is the first-line evidence-based prophylactic drug of choice for chronic tension-type headache?",
        "options": [
            {"text": "Amitriptyline", "is_correct": True},
            {"text": "Sumatriptan", "is_correct": False},
            {"text": "Oxygen therapy", "is_correct": False},
            {"text": "Indomethacin", "is_correct": False},
            {"text": "Erenumab", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Amitriptyline.\n\nAmitriptyline (a tricyclic antidepressant) is the established first-line evidence-based preventive medication for chronic tension-type headache (as well as an effective migraine preventive). Mechanisms:\n• Inhibits the reuptake of Serotonin (SERT) and Norepinephrine (NET), augmenting endogenous descending inhibitory pain pathways in the spinal dorsal horn and trigeminal spinal nucleus.\n• Antagonizes 5-HT2 and NMDA receptors, reducing central sensitization.\nAdverse anticholinergic effects: Dry mouth, drowsiness, constipation, urinary retention, weight gain, and QT prolongation."
    }
]
