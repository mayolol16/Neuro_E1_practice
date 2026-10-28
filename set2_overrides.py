#!/usr/bin/env python3
"""
Meticulously audited option, stem, and explanation overrides for Neuro Exam 2 "Set 2" Bank (100 Qs).
Eliminates option length bias, asymmetric parentheses/punctuation, and giveaway phrases.
"""

SET2_OVERRIDES = {
    # Q1: Balance rod photoreceptor response options
    1: {
        'opts': {
            'A': "It depolarizes from its resting state and initiates axonal action potentials",
            'B': "It fires repetitive action potentials at a frequency proportional to luminance",
            'C': "It hyperpolarizes from its resting state and generates axonal action potentials",
            'D': "It maintains a constant resting membrane potential without changing polarization",
            'E': "It hyperpolarizes from its dark resting state without firing action potentials"
        }
    },
    # Q2: Balance retinal cell type names
    2: {
        'opts': {
            'A': "Retinal ganglion cells",
            'B': "Retinal bipolar cells",
            'C': "Rod photoreceptor cells",
            'D': "Cone photoreceptor cells",
            'E': "Müller glial support cells"
        }
    },
    # Q3: Balance optic nerve anatomy options
    3: {
        'opts': {
            'A': "The optic nerve is a peripheral cranial nerve surrounded by dense perineurium",
            'B': "Optic nerve sheath CSF drains freely into anterior chamber aqueous humor",
            'C': "The optic nerve sheath contains a subarachnoid space continuous with the brain",
            'D': "Optic nerve axons are myelinated by peripheral myelinating Schwann cells",
            'E': "The central retinal artery arises as a direct branch of the anterior cerebral"
        }
    },
    # Q6: Balance optic chiasm crossing options
    6: {
        'opts': {
            'A': "Temporal retinal fibers, which carry information from the nasal visual field",
            'B': "Nasal retinal fibers, which carry information from the temporal visual field",
            'C': "Central macular fibers, which project equally to both occipital hemispheres",
            'D': "Inferior retinal fibers, which loop through the temporal lobe Meyer pathway",
            'E': "Complete decussation occurs, with all retinal projections crossing midline"
        }
    },
    # Q8: Balance visual deficit descriptions
    8: {
        'opts': {
            'A': "Complete cortical blindness from primary striate cortex infarct",
            'B': "Complete homonymous hemianopia from geniculocalcarine disruption",
            'C': "Visual object agnosia from visual sensory association damage",
            'D': "Functional amblyopia from childhood binocular visual deprivation",
            'E': "Dense central scotoma from localized macular pathway infarction"
        }
    },
    # Q9: Remove giveaway parenthesis (Müller) and balance muscle names
    9: {
        'opts': {
            'A': "Levator palpebrae superioris muscle",
            'B': "Orbicularis oculi palpebral muscle",
            'C': "Frontalis anterior scalp muscle",
            'D': "Superior tarsal smooth muscle",
            'E': "Procerus nasal bridge muscle"
        }
    },
    # Q13: Remove giveaway parenthesis (Marcus Gunn) and balance pupillary defect options
    13: {
        'opts': {
            'A': "Efferent motor defect of the right oculomotor nerve",
            'B': "Efferent motor defect of the left oculomotor nerve",
            'C': "Afferent pupillary defect of the right optic nerve",
            'D': "Sympathetic pathway disruption of the right cervical chain",
            'E': "Bilateral dorsal midbrain pretectal pathway disruption"
        }
    },
    # Q18: Balance horizontal gaze palsy descriptions
    18: {
        'opts': {
            'A': "Both eyes deviate conjugately left with total inability to look right",
            'B': "Left eye cannot abduct on left gaze and right eye cannot adduct left",
            'C': "Right eye cannot move horizontally, and left eye can only abduct left",
            'D': "Both eyes retain completely normal horizontal gaze without nystagmus",
            'E': "Horizontal gaze is preserved, but all vertical gaze motions are lost"
        }
    },
    # Q20: Balance ocular movement terminology
    20: {
        'opts': {
            'A': "Saccadic eye movement",
            'B': "Smooth pursuit movement",
            'C': "Vergence ocular movement",
            'D': "Optokinetic nystagmus",
            'E': "Vestibulo-ocular reflex"
        }
    },
    # Q23: Balance Argyll Robertson pupil mechanisms
    23: {
        'opts': {
            'A': "Selective ischemia of bilateral optic nerve fibers carrying pupillomotor input",
            'B': "Apoptotic degeneration of parasympathetic preganglionic Edinger-Westphal cells",
            'C': "Postganglionic pupillomotor fiber degeneration within bilateral ciliary ganglia",
            'D': "Mechanical compression of superficial parasympathetic oculomotor nerve fibers",
            'E': "Pretectal area damage sparing descending cortical fibers for accommodation"
        }
    },
    # Q24: Balance visual perception mechanisms
    24: {
        'opts': {
            'A': "Peripheral retinal photoreceptor fatigue and bleaching",
            'B': "Cortical interpretation shaped by contextual perception",
            'C': "Selective congenital cone photopigment dysfunction",
            'D': "Primary visual striate cortex ischemic damage",
            'E': "Compression of macular fibers at the optic chiasm"
        }
    },
    # Q25: Balance aqueous humor flow sequences
    25: {
        'opts': {
            'A': "Ciliary body → anterior chamber → pupil → posterior chamber → episcleral veins",
            'B': "Ciliary body → vitreous body → posterior chamber → pupil → canal of Schlemm",
            'C': "Ciliary body → posterior chamber → pupil → trabecular meshwork → canal of Schlemm",
            'D': "Choroid plexus → vitreous cavity → posterior chamber → uveoscleral collector veins",
            'E': "Ciliary epithelium → posterior chamber → vitreous body → retinal venous plexus"
        }
    },
    # Q26: Remove giveaway parenthesis (WAGR) and balance genetics options
    26: {
        'opts': {
            'A': "RB1 mutation and retinoblastoma tumor",
            'B': "PAX6 mutation and hepatoblastoma tumor",
            'C': "HTT expansion and pediatric astrocytoma",
            'D': "ATP7B mutation and nephroblastoma tumor",
            'E': "PAX6 mutation and nephroblastoma tumor"
        }
    },
    # Q28: Balance retinopathy of prematurity pathophysiology options
    28: {
        'opts': {
            'A': "Trabecular meshwork hypoplasia causing elevated intraocular pressure",
            'B': "Oxidative cross-linking and hydration of crystalline lens proteins",
            'C': "Lipid-rich basophilic drusen deposition between Bruch membrane layers",
            'D': "Retinal vessel injury triggering VEGF-induced neovascular proliferation",
            'E': "Apoptotic degeneration of photoreceptors from oxygen radical exposure"
        }
    },
    # Q29: Balance diabetic retinopathy neovascularization options
    29: {
        'opts': {
            'A': "Ciliary epithelial hypersecretion elevating intraocular hydrostatic pressure",
            'B': "Capillary microangiopathy and retinal hypoxia driving VEGF neovascularization",
            'C': "Separation of the neurosensory retinal layer from choroidal blood supply",
            'D': "Extracellular lipid and protein accumulation beneath the retinal epithelium",
            'E': "Axoplasmic stasis from elevated intracranial pressure compressing the nerve"
        }
    },
    # Q32: Balance auditory hair cell anatomical locations
    32: {
        'opts': {
            'A': "Within the stria vascularis producing endolymph",
            'B': "Within the spiral ganglion of the cochlear nerve",
            'C': "Within the bony vestibule adjacent to the stapes",
            'D': "Within the organ of Corti on the basilar membrane",
            'E': "Within the secondary membrane of the round window"
        }
    },
    # Q36: Balance inner ear membrane names
    36: {
        'opts': {
            'A': "Gelatinous cupula",
            'B': "Otolithic membrane",
            'C': "Tectorial membrane",
            'D': "Basilar membrane",
            'E': "Vestibular membrane"
        }
    },
    # Q37: Remove giveaway parenthesis (otoconia) and balance otolithic gravity sensors
    37: {
        'opts': {
            'A': "Active motile contraction of outer sensory hair cell stereocilia",
            'B': "Endolymphatic displacement of the gelatinous crista ampullaris cupula",
            'C': "Temperature-dependent convection currents within the endolymph fluid",
            'D': "Traveling wave displacement of the tonotopically tuned basilar membrane",
            'E': "Heavy calcium carbonate otoconia embedding the gelatinous layer"
        }
    },
    # Q40: Balance doll's eye vestibulo-ocular reflex options
    40: {
        'opts': {
            'A': "Functional integrity of bilateral frontal eye field cortical centers",
            'B': "Functional integrity of primary visual striate occipital cortex",
            'C': "Functional integrity of temporal lobe auditory association pathways",
            'D': "Functional integrity of pontomedullary and midbrain brainstem circuits",
            'E': "Functional integrity of striatal and pallidal basal ganglia loops"
        }
    },
    # Q42: Balance vestibular projection tracts
    42: {
        'opts': {
            'A': "Medial longitudinal fasciculus pathway to the abducens nucleus",
            'B': "Medial vestibulospinal descending tract to cervical cord neurons",
            'C': "Lateral vestibulospinal descending tract to lumbar motor neurons",
            'D': "Vestibulocerebellar ascending pathway to the flocculonodular lobe",
            'E': "Vestibulothalamocortical pathway projecting to parietal cortex"
        }
    },
    # Q45: Balance UMN vs LMN definitions
    45: {
        'opts': {
            'A': "UMN axons exit the central nervous system to synapse on neuromuscular junctions",
            'B': "LMN cell bodies reside in the precentral gyrus and descend in the spinal cord",
            'C': "UMNs synapse on LMNs in the CNS, while LMNs exit the CNS to innervate muscle",
            'D': "Both classes of motor neurons extend axons into the peripheral nervous system",
            'E': "LMN cell bodies are confined strictly to the brainstem cranial nerve nuclei"
        }
    },
    # Q47: Balance motor cortical localization options
    47: {
        'opts': {
            'A': "Supplementary motor area or premotor cortex",
            'B': "Primary motor cortex in the precentral gyrus",
            'C': "Posterior limb of the internal capsule tract",
            'D': "Midline cerebellar vermis cortical region",
            'E': "Cervical spinal cord anterior gray horn"
        }
    },
    # Q50: Balance corticospinal lesion deficit options
    50: {
        'opts': {
            'A': "Left spastic weakness below the level of the lesion",
            'B': "Right flaccid weakness below the level of the lesion",
            'C': "Right spastic weakness below the level of the lesion",
            'D': "Bilateral flaccid weakness below the level of lesion",
            'E': "Left flaccid weakness below the level of the lesion"
        }
    },
    # Q51: Balance decorticate posturing anatomical levels
    51: {
        'opts': {
            'A': "Brainstem tegmentum at the level of the caudal pons",
            'B': "Brainstem tegmentum at the level of rostral medulla",
            'C': "Cervical spinal cord at the level of C5 segment",
            'D': "Midline cerebellar cortex in the posterior vermis",
            'E': "Cerebral hemisphere or tract above the red nucleus"
        }
    },
    # Q53: Balance rostral medulla corticobulbar deficit options
    53: {
        'opts': {
            'A': "Tongue deviates to the left with concurrent left facial droop",
            'B': "Tongue deviates to the left with completely normal facial tone",
            'C': "Tongue deviates to the right with concurrent right facial droop",
            'D': "Tongue deviates to the right with completely normal facial tone",
            'E': "Mandible deviates to the left with completely normal tongue tone"
        }
    },
    # Q54: Balance Bell palsy treatment descriptions
    54: {
        'opts': {
            'A': "Immediate surgical middle fossa facial nerve decompression",
            'B': "Oral corticosteroid therapy accompanied by eye lubrication",
            'C': "Close clinical observation without pharmacologic therapy",
            'D': "Targeted local botulinum toxin chemodenervation injections",
            'E': "Continuous intrathecal baclofen infusion pump placement"
        }
    },
    # Q55: Remove giveaway parenthesis (Ramsay Hunt) and balance viral etiology options
    55: {
        'opts': {
            'A': "Herpes simplex virus type 1 reactivation in geniculate ganglion",
            'B': "Borrelia burgdorferi spirochetal Lyme disease polyneuropathy",
            'C': "Varicella-zoster virus reactivation in the geniculate ganglion",
            'D': "Malignant external otitis pseudomonal skull base osteomyelitis",
            'E': "Destructive middle ear expanding squamous cell cholesteatoma"
        }
    },
    # Q57: Balance poliomyelitis spinal localization options
    57: {
        'opts': {
            'A': "Anterior gray horn lower motor neurons",
            'B': "Dorsal column sensory projection axons",
            'C': "Lateral corticospinal upper motor tracts",
            'D': "Primary sensory dorsal root ganglia cells",
            'E': "Spinothalamic anterolateral sensory tracts"
        }
    },
    # Q61: Remove giveaway explanatory clause from abducens nuclear lesion
    61: {
        'opts': {
            'A': "Conjugate right gaze palsy and ipsilateral right lower facial droop",
            'B': "Isolated left eye adduction deficit during attempted right gaze",
            'C': "Bilateral facial diplegia with preserved horizontal eye movements",
            'D': "Completely normal horizontal conjugate gaze with vertical nystagmus",
            'E': "Conjugate left gaze palsy and ipsilateral left complete facial palsy"
        }
    },
    # Q64: Remove giveaway parenthesis (CN V) and balance bilateral corticobulbar muscle options
    64: {
        'opts': {
            'A': "Lower facial muscles of expression",
            'B': "Muscles of mastication of the jaw",
            'C': "Extrinsic muscles of the tongue",
            'D': "Flexor muscles of the upper limb",
            'E': "Extensor muscles of the lower limb"
        }
    },
    # Q65: Balance hypothalamic portal regulation mechanisms
    65: {
        'opts': {
            'A': "Axons descend through the pituitary stalk to terminate directly in the anterior lobe",
            'B': "Nerve terminals secrete vasopressin directly into systemic inferior hypophyseal veins",
            'C': "Postganglionic autonomic axons establish direct synaptic junctions on endocrine cells",
            'D': "Releasing hormones enter primary capillary plexuses in the hypophyseal portal system",
            'E': "Sympathetic chain postganglionic fibers stimulate anterior pituitary hormone release"
        }
    },
    # Q67: Balance retinohypothalamic circadian tracts
    67: {
        'opts': {
            'A': "Retina to lateral geniculate nucleus to occipital cortex to pineal gland",
            'B': "Retina to midbrain pretectal area to bilateral Edinger-Westphal nuclei",
            'C': "Retina to suprachiasmatic nucleus to thoracic sympathetics to pineal gland",
            'D': "Retina to ventromedial hypothalamic nucleus to anterior pituitary gland",
            'E': "Retina to posterior mammillary bodies to epithalamic habenular nuclei"
        }
    },
    # Q71: Balance basal ganglia nuclear names
    71: {
        'opts': {
            'A': "Putamen and globus pallidus nuclei",
            'B': "Caudate nucleus and putamen nuclei",
            'C': "Globus pallidus and subthalamic nucleus",
            'D': "Substantia nigra and subthalamic nucleus",
            'E': "Motor thalamus and caudate nucleus"
        }
    },
    # Q76: Balance direct basal ganglia pathway options
    76: {
        'opts': {
            'A': "Striatum excites GPi, increasing thalamic inhibition and suppressing motor cortex drive",
            'B': "Striatum inhibits GPi, reducing thalamic inhibition and increasing motor cortex drive",
            'C': "Striatum excites GPe, suppressing subthalamic excitation and decreasing thalamic drive",
            'D': "Striatum inhibits GPe, increasing subthalamic excitation and decreasing thalamic drive",
            'E': "Subthalamus excites GPi, suppressing motor thalamic activity and reducing movement"
        }
    },
    # Q77: Balance indirect basal ganglia pathway options
    77: {
        'opts': {
            'A': "Striatum excites GPi, disinhibiting the motor thalamus and augmenting cortical motor activity",
            'B': "Striatum inhibits GPi directly, which disinhibits motor thalamus and initiates movements",
            'C': "Striatum excites GPe, disinhibiting the subthalamic nucleus and driving cortical output",
            'D': "Striatum projects directly to the ventral lateral thalamus to block cortical motor output",
            'E': "Striatum inhibits GPe, disinhibiting the subthalamic nucleus to increase GPi thalamic block"
        }
    },
    # Q78: Balance tardive dyskinesia pathophysiologic mechanisms
    78: {
        'opts': {
            'A': "Progressive apoptotic loss of dopaminergic neurons in the substantia nigra pars compacta",
            'B': "Extensive GABAergic medium spiny neuronal degeneration within the caudate and putamen",
            'C': "Upregulation and supersensitivity of postsynaptic striatal dopamine D2 receptors",
            'D': "Unopposed glutamatergic hyperactivation originating from the subthalamic nucleus of Luys",
            'E': "Excessive striatal muscarinic cholinergic interneuron excitability from dopamine loss"
        }
    },
    # Q81: Balance Parkinson-plus neurodegenerative disorders
    81: {
        'opts': {
            'A': "Huntington chorea disease",
            'B': "Progressive supranuclear palsy",
            'C': "Amyotrophic lateral sclerosis",
            'D': "Multiple system atrophy disorder",
            'E': "Severe essential tremor disorder"
        }
    },
    # Q85: Balance MAO inhibitor tyramine reaction options
    85: {
        'opts': {
            'A': "Massive serotonin accumulation from central 5-HT reuptake blockade",
            'B': "GABAergic hyperpolarization causing acute autonomic dysregulation",
            'C': "Postsynaptic D2 receptor blockade precipitating neuroleptic crisis",
            'D': "Dietary tyramine displacement of stored neuronal norepinephrine",
            'E': "Systemic muscarinic hyperstimulation from acetylcholinesterase block"
        }
    },
    # Q87: Balance benztropine clinical action descriptions
    87: {
        'opts': {
            'A': "It significantly improves gait bradykinesia and akinesia",
            'B': "It suppresses peak-dose levodopa-induced dyskinesias",
            'C': "It augments presynaptic striatal dopamine biosynthesis",
            'D': "It selectively and irreversibly inhibits central MAO-B",
            'E': "It improves resting tremor without reducing bradykinesia"
        }
    },
    # Q88: Balance shared neurodegenerative molecular mechanisms
    88: {
        'opts': {
            'A': "Cytotoxic hypersecretion of monoaminergic transmitters into synaptic clefts",
            'B': "Mitochondrial electron transport failure and calcium sequestration arrest",
            'C': "Misfolded protein aggregate accumulation and impaired proteasomal clearance",
            'D': "Antibody-mediated autoimmune demyelination of central white matter tracts",
            'E': "Persistent neurotropic viral infection triggering chronic neuroinflammation"
        }
    },
    # Q90: Balance sleep-wake neuronal populations
    90: {
        'opts': {
            'A': "Suprachiasmatic retinal-recipient neurons",
            'B': "Pineal melatonin-synthesizing pinealocytes",
            'C': "Cerebellar cortex inhibitory Purkinje cells",
            'D': "Hippocampal CA1 excitatory pyramidal neurons",
            'E': "Lateral hypothalamic orexinergic neurons"
        }
    },
    # Q92: Balance sleep stage terminology
    92: {
        'opts': {
            'A': "Alert wakefulness stage",
            'B': "NREM stage N1 sleep",
            'C': "NREM stage N2 sleep",
            'D': "Rapid eye movement sleep",
            'E': "NREM stage N3 sleep"
        }
    },
    # Q93: Balance restless legs diagnostic evaluations
    93: {
        'opts': {
            'A': "Diagnostic overnight polysomnography",
            'B': "Contrast-enhanced brain MRI study",
            'C': "Serum ferritin level for iron deficiency",
            'D': "Routine 24-hour ambulatory EEG study",
            'E': "Lumbar puncture for CSF hypocretin"
        }
    },
    # Q94: Balance zolpidem mechanism descriptions
    94: {
        'opts': {
            'A': "Allosteric modulation of GABA-A receptors at the benzodiazepine site",
            'B': "Agonism of suprachiasmatic melatonin MT1 and MT2 G-protein receptors",
            'C': "Competitive antagonism of dual hypocretin/orexin OX1/OX2 receptors",
            'D': "Direct postsynaptic stimulation of striatal dopamine D2 receptors",
            'E': "Central presynaptic stimulation of alpha-2 adrenergic receptors"
        }
    },
    # Q96: Balance pseudobulbar affect pharmacology
    96: {
        'opts': {
            'A': "Oral riluzole therapy",
            'B': "Oral baclofen therapy",
            'C': "Haloperidol pharmacotherapy",
            'D': "Dextromethorphan-quinidine",
            'E': "Oral levodopa-carbidopa"
        }
    },
    # Q97: Balance ALS epidemiology and clinical onset options
    97: {
        'opts': {
            'A': "Limb-onset disease accounts for two-thirds of cases, while bulbar-onset carries a worse prognosis",
            'B': "Inherited familial cases account for more than 75% of all confirmed clinical presentations of ALS",
            'C': "Distal ascending symmetric sensory loss in a stocking-glove pattern is an early cardinal feature",
            'D': "Autonomic neurogenic urinary incontinence and detrusor hyperreflexia occur in early-stage disease",
            'E': "Extraocular muscles and pupillary constrictors are typically the earliest muscle groups to fail"
        }
    },
    # Q98: Balance ALS diagnostic criteria combinations
    98: {
        'opts': {
            'A': "Isolated lower motor neuron weakness confined strictly to distal intrinsic hand muscles",
            'B': "Isolated upper motor neuron spasticity and hyperreflexia without muscle denervation",
            'C': "Concomitant upper and lower motor neuron signs across multiple segments without sensory loss",
            'D': "Prominent stocking-glove sensory loss accompanied by progressive lower motor neuron weakness",
            'E': "Prominent appendicular cerebellar ataxia and intention tremor with preservation of strength"
        }
    },
    # Q99: Balance edaravone mechanism descriptions
    99: {
        'opts': {
            'A': "Antagonism of glutamatergic NMDA receptors to decrease excitotoxic neuronal death",
            'B': "Presynaptic stimulation of GABAB receptors to reduce spinal motor neuron reflex drive",
            'C': "Central agonism of alpha-2 adrenergic receptors to reduce upper motor neuron spasticity",
            'D': "Inhibition of ryanodine channels to prevent calcium release from sarcoplasmic reticulum",
            'E': "Scavenging of reactive oxygen species to reduce motor neuron oxidative cellular injury"
        }
    },
    # Q100: Balance spasticity local therapy options
    100: {
        'opts': {
            'A': "Intrathecal baclofen, acting as a GABAB agonist to reduce spinal reflex arcs",
            'B': "Dantrolene therapy, acting on ryanodine receptors to block muscle calcium release",
            'C': "Oral tizanidine, acting as a central alpha-2 agonist to reduce motor excitation",
            'D': "Botulinum toxin, cleaving SNARE proteins to inhibit motor endplate acetylcholine",
            'E': "Cyclobenzaprine, inhibiting descending brainstem monoaminergic motor pathways"
        }
    }
}
