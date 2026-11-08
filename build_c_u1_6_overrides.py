# build_c_u1_6_overrides.py
# High-yield, balanced overrides for MCQ answer choices across Units 1-6

u1_overrides = {
    1: {
        'A': 'Argyll Robertson pupil of the right eye',
        'B': 'Relative afferent pupillary defect of the right eye',
        'C': 'Postganglionic Horner syndrome of the right eye',
        'D': 'Parasympathetic Adie tonic pupil of the right eye',
        'E': 'Oculomotor third nerve palsy of the right eye'
    },
    3: {
        'A': 'Oligoclonal IgG bands with mild lymphocytic pleocytosis',
        'B': 'Marked neutrophilic pleocytosis with decreased glucose',
        'C': 'Albuminocytologic dissociation with normal cell count',
        'D': 'Gross xanthochromia with numerous crenated erythrocytes',
        'E': 'Markedly elevated opening pressure with positive India ink'
    },
    12: {
        'A': 'Drug-induced autoimmune hepatitis',
        'B': 'Progressive multifocal leukoencephalopathy',
        'C': 'Severe gingival fibromatosis',
        'D': 'Interstitial pulmonary fibrosis',
        'E': 'Cardiac rhabdomyomatosis'
    },
    14: {
        'A': 'Aquaporin-4 water channel',
        'B': 'Myelin oligodendrocyte glycoprotein',
        'C': 'Contactin-associated protein 2',
        'D': 'Voltage-gated potassium channel',
        'E': 'Myelin basic protein antigen'
    },
    15: {
        'A': 'Multiple short peripheral lesions spanning <1 vertebral segment',
        'B': 'Isolated posterior column lesions with dorsal tract involvement',
        'C': 'Longitudinally extensive transverse myelitis spanning ≥3 vertebral segments',
        'D': 'Central cavitation and syrinx with cape-like sensory distribution',
        'E': 'Diffuse spinal cord atrophy without distinct focal lesions'
    },
    16: {
        'A': 'Monoclonal antibody therapy with rituximab or eculizumab',
        'B': 'Intravenous immunoglobulin maintenance monotherapy',
        'C': 'High-dose oral prednisone monotherapy without taper',
        'D': 'Prophylactic anticonvulsant therapy with carbamazepine',
        'E': 'Long-term suppressive antiviral therapy with acyclovir'
    },
    17: {
        'A': 'Predominant cerebral white matter plaques with Dawson fingers',
        'B': 'Milder disease course with complete recovery between relapses',
        'C': 'Subcortical demyelination driven by latent JC virus reactivation',
        'D': 'Severe attacks predominantly affecting optic nerves and spinal cord',
        'E': 'Autoimmune peripheral demyelination mediated by ganglioside antibodies'
    },
    18: {
        'A': 'Direct viral destruction of anterior horn motor neurons',
        'B': 'Autoantibody blockade of presynaptic calcium channels',
        'C': 'Molecular mimicry between microbial antigens and neural gangliosides',
        'D': 'Toxin-mediated inhibition of presynaptic acetylcholine release',
        'E': 'Clonal proliferation of Epstein-Barr virus-infected B cells'
    },
    20: {
        'A': 'AMAN; reduced compound muscle action potentials without slowing',
        'B': 'Miller Fisher variant; isolated sensory nerve potential reduction',
        'C': 'AIDP; marked conduction velocity slowing and conduction block',
        'D': 'CIDP; normal nerve conduction studies and intact reflexes',
        'E': 'Axonal sensory neuronopathy; preserved motor nerve conduction'
    },
    21: {
        'A': 'Daily therapeutic lumbar punctures for pressure relief',
        'B': 'Serial forced vital capacity and inspiratory force assessments',
        'C': 'Weekly serial contrast-enhanced brain magnetic resonance imaging',
        'D': 'Continuous twenty-four-hour electroencephalography monitoring',
        'E': 'Daily cerebrospinal fluid oligoclonal band and protein testing'
    },
    22: {
        'A': 'Intravenous immunoglobulin infusion',
        'B': 'Therapeutic plasma exchange',
        'C': 'Systemic corticosteroid therapy',
        'D': 'Mechanical ventilatory support',
        'E': 'Continuous cardiac monitoring'
    },
    23: {
        'A': 'Autonomic instability with labile blood pressure and arrhythmias',
        'B': 'Upper motor neuron signs with hyperreflexia and spasticity',
        'C': 'Rapidly progressive cognitive decline and prominent dementia',
        'D': 'Profound isolated sensory loss with preserved motor strength',
        'E': 'Prominent early fasciculations with diffuse muscular atrophy'
    },
    24: {
        'A': 'Schwann cells readily proliferate and remyelinate; oligodendrocytes have limited capacity',
        'B': 'Oligodendrocytes regenerate rapidly after injury; Schwann cells cannot divide or migrate',
        'C': 'Peripheral nerve axons lack myelin sheaths; central axons are densely myelinated',
        'D': 'Central nervous system axons regenerate spontaneously; peripheral axons cannot reinnervate',
        'E': 'The blood-brain barrier excludes antibodies in the PNS but admits them into the CNS'
    },
    26: {
        'A': 'Acute autoimmune ascending motor paralysis following bacterial enteritis',
        'B': 'Rapidly progressive neurodegenerative disease confined to cerebral cortex',
        'C': 'Acute demyelinating polyradiculoneuropathy with albuminocytologic dissociation',
        'D': 'Subacute dementia accompanied by generalized myoclonus and cerebellar ataxia',
        'E': 'Hereditary length-dependent sensorimotor polyneuropathy affecting distal limbs'
    },
    29: {
        'A': 'Multiple ring-enhancing basal ganglia lesions with surrounding vasogenic edema',
        'B': 'Non-enhancing subcortical white matter lesions without significant mass effect',
        'C': 'A solitary periventricular contrast-enhancing mass producing midline shift',
        'D': 'Bitemporal hemorrhagic necrotizing lesions with temporal lobe swelling',
        'E': 'Extra-axial dural-based enhancing convexity mass with a prominent dural tail'
    },
    30: {
        'A': 'Wernicke encephalopathy',
        'B': 'Central pontine myelinolysis',
        'C': 'Guillain-Barré syndrome',
        'D': 'Multiple sclerosis',
        'E': 'Brainstem glioma'
    },
    31: {
        'A': 'Acute disseminated encephalomyelitis',
        'B': 'Herpes simplex virus encephalitis',
        'C': 'Relapsing-remitting multiple sclerosis',
        'D': 'Bacterial cerebral abscess',
        'E': 'Charcot-Marie-Tooth disease'
    },
    32: {
        'A': 'One Schwann cell myelinates multiple axons; one oligodendrocyte myelinates one segment',
        'B': 'One oligodendrocyte myelinates multiple axon segments; one Schwann cell myelinates a single segment',
        'C': 'Both central and peripheral myelin sheaths are produced by identical neuroglial cell lineages',
        'D': 'Peripheral nervous system myelin is immune-privileged and resistant to inflammatory attack',
        'E': 'Central myelin demonstrates vigorous regeneration; peripheral myelin undergoes permanent loss'
    },
    33: {
        'A': 'Male sex with symptom onset after age 60',
        'B': 'HLA-DRB1 allele positivity and female sex',
        'C': 'HLA-B27 allele positivity and male sex',
        'D': 'Chronic alcohol use disorder and malnutrition',
        'E': 'Trinucleotide CAG expansion on chromosome 9'
    }
}

