# zen_part3.py - Topics 9 to 12 (80 Questions total)
import json

part3_questions = [
    # =========================================================================
    # 9. PAIN PATHWAY (20 Questions: Q1 - Q20)
    # =========================================================================
    {
        "q_num": "PAIN-01",
        "category": "Pain Pathway",
        "stem": "A 25-year-old carpenter accidentally hits his thumb with a hammer. Immediately, he feels an intense, sharp, well-localized pain, followed several seconds later by a persistent, dull, throbbing, poorly localized ache. Which of the following pairs of primary sensory nerve fibers is responsible for transmitting the initial sharp pain versus the subsequent dull aching pain, respectively?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "A-alpha fibers; A-beta fibers"},
            {"letter": "B", "is_correct": False, "text": "A-beta fibers; A-delta fibers"},
            {"letter": "C", "is_correct": True, "text": "A-delta fibers; C fibers"},
            {"letter": "D", "is_correct": False, "text": "C fibers; A-delta fibers"},
            {"letter": "E", "is_correct": False, "text": "A-delta fibers; B fibers"}
        ],
        "explanation": "Correct Answer: C. A-delta fibers; C fibers.\n\nDual pain transmission:\n• 'Fast pain' (first pain): Transmitted by lightly myelinated A-delta fibers (conduction velocity 5-30 m/s). It is sharp, pricking, rapid, and well-localized, terminating primarily in Rexed lamina I and V of the spinal cord dorsal horn.\n• 'Slow pain' (second pain): Transmitted by unmyelinated C fibers (conduction velocity 0.5-2 m/s). It is dull, burning, aching, and poorly localized, terminating primarily in Rexed lamina II (substantia gelatinosa)."
    },
    {
        "q_num": "PAIN-02",
        "category": "Pain Pathway",
        "stem": "Second-order nociceptive projection neurons of the spinothalamic tract originate in the dorsal horn of the spinal cord. Where do the axons of these second-order neurons cross the midline to enter the contralateral anterolateral column?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Sensory decussation in the caudal medulla"},
            {"letter": "B", "is_correct": True, "text": "Anterior white commissure, ascending 1–2 spinal segments as they cross"},
            {"letter": "C", "is_correct": False, "text": "Posterior gray commissure at the exact segment of entry"},
            {"letter": "D", "is_correct": False, "text": "Pyramidal decussation in the caudal medulla"},
            {"letter": "E", "is_correct": False, "text": "Dorsal root entry zone"}
        ],
        "explanation": "Correct Answer: B. Anterior white commissure, ascending 1–2 spinal segments as they cross.\n\nPrimary nociceptive afferents enter the spinal cord, ascend or descend 1-2 segments in the tract of Lissauer (dorsolateral fasciculus), and synapse in the dorsal horn (substantia gelatinosa / Rexed laminae I, II, V). The axons of second-order spinothalamic neurons then cross the midline obliquely through the anterior white commissure over 1 to 2 spinal segments before ascending in the contralateral anterolateral funiculus. This explains why an anterior cord lesion or syringomyelia selectively abolishes bilateral pain and temperature sensation."
    },
    {
        "q_num": "PAIN-03",
        "category": "Pain Pathway",
        "stem": "Immediately after bumping his elbow against a wall, a man vigorously rubs the injured area with his hand, which significantly reduces the perceived sharpness of the pain. According to the Gate Control Theory of pain proposed by Melzack and Wall, which of the following mechanisms accounts for this pain relief?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Activation of descending noradrenergic projections from the locus coeruleus"},
            {"letter": "B", "is_correct": True, "text": "Activation of large myelinated A-beta fibers stimulating inhibitory interneurons in the substantia gelatinosa"},
            {"letter": "C", "is_correct": False, "text": "Direct depletion of substance P from peripheral nociceptors"},
            {"letter": "D", "is_correct": False, "text": "Inhibition of NMDA receptors by magnesium in the thalamus"},
            {"letter": "E", "is_correct": False, "text": "Upregulation of opioid receptors on peripheral free nerve endings"}
        ],
        "explanation": "Correct Answer: B. Activation of large myelinated A-beta fibers stimulating inhibitory interneurons in the substantia gelatinosa.\n\nThe Gate Control Theory of pain states that transmission of pain through dorsal horn projection neurons can be modulated locally:\n• Noxious inputs via C-fibers activate projection neurons and inhibit local inhibitory interneurons, 'opening the gate.'\n• Non-noxious mechanical tactile stimulation (rubbing, shaking) activates large-diameter myelinated A-beta fibers.\n• A-beta collaterals excite local GABAergic/enkephalinergic inhibitory interneurons in the substantia gelatinosa (Rexed lamina II).\n• These interneurons presynaptically and postsynaptically inhibit the transmission of pain signals to ascending spinothalamic projection neurons, 'closing the gate.'"
    },
    {
        "q_num": "PAIN-04",
        "category": "Pain Pathway",
        "stem": "The periaqueductal gray (PAG) of the midbrain plays a central role in the endogenous descending pain-modulatory pathway. Electrical stimulation of the PAG produces profound analgesia. The PAG exerts this analgesic effect primarily by sending excitatory projections to which serotonergic brainstem nucleus in the rostral ventromedial medulla?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Locus coeruleus"},
            {"letter": "B", "is_correct": True, "text": "Nucleus raphe magnus"},
            {"letter": "C", "is_correct": False, "text": "Nucleus ambiguus"},
            {"letter": "D", "is_correct": False, "text": "Substantia nigra"},
            {"letter": "E", "is_correct": False, "text": "Edinger-Westphal nucleus"}
        ],
        "explanation": "Correct Answer: B. Nucleus raphe magnus.\n\nDescending pain inhibition pathway:\n1. Neurons in the periaqueductal gray (PAG) of the midbrain project to the rostral ventromedial medulla, specifically the nucleus raphe magnus (serotonergic) and the locus coeruleus (noradrenergic).\n2. Nucleus raphe magnus axons descend in the dorsolateral funiculus of the spinal cord to the dorsal horn.\n3. They release serotonin (and norepinephrine), which excites local enkephalinergic inhibitory interneurons in the substantia gelatinosa.\n4. Enkephalin binds to presynaptic mu-opioid receptors on primary afferent C-fibers (inhibiting Ca2+ influx and substance P release) and postsynaptic receptors on projection neurons (hyperpolarizing them via K+ efflux)."
    },
    {
        "q_num": "PAIN-05",
        "category": "Pain Pathway",
        "stem": "A 55-year-old man presents with severe burning pain across his right flank 3 months after a vesicular rash in the same dermatome resolved (postherpetic neuralgia). Even the light touch of a cotton shirt against his skin causes agonizing, intolerable pain. Which of the following terms correctly defines the perception of pain from an ordinarily non-painful stimulus?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Hyperalgesia"},
            {"letter": "B", "is_correct": True, "text": "Allodynia"},
            {"letter": "C", "is_correct": False, "text": "Hyperpathia"},
            {"letter": "D", "is_correct": False, "text": "Paresthesia"},
            {"letter": "E", "is_correct": False, "text": "Dysesthesia"}
        ],
        "explanation": "Correct Answer: B. Allodynia.\n\nDefinitions of pain terms:\n• Allodynia: Pain resulting from a stimulus that does not normally provoke pain (e.g., light touch of clothing triggering intense pain in postherpetic neuralgia or trigeminal neuralgia).\n• Hyperalgesia: Increased pain sensitivity to a stimulus that is normally painful (e.g., mild pinprick feeling intensely agonizing).\n• Paresthesia: An abnormal sensation, whether spontaneous or evoked, not unpleasant (e.g., tingling, 'pins and needles').\n• Dysesthesia: An unpleasant abnormal sensation (spontaneous or evoked)."
    },
    {
        "q_num": "PAIN-06",
        "category": "Pain Pathway",
        "stem": "Capsaicin, the chemical compound responsible for the heat of chili peppers, is applied topically to manage neuropathic pain. Capsaicin selectively binds to and activates which specialized heat- and acid-sensitive non-selective cation channel on nociceptive nerve endings?",
        "options": [
            {"letter": "A", "is_correct": True, "text": "TRPV1 (Transient Receptor Potential Vanilloid 1)"},
            {"letter": "B", "is_correct": False, "text": "TRPM8 (Transient Receptor Potential Melastatin 8)"},
            {"letter": "C", "is_correct": False, "text": "TRPA1 (Transient Receptor Potential Ankyrin 1)"},
            {"letter": "D", "is_correct": False, "text": "ASIC3 (Acid-Sensing Ion Channel 3)"},
            {"letter": "E", "is_correct": False, "text": "Piezo2 mechanosensitive channel"}
        ],
        "explanation": "Correct Answer: A. TRPV1 (Transient Receptor Potential Vanilloid 1).\n\nTRPV1 is a non-selective cation channel expressed on nociceptive A-delta and C fibers that is gated by noxious heat (>43°C), extracellular protons (acidosis / pH < 5.9), and capsaicin. \n• Therapeutic mechanism of topical capsaicin: Initial application causes burning pain by opening TRPV1; chronic repeated application causes massive sustained Ca2+ influx that overloads mitochondria and depletes substance P, leading to prolonged defunctionalization and desensitization of nociceptive terminals."
    },
    {
        "q_num": "PAIN-07",
        "category": "Pain Pathway",
        "stem": "A 58-year-old man experiencing an acute myocardial infarction presents with crushing retrosternal chest pressure that radiates to his left neck, jaw, and the medial aspect of his left arm. What neuroanatomical mechanism explains why visceral pain from the heart is referred to these specific somatic dermatomes?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Direct electrical ephaptic transmission between autonomic and somatic peripheral nerves"},
            {"letter": "B", "is_correct": True, "text": "Convergence of cardiac visceral afferents and somatic cutaneous afferents on the same second-order dorsal horn neurons at T1–T4"},
            {"letter": "C", "is_correct": False, "text": "Retrograde axonal transport of substance P from cardiac nerves to the brachial plexus"},
            {"letter": "D", "is_correct": False, "text": "Infarction of the medial lemniscus within the caudal brainstem"},
            {"letter": "E", "is_correct": False, "text": "Spillover of noradrenaline in the sympathetic chain ganglia"}
        ],
        "explanation": "Correct Answer: B. Convergence of cardiac visceral afferents and somatic cutaneous afferents on the same second-order dorsal horn neurons at T1–T4.\n\nReferred pain occurs due to convergence-projection in the spinal cord dorsal horn:\n• Visceral nociceptive afferents from the ischemic myocardium travel with sympathetic nerves to enter upper thoracic spinal cord segments (T1-T4/T5).\n• Somatic cutaneous sensory afferents from the chest wall and medial arm (T1-T4 dermatomes) enter the exact same spinal segments.\n• Both visceral and somatic fibers converge onto the same second-order spinothalamic projection neurons.\n• Because the cerebral cortex has vastly more prior experience processing somatic cutaneous inputs, it misinterprets the ascending visceral nociceptive activity as arising from the somatic dermatomes."
    },
    {
        "q_num": "PAIN-08",
        "category": "Pain Pathway",
        "stem": "Which of the following pro-inflammatory neuropeptides is stored alongside glutamate in dense-core vesicles of primary nociceptive C-fibers, is released into the dorsal horn upon high-frequency noxious stimulation, and binds to neurokinin-1 (NK1) receptors to mediate slow, long-lasting pain transmission and central sensitization?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Neuropeptide Y"},
            {"letter": "B", "is_correct": True, "text": "Substance P"},
            {"letter": "C", "is_correct": False, "text": "Somatostatin"},
            {"letter": "D", "is_correct": False, "text": "Neurotensin"},
            {"letter": "E", "is_correct": False, "text": "Galanin"}
        ],
        "explanation": "Correct Answer: B. Substance P.\n\nSubstance P is an 11-amino acid neuropeptide synthesized in dorsal root ganglion cells and transported to primary nociceptive C-fiber terminals. \n• In the spinal cord dorsal horn, substance P is coreleased with glutamate in response to intense, repetitive noxious stimuli, binding to postsynaptic Neurokinin-1 (NK-1) receptors to produce prolonged depolarization and initiate central sensitization ('wind-up').\n• Peripherally, substance P causes neurogenic inflammation: arteriolar vasodilation and mast cell degranulation (histamine release), producing edema and hyperalgesia."
    },
    {
        "q_num": "PAIN-09",
        "category": "Pain Pathway",
        "stem": "Following tissue injury, uninjured skin surrounding the primary wound site becomes hypersensitive to touch and mild thermal stimuli. This secondary hyperalgesia and 'wind-up' phenomenon in the spinal cord dorsal horn is mediated by continuous activation of which postsynaptic receptor leading to calcium influx?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "GABA-B receptor"},
            {"letter": "B", "is_correct": True, "text": "NMDA receptor"},
            {"letter": "C", "is_correct": False, "text": "Alpha-2 adrenergic receptor"},
            {"letter": "D", "is_correct": False, "text": "Mu-opioid receptor"},
            {"letter": "E", "is_correct": False, "text": "Glycine receptor"}
        ],
        "explanation": "Correct Answer: B. NMDA receptor.\n\nCentral sensitization ('wind-up') is an activity-dependent increase in neuronal excitability in the dorsal horn:\n• Repetitive C-fiber firing causes sustained release of glutamate and substance P, leading to prolonged baseline depolarization via AMPA and NK-1 receptors.\n• This sustained depolarization repels the resting Mg2+ block from NMDA receptors.\n• Unblocked NMDA receptors allow massive Ca2+ influx into postsynaptic neurons, activating protein kinase C (PKC) and nitric oxide synthase (NOS).\n• This increases synaptic strength (long-term potentiation of pain pathways), expanding receptive fields and causing secondary hyperalgesia."
    },
    {
        "q_num": "PAIN-10",
        "category": "Pain Pathway",
        "stem": "Which cortical and limbic structures receive ascending nociceptive projections from the intralaminar and medial thalamic nuclei (paleospinothalamic tract), mediating the unpleasant, emotional, and affective suffering of pain rather than its sensory-discriminative localization?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Primary motor cortex and supplementary motor area"},
            {"letter": "B", "is_correct": True, "text": "Anterior cingulate cortex and insular cortex"},
            {"letter": "C", "is_correct": False, "text": "Primary visual cortex and lingual gyrus"},
            {"letter": "D", "is_correct": False, "text": "Dentate gyrus and entorhinal cortex"},
            {"letter": "E", "is_correct": False, "text": "Inferior temporal gyrus and fusiform gyrus"}
        ],
        "explanation": "Correct Answer: B. Anterior cingulate cortex and insular cortex.\n\nThe pain pathway bifurcates in the brain:\n1. Lateral pain system (spinothalamic → VPL thalamus → primary somatosensory cortex S1/S2): Mediates sensory-discriminative aspects (location, intensity, duration, and quality of pain).\n2. Medial pain system (spinoreticular / paleospinothalamic → medial thalamus → anterior cingulate cortex [ACC] and anterior insula): Mediates motivational-affective suffering, autonomic arousal, and emotional unpleasantness of pain. Patients with lesions of the ACC perceive that pain is present but are no longer distressed or bothered by it ('pain asymbolia')."
    },
    {
        "q_num": "PAIN-11",
        "category": "Pain Pathway",
        "stem": "A 50-year-old man with intractable cancer pain undergoes a percutaneous cordotomy to achieve pain relief. The neurosurgeon surgically transects which ascending tract in the spinal cord anterolateral column contralateral to the painful region?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Dorsal columns (fasciculus gracilis)"},
            {"letter": "B", "is_correct": True, "text": "Lateral spinothalamic tract"},
            {"letter": "C", "is_correct": False, "text": "Lateral corticospinal tract"},
            {"letter": "D", "is_correct": False, "text": "Dorsal spinocerebellar tract"},
            {"letter": "E", "is_correct": False, "text": "Rubrospinal tract"}
        ],
        "explanation": "Correct Answer: B. Lateral spinothalamic tract.\n\nA cordotomy is a neurosurgical procedure used for unilateral intractable cancer pain below the neck. The lateral spinothalamic tract in the anterolateral quadrant of the spinal cord is ablated CONTRALATERAL to the site of pain (since spinothalamic axons decussate in the anterior white commissure 1-2 segments above their entry level)."
    },
    {
        "q_num": "PAIN-12",
        "category": "Pain Pathway",
        "stem": "Rexed laminae divide the spinal cord gray matter into ten distinct histological zones from dorsal to ventral. Which Rexed lamina corresponds to the substantia gelatinosa, which receives dense terminations from primary unmyelinated C-fibers and serves as a major site of pain gating?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Lamina I (marginal zone)"},
            {"letter": "B", "is_correct": True, "text": "Lamina II (substantia gelatinosa)"},
            {"letter": "C", "is_correct": False, "text": "Lamina IV (nucleus proprius)"},
            {"letter": "D", "is_correct": False, "text": "Lamina VII (zona intermedia)"},
            {"letter": "E", "is_correct": False, "text": "Lamina IX (motor nuclei)"}
        ],
        "explanation": "Correct Answer: B. Lamina II (substantia gelatinosa).\n\n• Lamina I: Marginal zone (receives A-delta and C fibers; origin of some spinothalamic projection neurons).\n• Lamina II: Substantia gelatinosa of Rolando (high density of interneurons regulating pain transmission; primary site of opiate receptors and gate-control inhibition).\n• Laminae III and IV: Nucleus proprius (mechanoreceptive input).\n• Lamina V: Deep dorsal horn containing wide dynamic range (WDR) neurons that receive convergent tactile and nociceptive inputs.\n• Lamina IX: Ventral horn alpha and gamma motor neurons."
    },
    {
        "q_num": "PAIN-13",
        "category": "Pain Pathway",
        "stem": "Which cold-activated TRP ion channel is expressed on sensory nerve endings, is activated by moderate cool temperatures (10–28°C) as well as by menthol and icilin, and imparts the familiar cooling sensation of peppermint?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "TRPV1"},
            {"letter": "B", "is_correct": True, "text": "TRPM8"},
            {"letter": "C", "is_correct": False, "text": "TRPA1"},
            {"letter": "D", "is_correct": False, "text": "TRPV4"},
            {"letter": "E", "is_correct": False, "text": "TRPC1"}
        ],
        "explanation": "Correct Answer: B. TRPM8.\n\nTRPM8 (Transient Receptor Potential Melastatin 8) is a non-selective cation channel on sensory afferents activated by cool temperatures (10-28°C) and cooling chemical agonists like menthol, eucalyptol, and icilin. Activation produces the perception of coldness and can produce analgesia via gate-control mechanisms."
    },
    {
        "q_num": "PAIN-14",
        "category": "Pain Pathway",
        "stem": "During tissue injury and inflammation, a chemical 'inflammatory soup' is released that sensitizes peripheral nociceptors (peripheral sensitization). Which of the following inflammatory mediators binds to Gs-coupled receptors to increase intracellular cyclic AMP (cAMP) and activate protein kinase A (PKA), lowering the activation threshold of voltage-gated Nav1.8 sodium channels?",
        "options": [
            {"letter": "A", "is_correct": True, "text": "Prostaglandin E2 (PGE2)"},
            {"letter": "B", "is_correct": False, "text": "Endothelin-1"},
            {"letter": "C", "is_correct": False, "text": "Interleukin-10"},
            {"letter": "D", "is_correct": False, "text": "GABA"},
            {"letter": "E", "is_correct": False, "text": "Transforming growth factor-beta"}
        ],
        "explanation": "Correct Answer: A. Prostaglandin E2 (PGE2).\n\nProstaglandin E2 (PGE2), synthesized by cyclooxygenase-2 (COX-2) at sites of inflammation, binds to EP2 and EP4 Gs-coupled receptors on nociceptive nerve terminals. This activates adenylyl cyclase, elevating intracellular cAMP and activating Protein Kinase A (PKA). PKA phosphorylates tetrodotoxin-resistant voltage-gated sodium channels (Nav1.8 and Nav1.9) and TRPV1, lowering their activation thresholds and causing peripheral sensitization (primary hyperalgesia). NSAIDs relieve inflammatory pain by inhibiting COX-2, preventing PGE2 synthesis."
    },
    {
        "q_num": "PAIN-15",
        "category": "Pain Pathway",
        "stem": "A 40-year-old woman with severe fibromyalgia complains of widespread musculoskeletal aching and fatigue. Functional neuroimaging demonstrates normal peripheral nerve function but exaggerated activity in the insula and anterior cingulate cortex during low-intensity pressure stimuli. This central amplification of pain perception without ongoing peripheral tissue damage is classified as:",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Nociceptive pain"},
            {"letter": "B", "is_correct": False, "text": "Neuropathic pain"},
            {"letter": "C", "is_correct": True, "text": "Nociplastic pain"},
            {"letter": "D", "is_correct": False, "text": "Visceral pain"},
            {"letter": "E", "is_correct": False, "text": "Psychogenic conversion pain"}
        ],
        "explanation": "Correct Answer: C. Nociplastic pain.\n\nMechanistic classifications of pain (IASP):\n1. Nociceptive pain: Arises from actual or threatened damage to non-neural tissue and activation of nociceptors (e.g., osteoarthritis, burn, bone fracture).\n2. Neuropathic pain: Caused by a demonstrable lesion or disease of the somatosensory nervous system (e.g., diabetic polyneuropathy, postherpetic neuralgia, spinal cord injury).\n3. Nociplastic pain: Pain arising from altered nociception despite no clear evidence of actual or threatened tissue damage or somatosensory lesion (e.g., fibromyalgia, irritable bowel syndrome, tension headache, chronic widespread pain). It is characterized by central sensitization and augmented CNS sensory processing."
    },
    {
        "q_num": "PAIN-16",
        "category": "Pain Pathway",
        "stem": "A 60-year-old man with painful diabetic peripheral neuropathy is started on duloxetine. Duloxetine relieves neuropathic pain primarily by which mechanism of action in the central nervous system?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Direct agonism at mu-opioid receptors in the dorsal horn"},
            {"letter": "B", "is_correct": True, "text": "Inhibiting reuptake of serotonin and norepinephrine, enhancing descending pain-inhibitory pathways"},
            {"letter": "C", "is_correct": False, "text": "Irreversible inhibition of cyclooxygenase-1 and -2"},
            {"letter": "D", "is_correct": False, "text": "Direct blockade of NMDA glutamate receptors"},
            {"letter": "E", "is_correct": False, "text": "Antagonism of voltage-gated sodium channels in peripheral axons"}
        ],
        "explanation": "Correct Answer: B. Inhibiting reuptake of serotonin and norepinephrine, enhancing descending pain-inhibitory pathways.\n\nDuloxetine is a Serotonin-Norepinephrine Reuptake Inhibitor (SNRI) approved for diabetic neuropathic pain and fibromyalgia. It blocks the presynaptic transporters for both norepinephrine (NET) and serotonin (SERT). By increasing synaptic concentrations of norepinephrine and serotonin in the spinal cord dorsal horn, it potentiates the endogenous descending inhibitory pain pathways (from locus coeruleus and nucleus raphe magnus), suppressing spinal nociceptive transmission."
    },
    {
        "q_num": "PAIN-17",
        "category": "Pain Pathway",
        "stem": "Pregabalin and gabapentin are first-line medications for neuropathic pain. Despite their chemical similarity to GABA, they do not bind to GABA receptors. What is their true pharmacological target?",
        "options": [
            {"letter": "A", "is_correct": True, "text": "Alpha-2-delta (α2δ) auxiliary subunit of voltage-gated calcium channels"},
            {"letter": "B", "is_correct": False, "text": "GABA transaminase"},
            {"letter": "C", "is_correct": False, "text": "GABA transporter 1 (GAT-1)"},
            {"letter": "D", "is_correct": False, "text": "Sodium-potassium-chloride cotransporter (NKCC1)"},
            {"letter": "E", "is_correct": False, "text": "KCNQ potassium channels"}
        ],
        "explanation": "Correct Answer: A. Alpha-2-delta (α2δ) auxiliary subunit of voltage-gated calcium channels.\n\nGabapentinoids (gabapentin and pregabalin) bind with high affinity to the alpha-2-delta-1 (α2δ-1) auxiliary subunit of presynaptic voltage-gated calcium channels in the dorsal horn and brain. This binding disrupts channel trafficking to the presynaptic terminal, decreasing calcium influx upon action potential arrival and thereby reducing the exocytotic release of excitatory neurotransmitters (glutamate, substance P, and CGRP) from sensitized primary afferents."
    },
    {
        "q_num": "PAIN-18",
        "category": "Pain Pathway",
        "stem": "Bradykinin is one of the most potent endogenous algogenic (pain-producing) substances generated during tissue damage. Bradykinin is cleaved from high-molecular-weight kininogen by which plasma enzyme?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Thrombin"},
            {"letter": "B", "is_correct": True, "text": "Kallikrein"},
            {"letter": "C", "is_correct": False, "text": "Angiotensin-converting enzyme"},
            {"letter": "D", "is_correct": False, "text": "Plasminogen activator"},
            {"letter": "E", "is_correct": False, "text": "Tryptase"}
        ],
        "explanation": "Correct Answer: B. Kallikrein.\n\nDuring tissue injury and coagulation cascade activation, factor XIIa converts prekallikrein to active kallikrein. Kallikrein then cleaves high-molecular-weight kininogen (HMWK) to release bradykinin (a 9-amino acid peptide). Bradykinin binds to Gq-coupled B2 receptors on nociceptive terminals, activating PLC and PKC to directly depolarize nociceptors and sensitize TRPV1 channels, producing intense burning pain, vasodilation, and vascular permeability."
    },
    {
        "q_num": "PAIN-19",
        "category": "Pain Pathway",
        "stem": "Which bundle of small-diameter unmyelinated and thinly myelinated axons is located at the apex of the spinal cord dorsal horn, allowing primary pain and temperature afferents to ascend or descend 1–2 vertebral segments before synapsing in the gray matter?",
        "options": [
            {"letter": "A", "is_correct": True, "text": "Tract of Lissauer (dorsolateral fasciculus)"},
            {"letter": "B", "is_correct": False, "text": "Fasciculus interfascicularis"},
            {"letter": "C", "is_correct": False, "text": "Fasciculus septomarginalis"},
            {"letter": "D", "is_correct": False, "text": "Medial longitudinal fasciculus"},
            {"letter": "E", "is_correct": False, "text": "Anterior corticospinal tract"}
        ],
        "explanation": "Correct Answer: A. Tract of Lissauer (dorsolateral fasciculus).\n\nThe tract of Lissauer (posterolateral tract) lies capping the dorsal horn between the substantia gelatinosa and the surface of the spinal cord. It contains bifurcating primary afferent fibers (A-delta and C fibers) that travel rostrally or caudally 1 to 2 segments before penetrating the dorsal horn gray matter (Rexed laminae I, II, and V). This intersegmental spread contributes to the overlap of sensory dermatomes."
    },
    {
        "q_num": "PAIN-20",
        "category": "Pain Pathway",
        "stem": "Wide dynamic range (WDR) neurons located in lamina V of the dorsal horn respond to both non-noxious low-threshold tactile stimuli and high-threshold noxious stimuli. What unique firing characteristic enables WDR neurons to signal stimulus intensity across the entire spectrum from light brush to intense pain?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "All-or-none burst firing only at supramaximal stimuli"},
            {"letter": "B", "is_correct": True, "text": "Monotonic increase in action potential discharge frequency proportional to stimulus intensity"},
            {"letter": "C", "is_correct": False, "text": "Rapid complete adaptation within 50 milliseconds of stimulus onset"},
            {"letter": "D", "is_correct": False, "text": "Spontaneous rhythmic oscillation independent of input"},
            {"letter": "E", "is_correct": False, "text": "Selective response only to cold temperatures below 0°C"}
        ],
        "explanation": "Correct Answer: B. Monotonic increase in action potential discharge frequency proportional to stimulus intensity.\n\nWide Dynamic Range (WDR) neurons in lamina V receive convergent polysynaptic inputs from A-beta (light touch), A-delta, and C fibers (noxious). Unlike nociceptive-specific (NS) neurons in lamina I which fire only when tissue damage occurs, WDR neurons increase their action potential firing frequency graded proportionally to increasing mechanical pressure, encoding both tactile intensity and the transition into noxious pain. They are also central to the wind-up phenomenon and convergence in referred pain."
    },

    # =========================================================================
    # 10. TRIGEMINAL PATHWAY (20 Questions: Q21 - Q40)
    # =========================================================================
    {
        "q_num": "TRIG-01",
        "category": "Trigeminal Pathway",
        "stem": "A 62-year-old woman presents with paroxysms of severe, sharp, electric shock-like pain shooting across her right cheek and lower jaw (V2 and V3 distribution). The pain lasts 10 to 15 seconds at a time and is triggered by light touch, brushing her teeth, or a cold gust of wind. Neurological examination is completely normal with no sensory loss. What is the first-line pharmacological treatment for this disorder?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Indomethacin"},
            {"letter": "B", "is_correct": False, "text": "Sumatriptan"},
            {"letter": "C", "is_correct": True, "text": "Carbamazepine"},
            {"letter": "D", "is_correct": False, "text": "Prednisone"},
            {"letter": "E", "is_correct": False, "text": "Oxygen 100% via non-rebreather mask"}
        ],
        "explanation": "Correct Answer: C. Carbamazepine.\n\nThis patient has Trigeminal Neuralgia (tic douloureux):\n• Classic presentation: Brief, paroxysmal, lancinating, electric-shock pain in the distribution of CN V2/V3, triggered by innocuous tactile stimuli (touch, chewing, shaving, wind).\n• Pathophysiology: Neurovascular compression of the trigeminal nerve root entry zone by an aberrant arterial loop (most commonly the superior cerebellar artery), causing focal demyelination and ephaptic cross-talk between tactile and nociceptive axons.\n• First-line medical therapy: Carbamazepine (or oxcarbazepine), which blocks use-dependent voltage-gated sodium channels, suppressing high-frequency neuronal firing. (Monitor for aplastic anemia, agranulocytosis, SIADH, and Stevens-Johnson syndrome)."
    },
    {
        "q_num": "TRIG-02",
        "category": "Trigeminal Pathway",
        "stem": "During a neurological examination, the physician tests the corneal reflex by touching a wisp of sterile cotton to the right cornea. Both the right and left eyes blink symmetrically. Which cranial nerves serve as the afferent and efferent limbs of this reflex, respectively?",
        "options": [
            {"letter": "A", "is_correct": True, "text": "Afferent: CN V1 (Ophthalmic); Efferent: CN VII (Facial)"},
            {"letter": "B", "is_correct": False, "text": "Afferent: CN II (Optic); Efferent: CN III (Oculomotor)"},
            {"letter": "C", "is_correct": False, "text": "Afferent: CN V2 (Maxillary); Efferent: CN VII (Facial)"},
            {"letter": "D", "is_correct": False, "text": "Afferent: CN VII (Facial); Efferent: CN V1 (Ophthalmic)"},
            {"letter": "E", "is_correct": False, "text": "Afferent: CN V1 (Ophthalmic); Efferent: CN III (Oculomotor)"}
        ],
        "explanation": "Correct Answer: A. Afferent: CN V1 (Ophthalmic); Efferent: CN VII (Facial).\n\nThe corneal reflex pathway:\n• Afferent limb: Nasociliary branch of the ophthalmic division of the trigeminal nerve (CN V1) senses mechanical stimulation on the cornea.\n• Central relay: Enters the pons, descends to the spinal trigeminal nucleus, and sends bilateral interneuronal projections via the reticular formation to the facial motor nuclei (CN VII) in both the ipsilateral and contralateral pons.\n• Efferent limb: CN VII motor fibers innervate the orbicularis oculi muscles bilaterally, producing both a direct blink (stimulated eye) and a consensual blink (opposite eye)."
    },
    {
        "q_num": "TRIG-03",
        "category": "Trigeminal Pathway",
        "stem": "Which of the following sensory nuclei of the trigeminal nerve contains primary pseudounipolar sensory cell bodies located entirely inside the central nervous system (rather than in a peripheral ganglion) and mediates proprioception from the muscles of mastication, periodontal ligaments, and teeth?",
        "options": [
            {"letter": "A", "is_correct": True, "text": "Mesencephalic nucleus of the trigeminal nerve"},
            {"letter": "B", "is_correct": False, "text": "Chief (principal) sensory nucleus of the trigeminal nerve"},
            {"letter": "C", "is_correct": False, "text": "Spinal trigeminal nucleus pars caudalis"},
            {"letter": "D", "is_correct": False, "text": "Motor nucleus of the trigeminal nerve"},
            {"letter": "E", "is_correct": False, "text": "Nucleus of the solitary tract"}
        ],
        "explanation": "Correct Answer: A. Mesencephalic nucleus of the trigeminal nerve.\n\nThe mesencephalic trigeminal nucleus (located in the lateral periaqueductal gray of the midbrain and rostral pons) is unique in neuroanatomy: it is the ONLY structure in the CNS that contains primary sensory pseudounipolar cell bodies (derived embryologically from neural crest cells that failed to migrate outside the neural tube). It receives proprioceptive inputs from muscle spindles in the muscles of mastication (jaw jerk reflex) and mechanoreceptors in periodontal ligaments."
    },
    {
        "q_num": "TRIG-04",
        "category": "Trigeminal Pathway",
        "stem": "A 55-year-old man undergoes testing of cranial nerve reflexes. The examiner places a finger on the patient's chin and taps the finger downward with a reflex hammer. The patient demonstrates a brisk, hyperactive upward closure of the jaw (hyperactive jaw jerk reflex). Which type of motor neuron lesion does a hyperactive jaw jerk reflex indicate, and where is the lesion located?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Lower motor neuron lesion of CN V in the peripheral mandibular nerve"},
            {"letter": "B", "is_correct": False, "text": "Lower motor neuron lesion of the trigeminal motor nucleus in the mid-pons"},
            {"letter": "C", "is_correct": True, "text": "Bilateral upper motor neuron (corticobulbar) lesion located rostral to the mid-pons"},
            {"letter": "D", "is_correct": False, "text": "Unilateral lower motor neuron lesion of CN VII"},
            {"letter": "E", "is_correct": False, "text": "Isolated spinal cord lesion at C5-C6"}
        ],
        "explanation": "Correct Answer: C. Bilateral upper motor neuron (corticobulbar) lesion located rostral to the mid-pons.\n\nThe jaw jerk reflex is a monosynaptic stretch reflex mediated entirely by the mandibular nerve (CN V3):\n• Afferent limb: Muscle spindle stretch travels via CN V3 to cell bodies in the mesencephalic trigeminal nucleus.\n• Efferent limb: Direct monosynaptic synapse onto the trigeminal motor nucleus in the mid-pons → CN V3 → masseter contraction.\n• Clinical significance: Under normal conditions, this reflex is minimal or absent. A brisk, hyperactive jaw jerk reflex is a pathognomonic sign of bilateral Upper Motor Neuron (pseudobulbar) pathology located above the mid-pons (such as in ALS or bilateral stroke), indicating that the lesion is intracranial and supranuclear."
    },
    {
        "q_num": "TRIG-05",
        "category": "Trigeminal Pathway",
        "stem": "Pain and temperature sensation from the entire face enters the brainstem via the trigeminal nerve and descends in the spinal trigeminal tract to synapse in which specific subdivision of the spinal trigeminal nucleus, which extends caudally into the upper cervical spinal cord (C2-C3) and merges with the substantia gelatinosa?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Pars oralis"},
            {"letter": "B", "is_correct": False, "text": "Pars interpolaris"},
            {"letter": "C", "is_correct": True, "text": "Pars caudalis"},
            {"letter": "D", "is_correct": False, "text": "Principal sensory nucleus"},
            {"letter": "E", "is_correct": False, "text": "Mesencephalic nucleus"}
        ],
        "explanation": "Correct Answer: C. Pars caudalis.\n\nThe spinal trigeminal nucleus is divided rostrocaudally into three subnuclei:\n1. Pars oralis (rostral pons): Tactile and dental sensation.\n2. Pars interpolaris (mid-medulla): Dental pain and tactile.\n3. Pars caudalis (caudal medulla extending down to C2/C3 in the dorsal horn): The primary relay for pain and temperature from the head and face. Histologically continuous with the substantia gelatinosa of the spinal cord (Rexed lamina II), it sends crossed secondary axons (ventral trigeminothalamic tract) to the VPM nucleus of the thalamus."
    },
    {
        "q_num": "TRIG-06",
        "category": "Trigeminal Pathway",
        "stem": "The three divisions of the trigeminal nerve exit the middle cranial fossa through three distinct skull base foramina. Which of the following lists correctly pairs the nerve division with its exit foramen?",
        "options": [
            {"letter": "A", "is_correct": True, "text": "V1: Superior orbital fissure; V2: Foramen rotundum; V3: Foramen ovale"},
            {"letter": "B", "is_correct": False, "text": "V1: Optic canal; V2: Foramen ovale; V3: Foramen spinosum"},
            {"letter": "C", "is_correct": False, "text": "V1: Foramen rotundum; V2: Superior orbital fissure; V3: Foramen lacerum"},
            {"letter": "D", "is_correct": False, "text": "V1: Superior orbital fissure; V2: Foramen ovale; V3: Foramen rotundum"},
            {"letter": "E", "is_correct": False, "text": "V1: Foramen ovale; V2: Foramen spinosum; V3: Jugular foramen"}
        ],
        "explanation": "Correct Answer: A. V1: Superior orbital fissure; V2: Foramen rotundum; V3: Foramen ovale.\n\nTrigeminal skull foramina mnemonic ('Standing Room Only'):\n• V1 (Ophthalmic): Superior orbital fissure (S)\n• V2 (Maxillary): Foramen Rotundum (R)\n• V3 (Mandibular): Foramen Ovale (O)"
    },
    {
        "q_num": "TRIG-07",
        "category": "Trigeminal Pathway",
        "stem": "A 70-year-old man presents with severe, burning pain and a vesicular erythematous rash over his right forehead, upper eyelid, and the tip and side of his nose (Hutchinson sign). Fluorescein staining reveals dendritic corneal ulcers. The presence of lesions on the tip of the nose indicates involvement of which specific nerve branch, placing the eye at high risk for vision loss?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Frontal nerve (supraorbital branch)"},
            {"letter": "B", "is_correct": False, "text": "Lacrimal nerve"},
            {"letter": "C", "is_correct": True, "text": "Nasociliary nerve (external nasal branch)"},
            {"letter": "D", "is_correct": False, "text": "Infraorbital nerve"},
            {"letter": "E", "is_correct": False, "text": "Zygomaticotemporal nerve"}
        ],
        "explanation": "Correct Answer: C. Nasociliary nerve (external nasal branch).\n\nThis patient has Herpes Zoster Ophthalmicus (reactivation of varicella-zoster virus in the trigeminal ganglion, V1 distribution). Hutchinson sign (vesicles on the tip, side, or root of the nose) indicates involvement of the external nasal branch of the nasociliary nerve. Because the nasociliary nerve also supplies sensory innervation to the cornea, ciliary body, and iris via long and short ciliary nerves, Hutchinson sign is a powerful clinical predictor of herpes zoster keratitis, uveitis, and potential blindness."
    },
    {
        "q_num": "TRIG-08",
        "category": "Trigeminal Pathway",
        "stem": "The motor root of the trigeminal nerve travels exclusively with the mandibular division (CN V3). Which of the following muscles is innervated by the motor division of the trigeminal nerve?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Orbicularis oris"},
            {"letter": "B", "is_correct": False, "text": "Buccinator"},
            {"letter": "C", "is_correct": True, "text": "Tensor tympani and mylohyoid"},
            {"letter": "D", "is_correct": False, "text": "Posterior belly of the digastric"},
            {"letter": "E", "is_correct": False, "text": "Stapedius"}
        ],
        "explanation": "Correct Answer: C. Tensor tympani and mylohyoid.\n\nMuscles innervated by the motor root of CN V3 (derived from the 1st pharyngeal arch):\n• 4 Muscles of mastication: Masseter, temporalis, medial pterygoid, lateral pterygoid.\n• Mylohyoid and anterior belly of the digastric.\n• Tensor tympani (dampens sound of chewing on the malleus).\n• Tensor veli palatini (tenses the soft palate).\n(In contrast, facial expression muscles, stapedius, and posterior belly of the digastric are innervated by CN VII [2nd pharyngeal arch])."
    },
    {
        "q_num": "TRIG-09",
        "category": "Trigeminal Pathway",
        "stem": "A 45-year-old woman presents with persistent facial pain following dental surgery. Neuroimaging confirms compression of the trigeminal nerve. Sensory cell bodies for discriminative touch, pain, and temperature from the face (analogous to the dorsal root ganglion of spinal nerves) are located in which peripheral ganglion?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Ciliary ganglion"},
            {"letter": "B", "is_correct": False, "text": "Otic ganglion"},
            {"letter": "C", "is_correct": True, "text": "Trigeminal (Gasserian / semilunar) ganglion"},
            {"letter": "D", "is_correct": False, "text": "Pterygopalatine ganglion"},
            {"letter": "E", "is_correct": False, "text": "Submandibular ganglion"}
        ],
        "explanation": "Correct Answer: C. Trigeminal (Gasserian / semilunar) ganglion.\n\nThe trigeminal (semilunar or Gasserian) ganglion is located in Meckel cave, a dural recess on the petrous apex of the temporal bone in the middle cranial fossa. It contains pseudounipolar sensory cell bodies for almost all somatosensory modalities from the three divisions of the trigeminal nerve (V1, V2, V3). (The only exception is proprioception, whose cell bodies reside in the central mesencephalic nucleus)."
    },
    {
        "q_num": "TRIG-10",
        "category": "Trigeminal Pathway",
        "stem": "Discriminative fine touch and two-point discrimination from the facial skin and oral mucosa are relayed to which brainstem trigeminal nucleus, which is the cranial nerve analogue of the dorsal column nuclei (nucleus gracilis and cuneatus)?",
        "options": [
            {"letter": "A", "is_correct": True, "text": "Chief (principal) sensory nucleus of the trigeminal nerve"},
            {"letter": "B", "is_correct": False, "text": "Spinal trigeminal nucleus pars caudalis"},
            {"letter": "C", "is_correct": False, "text": "Mesencephalic trigeminal nucleus"},
            {"letter": "D", "is_correct": False, "text": "Edinger-Westphal nucleus"},
            {"letter": "E", "is_correct": False, "text": "Superior salivatory nucleus"}
        ],
        "explanation": "Correct Answer: A. Chief (principal) sensory nucleus of the trigeminal nerve.\n\nThe chief (principal) sensory nucleus of CN V is located in the mid-pons lateral to the trigeminal motor nucleus. It receives primary A-beta fibers conveying fine touch, pressure, and dental tactile sensation. Most second-order axons cross the midline and ascend in the ventral trigeminothalamic tract (trigeminal lemniscus) to the contralateral VPM nucleus of the thalamus (with a small uncrossed dorsal trigeminothalamic tract from oral structures)."
    },
    {
        "q_num": "TRIG-11",
        "category": "Trigeminal Pathway",
        "stem": "A 52-year-old man who experiences intractable trigeminal neuralgia refractory to carbamazepine and gabapentin undergoes microvascular decompression (Janetta procedure). During suboccipital craniectomy, which artery is most frequently identified as the compressive vessel impinging on the trigeminal nerve root?",
        "options": [
            {"letter": "A", "is_correct": True, "text": "Superior cerebellar artery (SCA)"},
            {"letter": "B", "is_correct": False, "text": "Posterior inferior cerebellar artery (PICA)"},
            {"letter": "C", "is_correct": False, "text": "Anterior spinal artery"},
            {"letter": "D", "is_correct": False, "text": "Middle cerebral artery"},
            {"letter": "E", "is_correct": False, "text": "Ophthalmic artery"}
        ],
        "explanation": "Correct Answer: A. Superior cerebellar artery (SCA).\n\nIn >75% of cases of classical trigeminal neuralgia, microvascular compression at the root entry zone (where the nerve transitions from central oligodendrocyte myelin to peripheral Schwann cell myelin) is caused by an aberrant, tortuous loop of the Superior Cerebellar Artery (SCA). Other culprits include the anterior inferior cerebellar artery (AICA) or a petrosal vein."
    },
    {
        "q_num": "TRIG-12",
        "category": "Trigeminal Pathway",
        "stem": "Which of the following parasympathetic ganglia receives preganglionic fibers from the glossopharyngeal nerve (CN IX) via the lesser petrosal nerve and distributes postganglionic secretomotor fibers to the parotid salivary gland via the auriculotemporal branch of CN V3?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Ciliary ganglion"},
            {"letter": "B", "is_correct": True, "text": "Otic ganglion"},
            {"letter": "C", "is_correct": False, "text": "Pterygopalatine ganglion"},
            {"letter": "D", "is_correct": False, "text": "Submandibular ganglion"},
            {"letter": "E", "is_correct": False, "text": "Geniculate ganglion"}
        ],
        "explanation": "Correct Answer: B. Otic ganglion.\n\nParasympathetic ganglia associated with branches of CN V ('COPS'):\n• Ciliary (V1): CN III preganglionic → ciliary ganglion → short ciliary nerves to pupillary sphincter and ciliary muscle.\n• Otic (V3): CN IX preganglionic (lesser petrosal) → otic ganglion → auriculotemporal nerve (V3) to parotid gland.\n• Pterygopalatine (V2): CN VII preganglionic (greater petrosal) → pterygopalatine ganglion → lacrimal gland, nasal/palatal glands.\n• Submandibular (V3): CN VII preganglionic (chorda tympani) → lingual nerve (V3) → submandibular ganglion → submandibular and sublingual glands."
    },
    {
        "q_num": "TRIG-13",
        "category": "Trigeminal Pathway",
        "stem": "During a routine dental procedure, an inferior alveolar nerve block is administered to anesthetize the mandibular teeth. This injection targets a nerve that is a branch of which division of the trigeminal nerve?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Ophthalmic division (V1)"},
            {"letter": "B", "is_correct": False, "text": "Maxillary division (V2)"},
            {"letter": "C", "is_correct": True, "text": "Mandibular division (V3)"},
            {"letter": "D", "is_correct": False, "text": "Facial nerve (CN VII)"},
            {"letter": "E", "is_correct": False, "text": "Glossopharyngeal nerve (CN IX)"}
        ],
        "explanation": "Correct Answer: C. Mandibular division (V3).\n\nThe inferior alveolar nerve is a terminal branch of the posterior division of the mandibular nerve (CN V3). It enters the mandibular foramen on the medial surface of the ramus, traverses the mandibular canal to provide sensory innervation to all lower teeth, and exits the mental foramen as the mental nerve (supplying sensation to the chin and lower lip)."
    },
    {
        "q_num": "TRIG-14",
        "category": "Trigeminal Pathway",
        "stem": "A 45-year-old woman presents with numbness of her right upper lip, right cheek, and upper teeth following a blow to the face that fractured the inferior orbital rim (orbital blowout fracture). Which specific nerve is compressed or injured as it courses through the floor of the orbit?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Supraorbital nerve"},
            {"letter": "B", "is_correct": True, "text": "Infraorbital nerve"},
            {"letter": "C", "is_correct": False, "text": "Mental nerve"},
            {"letter": "D", "is_correct": False, "text": "Buccal branch of CN VII"},
            {"letter": "E", "is_correct": False, "text": "Auriculotemporal nerve"}
        ],
        "explanation": "Correct Answer: B. Infraorbital nerve.\n\nIn orbital blowout fractures (fracture of the thin orbital floor into the maxillary sinus), the infraorbital nerve (a direct continuation of the maxillary nerve CN V2) is frequently entrapped or contused as it traverses the infraorbital groove and canal in the orbital floor. This produces numbness, paresthesias, or hypesthesia of the ipsilateral lower eyelid, cheek, lateral nose, and upper lip/teeth."
    },
    {
        "q_num": "TRIG-15",
        "category": "Trigeminal Pathway",
        "stem": "Ascending second-order fibers from the spinal trigeminal nucleus pars caudalis decussate across the brainstem midline and ascend to the VPM nucleus of the thalamus within which pathway?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Medial lemniscus"},
            {"letter": "B", "is_correct": True, "text": "Ventral trigeminothalamic tract (trigeminal lemniscus)"},
            {"letter": "C", "is_correct": False, "text": "Lateral lemniscus"},
            {"letter": "D", "is_correct": False, "text": "Central tegmental tract"},
            {"letter": "E", "is_correct": False, "text": "Dorsal trigeminothalamic tract"}
        ],
        "explanation": "Correct Answer: B. Ventral trigeminothalamic tract (trigeminal lemniscus).\n\nSecond-order nociceptive and thermal axons from the spinal trigeminal nucleus pars caudalis cross the brainstem midline and ascend as the Ventral Trigeminothalamic Tract (VTHT), running adjacent to the medial lemniscus and spinothalamic tract. They terminate in the contralateral Ventral Posteromedial (VPM) nucleus of the thalamus. (In contrast, the dorsal trigeminothalamic tract carries uncrossed fine touch from the principal sensory nucleus)."
    },
    {
        "q_num": "TRIG-16",
        "category": "Trigeminal Pathway",
        "stem": "Which of the following intracranial structures receives somatic sensory innervation from the tentorial nerve (recurrent meningeal branch of Arnold), derived from the ophthalmic division of the trigeminal nerve (CN V1)?",
        "options": [
            {"letter": "A", "is_correct": True, "text": "Tentorium cerebelli and superior surface of the falx cerebri"},
            {"letter": "B", "is_correct": False, "text": "Floor of the posterior cranial fossa around the foramen magnum"},
            {"letter": "C", "is_correct": False, "text": "Cervical spinal thecal sac"},
            {"letter": "D", "is_correct": False, "text": "Middle ear ossicles and tympanic cavity"},
            {"letter": "E", "is_correct": False, "text": "Choroid plexus of the lateral ventricles"}
        ],
        "explanation": "Correct Answer: A. Tentorium cerebelli and superior surface of the falx cerebri.\n\nSupratentorial dura mater (anterior and middle cranial fossae, anterior falx cerebri, and tentorium cerebelli) is innervated by the trigeminal nerve (principally CN V1 via the tentorial nerve of Arnold). Irritation or stretch of the tentorium (e.g., from posterior fossa tumors or subarachnoid blood) refers pain to the V1 distribution (forehead, retro-orbital area, and eyes). (In contrast, infratentorial dura in the posterior fossa is innervated by CN IX, CN X, and upper cervical nerves C1-C3, referring pain to the occiput and neck)."
    },
    {
        "q_num": "TRIG-17",
        "category": "Trigeminal Pathway",
        "stem": "On examination, when a patient is asked to open his mouth wide against resistance, the mandible deviates markedly to the right side. Strength of the left pterygoid muscles is normal. This finding localizes to a lower motor neuron lesion of which nerve?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Left trigeminal nerve motor root"},
            {"letter": "B", "is_correct": True, "text": "Right trigeminal nerve motor root (CN V3)"},
            {"letter": "C", "is_correct": False, "text": "Right facial nerve (CN VII)"},
            {"letter": "D", "is_correct": False, "text": "Right hypoglossal nerve (CN XII)"},
            {"letter": "E", "is_correct": False, "text": "Left glossopharyngeal nerve (CN IX)"}
        ],
        "explanation": "Correct Answer: B. Right trigeminal nerve motor root (CN V3).\n\nThe lateral pterygoid muscle protrudes and depresses the mandible, pushing the chin toward the CONTRALATERAL side. When the right lateral pterygoid is paralyzed due to a right CN V3 LMN lesion, the unopposed action of the intact left lateral pterygoid muscle pushes the mandible toward the paralyzed (right) side upon opening ('the jaw deviates toward the side of the lesion')."
    },
    {
        "q_num": "TRIG-18",
        "category": "Trigeminal Pathway",
        "stem": "A 28-year-old woman with multiple sclerosis presents with bilateral trigeminal neuralgia. Trigeminal neuralgia occurring bilaterally in a young patient is a classic presentation of which pathological process?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Bilateral superior cerebellar artery ectasia"},
            {"letter": "B", "is_correct": True, "text": "Demyelinating plaques within the intrapontine trigeminal primary afferent fibers"},
            {"letter": "C", "is_correct": False, "text": "Bilateral cavernous sinus thrombosis"},
            {"letter": "D", "is_correct": False, "text": "Bilateral vestibular schwannomas"},
            {"letter": "E", "is_correct": False, "text": "Idiopathic intracranial hypertension"}
        ],
        "explanation": "Correct Answer: B. Demyelinating plaques within the intrapontine trigeminal primary afferent fibers.\n\nWhile classical trigeminal neuralgia in older adults is typically unilateral and caused by neurovascular compression, trigeminal neuralgia in young patients (<40 years old)—especially when BILATERAL—should immediately raise suspicion for Multiple Sclerosis. In MS, demyelinating plaques involve the central myelin (oligodendrocyte-myelinated) portion of the trigeminal root entry zone within the pons, causing ephaptic transmission."
    },
    {
        "q_num": "TRIG-19",
        "category": "Trigeminal Pathway",
        "stem": "The ophthalmic division of the trigeminal nerve (CN V1) divides into three major terminal branches before entering the orbit through the superior orbital fissure. Which of the following represents these three branches?",
        "options": [
            {"letter": "A", "is_correct": True, "text": "Frontal, Lacrimal, and Nasociliary nerves"},
            {"letter": "B", "is_correct": False, "text": "Infraorbital, Zygomatic, and Buccal nerves"},
            {"letter": "C", "is_correct": False, "text": "Auriculotemporal, Lingual, and Mental nerves"},
            {"letter": "D", "is_correct": False, "text": "Greater petrosal, Lesser petrosal, and Deep petrosal nerves"},
            {"letter": "E", "is_correct": False, "text": "Supraorbital, Supratrochlear, and Infratrochlear nerves only"}
        ],
        "explanation": "Correct Answer: A. Frontal, Lacrimal, and Nasociliary nerves.\n\nBranches of CN V1 mnemonic ('Football Lovers Need'):\n• Frontal nerve (largest; divides into supraorbital and supratrochlear nerves to supply forehead and scalp).\n• Lacrimal nerve (supplies lateral upper eyelid and conveys parasympathetic fibers to lacrimal gland).\n• Nasociliary nerve (supplies cornea, ciliary body, ethmoid sinuses, and skin of nasal dorsum and tip via external nasal branch)."
    },
    {
        "q_num": "TRIG-20",
        "category": "Trigeminal Pathway",
        "stem": "In addition to conveying somatosensory fibers from the skin and mucous membranes of the face, cranial nerves VII, IX, and X also share the spinal trigeminal nucleus. Somatic sensory fibers from the external auditory canal and auricle traveling in the vagus nerve (Arnold nerve) synapse in which nucleus?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Nucleus ambiguus"},
            {"letter": "B", "is_correct": False, "text": "Dorsal motor nucleus of vagus"},
            {"letter": "C", "is_correct": True, "text": "Spinal trigeminal nucleus"},
            {"letter": "D", "is_correct": False, "text": "Nucleus solitarius"},
            {"letter": "E", "is_correct": False, "text": "Edinger-Westphal nucleus"}
        ],
        "explanation": "Correct Answer: C. Spinal trigeminal nucleus.\n\nAll general somatic afferent (GSA) fibers from the head—regardless of whether they travel in CN V, CN VII (ear skin), CN IX (posterior ear canal and tympanic membrane), or CN X (auricular branch / Arnold nerve to external auditory canal)—converge and synapse in the Spinal Trigeminal Nucleus. This explains why stimulating the external ear canal with a cotton swab or ear speculum can trigger referred reflex coughing (vagal afferent converging with vagal autonomic motor pathways: the Arnold ear-cough reflex)."
    },

    # =========================================================================
    # 11. ANESTHETIC & NMJ BLOCKING AGENTS (20 Questions: Q41 - Q60)
    # =========================================================================
    {
        "q_num": "ANES-01",
        "category": "Anesthetic & NMJ Blocking Agents",
        "stem": "A 25-year-old man with a family history of anesthetic complications undergoes emergency appendectomy. Anesthesia is induced with propofol and succinylcholine, followed by maintenance with inhaled sevoflurane. Within 15 minutes, his end-tidal CO2 rises sharply from 38 to 85 mm Hg despite hyperventilation. He develops generalized muscle rigidity, tachycardia (145 bpm), tachypnea, and his body temperature spikes to 41.2°C (106.2°F). Laboratory studies reveal severe metabolic acidosis and hyperkalemia. Mutation in which gene is most commonly responsible for this life-threatening pharmacogenetic syndrome?",
        "options": [
            {"letter": "A", "is_correct": True, "text": "RYR1 (Ryanodine receptor 1)"},
            {"letter": "B", "is_correct": False, "text": "CACNA1S (Dihydropyridine receptor)"},
            {"letter": "C", "is_correct": False, "text": "SCN4A (Voltage-gated sodium channel)"},
            {"letter": "D", "is_correct": False, "text": "BCHE (Butyrylcholinesterase)"},
            {"letter": "E", "is_correct": False, "text": "ATP2A1 (SERCA1 pump)"}
        ],
        "explanation": "Correct Answer: A. RYR1 (Ryanodine receptor 1).\n\nThis patient has Malignant Hyperthermia (MH):\n• Trigger: Volatile halogenated inhaled anesthetics (sevoflurane, desflurane, isoflurane, halothane) or the depolarizing muscle relaxant Succinylcholine.\n• Genetics: Autosomal dominant mutation in the RYR1 gene (~70-80% of cases) encoding the skeletal muscle sarcoplasmic reticulum ryanodine receptor calcium release channel (or less commonly CACNA1S).\n• Pathophysiology: Uncontrolled massive release of Ca2+ from the sarcoplasmic reticulum into the myoplasm triggers sustained muscle contraction, hypermetabolism, ATP depletion, massive CO2 production, hyperthermia, rhabdomyolysis, and hyperkalemia.\n• Treatment: Immediate discontinuation of triggers, hyperventilation with 100% O2, and IV Dantrolene."
    },
    {
        "q_num": "ANES-02",
        "category": "Anesthetic & NMJ Blocking Agents",
        "stem": "Dantrolene is the life-saving antidote for malignant hyperthermia. By what specific molecular mechanism does dantrolene arrest the hypermetabolic crisis of malignant hyperthermia?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Inhibits acetylcholinesterase to increase synaptic acetylcholine"},
            {"letter": "B", "is_correct": True, "text": "Blocks ryanodine receptors (RYR1), preventing calcium release from the sarcoplasmic reticulum"},
            {"letter": "C", "is_correct": False, "text": "Competitively blocks postsynaptic nicotinic receptors"},
            {"letter": "D", "is_correct": False, "text": "Activates mitochondrial ATP synthesis"},
            {"letter": "E", "is_correct": False, "text": "Chelates extracellular calcium ions"}
        ],
        "explanation": "Correct Answer: B. Blocks ryanodine receptors (RYR1), preventing calcium release from the sarcoplasmic reticulum.\n\nDantrolene is a skeletal muscle relaxant that acts intracellularly by directly binding to the Ryanodine Receptor 1 (RYR1) channel on the sarcoplasmic reticulum membrane. It inhibits channel opening, blocking the release of sequestered Ca2+ into the cytoplasm. This decouples excitation-contraction coupling, halting actin-myosin cross-bridge cycling and terminating the hypermetabolic cascade."
    },
    {
        "q_num": "ANES-03",
        "category": "Anesthetic & NMJ Blocking Agents",
        "stem": "Succinylcholine is a depolarizing neuromuscular blocker commonly used for rapid sequence intubation. Following a single bolus of succinylcholine, a patient exhibits Phase I neuromuscular blockade. Which of the following electrophysiological findings on train-of-four (TOF) peripheral nerve stimulation is characteristic of Phase I block?",
        "options": [
            {"letter": "A", "is_correct": True, "text": "Constant but equal reduction in twitch height across all four stimuli (no fade) and absent post-tetanic potentiation"},
            {"letter": "B", "is_correct": False, "text": "Progressive decrease in twitch height across the four stimuli (fade) with post-tetanic facilitation"},
            {"letter": "C", "is_correct": False, "text": "Complete reversal of the block following administration of neostigmine"},
            {"letter": "D", "is_correct": False, "text": "Selective enhancement of the fourth twitch relative to the first"},
            {"letter": "E", "is_correct": False, "text": "Complete absence of motor endplate depolarization"}
        ],
        "explanation": "Correct Answer: A. Constant but equal reduction in twitch height across all four stimuli (no fade) and absent post-tetanic potentiation.\n\nComparison of Neuromuscular Blockade Phases:\n• Phase I Block (depolarizing block by succinylcholine): Sustained depolarization of the motor endplate. On Train-of-Four (TOF), all 4 twitches are equally reduced in amplitude (NO fade, TOF ratio = 1.0). There is NO post-tetanic facilitation. Reversal by neostigmine is CONTRAINDICATED (it intensifies Phase I block by inhibiting butyrylcholinesterase).\n• Phase II Block (desensitization block from prolonged/repeated succinylcholine exposure or non-depolarizing agents): Characterized by FADE on TOF (progressive decrease in twitch height 1 to 4) and post-tetanic facilitation; CAN be reversed by neostigmine."
    },
    {
        "q_num": "ANES-04",
        "category": "Anesthetic & NMJ Blocking Agents",
        "stem": "A 30-year-old man who sustained full-thickness third-degree burns covering 45% of his body surface area 10 days ago requires emergency surgical debridement. The anesthesiologist avoids using succinylcholine for intubation. Why is succinylcholine strictly contraindicated in patients with severe burns, crush injuries, or denervation injuries?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Risk of severe hypocalcemia and tetany"},
            {"letter": "B", "is_correct": True, "text": "Risk of life-threatening hyperkalemia and fatal cardiac arrest"},
            {"letter": "C", "is_correct": False, "text": "Risk of irreversible bronchospasm"},
            {"letter": "D", "is_correct": False, "text": "Immediate metabolism by pseudocholinesterase rendering it ineffective"},
            {"letter": "E", "is_correct": False, "text": "Risk of severe hypertension and cerebral hemorrhage"}
        ],
        "explanation": "Correct Answer: B. Risk of life-threatening hyperkalemia and fatal cardiac arrest.\n\nIn severe burns, crush injuries, stroke, or denervation injuries, skeletal muscle undergoes widespread upregulation and proliferation of extrajunctional acetylcholine receptors (including embryonic alpha-7 nicotinic AChRs) across the entire sarcolemma. Administration of succinylcholine causes open-channel depolarization across these vast extrajunctional receptors, resulting in massive, uncontrolled efflux of intracellular K+ into the circulation. Serum potassium can surge by 5-10 mEq/L within minutes, triggering ventricular fibrillation and cardiac arrest."
    },
    {
        "q_num": "ANES-05",
        "category": "Anesthetic & NMJ Blocking Agents",
        "stem": "A 24-year-old woman undergoes elective laparoscopic surgery. She receives succinylcholine for tracheal intubation. Normally, muscle paralysis from succinylcholine resolves within 5 to 10 minutes. However, this patient remains completely paralyzed and apneic for over 4 hours postoperatively. Which genetic enzyme deficiency is the cause of her prolonged neuromuscular blockade?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Acetylcholinesterase deficiency"},
            {"letter": "B", "is_correct": True, "text": "Pseudocholinesterase (butyrylcholinesterase / plasma cholinesterase) deficiency"},
            {"letter": "C", "is_correct": False, "text": "Glucose-6-phosphate dehydrogenase deficiency"},
            {"letter": "D", "is_correct": False, "text": "Cytochrome P450 2D6 poor metabolizer"},
            {"letter": "E", "is_correct": False, "text": "Dihydropyrimidine dehydrogenase deficiency"}
        ],
        "explanation": "Correct Answer: B. Pseudocholinesterase (butyrylcholinesterase / plasma cholinesterase) deficiency.\n\nSuccinylcholine is normally rapidly hydrolyzed in the bloodstream by plasma Pseudocholinesterase (butyrylcholinesterase / BCHE), synthesized by the liver, giving it a brief clinical duration of 5-10 minutes. Patients with atypical or deficient pseudocholinesterase (autosomal recessive inheritance, detected by the dibucaine number test) cannot metabolize succinylcholine, leading to persistent neuromuscular blockade and prolonged apnea lasting several hours. Management is mechanical ventilation until the drug clears passively."
    },
    {
        "q_num": "ANES-06",
        "category": "Anesthetic & NMJ Blocking Agents",
        "stem": "The potency of an inhaled general anesthetic is quantified by its Minimum Alveolar Concentration (MAC). Agent X has a MAC of 1.2%, while Agent Y has a MAC of 6.0%. Which of the following statements comparing these two anesthetics is correct?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Agent Y is 5 times more potent than Agent X"},
            {"letter": "B", "is_correct": True, "text": "Agent X is 5 times more potent than Agent Y"},
            {"letter": "C", "is_correct": False, "text": "Agent X induces anesthesia faster than Agent Y"},
            {"letter": "D", "is_correct": False, "text": "Agent Y has a higher oil-gas partition coefficient than Agent X"},
            {"letter": "E", "is_correct": False, "text": "Agent X and Agent Y have equal potency"}
        ],
        "explanation": "Correct Answer: B. Agent X is 5 times more potent than Agent Y.\n\n• Minimum Alveolar Concentration (MAC) is the alveolar concentration of an inhaled anesthetic at 1 atmosphere of pressure that prevents movement in 50% of patients in response to a standard surgical incision (noxious stimulus).\n• MAC is INVERSELY proportional to potency (Potency = 1 / MAC).\n• Agent X (MAC 1.2%) has a lower MAC than Agent Y (MAC 6.0%), meaning Agent X requires a lower concentration to produce anesthesia and is therefore 5 times more potent (6.0 / 1.2 = 5).\n• Potency correlates directly with lipid solubility (high oil-gas partition coefficient / Meyer-Overton rule)."
    },
    {
        "q_num": "ANES-07",
        "category": "Anesthetic & NMJ Blocking Agents",
        "stem": "The speed of induction and recovery of an inhaled general anesthetic is primarily determined by which physicochemical property?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Oil-gas partition coefficient"},
            {"letter": "B", "is_correct": True, "text": "Blood-gas partition coefficient (solubility in blood)"},
            {"letter": "C", "is_correct": False, "text": "Molecular weight of the anesthetic molecule"},
            {"letter": "D", "is_correct": False, "text": "Alveolar ventilation rate only"},
            {"letter": "E", "is_correct": False, "text": "Rate of hepatic metabolism"}
        ],
        "explanation": "Correct Answer: B. Blood-gas partition coefficient (solubility in blood).\n\n• Speed of induction/recovery is INVERSELY proportional to blood solubility (blood-gas partition coefficient):\n  - Insoluble gases (low blood-gas coefficient, e.g., nitrous oxide = 0.47, desflurane = 0.42): Very little gas dissolves in blood; blood saturates quickly, allowing alveolar and arterial partial pressures to rise rapidly, which rapidly equilibrates with brain partial pressure → FAST induction and FAST recovery.\n  - Highly soluble gases (high blood-gas coefficient, e.g., halothane = 2.4): Large amounts of drug dissolve in blood (acting as a sponge); alveolar and arterial partial pressures rise slowly → SLOW induction and SLOW recovery."
    },
    {
        "q_num": "ANES-08",
        "category": "Anesthetic & NMJ Blocking Agents",
        "stem": "Which intravenous anesthetic is an alkylphenol derivative that potentiates GABA-A receptors, causes rapid onset of anesthesia with smooth recovery, possesses significant antiemetic properties, but can cause vasodilation, hypotension, and 'propofol infusion syndrome' during prolonged high-dose infusions?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Ketamine"},
            {"letter": "B", "is_correct": False, "text": "Etomidate"},
            {"letter": "C", "is_correct": True, "text": "Propofol"},
            {"letter": "D", "is_correct": False, "text": "Midazolam"},
            {"letter": "E", "is_correct": False, "text": "Dexmedetomidine"}
        ],
        "explanation": "Correct Answer: C. Propofol.\n\nPropofol (2,6-diisopropylphenol) is the most widely used IV induction agent:\n• Mechanism: Allosteric potentiation of inhibitory GABA-A receptors and direct channel gating at higher concentrations.\n• Clinical advantages: Rapid onset (~30-40 seconds), rapid emergence, and intrinsic antiemetic properties.\n• Adverse effects: Marked systemic vasodilation and myocardial depression (hypotension). Prolonged high-dose ICU infusion can cause Propofol Infusion Syndrome (PRIS: metabolic acidosis, hyperkalemia, hyperlipidemia, rhabdomyolysis, hepatomegaly, and refractory heart failure)."
    },
    {
        "q_num": "ANES-09",
        "category": "Anesthetic & NMJ Blocking Agents",
        "stem": "A 75-year-old man with severe aortic stenosis and ischemic cardiomyopathy requires emergency abdominal surgery. The anesthesiologist selects etomidate for induction because of its remarkable hemodynamic stability. What is the major endocrine adverse effect of etomidate that limits its use to single induction boluses?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Inhibition of insulin release causing severe ketoacidosis"},
            {"letter": "B", "is_correct": True, "text": "Inhibition of 11-beta-hydroxylase causing primary adrenocortical suppression"},
            {"letter": "C", "is_correct": False, "text": "Suppression of parathyroid hormone causing tetany"},
            {"letter": "D", "is_correct": False, "text": "Stimulation of antidiuretic hormone causing severe hyponatremia"},
            {"letter": "E", "is_correct": False, "text": "Inhibition of thyroid hormone synthesis"}
        ],
        "explanation": "Correct Answer: B. Inhibition of 11-beta-hydroxylase causing primary adrenocortical suppression.\n\nEtomidate is an imidazole-derived IV induction agent prized for its minimal cardiovascular depression (no drop in blood pressure or cardiac output). However, its imidazole ring binds to and inhibits 11-beta-hydroxylase, the key enzyme converting 11-deoxycortisol to cortisol (and 11-deoxycorticosterone to corticosterone) in the adrenal cortex. Even a single induction dose can cause transient primary adrenal insufficiency, and continuous infusions are associated with increased mortality in septic shock."
    },
    {
        "q_num": "ANES-10",
        "category": "Anesthetic & NMJ Blocking Agents",
        "stem": "A 10-year-old child with severe asthma requires closed reduction of a fractured forearm in the emergency department. Ketamine is administered. Ketamine provides 'dissociative anesthesia' where the patient appears awake with eyes open but is completely detached from the environment. What is the primary molecular mechanism of action of ketamine?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Agonist at GABA-A receptors"},
            {"letter": "B", "is_correct": True, "text": "Non-competitive antagonist at NMDA glutamate receptors"},
            {"letter": "C", "is_correct": False, "text": "Agonist at mu-opioid receptors"},
            {"letter": "D", "is_correct": False, "text": "Antagonist at D2 dopamine receptors"},
            {"letter": "E", "is_correct": False, "text": "Agonist at alpha-2 adrenergic receptors"}
        ],
        "explanation": "Correct Answer: B. Non-competitive antagonist at NMDA glutamate receptors.\n\nKetamine (a phencyclidine / PCP derivative) acts as a non-competitive antagonist at the NMDA receptor ion channel pore, inhibiting excitatory glutamatergic transmission in the cortex and limbic system:\n• Effects: Dissociative anesthesia, intense analgesia, and amnesia, while preserving spontaneous respiration and airway reflexes.\n• Sympathomimetic: Inhibits catecholamine reuptake, increasing heart rate, blood pressure, and causing bronchodilation (ideal for asthmatics and hypovolemic trauma patients).\n• Adverse effects: Increases intracranial pressure (ICP) and causes emergence delirium/vivid hallucinations (reduced by co-administering benzodiazepines)."
    },
    {
        "q_num": "ANES-11",
        "category": "Anesthetic & NMJ Blocking Agents",
        "stem": "Which of the following intravenous sedative-anesthetics is a highly selective alpha-2 adrenergic agonist that acts in the locus coeruleus to produce conscious sedation that resembles natural non-REM sleep, provides mild analgesia, and does not cause respiratory depression?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Propofol"},
            {"letter": "B", "is_correct": False, "text": "Etomidate"},
            {"letter": "C", "is_correct": False, "text": "Midazolam"},
            {"letter": "D", "is_correct": True, "text": "Dexmedetomidine"},
            {"letter": "E", "is_correct": False, "text": "Thiopental"}
        ],
        "explanation": "Correct Answer: D. Dexmedetomidine.\n\nDexmedetomidine is a potent, centrally-acting alpha-2 adrenergic receptor agonist (selectivity ratio alpha-2:alpha-1 is 1620:1, ~8x higher than clonidine):\n• Mechanism: Binds presynaptic alpha-2 receptors in the locus coeruleus of the pons, inhibiting norepinephrine release.\n• Unique features: Produces 'cooperative sedation' (patients are easily rousable and can follow commands when stimulated) without causing respiratory depression, making it ideal for ICU weaning from mechanical ventilation and awake fiberoptic intubation.\n• Side effects: Bradycardia and hypotension."
    },
    {
        "q_num": "ANES-12",
        "category": "Anesthetic & NMJ Blocking Agents",
        "stem": "Which non-depolarizing neuromuscular blocking drug is an isoquinoline derivative that undergoes spontaneous, non-enzymatic degradation in plasma and tissue via Hofmann elimination at physiological body temperature and pH, making it the neuromuscular blocker of choice for patients with renal or hepatic failure?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Rocuronium"},
            {"letter": "B", "is_correct": False, "text": "Vecuronium"},
            {"letter": "C", "is_correct": False, "text": "Pancuronium"},
            {"letter": "D", "is_correct": True, "text": "Cisatracurium (and atracurium)"},
            {"letter": "E", "is_correct": False, "text": "Succinylcholine"}
        ],
        "explanation": "Correct Answer: D. Cisatracurium (and atracurium).\n\nCisatracurium and atracurium are benzylisoquinolinium non-depolarizing neuromuscular blockers that undergo organ-independent elimination:\n• Hofmann elimination: Spontaneous chemical breakdown of the molecule in plasma and tissues driven purely by physiological pH (7.4) and temperature (37°C) into inactive laudanosine and monoquaternary alcohol.\n• Because clearance does not depend on liver metabolism or renal excretion, cisatracurium is the preferred paralytic agent for patients with end-stage renal disease (ESRD) or severe hepatic failure, and for prolonged neuromuscular blockade in ARDS."
    },
    {
        "q_num": "ANES-13",
        "category": "Anesthetic & NMJ Blocking Agents",
        "stem": "During a knee arthroscopy under local infiltration anesthesia, 30 mL of 0.5% bupivacaine is inadvertently injected into a vein. Five minutes later, the patient develops circumoral numbness, tinnitus, metallic taste in his mouth, followed immediately by generalized tonic-clonic seizures, severe bradycardia, wide-complex ventricular tachycardia, and cardiovascular collapse. Which of the following is the specific rescue antidote for Local Anesthetic Systemic Toxicity (LAST)?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Intravenous calcium gluconate"},
            {"letter": "B", "is_correct": True, "text": "Intravenous 20% lipid emulsion (Intralipid)"},
            {"letter": "C", "is_correct": False, "text": "Intravenous sodium bicarbonate"},
            {"letter": "D", "is_correct": False, "text": "Intravenous flumazenil"},
            {"letter": "E", "is_correct": False, "text": "Intravenous dantrolene"}
        ],
        "explanation": "Correct Answer: B. Intravenous 20% lipid emulsion (Intralipid).\n\nThis patient has Local Anesthetic Systemic Toxicity (LAST):\n• Bupivacaine is highly lipophilic and dissociates very slowly from cardiac sodium channels during diastole ('fast in, slow out'), leading to severe cardiotoxicity, refractory ventricular arrhythmias, and cardiac arrest.\n• Antidote: 20% IV Lipid Emulsion (Intralipid). Mechanism involves the 'lipid sink' theory (the lipid emulsion creates an intravascular lipid phase that sequesters the lipophilic bupivacaine away from target tissues in the heart and brain) and direct metabolic/inotropic support to cardiac mitochondria."
    },
    {
        "q_num": "ANES-14",
        "category": "Anesthetic & NMJ Blocking Agents",
        "stem": "Local anesthetics block voltage-gated sodium channels from the intracellular side of the axonal membrane. To reach their binding site, local anesthetics must cross the lipophilic lipid bilayer in which chemical form, and bind to the channel in which chemical form?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Cross membrane as ionized (charged); bind to channel as non-ionized (uncharged)"},
            {"letter": "B", "is_correct": True, "text": "Cross membrane as non-ionized (uncharged/base); bind to channel as ionized (charged/cation)"},
            {"letter": "C", "is_correct": False, "text": "Cross membrane as ionized; bind to channel as ionized"},
            {"letter": "D", "is_correct": False, "text": "Cross membrane as non-ionized; bind to channel as non-ionized"},
            {"letter": "E", "is_correct": False, "text": "Pass through open aquaporin pores"}
        ],
        "explanation": "Correct Answer: B. Cross membrane as non-ionized (uncharged/base); bind to channel as ionized (charged/cation).\n\nLocal anesthetics are weak bases (pKa typically 7.6-8.9):\n• To diffuse across the hydrophobic neuronal lipid bilayer, the molecule MUST be in its uncharged (non-ionized, free base) form (B).\n• Once inside the axoplasm, the molecule becomes protonated into its charged, ionized cation form (BH+).\n• The ionized (BH+) form binds to the intracellular mouth of the voltage-gated Na+ channel to block Na+ conductance.\n• In infected or inflamed tissue (acidic pH < 6.0), more of the drug is ionized outside the cell, preventing membrane penetration and explaining why local anesthetics are ineffective in abscesses."
    },
    {
        "q_num": "ANES-15",
        "category": "Anesthetic & NMJ Blocking Agents",
        "stem": "Which of the following inhaled anesthetics has the lowest blood-gas partition coefficient (0.42), allowing the fastest induction and emergence of all volatile agents, but can cause airway irritation, coughing, and breath-holding during inhalation induction, requiring a specialized heated vaporizer?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Halothane"},
            {"letter": "B", "is_correct": False, "text": "Isoflurane"},
            {"letter": "C", "is_correct": False, "text": "Sevoflurane"},
            {"letter": "D", "is_correct": True, "text": "Desflurane"},
            {"letter": "E", "is_correct": False, "text": "Enflurane"}
        ],
        "explanation": "Correct Answer: D. Desflurane.\n\n• Desflurane has the lowest blood-gas solubility (0.42) of all volatile agents, providing near-instantaneous changes in anesthetic depth and rapid emergence regardless of procedure duration.\n• However, it has a high vapor pressure (boils at 22.8°C / room temperature), requiring a specialized heated, pressurized vaporizer (Tec 6).\n• It is pungent and irritates the airway, making it unsuitable for mask induction.\n• (In contrast, Sevoflurane has sweet, non-pungent odor and is preferred for pediatric mask induction)."
    },
    {
        "q_num": "ANES-16",
        "category": "Anesthetic & NMJ Blocking Agents",
        "stem": "A 58-year-old woman undergoes elective surgery with halothane anesthesia in a developing country. Five days postoperatively, she develops anorexia, nausea, fever, jaundice, and tender hepatomegaly. Laboratory evaluation reveals marked AST and ALT elevations (>3,000 U/L) and a prolonged prothrombin time. Liver biopsy shows massive centrilobular hepatic necrosis. What is the pathogenesis of halothane hepatitis?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Direct dose-dependent toxic inhibition of mitochondrial beta-oxidation"},
            {"letter": "B", "is_correct": True, "text": "Immune-mediated hypersensitivity reaction against trifluoroacetylated liver proteins"},
            {"letter": "C", "is_correct": False, "text": "Biliary sludge obstruction of the common bile duct"},
            {"letter": "D", "is_correct": False, "text": "Reactivation of hepatitis B virus"},
            {"letter": "E", "is_correct": False, "text": "Ischemic necrosis from portal vein thrombosis"}
        ],
        "explanation": "Correct Answer: B. Immune-mediated hypersensitivity reaction against trifluoroacetylated liver proteins.\n\nHalothane undergoes significant hepatic metabolism (~20-25%) by CYP2E1, producing a reactive trifluoroacetyl (TFA) chloride intermediate. This intermediate covalently binds to normal hepatocyte proteins, forming trifluoroacetylated neoantigens. In susceptible patients (especially with prior halothane exposure), the immune system generates anti-TFA antibodies that trigger a severe, antibody-mediated auto-allergic response, causing fulminant centrilobular hepatic necrosis (halothane hepatitis) with a mortality rate of up to 50%."
    },
    {
        "q_num": "ANES-17",
        "category": "Anesthetic & NMJ Blocking Agents",
        "stem": "Which of the following local anesthetics is formulated with prilocaine in EMLA cream, can be used for mucous membrane anesthesia, and can cause methemoglobinemia (chocolate-colored blood and cyanosis unresponsive to oxygen) as a classic toxic metabolite adverse effect?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Bupivacaine"},
            {"letter": "B", "is_correct": True, "text": "Benzocaine (and Prilocaine)"},
            {"letter": "C", "is_correct": False, "text": "Ropivacaine"},
            {"letter": "D", "is_correct": False, "text": "Procaine"},
            {"letter": "E", "is_correct": False, "text": "Chloroprocaine"}
        ],
        "explanation": "Correct Answer: B. Benzocaine (and Prilocaine).\n\nBenzocaine (topical spray for endoscopy/dental work) and Prilocaine (metabolized to o-toluidine) can oxidize ferrous iron (Fe2+) in hemoglobin to ferric iron (Fe3+), forming Methemoglobin. Methemoglobin cannot bind oxygen and shifts the remaining hemoglobin oxygen dissociation curve to the left (tissue hypoxia). Patients present with 'chocolate brown' blood, cyanosis, and low oxygen saturation (pulse oximeter reads ~85% regardless of actual PO2). Treatment: IV Methylene Blue (reduces Fe3+ back to Fe2+)."
    },
    {
        "q_num": "ANES-18",
        "category": "Anesthetic & NMJ Blocking Agents",
        "stem": "Why is epinephrine frequently added to local anesthetic solutions (e.g., 1% lidocaine with 1:100,000 epinephrine) for infiltration into peripheral tissues?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "To increase the systemic absorption of the local anesthetic"},
            {"letter": "B", "is_correct": True, "text": "To induce local vasoconstriction, which prolongs the duration of anesthesia and decreases systemic toxicity"},
            {"letter": "C", "is_correct": False, "text": "To decrease the latency of local anesthetic onset by neutralizing tissue pH"},
            {"letter": "D", "is_correct": False, "text": "To directly block voltage-gated sodium channels"},
            {"letter": "E", "is_correct": False, "text": "To prevent allergic reactions to ester local anesthetics"}
        ],
        "explanation": "Correct Answer: B. To induce local vasoconstriction, which prolongs the duration of anesthesia and decreases systemic toxicity.\n\nEpinephrine acts on alpha-1 adrenergic receptors in local vascular smooth muscle, causing profound vasoconstriction. This:\n1. Decreases local blood flow, reducing surgical bleeding.\n2. Slows systemic absorption of the local anesthetic into the bloodstream, prolonging the local duration of action.\n3. Decreases peak plasma concentrations of the local anesthetic, lowering the risk of systemic toxicity (LAST)."
    },
    {
        "q_num": "ANES-19",
        "category": "Anesthetic & NMJ Blocking Agents",
        "stem": "Which of the following competitive non-depolarizing neuromuscular blocking agents has the most rapid onset of action (60–90 seconds at a dose of 1.2 mg/kg), making it the primary non-depolarizing alternative to succinylcholine for rapid sequence intubation (RSI)?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Pancuronium"},
            {"letter": "B", "is_correct": True, "text": "Rocuronium"},
            {"letter": "C", "is_correct": False, "text": "Vecuronium"},
            {"letter": "D", "is_correct": False, "text": "Atracurium"},
            {"letter": "E", "is_correct": False, "text": "Tubocurarine"}
        ],
        "explanation": "Correct Answer: B. Rocuronium.\n\nRocuronium is an aminosteroid non-depolarizing neuromuscular blocker. Because it has relatively low potency compared to vecuronium, a larger molar dose is administered. This high concentration gradient drives rapid diffusion to the neuromuscular junction, providing intubating conditions in 60-90 seconds. It is the primary non-depolarizing drug for Rapid Sequence Intubation when succinylcholine is contraindicated (burns, hyperkalemia, denervation). Its effects can be rapidly reversed by sugammadex."
    },
    {
        "q_num": "ANES-20",
        "category": "Anesthetic & NMJ Blocking Agents",
        "stem": "Which of the following intravenous general anesthetics is an ultra-short-acting barbiturate that induces anesthesia within one arm-brain circulation time (~20 seconds) and whose rapid recovery from a single bolus is driven not by metabolic clearance, but by rapid redistribution from the brain to skeletal muscle and adipose tissue?",
        "options": [
            {"letter": "A", "is_correct": True, "text": "Thiopental"},
            {"letter": "B", "is_correct": False, "text": "Midazolam"},
            {"letter": "C", "is_correct": False, "text": "Etomidate"},
            {"letter": "D", "is_correct": False, "text": "Ketamine"},
            {"letter": "E", "is_correct": False, "text": "Lorazepam"}
        ],
        "explanation": "Correct Answer: A. Thiopental.\n\nThiopental is an ultra-short-acting barbiturate with high lipid solubility:\n• Onset: Crosses the blood-brain barrier rapidly into the well-perfused brain within 20-30 seconds.\n• Termination of action: Patient awakens within 5-10 minutes following a single bolus dose. This termination is NOT due to hepatic metabolism, but rather rapid REDISTRIBUTION of the drug from highly perfused organs (brain, heart) to intermediate-perfused tissues (skeletal muscle) and ultimately into poorly perfused adipose tissue."
    },

    # =========================================================================
    # 12. HEADACHE (20 Questions: Q61 - Q80)
    # =========================================================================
    {
        "q_num": "HA-01",
        "category": "Headache",
        "stem": "A 28-year-old woman presents with recurrent, severe, throbbing headaches that are strictly unilateral (left-sided) and last 12 to 24 hours. During attacks, she experiences nausea, vomiting, and extreme sensitivity to bright light (photophobia) and loud sounds (phonophobia). Prior to headache onset, she sees shimmering, jagged, zigzag lines with a blind spot in her right visual field lasting 30 minutes. What underlying neurophysiological process is responsible for the visual aura in migraine?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Acute spasm of the ophthalmic artery causing retinal ischemia"},
            {"letter": "B", "is_correct": True, "text": "Cortical spreading depression (CSD)"},
            {"letter": "C", "is_correct": False, "text": "Transient occlusion of the basilar artery"},
            {"letter": "D", "is_correct": False, "text": "Hyperpolarization of cerebellar Purkinje cells"},
            {"letter": "E", "is_correct": False, "text": "Dural venous sinus microthrombosis"}
        ],
        "explanation": "Correct Answer: B. Cortical spreading depression (CSD).\n\nMigraine with aura is mediated by Cortical Spreading Depression (CSD):\n• A self-propagating wave of slow cellular depolarization (traveling at 2-5 mm/min across the cerebral cortex, typically occipital), followed by prolonged neuronal and glial suppression.\n• The initial wave of depolarization triggers visual scintillating scotomas (aura), while the subsequent activation of meningeal trigeminal perivascular nerves stimulates the release of pro-inflammatory neuropeptides (CGRP, substance P), causing neurogenic vasodilation and throbbing headache."
    },
    {
        "q_num": "HA-02",
        "category": "Headache",
        "stem": "Sumatriptan is an acute abortive medication for moderate-to-severe migraine attacks. Sumatriptan provides rapid relief by acting as an agonist at which specific serotonin receptor subtypes?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "5-HT2A and 5-HT2C receptors"},
            {"letter": "B", "is_correct": True, "text": "5-HT1B and 5-HT1D receptors"},
            {"letter": "C", "is_correct": False, "text": "5-HT3 receptors"},
            {"letter": "D", "is_correct": False, "text": "5-HT4 receptors"},
            {"letter": "E", "is_correct": False, "text": "5-HT7 receptors"}
        ],
        "explanation": "Correct Answer: B. 5-HT1B and 5-HT1D receptors.\n\nTriptans (sumatriptan, rizatriptan, zolmitriptan) are selective 5-HT1B/1D receptor agonists:\n• 5-HT1B receptors: Located on intracranial and meningeal blood vessels; activation causes vasoconstriction of painfully dilated cerebral vessels.\n• 5-HT1D receptors: Located presynaptically on trigeminal nerve endings; activation inhibits the release of calcitonin gene-related peptide (CGRP) and substance P, suppressing neurogenic inflammation and central pain transmission.\n• Contraindication: Coronary artery disease or Prinzmetal angina (can cause coronary vasospasm)."
    },
    {
        "q_num": "HA-03",
        "category": "Headache",
        "stem": "A 35-year-old male smoker awakens at 2:00 AM every night for the past 2 weeks with excruciating, piercing, 'ice-pick' pain centered behind his right eye. The pain lasts 45 minutes and is accompanied by ipsilateral eye redness, profuse tearing (lacrimation), nasal congestion, rhinorrhea, and partial ptosis with miosis (Horner syndrome). During attacks, he paces around the room agitated and unable to lie still. What is the most effective first-line acute abortive treatment for this condition?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Oral acetaminophen and ibuprofen"},
            {"letter": "B", "is_correct": True, "text": "100% high-flow oxygen via non-rebreather mask and subcutaneous sumatriptan"},
            {"letter": "C", "is_correct": False, "text": "Intravenous high-dose methylprednisolone"},
            {"letter": "D", "is_correct": False, "text": "Indomethacin oral therapy"},
            {"letter": "E", "is_correct": False, "text": "Oral topiramate"}
        ],
        "explanation": "Correct Answer: B. 100% high-flow oxygen via non-rebreather mask and subcutaneous sumatriptan.\n\nThis patient has Cluster Headache (a Trigeminal Autonomic Cephalalgia / TAC):\n• Clinical hallmarks: Strictly unilateral, severe retro-orbital/temporal pain lasting 15-180 minutes, nocturnal predilection, ipsilateral autonomic signs (lacrimation, rhinorrhea, conjunctival injection, Horner syndrome), and motor restlessness/pacing.\n• Acute abortive treatment: 100% High-flow Oxygen (12-15 L/min via non-rebreather mask) is first-line and highly effective within 10-15 minutes; subcutaneous sumatriptan or zolmitriptan nasal spray are also first-line.\n• Prophylaxis: Verapamil is the first-line preventive drug of choice."
    },
    {
        "q_num": "HA-04",
        "category": "Headache",
        "stem": "A 72-year-old woman presents with severe right-sided temple headache, scalp tenderness when brushing her hair, malaise, and fatigue. For the past month, she has experienced pain and fatigue in her jaw when chewing tough meats (jaw claudication). She also complains of bilateral aching and morning stiffness in her shoulders and hips. Laboratory studies show an erythrocyte sedimentation rate (ESR) of 105 mm/hr and C-reactive protein (CRP) of 45 mg/L. What is the most feared complication if treatment is delayed, and what is the immediate management?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Rupture of a cerebral aneurysm; Urgent neurosurgical clipping"},
            {"letter": "B", "is_correct": True, "text": "Irreversible blindness from anterior ischemic optic neuropathy; Immediate high-dose oral prednisone"},
            {"letter": "C", "is_correct": False, "text": "Cavernous sinus thrombosis; Therapeutic anticoagulation"},
            {"letter": "D", "is_correct": False, "text": "Brainstem stroke; Intravenous thrombolysis"},
            {"letter": "E", "is_correct": False, "text": "Meningitis; Intravenous ceftriaxone and vancomycin"}
        ],
        "explanation": "Correct Answer: B. Irreversible blindness from anterior ischemic optic neuropathy; Immediate high-dose oral prednisone.\n\nThis patient has Giant Cell (Temporal) Arteritis (GCA), commonly associated with Polymyalgia Rheumatica:\n• Presentation: Age >50, new unaccustomed headache, temporal artery tenderness/induration, jaw claudication (highly specific), and markedly elevated ESR/CRP.\n• Feared complication: Permanent, irreversible blindness due to occlusion of the posterior ciliary arteries supplying the optic nerve head (Arteritic Anterior Ischemic Optic Neuropathy / AION).\n• Management: Immediate high-dose systemic corticosteroids (prednisone 60 mg/day or IV methylprednisolone if visual symptoms exist) MUST be initiated immediately before waiting for a temporal artery biopsy (which demonstrates granulomatous inflammation of the media with multinucleated giant cells)."
    },
    {
        "q_num": "HA-05",
        "category": "Headache",
        "stem": "A 45-year-old accountant presents with a dull, bilateral, aching headache that feels like a 'tight band squeezing around my entire head.' The headache is present almost daily, worsening toward the end of the workday. There is no nausea, vomiting, photophobia, or phonophobia, and physical activity does not worsen the pain. Examination reveals pericranial muscle tenderness upon palpation of the trapezius and temporalis muscles. What is the diagnosis?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Migraine without aura"},
            {"letter": "B", "is_correct": True, "text": "Tension-type headache"},
            {"letter": "C", "is_correct": False, "text": "Cluster headache"},
            {"letter": "D", "is_correct": False, "text": "Trigeminal neuralgia"},
            {"letter": "E", "is_correct": False, "text": "Temporal arteritis"}
        ],
        "explanation": "Correct Answer: B. Tension-type headache.\n\nTension-type headache (TTH) is the most common primary headache disorder in adults:\n• Clinical features: Bilateral, non-pulsatile, dull/pressing/tightening pain ('tight band or vise around the head'), mild-to-moderate intensity, not aggravated by routine physical activity.\n• Diagnostic criteria: NO nausea or vomiting; at most one of photophobia OR phonophobia (never both).\n• Physical exam: Tenderness of pericranial and neck/shoulder musculature.\n• Acute treatment: NSAIDs, acetaminophen, aspirin.\n• Chronic prophylaxis (if >15 days/month): Amitriptyline (tricyclic antidepressant)."
    },
    {
        "q_num": "HA-06",
        "category": "Headache",
        "stem": "Calcitonin Gene-Related Peptide (CGRP) is a 37-amino acid neuropeptide that plays a pivotal role in the pathophysiology of migraine by inducing potent intracranial vasodilation and mast cell degranulation. Which of the following monoclonal antibodies is approved for migraine prevention and acts by specifically binding to and blocking the CGRP receptor?",
        "options": [
            {"letter": "A", "is_correct": True, "text": "Erenumab"},
            {"letter": "B", "is_correct": False, "text": "Fremanezumab"},
            {"letter": "C", "is_correct": False, "text": "Galcanezumab"},
            {"letter": "D", "is_correct": False, "text": "Eptinezumab"},
            {"letter": "E", "is_correct": False, "text": "Ubrogepant"}
        ],
        "explanation": "Correct Answer: A. Erenumab.\n\nCGRP-targeted therapies for migraine:\n• CGRP Receptor antagonist monoclonal antibody: Erenumab (specifically binds to the canonical CGRP receptor complex).\n• CGRP Ligand-targeted monoclonal antibodies: Fremanezumab, Galcanezumab, and Eptinezumab (bind directly to the circulating CGRP peptide itself).\n• Small-molecule CGRP receptor antagonists ('gepants'): Ubrogepant, Rimegepant, and Atogepant (oral agents for acute treatment and/or prevention)."
    },
    {
        "q_num": "HA-07",
        "category": "Headache",
        "stem": "A 36-year-old woman with a history of episodic migraines presents with daily, dull, diffuse headaches that have worsened over the past 4 months. She reports taking combination acetaminophen/aspirin/caffeine tablets 5 days a week, plus rizatriptan 3 to 4 days a week for the last 6 months. Whenever she tries to stop taking these medications, her headache intensifies severely within 24 hours. What is the diagnosis?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Chronic tension-type headache"},
            {"letter": "B", "is_correct": True, "text": "Medication overuse headache (rebound headache)"},
            {"letter": "C", "is_correct": False, "text": "Idiopathic intracranial hypertension"},
            {"letter": "D", "is_correct": False, "text": "Paroxysmal hemicrania"},
            {"letter": "E", "is_correct": False, "text": "Chronic meningitis"}
        ],
        "explanation": "Correct Answer: B. Medication overuse headache (rebound headache).\n\nMedication Overuse Headache (MOH) occurs in patients with pre-existing primary headache disorders (usually migraine):\n• Diagnostic criteria: Headache present on ≥15 days per month in a patient with regular overuse of acute headache medications for >3 months (≥10 days/month for triptans, opioids, or combination analgesics; ≥15 days/month for simple NSAIDs/acetaminophen).\n• Presentation: Daily, dull, refractory headache present upon waking that temporarily abates after taking analgesics, only to recur when the drug wears off.\n• Treatment: Complete withdrawal of the overused acute medication, bridging therapy, and initiation of a preventive medication (e.g., topiramate, beta-blocker, or CGRP antibody)."
    },
    {
        "q_num": "HA-08",
        "category": "Headache",
        "stem": "A 30-year-old woman with frequent disabling migraines is evaluated for preventive therapy. Which of the following oral medications is an anticonvulsant approved for migraine prophylaxis that blocks voltage-gated sodium channels, potentiates GABA, inhibits AMPA receptors, and commonly causes paresthesias, weight loss, kidney stones, and cognitive slowing ('dopamax')?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Valproic acid"},
            {"letter": "B", "is_correct": True, "text": "Topiramate"},
            {"letter": "C", "is_correct": False, "text": "Lamotrigine"},
            {"letter": "D", "is_correct": False, "text": "Carbamazepine"},
            {"letter": "E", "is_correct": False, "text": "Phenytoin"}
        ],
        "explanation": "Correct Answer: B. Topiramate.\n\nTopiramate is a first-line oral preventive agent for chronic and high-frequency episodic migraine:\n• Multiple mechanisms: Blocks voltage-gated Na+ channels, potentiates GABA-A receptor currents, inhibits AMPA/kainate glutamate receptors, and weakly inhibits carbonic anhydrase.\n• Side effect profile: Paresthesias (distal tingling due to carbonic anhydrase inhibition), anorexia and weight loss (often favored by patients), nephrolithiasis (calcium phosphate stones), metabolic acidosis, and word-finding difficulty/cognitive blunting ('dopamax'). It is also teratogenic (cleft lip/palate)."
    },
    {
        "q_num": "HA-09",
        "category": "Headache",
        "stem": "A 40-year-old woman presents with severe unilateral retro-orbital headaches that recur 10 to 20 times per day, each lasting 15 to 30 minutes, accompanied by prominent ipsilateral conjunctival injection and rhinorrhea. Brain MRI is normal. The attacks completely resolve within 48 hours of starting indomethacin. What is the diagnosis?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Cluster headache"},
            {"letter": "B", "is_correct": True, "text": "Paroxysmal hemicrania"},
            {"letter": "C", "is_correct": False, "text": "SUNCT syndrome"},
            {"letter": "D", "is_correct": False, "text": "Hemicrania continua"},
            {"letter": "E", "is_correct": False, "text": "Trigeminal neuralgia"}
        ],
        "explanation": "Correct Answer: B. Paroxysmal hemicrania.\n\nParoxysmal Hemicrania is a Trigeminal Autonomic Cephalalgia (TAC) that predominantly affects women:\n• Clinical presentation: Frequent (usually >5 per day, up to 30/day), brief (2-30 minutes), excruciating unilateral retro-orbital pain accompanied by ipsilateral cranial autonomic features.\n• Hallmark: Complete, absolute responsiveness to therapeutic doses of INDOMETHACIN (indomethacin-responsive headache). If a patient fails to respond to indomethacin, the diagnosis is excluded."
    },
    {
        "q_num": "HA-10",
        "category": "Headache",
        "stem": "A 24-year-old woman with migraine attacks fails therapy with triptans because of severe chest tightness and palpitations. She has a history of coronary vasospasm (Prinzmetal angina). The physician prescribes lasmiditan. Lasmiditan aborts acute migraine attacks without causing vasoconstriction by selectively activating which serotonin receptor?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "5-HT1A receptor"},
            {"letter": "B", "is_correct": False, "text": "5-HT1B receptor"},
            {"letter": "C", "is_correct": False, "text": "5-HT1D receptor"},
            {"letter": "D", "is_correct": True, "text": "5-HT1F receptor"},
            {"letter": "E", "is_correct": False, "text": "5-HT2B receptor"}
        ],
        "explanation": "Correct Answer: D. 5-HT1F receptor.\n\nLasmiditan is a selective 5-HT1F receptor agonist ('ditan'):\n• Unlike triptans (which bind 5-HT1B and cause vasoconstriction), 5-HT1F receptors are located exclusively on trigeminal sensory neurons and in the trigeminal nucleus caudalis without vascular expression.\n• Activation inhibits trigeminal neuropeptide release and central pain transmission without causing vasoconstriction.\n• It is safe in patients with coronary artery disease, stroke, or peripheral vascular disease (though it causes central sedation)."
    },
    {
        "q_num": "HA-11",
        "category": "Headache",
        "stem": "A 50-year-old man presents with episodic headaches. His attacks are strictly unilateral, last 2 to 3 hours, and are triggered predictably within 1 hour of consuming a single alcoholic drink during cluster periods. Verapamil is prescribed for prevention. Verapamil prevents cluster headaches primarily through which pharmacological mechanism?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Potentiation of GABA-A receptors in the hypothalamus"},
            {"letter": "B", "is_correct": True, "text": "Blockade of L-type voltage-gated calcium channels modulating hypothalamic-trigeminal circuitry"},
            {"letter": "C", "is_correct": False, "text": "Competitive inhibition of beta-1 adrenergic receptors"},
            {"letter": "D", "is_correct": False, "text": "Depletion of calcitonin gene-related peptide"},
            {"letter": "E", "is_correct": False, "text": "Inhibition of neuronal nitric oxide synthase"}
        ],
        "explanation": "Correct Answer: B. Blockade of L-type voltage-gated calcium channels modulating hypothalamic-trigeminal circuitry.\n\nVerapamil (a non-dihydropyridine calcium channel blocker) is the first-line prophylactic medication for cluster headache:\n• It blocks L-type voltage-gated Ca2+ channels in vascular smooth muscle and central neurons, stabilizing the posterior hypothalamic pacemaker and inhibiting trigeminovascular activation.\n• High doses are often required (240-960 mg/day), necessitating baseline and surveillance ECGs to monitor for PR interval prolongation and heart block."
    },
    {
        "q_num": "HA-12",
        "category": "Headache",
        "stem": "Which brain structure acts as the primary 'biological clock' and generator for the circadian rhythmicity and nocturnal clustering seen in cluster headaches?",
        "options": [
            {"letter": "A", "is_correct": True, "text": "Posterior hypothalamus (suprachiasmatic nucleus circuitry)"},
            {"letter": "B", "is_correct": False, "text": "Substantia nigra"},
            {"letter": "C", "is_correct": False, "text": "Red nucleus"},
            {"letter": "D", "is_correct": False, "text": "Locus coeruleus"},
            {"letter": "E", "is_correct": False, "text": "Dentate nucleus"}
        ],
        "explanation": "Correct Answer: A. Posterior hypothalamus (suprachiasmatic nucleus circuitry).\n\nCluster headache is closely linked to hypothalamic dysfunction:\n• Attacks demonstrate striking circadian periodicity (frequently striking at the exact same hour every night during REM sleep) and circannual periodicity (clustering in spring and autumn).\n• Functional PET and fMRI imaging show selective activation of the ipsilateral posterior hypothalamic gray matter during acute cluster attacks, confirming the hypothalamus as the central generator."
    },
    {
        "q_num": "HA-13",
        "category": "Headache",
        "stem": "A 22-year-old woman presents to the student health clinic with a throbbing unilateral headache accompanied by photophobia. She has asthma. Which of the following first-line migraine prophylactic medications should be avoided in this patient because of the risk of life-threatening bronchospasm?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Topiramate"},
            {"letter": "B", "is_correct": True, "text": "Propranolol"},
            {"letter": "C", "is_correct": False, "text": "Amitriptyline"},
            {"letter": "D", "is_correct": False, "text": "Erenumab"},
            {"letter": "E", "is_correct": False, "text": "Botulinum toxin type A"}
        ],
        "explanation": "Correct Answer: B. Propranolol.\n\nPropranolol is a non-selective beta-adrenergic antagonist (blocks both beta-1 and beta-2 receptors) approved as first-line migraine prophylaxis. Because it blocks beta-2 receptors on bronchial smooth muscle, it prevents endogenous epinephrine-mediated bronchodilation and can precipitate severe bronchospasm in patients with asthma or COPD. In asthmatic migraineurs, topiramate, valproate, or CGRP monoclonal antibodies are preferred."
    },
    {
        "q_num": "HA-14",
        "category": "Headache",
        "stem": "A 30-year-old woman with chronic migraine (>15 headache days per month for >3 months, with at least 8 meeting migraine criteria) fails multiple oral prophylactic medications. Which treatment involves injecting a neurotoxin into 31 specific sites across the forehead, temples, back of the head, and neck every 12 weeks to prevent chronic migraine?",
        "options": [
            {"letter": "A", "is_correct": True, "text": "OnabotulinumtoxinA (Botox)"},
            {"letter": "B", "is_correct": False, "text": "Tetrodotoxin"},
            {"letter": "C", "is_correct": False, "text": "Capsaicin intradermal injection"},
            {"letter": "D", "is_correct": False, "text": "Bupivacaine trigger point injection"},
            {"letter": "E", "is_correct": False, "text": "Phenol nerve neurolysis"}
        ],
        "explanation": "Correct Answer: A. OnabotulinumtoxinA (Botox).\n\nOnabotulinumtoxinA (Botox) is FDA-approved for the prophylaxis of Chronic Migraine (headache ≥15 days/month, with ≥8 days meeting migraine criteria):\n• Administration: 155 units divided across 31 standardized pericranial injection sites (corrugator, procerus, frontalis, temporalis, occipitalis, cervical paraspinal, and trapezius muscles) every 12 weeks.\n• Mechanism: Cleaves SNAP-25 in peripheral nociceptive nerve endings, inhibiting the release of glutamate, substance P, and CGRP, thereby reducing peripheral nociceptive input to the trigeminal nucleus caudalis and preventing central sensitization."
    },
    {
        "q_num": "HA-15",
        "category": "Headache",
        "stem": "A 26-year-old woman presents with severe episodic headaches preceded by vertigo, bilateral tinnitus, dysarthria, diplopia, and ataxia lasting 45 minutes, followed by an intense occipital throbbing headache. Motor strength is completely normal, and brain MRI is unremarkable. What specific subtype of migraine with aura is present?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Hemiplegic migraine"},
            {"letter": "B", "is_correct": True, "text": "Migraine with brainstem aura (basilar-type migraine)"},
            {"letter": "C", "is_correct": False, "text": "Retinal migraine"},
            {"letter": "D", "is_correct": False, "text": "Vestibular schwannoma"},
            {"letter": "E", "is_correct": False, "text": "Meniere disease"}
        ],
        "explanation": "Correct Answer: B. Migraine with brainstem aura (basilar-type migraine).\n\nMigraine with Brainstem Aura (formerly basilar migraine):\n• Clinical criteria: Migraine accompanied by aura symptoms originating clearly from the brainstem (dysarthria, vertigo, tinnitus, hyperacusis, diplopia, bilateral ataxia, decreased level of consciousness) without motor weakness.\n• Triptans and ergotamines are historically avoided in this disorder due to theoretical concerns over basilar artery vasoconstriction."
    },
    {
        "q_num": "HA-16",
        "category": "Headache",
        "stem": "Familial hemiplegic migraine (FHM) is a rare autosomal dominant form of migraine with aura characterized by reversible motor weakness during the aura phase. FHM type 1 is caused by a gain-of-function mutation in the CACNA1A gene on chromosome 19p13. What ion channel is encoded by CACNA1A?",
        "options": [
            {"letter": "A", "is_correct": True, "text": "P/Q-type voltage-gated calcium channel (Cav2.1)"},
            {"letter": "B", "is_correct": False, "text": "L-type voltage-gated calcium channel (Cav1.2)"},
            {"letter": "C", "is_correct": False, "text": "Voltage-gated sodium channel (Nav1.1)"},
            {"letter": "D", "is_correct": False, "text": "Na+/K+ ATPase alpha-2 subunit"},
            {"letter": "E", "is_correct": False, "text": "Inwardly rectifying potassium channel (Kir2.1)"}
        ],
        "explanation": "Correct Answer: A. P/Q-type voltage-gated calcium channel (Cav2.1).\n\nFamilial Hemiplegic Migraine (FHM) genetics:\n• FHM1 (~50% of cases): Mutations in CACNA1A encoding the pore-forming alpha-1A subunit of neuronal P/Q-type voltage-gated Ca2+ channels (Cav2.1). (Also causes episodic ataxia type 2 and spinocerebellar ataxia type 6).\n• FHM2: Mutations in ATP1A2 encoding the alpha-2 subunit of Na+/K+ ATPase.\n• FHM3: Mutations in SCN1A encoding the voltage-gated Na+ channel Nav1.1.\nThese channelopathies increase cortical glutamate release, lowering the threshold for cortical spreading depression."
    },
    {
        "q_num": "HA-17",
        "category": "Headache",
        "stem": "Which of the following classes of acute migraine medications includes dihydroergotamine (DHE) and ergotamine tartrate, which act as non-selective agonists at multiple 5-HT, dopamine, and alpha-adrenergic receptors, and are strictly contraindicated in pregnant patients due to their potent oxytocic uterine-stimulating properties?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Triptans"},
            {"letter": "B", "is_correct": True, "text": "Ergot alkaloids"},
            {"letter": "C", "is_correct": False, "text": "Gepants"},
            {"letter": "D", "is_correct": False, "text": "Ditans"},
            {"letter": "E", "is_correct": False, "text": "NSAIDs"}
        ],
        "explanation": "Correct Answer: B. Ergot alkaloids.\n\nErgot alkaloids (ergotamine, dihydroergotamine / DHE) are derived from the fungus Claviceps purpurea:\n• Broad pharmacology: Non-selective agonists at 5-HT1, 5-HT2, alpha-1, alpha-2, and dopamine receptors, producing prolonged vasoconstriction.\n• Adverse effects: Nausea (dopaminergic CTZ stimulation), coronary vasospasm, and peripheral gangrene ('ergotism' / St. Anthony's fire).\n• Contraindication: Pregnancy (causes uterine smooth muscle contraction and fetal abortion) and uncontrolled hypertension / vascular disease."
    },
    {
        "q_num": "HA-18",
        "category": "Headache",
        "stem": "A 32-year-old woman presents to the emergency department with a severe migraine attack lasting 4 days that has failed oral sumatriptan and ketorolac (status migrainosus). In addition to IV fluids and IV ketorolac, which IV antiemetic dopamine D2 antagonist is commonly administered to provide both antiemetic and acute abortive analgesic relief?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Ondansetron"},
            {"letter": "B", "is_correct": True, "text": "Metoclopramide (or Prochlorperazine)"},
            {"letter": "C", "is_correct": False, "text": "Aprepitant"},
            {"letter": "D", "is_correct": False, "text": "Scopolamine"},
            {"letter": "E", "is_correct": False, "text": "Diphenhydramine alone"}
        ],
        "explanation": "Correct Answer: B. Metoclopramide (or Prochlorperazine).\n\nIn status migrainosus (migraine lasting >72 hours), IV dopamine receptor antagonists (metoclopramide, prochlorperazine, or chlorpromazine) are first-line therapies in the emergency department:\n• Mechanisms: Block D2 receptors in the area postrema to relieve nausea and vomiting, and modulate central trigeminovascular processing to provide significant headache relief.\n• Co-administration: Diphenhydramine is often co-administered to prevent acute dystonic extrapyramidal reactions and akathisia."
    },
    {
        "q_num": "HA-19",
        "category": "Headache",
        "stem": "Which of the following 'red flag' headache clinical features is captured by the mnemonic SNOOP and warrants immediate emergency neuroimaging (CT or MRI) to rule out life-threatening secondary headache disorders?",
        "options": [
            {"letter": "A", "is_correct": True, "text": "Systemic symptoms (fever, weight loss), Neurologic deficits, Onset sudden (thunderclap), Older age (>50), Pattern change / Positional"},
            {"letter": "B", "is_correct": False, "text": "Stress, Nausea, Occipital location, Oral contraceptive use, Photophobia"},
            {"letter": "C", "is_correct": False, "text": "Sinus congestion, Neck stiffness only, Ocular itching, Paresthesias in fingertips"},
            {"letter": "D", "is_correct": False, "text": "Sleep deprivation, Nocturnal awakening, Ophthalmic aura, Pulsatile pain"},
            {"letter": "E", "is_correct": False, "text": "Subacute onset, Nasal discharge, Osmophobia, Pain relieved by sleep"}
        ],
        "explanation": "Correct Answer: A. Systemic symptoms (fever, weight loss), Neurologic deficits, Onset sudden (thunderclap), Older age (>50), Pattern change / Positional.\n\nThe SNOOP mnemonic for secondary headache red flags:\n• S: Systemic symptoms (fever, weight loss, HIV, cancer) or Secondary risk factors\n• N: Neurologic symptoms or abnormal signs (confusion, focal deficit, papilledema)\n• O: Onset sudden (thunderclap / maximal in seconds: rule out SAH)\n• O: Older age at onset (>50 years: rule out giant cell arteritis or mass)\n• P: Pattern change, Positional worsening (rule out intracranial hypo/hypertension), Precipitated by Valsalva/cough, or Papilledema."
    },
    {
        "q_num": "HA-20",
        "category": "Headache",
        "stem": "A 48-year-old woman presents with persistent, strictly unilateral continuous headache present for 8 months without pain-free periods (hemicrania continua). She experiences superimposed exacerbations with ipsilateral eye tearing and ptosis. Brain MRI is normal. What pharmacological challenge confirms the diagnosis of hemicrania continua?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Complete relief with high-flow oxygen"},
            {"letter": "B", "is_correct": True, "text": "Complete, dramatic relief with oral indomethacin"},
            {"letter": "C", "is_correct": False, "text": "Temporary relief with sublingual nitroglycerin"},
            {"letter": "D", "is_correct": False, "text": "Improvement following a trial of sumatriptan"},
            {"letter": "E", "is_correct": False, "text": "Worsening with oral carbamazepine"}
        ],
        "explanation": "Correct Answer: B. Complete, dramatic relief with oral indomethacin.\n\nHemicrania Continua is a primary headache disorder characterized by continuous, strictly unilateral, daily headache for >3 months with fluctuating intensity and autonomic features. By diagnostic criteria, it is universally and completely responsive to INDOMETHACIN. An 'indomethacin challenge' (indotest) confirms the diagnosis."
    }
]

if __name__ == '__main__':
    print(f'Part 3 loaded successfully with {len(part3_questions)} questions.')
