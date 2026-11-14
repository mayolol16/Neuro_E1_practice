# Option balancing and giveaway elimination overrides for Exam 3 "In House c2" (100 Qs)
# Sourced from /Users/markyoussef_1/Downloads/Neuro E3 Practice Exam USMLE Step 1 Style (100 Questions).md
# Rules enforced:
# - Correct answer letter for every question is NEVER changed
# - Eliminate single-parenthetical and single-semicolon giveaways
# - Balance length ratios cleanly across A-E (0.72 <= ratio <= 1.38, max/min <= 1.72)
# - Embed clinical vignettes into Q6, Q9, Q84, Q86 for 100% standalone stems

STEM_OVERRIDES = {
    6: (
        "A 33-year-old man who presented with 4 days of progressive symmetric leg weakness and hyporeflexia "
        "4 weeks after a diarrheal illness develops shortness of breath, and his bedside forced vital capacity "
        "is falling. Which of the following is the most appropriate next step in management?"
    ),
    9: (
        "A 33-year-old man who was diagnosed with Guillain-Barré syndrome is improving 3 months later. "
        "His wife asks why recovery after his peripheral demyelinating illness is usually good while recovery "
        "from the central demyelinating disease in her sister (multiple sclerosis) is poor. Which of the "
        "following is the best explanation?"
    ),
    84: (
        "A 25-year-old woman experiences focal muscular contractions that begin in her right arm and "
        "sequentially spread to her hand and face, followed by generalization to a bilateral tonic-clonic "
        "convulsion. Which of the following best explains why the contractions spread from the arm to the "
        "hand to the face?"
    ),
    86: (
        "A 6-year-old girl with childhood absence epilepsy characterized by 10- to 20-second blank staring "
        "spells with eyelid fluttering, 3-Hz generalized spike-and-wave discharges on EEG, and no postictal "
        "confusion is started on ethosuximide. Which of the following is its mechanism of action?"
    ),
}