u2_overrides = {
    4: {
        'A': 'The corticospinal tract descends uncrossed to the spinal lower motor neurons',
        'B': 'The cerebrocerebellar circuit and corticospinal tract each decussate across the midline',
        'C': 'Cerebellar hemisphere efferents project exclusively to the ipsilateral motor cortex',
        'D': 'The cerebellum modulates motor output without any communication with the cerebral cortex',
        'E': 'Spinocerebellar afferent tracts terminate in the contralateral cerebellar hemisphere'
    },
    6: {
        'A': 'Rubrocerebellar fibers projecting to the red nucleus',
        'B': 'Vestibulocerebellar fibers from vestibular nuclei',
        'C': 'Pontocerebellar fibers from contralateral pontine nuclei',
        'D': 'Olivocerebellar climbing fibers from the inferior olive',
        'E': 'Dorsal spinocerebellar fibers from Clarke nucleus'
    },
    10: {
        'A': 'Intention tremor is present at rest and completely abates during target movement',
        'B': 'Both intention and resting tremors disappear completely during targeted action',
        'C': 'Intention tremor fluctuates with emotional stress and worsens during sleep states',
        'D': 'Intention tremor worsens during targeted voluntary movement and is absent at rest',
        'E': 'Intention tremor presents as a bilateral low-frequency pill-rolling oscillation'
    },
    12: {
        'A': 'Dorsal spinocerebellar tract from Clarke nucleus',
        'B': 'Dorsal columns directly to cerebellar cortex',
        'C': 'Cuneocerebellar tract from lateral cuneate',
        'D': 'Ventral spinothalamic tract to vermis',
        'E': 'Corticospinal tract collateral pathways'
    },
    13: {
        'A': 'Nucleus gracilis',
        'B': 'Clarke nucleus',
        'C': 'Red nucleus',
        'D': 'Nucleus solitarius',
        'E': 'Accessory cuneate nucleus'
    },
    16: {
        'A': 'Intravenous acyclovir therapy',
        'B': 'Oral meclizine maintenance therapy',
        'C': 'Epley canalith repositioning maneuver',
        'D': 'Surgical labyrinthectomy procedure',
        'E': 'Intravenous methylprednisolone pulse'
    },
    17: {
        'A': 'Displaced otoliths within the semicircular canals',
        'B': 'Autoimmune demyelination of the vestibular nerve',
        'C': 'Ischemic atrophy of the anterior cerebellar vermis',
        'D': 'Endolymphatic hydrops distending the cochlear duct',
        'E': 'Atherosclerotic infarction of the flocculonodular lobe'
    },
    20: {
        'A': 'Anterior horn alpha motor neurons',
        'B': 'Lateral corticospinal tract axons',
        'C': 'Postsynaptic neuromuscular junctions',
        'D': 'Large-diameter dorsal root ganglion fibers',
        'E': 'Medial cerebellar vermis Purkinje cells'
    },
    21: {
        'A': 'CAG trinucleotide repeat expansion in ATXN1',
        'B': 'Peripheral myelin protein 22 (PMP22) duplication',
        'C': 'GAA trinucleotide repeat expansion in FXN',
        'D': 'CGG trinucleotide repeat expansion in FMR1',
        'E': 'Superoxide dismutase 1 (SOD1) missense mutation'
    },
    22: {
        'A': 'Frataxin; mitochondria',
        'B': 'Hamartin; peroxisomes',
        'C': 'Neurofibromin; endoplasmic reticulum',
        'D': 'Merlin; lysosomes',
        'E': 'Tau protein; cell nucleus'
    },
    24: {
        'A': 'Spinothalamic tracts and anterior horn motor neurons',
        'B': 'Dorsal columns, spinocerebellar tracts, and corticospinal tracts',
        'C': 'Dentate nuclei and parvocellular red nucleus neurons',
        'D': 'Motor and sensory cranial nerve nuclei in the pons',
        'E': 'Intracranial optic nerves and decussating chiasmal fibers'
    },
    26: {
        'A': 'Right CN III palsy',
        'B': 'Left hemisensory loss',
        'C': 'Right Horner syndrome',
        'D': 'Bilateral visual loss',
        'E': 'Left CN III palsy'
    },
    28: {
        'A': 'Finger-to-nose dysmetria testing',
        'B': 'Heel-to-shin ataxia assessment',
        'C': 'Rapid alternating movement evaluation',
        'D': 'Rebound phenomenon assessment',
        'E': 'Tandem gait and walking observation'
    },
    32: {
        'A': 'Basal ganglia modulate movement initiation; cerebellum coordinates movement accuracy',
        'B': 'Cerebellum initiates voluntary movements; basal ganglia coordinate sensory feedback',
        'C': 'Basal ganglia regulate vestibular reflexes; cerebellum generates resting muscle tone',
        'D': 'Both structures directly innervate lower motor neurons to produce muscle contraction',
        'E': 'Cerebellum forms the final common motor pathway; basal ganglia relay sensory afferents'
    }
}

