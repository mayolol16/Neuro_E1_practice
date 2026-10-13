# inhouse_section1.py
# Section 1: Neuro-Foundations
# Covers:
# - CNS Anatomy (LOs 1-6 + Content questions on gray/white matter, meninges, BBB/barriers)
# - CNS Development (LOs 1-6 + Content questions on neurulation, vesicles, migration + Cases: Chiari I/II, Tay-Sachs, Niemann-Pick, Gaucher)
# - Neurotransmission & Action Potentials (LOs 1-5 + Content questions on Na/K pump, saltatory conduction, GABA-A, NMDA, monoamines, local anesthetics, astrocyte-lactate shuttle)
# - Ventricular System & CSF (LOs 1-4 + Content questions on CSF flow, hydrocephalus types, ICP, herniation, glymphatics)

questions_section1 = [
    # ==========================================
    # CNS ANATOMY: LO 1 - Divisions of CNS & Lobes
    # ==========================================
    {
        "id": "IH_Q001",
        "question_number": 1,
        "category": "In House: CNS Anatomy",
        "stem": "A 64-year-old right-handed man is evaluated following an ischemic stroke. On neurological examination, he speaks fluently with normal prosody and grammar, but his speech is completely devoid of meaning ('word salad'). When given simple commands such as 'close your eyes' or 'point to the door,' he fails to comply. He is unaware of his deficits. A lesion in which of the following cortical lobes and gyri is most likely responsible for this patient's condition?",
        "options": [
            {"text": "Frontal lobe, inferior frontal gyrus (pars opercularis/triangularis)", "is_correct": False},
            {"text": "Temporal lobe, superior temporal gyrus (posterior aspect)", "is_correct": True},
            {"text": "Parietal lobe, inferior parietal lobule (angular gyrus)", "is_correct": False},
            {"text": "Occipital lobe, lingual gyrus", "is_correct": False},
            {"text": "Temporal lobe, parahippocampal gyrus", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. Temporal lobe, superior temporal gyrus (posterior aspect).\n\nWernicke area is situated in the posterior portion of the superior temporal gyrus in the dominant hemisphere (Brodmann area 22). Lesions here cause sensory/receptive aphasia characterized by fluent, effortless, yet nonsensical speech, severe impaired comprehension, impaired repetition, and lack of awareness of the deficit (anosognosia).\n\n• Option A is incorrect: The inferior frontal gyrus contains Broca area; lesions cause non-fluent, expressive aphasia with preserved comprehension and severe frustration.\n• Option C is incorrect: The angular gyrus in the parietal lobe is involved in Gerstmann syndrome (acalculia, agraphia, finger agnosia, right-left disorientation).\n• Option D is incorrect: The lingual gyrus in the occipital lobe processes lower visual quadrant fields.\n• Option E is incorrect: The parahippocampal gyrus surrounds the hippocampus and plays a key role in memory encoding."
    },
    {
        "id": "IH_Q002",
        "question_number": 2,
        "category": "In House: CNS Anatomy",
        "stem": "A 45-year-old construction worker is brought to the clinic by his wife, who notes drastic changes in his personality following an accident in which an iron rod pierced his anterior skull. Once polite and meticulous, he has become irritable, profane, disinhibited, and unable to plan future actions or control impulses. His motor strength, sensory testing, and language comprehension remain intact. Which of the following functional divisions of the cerebral cortex was primarily damaged?",
        "options": [
            {"text": "Dorsolateral and orbitofrontal prefrontal cortex", "is_correct": True},
            {"text": "Primary somatosensory cortex (postcentral gyrus)", "is_correct": False},
            {"text": "Primary motor cortex (precentral gyrus)", "is_correct": False},
            {"text": "Insular cortex (gustatory and visceral sensory area)", "is_correct": False},
            {"text": "Cingulate cortex (subgenual region)", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Dorsolateral and orbitofrontal prefrontal cortex.\n\nThe prefrontal cortex of the frontal lobe governs executive functions, including decision-making, working memory, emotional regulation, and social behavior. Lesions of the orbitofrontal and ventromedial prefrontal cortex (famously seen in the historical Phineas Gage injury) lead to disinhibition, emotional lability, impulsivity, and profound personality changes, whereas dorsolateral damage leads to dysexecutive syndrome (poor planning, apathy).\n\n• Option B is incorrect: The postcentral gyrus is the primary somatosensory cortex (tactile, pain, proprioception).\n• Option C is incorrect: The precentral gyrus is the primary motor cortex; damage causes contralateral weakness/hemiparesis.\n• Option D is incorrect: The insula processes visceral sensation, autonomic regulation, and taste.\n• Option E is incorrect: The anterior/subgenual cingulate is involved in mood regulation and depression."
    },
    {
        "id": "IH_Q003",
        "question_number": 3,
        "category": "In House: CNS Anatomy",
        "stem": "A 52-year-old woman presents with difficulty recognizing familiar objects placed in her left visual field. Neurological evaluation reveals a left homonymous hemianopia with macular sparing. Further testing confirms intact visual acuity in the central field. The lesion is localized to the primary visual cortex (Brodmann area 17) along the calcarine sulcus. Why is the macula typically spared in ischemic infarctions of the primary visual cortex caused by posterior cerebral artery (PCA) occlusion?",
        "options": [
            {"text": "The macular representation is exclusively located in the optic chiasm", "is_correct": False},
            {"text": "The occipital pole receiving macular projections has dual blood supply from the PCA and middle cerebral artery (MCA)", "is_correct": True},
            {"text": "Macular fibers bypass the lateral geniculate nucleus and project directly to the parietal cortex", "is_correct": False},
            {"text": "The macular fibers decussate at the anterior commissure", "is_correct": False},
            {"text": "The macular cortex receives collateral circulation from the anterior inferior cerebellar artery (AICA)", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. The occipital pole receiving macular projections has dual blood supply from the PCA and middle cerebral artery (MCA).\n\nThe primary visual cortex lines the banks of the calcarine sulcus in the occipital lobe. The macular region of the retina maps to the posterior-most occipital pole. The occipital pole possesses a dual vascular supply from terminal cortical branches of both the posterior cerebral artery (PCA) and middle cerebral artery (MCA). Consequently, proximal PCA occlusion spares the occipital pole due to MCA collaterals, preserving central macular vision.\n\n• Option A is incorrect: The macula is represented in the retina, LGN, and visual cortex, not the chiasm.\n• Option C is incorrect: Macular fibers synapse in the lateral geniculate nucleus (layers 1-6) before projecting via optic radiations to the occipital pole.\n• Option D is incorrect: Retinal nasal fibers decussate at the optic chiasm, not the anterior commissure.\n• Option E is incorrect: AICA supplies the lateral pons and anterior inferior cerebellum, not the occipital lobe."
    },
    {
        "id": "IH_Q004",
        "question_number": 4,
        "category": "In House: CNS Anatomy",
        "stem": "A 70-year-old man presents with progressive memory loss and visual hallucinations. During a gross neuroanatomy demonstration comparing coronal brain sections, the instructor asks students to contrast the internal organization of gray and white matter in the cerebral hemispheres versus the spinal cord. Which of the following statements correctly distinguishes this anatomical organization?",
        "options": [
            {"text": "The cerebral hemispheres feature an outer white matter cortex and central gray matter, whereas the spinal cord features outer gray matter", "is_correct": False},
            {"text": "The cerebral hemispheres have peripheral gray matter cortex with internal white matter and deep gray nuclei, whereas the spinal cord has internal 'H-shaped' gray matter surrounded by peripheral white matter tracts", "is_correct": True},
            {"text": "Both the cerebral hemispheres and the spinal cord feature alternating concentric rings of gray and white matter", "is_correct": False},
            {"text": "The cerebral cortex is composed purely of myelinated axons, whereas the spinal cord dorsal horn is purely white matter", "is_correct": False},
            {"text": "The spinal cord possesses deep subcortical nuclei surrounded completely by the pia mater without superficial white matter", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. The cerebral hemispheres have peripheral gray matter cortex with internal white matter and deep gray nuclei, whereas the spinal cord has internal 'H-shaped' gray matter surrounded by peripheral white matter tracts.\n\nIn the cerebral and cerebellar hemispheres, neuronal cell bodies, dendrites, and synapses are concentrated peripherally in the cortex (outer gray matter), beneath which lie subcortical myelinated projection, association, and commissural white matter tracts, along with deep gray nuclei (e.g., basal ganglia, thalamus). In sharp contrast, the spinal cord is arranged with a central 'butterfly' or 'H-shaped' gray matter core (containing neuronal cell bodies) encircled by peripheral ascending and descending white matter funiculi/columns.\n\n• Option A is incorrect: It reverses the actual cerebral and spinal cord anatomy.\n• Option C is incorrect: Brain and spinal cord do not feature concentric alternating rings.\n• Option D is incorrect: The cerebral cortex consists of gray matter (neuronal somas and neuropil), not pure myelinated axons.\n• Option E is incorrect: The spinal cord white matter funiculi are superficial, immediately beneath the pia mater."
    },
    {
        "id": "IH_Q005",
        "question_number": 5,
        "category": "In House: CNS Anatomy",
        "stem": "During a neuroanatomy laboratory, students identify structures of the brainstem on a ventral specimen. Moving from rostral to caudal, which of the following sequences represents the correct anatomical order of the brainstem subdivisions, and which cranial nerves exit at the pontomedullary junction?",
        "options": [
            {"text": "Medulla -> Pons -> Midbrain; Cranial nerves III, IV, and VI exit at the pontomedullary junction", "is_correct": False},
            {"text": "Midbrain -> Pons -> Medulla; Cranial nerves VI, VII, and VIII exit at the pontomedullary junction", "is_correct": True},
            {"text": "Pons -> Midbrain -> Medulla; Cranial nerves V, VI, and VII exit at the pontomedullary junction", "is_correct": False},
            {"text": "Midbrain -> Medulla -> Pons; Cranial nerves IX, X, and XI exit at the pontomedullary junction", "is_correct": False},
            {"text": "Medulla -> Midbrain -> Pons; Cranial nerves I and II exit at the pontomedullary junction", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. Midbrain -> Pons -> Medulla; Cranial nerves VI, VII, and VIII exit at the pontomedullary junction.\n\nRostral to caudal, the brainstem consists of the midbrain (mesencephalon), pons (metencephalon), and medulla oblongata (myelencephalon). At the ventral groove between the pons and medulla (pontomedullary junction), cranial nerves VI (abducens, medially), VII (facial, intermediate), and VIII (vestibulocochlear, laterally at the cerebellopontine angle) emerge.\n\n• Option A is incorrect: Medulla is the most caudal, not rostral; CN III exits the interpeduncular fossa of the midbrain, and CN IV exits the dorsal midbrain.\n• Option C is incorrect: Pons is inferior to the midbrain; CN V emerges from the mid-lateral surface of the pons.\n• Option D is incorrect: Cranial nerves IX, X, and XI exit from the post-olivary sulcus of the medulla.\n• Option E is incorrect: CN I and CN II attach directly to the forebrain (telencephalon and diencephalon), not the brainstem."
    },
    {
        "id": "IH_Q006",
        "question_number": 6,
        "category": "In House: CNS Anatomy",
        "stem": "A 31-year-old cyclist is struck by a vehicle. He arrives unconscious with an acute right pupillary dilation and sluggish light reflex. Non-contrast head CT reveals a biconvex (lenticular) hyperdense extra-axial collection that does not cross cranial sutures. A tear of the middle meningeal artery is confirmed. In which of the following anatomical spaces has this hemorrhage accumulated?",
        "options": [
            {"text": "Epidural space (between inner skull table and periosteal dura mater)", "is_correct": True},
            {"text": "Subdural space (between meningeal dura mater and arachnoid mater)", "is_correct": False},
            {"text": "Subarachnoid space (between arachnoid mater and pia mater)", "is_correct": False},
            {"text": "Subpial space (between pia mater and glia limitans)", "is_correct": False},
            {"text": "Virchow-Robin perivascular space", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Epidural space (between inner skull table and periosteal dura mater).\n\nAn epidural hematoma occurs in the potential space between the inner table of the calvarium and the outer periosteal layer of the dura mater, most commonly due to fracture at the pterion rupturing the middle meningeal artery. Because the periosteal dura is firmly adherent to the cranial sutures, an epidural hematoma cannot cross sutures, creating a characteristic biconvex (lens-shaped) hyperdensity on head CT.\n\n• Option B is incorrect: Subdural hematomas occur between the dura and arachnoid from tearing of bridging veins; they cross suture lines and present as crescent-shaped collections.\n• Option C is incorrect: Subarachnoid hemorrhage occurs between the arachnoid and pia, filling the sulci, basal cisterns, and CSF spaces, typically from ruptured berry aneurysms.\n• Option D is incorrect: There is no distinct anatomical subpial compartment; the pia adheres intimately to the glia limitans.\n• Option E is incorrect: Virchow-Robin spaces are microscopic pial invaginations surrounding penetrating cerebral vessels."
    },
    {
        "id": "IH_Q007",
        "question_number": 7,
        "category": "In House: CNS Anatomy",
        "stem": "A researcher is studying the histological composition of brain tissue. In a biopsy sample from the subcortical white matter, which of the following cellular components is expected to be present in high abundance?",
        "options": [
            {"text": "Neuronal perikarya (cell bodies) and dendritic arborizations", "is_correct": False},
            {"text": "Myelinated axons and oligodendrocytes", "is_correct": True},
            {"text": "High concentrations of chemical synapses and neurotransmitter vesicles", "is_correct": False},
            {"text": "Choroid plexus epithelial cells and ependymal cilia", "is_correct": False},
            {"text": "Spinal motor neuron nuclei and Nissl substance", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. Myelinated axons and oligodendrocytes.\n\nWhite matter in the CNS consists predominantly of bundles of myelinated (and some unmyelinated) axons traveling as projection, association, or commissural tracts, enveloped by oligodendrocytes (which provide myelin sheaths), along with fibrous astrocytes and microglia. Neuronal cell bodies (perikarya), dendrites, and the overwhelming majority of synaptic connections are located exclusively within gray matter (cortex and deep nuclei).\n\n• Option A is incorrect: Neuronal cell bodies and dendrites are found in gray matter.\n• Option C is incorrect: Synapses and neuropil are localized to gray matter.\n• Option D is incorrect: Choroid plexus and ependymal cells line the ventricular cavities.\n• Option E is incorrect: Nissl bodies (rough endoplasmic reticulum) are found in neuronal cell bodies in gray matter."
    },
    {
        "id": "IH_Q008",
        "question_number": 8,
        "category": "In House: CNS Anatomy",
        "stem": "A medical student is examining the cellular architecture of the blood-brain barrier (BBB). She notes that lipophobic therapeutic agents are prevented from entering the cerebral parenchyma. Which of the following structures constitutes the primary physical barrier and primary determinant of selective permeability across the BBB?",
        "options": [
            {"text": "Fenestrations within the capillary endothelial wall", "is_correct": False},
            {"text": "Continuous non-fenestrated capillary endothelial cells joined by tight junctions (zonula occludens)", "is_correct": True},
            {"text": "Astrocyte end-feet forming an impermeable mechanical seal without underlying basement membrane", "is_correct": False},
            {"text": "Pia mater cell layers reflecting around penetrating arterioles", "is_correct": False},
            {"text": "Arachnoid villi filtering plasma macromolecules into venous sinuses", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. Continuous non-fenestrated capillary endothelial cells joined by tight junctions (zonula occludens).\n\nThe blood-brain barrier (BBB) is composed of: (1) continuous non-fenestrated capillary endothelial cells sealed by tight junctions (zonulae occludentes, comprising claudins, occludin, and JAMs), (2) a continuous endothelial basement membrane, (3) pericytes, and (4) astrocyte end-feet (podocytes) expressing aquaporin-4. The tight junctions between endothelial cells provide the primary physical barrier to polar solutes and macromolecules.\n\n• Option A is incorrect: Brain capillaries lack fenestrations (unlike circumventricular organs or renal glomeruli).\n• Option C is incorrect: Astrocyte foot processes induce tight junction formation and regulate flow, but do not form the tight physical barrier themselves.\n• Option D is incorrect: Pia mater does not form the tight physiological barrier.\n• Option E is incorrect: Arachnoid villi resorb CSF into the dural venous sinuses, having no role in capillary BBB permeability."
    },

    # ==========================================
    # CNS DEVELOPMENT: LOs 1-6 & In-House Content
    # ==========================================
    {
        "id": "IH_Q009",
        "question_number": 9,
        "category": "In House: CNS Development",
        "stem": "During human embryonic development, primary neurulation begins in the third week of gestation following induction by the notochord. Which embryonic germ layer differentiates to form the neural plate, and what adult central nervous system structures are derived from the resulting neural tube?",
        "options": [
            {"text": "Endoderm; gives rise to the spinal cord and dorsal root ganglia", "is_correct": False},
            {"text": "Neuroectoderm; gives rise to the brain, spinal cord, retina, and motor neurons", "is_correct": True},
            {"text": "Mesoderm; gives rise to the cerebral hemispheres and sympathetic chain", "is_correct": False},
            {"text": "Surface ectoderm; gives rise to microglia and dura mater", "is_correct": False},
            {"text": "Neural crest; gives rise to oligodendrocytes and ependyma", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. Neuroectoderm; gives rise to the brain, spinal cord, retina, and motor neurons.\n\nThe notochord secretes inductive signaling factors (such as noggin and chordin) that stimulate the overlying ectoderm to differentiate into neuroectoderm, forming the neural plate. The neural plate folds into the neural tube, which gives rise to the entire central nervous system: the brain (cerebrum, cerebellum, brainstem), spinal cord, neurohypophysis, retina, motor neurons, preganglionic autonomic neurons, oligodendrocytes, astrocytes, and ependymal cells.\n\n• Option A is incorrect: Endoderm forms GI and respiratory linings, not neural structures.\n• Option C is incorrect: Mesoderm forms bone, muscle, cardiovascular system, and microglia (derived from yolk sac mesoderm).\n• Option D is incorrect: Surface ectoderm forms the epidermis, lens of the eye, and adenohypophysis; dura mater is mesodermal.\n• Option E is incorrect: Neural crest gives rise to the PNS (Schwann cells, sensory and autonomic ganglia, adrenal chromaffin cells, melanocytes)."
    },
    {
        "id": "IH_Q010",
        "question_number": 10,
        "category": "In House: CNS Development",
        "stem": "A 2-day-old infant is found to have absent enteric ganglion cells in the distal colon (Hirschsprung disease), along with hypopigmented skin patches and sensory hearing loss. These findings are attributed to defective migration and differentiation of cells that detach from the lateral margins of the neural plate during neurulation. Which of the following cell types is also derived from this specific embryonic precursor population?",
        "options": [
            {"text": "Oligodendrocytes in the cerebral white matter", "is_correct": False},
            {"text": "Schwann cells in the peripheral nervous system", "is_correct": True},
            {"text": "Ependymal cells lining the central canal", "is_correct": False},
            {"text": "Anterior horn alpha motor neurons", "is_correct": False},
            {"text": "Microglia in the cerebral cortex", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. Schwann cells in the peripheral nervous system.\n\nNeural crest cells arise from the crests of the closing neural folds (ectoderm). They undergo epithelial-to-mesenchymal transition and migrate extensively throughout the embryo to form: (1) Schwann cells, (2) dorsal root ganglia, (3) autonomic (sympathetic and parasympathetic) ganglia, (4) enteric nervous system (Auerbach and Meissner plexuses), (5) adrenal medulla chromaffin cells, (6) melanocytes, (7) arachnoid and pia mater (leptomeninges), and (8) craniofacial cartilage/bones.\n\n• Option A is incorrect: Oligodendrocytes derive from the neural tube neuroectoderm.\n• Option C is incorrect: Ependymal cells derive from the neural tube neuroepithelium.\n• Option D is incorrect: Motor neurons derive from the basal plate of the neural tube.\n• Option E is incorrect: Microglia are mesodermal/monocyte-macrophage lineage."
    },
    {
        "id": "IH_Q011",
        "question_number": 11,
        "category": "In House: CNS Development",
        "stem": "By the fifth week of human embryonic development, the primary brain vesicles divide into five secondary brain vesicles. Which of the following secondary brain vesicles gives rise to the adult thalamus, hypothalamus, and third ventricle?",
        "options": [
            {"text": "Telencephalon", "is_correct": False},
            {"text": "Diencephalon", "is_correct": True},
            {"text": "Mesencephalon", "is_correct": False},
            {"text": "Metencephalon", "is_correct": False},
            {"text": "Myelencephalon", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. Diencephalon.\n\nThe prosencephalon (forebrain) divides into: (1) Telencephalon (forming cerebral hemispheres, basal ganglia, and lateral ventricles) and (2) Diencephalon (forming the thalamus, hypothalamus, epithalamus, subthalamus, optic vesicles/retina, and third ventricle).\n\n• Option A is incorrect: Telencephalon forms cerebral cortex and basal ganglia.\n• Option C is incorrect: Mesencephalon (midbrain) forms the tectum, tegmentum, cerebral peduncles, and cerebral aqueduct.\n• Option D is incorrect: Metencephalon (hindbrain derivative) forms the pons, cerebellum, and upper 4th ventricle.\n• Option E is incorrect: Myelencephalon forms the medulla oblongata and lower 4th ventricle."
    },
    {
        "id": "IH_Q012",
        "question_number": 12,
        "category": "In House: CNS Development",
        "stem": "During spinal cord and brainstem embryogenesis, the sulcus limitans separates the developing neural tube into the dorsal alar plate and ventral basal plate. What functional organization is established by this division, and what signaling morphogens pattern these dorsal and ventral axes?",
        "options": [
            {"text": "The alar plate becomes motor (induced by Sonic hedgehog), while the basal plate becomes sensory (induced by BMPs)", "is_correct": False},
            {"text": "The alar plate forms sensory nuclei (induced by BMP and Wnt from the roof plate), while the basal plate forms motor nuclei (induced by Sonic hedgehog from the notochord and floor plate)", "is_correct": True},
            {"text": "The alar plate forms the ventricular lining, while the basal plate forms the pia mater", "is_correct": False},
            {"text": "The alar plate forms preganglionic sympathetic fibers, while the basal plate forms primary nociceptive neurons", "is_correct": False},
            {"text": "Both plates form exclusively interneurons, whereas motor and sensory nuclei derive from the neural crest", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. The alar plate forms sensory nuclei (induced by BMP and Wnt from the roof plate), while the basal plate forms motor nuclei (induced by Sonic hedgehog from the notochord and floor plate).\n\nThe embryonic neural tube is patterned along its dorsal-ventral axis by opposing morphogen gradients: Sonic hedgehog (Shh), secreted ventrally by the notochord and floor plate, directs ventralization to form the basal plate (motor neurons/horns). Bone morphogenetic proteins (BMPs) and Wnt, secreted dorsally by the roof plate and surface ectoderm, direct dorsalization to form the alar plate (sensory neurons/dorsal horn).\n\n• Option A is incorrect: It reverses the roles; alar is sensory (dorsal) and basal is motor (ventral).\n• Option C is incorrect: Ventricular lining derives from neuroepithelium and pia from neural crest.\n• Option D is incorrect: Autonomic lateral horn neurons also derive from the basal plate (visceral motor).\n• Option E is incorrect: Basal plate forms somatic and visceral motor neurons."
    },
    {
        "id": "IH_Q013",
        "question_number": 13,
        "category": "In House: CNS Development",
        "stem": "A newborn infant is evaluated for severe developmental delay and seizures. High-resolution brain MRI reveals a completely smooth cerebral surface lacking normal sulci and gyri (lissencephaly), along with an abnormally thickened 4-layered cortex. Mutation in the LIS1 gene is identified. This pathological condition represents a failure of which of the following developmental processes?",
        "options": [
            {"text": "Primary neurulation (neural tube closure)", "is_correct": False},
            {"text": "Radial neuronal migration along radial glial fibers", "is_correct": True},
            {"text": "Synaptogenesis during the third trimester", "is_correct": False},
            {"text": "Myelination by oligodendrocytes during childhood", "is_correct": False},
            {"text": "Hemispheric separation across the midline", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. Radial neuronal migration along radial glial fibers.\n\nDuring corticogenesis, neuroblasts proliferate in the ventricular zone and migrate outward along radial glial scaffolding to form the 6-layered cerebral neocortex in an 'inside-out' pattern (earliest-born neurons occupy deep layers, later-born migrate past them to superficial layers). Defects in neuronal migration (e.g., mutations in LIS1 or DCX) cause lissencephaly (agyria/smooth brain) or pachygyria, characterized by absent gyration, intellectual disability, and intractable epilepsy.\n\n• Option A is incorrect: Neurulation defects cause neural tube defects (anencephaly, spina bifida).\n• Option C is incorrect: Synaptogenesis occurs after migration.\n• Option D is incorrect: Myelination is a late prenatal and postnatal process.\n• Option E is incorrect: Failure of hemispheric separation causes holoprosencephaly (associated with Sonic hedgehog mutations and trisomy 13)."
    },
    {
        "id": "IH_Q014",
        "question_number": 14,
        "category": "In House: CNS Development",
        "stem": "A 28-year-old woman presents with persistent occipital headaches that worsen significantly when coughing, sneezing, or lifting heavy weights. Neurological examination reveals bilateral loss of pain and temperature sensation across her shoulders and upper arms in a 'cape-like' distribution, with preserved light touch and proprioception. Sagittal T1-weighted MRI of the brain and spine reveals herniation of the cerebellar tonsils 7 mm below the foramen magnum and a fluid-filled cavity in the cervical spinal cord. There is no lumbar sacral defect. What is the most likely diagnosis?",
        "options": [
            {"text": "Chiari I malformation complicated by syringomyelia", "is_correct": True},
            {"text": "Chiari II malformation with myelomeningocele", "is_correct": False},
            {"text": "Dandy-Walker malformation with cerebellar agenesis", "is_correct": False},
            {"text": "Holoprosencephaly with fusion of the lateral ventricles", "is_correct": False},
            {"text": "Normal pressure hydrocephalus with aqueductal web", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Chiari I malformation complicated by syringomyelia.\n\nChiari I malformation is characterized by downward displacement (ectopia) of the cerebellar tonsils >5 mm below the level of the foramen magnum into the upper cervical canal. It is typically asymptomatic in childhood and presents in early adulthood with occipital headaches worsened by Valsalva maneuvers (coughing, straining). It is strongly associated with syringomyelia (fluid-filled syrinx within the spinal cord, most often cervical), which compresses the anterior white commissure and produces a bilateral 'cape-like' loss of pain and temperature sensation with preserved touch.\n\n• Option B is incorrect: Chiari II malformation involves downward herniation of both cerebellar tonsils AND the vermis/brainstem, presents at birth/infancy, and is virtually always associated with myelomeningocele and obstructive hydrocephalus.\n• Option C is incorrect: Dandy-Walker malformation features agenesis of the cerebellar vermis and cystic dilation of the 4th ventricle.\n• Option D is incorrect: Holoprosencephaly is failure of prosencephalon cleavage, presenting with cyclopia/cleft lip.\n• Option E is incorrect: NPH presents with the triad of dementia, gait disturbance, and urinary incontinence in elderly patients."
    },
    {
        "id": "IH_Q015",
        "question_number": 15,
        "category": "In House: CNS Development",
        "stem": "A pregnant woman undergoes routine second-trimester screening at 16 weeks gestation. Maternal serum alpha-fetoprotein (MSAFP) is markedly elevated. Subsequent amniocentesis demonstrates elevated amniotic fluid alpha-fetoprotein and elevated acetylcholinesterase (AChE). High-resolution ultrasound shows a cystic defect over the lumbosacral spine containing both meninges and neural tissue (spinal cord), along with downward displacement of the cerebellar vermis and tonsils into the foramen magnum. What is the primary embryological cause of this anomaly?",
        "options": [
            {"text": "Failure of the rostral (anterior) neuropore to close on embryonic day 25", "is_correct": False},
            {"text": "Failure of the caudal (posterior) neuropore to close on embryonic day 27", "is_correct": True},
            {"text": "Failure of cleavage of the forebrain during the fifth week of development", "is_correct": False},
            {"text": "Premature fusion of the sagittal and coronal cranial sutures", "is_correct": False},
            {"text": "Defective development of the foramina of Luschka and Magendie", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. Failure of the caudal (posterior) neuropore to close on embryonic day 27.\n\nFailure of the caudal (posterior) neuropore to close at approximately embryonic day 27 leads to neural tube defects of the spinal cord (spina bifida cystica: meningocele or myelomeningocele). When neural tissue is exposed to amniotic fluid, alpha-fetoprotein (AFP) and neural-specific acetylcholinesterase (AChE) leak into the amniotic fluid and maternal circulation. Myelomeningocele is almost universally associated with Chiari II malformation (downward displacement of the cerebellar vermis and medulla) and subsequent hydrocephalus from aqueductal stenosis.\n\n• Option A is incorrect: Failure of the rostral neuropore to close (day 25) results in anencephaly (absence of calvarium and cerebral hemispheres, leading to polyhydramnios).\n• Option C is incorrect: Failure of forebrain cleavage produces holoprosencephaly.\n• Option D is incorrect: Premature suture fusion produces craniosynostosis.\n• Option E is incorrect: Atresia of the foramina of Luschka and Magendie is characteristic of Dandy-Walker malformation."
    },
    {
        "id": "IH_Q016",
        "question_number": 16,
        "category": "In House: CNS Development",
        "stem": "Which of the following interventions initiated prior to conception and continued throughout the first trimester reduces the incidence of neural tube defects by up to 70%?",
        "options": [
            {"text": "High-dose Vitamin A (retinol) supplementation", "is_correct": False},
            {"text": "Folic acid (Vitamin B9) supplementation (400 mcg daily for low risk, 4 mg daily for high risk)", "is_correct": True},
            {"text": "Prophylactic administration of broad-spectrum cephalosporins", "is_correct": False},
            {"text": "Routine intramuscular administration of Vitamin K", "is_correct": False},
            {"text": "Calcium and Vitamin D3 supplementation", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. Folic acid (Vitamin B9) supplementation (400 mcg daily for low risk, 4 mg daily for high risk).\n\nPericonceptional folic acid supplementation is critical for purine and thymidylate synthesis required for rapid cell proliferation during primary neurulation. Daily supplementation of 400 mcg (0.4 mg) in all women of childbearing age, or 4 mg in high-risk women (e.g., prior affected child, taking valproic acid or carbamazepine), prevents approximately 70% of neural tube defects.\n\n• Option A is incorrect: High-dose Vitamin A is highly teratogenic, causing microtia, thymic aplasia, and cardiac outflow tract defects.\n• Option C is incorrect: Antibiotics do not prevent neural tube closure defects.\n• Option D is incorrect: Vitamin K is given to newborns to prevent hemorrhagic disease of the newborn.\n• Option E is incorrect: Calcium and Vitamin D prevent neonatal hypocalcemia and rickets, but not NTDs."
    },

    # ==========================================
    # CNS DEVELOPMENT CASES: SPHINGOLIPIDOSES
    # ==========================================
    {
        "id": "IH_Q017",
        "question_number": 17,
        "category": "In House: CNS Development Cases",
        "stem": "A 6-month-old infant of Ashkenazi Jewish ancestry is brought to the clinic because he has lost the ability to sit up and roll over. On examination, he exhibits severe generalized hypotonia and an exaggerated startle response to clapping or sudden loud sounds (hyperacusis). Funduscopic examination reveals a prominent cherry-red spot in the center of the macula bilaterally. Physical examination reveals no hepatosplenomegaly or abdominal distension. Which of the following enzyme deficiencies and accumulating substrates are responsible for this infant's presentation?",
        "options": [
            {"text": "Deficiency of Hexosaminidase A with accumulation of GM2 ganglioside", "is_correct": True},
            {"text": "Deficiency of Sphingomyelinase with accumulation of sphingomyelin", "is_correct": False},
            {"text": "Deficiency of Glucocerebrosidase with accumulation of glucocerebroside", "is_correct": False},
            {"text": "Deficiency of Galactocerebrosidase with accumulation of galactosylceramide", "is_correct": False},
            {"text": "Deficiency of Arylsulfatase A with accumulation of sulfatides", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Deficiency of Hexosaminidase A with accumulation of GM2 ganglioside.\n\nTay-Sachs disease is an autosomal recessive lysosomal storage disease caused by a deficiency in β-hexosaminidase A, leading to the accumulation of GM2 ganglioside in neuronal lysosomes (revealing 'onion skin' lysosomal inclusions on electron microscopy). Classic features include: neurodevelopmental regression, hypotonia, hyperacusis (exaggerated acoustic startle response), and a macular cherry-red spot. Critically, Tay-Sachs disease exhibits NO hepatosplenomegaly, which definitively differentiates it from Niemann-Pick disease.\n\n• Option B is incorrect: Sphingomyelinase deficiency causes Niemann-Pick disease, which presents with a cherry-red spot AND hepatosplenomegaly, along with lipid-laden foam cells.\n• Option C is incorrect: Glucocerebrosidase deficiency causes Gaucher disease, presenting with bone crises, hepatosplenomegaly, and 'wrinkled tissue paper' macrophages, without a cherry-red spot.\n• Option D is incorrect: Galactocerebrosidase deficiency causes Krabbe disease (globoid cells, optic atrophy, peripheral neuropathy).\n• Option E is incorrect: Arylsulfatase A deficiency causes metachromatic leukodystrophy (demyelination with ataxia and dementia)."
    },
    {
        "id": "IH_Q018",
        "question_number": 18,
        "category": "In House: CNS Development Cases",
        "stem": "A 7-month-old girl of Ashkenazi Jewish descent is evaluated for loss of developmental milestones, progressive weakness, and difficulty feeding. Abdominal examination reveals massive hepatosplenomegaly. Funduscopy demonstrates a bilateral macular cherry-red spot. Bone marrow aspirate reveals numerous lipid-laden histiocytes with a foamy, vacuolated appearance ('foam cells'). Which of the following modes of inheritance and underlying enzyme defects characterizes this disorder?",
        "options": [
            {"text": "Autosomal recessive; Sphingomyelinase deficiency", "is_correct": True},
            {"text": "X-linked recessive; Alpha-galactosidase A deficiency", "is_correct": False},
            {"text": "Autosomal recessive; Hexosaminidase A deficiency", "is_correct": False},
            {"text": "Autosomal dominant; Iduronate sulfatase deficiency", "is_correct": False},
            {"text": "Autosomal recessive; Beta-galactocerebrosidase deficiency", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Autosomal recessive; Sphingomyelinase deficiency.\n\nNiemann-Pick disease (Type A) is an autosomal recessive sphingolipidosis caused by a deficiency of acid sphingomyelinase, resulting in toxic accumulation of sphingomyelin within lysosomes of the reticuloendothelial system and CNS. Hallmarks include early neurodegeneration, hypotonia, a macular cherry-red spot, massive hepatosplenomegaly, and lipid-laden 'foam cells' on tissue biopsy.\n\n• Option B is incorrect: Alpha-galactosidase A deficiency causes Fabry disease (X-linked recessive; angiokeratomas, peripheral neuropathy, renal/cardiac failure).\n• Option C is incorrect: Hexosaminidase A deficiency causes Tay-Sachs disease, which lacks hepatosplenomegaly.\n• Option D is incorrect: Iduronate sulfatase deficiency causes Hunter syndrome (mucopolysaccharidosis II, X-linked recessive).\n• Option E is incorrect: Beta-galactocerebrosidase deficiency causes Krabbe disease."
    },
    {
        "id": "IH_Q019",
        "question_number": 19,
        "category": "In House: CNS Development Cases",
        "stem": "A 6-year-old Ashkenazi Jewish boy presents with severe bone pain in his right thigh ('bone crisis') and fatigue. Physical examination reveals massive splenomegaly and mild hepatomegaly without jaundice. Complete blood count shows hemoglobin 8.5 g/dL and platelet count 65,000/mm³. Radiographs of the distal femurs reveal flaring of the metaphysis resembling an Erlenmeyer flask. Bone marrow biopsy reveals lipid-engorged macrophages with fibrillary, wrinkled appearance resembling 'wrinkled tissue paper.' Which of the following is the deficient enzyme in this patient?",
        "options": [
            {"text": "Beta-glucocerebrosidase (acid beta-glucosidase)", "is_correct": True},
            {"text": "Sphingomyelinase", "is_correct": False},
            {"text": "Hexosaminidase A", "is_correct": False},
            {"text": "Alpha-L-iduronidase", "is_correct": False},
            {"text": "Ceramidase", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Beta-glucocerebrosidase (acid beta-glucosidase).\n\nGaucher disease is the most common lysosomal storage disorder, inherited in an autosomal recessive pattern due to deficiency of β-glucocerebrosidase (acid β-glucosidase), causing accumulation of glucocerebroside. It presents with hepatosplenomegaly, pancytopenia (anemia, thrombocytopenia due to hypersplenism and marrow infiltration), and skeletal manifestations (avascular necrosis of the femoral head, bone crises, osteopenia, and the pathognomonic 'Erlenmeyer flask' deformity of distal femurs). Bone marrow biopsy shows classic Gaucher cells (lipid-laden macrophages with a 'wrinkled tissue paper' or 'crumpled silk' cytoplasm).\n\n• Option B is incorrect: Sphingomyelinase deficiency causes Niemann-Pick disease (foam cells, cherry-red spot).\n• Option C is incorrect: Hexosaminidase A deficiency causes Tay-Sachs disease (cherry-red spot, no hepatosplenomegaly).\n• Option D is incorrect: Alpha-L-iduronidase deficiency causes Hurler syndrome (MPS I; coarse facial features, corneal clouding).\n• Option E is incorrect: Ceramidase deficiency causes Farber disease (painful joint deformity, subcutaneous nodules, hoarseness)."
    },

    # ==========================================
    # NEUROTRANSMISSION & ACTION POTENTIALS: LOs 1-5 & In-House Content
    # ==========================================
    {
        "id": "IH_Q020",
        "question_number": 20,
        "category": "In House: Neurotransmission",
        "stem": "During an action potential in a large myelinated motor axon, rapid depolarization from resting membrane potential (-70 mV) to +30 mV is driven by a surge in ionic conductance. Which of the following molecular events is directly responsible for this depolarizing upstroke?",
        "options": [
            {"text": "Opening of voltage-gated Na+ channels and rapid Na+ influx into the axon", "is_correct": True},
            {"text": "Opening of voltage-gated K+ channels and rapid K+ influx into the axon", "is_correct": False},
            {"text": "Opening of voltage-gated Ca2+ channels and rapid Ca2+ efflux from the axon", "is_correct": False},
            {"text": "Inactivation of the electrogenic Na+/K+-ATPase pump", "is_correct": False},
            {"text": "Opening of ligand-gated Cl- channels and rapid Cl- efflux", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Opening of voltage-gated Na+ channels and rapid Na+ influx into the axon.\n\nWhen a neuronal membrane is depolarized to its threshold potential (~ -55 mV), voltage-gated Na+ channels rapidly open (m-gates activate), causing a tremendous increase in Na+ permeability (gNa). Driven by both chemical and electrical gradients, Na+ rushes into the intracellular compartment, driving the membrane potential toward the Na+ equilibrium potential (+60 mV), peaking at roughly +30 to +40 mV.\n\n• Option B is incorrect: Delayed rectifier voltage-gated K+ channels open slowly and mediate K+ efflux, causing repolarization, not depolarization.\n• Option C is incorrect: Voltage-gated Ca2+ channels open at presynaptic nerve terminals to mediate vesicle fusion; they do not mediate the axonal upstroke.\n• Option D is incorrect: The Na+/K+-ATPase maintains baseline resting concentration gradients, but does not drive acute action potential phases.\n• Option E is incorrect: Cl- influx causes hyperpolarization (IPSPs)."
    },
    {
        "id": "IH_Q021",
        "question_number": 21,
        "category": "In House: Neurotransmission",
        "stem": "What molecular mechanism is responsible for the absolute refractory period of a neuron, preventing the initiation of a second action potential regardless of the strength of a depolarizing stimulus?",
        "options": [
            {"text": "Inactivation of voltage-gated Na+ channels (closure of the h-inactivation gate)", "is_correct": True},
            {"text": "Complete dephosphorylation of the Na+/K+-ATPase pump", "is_correct": False},
            {"text": "Persistent opening of inward-rectifying Ca2+ channels", "is_correct": False},
            {"text": "Slow activation of ligand-gated nicotinic acetylcholine receptors", "is_correct": False},
            {"text": "Exhaustion of intracellular ATP stores in the axon", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Inactivation of voltage-gated Na+ channels (closure of the h-inactivation gate).\n\nThe absolute refractory period occurs immediately after the action potential upstroke and lasts through early repolarization. During this phase, voltage-gated Na+ channels undergo time-dependent inactivation via closure of their intracellular inactivation gate (h-gate / 'ball-and-chain'). While inactivated, these channels cannot be reopened by any depolarizing voltage. Only when the membrane repolarizes to near resting potential do the h-gates reopen (and m-gates close), transitioning the channels back to the resting (activatable) state.\n\n• Option B is incorrect: The Na+/K+-ATPase does not set the refractory period.\n• Option C is incorrect: Persistent K+ conductance mediates the relative refractory period (where an action potential can be triggered, but requires a suprathreshold stimulus), not Ca2+ channels.\n• Option D is incorrect: Nicotinic receptors are at synapses, not responsible for axonal action potential refractoriness.\n• Option E is incorrect: Action potentials consume minimal ATP per single impulse."
    },
    {
        "id": "IH_Q022",
        "question_number": 22,
        "category": "In House: Neurotransmission",
        "stem": "In myelinated axons, action potentials propagate substantially faster than in unmyelinated axons of the same caliber. What physiological principle explains this increased conduction velocity?",
        "options": [
            {"text": "Decreased membrane electrical resistance along the internodal axolemma", "is_correct": False},
            {"text": "Saltatory conduction due to increased membrane resistance, decreased membrane capacitance, and clustering of voltage-gated Na+ channels at the nodes of Ranvier", "is_correct": True},
            {"text": "Continuous uniform distribution of Na+ channels along every micrometer of the axolemma", "is_correct": False},
            {"text": "Increased inward leak of chloride ions across the myelin sheath", "is_correct": False},
            {"text": "Active ATP-dependent transport of sodium along the internodal myelin layers", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. Saltatory conduction due to increased membrane resistance, decreased membrane capacitance, and clustering of voltage-gated Na+ channels at the nodes of Ranvier.\n\nMyelin, formed by oligodendrocytes (CNS) or Schwann cells (PNS), wraps axons in multiple concentric lipid bilayers. This increases membrane resistance (preventing ion leakage across internodes) and decreases membrane capacitance (allowing rapid passive electrotonic spread of current between nodes). High densities of voltage-gated Na+ channels and Na+/K+ pumps are clustered at the unmyelinated nodes of Ranvier, causing the action potential to 'jump' from node to node (saltatory conduction), dramatically speeding conduction velocity.\n\n• Option A is incorrect: Myelin increases membrane resistance (Rm) and increases the length constant (λ).\n• Option C is incorrect: Unmyelinated axons feature continuous distribution of channels, resulting in slow continuous conduction.\n• Option D is incorrect: Myelin prevents ion leakage; chloride leak would inhibit conduction.\n• Option E is incorrect: Current travels passively (electrotonically) beneath myelin, not via ATP pumps."
    },
    {
        "id": "IH_Q023",
        "question_number": 23,
        "category": "In House: Neurotransmission",
        "stem": "A neuroscientist applies an experimental toxin to hippocampal slice preparations. The toxin selectively binds to synaptotagmin and prevents its interaction with intracellular calcium ions in the presynaptic terminal. Which of the following steps of synaptic transmission will be directly inhibited?",
        "options": [
            {"text": "Depolarization of the presynaptic terminal by the action potential", "is_correct": False},
            {"text": "Opening of presynaptic P/Q- and N-type voltage-gated Ca2+ channels", "is_correct": False},
            {"text": "Ca2+-triggered fusion of docked synaptic vesicles with the presynaptic plasma membrane and neurotransmitter exocytosis", "is_correct": True},
            {"text": "Synthesis of neurotransmitters from amino acid precursors", "is_correct": False},
            {"text": "Astrocytic reuptake of glutamate from the synaptic cleft", "is_correct": False}
        ],
        "explanation": "Correct Answer: C. Ca2+-triggered fusion of docked synaptic vesicles with the presynaptic plasma membrane and neurotransmitter exocytosis.\n\nWhen an action potential reaches the presynaptic bouton, voltage-gated Ca2+ channels open, allowing Ca2+ influx. Synaptotagmin, a calcium-sensing protein embedded in synaptic vesicle membranes, binds Ca2+ and acts as the trigger for the SNARE complex (syntaxin, SNAP-25, and synaptobrevin) to complete full membrane fusion and exocytosis of neurotransmitter into the synaptic cleft. Blocking synaptotagmin's Ca2+ binding halts neurotransmitter release despite normal terminal depolarization and Ca2+ entry.\n\n• Option A is incorrect: Terminal depolarization is mediated by voltage-gated Na+ and K+ channels.\n• Option B is incorrect: Opening of Ca2+ channels occurs upstream of synaptotagmin activation.\n• Option D is incorrect: Neurotransmitter synthesis occurs enzymatically in the soma or terminal.\n• Option E is incorrect: Astrocytic glutamate uptake via EAAT occurs downstream following release."
    },
    {
        "id": "IH_Q024",
        "question_number": 24,
        "category": "In House: Neurotransmission",
        "stem": "During an acute ischemic stroke, energy failure leads to loss of the Na+/K+-ATPase gradient, depolarizing presynaptic terminals and causing excessive, uncontrolled release of glutamate into the extracellular space. Prolonged activation of which of the following postsynaptic receptors leads to massive calcium influx, activation of calpains/phospholipases, and subsequent neuronal excitotoxic death?",
        "options": [
            {"text": "GABA-A receptor", "is_correct": False},
            {"text": "NMDA (N-methyl-D-aspartate) receptor", "is_correct": True},
            {"text": "Glycine receptor", "is_correct": False},
            {"text": "Muscarinic M2 receptor", "is_correct": False},
            {"text": "Dopamine D2 receptor", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. NMDA (N-methyl-D-aspartate) receptor.\n\nNMDA receptors are ionotropic glutamate receptors permeable to Ca2+, Na+, and K+. At resting potential, their ion pore is blocked by an extracellular magnesium ion (Mg2+ block). Membrane depolarization (via AMPA receptor activation) relieves the Mg2+ block, allowing glutamate (and co-agonist glycine) to open the channel. In ischemia, continuous depolarizing release of glutamate causes persistent, unrestrained Ca2+ influx via NMDA receptors, activating intracellular proteases (calpains), endonucleases, and nitric oxide synthase, leading to excitotoxic necrosis and apoptosis.\n\n• Option A is incorrect: GABA-A receptors are inhibitory Cl- channels that protect against excitotoxicity.\n• Option C is incorrect: Glycine receptors are inhibitory strychnine-sensitive Cl- channels in the spinal cord and brainstem.\n• Option D is incorrect: M2 receptors are Gi-coupled inhibitory GPCRs in the heart and brain.\n• Option E is incorrect: D2 receptors are Gi-coupled inhibitory dopamine receptors."
    },
    {
        "id": "IH_Q025",
        "question_number": 25,
        "category": "In House: Neurotransmission",
        "stem": "A 35-year-old woman with generalized anxiety disorder is prescribed diazepam for acute symptom relief. Diazepam binds allosterically to the GABA-A receptor complex. What is the electrophysiological consequence of diazepam binding on GABA-A receptor function?",
        "options": [
            {"text": "It directly opens the channel in the complete absence of GABA", "is_correct": False},
            {"text": "It increases the frequency of chloride channel opening in the presence of GABA, leading to membrane hyperpolarization (IPSPs)", "is_correct": True},
            {"text": "It increases the duration of chloride channel opening, identical to the mechanism of barbiturates", "is_correct": False},
            {"text": "It blocks potassium efflux, prolonging action potential duration", "is_correct": False},
            {"text": "It acts as a competitive antagonist at the orthosteric GABA binding site", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. It increases the frequency of chloride channel opening in the presence of GABA, leading to membrane hyperpolarization (IPSPs).\n\nThe GABA-A receptor is an ionotropic pentameric ligand-gated chloride channel. Benzodiazepines (e.g., diazepam) bind to an allosteric regulatory site between the α and γ subunits, increasing the FREQUENCY of channel opening in response to GABA. This enhances Cl- influx, hyperpolarizing the postsynaptic neuron away from firing threshold (inhibitory postsynaptic potential, IPSP). Remember: 'Frenzodiazepines' increase Frequency; 'BarbiDURATes' increase Duration.\n\n• Option A is incorrect: Benzodiazepines require the presence of endogenous GABA to exert their effect; they do not open the channel alone at therapeutic doses.\n• Option C is incorrect: Increasing channel duration is the mechanism of barbiturates (e.g., phenobarbital), which can also open the channel directly at high doses.\n• Option D is incorrect: GABA-A is a chloride channel, not a potassium channel.\n• Option E is incorrect: Flumazenil is a competitive antagonist at the benzodiazepine site; diazepam is a positive allosteric modulator."
    },
    {
        "id": "IH_Q026",
        "question_number": 26,
        "category": "In House: Neurotransmission",
        "stem": "A 28-year-old medical student is studying metabolic coupling between astrocytes and neurons. Under physiological conditions, astrocytes clear excess glutamate from the synaptic cleft and supply fuel to active neurons. According to the astrocyte-neuron lactate shuttle hypothesis emphasized in course lectures, what metabolite is produced by astrocytic glycolysis and transported into neurons via monocarboxylate transporters (MCTs) to fuel oxidative phosphorylation in neurons?",
        "options": [
            {"text": "Ketone bodies (beta-hydroxybutyrate)", "is_correct": False},
            {"text": "L-Lactate", "is_correct": True},
            {"text": "Free fatty acids (palmitate)", "is_correct": False},
            {"text": "Glycogen granules", "is_correct": False},
            {"text": "Glutamine synthetase", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. L-Lactate.\n\nAstrocytes possess high rates of glycolysis and store the brain's glycogen. When neurons are active, astrocytic glutamate uptake stimulates astrocytic glucose uptake and glycolysis, generating lactate. Astrocytes release lactate into the extracellular space via monocarboxylate transporters 1 and 4 (MCT1/4). Neurons then take up lactate via MCT2 and convert it to pyruvate via lactate dehydrogenase 1 (LDH-1), which enters neuronal mitochondria to fuel the TCA cycle and oxidative ATP generation. This mechanism is known as the Astrocyte-Neuron Lactate Shuttle (ANLS).\n\n• Option A is incorrect: Ketone bodies are used during prolonged fasting/starvation, but lactate is the immediate shuttle metabolite during normal activity.\n• Option C is incorrect: The brain does not utilize free fatty acids for fuel due to low beta-oxidation enzyme activity and the blood-brain barrier.\n• Option D is incorrect: Glycogen is macromolecular and strictly intracellular within astrocytes.\n• Option E is incorrect: Glutamine synthetase is an astrocytic enzyme that converts glutamate to glutamine, not an energy fuel."
    },
    {
        "id": "IH_Q027",
        "question_number": 27,
        "category": "In House: Neurotransmission & Anesthesia",
        "stem": "A 24-year-old man requires local anesthesia for excision of a sebaceous cyst on his back. The resident prepares lidocaine with epinephrine (1:100,000). What is the primary physiological rationale for co-administering epinephrine with local anesthetics, and in which anatomical locations is this combination strictly contraindicated?",
        "options": [
            {"text": "Epinephrine blocks sodium channels directly; contraindicated in the abdominal wall", "is_correct": False},
            {"text": "Epinephrine causes alpha-1 mediated local vasoconstriction, which decreases systemic absorption, prolongs the local anesthetic duration, and reduces bleeding; contraindicated in end-arterial appendages (fingers, toes, nose, penis)", "is_correct": True},
            {"text": "Epinephrine alkalinizes the solution to accelerate uncharged drug entry; contraindicated in large muscle beds", "is_correct": False},
            {"text": "Epinephrine stimulates beta-2 receptors to dilate vessels and increase regional drug clearance; contraindicated on the scalp", "is_correct": False},
            {"text": "Epinephrine prevents allergic hypersensitivity reactions to ester-type anesthetics; contraindicated in the spinal cord", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. Epinephrine causes alpha-1 mediated local vasoconstriction, which decreases systemic absorption, prolongs the local anesthetic duration, and reduces bleeding; contraindicated in end-arterial appendages (fingers, toes, nose, penis).\n\nLocal anesthetics inherently cause vasodilation (except cocaine). Co-administration of epinephrine stimulates vascular smooth muscle α1-adrenergic receptors, inducing local vasoconstriction. This: (1) slows systemic vascular absorption, (2) prolongs local anesthetic duration at the target site, (3) reduces peak systemic plasma concentrations (reducing cardiac/CNS toxicity), and (4) minimizes intraoperative bleeding. Epinephrine is contraindicated in tissues with terminal end-arterial circulations (fingers, toes, earlobes, tip of the nose, penis) due to the risk of severe ischemic necrosis.\n\n• Option A is incorrect: Epinephrine does not block Na+ channels.\n• Option C is incorrect: Sodium bicarbonate alkalinizes the solution, not epinephrine.\n• Option D is incorrect: Epinephrine causes vasoconstriction via α1, not vasodilation.\n• Option E is incorrect: Epinephrine does not prevent immune reactions to esters (which are caused by PABA metabolites)."
    },
    {
        "id": "IH_Q028",
        "question_number": 28,
        "category": "In House: Neurotransmission & Anesthesia",
        "stem": "A 40-year-old woman undergoing wrist surgery receives an excessive intravenous dose of bupivacaine during an attempted Bier block, resulting in accidental systemic entry. Within minutes, she develops perioral numbness, tinnitus, metallic taste, tonic-clonic seizures, and sudden severe ventricular arrhythmias with cardiovascular collapse. Why are aminoamide local anesthetics such as bupivacaine particularly prone to causing prolonged systemic toxicity compared to aminoester local anesthetics?",
        "options": [
            {"text": "Aminoamides are rapidly hydrolyzed by pseudocholinesterase in the bloodstream within seconds", "is_correct": False},
            {"text": "Aminoamides depend on hepatic cytochrome P450 metabolism, which is slower, and bupivacaine dissociates very slowly from cardiac sodium channels ('fast in, slow out')", "is_correct": True},
            {"text": "Aminoamides are strictly eliminated unchanged by glomerular filtration without metabolism", "is_correct": False},
            {"text": "Aminoamides cause irreversible alkylation of muscarinic acetylcholine receptors", "is_correct": False},
            {"text": "Aminoamides stimulate peripheral mast cell degranulation via IgE antibodies", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. Aminoamides depend on hepatic cytochrome P450 metabolism, which is slower, and bupivacaine dissociates very slowly from cardiac sodium channels ('fast in, slow out').\n\nLocal anesthetics fall into two classes: (1) Aminoesters (procaine, chloroprocaine, tetracaine, cocaine), which are rapidly metabolized by plasma pseudocholinesterases (butyrylcholinesterase), giving them short systemic half-lives, and (2) Aminoamides (lidocaine, bupivacaine, ropivacaine, mepivacaine — remember: amIdes have TWO 'i's in their name), which require hepatic cytochrome P450 metabolism. Bupivacaine has high lipophilicity, strong protein binding, and slow dissociation from cardiac voltage-gated Na+ channels during diastole, causing severe, refractory ventricular arrhythmias treated with intravenous 20% lipid emulsion ('lipid rescue').\n\n• Option A is incorrect: Plasma pseudocholinesterase hydrolyzes aminoesters, not aminoamides.\n• Option C is incorrect: Aminoamides are heavily metabolized in the liver, not excreted unchanged.\n• Option D is incorrect: Local anesthetics block voltage-gated Na+ channels, not muscarinic receptors.\n• Option E is incorrect: Allergic reactions are more common with aminoesters due to PABA formation."
    },
    {
        "id": "IH_Q029",
        "question_number": 29,
        "category": "In House: Neurotransmission",
        "stem": "Which of the following local anesthetics belongs to the aminoester class and is metabolized by plasma pseudocholinesterase into para-aminobenzoic acid (PABA), a compound associated with allergic hypersensitivity reactions?",
        "options": [
            {"text": "Lidocaine", "is_correct": False},
            {"text": "Bupivacaine", "is_correct": False},
            {"text": "Procaine", "is_correct": True},
            {"text": "Ropivacaine", "is_correct": False},
            {"text": "Mepivacaine", "is_correct": False}
        ],
        "explanation": "Correct Answer: C. Procaine.\n\nLocal anesthetics are divided into aminoamides and aminoesters. Mnemonic: Aminoamides contain an 'i' BEFORE the '-caine' suffix (L-i-docaine, Bup-i-vacaine, Rop-i-vacaine, Mep-i-vacaine, Pr-i-locaine). Aminoesters have only ONE 'i' in the '-caine' suffix (Procaine, Chloroprocaine, Tetracaine, Cocaine, Benzocaine). Aminoesters are hydrolyzed by plasma cholinesterases into para-aminobenzoic acid (PABA), which can cause IgE-mediated allergic reactions.\n\n• Options A, B, D, and E are all aminoamides (they have two 'i's in their name) and undergo hepatic metabolism without forming PABA."
    },
    {
        "id": "IH_Q030",
        "question_number": 30,
        "category": "In House: Neurotransmission",
        "stem": "When a peripheral nerve trunk (such as the sciatic or median nerve) is exposed to a local anesthetic, which sensory and motor modalities are typically blocked first versus last, and what anatomical/physiological properties account for this differential block?",
        "options": [
            {"text": "Motor function and vibration are blocked first because large A-alpha fibers have the lowest surface area", "is_correct": False},
            {"text": "Pain, temperature, and autonomic fibers (small B, C, and A-delta fibers) are blocked first, while motor function and proprioception (large A-alpha and A-beta fibers) are blocked last", "is_correct": True},
            {"text": "All fiber modalities are blocked simultaneously at identical concentrations", "is_correct": False},
            {"text": "Proprioception and touch are blocked first because they lack myelin", "is_correct": False},
            {"text": "Motor fibers are blocked first because they are situated in the center of the nerve trunk", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. Pain, temperature, and autonomic fibers (small B, C, and A-delta fibers) are blocked first, while motor function and proprioception (large A-alpha and A-beta fibers) are blocked last.\n\nSensitivity to local anesthetics depends on fiber diameter, myelination, and firing frequency. Smaller-diameter fibers have shorter internodal distances, so a given concentration of local anesthetic can easily bathe at least 2–3 consecutive nodes of Ranvier (the requirement for blocking saltatory conduction). Furthermore, highly active, rapidly firing nociceptive fibers exhibit state-dependent block. Hence, the typical sequence of sensory loss is: Pain -> Temperature -> Touch -> Pressure -> Motor function.\n\n• Option A is incorrect: Large myelinated motor fibers (A-alpha) are the most resistant to local anesthetic blockade.\n• Option C is incorrect: There is a distinct hierarchy of differential nerve block.\n• Option D is incorrect: Proprioceptive and touch fibers are heavily myelinated A-alpha and A-beta fibers.\n• Option E is incorrect: Mantle (outer) fibers are blocked before core (inner) fibers; furthermore, core vs mantle location relates to proximal vs distal dermatomal distribution."
    },

    # ==========================================
    # VENTRICULAR SYSTEM & CSF: LOs 1-4 & In-House Content
    # ==========================================
    {
        "id": "IH_Q031",
        "question_number": 31,
        "category": "In House: Ventricular System & CSF",
        "stem": "Cerebrospinal fluid (CSF) is actively produced by the choroid plexus and circulates through the ventricular system before entering the systemic venous circulation. Which of the following sequences represents the correct anatomical path of CSF flow starting from the lateral ventricles to the internal jugular vein?",
        "options": [
            {"text": "Lateral ventricles -> Foramen of Magendie -> 3rd ventricle -> Foramen of Monro -> 4th ventricle -> Arachnoid villi -> Internal jugular vein", "is_correct": False},
            {"text": "Lateral ventricles -> Interventricular foramen of Monro -> 3rd ventricle -> Cerebral aqueduct of Sylvius -> 4th ventricle -> Foramina of Luschka & Magendie -> Subarachnoid space -> Arachnoid granulations -> Superior sagittal sinus -> Internal jugular vein", "is_correct": True},
            {"text": "Lateral ventricles -> Cerebral aqueduct -> 4th ventricle -> 3rd ventricle -> Subarachnoid space -> Jugular foramen", "is_correct": False},
            {"text": "Lateral ventricles -> Foramina of Luschka -> 3rd ventricle -> Interventricular foramen -> 4th ventricle -> Central canal -> Internal jugular vein", "is_correct": False},
            {"text": "Lateral ventricles -> Subdural space -> 3rd ventricle -> Cerebral aqueduct -> Dural sinuses -> Internal jugular vein", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. Lateral ventricles -> Interventricular foramen of Monro -> 3rd ventricle -> Cerebral aqueduct of Sylvius -> 4th ventricle -> Foramina of Luschka & Magendie -> Subarachnoid space -> Arachnoid granulations -> Superior sagittal sinus -> Internal jugular vein.\n\nCSF is produced by choroid plexus epithelial cells in the lateral, 3rd, and 4th ventricles (approx. 500 mL/day; total circulating volume ~150 mL). The path of flow is: Lateral ventricles -> Interventricular foramina of Monro -> 3rd ventricle (in midline diencephalon) -> Cerebral aqueduct of Sylvius (in midbrain) -> 4th ventricle (between pons/medulla and cerebellum) -> Foramina of Luschka (lateral) and Magendie (median) -> Subarachnoid space -> Arachnoid granulations (villi) -> Superior sagittal sinus -> Confluence of sinuses -> Transverse sinus -> Sigmoid sinus -> Internal jugular vein.\n\n• Options A, C, and D disrupt the correct anatomical order of foramina and ventricles.\n• Option E incorrectly involves the subdural space, which is a potential space containing bridging veins, not circulating CSF."
    },
    {
        "id": "IH_Q032",
        "question_number": 32,
        "category": "In House: Ventricular System & CSF",
        "stem": "Which anatomical structure within the ventricular system has the smallest cross-sectional diameter, making it the most vulnerable site for non-communicating (obstructive) hydrocephalus caused by tumors (e.g., pinealomas) or congenital stenosis?",
        "options": [
            {"text": "Foramen of Monro", "is_correct": False},
            {"text": "Cerebral aqueduct of Sylvius", "is_correct": True},
            {"text": "Fourth ventricle", "is_correct": False},
            {"text": "Foramen of Magendie", "is_correct": False},
            {"text": "Anterior horn of the lateral ventricle", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. Cerebral aqueduct of Sylvius.\n\nThe cerebral aqueduct of Sylvius is a narrow, 1.5 cm long channel traversing the midbrain beneath the tectum (superior and inferior colliculi). Due to its extremely narrow caliber (~1-2 mm), it is the most common site of ventricular obstruction. Obstruction (via congenital aqueductal stenosis, blood clots, or compression from a pineal gland tumor) produces non-communicating obstructive hydrocephalus, causing massive dilation of both lateral ventricles and the 3rd ventricle with a normal-sized 4th ventricle.\n\n• Option A is incorrect: Foramen of Monro obstruction dilates only one lateral ventricle (if unilateral) or both (if colloid cyst of 3rd ventricle), but is less commonly stenosed than the aqueduct.\n• Option C is incorrect: The 4th ventricle is a wide rhomboid cavity.\n• Option D is incorrect: Foramen of Magendie is midline; CSF can still exit via paired lateral foramina of Luschka.\n• Option E is incorrect: Lateral ventricular horns are large cavities."
    },
    {
        "id": "IH_Q033",
        "question_number": 33,
        "category": "In House: Ventricular System & CSF",
        "stem": "A 74-year-old retired accountant is brought to the clinic by his daughter because of a 9-month history of gradual cognitive decline, urinary incontinence, and difficulty walking. His daughter notes that he walks with a wide base and drags his feet as if they are 'glued to the floor' (magnetic gait). Brain MRI shows marked symmetrical enlargement of the cerebral ventricles out of proportion to mild cortical sulcal atrophy. Lumbar puncture reveals a normal opening pressure (140 mm H2O); removal of 30 mL of CSF leads to marked improvement in his walking speed. What is the most likely diagnosis?",
        "options": [
            {"text": "Alzheimer disease (hydrocephalus ex vacuo)", "is_correct": False},
            {"text": "Normal pressure hydrocephalus (NPH)", "is_correct": True},
            {"text": "Idiopathic intracranial hypertension (pseudotumor cerebri)", "is_correct": False},
            {"text": "Aqueductal stenosis", "is_correct": False},
            {"text": "Subacute sclerosing panencephalitis", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. Normal pressure hydrocephalus (NPH).\n\nNormal pressure hydrocephalus (NPH) is a form of communicating hydrocephalus affecting the elderly, characterized by impaired CSF resorption through arachnoid granulations. It features the classic triad: (1) Gait disturbance (magnetic, wide-based, apraxic gait — 'wobbly'), (2) Urinary incontinence ('wet'), and (3) Dementia / cognitive slowing ('wacky'). Ventricular enlargement without proportional cortical atrophy stretches paraventricular sacral motor fibers of the corticospinal tract. Lumbar puncture reveals normal opening pressure, and temporary improvement following high-volume tap (Miller Fisher test) confirms diagnosis and predicts benefit from ventriculoperitoneal (VP) shunting.\n\n• Option A is incorrect: Hydrocephalus ex vacuo is secondary ventricular enlargement due to cerebral cortical atrophy (neuronal loss in Alzheimer disease), without elevated ICP or response to CSF tap.\n• Option C is incorrect: Idiopathic intracranial hypertension occurs in young obese women with headaches, papilledema, elevated opening pressure (>250 mm H2O), and normal-to-small ventricles.\n• Option D is incorrect: Aqueductal stenosis causes non-communicating hydrocephalus with elevated ICP.\n• Option E is incorrect: SSPE is a progressive measles complication in children/young adults."
    },
    {
        "id": "IH_Q034",
        "question_number": 34,
        "category": "In House: Ventricular System & CSF",
        "stem": "A 28-year-old obese woman presents with daily throbbing headaches, pulsatile tinnitus ('whooshing sound in ears'), and transient episodes of vision loss when bending over. Funduscopic examination reveals bilateral optic disc swelling with blurred margins (papilledema). Non-contrast head CT and MRI of the brain show normal-to-slit ventricles and an empty sella, without any mass lesion. Lumbar puncture reveals an elevated opening pressure of 310 mm H2O (normal <200 mm H2O) with normal CSF chemistry and cell counts. Which of the following is the first-line medical therapy to decrease CSF production in this condition?",
        "options": [
            {"text": "Acetazolamide", "is_correct": True},
            {"text": "Mannitol", "is_correct": False},
            {"text": "Dexamethasone", "is_correct": False},
            {"text": "Furosemide with hypertonic 3% saline", "is_correct": False},
            {"text": "High-dose pyridostigmine", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Acetazolamide.\n\nThis patient has Idiopathic Intracranial Hypertension (IIH, pseudotumor cerebri), which classically presents in young, overweight females of childbearing age with headaches, pulsatile tinnitus, diplopia (CN VI palsy due to long intracranial course), papilledema, and elevated opening pressure on LP. The first-line medical pharmacotherapy is acetazolamide, a carbonic anhydrase inhibitor that reduces CSF production by the choroid plexus. Weight loss is also essential.\n\n• Option B is incorrect: Mannitol is an osmotic diuretic used for acute, emergent intracranial pressure reduction (e.g., pending herniation in trauma), not chronic maintenance in IIH.\n• Option C is incorrect: Dexamethasone is used for vasogenic edema around brain tumors, not IIH.\n• Option D is incorrect: Hypertonic saline is for emergent brain edema in ICU settings.\n• Option E is incorrect: Pyridostigmine is an acetylcholinesterase inhibitor for myasthenia gravis."
    },
    {
        "id": "IH_Q035",
        "question_number": 35,
        "category": "In House: Ventricular System & CSF",
        "stem": "A 48-year-old man with a large right hemispheric glioblastoma experiences sudden neurological deterioration. His right pupil becomes widely dilated and fixed to light, he develops left hemiplegia, and his consciousness drops to a stupor. Brain CT reveals herniation of the medial temporal lobe (uncus) over the edge of the tentorium cerebelli (uncal transtentorial herniation). Compression of which cranial nerve and vascular structure produces the ipsilateral pupillary dilation and contralateral homonymous hemianopia associated with this herniation?",
        "options": [
            {"text": "Trochlear nerve (CN IV) and middle cerebral artery", "is_correct": False},
            {"text": "Oculomotor nerve (CN III) and posterior cerebral artery (PCA)", "is_correct": True},
            {"text": "Abducens nerve (CN VI) and anterior cerebral artery", "is_correct": False},
            {"text": "Trigeminal nerve (CN V) and superior cerebellar artery", "is_correct": False},
            {"text": "Optic nerve (CN II) and ophthalmic artery", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. Oculomotor nerve (CN III) and posterior cerebral artery (PCA).\n\nIn uncal (transtentorial) herniation, the uncus of the medial temporal lobe herniates inferiorly across the tentorial notch. This causes: (1) Compression of the ipsilateral oculomotor nerve (CN III), specifically the outer parasympathetic pupilloconstrictor fibers first, resulting in an 'uncal pupil' (ipsilateral dilated, fixed pupil, followed later by ptosis and 'down-and-out' gaze), (2) Compression of the ipsilateral posterior cerebral artery (PCA), resulting in ischemic infarction of the occipital cortex with contralateral homonymous hemianopia (macular sparing), (3) Compression of the ipsilateral cerebral peduncle (corticospinal tract) causing contralateral hemiparesis, or compression of the contralateral cerebral peduncle against the tentorial edge (Kernohan notch) producing ipsilateral hemiparesis (a false localizing sign), and (4) Secondary Duret hemorrhages in the midbrain and pons due to stretching of basilar perforating branches.\n\n• Option A is incorrect: CN IV does not innervate the pupillary sphincter, and MCA is not compressed at the tentorial notch.\n• Option C is incorrect: CN VI palsy causes lateral rectus weakness (inward gaze deviation), not pupillary dilation.\n• Options D and E do not match the anatomy of the tentorial incisura."
    },
    {
        "id": "IH_Q036",
        "question_number": 36,
        "category": "In House: Ventricular System & CSF",
        "stem": "A 19-year-old college student presents to the emergency department with fever, severe neck stiffness, and confusion. The resident prepares to perform an immediate diagnostic lumbar puncture. The attending physician halts the procedure and orders an immediate non-contrast head CT. Why is performing a lumbar puncture strictly contraindicated in the presence of an intracranial mass lesion or severe midline shift?",
        "options": [
            {"text": "The needle will cause immediate rupture of the anterior spinal artery", "is_correct": False},
            {"text": "Removal of CSF from the lumbar cistern creates a steep caudal pressure gradient that can precipitate fatal uncal or tonsillar herniation through the foramen magnum", "is_correct": True},
            {"text": "It will cause retrograde seeding of bacteria into the ventricles", "is_correct": False},
            {"text": "It permanently disrupts the blood-brain barrier tight junctions", "is_correct": False},
            {"text": "It induces immediate reflex hypertension and cardiac standstill (Cushing reflex reversal)", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. Removal of CSF from the lumbar cistern creates a steep caudal pressure gradient that can precipitate fatal uncal or tonsillar herniation through the foramen magnum.\n\nIn patients with space-occupying lesions (tumors, abscesses, large hematomas) or obstructive hydrocephalus with elevated ICP and midline shift, the brain tissue is under massive positive pressure. Withdrawing CSF from the lumbar thecal sac rapidly drops pressure in the lumbar and spinal compartments. This establishes a precipitous rostral-to-caudal pressure gradient, causing the cerebellar tonsils to herniate downward through the foramen magnum (tonsillar herniation), compressing the medullary respiratory and cardiac centers, causing immediate apnea, bradycardia, and death.\n\n• Option A is incorrect: A properly placed lumbar needle at L3/L4 or L4/L5 enters the lumbar cistern well below the conus medullaris (which ends at L1-L2 in adults).\n• Option C is incorrect: Lumbar puncture does not cause retrograde bacterial seeding into ventricles.\n• Option D is incorrect: LP does not disrupt cerebral endothelial tight junctions.\n• Option E is incorrect: The Cushing reflex is caused by increased ICP/medullary ischemia, not LP itself."
    },
    {
        "id": "IH_Q037",
        "question_number": 37,
        "category": "In House: Ventricular System & CSF",
        "stem": "In recent neuroscience research highlighted in medical school curriculum, what term describes the glia-mediated convective waste clearance pathway in which CSF flows through periarterial spaces, sweeps through brain parenchyma via aquaporin-4 (AQP4) water channels on astrocytic end-feet, and flushes interstitial solutes (such as amyloid-beta) into perivenous spaces, primarily active during deep sleep?",
        "options": [
            {"text": "The lymphatic-cisternal anastomosis", "is_correct": False},
            {"text": "The glymphatic system", "is_correct": True},
            {"text": "The reticuloendothelial drainage plexus", "is_correct": False},
            {"text": "The choroid ependymal filtration apparatus", "is_correct": False},
            {"text": "The Virchow-Robin thrombotic pathway", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. The glymphatic system.\n\nThe glymphatic system (glial-lymphatic system) is a brain-wide macroscopic waste clearance system. Cerebrospinal fluid (CSF) from the subarachnoid space enters periarterial Virchow-Robin spaces and is driven through the neuropil by arterial pulsations. Astrocytic end-feet expressing the water channel aquaporin-4 (AQP4) facilitate convective fluid movement from the periarterial compartment across the interstitial space toward perivenous spaces and cervical lymph nodes. This system clears metabolic waste products, including amyloid-β and tau, and is significantly more active during slow-wave sleep when interstitial space volume increases by up to 60%.\n\n• Options A, C, D, and E do not represent this established neurovascular clearance system."
    },
    {
        "id": "IH_Q038",
        "question_number": 38,
        "category": "In House: Ventricular System & CSF",
        "stem": "A 55-year-old man with a history of hypertension is found unresponsive. In the emergency department, his blood pressure is 210/110 mm Hg, heart rate is 44 beats/min, and respiratory rate is 8 breaths/min with irregular breathing patterns (Cushing triad). What is the underlying pathophysiological mechanism triggering this characteristic hemodynamic triad?",
        "options": [
            {"text": "Systemic bacteremia causing septic shock and peripheral vasodilation", "is_correct": False},
            {"text": "Massive increase in intracranial pressure causing brainstem and medullary ischemia, triggering reflex sympathetic vasoconstriction (hypertension) followed by baroreceptor-mediated parasympathetic bradycardia and respiratory center distortion", "is_correct": True},
            {"text": "Direct trauma to the vagus nerve in the carotid sheath", "is_correct": False},
            {"text": "Acute adrenal insufficiency causing aldosterone depletion", "is_correct": False},
            {"text": "Cardiogenic shock from anterior wall myocardial infarction", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. Massive increase in intracranial pressure causing brainstem and medullary ischemia, triggering reflex sympathetic vasoconstriction (hypertension) followed by baroreceptor-mediated parasympathetic bradycardia and respiratory center distortion.\n\nThe Cushing triad (hypertension, bradycardia, irregular respirations) is a life-threatening sign of dangerously elevated intracranial pressure (ICP) and impending herniation. Marked elevation in ICP compresses cerebral microvasculature, reducing cerebral perfusion pressure (CPP = MAP - ICP) and causing brainstem/medullary ischemia. In response, medullary vasomotor centers activate massive sympathetic outflow to elevate mean arterial pressure (MAP) and maintain cerebral perfusion. Carotid sinus and aortic arch baroreceptors detect this extreme hypertension and trigger reflex parasympathetic (vagal) activation, slowing heart rate (bradycardia). Compression of medullary respiratory centers results in Cheyne-Stokes or ataxic breathing.\n\n• Option A is incorrect: Septic shock causes hypotension and tachycardia.\n• Option C is incorrect: Vagus nerve trauma causes hoarseness/tachycardia, not the Cushing triad.\n• Option D is incorrect: Adrenal crisis causes hypotension and hyperkalemia.\n• Option E is incorrect: Cardiogenic shock causes hypotension and tachycardia."
    },
    {
        "id": "IH_Q039",
        "question_number": 39,
        "category": "In House: Ventricular System & CSF",
        "stem": "A 60-year-old woman is admitted to the intensive care unit with acute cerebral edema following evacuation of a subdural hematoma. Her intracranial pressure monitor registers 28 mm Hg (normal <15 mm Hg). The neurointensivist orders an intravenous bolus of 20% mannitol. What is the mechanism of action of mannitol in acutely lowering intracranial pressure?",
        "options": [
            {"text": "It enters neurons and enhances GABA-A chloride conductance", "is_correct": False},
            {"text": "It creates an osmotic gradient across an intact blood-brain barrier, drawing water from the brain parenchyma into the intravascular space", "is_correct": True},
            {"text": "It selectively blocks carbonic anhydrase in the choroid plexus epithelium", "is_correct": False},
            {"text": "It induces widespread cerebral vasodilation to increase total cerebral blood volume", "is_correct": False},
            {"text": "It increases the permeability of endothelial tight junctions to allow protein leak", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. It creates an osmotic gradient across an intact blood-brain barrier, drawing water from the brain parenchyma into the intravascular space.\n\nMannitol is a non-metabolizable, membrane-impermeant six-carbon polyol sugar. When infused intravenously, it remains confined to the vascular compartment due to the intact blood-brain barrier, significantly raising plasma osmolarity. This establishes a steep transendothelial osmotic gradient that draws free water from the intracellular and interstitial compartments of the brain parenchyma into the cerebral capillaries, reducing brain tissue volume and rapidly lowering intracranial pressure. Subsequently, it acts as an osmotic diuretic in the renal proximal tubule and descending limb of Henle, promoting water excretion.\n\n• Option A is incorrect: Mannitol does not act on GABA receptors.\n• Option C is incorrect: Acetazolamide inhibits carbonic anhydrase, not mannitol.\n• Option D is incorrect: Cerebral vasodilation would INCREASE cerebral blood volume and worsen ICP.\n• Option E is incorrect: Mannitol requires an intact BBB; leaking into brain tissue would reverse the gradient and cause rebound edema."
    },
    {
        "id": "IH_Q040",
        "question_number": 40,
        "category": "In House: Ventricular System & CSF",
        "stem": "A neuropathologist is examining brain tissue obtained at autopsy from four different patients who died with distinct forms of cerebral edema. Which type of cerebral edema is characterized by disruption of endothelial tight junctions of the blood-brain barrier, leading to extravasation of plasma proteins and fluid into the extracellular space of white matter, typically surrounding brain tumors, infections, or acute contusions?",
        "options": [
            {"text": "Cytotoxic edema", "is_correct": False},
            {"text": "Vasogenic edema", "is_correct": True},
            {"text": "Interstitial (hydrocephalic) edema", "is_correct": False},
            {"text": "Osmotic edema", "is_correct": False},
            {"text": "Ischemic uncoupling edema", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. Vasogenic edema.\n\nThere are three major recognized types of cerebral edema: (1) Vasogenic edema: Breakdown of the blood-brain barrier tight junctions allows protein-rich plasma exudate to escape into the extracellular space, spreading predominantly through the compliant white matter; common around tumors (glioblastoma, metastases), abscesses, and trauma; responds dramatically to corticosteroids (dexamethasone). (2) Cytotoxic edema: Intracellular swelling of neurons and glia due to Na+/K+-ATPase failure and energy depletion; BBB remains intact; common in acute cerebral ischemia/stroke and toxins. (3) Interstitial (hydrocephalic) edema: Transependymal transudation of CSF across the ventricular wall into periventricular white matter in obstructive hydrocephalus.\n\n• Option A is incorrect: Cytotoxic edema is intracellular swelling without BBB breakdown.\n• Option C is incorrect: Interstitial edema occurs across the ependyma in hydrocephalus.\n• Option D is incorrect: Osmotic edema occurs during severe systemic hypo-osmolarity (e.g., SIADH, water intoxication)."
    }
]

questions_section1.extend([
    {'category': 'In House: CNS Development',
 'explanation': 'Correct Answer: B. Myelination proceeds in a caudal-to-rostral, posterior-to-anterior direction, with '
                'sensory and motor pathways myelinating before higher-order cortical association areas.\n'
                '\n'
                'Postnatal CNS maturation follows a strictly programmed spatio-temporal order: (1) Caudal to rostral: '
                'spinal cord and brainstem myelinate before cerebral hemispheres; (2) Posterior to anterior: '
                'occipital/parietal sensory cortex myelinates before frontal prefrontal cortex; (3) Primary sensory '
                'and motor pathways myelinate in infancy, whereas prefrontal executive association regions continue '
                'myelinating into the third decade of life. Massive synaptic overproduction in early infancy is '
                'followed by activity-dependent synaptic pruning during childhood and adolescence. Brain weight '
                'doubles in the first year of life and reaches ~90% of adult weight by age 5.\n'
                '\n'
                '• Option A is incorrect: Prefrontal cortex is the last, not first, region to complete myelination.\n'
                '• Option C is incorrect: Synaptic density peaks in early childhood and undergoes extensive pruning.\n'
                '• Option D is incorrect: Fetal brain weight at 4 months is a fraction of adult size.\n'
                '• Option E is incorrect: Oligodendrocytes myelinate only the CNS; Schwann cells myelinate the PNS.',
 'id': 'IH_Q041',
 'options': [{'is_correct': False,
              'text': 'Myelination occurs first in the prefrontal association cortex and proceeds caudally toward the '
                      'brainstem and spinal cord'},
             {'is_correct': True,
              'text': 'Myelination proceeds in a caudal-to-rostral, posterior-to-anterior direction, with sensory and '
                      'motor pathways myelinating before higher-order cortical association areas'},
             {'is_correct': False,
              'text': 'Total synaptic density increases linearly throughout adulthood without any phase of synaptic '
                      'pruning'},
             {'is_correct': False,
              'text': 'The human brain achieves its full adult weight and volume by the end of the fourth '
                      'post-conceptual month'},
             {'is_correct': False,
              'text': 'Oligodendrocytes begin myelinating peripheral motor nerves before Schwann cells appear'}],
 'question_number': 41,
 'stem': 'Postnatal human brain maturation is characterized by dynamic structural remodeling rather than significant '
         'neurogenesis. Which of the following statements correctly describes the temporal and spatial progression of '
         'myelination and synaptogenesis during early childhood development?'},
    {'category': 'In House: CNS Development',
 'explanation': 'Correct Answer: B. Disruption of ocular dominance column competition in layer IV of the primary '
                'visual cortex during a critical period of development.\n'
                '\n'
                'During postnatal neurodevelopment, neural circuits require patterned sensory stimulation during a '
                "designated 'critical period' for proper structural refinement. In the primary visual cortex (V1, "
                'Brodmann area 17), inputs from each eye compete for synaptic territory in cortical layer IV to form '
                'ocular dominance columns. In uncorrected strabismus or monocular cataract, unequal or discordant '
                'visual input leads to atrophy of cortical inputs driven by the misaligned eye and expansion of inputs '
                'from the fixing eye. If untreated before the critical period closes (typically by age 7-8), permanent '
                'cortical blindness (amblyopia) ensues despite normal ocular anatomy.\n'
                '\n'
                '• Option A is incorrect: Retinal photoreceptors remain structurally intact.\n'
                '• Option C is incorrect: Optic nerve myelination is complete in infancy and is not halted by '
                'strabismus.\n'
                '• Option D is incorrect: Fontanelle closure does not compress the optic chiasm.\n'
                '• Option E is incorrect: Hyaloid artery regression is a normal embryonic event occurring prior to '
                'birth.',
 'id': 'IH_Q042',
 'options': [{'is_correct': False, 'text': 'Excessive apoptosis of retinal rod photoreceptors in the turned eye'},
             {'is_correct': True,
              'text': 'Disruption of ocular dominance column competition in layer IV of the primary visual cortex '
                      'during a critical period of development'},
             {'is_correct': False, 'text': 'Failure of the optic nerve to myelinate due to reduced light entry'},
             {'is_correct': False,
              'text': 'Irreversible closure of the anterior fontanelle compressing the optic chiasm'},
             {'is_correct': False, 'text': 'Premature regression of the hyaloid artery'}],
 'question_number': 42,
 'stem': 'A 4-year-old boy is brought to the ophthalmologist for evaluation of an inward turning of his right eye '
         '(strabismus) that was noticed at 8 months of age but never treated. Corrective lenses now align his visual '
         'axes, but visual acuity in the right eye remains 20/200, despite completely normal ocular media, retina, and '
         'optic nerve. Patching of the left eye is initiated immediately. Which of the following neurodevelopmental '
         'principles explains why early correction of strabismus is mandatory to prevent permanent visual deficit '
         '(amblyopia)?'},
    {'category': 'In House: Neurotransmission',
 'explanation': 'Correct Answer: B. Tyrosine hydroxylase; requires Tetrahydrobiopterin (BH4).\n'
                '\n'
                'The biosynthesis of catecholamines proceeds as follows: Phenylalanine -> Tyrosine -> L-DOPA -> '
                'Dopamine -> Norepinephrine -> Epinephrine. The initial and rate-limiting step is the conversion of '
                'L-tyrosine to L-DOPA catalyzed by tyrosine hydroxylase, which strictly requires tetrahydrobiopterin '
                '(BH4), molecular oxygen, and iron as cofactors. Defects in BH4 synthesis or dihydrobiopterin '
                'reductase cause hyperphenylalaninemia and severe secondary deficiency of dopamine, norepinephrine, '
                'and serotonin.\n'
                '\n'
                '• Option A is incorrect: DOPA decarboxylase converts L-DOPA to dopamine; while it requires vitamin B6 '
                '(PLP), it is not the rate-limiting step.\n'
                '• Option C is incorrect: Dopamine β-hydroxylase converts dopamine to norepinephrine inside synaptic '
                'vesicles and requires Vitamin C and copper, not B12.\n'
                '• Option D is incorrect: PNMT converts NE to epinephrine in the adrenal medulla; it requires '
                'S-adenosylmethionine (SAM) and is induced by cortisol.\n'
                '• Option E is incorrect: MAO-A degrades monoamines; it contains an FAD cofactor.',
 'id': 'IH_Q043',
 'options': [{'is_correct': False, 'text': 'DOPA decarboxylase; requires Pyridoxal phosphate (Vitamin B6)'},
             {'is_correct': True, 'text': 'Tyrosine hydroxylase; requires Tetrahydrobiopterin (BH4)'},
             {'is_correct': False, 'text': 'Dopamine beta-hydroxylase; requires Vitamin B12'},
             {'is_correct': False, 'text': 'Phenylethanolamine N-methyltransferase (PNMT); requires Thiamine'},
             {'is_correct': False, 'text': 'Monoamine oxidase A; requires Vitamin C'}],
 'question_number': 43,
 'stem': 'A 23-year-old researcher is studying the enzymatic pathway for catecholamine biosynthesis in adrenergic and '
         'dopaminergic neurons. Which of the following enzymes represents the rate-limiting step in the synthesis of '
         'all endogenous catecholamines, and what cofactor is strictly required for its catalytic activity?'},
    {'category': 'In House: Neurotransmission',
 'explanation': 'Correct Answer: C. Serotonin (5-hydroxytryptamine); metabolized by Monoamine oxidase (MAO).\n'
                '\n'
                'Serotonin (5-HT) is synthesized from L-tryptophan (via tryptophan hydroxylase, requiring BH4, '
                'followed by aromatic L-amino acid decarboxylase). Serotonin is cleared from synapses by the serotonin '
                'transporter (SERT) and metabolized by monoamine oxidase A (MAO-A) and aldehyde dehydrogenase into '
                '5-hydroxyindoleacetic acid (5-HIAA). Neuroendocrine carcinoid tumors (often originating in the ileum '
                'with liver metastases) hypersecrete serotonin, producing carcinoid syndrome (flushing, diarrhea, '
                'right-sided valvular heart disease) and massive urinary excretion of 5-HIAA.\n'
                '\n'
                '• Option A is incorrect: Dopamine is metabolized to homovanillic acid (HVA).\n'
                '• Option B is incorrect: Norepinephrine is metabolized to vanillylmandelic acid (VMA) and '
                'metanephrines.\n'
                '• Option D is incorrect: Histamine is metabolized to N-methylhistamine and methylimidazoleacetic '
                'acid.\n'
                '• Option E is incorrect: Acetylcholine is broken down to choline and acetate by AChE.',
 'id': 'IH_Q044',
 'options': [{'is_correct': False, 'text': 'Dopamine; metabolized by Catechol-O-methyltransferase (COMT)'},
             {'is_correct': False,
              'text': 'Norepinephrine; metabolized by Phenylethanolamine N-methyltransferase (PNMT)'},
             {'is_correct': True, 'text': 'Serotonin (5-hydroxytryptamine); metabolized by Monoamine oxidase (MAO)'},
             {'is_correct': False, 'text': 'Histamine; metabolized by Diamine oxidase'},
             {'is_correct': False, 'text': 'Acetylcholine; metabolized by Acetylcholinesterase'}],
 'question_number': 44,
 'stem': 'A 54-year-old woman presents with episodes of intense facial flushing, watery diarrhea, and bronchospasm. '
         'Urinary analysis demonstrates markedly elevated excretion of 5-hydroxyindoleacetic acid (5-HIAA). In this '
         'patient, 5-HIAA is the primary end-stage metabolic breakdown product of which monoamine neurotransmitter, '
         'and what enzyme initiates its breakdown?'},
    {'category': 'In House: Neurotransmission',
 'explanation': 'Correct Answer: B. Nigrostriatal pathway (parkinsonism) and Tuberoinfundibular pathway '
                '(galactorrhea).\n'
                '\n'
                'The brain contains four major dopamine pathways: (1) Nigrostriatal pathway (substantia nigra pars '
                'compacta to dorsal striatum): controls voluntary motor coordination; D2 blockade causes '
                'extrapyramidal symptoms (EPS) and drug-induced parkinsonism. (2) Tuberoinfundibular pathway (arcuate '
                'nucleus of hypothalamus to anterior pituitary): dopamine acts as prolactin-inhibiting factor; D2 '
                'blockade removes inhibition, causing hyperprolactinemia, galactorrhea, amenorrhea, and gynecomastia. '
                '(3) Mesolimbic pathway (VTA to nucleus accumbens): mediates motivation/reward; overactivity causes '
                'positive symptoms of schizophrenia; D2 blockade reduces delusions/hallucinations. (4) Mesocortical '
                'pathway (VTA to prefrontal cortex): mediates cognition/affect; underactivity causes negative and '
                'cognitive symptoms.\n'
                '\n'
                '• Option A is incorrect: Mesolimbic mediates psychosis/reward; mesocortical mediates negative '
                'symptoms.\n'
                '• Options C, D, and E do not match the anatomy of parkinsonism and prolactin regulation.',
 'id': 'IH_Q045',
 'options': [{'is_correct': False, 'text': 'Mesolimbic pathway and Mesocortical pathway'},
             {'is_correct': True,
              'text': 'Nigrostriatal pathway (parkinsonism) and Tuberoinfundibular pathway (galactorrhea)'},
             {'is_correct': False, 'text': 'Tuberoinfundibular pathway and Locus coeruleus projection'},
             {'is_correct': False, 'text': 'Raphe nuclei tract and Medial forebrain bundle'},
             {'is_correct': False, 'text': 'Area postrema and Tectospinal tract'}],
 'question_number': 45,
 'stem': 'A 26-year-old man with schizophrenia is treated with haloperidol, a high-potency dopamine D2 receptor '
         'antagonist. Three weeks later, he develops bilateral resting tremor, rigidity, bradykinesia, and masked '
         'facies. Concurrently, he reports bilateral breast enlargement and milky nipple discharge (galactorrhea). '
         'Antagonism of dopamine D2 receptors in which two respective central dopaminergic pathways accounts for his '
         'parkinsonian symptoms and galactorrhea?'},
    {'category': 'In House: Neurotransmission',
 'explanation': 'Correct Answer: B. Locus coeruleus; Norepinephrine.\n'
                '\n'
                "The locus coeruleus ('blue place', due to neuromelanin granules) is located in the posterior rostral "
                'pons near the lateral floor of the 4th ventricle. It is the primary site of norepinephrine (NE) '
                'synthesis and source of noradrenergic projections throughout the neuraxis. Hyperactivity of the locus '
                'coeruleus is implicated in the pathogenesis of panic disorder, generalized anxiety, PTSD, and the '
                'physiological manifestations of opiate withdrawal. Conversely, its hypoactivity is associated with '
                'depression.\n'
                '\n'
                '• Option A is incorrect: Substantia nigra is in the midbrain and synthesizes dopamine (degenerated in '
                'Parkinson disease).\n'
                '• Option C is incorrect: Dorsal raphe nuclei are in the brainstem midline and synthesize serotonin.\n'
                '• Option D is incorrect: Nucleus basalis of Meynert is in the basal forebrain and synthesizes '
                'acetylcholine (degenerated in Alzheimer disease).\n'
                '• Option E is incorrect: Red nucleus is in the rostral midbrain tegmentum and controls upper limb '
                'flexor tone (rubrospinal tract).',
 'id': 'IH_Q046',
 'options': [{'is_correct': False, 'text': 'Substantia nigra; Dopamine'},
             {'is_correct': True, 'text': 'Locus coeruleus; Norepinephrine'},
             {'is_correct': False, 'text': 'Dorsal raphe nucleus; Serotonin'},
             {'is_correct': False, 'text': 'Basal nucleus of Meynert; Acetylcholine'},
             {'is_correct': False, 'text': 'Red nucleus; Glutamate'}],
 'question_number': 46,
 'stem': 'A 32-year-old woman experiences abrupt episodes of intense fear, heart palpitations, trembling, sweating, '
         'and feelings of impending doom. Functional neuroimaging during an episode reveals marked hyperactivation of '
         'a small, bluish-pigmented bilateral nucleus situated in the rostral dorsolateral pontine tegmentum beneath '
         'the floor of the fourth ventricle. Which nucleus is this, and what is its primary neurotransmitter?'},
    {'category': 'In House: Neurotransmission',
 'explanation': 'Correct Answer: A. Raphe nuclei of the brainstem midline.\n'
                '\n'
                'The raphe nuclei form a contiguous column of serotonergic cell bodies lining the midline of the '
                'brainstem (midbrain, pons, and medulla). Rostral raphe nuclei (dorsal and median raphe in the '
                'midbrain/pons) project widely to the cerebral cortex, limbic system, and basal ganglia, regulating '
                'mood, sleep-wake cycles, appetite, and cognition. Caudal raphe nuclei (in the medulla) project down '
                'the spinal cord to modulate nociceptive transmission in the dorsal horn (descending pain inhibitory '
                'pathway).\n'
                '\n'
                '• Option B is incorrect: Striatum receives dopaminergic inputs and consists primarily of GABAergic '
                'medium spiny neurons.\n'
                '• Option C is incorrect: VTA synthesizes dopamine.\n'
                '• Option D is incorrect: Lateral hypothalamus synthesizes orexin/hypocretin (deficient in '
                'narcolepsy).\n'
                '• Option E is incorrect: Hippocampal dentate gyrus is a primary site of adult neurogenesis and memory '
                'formation.',
 'id': 'IH_Q047',
 'options': [{'is_correct': True, 'text': 'Raphe nuclei of the brainstem midline'},
             {'is_correct': False, 'text': 'Caudate nucleus and putamen'},
             {'is_correct': False, 'text': 'Ventral tegmental area of Tsai'},
             {'is_correct': False, 'text': 'Lateral hypothalamic area'},
             {'is_correct': False, 'text': 'Dentate gyrus of the hippocampus'}],
 'question_number': 47,
 'stem': 'A 29-year-old man with severe major depressive disorder is started on sertraline. Therapeutic efficacy '
         'depends on increasing synaptic concentrations of serotonin throughout the central nervous system. Where are '
         'the neuronal cell bodies responsible for synthesizing the majority of central serotonin located?'},
    {'category': 'In House: CNS Anatomy & Glia',
 'explanation': 'Correct Answer: B. Mesoderm (embryonic yolk sac myeloid progenitors); resident immune surveillance '
                'and phagocytosis.\n'
                '\n'
                'Unlike all other central nervous system cells (neurons, astrocytes, oligodendrocytes, ependyma), '
                'which originate from neuroectoderm, microglia are derived from mesodermal primitive myeloid '
                'progenitor cells in the embryonic yolk sac that migrate into the developing brain. Microglia function '
                'as the resident mononuclear phagocytes of the CNS, participating in immune defense, synaptic pruning '
                'during development, and clearing cellular debris following injury. In HIV encephalitis, HIV infects '
                'microglia/macrophages via CD4 and CCR5/CXCR4 coreceptors, causing them to fuse into characteristic '
                'multinucleated giant cells.\n'
                '\n'
                '• Option A is incorrect: Astrocytes are neuroectodermal and support the BBB.\n'
                '• Option C is incorrect: Schwann cells are neural crest-derived.\n'
                '• Option D is incorrect: Choroid plexus epithelium produces CSF and is neuroectodermal.\n'
                '• Option E is incorrect: Ependyma is neuroectodermal.',
 'id': 'IH_Q048',
 'options': [{'is_correct': False,
              'text': 'Neuroectoderm of the neural tube; structural support of the blood-brain barrier'},
             {'is_correct': True,
              'text': 'Mesoderm (embryonic yolk sac myeloid progenitors); resident immune surveillance and '
                      'phagocytosis'},
             {'is_correct': False, 'text': 'Neural crest; myelination of peripheral sensory axons'},
             {'is_correct': False, 'text': 'Endoderm; secretion of cerebrospinal fluid in the lateral ventricles'},
             {'is_correct': False, 'text': 'Surface ectoderm; maintenance of the ependymal ciliary carpet'}],
 'question_number': 48,
 'stem': 'An autopsy performed on a 38-year-old patient who died of untreated advanced HIV infection reveals '
         'microglial nodules and multinucleated giant cells throughout the subcortical white matter (HIV-associated '
         'dementia). From which embryonic tissue origin are microglia derived, and what is their primary physiological '
         'function?'},
    {'category': 'In House: CNS Anatomy & Glia',
 'explanation': 'Correct Answer: B. A single oligodendrocyte can myelinate internodes on up to 30 to 50 different CNS '
                'axons, whereas a Schwann cell myelinates only a single internode of a single PNS axon.\n'
                '\n'
                'Oligodendrocytes (derived from neural tube neuroectoderm) are the myelin-producing cells of the CNS; '
                'each oligodendrocyte extends multiple cytoplasmic processes that wrap around and myelinate internodes '
                'on up to 30–50 separate axons. In contrast, Schwann cells (derived from neural crest) are the '
                'myelinating cells of the PNS; each myelinating Schwann cell envelops only ONE single internodal '
                'segment on ONE individual axon. Schwann cells also surround unmyelinated axons (Remak bundles) and '
                'promote peripheral axonal regeneration by forming Bands of Büngner.\n'
                '\n'
                '• Option A is incorrect: It reverses the actual anatomy.\n'
                '• Option C is incorrect: Oligodendrocytes derive from neuroectoderm, Schwann cells from neural '
                'crest.\n'
                '• Option D is incorrect: Schwann cells are enveloped by an endoneurial basement membrane; '
                'oligodendrocytes lack a basement membrane.\n'
                '• Option E is incorrect: Myelin protein zero (P0) is specific to PNS Schwann cell myelin; proteolipid '
                'protein (PLP) and myelin basic protein (MBP) dominate CNS myelin.',
 'id': 'IH_Q049',
 'options': [{'is_correct': False,
              'text': 'A single Schwann cell can myelinate up to 50 individual CNS axons simultaneously, whereas an '
                      'oligodendrocyte myelinates only a single axon internode'},
             {'is_correct': True,
              'text': 'A single oligodendrocyte can myelinate internodes on up to 30 to 50 different CNS axons, '
                      'whereas a Schwann cell myelinates only a single internode of a single PNS axon'},
             {'is_correct': False,
              'text': 'Oligodendrocytes are derived from neural crest, while Schwann cells are derived from '
                      'neuroectoderm'},
             {'is_correct': False,
              'text': 'Schwann cells lack basement membranes, whereas oligodendrocytes possess thick collagenous '
                      'basement membranes'},
             {'is_correct': False,
              'text': 'Oligodendrocytes express myelin protein zero (P0), while Schwann cells exclusively express '
                      'proteolipid protein (PLP)'}],
 'question_number': 49,
 'stem': 'A 16-year-old boy presents with progressive balance difficulties and intention tremor. Genetic testing '
         'confirms a diagnosis of Friedreich ataxia, an autosomal recessive neurodegenerative disorder. In contrast to '
         'multiple sclerosis, in which demyelination is mediated by autoimmune destruction of oligodendrocytes, '
         'peripheral demyelinating polyneuropathies (e.g., Charcot-Marie-Tooth) involve pathology of Schwann cells. '
         'What is a key structural difference between oligodendrocytes and Schwann cells?'},
    {'category': 'In House: Ventricular System & CSF',
 'explanation': 'Correct Answer: B. Choroid epithelial cells (modified ependymal cells) joined by apical tight '
                'junctions (zonulae occludentes).\n'
                '\n'
                'In the choroid plexus, the capillary endothelial cells are FENESTRATED, allowing free leakage of '
                'water, electrolytes, and plasma proteins into the stroma of the choroid plexus. However, the modified '
                'ependymal cells that cover the choroid villi (choroid epithelial cells) are bound tightly to one '
                'another by apical tight junctions (zonulae occludentes). This continuous epithelial monolayer forms '
                'the Blood-CSF Barrier, selectively controlling which ions and solutes are actively transported into '
                'the ventricular lumen to generate cerebrospinal fluid.\n'
                '\n'
                '• Option A is incorrect: Capillaries of the choroid plexus are fenestrated and lack tight junctions '
                '(unlike parenchymal BBB capillaries).\n'
                '• Option C is incorrect: Pial trabeculae are loose connective tissue elements.\n'
                '• Option D is incorrect: Pericytes do not form the tight physiological barrier in the choroid '
                'plexus.\n'
                '• Option E is incorrect: Arachnoid barrier cells seal the subarachnoid space from the dura, not the '
                'ventricular CSF.',
 'id': 'IH_Q050',
 'options': [{'is_correct': False, 'text': 'Choroid plexus capillary endothelial cells joined by zonulae occludentes'},
             {'is_correct': True,
              'text': 'Choroid epithelial cells (modified ependymal cells) joined by apical tight junctions (zonulae '
                      'occludentes)'},
             {'is_correct': False, 'text': 'Pia mater connective tissue trabeculae'},
             {'is_correct': False, 'text': 'Pericytes covering choroid capillary venules'},
             {'is_correct': False, 'text': 'Arachnoid barrier cells lining the dural border'}],
 'question_number': 50,
 'stem': 'During a neuroanatomy tutorial on brain barriers, the professor emphasizes that while the capillary '
         'endothelium of the brain parenchyma constitutes the blood-brain barrier (BBB), an entirely different layer '
         'forms the physiological barrier within the choroid plexus (the blood-CSF barrier). Which cellular component '
         'forms the true selective barrier in the choroid plexus?'},
    {'category': 'In House: Ventricular System & CSF',
 'explanation': 'Correct Answer: A. Area postrema.\n'
                '\n'
                'Circumventricular organs (CVOs) are specialized brain structures situated around the 3rd and 4th '
                'ventricles that have fenestrated capillaries and lack a normal blood-brain barrier, allowing them to '
                'sample blood-borne chemicals. The Area Postrema is located on the dorsal surface of the caudal '
                'medulla in the floor of the 4th ventricle. It contains the chemoreceptor trigger zone (CTZ), which '
                'detects circulating emetogenic toxins (such as chemotherapy drugs) and initiates the vomiting reflex '
                'via projections to the nucleus tractus solitarius (NTS).\n'
                '\n'
                '• Option B is incorrect: OVLT senses plasma osmolarity and fever-inducing pyrogens (IL-1, PGE2).\n'
                '• Option C is incorrect: Subfornical organ responds to circulating angiotensin II to regulate thirst '
                'and fluid balance.\n'
                '• Option D is incorrect: The pineal gland secretes melatonin to regulate circadian rhythms.\n'
                '• Option E is incorrect: The median eminence releases hypothalamic hypophysiotropic hormones into the '
                'hypophyseal portal circulation.',
 'id': 'IH_Q051',
 'options': [{'is_correct': True, 'text': 'Area postrema'},
             {'is_correct': False, 'text': 'Organum vasculosum of the lamina terminalis (OVLT)'},
             {'is_correct': False, 'text': 'Subfornical organ'},
             {'is_correct': False, 'text': 'Pineal gland'},
             {'is_correct': False, 'text': 'Median eminence'}],
 'question_number': 51,
 'stem': 'A 50-year-old man undergoing chemotherapy with cisplatin experiences intense nausea and vomiting within 30 '
         'minutes of infusion. Cisplatin triggers emesis by crossing into a circumventricular organ situated in the '
         'caudal floor of the fourth ventricle that lacks a blood-brain barrier. Which circumventricular organ '
         'functions as this chemoreceptor trigger zone for vomiting?'},
    {'category': 'In House: Ventricular System & CSF',
 'explanation': 'Correct Answer: B. Anterior cerebral artery (ACA).\n'
                '\n'
                'Subfalcine (cingulate) herniation occurs when a unilateral mass lesion in the cerebral hemisphere '
                'forces the cingulate gyrus medially beneath the rigid, sickle-shaped free margin of the falx cerebri. '
                'This compresses the ipsilateral (and sometimes contralateral) anterior cerebral artery (ACA) against '
                'the falx. Because the ACA supplies the medial surface of the primary motor and somatosensory cortex '
                '(which represents the contralateral leg and foot on the cortical homunculus, as well as the '
                'micturition center in the medial frontal lobe), ACA compression results in contralateral leg '
                'weakness, sensory loss, and urinary incontinence.\n'
                '\n'
                '• Option A is incorrect: MCA supplies the lateral cortical convexity (face and arm areas).\n'
                '• Option C is incorrect: PCA is compressed in uncal (transtentorial) herniation, causing '
                'contralateral homonymous hemianopia.\n'
                '• Option D is incorrect: Anterior choroidal artery supplies the posterior limb of internal capsule '
                'and optic tract.\n'
                '• Option E is incorrect: PICA supplies the lateral medulla and inferior cerebellum.',
 'id': 'IH_Q052',
 'options': [{'is_correct': False, 'text': 'Middle cerebral artery (MCA), superior division'},
             {'is_correct': True, 'text': 'Anterior cerebral artery (ACA)'},
             {'is_correct': False, 'text': 'Posterior cerebral artery (PCA), calcarine branch'},
             {'is_correct': False, 'text': 'Anterior choroidal artery'},
             {'is_correct': False, 'text': 'Posterior inferior cerebellar artery (PICA)'}],
 'question_number': 52,
 'stem': 'A 62-year-old woman with a large right frontal meningioma is brought to the emergency department after '
         'developing acute left leg and foot weakness, accompanied by sensory loss in the left foot and urinary '
         'urgency. Non-contrast head CT demonstrates subfalcine herniation with a 12 mm midline shift. Compression of '
         'which of the following cerebral arteries is responsible for her selective lower extremity deficits?'},
    {'category': 'In House: Ventricular System & CSF',
 'explanation': 'Correct Answer: C. Dandy-Walker malformation.\n'
                '\n'
                'Dandy-Walker malformation is a congenital posterior fossa anomaly characterized by a classic triad: '
                '(1) Agenesis or hypoplasia of the cerebellar vermis, (2) Cystic dilation of the fourth ventricle that '
                'fills the posterior fossa, and (3) An enlarged posterior cranial fossa with upward displacement of '
                'the tentorium and transverse sinuses. Obstruction of the foramina of Luschka and Magendie leads to '
                'non-communicating hydrocephalus in ~80% of patients, presenting with macrocephaly, delayed motor '
                'milestones, and signs of increased ICP.\n'
                '\n'
                '• Option A is incorrect: Chiari I features cerebellar tonsillar ectopia >5 mm into the cervical canal '
                'without posterior fossa enlargement.\n'
                '• Option B is incorrect: Chiari II features herniation of tonsils and vermis with a SMALL posterior '
                'fossa and myelomeningocele.\n'
                '• Option C is incorrect: Holoprosencephaly is failure of forebrain separation.\n'
                '• Option E is incorrect: Arachnoid cysts do not feature vermian agenesis or 4th ventricular cystic '
                'ballooning.',
 'id': 'IH_Q053',
 'options': [{'is_correct': False, 'text': 'Chiari I malformation'},
             {'is_correct': False, 'text': 'Chiari II malformation'},
             {'is_correct': True, 'text': 'Dandy-Walker malformation'},
             {'is_correct': False, 'text': 'Holoprosencephaly'},
             {'is_correct': False, 'text': 'Arachnoid cyst of the middle cranial fossa'}],
 'question_number': 53,
 'stem': 'A 5-year-old child presents with progressive macrocephaly, clumsiness, and morning vomiting. Brain MRI '
         'demonstrates complete absence of the cerebellar vermis, cystic ballooning of the fourth ventricle occupying '
         'an enlarged posterior cranial fossa, and high tentorial insertion, associated with marked lateral and third '
         'ventricular dilation. What is the diagnosis?'},
    {'category': 'In House: CNS Development',
 'explanation': 'Correct Answer: B. Holoprosencephaly.\n'
                '\n'
                'Holoprosencephaly (HPE) is a failure of the embryonic prosencephalon (forebrain) to cleave into two '
                'distinct cerebral hemispheres during the 5th to 6th weeks of gestation. It is classically associated '
                'with mutations in Sonic Hedgehog (SHH), Trisomy 13 (Patau syndrome), and maternal diabetes/fetal '
                'alcohol syndrome. The condition exists on a spectrum: alobar (most severe; single monoventricular '
                "brain, fused thalami, cyclopia/proboscis), semilobar, and lobar. Facial anomalies ('the face predicts "
                "the brain') include cyclopia, ethmocephaly, cebocephaly, premaxillary agenesis, or a single central "
                'incisor.\n'
                '\n'
                '• Option A is incorrect: Lissencephaly is smooth brain caused by abnormal neuronal migration.\n'
                '• Option C is incorrect: Schizencephaly features full-thickness clefts in the cerebral hemispheres '
                'lined with gray matter.\n'
                '• Option D is incorrect: Polymicrogyria features an excessive number of small, abnormally folded '
                'gyri.\n'
                '• Option E is incorrect: Dandy-Walker malformation is a posterior fossa disorder (vermian agenesis).',
 'id': 'IH_Q054',
 'options': [{'is_correct': False, 'text': 'Lissencephaly'},
             {'is_correct': True, 'text': 'Holoprosencephaly'},
             {'is_correct': False, 'text': 'Schizencephaly'},
             {'is_correct': False, 'text': 'Polymicrogyria'},
             {'is_correct': False, 'text': 'Dandy-Walker malformation'}],
 'question_number': 54,
 'stem': 'An infant is born at 36 weeks gestation with severe craniofacial malformations, including hypotelorism, a '
         'single median maxillary central incisor, cleft lip and palate, and microcephaly. High-resolution cranial '
         'ultrasound reveals a monoventricular brain cavity with fusion of the frontal lobes and absence of the corpus '
         'callosum and septum pellucidum. Prenatal genetic testing confirms a heterozygous mutation in the Sonic '
         'Hedgehog (SHH) gene. What developmental diagnosis best fits these findings?'},
    {'category': 'In House: CNS Development',
 'explanation': 'Correct Answer: B. Failure of the rostral (anterior) neuropore to close; absent fetal swallowing '
                'reflex due to destruction of brainstem swallowing centers.\n'
                '\n'
                'Anencephaly is the most common lethal congenital CNS malformation, resulting from failure of the '
                'rostral (anterior) neuropore to close around embryonic day 25. The unclosed neural tube remains '
                'exposed to amniotic fluid, undergoing secondary hemorrhagic necrosis and degeneration (leaving only a '
                'vascular mass called area cerebrovasculosa), while the overlying calvarium and scalp fail to form. '
                'Polyhydramnios (excess amniotic fluid) occurs because destruction of the forebrain and brainstem '
                'centers eliminates the fetal swallowing reflex, preventing the fetus from ingesting and recirculating '
                'amniotic fluid.\n'
                '\n'
                '• Option A is incorrect: Caudal neuropore failure causes spina bifida; amniotic fluid is removed by '
                'fetal swallowing, not kidneys.\n'
                '• Option C is incorrect: Neural crest failure causes Hirschsprung disease (distal bowel), not '
                'anencephaly.\n'
                '• Option D is incorrect: Metopic craniosynostosis causes trigonocephaly, not anencephaly.\n'
                '• Option E is incorrect: Notochord duplication causes split cord malformation.',
 'id': 'IH_Q055',
 'options': [{'is_correct': False,
              'text': 'Failure of the caudal neuropore to close; fetal polyuria due to impaired renal concentrating '
                      'ability'},
             {'is_correct': True,
              'text': 'Failure of the rostral (anterior) neuropore to close; absent fetal swallowing reflex due to '
                      'destruction of brainstem swallowing centers'},
             {'is_correct': False,
              'text': 'Failure of neural crest migration; lack of esophageal innervation preventing peristalsis'},
             {'is_correct': False, 'text': 'Premature fusion of the metopic suture; obstruction of the amniotic sac'},
             {'is_correct': False,
              'text': 'Duplication of the notochord; mechanical compression of the umbilical cord'}],
 'question_number': 55,
 'stem': 'A 22-year-old primigravida delivers a stillborn male infant at 28 weeks gestation. Physical examination '
         'shows complete absence of the cranial vault (calvarium), with rudimentary brain tissue exposed to the '
         "amniotic environment and prominent, bulging orbits ('frog-like appearance'). Prenatal ultrasound had "
         'demonstrated profound polyhydramnios. What was the embryonic origin of this defect, and why did '
         'polyhydramnios develop?'},
    {'category': 'In House: Neurotransmission & Anesthesia',
 'explanation': 'Correct Answer: B. The low extracellular pH shifts the equilibrium toward the charged (ionized) '
                'protonated form, severely reducing the uncharged fraction capable of crossing the lipid neuronal '
                'membrane.\n'
                '\n'
                'Local anesthetics are weak bases (pKa typically between 7.6 and 9.0). According to the '
                'Henderson-Hasselbalch equation (pH = pKa + log [Base]/[Cation]), only the uncharged (non-ionized) '
                'free base form can permeate through the hydrophobic lipid bilayer of the neuronal membrane. Once '
                'inside the axoplasm, the drug equilibrates and the protonated (ionized) cation binds to the inner '
                'pore of the voltage-gated Na+ channel. In inflamed or infected tissues, the extracellular pH drops '
                'substantially (to pH 5.5-6.0). In this acidic environment, the drug is overwhelmingly protonated '
                '(ionized), leaving virtually no lipophilic uncharged drug available to cross the axonal membrane, '
                'resulting in profound anesthetic failure.\n'
                '\n'
                '• Option A is incorrect: Bacteria do not degrade lidocaine via specific amidases.\n'
                '• Option C is incorrect: Acidosis does not denature the sodium channel.\n'
                '• Option D is incorrect: Lidocaine does not precipitate at acidic pH; it is actually more '
                'water-soluble when protonated.\n'
                '• Option E is incorrect: Nodes of Ranvier do not close mechanically.',
 'id': 'IH_Q056',
 'options': [{'is_correct': False, 'text': 'Bacterial enzymes rapidly metabolize lidocaine via extracellular amidases'},
             {'is_correct': True,
              'text': 'The low extracellular pH shifts the equilibrium toward the charged (ionized) protonated form, '
                      'severely reducing the uncharged fraction capable of crossing the lipid neuronal membrane'},
             {'is_correct': False, 'text': 'Acidic pH permanently denatures the voltage-gated sodium channel protein'},
             {'is_correct': False, 'text': 'Lidocaine precipitates into insoluble crystals at pH below 7.0'},
             {'is_correct': False, 'text': 'Local inflammation closes all nodes of Ranvier'}],
 'question_number': 56,
 'stem': 'A 34-year-old dentist prepares to extract an infected lower molar surrounded by purulent exudate (pH 5.8). '
         'He infiltrates the adjacent tissue with 2% lidocaine (pKa = 7.9). Despite administering three separate '
         'cartridges, the patient continues to experience sharp, excruciating pain. What pharmacological principle '
         'explains why local anesthetics have markedly reduced clinical efficacy in infected, acidic tissue?'},
    {'category': 'In House: Neurotransmission & Anesthesia',
 'explanation': "Correct Answer: A. Intravenous 20% lipid emulsion ('lipid rescue').\n"
                '\n'
                'Local Anesthetic Systemic Toxicity (LAST) is a life-threatening complication resulting from '
                'accidental intravascular injection or rapid systemic absorption of high doses of local anesthetics '
                '(particularly highly lipophilic agents like bupivacaine). Bupivacaine strongly blocks cardiac '
                'voltage-gated Na+ channels and inhibits myocardial fatty acid oxidation. The definitive treatment for '
                "LAST is intravenous 20% lipid emulsion (e.g., Intralipid). Lipid emulsion acts as a 'lipid sink' "
                '(extracting the lipophilic anesthetic from myocardial and brain tissue into an intravascular lipid '
                'partition) and directly overcomes metabolic inhibition, rapidly restoring cardiac conduction and '
                'contractility.\n'
                '\n'
                '• Option B is incorrect: Calcium gluconate stabilizes cardiac membranes in hyperkalemia, but is '
                'ineffective in LAST.\n'
                '• Option C is incorrect: Flumazenil reverses benzodiazepines; it does not reverse local anesthetics '
                'and may trigger seizures.\n'
                '• Option D is incorrect: Sodium bicarbonate treats TCA toxicity and metabolic acidosis, but is not '
                'the primary rescue agent for LAST.\n'
                '• Option E is incorrect: Naloxone reverses opioid overdose.',
 'id': 'IH_Q057',
 'options': [{'is_correct': True, 'text': "Intravenous 20% lipid emulsion ('lipid rescue')"},
             {'is_correct': False, 'text': 'Intravenous calcium gluconate'},
             {'is_correct': False, 'text': 'Intravenous flumazenil'},
             {'is_correct': False, 'text': 'Intravenous sodium bicarbonate'},
             {'is_correct': False, 'text': 'Intravenous naloxone'}],
 'question_number': 57,
 'stem': 'A 45-year-old man undergoes an ultrasound-guided femoral nerve block using 0.5% bupivacaine. Ten minutes '
         'later, he complains of perioral numbness, metallic taste, and dizziness, rapidly followed by generalized '
         'tonic-clonic seizures, wide-complex ventricular tachycardia, and severe cardiovascular collapse (Local '
         'Anesthetic Systemic Toxicity, LAST). In addition to airway control and cardiopulmonary resuscitation, which '
         'of the following is the specific antidote of choice to reverse local anesthetic cardiotoxicity?'},
    {'category': 'In House: Neurotransmission',
 'explanation': 'Correct Answer: B. Barbiturates increase the duration of chloride channel opening and can directly '
                'open chloride channels at high concentrations even in the complete absence of GABA.\n'
                '\n'
                'Barbiturates and benzodiazepines both enhance GABA-A receptor-mediated inhibitory neurotransmission, '
                'but through fundamentally distinct allosteric actions: (1) Benzodiazepines increase the FREQUENCY of '
                'channel opening in response to GABA, but cannot open the channel independently of endogenous GABA. '
                "(2) Barbiturates prolong the DURATION of chloride channel opening ('barbiDURATe'). Crucially, at high "
                'concentrations, barbiturates become GABA-mimetic, directly opening the chloride pore even without '
                'GABA present. This ability to directly activate chloride conductance produces profound, unchecked CNS '
                'and medullary respiratory depression, leading to a much lower therapeutic index and high overdose '
                'fatality.\n'
                '\n'
                '• Option A is incorrect: It reverses the mechanisms (BZD = frequency, Barbiturate = duration).\n'
                '• Option C is incorrect: Tiagabine blocks GABA reuptake (GAT-1), not barbiturates.\n'
                '• Option D is incorrect: Barbiturates actually inhibit AMPA receptors, they do not stimulate NMDA '
                'receptors.\n'
                '• Option E is incorrect: Barbiturates are metabolized by hepatic P450 enzymes (and are potent CYP '
                'inducers).',
 'id': 'IH_Q058',
 'options': [{'is_correct': False,
              'text': 'Barbiturates increase the frequency of chloride channel opening, whereas benzodiazepines '
                      'increase channel duration'},
             {'is_correct': True,
              'text': 'Barbiturates increase the duration of chloride channel opening and can directly open chloride '
                      'channels at high concentrations even in the complete absence of GABA'},
             {'is_correct': False, 'text': 'Barbiturates irreversibly block astrocytic GABA reuptake transporters'},
             {'is_correct': False, 'text': 'Barbiturates act as full agonists at NMDA glutamate receptors'},
             {'is_correct': False,
              'text': 'Barbiturates lack hepatic metabolism and accumulate indefinitely in adipose tissue'}],
 'question_number': 58,
 'stem': 'A neuropharmacologist is contrasting the molecular mechanisms of phenobarbital (a barbiturate) versus '
         'lorazepam (a benzodiazepine) on the GABA-A receptor. Why are barbiturates associated with a significantly '
         'higher risk of fatal respiratory depression and toxicity in overdose compared to benzodiazepines?'},
    {'category': 'In House: Ventricular System & CSF',
 'explanation': 'Correct Answer: A. Calcified glomus of the choroid plexus; a common normal physiological finding that '
                'should not be mistaken for an intraventricular hemorrhage.\n'
                '\n'
                'The atrium (trigone) of the lateral ventricle is the confluence of the ventricular body, occipital '
                '(posterior) horn, and temporal (inferior) horn. Within the atrium, the choroid plexus forms a '
                'prominent enlargement called the Glomus of the choroid plexus. Physiological calcification of the '
                'glomus is extremely common with advancing age (seen in >50% of elderly adults) and appears as dense, '
                'symmetrical hyperdensities on CT. Recognizing this normal anatomical variant prevents '
                'misinterpretation as intraventricular hemorrhage or intraventricular neoplasm.\n'
                '\n'
                '• Option B is incorrect: Colloid cysts occur at the roof of the 3rd ventricle near the foramen of '
                'Monro, not in the lateral ventricular trigone.\n'
                '• Option C is incorrect: Ependymomas typically arise from the floor of the 4th ventricle in '
                'children.\n'
                '• Option D is incorrect: SEGAs arise near the foramen of Monro in tuberous sclerosis.\n'
                '• Option E is incorrect: The head of the caudate bulges into the lateral wall of the anterior '
                '(frontal) horn.',
 'id': 'IH_Q059',
 'options': [{'is_correct': True,
              'text': 'Calcified glomus of the choroid plexus; a common normal physiological finding that should not '
                      'be mistaken for an intraventricular hemorrhage'},
             {'is_correct': False, 'text': 'Bilateral colloid cysts of the third ventricle'},
             {'is_correct': False, 'text': 'Ependymoma of the fourth ventricle'},
             {'is_correct': False, 'text': 'Subependymal giant cell astrocytoma'},
             {'is_correct': False, 'text': 'Calcification of the caudate nucleus head'}],
 'question_number': 59,
 'stem': 'On an axial non-contrast brain CT scan of an 82-year-old patient, dense, symmetric bilateral calcifications '
         'are visualized in the posterior aspect of the lateral ventricles at the junction where the body, occipital '
         'horn, and temporal horn meet (the atrium / trigone). What normal anatomical structure is this, and what is '
         'its clinical significance?'},
    {'category': 'In House: Neurotransmission',
 'explanation': 'Correct Answer: B. It exports 3 Na+ ions out of the cell and imports 2 K+ ions into the cell per ATP '
                'molecule hydrolyzed, generating a net outward current that contributes directly (-3 to -5 mV) to '
                'membrane hyperpolarization.\n'
                '\n'
                'The Na+/K+-ATPase is an electrogenic P-type ATPase that consumes roughly 50-70% of total neuronal '
                'ATP. With each ATP hydrolyzed, it pumps 3 Na+ ions OUT of the intracellular space and 2 K+ ions IN. '
                'Because 3 positive charges leave while only 2 positive charges enter, the pump creates a net outward '
                'positive current (net loss of 1 positive charge per cycle), making the inside of the membrane '
                'slightly more negative (-3 to -5 mV hyperpolarizing contribution). Its principal role is maintaining '
                'the low intracellular Na+ and high intracellular K+ gradients necessary for action potentials and '
                'secondary active transport.\n'
                '\n'
                '• Option A is incorrect: It reverses the stoichiometry (it is 3 Na+ out, 2 K+ in, not vice versa).\n'
                '• Option C is incorrect: The pump is electrogenic, not electrically neutral.\n'
                '• Option D is incorrect: The Na+/Ca2+ exchanger (NCX) moves Na+ down its gradient to export Ca2+; it '
                'does not consume ATP directly.\n'
                '• Option E is incorrect: The Na+/K+ pump is distributed throughout the entire neuronal axolemma, '
                'soma, and glia, especially clustered at nodes of Ranvier.',
 'id': 'IH_Q060',
 'options': [{'is_correct': False,
              'text': 'It exports 2 Na+ ions and imports 3 K+ ions per ATP, producing a net positive inward current'},
             {'is_correct': True,
              'text': 'It exports 3 Na+ ions out of the cell and imports 2 K+ ions into the cell per ATP molecule '
                      'hydrolyzed, generating a net outward current that contributes directly (-3 to -5 mV) to '
                      'membrane hyperpolarization'},
             {'is_correct': False,
              'text': 'It transports equal numbers of Na+ and K+ ions, having no net effect on membrane charge'},
             {'is_correct': False, 'text': 'It moves Na+ down its concentration gradient to pump Ca2+ out of the cell'},
             {'is_correct': False, 'text': 'It is localized exclusively to the postsynaptic dendritic spine density'}],
 'question_number': 60,
 'stem': 'The electrogenic Na+/K+-ATPase pump is vital for maintaining resting neuronal membrane potential and '
         'cellular volume. Which of the following statements correctly describes the stoichiometry and direct '
         'electrophysiological effect of this pump?'},
])

questions_section1.extend([
    {'category': 'In House: Neurotransmission',
 'explanation': 'Correct Answer: B. Pinching off (scission) of clathrin-coated endocytic vesicles from the presynaptic '
                'plasma membrane during synaptic vesicle recycling.\n'
                '\n'
                'Following neurotransmitter exocytosis, the presynaptic terminal must rapidly recycle vesicular '
                'membrane components to sustain high-frequency transmission. Vesicular proteins are retrieved via '
                'clathrin-mediated endocytosis. Clathrin coats assemble around invaginating membranes, forming coated '
                'pits. Dynamin, a large mechanochemical GTPase, forms a polymeric collar around the neck of the '
                "invaginating vesicle and hydrolyzes GTP to pinch off ('scission') the vesicle from the plasma "
                'membrane. Inhibiting dynamin leads to a massive accumulation of unpinched, invaginated coated pits at '
                'the axolemma and rapid depletion of the readily releasable vesicle pool.\n'
                '\n'
                '• Option A is incorrect: Synaptotagmin Ca2+ sensing and exocytosis occur before endocytic retrieval.\n'
                '• Option C is incorrect: SNARE-mediated docking precedes membrane fusion.\n'
                '• Option D is incorrect: The vacuolar H+-ATPase acidifies the recycled vesicle to provide the '
                'electrochemical proton gradient driving neurotransmitter loading.\n'
                '• Option E is incorrect: Microtubular transport is driven by kinesin (anterograde) and dynein '
                '(retrograde), not dynamin.',
 'id': 'IH_Q061',
 'options': [{'is_correct': False, 'text': 'Vesicular exocytosis triggered by synaptotagmin'},
             {'is_correct': True,
              'text': 'Pinching off (scission) of clathrin-coated endocytic vesicles from the presynaptic plasma '
                      'membrane during synaptic vesicle recycling'},
             {'is_correct': False, 'text': 'Docking of vesicles via syntaxin and synaptobrevin'},
             {'is_correct': False, 'text': 'Proton pumping by vesicular V-ATPase'},
             {'is_correct': False, 'text': 'Axonal transport of mitochondria along microtubules'}],
 'question_number': 61,
 'stem': 'A neurobiology researcher uses a cell-permeable peptide that selectively inhibits the GTPase activity of '
         'dynamin in cultured cortical neurons. Following high-frequency electrical stimulation of the neurons, which '
         'of the following processes will be blocked at the presynaptic nerve terminal?'},
    {'category': 'In House: Neurotransmission',
 'explanation': 'Correct Answer: B. Substrate displacement of monoamines from vesicular monoamine transporter 2 '
                '(VMAT2) into the cytoplasm, followed by reverse transport of monoamines through DAT and NET into the '
                'synaptic cleft.\n'
                '\n'
                'Amphetamines exert a potent, multi-pronged sympathomimetic effect through non-vesicular release: (1) '
                'They enter presynaptic terminals via dopamine (DAT) and norepinephrine (NET) transporters, (2) They '
                'inhibit and disrupt the pH gradient of vesicular monoamine transporter 2 (VMAT2), causing '
                'displacement and leakage of stored dopamine and norepinephrine from synaptic vesicles into the '
                'axoplasm, (3) They inhibit monoamine oxidase (MAO), preventing intraneuronal breakdown, and (4) They '
                'reverse the transport direction of DAT and NET (via phosphorylation), pumping free cytosolic '
                'monoamines backwards OUT of the terminal into the synaptic cleft independently of action potentials. '
                'In contrast, cocaine simply blocks DAT/NET/SERT reuptake.\n'
                '\n'
                '• Option A is incorrect: Amphetamine does not act as a direct receptor agonist.\n'
                '• Option C is incorrect: Entacapone and tolcapone inhibit COMT, not amphetamine.\n'
                '• Option D is incorrect: Amphetamine release is non-exocytic and Ca2+-independent.\n'
                '• Option E is incorrect: Sympathetic postganglionic terminals release norepinephrine, not '
                'acetylcholine (except sweat glands).',
 'id': 'IH_Q062',
 'options': [{'is_correct': False, 'text': 'Direct agonism at postsynaptic adrenergic and dopamine receptors'},
             {'is_correct': True,
              'text': 'Substrate displacement of monoamines from vesicular monoamine transporter 2 (VMAT2) into the '
                      'cytoplasm, followed by reverse transport of monoamines through DAT and NET into the synaptic '
                      'cleft'},
             {'is_correct': False, 'text': 'Irreversible suicide inhibition of catechol-O-methyltransferase (COMT)'},
             {'is_correct': False, 'text': 'Blocking potassium channels to cause prolonged presynaptic calcium influx'},
             {'is_correct': False,
              'text': 'Stimulating acetylcholine synthesis in postganglionic sympathetic terminals'}],
 'question_number': 62,
 'stem': 'A 19-year-old college student presents to the emergency department with severe agitation, hyperthermia '
         '(104.2°F / 40.1°C), hypertension (190/110 mm Hg), tachycardia (140 bpm), dilated pupils (mydriasis), '
         'diaphoresis, and paranoia after consuming a party drug. Laboratory testing confirms acute amphetamine '
         'intoxication. What is the cellular mechanism by which amphetamines cause massive release of monoamines '
         '(dopamine and norepinephrine) into the synaptic cleft?'},
    {'category': 'In House: CNS Anatomy & Glia',
 'explanation': 'Correct Answer: A. Inward-rectifying potassium (Kir4.1) channels on astrocyte membranes and gap '
                'junctions (connexin 43) connecting astrocytes.\n'
                '\n'
                'During intense neuronal activity, K+ efflux into the narrow extracellular space threatens to '
                "depolarize resting membrane potentials. Astrocytes perform 'spatial potassium buffering': (1) "
                'Astrocytes express high levels of inwardly rectifying potassium channels (Kir4.1), which take up '
                'excess K+ from regions of high extracellular concentration; (2) Astrocytes are extensively coupled to '
                'one another via gap junctions composed of Connexin 43, forming a vast functional syncytium; (3) The '
                'accumulated K+ is rapidly redistributed through the syncytium and extruded into distant regions with '
                'lower K+ concentrations (e.g., around cerebral blood vessels). Loss-of-function mutations in Kir4.1 '
                'cause EAST syndrome (epilepsy, ataxia, sensorineural deafness, and tubulopathy).\n'
                '\n'
                '• Option B is incorrect: Astrocytes do not fire sodium action potentials or use desmosomes for '
                'buffering.\n'
                '• Option C is incorrect: Claudin-5 forms tight junctions between endothelial cells of the BBB.\n'
                '• Option D is incorrect: L-type calcium channels do not clear potassium.\n'
                '• Option E is incorrect: Aquaporin-4 (not AQP1) is localized to astrocytic end-feet for water '
                'homeostasis and glymphatics.',
 'id': 'IH_Q063',
 'options': [{'is_correct': True,
              'text': 'Inward-rectifying potassium (Kir4.1) channels on astrocyte membranes and gap junctions '
                      '(connexin 43) connecting astrocytes'},
             {'is_correct': False, 'text': 'Voltage-gated sodium channels and desmosomes'},
             {'is_correct': False, 'text': 'Ligand-gated chloride channels and tight junctions (claudin 5)'},
             {'is_correct': False, 'text': 'L-type calcium channels and hemidesmosomes'},
             {'is_correct': False, 'text': 'Aquaporin-1 channels and focal adhesions'}],
 'question_number': 63,
 'stem': 'During repetitive, high-frequency neuronal firing in the hippocampus, local extracellular potassium '
         'concentration rises from 3 mM to over 10 mM, which would depolarize neighboring neurons and trigger '
         'unconstrained seizure activity if left uncorrected. Astrocytes rapidly clear this excess extracellular K+ '
         'and disperse it across an interconnected astrocytic syncytium. What specialized channels and intercellular '
         "junctions mediate this astrocytic 'spatial potassium buffering'?"},
    {'category': 'In House: CNS Anatomy & Glia',
 'explanation': 'Correct Answer: B. Glial Fibrillary Acidic Protein (GFAP).\n'
                '\n'
                'In response to any central nervous system injury (ischemia, trauma, infection, neurodegeneration, or '
                'surgical margins), astrocytes undergo reactive astrogliosis. This process involves cellular '
                'hypertrophy, proliferation, and dramatic upregulation of Glial Fibrillary Acidic Protein (GFAP), a '
                'class III intermediate filament unique to mature astrocytes and ependymal cells. Reactive astrocytes '
                'extend dense overlapping processes to wall off the injury site and form a permanent physical and '
                "chemical barrier known as the 'glial scar'. GFAP is also a diagnostic immunohistochemical marker for "
                'astrocytic tumors (e.g., pilocytic astrocytoma, glioblastoma).\n'
                '\n'
                '• Option A is incorrect: Desmin is an intermediate filament marker for muscle cells.\n'
                '• Option C is incorrect: Vimentin is present in mesenchymal cells and immature glia, but GFAP is the '
                'specific marker for mature astrocytes.\n'
                '• Option D is incorrect: Cytokeratins are intermediate filaments of epithelial cells.\n'
                '• Option E is incorrect: Neurofilaments are the intermediate filaments of neurons.',
 'id': 'IH_Q064',
 'options': [{'is_correct': False, 'text': 'Desmin'},
             {'is_correct': True, 'text': 'Glial Fibrillary Acidic Protein (GFAP)'},
             {'is_correct': False, 'text': 'Vimentin exclusively'},
             {'is_correct': False, 'text': 'Cytokeratin'},
             {'is_correct': False, 'text': 'Neurofilament light chain'}],
 'question_number': 64,
 'stem': 'A 58-year-old woman undergoes resection of a brain tumor. Histopathological examination of the surrounding '
         'non-neoplastic brain tissue reveals extensive astrogliosis (reactive gliosis) characterized by hypertrophy '
         'of astrocytic cell bodies and thick, elongated cytoplasmic processes packed with intermediate filaments. '
         'Immunohistochemical staining confirms robust upregulation of which intermediate filament protein, which '
         'serves as a definitive biomarker for astrocytes?'},
    {'category': 'In House: CNS Anatomy',
 'explanation': 'Correct Answer: B. Carrier-mediated transport via the Large Neutral Amino Acid Transporter 1 (LAT1).\n'
                '\n'
                'The blood-brain barrier lacks fenestrations and has tight junctions, preventing polar monoamines like '
                'dopamine (which has a positive charge at physiological pH and lacks lipid solubility) from entering '
                'the brain. Levodopa (L-DOPA), the immediate amino acid precursor of dopamine, is recognized as a '
                'substrate by the Large Neutral Amino Acid Transporter 1 (LAT1, SLC7A5) expressed on both luminal and '
                'abluminal membranes of brain capillary endothelial cells. LAT1 transports L-DOPA into the brain via '
                'facilitated diffusion, where central DOPA decarboxylase converts it into dopamine. High-protein meals '
                "compete for LAT1 and can decrease L-DOPA absorption ('on-off' phenomenon).\n"
                '\n'
                '• Option A is incorrect: L-DOPA is polar and cannot cross by passive simple diffusion.\n'
                '• Option C is incorrect: Transferrin receptor mediates iron uptake, not L-DOPA.\n'
                '• Option D is incorrect: Pericytes do not transport L-DOPA by retrograde pinocytosis.\n'
                '• Option E is incorrect: Cerebral capillary endothelial cells lack fenestrations.',
 'id': 'IH_Q065',
 'options': [{'is_correct': False, 'text': 'Passive non-ionic diffusion through endothelial lipid membranes'},
             {'is_correct': True,
              'text': 'Carrier-mediated transport via the Large Neutral Amino Acid Transporter 1 (LAT1)'},
             {'is_correct': False, 'text': 'Receptor-mediated endocytosis via the transferrin receptor'},
             {'is_correct': False, 'text': 'Active retrograde pinocytosis through pericytes'},
             {'is_correct': False, 'text': 'Convective bulk flow through endothelial fenestrations'}],
 'question_number': 65,
 'stem': 'A 65-year-old man with Parkinson disease is prescribed oral levodopa (L-DOPA) combined with carbidopa. Plain '
         'dopamine cannot be administered systemically because it fails to cross the blood-brain barrier. How does '
         'L-DOPA successfully cross the capillary endothelial cells of the blood-brain barrier into the cerebral '
         'parenchyma?'},
    {'category': 'In House: Ventricular System & CSF',
 'explanation': 'Correct Answer: A. Head of the caudate nucleus.\n'
                '\n'
                'The anterior (frontal) horn of the lateral ventricle is bounded by: (1) Medially: the vertical septum '
                'pellucidum; (2) Superiorly and anteriorly (roof and anterior wall): the genu and body of the corpus '
                'callosum; (3) Laterally: the prominent rounded head of the caudate nucleus. In Huntington disease, '
                'bilateral atrophy of the caudate head removes this normal lateral convexity, resulting in '
                'characteristic box-car / squared-off enlargement of the frontal horns on MRI/CT.\n'
                '\n'
                '• Option B is incorrect: Globus pallidus lies lateral to the internal capsule, deep within the '
                'hemispheric white matter.\n'
                '• Option C is incorrect: The hippocampus bulges into the floor and medial wall of the INFERIOR '
                '(temporal) horn of the lateral ventricle.\n'
                '• Option D is incorrect: The putamen lies lateral to the internal capsule and globus pallidus.\n'
                '• Option E is incorrect: The anterior commissure lies at the rostral boundary of the 3rd ventricle.',
 'id': 'IH_Q066',
 'options': [{'is_correct': True, 'text': 'Head of the caudate nucleus'},
             {'is_correct': False, 'text': 'Globus pallidus'},
             {'is_correct': False, 'text': 'Hippocampus'},
             {'is_correct': False, 'text': 'Putamen'},
             {'is_correct': False, 'text': 'Anterior commissure'}],
 'question_number': 66,
 'stem': 'A radiologist is reviewing an axial T2-weighted MRI of the brain and pointing out the anatomical boundaries '
         'of the lateral ventricles to a medical student. What structure forms the curved lateral wall of the anterior '
         '(frontal) horn of the lateral ventricle, bulging into the ventricular lumen?'},
    {'category': 'In House: Ventricular System & CSF',
 'explanation': 'Correct Answer: A. Infundibulum (pituitary stalk) and tuber cinereum.\n'
                '\n'
                'The third ventricle is a narrow, slit-like cavity situated in the midline of the diencephalon between '
                'the two thalami. Its floor, moving anterior to posterior, consists of: the optic chiasm, the '
                'infundibular recess (giving rise to the pituitary stalk/infundibulum), the tuber cinereum, the paired '
                'mammillary bodies, and the posterior perforated substance extending to the midbrain tegmentum. During '
                'endoscopic third ventriculostomy (ETV), the surgeon perforates the thin, translucent floor of the '
                'third ventricle between the infundibular recess and the mammillary bodies into the '
                'prepontine/interpeduncular cistern to bypass aqueductal stenosis.\n'
                '\n'
                '• Option B is incorrect: The pineal gland is attached to the posterior wall/epithalamus of the 3rd '
                'ventricle above the posterior commissure.\n'
                '• Option C is incorrect: Colloid cysts are pathological cysts located at the roof near the foramen of '
                'Monro.\n'
                '• Option D is incorrect: Posterior commissure lies on the posterior wall.\n'
                '• Option E is incorrect: Facial colliculus is located in the rhomboid fossa of the 4th ventricle.',
 'id': 'IH_Q067',
 'options': [{'is_correct': True, 'text': 'Infundibulum (pituitary stalk) and tuber cinereum'},
             {'is_correct': False, 'text': 'Pineal gland'},
             {'is_correct': False, 'text': 'Colloid cyst cavity'},
             {'is_correct': False, 'text': 'Posterior commissure'},
             {'is_correct': False, 'text': 'Facial colliculus'}],
 'question_number': 67,
 'stem': 'During a neurosurgery case involving endoscopic third ventriculostomy (ETV), the surgeon navigates an '
         'endoscope into the third ventricle. On the floor of the third ventricle, which of the following midline '
         'neuroendocrine structures serves as an essential anatomical landmark situated immediately posterior to the '
         'optic chiasm and optic recess?'},
    {'category': 'In House: Ventricular System & CSF',
 'explanation': 'Correct Answer: B. Abducens nerve (CN VI) motor nucleus looped internally by motor fibers of the '
                'facial nerve (CN VII).\n'
                '\n'
                'The facial colliculus is a prominent landmark on the dorsal surface of the pons in the floor of the '
                'fourth ventricle. It is formed by the underlying abducens (CN VI) nucleus, which is encircled '
                'dorsally by axons of the facial motor (CN VII) nucleus (the internal genu of the facial nerve) before '
                'they exit anterolaterally. A lesion at the facial colliculus (e.g., pontine glioma, infarction, or MS '
                'plaque) produces a combined ipsilateral lateral gaze paralysis (CN VI palsy) and complete ipsilateral '
                "lower motor neuron facial paralysis (CN VII Bell's-type palsy).\n"
                '\n'
                '• Option A is incorrect: It reverses the nucleus and the looping fibers.\n'
                '• Option C is incorrect: CN IV exits the dorsal midbrain beneath the inferior colliculi.\n'
                '• Option D is incorrect: The hypoglossal trigone lies inferiorly in the medullary portion of the '
                'rhomboid fossa.\n'
                '• Option E is incorrect: Trigeminal motor nucleus is located in the mid-pons and does not form a '
                'collicular bulge in the 4th ventricle.',
 'id': 'IH_Q068',
 'options': [{'is_correct': False,
              'text': 'Facial nerve (CN VII) motor nucleus looped by abducens nerve (CN VI) fibers'},
             {'is_correct': True,
              'text': 'Abducens nerve (CN VI) motor nucleus looped internally by motor fibers of the facial nerve (CN '
                      'VII)'},
             {'is_correct': False,
              'text': 'Trochlear nerve (CN IV) nucleus looped by oculomotor nerve (CN III) fibers'},
             {'is_correct': False, 'text': 'Hypoglossal nerve (CN XII) nucleus looped by the solitary tract'},
             {'is_correct': False,
              'text': 'Trigeminal motor nucleus looped by sensory fibers of the spinal trigeminal tract'}],
 'question_number': 68,
 'stem': 'On the floor of the fourth ventricle (rhomboid fossa), a distinct round prominence known as the facial '
         'colliculus is visible in the medial pontine tegmentum. Which underlying cranial nerve motor nucleus and '
         'axonal loop form this bulge?'},
    {'category': 'In House: CNS Development & Spine',
 'explanation': 'Correct Answer: B. The syrinx initially destroys decussating second-order spinothalamic fibers in the '
                'anterior white commissure, and subsequent lateral extension destroys anterior horn alpha motor '
                'neurons.\n'
                '\n'
                'Syringomyelia begins as a cystic longitudinal cavity (syrinx) centered near the central canal of the '
                'spinal cord (most frequently C2-T1). (1) Sensory dissociation: The expanding syrinx first compresses '
                'and transects the second-order nociceptive axons of the anterolateral system (ALS) as they decussate '
                "across the anterior white commissure. This produces a bilateral, 'cape-like' loss of pain and "
                'temperature over the corresponding dermatomes, while light touch and dorsal column '
                'vibration/proprioception remain spared. (2) LMN weakness: As the syrinx enlarges radially and '
                'laterally, it directly invades and destroys the ventral (anterior) gray horns, destroying alpha motor '
                'neurons and producing lower motor neuron signs (flaccid paralysis, muscle atrophy, fasciculations, '
                'and areflexia) in the upper extremities.\n'
                '\n'
                '• Option A is incorrect: Posterior columns lie dorsal to the central canal and are spared until late; '
                'the syrinx does not reach the paravertebral sympathetic chain.\n'
                '• Option C is incorrect: DRGs are outside the spinal cord in the intervertebral foramina.\n'
                '• Option D is incorrect: Syrinx is within the spinal cord parenchyma, not compressing cerebellar '
                'arteries.\n'
                '• Option E is incorrect: Damage to anterior horn cells (gray matter) produces LMN signs; damage to '
                'corticospinal tracts (white matter) would produce spastic paraparesis below the lesion (UMN signs).',
 'id': 'IH_Q069',
 'options': [{'is_correct': False,
              'text': 'The cavity initially compresses the posterior columns, then extends laterally into the '
                      'sympathetic chain'},
             {'is_correct': True,
              'text': 'The syrinx initially destroys decussating second-order spinothalamic fibers in the anterior '
                      'white commissure, and subsequent lateral extension destroys anterior horn alpha motor neurons'},
             {'is_correct': False,
              'text': 'The syrinx causes selective demyelination of dorsal root ganglia, sparing ventral roots'},
             {'is_correct': False,
              'text': 'The fluid pressure blocks cerebrospinal fluid flow through the posterior inferior cerebellar '
                      'artery'},
             {'is_correct': False,
              'text': 'The syrinx damages descending corticospinal fibers without affecting spinal gray matter'}],
 'question_number': 69,
 'stem': 'A 32-year-old woman with a Chiari I malformation presents with progressive weakness and muscle wasting in '
         'both hands, accompanied by painless burns on her fingers from cooking. Neurological examination reveals '
         'bilateral loss of pain and temperature sensation across her upper chest, neck, and arms, with preserved '
         'light touch, vibration, and joint position sense. In her hands, there is marked intrinsic muscle atrophy, '
         'fasciculations, and bilateral absent triceps and biceps reflexes. How does the pathological expansion of a '
         'cervical syringomyelia produce both sensory dissociation and lower motor neuron weakness in the hands?'},
    {'category': 'In House: Ventricular System & CSF',
 'explanation': 'Correct Answer: B. Fibrosis and obliteration of the arachnoid granulations (villi) by purulent '
                'meningeal exudate, preventing CSF resorption into the dural venous sinuses.\n'
                '\n'
                'Communicating hydrocephalus occurs when CSF flow through the ventricular channels is completely '
                'unobstructed, but its absorption into the venous system is impaired. Following bacterial meningitis '
                'or subarachnoid hemorrhage, inflammatory exudate, debris, and red blood cells enter the subarachnoid '
                'space and arachnoid granulations (villi). Subsequent chronic organizing fibrosis (obliterative '
                'arachnoiditis) clogs the microscopic arachnoid villi, preventing CSF resorption into the superior '
                'sagittal sinus. Because CSF continues to be produced at ~500 mL/day, fluid accumulates upstream, '
                'symmetrically dilating all four ventricles (lateral, 3rd, and 4th) under elevated intracranial '
                'pressure.\n'
                '\n'
                '• Option A is incorrect: Aqueductal stenosis spares the 4th ventricle (non-communicating '
                'hydrocephalus).\n'
                '• Option C is incorrect: Choroid plexus papilloma is a rare childhood tumor; post-meningitis '
                'hydrocephalus is absorptive failure, not hypersecretion.\n'
                '• Option D is incorrect: Tonsillar herniation is a consequence of increased ICP, not the primary '
                'cause of hydrocephalus.\n'
                '• Option E is incorrect: Atresia of foramina of Luschka/Magendie is congenital Dandy-Walker '
                'malformation.',
 'id': 'IH_Q070',
 'options': [{'is_correct': False, 'text': 'Aqueductal stenosis secondary to ependymal scarring'},
             {'is_correct': True,
              'text': 'Fibrosis and obliteration of the arachnoid granulations (villi) by purulent meningeal exudate, '
                      'preventing CSF resorption into the dural venous sinuses'},
             {'is_correct': False, 'text': 'Choroid plexus papilloma causing massive CSF hypersecretion'},
             {'is_correct': False, 'text': 'Herniation of the cerebellar tonsils obstructing the foramen magnum'},
             {'is_correct': False, 'text': 'Atresia of the foramina of Luschka and Magendie'}],
 'question_number': 70,
 'stem': 'A 44-year-old man recovers from a severe episode of pneumococcal meningitis. Four months later, he presents '
         'with progressive headaches, lethargy, cognitive slowing, and bilateral papilledema. Brain MRI reveals '
         'marked, symmetrical dilation of all four cerebral ventricles (lateral, third, and fourth ventricles) without '
         'any intraventricular mass or focal structural obstruction. What is the pathological mechanism responsible '
         'for this communicating hydrocephalus?'},
    {'category': 'In House: Ventricular System & CSF',
 'explanation': 'Correct Answer: B. CPP = Mean Arterial Pressure (MAP) - Intracranial Pressure (ICP); Target 60 to 70 '
                'mm Hg.\n'
                '\n'
                'Cerebral Perfusion Pressure (CPP) represents the net pressure gradient driving blood flow and oxygen '
                'delivery to the cerebral capillary bed. It is defined mathematically as: CPP = Mean Arterial Pressure '
                '(MAP) - Intracranial Pressure (ICP) [where MAP = DBP + 1/3(SBP - DBP)]. In healthy individuals, '
                'autoregulation maintains constant cerebral blood flow across a CPP range of 50–150 mm Hg. In '
                'neurotrauma or elevated ICP, CPP < 60 mm Hg leads to critical cerebral hypoperfusion, ischemia, and '
                'worsening cytotoxic edema, whereas CPP > 70 mm Hg can induce hyperperfusion and ARDS. Neurocritical '
                'care guidelines target CPP between 60 and 70 mm Hg.\n'
                '\n'
                '• Options A, C, D, and E represent incorrect formulas and physiological targets.',
 'id': 'IH_Q071',
 'options': [{'is_correct': False, 'text': 'CPP = Systolic BP - ICP; Target > 120 mm Hg'},
             {'is_correct': True,
              'text': 'CPP = Mean Arterial Pressure (MAP) - Intracranial Pressure (ICP); Target 60 to 70 mm Hg'},
             {'is_correct': False, 'text': 'CPP = Diastolic BP + Central Venous Pressure; Target 30 to 40 mm Hg'},
             {'is_correct': False, 'text': 'CPP = MAP / ICP; Target > 4.0'},
             {'is_correct': False, 'text': 'CPP = Pulse Pressure * Respiratory Rate; Target 80 to 90 mm Hg'}],
 'question_number': 71,
 'stem': 'In the neurointensive care management of patients with severe traumatic brain injury and elevated '
         'intracranial pressure (ICP), cerebral perfusion pressure (CPP) must be rigorously maintained to prevent '
         'secondary ischemic injury. How is cerebral perfusion pressure calculated, and what is the minimum '
         'recommended CPP target in adults?'},
    {'category': 'In House: CNS Development & Genetics',
 'explanation': 'Correct Answer: A. Tay-Sachs disease, Gaucher disease, and Niemann-Pick disease.\n'
                '\n'
                'Due to founder effects and historical population bottlenecks, individuals of Ashkenazi Jewish '
                'ancestry have a significantly increased carrier frequency for several severe autosomal recessive '
                'lysosomal storage disorders: (1) Tay-Sachs disease (carrier rate ~1 in 27-30; hexosaminidase A '
                'deficiency), (2) Gaucher disease (carrier rate ~1 in 15-18; glucocerebrosidase deficiency), (3) '
                'Niemann-Pick disease type A (carrier rate ~1 in 90; sphingomyelinase deficiency), along with Bloom '
                'syndrome, Canavan disease, and Fanconi anemia. Preconception carrier screening is standard of care to '
                'identify at-risk couples.\n'
                '\n'
                '• Option B is incorrect: Huntington and Marfan are autosomal dominant; Fragile X is X-linked triplet '
                'repeat.\n'
                '• Option C is incorrect: DMD, Hemophilia A, and Fabry are X-linked recessive disorders.\n'
                '• Option D is incorrect: NF1, TSC, and VHL are autosomal dominant tumor suppressor syndromes.\n'
                '• Option E is incorrect: These are trinucleotide repeat expansion disorders.',
 'id': 'IH_Q072',
 'options': [{'is_correct': True, 'text': 'Tay-Sachs disease, Gaucher disease, and Niemann-Pick disease'},
             {'is_correct': False, 'text': 'Huntington disease, Fragile X syndrome, and Marfan syndrome'},
             {'is_correct': False, 'text': 'Duchenne muscular dystrophy, Hemophilia A, and Fabry disease'},
             {'is_correct': False,
              'text': 'Neurofibromatosis type 1, Tuberous sclerosis, and Von Hippel-Lindau disease'},
             {'is_correct': False, 'text': 'Myotonic dystrophy, Friedrich ataxia, and Spinocerebellar ataxia'}],
 'question_number': 72,
 'stem': 'A 26-year-old woman of Ashkenazi Jewish descent and her husband are planning their first pregnancy and '
         'consult a medical geneticist for preconception carrier screening. The genetic counselor orders a targeted '
         'screening panel for several autosomal recessive sphingolipidoses common in this population. For which of the '
         'following combinations of disorders should carrier status be assessed?'},
    {'category': 'In House: CNS Development & Biochemistry',
 'explanation': 'Correct Answer: A. Methionine synthase.\n'
                '\n'
                'Folate and vitamin B12 metabolism are tightly intertwined through Methionine Synthase: '
                '5-methyltetrahydrofolate (5-MTHF) transfers its methyl group to vitamin B12 (cobalamin), forming '
                'methylcobalamin, which then transfers the methyl group to homocysteine to synthesize methionine. '
                'Methionine is then activated to S-adenosylmethionine (SAM), the universal methyl donor required for '
                'DNA methylation and epigenetic regulation during embryogenesis. Concurrently, tetrahydrofolate (THF) '
                'is regenerated to enter purine and thymidylate synthesis for rapid neural progenitor mitosis. In '
                "vitamin B12 deficiency, folate is trapped as 5-MTHF ('folate trap'), causing secondary functional "
                'folate deficiency and homocysteine accumulation.\n'
                '\n'
                '• Option B is incorrect: Cystathionine β-synthase converts homocysteine to cystathionine and requires '
                'Vitamin B6 (pyridoxine).\n'
                '• Option C is incorrect: Dihydrofolate reductase converts DHF to THF using NADPH (inhibited by '
                'methotrexate).\n'
                '• Option D is incorrect: Thymidylate synthase converts dUMP to dTMP using 5,10-methylene-THF '
                '(inhibited by 5-fluorouracil).\n'
                '• Option E is incorrect: SHMT reversibly interconverts glycine and serine.',
 'id': 'IH_Q073',
 'options': [{'is_correct': True, 'text': 'Methionine synthase'},
             {'is_correct': False, 'text': 'Cystathionine beta-synthase'},
             {'is_correct': False, 'text': 'Dihydrofolate reductase'},
             {'is_correct': False, 'text': 'Thymidylate synthase'},
             {'is_correct': False, 'text': 'Serine hydroxymethyltransferase'}],
 'question_number': 73,
 'stem': 'A biochemist is analyzing maternal blood samples to evaluate the biochemical pathway linking folate '
         'metabolism to neural tube defect prevention. In the folate cycle, 5,10-methylenetetrahydrofolate is reduced '
         'by methylenetetrahydrofolate reductase (MTHFR) to 5-methyltetrahydrofolate (5-MTHF). Which subsequent '
         'reaction transfers the methyl group from 5-MTHF to homocysteine to generate methionine, requiring Vitamin '
         'B12 as a mandatory cofactor?'},
    {'category': 'In House: CNS Development & Milestones',
 'explanation': 'Correct Answer: A. By 4 to 6 months of age, due to descending inhibition from maturing frontal '
                'cerebral cortical circuits and myelination of the corticospinal tracts.\n'
                '\n'
                'Primitive reflexes (e.g., Moro, rooting, palmar grasp, sucking) are primitive brainstem and spinal '
                'cord motor patterns present at birth. As postnatal CNS maturation proceeds, rapid myelination of '
                'descending corticospinal tracts and development of frontal cortical inhibitory networks exert '
                'supraspinal control, suppressing these reflexes by roughly 4 to 6 months of age (the Babinski reflex '
                'may persist up to 12-24 months until walking is established). Re-emergence of primitive reflexes in '
                "an adult ('frontal release signs': grasp, snout, palmomental reflexes) signifies bilateral frontal "
                'lobe pathology or advanced neurodegeneration (e.g., frontotemporal dementia, Alzheimer disease).\n'
                '\n'
                '• Option B is incorrect: 2 weeks is far too early; primitive reflexes are robust throughout the first '
                'months.\n'
                '• Option C is incorrect: Fontanelles close at 12-18 months, but primitive reflexes disappear much '
                'earlier.\n'
                '• Option D is incorrect: Primitive reflexes disappear in normal adults; persistence or re-emergence '
                'is pathological.\n'
                '• Option E is incorrect: Spinal motor neurons do not degenerate in normal maturation.',
 'id': 'IH_Q074',
 'options': [{'is_correct': True,
              'text': 'By 4 to 6 months of age, due to descending inhibition from maturing frontal cerebral cortical '
                      'circuits and myelination of the corticospinal tracts'},
             {'is_correct': False, 'text': 'By 2 weeks of age, due to apoptosis of brainstem motor neurons'},
             {'is_correct': False, 'text': 'By 3 years of age, due to closure of the cranial sutures'},
             {'is_correct': False,
              'text': 'They normally persist throughout adult life as baseline defensive reflexes'},
             {'is_correct': False, 'text': 'By 12 months of age, due to loss of spinal motor neurons'}],
 'question_number': 74,
 'stem': 'A pediatrician examines a healthy 4-month-old infant. The Moro reflex (startle response to sudden head '
         'extension) and rooting reflex are easily elicited. By what age should these primitive infant reflexes '
         'disappear under normal neurodevelopmental conditions, and what neurological process accounts for their '
         'suppression?'},
    {'category': 'In House: Ventricular System & CSF',
 'explanation': 'Correct Answer: B. Shunt overdrainage causing intracranial hypotension, downward brain sag, and '
                'stretching of pain-sensitive meninges and bridging veins.\n'
                '\n'
                'Shunt overdrainage is a recognized complication of VP shunts when the valve siphon pressure is set '
                'too low. Excessive siphoning of CSF in the upright posture drops intracranial pressure below '
                'atmospheric pressure (intracranial hypotension / slit-ventricle syndrome). This loss of buoyant CSF '
                'support causes the brain to sag downward, exerting painful traction on pain-sensitive dural '
                'structures (producing classic orthostatic / postural headaches: worse upright, relieved supine). '
                'Furthermore, as the cerebral hemispheres collapse away from the calvarium, traction on delicate '
                'bridging veins can produce tearing, subdural hygromas, or chronic subdural hematomas. Management '
                'involves upgrading to a programmable anti-siphon valve.\n'
                '\n'
                '• Option A is incorrect: Shunt occlusion causes increased ICP with ventricular DILATION, headaches '
                'worse lying flat, and papilledema.\n'
                '• Option C is incorrect: Infection causes fever, meningismus, shunt erythema, and inflammatory CSF.\n'
                '• Option D is incorrect: Peritoneal pseudocyst impairs drainage, causing elevated ICP and shunt '
                'failure.\n'
                '• Option E is incorrect: Catheter malposition does not selectively cause postural orthostatic '
                'headaches and collapsed slit ventricles.',
 'id': 'IH_Q075',
 'options': [{'is_correct': False, 'text': 'Complete shunt occlusion leading to acute intraventricular hypertension'},
             {'is_correct': True,
              'text': 'Shunt overdrainage causing intracranial hypotension, downward brain sag, and stretching of '
                      'pain-sensitive meninges and bridging veins'},
             {'is_correct': False,
              'text': 'Bacterial colonization of the shunt with Propionibacterium acnes causing chronic ventriculitis'},
             {'is_correct': False, 'text': 'Peritoneal pseudocyst formation preventing abdominal CSF reabsorption'},
             {'is_correct': False, 'text': 'Malposition of the ventricular catheter into the third ventricle'}],
 'question_number': 75,
 'stem': 'A 3-year-old child with communicating hydrocephalus underwent placement of a ventriculoperitoneal (VP) shunt '
         '6 months ago. He is brought to the clinic because of severe, postural headaches that occur whenever he '
         'stands up or sits upright, and resolve completely within minutes of lying flat. His parents also note he has '
         'become irritable and vomits after prolonged upright activity. Brain MRI reveals bilateral slit-like '
         'collapsed lateral ventricles and small bilateral subdural fluid collections (subdural hygromas). What is the '
         'mechanism of his symptoms?'},
])

if __name__ == "__main__":
    print(f"Section 1 Question Count: {len(questions_section1)}")
    # Verify unique IDs
    ids = [q["id"] for q in questions_section1]
    assert len(ids) == len(set(ids)), "Duplicate IDs found!"
    print("All IDs unique and valid!")