OPTION_OVERRIDES = {
    # Demyelinating Disease (Q1-10)
    1: {
        'A': 'Albuminocytologic CSF dissociation',
        'B': 'Intrathecal oligoclonal IgG bands',
        'C': 'Elevated CSF 14-3-3 brain protein',
        'D': 'Grossly bloody CSF xanthochromia',
        'E': 'Encapsulated budding yeast forms',
    },
    2: {
        'A': 'Left medial longitudinal fasciculus',
        'B': 'Right medial longitudinal fasciculus',
        'C': 'Left abducens motor nerve nucleus',
        'D': 'Right paramedian pontine reticular center',
        'E': 'Left oculomotor somatic motor nerve',
    },
    4: {
        'A': 'Antibodies to myelin basic protein',
        'B': 'Antibodies to GM1 ganglioside',
        'C': 'Autoantibodies to aquaporin-4',
        'D': 'Antibodies to acetylcholine receptors',
        'E': 'Autoantibodies to neuronal Hu antigen',
    },
    5: {
        'A': 'Direct viral destruction of anterior horn motor cells',
        'B': 'Antibodies to presynaptic voltage-gated Ca2+ channels',
        'C': 'Autoantibodies to astrocyte end-foot aquaporin-4 channels',
        'D': 'T-cell mediated destruction of CNS oligodendrocytes',
        'E': 'Molecular mimicry against peripheral Schwann gangliosides',
    },
    6: {
        'A': 'High-dose IV methylprednisolone and outpatient follow-up',
        'B': 'Monitored unit admission, serial FVC, and IVIG or PEX',
        'C': 'Oral antibiotic therapy targeting preceding Campylobacter',
        'D': 'Defer all immunomodulatory therapy until lumbar puncture',
        'E': 'Intravenous edrophonium testing followed by pyridostigmine',
    },
    7: {
        'A': 'Dystrophin gene deletion',
        'B': 'GAA repeat expansion in FXN',
        'C': 'Tandem duplication of PMP22',
        'D': 'CAG repeat expansion in HTT',
        'E': 'Homozygous deletion of SMN1',
    },
    8: {
        'A': 'Temperature-dependent axonal conduction block',
        'B': 'Rapid formation of a new perivenular plaque',
        'C': 'Neuromuscular fatigue from receptor block',
        'D': 'Transient cerebral watershed hypoperfusion',
        'E': 'Osmotic demyelination of pontine tegmentum',
    },
    9: {
        'A': 'Peripheral myelin lacks immunogenic targets',
        'B': 'Each Schwann cell myelinates multiple axons',
        'C': 'Peripheral microglia clear debris rapidly',
        'D': 'Schwann cells remyelinate while central repair fails',
        'E': 'Peripheral neurons resist humoral antibodies',
    },
    10: {
        'A': 'Protoplasmic astrocytes',
        'B': 'Perivascular microglia',
        'C': 'Pyramidal neurons',
        'D': 'Peripheral Schwann cells',
        'E': 'Central oligodendrocytes',
    },

    # Cerebellum (Q11-18)
    11: {
        'A': 'Flocculonodular lobe cortex',
        'B': 'Left cerebellar hemisphere',
        'C': 'Anterior cerebellar vermis',
        'D': 'Spinal dorsal column pathway',
        'E': 'Medullary vestibular nuclei',
    },
    13: {
        'A': 'Urgent brain MRI with gadolinium',
        'B': 'Diagnostic lumbar puncture analysis',
        'C': 'Daily vestibular suppressant drug',
        'D': 'Canalith repositioning maneuver',
        'E': 'Tympanostomy tube placement surgery',
    },
    14: {
        'A': 'Dorsal roots and dorsal columns',
        'B': 'Anterior cerebellar vermis',
        'C': 'Lateral corticospinal tracts',
        'D': 'Anterior horn motor neurons',
        'E': 'Lateral spinothalamic tracts',
    },
    15: {
        'A': 'CAG repeat expansion in HTT gene',
        'B': 'CTG repeat expansion in DMPK gene',
        'C': 'Exon deletion in dystrophin gene',
        'D': 'Tandem duplication of PMP22 gene',
        'E': 'GAA repeat expansion in FXN gene',
    },
    16: {
        'A': 'Dorsal columns and anterior horn cells',
        'B': 'Spinothalamic tracts and dorsal columns',
        'C': 'Dorsal columns, corticospinal and spinocerebellar tracts',
        'D': 'Anterior spinal cord motor horn and funiculi',
        'E': 'Fasciculus gracilis and cuneatus columns only',
    },
    17: {
        'A': 'Cerebellar efferents project ipsilaterally to motor neurons',
        'B': 'Efferents cross in superior peduncle and recross in medulla',
        'C': 'The lateral corticospinal tract descends uncrossed in cord',
        'D': 'Cerebellar output exits via middle peduncle to motor cortex',
        'E': 'The lateral vestibulospinal tract carries voluntary output',
    },

    # Tumors & Phakomatoses (Q19-32)
    19: {
        'A': 'Meningothelial whorls with psammoma bodies',
        'B': 'Perinuclear halos with chicken-wire vessels',
        'C': 'Small blue cells with Homer Wright rosettes',
        'D': 'Pseudopalisading necrosis with proliferation',
        'E': 'Biphasic spindle cells with Verocay bodies',
    },
    21: {
        'A': 'Perivascular ependymal pseudorosettes',
        'B': 'Rosenthal fibers and GFAP positivity',
        'C': 'Homer Wright neuroblastic rosettes',
        'D': 'Pseudopalisading necrosis with atypia',
        'E': 'Calcified concentric psammoma bodies',
    },
    22: {
        'A': 'Perivascular pseudorosettes',
        'B': 'Homer Wright neuro rosettes',
        'C': 'Eosinophilic Rosenthal fibers',
        'D': 'Fried-egg cells with networks',
        'E': 'Laminated psammoma calcifieds',
    },
    23: {
        'A': 'Pseudopalisading necrosis; rapid growth with edema',
        'B': 'Perinuclear halos; bilateral callosal infiltration',
        'C': 'Arachnoid cap whorls; compression without invasion',
        'D': 'Antoni A and B areas; origin from nerve root sheaths',
        'E': 'Homer Wright rosettes; widespread CSF dissemination',
    },
    24: {
        'A': 'Pseudopalisading necrosis zones',
        'B': 'Perivascular pseudorosettes',
        'C': 'Eosinophilic Rosenthal fibers',
        'D': 'Fried-egg cells with networks',
        'E': 'Cellular palisading Verocay',
    },
    25: {
        'A': 'Optic nerve schwannoma; NF2 gene on chromosome 22',
        'B': 'Optic pathway glioma; NF1 gene on chromosome 17',
        'C': 'Retinal hemangioblastoma; VHL gene on chromosome 3',
        'D': 'Optic retrobulbar neuritis; HLA-DRB1 association',
        'E': 'Retinal astrocytic hamartoma; TSC1 on chromosome 9',
    },
    26: {
        'A': 'Neurofibromin, a Ras GTPase-activating protein',
        'B': 'Hamartin-tuberin complex, an mTOR regulator',
        'C': 'VHL protein, an oxygen-dependent HIF degrader',
        'D': 'Frataxin, an iron-binding mitochondrial chaperone',
        'E': 'Merlin, a membrane-cytoskeletal tumor suppressor',
    },
    27: {
        'A': 'Antoni A/B areas, Verocay bodies and S100 positivity',
        'B': 'Meningothelial whorls with calcified psammoma bodies',
        'C': 'Glial pseudopalisading necrosis and vascular atypia',
        'D': 'True ependymal rosettes and perivascular collarettes',
        'E': 'Small round blue cells forming Homer Wright rosettes',
    },
    28: {
        'A': 'Loss of Ras GTPase-activating protein function',
        'B': 'Mitochondrial iron accumulation from frataxin',
        'C': 'Loss of tuberin function causing unopposed mTOR',
        'D': 'Somatic activating GNAQ mosaic point variant',
        'E': 'Impaired VHL-mediated degradation of active HIF',
    },
    29: {
        'A': 'Bilateral cerebellopontine angle schwannomas',
        'B': 'Vascular cerebellar cystic hemangioblastoma',
        'C': 'Gyral tram-track calcification and angioma',
        'D': 'Cortical tubers and subependymal glial nodules',
        'E': 'Optic pathway glioma and plexiform neurofibroma',
    },
    30: {
        'A': 'Subependymal nodules; germline TSC2 mutation',
        'B': 'Leptomeningeal angioma; mosaic GNAQ mutation',
        'C': 'Cerebellar hemangioblastoma; germline VHL loss',
        'D': 'Plexiform neurofibroma; germline NF1 mutation',
        'E': 'Vestibular schwannomas; germline NF2 mutation',
    },
    31: {
        'A': 'Echocardiography for cardiac rhabdomyoma',
        'B': 'Dermatologic exam for facial angiofibromas',
        'C': 'Formal audiometry for acoustic neuroma',
        'D': 'Slit-lamp examination for iris Lisch nodules',
        'E': 'Abdominal imaging and plasma metanephrines',
    },
    32: {
        'A': 'Perivascular pseudorosettes; lack of CSF seeding',
        'B': 'Eosinophilic Rosenthal fibers; benign WHO grade I',
        'C': 'Homer Wright rosettes; risk of spinal drop metastases',
        'D': 'Concentric psammoma bodies; local dural invasion',
        'E': 'Antoni A and B cellular areas; sensorineural loss',
    },

    # Opportunistic Infections (Q33-42)
    33: {
        'A': 'Primary central nervous system lymphoma',
        'B': 'Progressive multifocal leukoencephalopathy',
        'C': 'Cerebral Toxoplasma gondii reactivation',
        'D': 'Cryptococcus neoformans fungal meningitis',
        'E': 'Cytomegalovirus ventriculoencephalitis',
    },
    34: {
        'A': 'Toxoplasma gondii; start pyrimethamine and sulfadiazine',
        'B': 'Primary CNS lymphoma; initiate high-dose methotrexate',
        'C': 'Progressive multifocal leukoencephalopathy; start ART',
        'D': 'Cryptococcal meningoencephalitis; amphotericin therapy',
        'E': 'Cytomegalovirus radiculitis; intravenous ganciclovir',
    },
    35: {
        'A': 'Avascular necrosis without inflammation',
        'B': 'Ring-enhancing abscess with tachyzoites',
        'C': 'Soap-bubble gelatinous Virchow-Robin cysts',
        'D': 'Enlarged oligodendrocytes with inclusions',
        'E': 'Perivascular atypical large B lymphocytes',
    },
    36: {
        'A': 'Toxoplasma gondii cyst reactivation',
        'B': 'JC virus demyelinating encephalitis',
        'C': 'Cytomegalovirus ventriculoencephalitis',
        'D': 'Cryptococcus neoformans cryptococcoma',
        'E': 'Herpes simplex virus type 1 encephalitis',
    },
    38: {
        'A': 'Opportunistic superinfection; switch broad antimicrobials',
        'B': 'Antifungal drug toxicity; stop amphotericin immediately',
        'C': 'Immune reconstitution syndrome; continue ART and steroids',
        'D': 'Antiretroviral treatment failure; switch second-line ART',
        'E': 'Toxoplasma relapse; add pyrimethamine and leucovorin',
    },
    39: {
        'A': 'Cortical dementia with severe fluent aphasia',
        'B': 'Subcortical dementia with psychomotor slowing',
        'C': 'Rapidly progressive dementia with startle jerks',
        'D': 'Pure episodic amnesia with hippocampal atrophy',
        'E': 'Frontotemporal dementia with sweet food cravings',
    },
    40: {
        'A': 'Await CSF viral PCR before initiating therapy',
        'B': 'Initiate intravenous acyclovir immediately',
        'C': 'Administer amphotericin B and flucytosine',
        'D': 'Initiate pyrimethamine and sulfadiazine',
        'E': 'Administer high-dose pulse methylprednisolone',
    },
    41: {
        'A': 'HIV vacuolar myelopathy',
        'B': 'CMV lumbosacral radiculitis',
        'C': 'NRTI-induced toxic neuropathy',
        'D': 'Guillain-Barré polyneuropathy',
        'E': 'Subacute combined degeneration',
    },
    42: {
        'A': 'Contralateral inferior quadrantanopia and visual neglect',
        'B': 'Bitemporal hemianopia and bilateral anosmia deficit',
        'C': 'Contralateral homonymous hemianopia and dense hemiparesis',
        'D': 'Contralateral hemiballismus and choreiform movements',
        'E': 'Superior quadrantanopia, olfactory hallucinations, amnesia',
    },

    # Stroke - Blood Supply (Q43-51)
    43: {
        'A': 'Middle cerebral artery superior branch',
        'B': 'Anterior cerebral artery medial trunk',
        'C': 'Posterior cerebral artery calcarine',
        'D': 'Lenticulostriate deep perforators',
        'E': 'Anterior choroidal deep branch',
    },
    44: {
        'A': 'Wernicke sensory aphasia; superior temporal gyrus',
        'B': 'Conduction aphasia; subcortical arcuate fasciculus',
        'C': 'Global aphasia; entire dominant perisylvian cortex',
        'D': 'Broca motor aphasia; inferior frontal gyrus of MCA',
        'E': 'Transcortical motor aphasia; anterior watershed zone',
    },
    45: {
        'A': 'Fluent speech, impaired comprehension, poor repetition',
        'B': 'Nonfluent speech, intact comprehension, poor repetition',
        'C': 'Fluent speech, intact comprehension, poor repetition',
        'D': 'Nonfluent speech, poor comprehension, poor repetition',
        'E': 'Fluent speech, intact comprehension, intact repetition',
    },
    46: {
        'A': 'Inferior frontal Broca motor area',
        'B': 'Superior temporal Wernicke center',
        'C': 'Arcuate superior longitudinal tract',
        'D': 'Frontal eye field cortical center',
        'E': 'Primary motor facial strip cortex',
    },
    47: {
        'A': 'Left PCA; collateral perfusion from the anterior cerebral',
        'B': 'Right MCA; macular representation in the parietal lobe',
        'C': 'Right choroidal; macular fibers in the lateral geniculate',
        'D': 'Left MCA; macular representation in the temporal lobe',
        'E': 'Right PCA; collateral MCA supply at the occipital pole',
    },
    48: {
        'A': 'Anterior communicating; compression of the optic chiasm',
        'B': 'Posterior communicating; superficial pupillary fibers on CN III',
        'C': 'Ophthalmic artery; compression of the intraorbital nerve',
        'D': 'Middle cerebral bifurcation; compression of abducens nerve',
        'E': 'Posterior inferior cerebellar; compression of vagus nerve',
    },
    49: {
        'A': 'Lenticulostriate penetrating branches; lipohyalinosis',
        'B': 'Anterior cerebral cortical trunk; cardiogenic embolus',
        'C': 'Pontine paramedian penetrating branch; artery dissection',
        'D': 'Posterior cerebral cortical branch; systemic vasculitis',
        'E': 'Internal carotid petrous segment; venous thrombosis',
    },
    50: {
        'A': 'Bilateral internal capsule lacunar infarcts',
        'B': 'Embolic occlusion of the proximal MCA trunk',
        'C': 'Anterior spinal artery territory cord ischemia',
        'D': 'Borderzone hypoperfusion between ACA and MCA',
        'E': 'Bilateral calcarine PCA branch thromboemboli',
    },
    51: {
        'A': 'Posterior spinal arteries',
        'B': 'Vertebral arterial trunks',
        'C': 'Anterior spinal cord artery',
        'D': 'Basilar trunk perforators',
        'E': 'Posterior inferior cerebellar',
    },

    # Stroke - Cerebrovascular Disease (Q52-61)
    52: {
        'A': 'Atherosclerosis of internal carotid',
        'B': 'Lipohyalinosis of penetrating vessel',
        'C': 'Cardioembolism from atrial fibrillation',
        'D': 'Internal carotid arterial dissection',
        'E': 'Paradoxical venous embolus via PFO',
    },
    53: {
        'A': 'Noncontrast computed tomography of head',
        'B': 'Magnetic resonance imaging with contrast',
        'C': 'Urgent diagnostic lumbar puncture tap',
        'D': 'Intravenous thrombolytic without scans',
        'E': 'Emergent surgical carotid endarterectomy',
    },
    54: {
        'A': 'Blood pressure of 170/95 mm Hg',
        'B': 'Therapeutic INR of 2.4 on warfarin',
        'C': 'Patient age of seventy-two years',
        'D': 'Transient ischemic attack 2 years ago',
        'E': 'Baseline NIHSS stroke score of 12',
    },
    55: {
        'A': 'Aspirin and permissive hypertension only',
        'B': 'Intravenous alteplase infusion monotherapy',
        'C': 'Dual antiplatelet therapy and close watch',
        'D': 'Endovascular mechanical thrombectomy',
        'E': 'Emergent decompressive hemicraniectomy',
    },
    56: {
        'A': 'Na+/K+ ATPase increase, hyperpolarization, Ca2+ efflux',
        'B': 'Chloride influx, hyperpolarization, reduced oxygen use',
        'C': 'ATP loss, Na+/K+ failure, glutamate surge, Ca2+ influx',
        'D': 'ATP increase, glutamate reuptake, calcium sequestration',
        'E': 'Potassium influx, hyperpolarization, GABA neuroprotection',
    },
    57: {
        'A': 'Internal carotid arterial dissection',
        'B': 'Septic cavernous venous thrombosis',
        'C': 'Atrial fibrillation cardioembolism',
        'D': 'Vertebral artery traumatic dissection',
        'E': 'Ruptured intracranial berry aneurysm',
    },
    58: {
        'A': 'Aneurysmal rebleeding; aspirin',
        'B': 'Obstructive hydrocephalus; tPA',
        'C': 'Cerebral vasogenic edema; mannitol',
        'D': 'Venous sinus thrombosis; heparin',
        'E': 'Delayed cerebral vasospasm; nimodipine',
    },
    59: {
        'A': 'Saccular aneurysm rupture on anterior communicating artery',
        'B': 'Cortical lobar hemorrhage from cerebral amyloid angiopathy',
        'C': 'Venous sinus congestion with hemorrhagic venous infarction',
        'D': 'Charcot-Bouchard microaneurysm rupture in lenticulostriates',
        'E': 'Arteriovenous malformation rupture in parietal cortex',
    },
    60: {
        'A': 'Rupture of saccular berry aneurysm',
        'B': 'Venous sinus thrombosis congestion',
        'C': 'Chronic hypertensive lipohyalinosis',
        'D': 'Paradoxical cardiogenic thromboembolus',
        'E': 'Traumatic tear of cortical bridging vein',
    },
    61: {
        'A': 'Arterial embolization through carotid system',
        'B': 'Direct bony erosion through cribriform plate',
        'C': 'Retrograde venous flow via ophthalmic veins',
        'D': 'Spread through petromastoid middle ear spaces',
        'E': 'Retrograde axonal transport along trigeminal',
    },

    # Stroke - Brainstem (Q62-72)
    63: {
        'A': 'Weber midbrain syndrome; PCA branches',
        'B': 'Benedikt midbrain syndrome; PCA branches',
        'C': 'Foville caudal pontine syndrome; AICA',
        'D': 'Wallenberg lateral medullary syndrome; PICA',
        'E': 'Dejerine medial medullary syndrome; ASA',
    },
    64: {
        'A': 'Nucleus ambiguus; CN IX and X',
        'B': 'Spinal trigeminal nucleus; CN V',
        'C': 'Solitary sensory nucleus; CN VII',
        'D': 'Facial motor nerve nucleus; CN VII',
        'E': 'Hypoglossal motor nucleus; CN XII',
    },
    65: {
        'A': 'PICA; nucleus ambiguus and STT',
        'B': 'AICA; facial motor nucleus and STT',
        'C': 'ASA; medullary pyramid and lemniscus',
        'D': 'PCA; red nucleus and cerebral peduncle',
        'E': 'Basilar; abducens and corticospinal',
    },
    66: {
        'A': 'Vertebral artery; nucleus ambiguus',
        'B': 'Paramedian basilar; pontine pyramid',
        'C': 'Anterior spinal; hypoglossal nucleus',
        'D': 'Posterior cerebral; crus cerebri',
        'E': 'AICA; facial motor nerve nucleus',
    },
    68: {
        'A': 'Claude syndrome; red nucleus and SCP',
        'B': 'Weber syndrome; crus cerebri and CN III',
        'C': 'Benedikt syndrome; red nucleus and lemniscus',
        'D': 'Millard-Gubler syndrome; basis and CN VII',
        'E': 'Dejerine syndrome; pyramid and CN XII',
    },
    69: {
        'A': 'Ipsilateral abducens motor nerve palsy',
        'B': 'Contralateral dorsal column sensory loss',
        'C': 'Ipsilateral jaw deviation on mouth opening',
        'D': 'Contralateral pain and temperature loss',
        'E': 'Ipsilateral tongue deviation with atrophy',
    },
    70: {
        'A': 'Occlusion of posterior cerebral artery',
        'B': 'Bilateral internal carotid occlusion',
        'C': 'Basilar artery trunk thrombotic occlusion',
        'D': 'Anterior spinal artery cord infarction',
        'E': 'Bilateral vertebral artery dissection',
    },
    71: {
        'A': 'Claude syndrome; midbrain tegmentum; PCA',
        'B': 'Weber syndrome; crus cerebri; PCA',
        'C': 'Wallenberg syndrome; lateral medulla; PICA',
        'D': 'Benedikt syndrome; red nucleus; PCA',
        'E': 'Foville syndrome; caudal pons; basilar',
    },
    72: {
        'A': 'Medullary pyramid and medial lemniscus',
        'B': 'Posterior limb of internal capsule',
        'C': 'Ventral posterolateral and medial thalamus',
        'D': 'Primary somatosensory postcentral gyrus',
        'E': 'Midbrain red nucleus and tegmentum',
    },

    # Dementia (Q73-82)
    73: {
        'A': 'Intracellular alpha-synuclein Lewy bodies',
        'B': 'Intracellular tau inclusions in Pick bodies',
        'C': 'Extracellular beta-amyloid and tau tangles',
        'D': 'Spongiform neuronal vacuolar degeneration',
        'E': 'Polyglutamine huntingtin nuclear aggregates',
    },
    74: {
        'A': 'Donepezil; NMDA receptor antagonist',
        'B': 'Memantine; acetylcholinesterase block',
        'C': 'Donepezil; cholinesterase inhibition',
        'D': 'Memantine; dopamine receptor agonism',
        'E': 'Galantamine; selective serotonin block',
    },
    75: {
        'A': 'Extra copy of APP gene on chromosome 21',
        'B': 'Homozygous inheritance of APOE epsilon-4',
        'C': 'Germline mutation in presenilin 1 gene',
        'D': 'Germline mutation in presenilin 2 gene',
        'E': 'Tandem duplication of MAPT tau gene',
    },
    76: {
        'A': 'Alzheimer disease dementia',
        'B': 'Behavioral variant FTD',
        'C': 'Dementia with Lewy bodies',
        'D': 'Normal pressure hydrocephalus',
        'E': 'Subcortical vascular dementia',
    },
    77: {
        'A': 'Amyloid-beta plaques in neocortex',
        'B': 'Prion protein scrapie conversions',
        'C': 'Tau or TDP-43 cortical inclusions',
        'D': 'Alpha-synuclein glial cytoplasmic',
        'E': 'Huntingtin striatal polyglutamine',
    },
    78: {
        'A': 'Visual hallucinations and neuroleptic sensitivity',
        'B': 'Magnetic apraxic gait and urinary incontinence',
        'C': 'Choreiform movements and caudate nucleus atrophy',
        'D': 'Rest tremor, rigidity, and prominent micrographia',
        'E': 'Early language impairment and frontal disinhibition',
    },
    79: {
        'A': 'Alzheimer disease dementia',
        'B': 'Dementia with Lewy bodies',
        'C': 'Behavioral frontotemporal',
        'D': 'Normal pressure hydrocephalus',
        'E': 'Creutzfeldt-Jakob disease',
    },
    80: {
        'A': 'Alpha-synuclein cortical Lewy bodies',
        'B': 'Hyperphosphorylated tau Pick bodies',
        'C': 'Neuritic plaques and neurofibrils',
        'D': 'Spongiform change without inflammation',
        'E': 'Caudate striatal neuronal dropout',
    },
    81: {
        'A': 'Surgical ventriculoperitoneal shunt',
        'B': 'Cholinesterase inhibitor donepezil',
        'C': 'Anti-amyloid monoclonal antibody',
        'D': 'Intravenous aqueous penicillin G',
        'E': 'VMAT2 inhibitor tetrabenazine',
    },
    82: {
        'A': 'GAA repeat expansion in FXN gene',
        'B': 'CTG repeat expansion in DMPK gene',
        'C': 'CGG repeat expansion in FMR1 gene',
        'D': 'CAG repeat expansion in HTT gene',
        'E': 'Hexanucleotide expansion in C9orf72',
    },

    # CBIL Epilepsy (Q83-100)
    83: {
        'A': 'Absence seizure with 3-Hz spike-wave',
        'B': 'Primary generalized tonic-clonic convulsion',
        'C': 'Focal motor seizure evolving to bilateral',
        'D': 'Convulsive vasovagal syncopal collapse',
        'E': 'Focal non-motor impaired awareness seizure',
    },
    84: {
        'A': 'Rapid spread across the anterior corpus callosum',
        'B': 'Synchronization within the centromedian thalamus',
        'C': 'Polysynaptic activation of the cerebellar cortex',
        'D': 'Direct propagation through the striatum and pallidum',
        'E': 'Sequential cortical recruitment along motor homunculus',
    },
    85: {
        'A': 'Hypsarrhythmia with chaotic waves',
        'B': 'Generalized 3-Hz spike-and-wave',
        'C': 'Periodic sharp-wave complexes',
        'D': 'Anterior temporal sharp spikes',
        'E': 'Frontally dominant triphasic waves',
    },
    86: {
        'A': 'Thalamic T-type calcium channel blockade',
        'B': 'Voltage-gated sodium channel inactivation',
        'C': 'GABA-A receptor chloride conductance boost',
        'D': 'Irreversible GABA transaminase inhibition',
        'E': 'Postsynaptic glutamate NMDA receptor block',
    },
    87: {
        'A': 'Gingival hyperplasia',
        'B': 'Bone marrow aplasia',
        'C': 'Coarse hirsutism',
        'D': 'Fetal neural defects',
        'E': 'Symptomatic SIADH',
    },
    91: {
        'A': 'Na+ and T-Ca2+ channel block; pancreatitis',
        'B': 'Sodium channel blockade; gingival hyperplasia',
        'C': 'T-type calcium block; Stevens-Johnson rash',
        'D': 'GABA-A potentiation; respiratory arrest',
        'E': 'Sodium channel block; agranulocytosis',
    },
    92: {
        'A': 'Observation without long-term medication',
        'B': 'Inpatient continuous video-EEG study',
        'C': 'Autonomic evaluation with tilt-table',
        'D': 'Initiate antiseizure drug therapy now',
        'E': 'Positron emission tomography scanning',
    },
    93: {
        'A': 'Genetic channelopathy',
        'B': 'Prior febrile seizures',
        'C': 'Acquired structural lesion',
        'D': 'Cortical malformation',
        'E': 'Inborn metabolic error',
    },
    94: {
        'A': 'Lightheadedness, diaphoresis, and pallor',
        'B': 'Immediate return of orientation in seconds',
        'C': 'Consistent onset after rapid upright stance',
        'D': 'A few brief synchronous jerks under 10 sec',
        'E': 'Prolonged confusion with lateral tongue bite',
    },
    95: {
        'A': 'Two discrete seizures within 24 hours with recovery',
        'B': 'Continuous seizure >5 min or no return to baseline',
        'C': 'Any witnessed convulsive seizure lasting >30 sec',
        'D': 'A single brief seizure accompanied by tongue bite',
        'E': 'Continuous abnormal EEG discharge lasting >1 hour',
    },
    96: {
        'A': 'Focal impaired awareness seizures in mesial temporal lobe',
        'B': 'Childhood absence seizures with 3-Hz spike-wave bursts',
        'C': 'Focal aware motor seizures arising from precentral gyrus',
        'D': 'Generalized myoclonic jerks upon morning awakening',
        'E': 'Sudden atonic drop attacks with abrupt loss of tone',
    },
    97: {
        'A': 'Tonic seizure',
        'B': 'Myoclonic jerk',
        'C': 'Absence spell',
        'D': 'Atonic seizure',
        'E': 'Focal aware spell',
    },
    98: {
        'A': 'Synchronous hypoactivity of cortical interneurons',
        'B': 'Excessive GABA-mediated recurrent inhibition',
        'C': 'Hypersynchronous discharge from excess excitation',
        'D': 'Demyelination causing slowed axonal conduction',
        'E': 'Dopamine depletion in the substantia nigra pars',
    },
    99: {
        'A': 'Mandatory driving restrictions',
        'B': 'Workplace and operating safety',
        'C': 'Avoiding heavy alcohol intake',
        'D': 'Calcium and vitamin D bone health',
        'E': 'Epilepsy surgery in refractory cases',
    },
    100: {
        'A': 'Initiate lifelong antiseizure drug therapy',
        'B': 'Manage the acute alcohol withdrawal cause',
        'C': 'Refer for surgical resective evaluation',
        'D': 'Implant an adjunctive vagus nerve unit',
        'E': 'Initiate a 4-to-1 fat ketogenic regimen',
    },
}