u3_overrides = {
    1: {
        'A': 'Psammoma bodies with concentric laminated calcifications',
        'B': 'Homer Wright rosettes with hyperchromatic round nuclei',
        'C': 'Antoni A and Antoni B regions with Verocay bodies',
        'D': 'Pseudopalisading necrosis with microvascular proliferation',
        'E': 'Perivascular pseudorosettes radially surrounding blood vessels'
    },
    3: {
        'A': 'Rosenthal fibers and eosinophilic granular bodies',
        'B': 'Small round blue cells forming Homer Wright rosettes',
        'C': 'Round cells with clear perinuclear halos and delicate vessels',
        'D': 'Pseudopalisading necrosis with vascular proliferation',
        'E': 'Spindle cells in concentric whorls with psammoma bodies'
    },
    6: {
        'A': 'Precipitation of acute cerebellar hemispheric infarction',
        'B': 'Direct inoculation of opportunistic pathogens into CSF',
        'C': 'Seeding of malignant neoplastic cells along the cord',
        'D': 'Precipitation of tonsillar herniation from high pressure',
        'E': 'Failure to obtain diagnostic cerebrospinal fluid volume'
    },
    7: {
        'A': 'Perivascular pseudorosettes',
        'B': 'Homer Wright rosettes',
        'C': 'Psammoma calcifications',
        'D': 'Rosenthal fibers',
        'E': 'Verocay bodies'
    },
    12: {
        'A': 'Pseudopalisading necrosis with vascular glomeruloid tufts',
        'B': 'Round oligodendroglial nuclei with clear perinuclear halos',
        'C': 'Concentric cellular whorls and laminated psammoma bodies',
        'D': 'Small hyperchromatic blue cells forming Homer Wright rosettes',
        'E': 'Biphasic compact and loose tissue with Rosenthal fibers'
    },
    13: {
        'A': 'Slow growth and extrinsic parenchymal compression allow brain accommodation',
        'B': 'Rapid parenchymal infiltration causes immediate focal neurological deficits',
        'C': 'Early systemic hematogenous dissemination produces distant cranial metastases',
        'D': 'Intraventricular location immediately obstructs normal ventricular outflow',
        'E': 'Autonomous ectopic hormone hypersecretion causes prominent systemic signs'
    },
    15: {
        'A': 'Pseudopalisading necrosis with prominent microvascular proliferation',
        'B': 'Spindle cells arranged in concentric whorls with psammoma bodies',
        'C': 'Antoni A cellular areas with Verocay bodies and loose Antoni B areas',
        'D': 'Small round hyperchromatic blue cells forming Homer Wright rosettes',
        'E': 'Perivascular pseudorosettes arranged radially around blood vessels'
    },
    17: {
        'A': 'Schwannomas infiltrate through nerve bundles; neurofibromas remain encapsulated',
        'B': 'Schwannomas behave as high-grade sarcomas; neurofibromas remain uniformly indolent',
        'C': 'Schwannomas displace adjacent nerve fibers; neurofibromas infiltrate nerve trunks',
        'D': 'Schwannomas are pathognomonic for NF1; neurofibromas define the NF2 syndrome',
        'E': 'Schwannomas arise from meningothelial cells; neurofibromas originate from dura'
    },
    19: {
        'A': 'GTPase-activating protein that negatively regulates Ras',
        'B': 'Receptor tyrosine kinase that promotes cell proliferation',
        'C': 'Membrane-cytoskeleton scaffold organizing focal adhesions',
        'D': 'Nuclear transcription factor regulating angiogenesis genes',
        'E': 'Mitochondrial iron chaperone mediating ferritin assembly'
    },
    21: {
        'A': 'Demyelinating optic neuritis',
        'B': 'Rhegmatogenous retinal detachment',
        'C': 'Pilocytic optic nerve glioma',
        'D': 'Non-functioning pituitary adenoma',
        'E': 'Suprasellar craniopharyngioma'
    },
    24: {
        'A': 'Forms a GTPase-activating complex with tuberin to inhibit mTOR',
        'B': 'Scaffolds cell cortex proteins to suppress contact-dependent growth',
        'C': 'Targets hypoxia-inducible factor subunits for proteasomal degradation',
        'D': 'Stimulates GTP hydrolysis on membrane-bound Ras proto-oncogenes',
        'E': 'Coordinates mitochondrial iron-sulfur cluster assembly pathways'
    },
    30: {
        'A': 'Tram-track gyriform cortical calcifications with leptomeningeal angioma',
        'B': 'Subependymal giant cell astrocytoma with obstructive hydrocephalus',
        'C': 'Bilateral cerebellopontine angle vestibular nerve schwannomas',
        'D': 'Cerebellar hemangioblastoma with prominent mural nodule enhancement',
        'E': 'Fusiform enlargement of the intracranial optic nerve and chiasm'
    },
    33: {
        'A': 'Cardiac rhabdomyoma and subependymal glial nodules',
        'B': 'Pheochromocytoma and clear cell renal cell carcinoma',
        'C': 'Dural convexity meningioma and vestibular schwannoma',
        'D': 'Cerebral cortical tubers and facial angiofibromas',
        'E': 'Multiple cutaneous neurofibromas and Lisch nodules'
    }
}

u4_overrides = {
    5: {
        'A': 'Elevated pressure, lymphocytic pleocytosis, normal glucose, mildly elevated protein',
        'B': 'Normal opening pressure, normal cell count, markedly elevated protein concentration',
        'C': 'Elevated pressure, neutrophilic pleocytosis, markedly elevated protein, low glucose',
        'D': 'Markedly elevated pressure, gross xanthochromia, abundant crenated erythrocytes',
        'E': 'Normal opening pressure, clear fluid, normal leukocyte count, normal glucose and protein'
    },
    6: {
        'A': 'Markedly elevated opening pressure exceeding 300 mm H2O',
        'B': 'Markedly decreased cerebrospinal fluid glucose below 40 mg/dL',
        'C': 'Markedly elevated cerebrospinal fluid protein above 500 mg/dL',
        'D': 'Marked neutrophilic pleocytosis exceeding 1,000 cells/µL',
        'E': 'Lymphocytic pleocytosis with normal glucose and mild protein elevation'
    },
    8: {
        'A': 'Eosinophilic cytoplasmic Negri bodies',
        'B': 'Cowdry type A intranuclear inclusions',
        'C': 'Homer Wright neuroblastic pseudorosettes',
        'D': 'Antoni A palisading Verocay bodies',
        'E': 'Pseudopalisading ischemic necrosis'
    },
    14: {
        'A': 'Pseudopalisading necrosis with vascular glomeruloid tufts',
        'B': 'Perivascular lymphocytic cuffing, neuronophagia, and microglial nodules',
        'C': 'Concentric psammoma bodies with laminated calcifications',
        'D': 'Epithelioid granulomas with extensive central caseous necrosis',
        'E': 'Diffuse cortical spongiform vacuolation without inflammation'
    },
    15: {
        'A': 'Reactivation of latent varicella-zoster virus in a dorsal root ganglion',
        'B': 'Acute primary cutaneous varicella-zoster infection of thoracic epidermis',
        'C': 'Reactivation of latent herpes simplex virus type 2 in sacral ganglia',
        'D': 'Reactivation of latent cytomegalovirus within anterior horn motor cells',
        'E': 'Retrograde axonal transport of Clostridium tetani metalloprotease toxin'
    },
    18: {
        'A': 'Anterior horn motor neurons',
        'B': 'Cerebral cortical Betz cells',
        'C': 'Dorsal root ganglion neurons',
        'D': 'Cerebellar Purkinje neurons',
        'E': 'Hippocampal pyramidal cells'
    },
    25: {
        'A': 'Intravenous acyclovir followed by oral valacyclovir',
        'B': 'Oral sulfadiazine plus pyrimethamine and leucovorin',
        'C': 'Amphotericin B plus flucytosine, then oral fluconazole',
        'D': 'High-dose systemic methotrexate and folinic acid',
        'E': 'Intravenous penicillin G followed by oral amoxicillin'
    },
    26: {
        'A': 'Broad-spectrum antibacterial therapy achieves complete long-term remission',
        'B': 'Antiretroviral therapy improves survival but carries risk of immune reconstitution',
        'C': 'High-dose intravenous corticosteroid monotherapy provides definitive cure',
        'D': 'Neuroimaging characteristically demonstrates multiple ring-enhancing lesions',
        'E': 'Histopathology reveals fungal pseudohyphae invading cerebral blood vessels'
    },
    28: {
        'A': 'Oral sulfadiazine and pyrimethamine therapy',
        'B': 'Intravenous fluconazole maintenance therapy',
        'C': 'Oral mefloquine and artesunate therapy',
        'D': 'Intravenous ganciclovir induction therapy',
        'E': 'High-dose methotrexate and antiretroviral therapy'
    },
    30: {
        'A': 'HIV-associated vacuolar myelopathy',
        'B': 'Tabes dorsalis from neurosyphilis',
        'C': 'Neuromyelitis optica spectrum disorder',
        'D': 'Anterior spinal artery cord infarction',
        'E': 'Thoracic syringomyelia and cavitation'
    },
    32: {
        'A': 'Antiretroviral drug failure from high viral resistance',
        'B': 'Immune reconstitution inflammatory syndrome',
        'C': 'Progressive multifocal leukoencephalopathy',
        'D': 'Primary central nervous system lymphoma',
        'E': 'Drug-induced aseptic chemical meningitis'
    },
    33: {
        'A': 'HIV-associated neurocognitive disorder',
        'B': 'Early-onset familial Alzheimer disease',
        'C': 'Subcortical vascular ischemic dementia',
        'D': 'Wernicke encephalopathy from thiamine loss',
        'E': 'Sporadic Creutzfeldt-Jakob disease'
    }
}

u5_overrides = {
    1: {
        'A': 'Primary generalized absence seizure with atypical recovery',
        'B': 'Focal aware seizure evolving to bilateral tonic-clonic seizure',
        'C': 'Primary generalized atonic seizure causing sudden drop collapse',
        'D': 'Vasovagal neurocardiogenic syncope with convulsive motor movements',
        'E': 'Psychogenic nonepileptic seizure with conversion reaction symptoms'
    },
    2: {
        'A': 'Propagation through the vermian cerebellar cortex',
        'B': 'Ascending reticular activating system excitation',
        'C': 'Generalized thalamocortical synchrony at 3 Hz',
        'D': 'Electrical spread along the precentral motor cortex homunculus',
        'E': 'Ephaptic transmission between peripheral motor nerve axons'
    },
    3: {
        'A': 'Periodic lateralized sharp wave complexes',
        'B': 'Chaotic high-voltage hypsarrhythmia pattern',
        'C': 'Anterior temporal sharp and slow wave spikes',
        'D': 'Continuous generalized triphasic wave bursts',
        'E': 'Generalized 3-Hz spike-and-wave discharges'
    },
    8: {
        'A': 'Primary generalized myoclonic seizure',
        'B': 'Typical generalized absence seizure',
        'C': 'Generalized tonic seizure without clonic phase',
        'D': 'Generalized atonic seizure with drop attack',
        'E': 'Focal to bilateral tonic-clonic seizure'
    },
    11: {
        'A': 'Continuous clinical seizure activity lasting between 30 and 60 seconds',
        'B': 'Seizure lasting >5 minutes or recurrent seizures without regaining consciousness',
        'C': 'Recurrence of unprovoked epileptic seizures separated by at least 12 months',
        'D': 'Transient postictal confusion resolving within 10 minutes of seizure offset',
        'E': 'Generalized motor paroxysms that fail to demonstrate an electrographic correlate'
    },
    13: {
        'A': 'Discharge with routine observation without pharmacotherapy',
        'B': 'Order upright tilt-table testing with autonomic monitoring',
        'C': 'Obtain urgent fluorodeoxyglucose brain PET-CT imaging',
        'D': 'Admit for inpatient long-term continuous video-EEG telemetry',
        'E': 'Initiate maintenance antiseizure medication monotherapy'
    },
    16: {
        'A': 'Causes fatal idiosyncratic bone marrow agranulocytosis',
        'B': 'Triggers acute hemorrhagic necrotizing pancreatitis',
        'C': 'Induces CYP enzymes, lowering contraceptive efficacy, and is teratogenic',
        'D': 'Demonstrates lack of efficacy against generalized tonic-clonic seizures',
        'E': 'Inhibits hepatic drug metabolism causing toxic buildup of oral estrogen'
    },
    17: {
        'A': 'Renal tubular excretion saturates, eliminating clearance pathways',
        'B': 'Hepatic enzymes saturate, shifting from first-order to zero-order kinetics',
        'C': 'Enterohepatic recirculation produces unpredictable secondary plasma peaks',
        'D': 'Competitive CYP auto-inhibition leads to exponential drug accumulation',
        'E': 'Irreversible binding to central GABA-A receptors causes cumulative toxicity'
    },
    18: {
        'A': 'Acute necrotizing pancreatitis',
        'B': 'Congenital neural tube defects',
        'C': 'Concentric visual field constriction',
        'D': 'Peripheral neuropathy and megaloblastic anemia',
        'E': 'Recurrent calcium oxalate nephrolithiasis'
    },
    19: {
        'A': 'Causes aplastic anemia, SIADH hyponatremia, and CYP450 induction',
        'B': 'Inhibits hepatic CYP enzymes and causes fulminant hepatic necrosis',
        'C': 'Irreversibly inhibits GABA transaminase to enhance inhibitory tone',
        'D': 'Serves as first-line monotherapy for childhood absence epilepsy',
        'E': 'Produces irreversible concentric peripheral visual field defects'
    },
    24: {
        'A': 'Fulminant idiosyncratic hepatotoxicity',
        'B': 'Severe generalized gingival hyperplasia',
        'C': 'Permanent concentric visual field constriction',
        'D': 'Acute hemorrhagic necrotizing pancreatitis',
        'E': 'Severe idiosyncratic agranulocytosis'
    },
    26: {
        'A': 'Benzodiazepines increase duration; barbiturates increase conductance of chloride channels',
        'B': 'Benzodiazepines increase channel opening frequency; barbiturates increase opening duration',
        'C': 'Benzodiazepines act as GABA-B agonists; barbiturates modulate central glycine receptors',
        'D': 'Barbiturates increase channel opening frequency; benzodiazepines increase opening duration',
        'E': 'Both drug classes act primarily by prolonging the inactive state of voltage-gated Na+ channels'
    },
    27: {
        'A': 'GABA transaminase; concentric visual field loss',
        'B': 'T-type Ca2+ channels; severe gastrointestinal pain',
        'C': 'α2δ subunit; peripheral edema and weight gain',
        'D': 'GAT-1 reuptake; encephalopathy and confusion',
        'E': 'SV2A vesicle protein; behavioral and psychiatric effects'
    },
    28: {
        'A': 'Maintain valproate monotherapy at maximum tolerated serum concentrations',
        'B': 'Abruptly discontinue all antiseizure medications prior to conception',
        'C': 'Switch to high-dose oral phenytoin monotherapy with regular drug levels',
        'D': 'Initiate topiramate monotherapy with rapid upward dosage escalation',
        'E': 'Avoid valproate and use lowest effective monotherapy with folate'
    },
    30: {
        'A': 'Inhibiting low-threshold T-type Ca2+ channel currents',
        'B': 'Inhibiting presynaptic GABA reuptake via GAT-1 transporters',
        'C': 'Prolonging the inactivation state of voltage-gated Na+ channels',
        'D': 'Binding to the α2δ subunit of voltage-gated Ca2+ channels',
        'E': 'Binding synaptic vesicle protein SV2A to inhibit exocytosis'
    },
    32: {
        'A': 'Unprovoked first seizure with normal neuroimaging and electroencephalogram',
        'B': 'Drug-resistant epilepsy failing at least two appropriate antiseizure drugs',
        'C': 'Typical absence seizures successfully controlled with ethosuximide monotherapy',
        'D': 'Simple febrile seizures occurring between six months and five years of age',
        'E': 'Single acute provoked seizure occurring in the setting of acute metabolic disturbance'
    }
}

u6_overrides = {
    2: {
        'A': 'Medial cortex leg area supplied by ACA, lateral arm and face areas by MCA',
        'B': 'Medial and lateral sensorimotor cortex supplied exclusively by the PCA',
        'C': 'Entire sensorimotor strip from vertex to sylvian fissure supplied by MCA',
        'D': 'Medial hemisphere cortex supplied by the posterior inferior cerebellar artery',
        'E': 'Sensorimotor cortex supplied by anterior choroidal penetrating branches'
    },
    3: {
        'A': 'Right anterior cerebral artery, pericallosal branch',
        'B': 'Left posterior cerebral artery, calcarine branch',
        'C': 'Left anterior choroidal artery, distal branches',
        'D': 'Left middle cerebral artery, superior division',
        'E': 'Basilar artery trunk, paramedian perforators'
    },
    4: {
        'A': 'Right middle cerebral artery, inferior division',
        'B': 'Left posterior cerebral artery, cortical branches',
        'C': 'Left middle cerebral artery, inferior division',
        'D': 'Left anterior cerebral artery, pericallosal branch',
        'E': 'Left lenticulostriate deep penetrating arteries'
    },
    5: {
        'A': 'Left anterior cerebral artery territory involving supplementary motor area',
        'B': 'Right middle cerebral artery territory involving the frontal eye field',
        'C': 'Left posterior cerebral artery territory involving primary visual cortex',
        'D': 'Right anterior cerebral artery territory involving paracentral lobule',
        'E': 'Right posterior cerebral artery territory involving the lingual gyrus'
    },
    7: {
        'A': 'Central retinal artery collaterals preserve foveal sensation',
        'B': 'Middle cerebral artery collaterals supply the occipital pole',
        'C': 'Temporal Meyer loop fibers project to distinct cortical layers',
        'D': 'Lateral geniculate nucleus collaterals maintain foveal pathways',
        'E': 'Decussating nasal retinal fibers provide bilateral macula input'
    },
    8: {
        'A': 'Lenticulostriate branches of the middle cerebral artery',
        'B': 'Paramedian perforating branches of anterior spinal artery',
        'C': 'Penetrating posterior branches of posterior spinal artery',
        'D': 'Medullary branches of posterior inferior cerebellar artery',
        'E': 'Hemispheric branches of the superior cerebellar artery'
    },
    9: {
        'A': 'Large-caliber superficial conduit vessels with abundant elastic lamina',
        'B': 'Low-pressure thin-walled venous channels with absent adventitial support',
        'C': 'Direct short branch vessels originating from the high-flow basilar trunk',
        'D': 'Long narrow penetrating arteries vulnerable to lipohyalinosis',
        'E': 'Redundant vascular networks protected by extensive anastomotic collaterals'
    },
    10: {
        'A': 'Callosomarginal branch of anterior cerebral artery',
        'B': 'Lenticulostriate branch of middle cerebral artery',
        'C': 'Ophthalmic branch of internal carotid artery',
        'D': 'Calcarine branch of posterior cerebral artery',
        'E': 'Paramedian branch of basilar artery'
    },
    11: {
        'A': 'Left temporal lobe involving Meyer loop',
        'B': 'Right occipital lobe involving calcarine fissure',
        'C': 'Optic chiasm decussating nasal fibers',
        'D': 'Left parietal lobe optic radiations',
        'E': 'Right optic nerve intracranial segment'
    },
    12: {
        'A': 'Medial frontal and parietal cortical lobes',
        'B': 'Lateral frontal operculum and insular cortex',
        'C': 'Occipital calcarine cortex and medial thalamus',
        'D': 'Medial medullary pyramid and hypoglossal nucleus',
        'E': 'Hippocampus, posterior limb of internal capsule, and LGN'
    },
    13: {
        'A': 'Anterior communicating artery; medial sympathetic pupillomotor fibers',
        'B': 'Middle cerebral artery bifurcation; ophthalmic sensory fibers',
        'C': 'Ophthalmic artery origin; central retinal sensory fibers',
        'D': 'Basilar artery bifurcation; somatic motor fibers of CN VI',
        'E': 'Posterior communicating artery; superficial parasympathetic fibers of CN III'
    },
    14: {
        'A': 'Arterial bifurcations around the Circle of Willis',
        'B': 'Deep penetrating lenticulostriate vessels',
        'C': 'Dural sinuses draining into jugular veins',
        'D': 'Anterior spinal artery midline branches',
        'E': 'Superficial cerebral bridging cortical veins'
    },
    16: {
        'A': 'Posterior cerebral, basilar, and superior cerebellar arteries',
        'B': 'Anterior cerebral, middle cerebral, and ophthalmic arteries',
        'C': 'Posterior inferior cerebellar and anterior spinal arteries',
        'D': 'Anterior spinal, posterior spinal, and radicular arteries',
        'E': 'Labyrinthine, pontine, and superior cerebellar arteries'
    },
    18: {
        'A': 'Acute embolic occlusion of the cervical carotid artery',
        'B': 'Hypertensive putaminal microaneurysm rupture',
        'C': 'Thrombotic occlusion of the superior sagittal sinus',
        'D': 'Prolonged systemic arterial hypotension or hypoperfusion',
        'E': 'Spontaneous subarachnoid saccular berry aneurysm rupture'
    },
    20: {
        'A': 'Basal ganglia, thalamus, pons, and cerebellum',
        'B': 'Bilateral occipital poles and posterior calcarine cortex',
        'C': 'Anterior frontal convexity and superior sagittal sinus',
        'D': 'Thoracic spinal cord gray matter and anterior horn',
        'E': 'Petroclival junction and cavernous sinus dural walls'
    },
    21: {
        'A': 'Paramedian, short circumferential, and long circumferential branches',
        'B': 'Paramedian penetrating branches of the posterior cerebral artery alone',
        'C': 'Medial anterior and posterior branches of the middle cerebral artery',
        'D': 'Circumferential descending branches of the anterior spinal artery',
        'E': 'Paramedian branches of the lateral internal carotid terminal network'
    },
    24: {
        'A': 'Vestibular nuclei, nucleus ambiguus, and descending sympathetic fibers',
        'B': 'Medial medulla, pyramid, medial lemniscus, and hypoglossal nucleus',
        'C': 'Posterolateral medulla, inferior cerebellar peduncle, and spinothalamic tract',
        'D': 'Inferior cerebellar peduncle, spinal trigeminal nucleus, and CN X',
        'E': 'Spinal trigeminal tract, cuneate nucleus, and solitary tract nucleus'
    },
    27: {
        'A': 'Cavernous sinus emptying into vertebral venous plexuses',
        'B': 'Dural venous sinuses draining into internal jugular veins',
        'C': 'Meningeal arteries communicating with deep vertebral plexuses',
        'D': 'Cortical diploic veins emptying into external jugular systems',
        'E': 'Epidural venous networks draining into azygos venous channels'
    },
    29: {
        'A': 'Aneurysmal subarachnoid hemorrhage',
        'B': 'Postpartum eclampsia encephalopathy',
        'C': 'Superior sagittal sinus thrombosis',
        'D': 'Acute community-acquired meningitis',
        'E': 'Acute traumatic epidural hematoma'
    },
    30: {
        'A': 'Direct bacterial transmural invasion into adjacent tissue',
        'B': 'Traumatic arterial wall dissection with extravasation',
        'C': 'Venous hypertension causing rupture of draining veins',
        'D': 'Hypertensive Charcot-Bouchard microaneurysm rupture',
        'E': 'Acute coagulative necrosis of hypervascular neoplasm'
    },
    31: {
        'A': 'Internal carotid artery, CN I, CN II, and optic chiasm',
        'B': 'Internal carotid artery, CN III, CN IV, CN V1, V2, and CN VI',
        'C': 'Vertebral artery, anterior spinal artery, CN IX, and CN XII',
        'D': 'Basilar artery, labyrinthine artery, CN VII, and CN VIII',
        'E': 'Superior sagittal sinus, straight sinus, CN X, and CN XI'
    },
    34: {
        'A': 'Broca motor speech area',
        'B': 'Superior temporal gyrus',
        'C': 'Arcuate fasciculus',
        'D': 'Frontal eye field',
        'E': 'Paracentral lobule'
    },
    35: {
        'A': 'Aphasia is a language disorder; dysarthria is a motor speech disorder',
        'B': 'Dysarthria impairs semantic comprehension; aphasia impairs motor fluency',
        'C': 'Both conditions arise exclusively from isolated cerebellar hemisphere damage',
        'D': 'Aphasia affects oral expression only; written syntax remains fully intact',
        'E': 'Dysarthria represents cortical language loss; aphasia represents nerve paresis'
    }
}

ALL_OVERRIDES = {}
for q, opts in u1_overrides.items():
    ALL_OVERRIDES[(1, q)] = opts
for q, opts in u2_overrides.items():
    ALL_OVERRIDES[(2, q)] = opts
for q, opts in u3_overrides.items():
    ALL_OVERRIDES[(3, q)] = opts
for q, opts in u4_overrides.items():
    ALL_OVERRIDES[(4, q)] = opts
for q, opts in u5_overrides.items():
    ALL_OVERRIDES[(5, q)] = opts
for q, opts in u6_overrides.items():
    ALL_OVERRIDES[(6, q)] = opts
