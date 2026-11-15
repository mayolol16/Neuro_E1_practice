import json
import re

def build_cleaned_questions():
    in_path = '/Users/markyoussef_1/.gemini/antigravity-ide/scratch/usmle_exam1/exam3_high_yield_questions.json'
    out_path = '/Users/markyoussef_1/.gemini/antigravity-ide/scratch/usmle_exam1/exam3_high_yield_questions.json'

    with open(in_path, 'r', encoding='utf-8') as f:
        questions = json.load(f)

    # Specific overrides dictionary:
    # key: q_num (int)
    # val: { 'stem': optional new stem, 'options': dict of letter -> text }
    overrides = {
        # --- UNIT 1: Demyelinating Diseases (Q1 - Q15) ---
        1: {
            'options': {
                'A': 'Neutrophilic pleocytosis with marked hypoglycorrhachia',
                'B': 'Albuminocytologic dissociation with normal IgG index',
                'C': 'Elevated IgG index and oligoclonal bands on electrophoresis',
                'D': 'Xanthochromia with persistent non-clearing erythrocytes',
                'E': 'Elevated opening pressure with positive cryptococcal antigen'
            }
        },
        2: {
            'options': {
                'A': 'Solitary ring-enhancing supratentorial mass with vasogenic edema',
                'B': 'Symmetrical T2/FLAIR hyperintensity within bilateral basal ganglia',
                'C': 'Longitudinally extensive spinal cord lesion with normal cranial MRI',
                'D': 'Extensive cortical ribboning involving cerebral cortex and basal ganglia',
                'E': 'Multiple demyelinating plaques in periventricular white matter'
            }
        },
        3: {
            'options': {
                'A': 'An afferent defect of the right optic nerve',
                'B': 'An efferent defect of the right oculomotor nerve',
                'C': 'An efferent defect of the left oculomotor nerve',
                'D': 'An interruption of the right sympathetic pathway',
                'E': 'A retrochiasmal lesion of the left optic tract'
            }
        },
        7: {
            'options': {
                'A': 'Direct bacterial invasion and replication in peripheral nerve roots',
                'B': 'Elaboration of a bacterial exotoxin destroying anterior horn cells',
                'C': 'Persistent dormant bacterial replication within the subarachnoid space',
                'D': 'Severe systemic dehydration producing metabolic axonal disruption',
                'E': 'Molecular mimicry of bacterial epitopes triggering anti-myelin antibodies'
            }
        },
        8: {
            'stem': 'A 33-year-old man presents with progressive ascending leg weakness, tingling, and absent deep tendon reflexes four weeks after an episode of chills and diarrhea after eating undercooked chicken. Nerve conduction studies are ordered. Which of the following is the best choice of region to test first and the expected result?',
            'options': {
                'A': 'Arms first; axonal loss with preserved velocities',
                'B': 'Face first; normal conduction velocities and amplitudes',
                'C': 'Legs first; slowed conduction indicating demyelination',
                'D': 'Legs first; absent sensory potentials with normal velocities',
                'E': 'Arms first; decremental response on repetitive stimulation'
            }
        },
        9: {
            'options': {
                'A': 'It replaces deficient peripheral myelin proteins',
                'B': 'It clears circulating antibodies, complement, and cytokines',
                'C': 'It directly stimulates remyelination of peripheral axons',
                'D': 'It eliminates persistent Campylobacter from the bloodstream',
                'E': 'It competitively blocks postsynaptic acetylcholine receptors'
            }
        },
        10: {
            'options': {
                'A': 'Pheochromocytoma',
                'B': 'Severe sepsis',
                'C': 'Pulmonary embolism',
                'D': 'Dysautonomia',
                'E': 'Myocardial infarction'
            }
        },
        11: {
            'options': {
                'A': 'Friedreich ataxia; frataxin deficiency',
                'B': 'Guillain-Barré syndrome; anti-ganglioside antibodies',
                'C': 'Spinal muscular atrophy; survival motor neuron 1 deletion',
                'D': 'Subacute combined degeneration; cobalamin deficiency',
                'E': 'Charcot-Marie-Tooth disease; peripheral myelin protein 22 mutation'
            }
        },
        12: {
            'options': {
                'A': 'Presence of autoantibodies targeting aquaporin-4 water channels',
                'B': 'Presence of circulating antibodies targeting peripheral gangliosides',
                'C': 'Selective sparing of the optic apparatus with purely motor deficits',
                'D': 'Demyelination restricted entirely to peripheral Schwann cell sheaths',
                'E': 'Reactivation of latent JC virus within central oligodendrocytes'
            }
        },
        15: {
            'options': {
                'A': 'Progressive dermatomal nerve root compression',
                'B': 'Degeneration of descending upper motor neuron tracts',
                'C': 'Selective loss of anterior horn cells at L4–S1',
                'D': 'Length-dependent degeneration of the longest axons',
                'E': 'Postsynaptic neuromuscular junction receptor failure'
            }
        },

        # --- UNIT 2: Cerebellum (Q16 - Q27) ---
        16: {
            'options': {
                'A': 'Resting tremor and lead-pipe rigidity',
                'B': 'Vertigo, truncal ataxia, and nystagmus',
                'C': 'Intention tremor and limb dysmetria',
                'D': 'Contralateral spastic hemiparesis',
                'E': 'Expressive non-fluent aphasia'
            }
        },
        18: {
            'options': {
                'A': 'Accessory cuneate nucleus in the caudal medulla (cuneocerebellar tract)',
                'B': 'Dorsal nucleus of Clarke in the spinal cord (dorsal spinocerebellar tract)',
                'C': 'Nucleus gracilis in the caudal medulla (medial lemniscus)',
                'D': 'Ventral posterolateral nucleus in the thalamus (thalamocortical tract)',
                'E': 'Inferior olivary nucleus in the rostral medulla (olivocerebellar tract)'
            }
        },
        20: {
            'options': {
                'A': 'Infarction of the left cerebellar hemisphere',
                'B': 'Ischemic injury to the cerebellar vermis',
                'C': 'Interruption of descending frontopontine fibers',
                'D': 'Demyelination of the ascending dorsal columns',
                'E': 'Occlusion of the right inferior cerebellar peduncle'
            }
        },
        22: {
            'options': {
                'A': 'Intention tremor on finger-to-nose testing',
                'B': 'Scanning dysarthric speech pattern',
                'C': 'Truncal ataxia when seated unsupported',
                'D': 'Direction-changing horizontal nystagmus',
                'E': 'Positive Romberg sign with eyes closed'
            }
        },
        23: {
            'options': {
                'A': 'Displaced otoliths in semicircular canals',
                'B': 'Endolymphatic hydrops of membranous labyrinth',
                'C': 'Schwannoma arising from cranial nerve VIII',
                'D': 'Transient vertebrobasilar hypoperfusion',
                'E': 'Atrophy of the anterior cerebellar vermis'
            }
        },
        24: {
            'options': {
                'A': 'Intravenous cyanocobalamin replacement',
                'B': 'High-dose intravenous corticosteroids',
                'C': 'Therapeutic plasma exchange',
                'D': 'Intravenous penicillin G therapy',
                'E': 'Supportive care and physical therapy'
            }
        },
        25: {
            'options': {
                'A': 'Lysosome; basal ganglia and substantia nigra',
                'B': 'Peroxisome; lateral cerebellar hemispheres',
                'C': 'Mitochondria; dorsal columns and spinocerebellar tracts',
                'D': 'Golgi apparatus; motor cortex and corticospinal tracts',
                'E': 'Nucleus; ventral anterior and lateral thalamus'
            }
        },
        26: {
            'options': {
                'A': 'Parkinson disease',
                'B': 'Cerebellar lesion',
                'C': 'Essential tremor',
                'D': 'Hyperthyroidism',
                'E': 'Physiologic tremor'
            }
        },

        # --- UNIT 3: Tumors & Phakomatoses (Q28 - Q48) ---
        28: {
            'options': {
                'A': 'Ring-enhancing mass with central necrosis and marked vasogenic edema',
                'B': 'Cystic cerebellar lesion with an intensely enhancing mural nodule',
                'C': 'Extra-axial dural-based mass demonstrating a prominent dural tail',
                'D': 'Cerebellopontine angle mass widening the internal acoustic meatus',
                'E': 'Multiple subependymal calcified nodules lining the lateral ventricles'
            }
        },
        30: {
            'options': {
                'A': 'Glioblastoma; pseudopalisading necrosis and vascular proliferation',
                'B': 'Oligodendroglioma; fried-egg cells with chicken-wire capillaries',
                'C': 'Ependymoma; true ependymal rosettes and perivascular pseudorosettes',
                'D': 'Pilocytic astrocytoma; biphasic pattern with Rosenthal fibers',
                'E': 'Meningioma; whorled arachnoid pattern with psammoma bodies'
            }
        },
        31: {
            'options': {
                'A': 'Left cerebellar hemisphere',
                'B': 'Cerebellar vermis',
                'C': 'Frontal eye field',
                'D': 'Cervical dorsal columns',
                'E': 'Occipital calcarine cortex'
            }
        },
        32: {
            'stem': 'A 2-year-old child presents with a 1-month history of irritability, daily vomiting, a wobbly wide-based gait, and bilateral papilledema, raising concern for a posterior fossa mass with elevated intracranial pressure. Why should a lumbar puncture be avoided in this patient?',
            'options': {
                'A': 'It introduces an unacceptable risk of iatrogenic bacterial meningitis',
                'B': 'It produces non-diagnostic CSF due to uninterpretable protein elevations',
                'C': 'It is contraindicated due to extreme pediatric procedural distress',
                'D': 'It results in technical failure to aspirate adequate CSF volumes',
                'E': 'It precipitates tonsillar herniation through the foramen magnum'
            }
        },
        34: {
            'options': {
                'A': 'Slow indolent tumor growth allowing progressive brain accommodation',
                'B': 'Rapid parenchymal infiltration without initial mass displacement',
                'C': 'Acute intratumoral hemorrhage causing sudden mass expansion',
                'D': 'Hematogenous dissemination with multiple micro-metastases',
                'E': 'Early obstruction of cerebral aqueduct CSF outflow pathways'
            }
        },
        35: {
            'options': {
                'A': 'Infratentorial pediatric tumor; cystic with Rosenthal fibers',
                'B': 'Intraventricular pediatric tumor; perivascular pseudorosettes',
                'C': 'Extra-axial adult tumor; dural tail with psammoma bodies',
                'D': 'Supratentorial adult tumor; fried-egg cells with chicken-wire capillaries',
                'E': 'Cerebellopontine angle tumor; biphasic Antoni A and B architecture'
            }
        },
        37: {
            'options': {
                'A': 'Schwannomas arise from fibroblasts; neurofibromas arise from perineurial cells',
                'B': 'Schwannomas lack a capsule; neurofibromas possess a thick fibrous capsule',
                'C': 'Schwannomas occur strictly intracranially; neurofibromas occur only peripherally',
                'D': 'Schwannomas metastasize widely; neurofibromas are entirely indolent',
                'E': 'Schwannomas displace adjacent axons; neurofibromas infiltrate through the nerve'
            }
        },
        38: {
            'options': {
                'A': 'Loss of merlin impairs contact inhibition, allowing unregulated Schwann cell growth',
                'B': 'Loss of merlin overactivates mTOR, leading to cell enlargement without hyperplasia',
                'C': 'Loss of merlin disables Ras-GAP activity, stimulating constitutive MAPK signaling',
                'D': 'Loss of merlin blocks ubiquitin ligase, causing uncontrolled hypoxia factor buildup',
                'E': 'Loss of merlin disrupts iron homeostasis, leading to oxidative mitochondrial damage'
            }
        },
        39: {
            'options': {
                'A': 'Resting pill-rolling tremor and cogwheel rigidity',
                'B': 'Non-fluent expressive aphasia and right hemiparesis',
                'C': 'Sensorineural hearing loss, tinnitus, and vertigo',
                'D': 'Bitemporal hemianopia and pituitary insufficiency',
                'E': 'Bilateral anosmia and Foster Kennedy syndrome'
            }
        },
        40: {
            'options': {
                'A': 'One isolated café-au-lait macule',
                'B': 'Bilateral vestibular schwannomas',
                'C': 'A single isolated cutaneous schwannoma',
                'D': 'Two or more neurofibromas of any type',
                'E': 'One isolated Lisch nodule'
            }
        },
        41: {
            'options': {
                'A': 'Cutaneous schwannoma',
                'B': 'Plexiform neurofibroma',
                'C': 'Capillary hemangioblastoma',
                'D': 'Transitional meningioma',
                'E': 'Subependymoma'
            }
        },
        44: {
            'options': {
                'A': 'TSC1 and TSC2, encoding hamartin and tuberin (inhibit mTOR)',
                'B': 'NF1, encoding neurofibromin (inactivates Ras GTPase)',
                'C': 'VHL, encoding pVHL (degrades hypoxia-inducible factor)',
                'D': 'GNAQ, encoding Gαq (activates phospholipase C)',
                'E': 'FXN, encoding frataxin (regulates mitochondrial iron)'
            }
        },
        45: {
            'options': {
                'A': 'Medulloblastoma',
                'B': 'Pilocytic astrocytoma',
                'C': 'Ependymoma',
                'D': 'Subependymal giant cell astrocytoma',
                'E': 'Meningioma'
            }
        },
        46: {
            'options': {
                'A': 'Calcified benign neoplasm arising from the choroid plexus epithelium',
                'B': 'Enlarged gyrus with disorganized cortical lamination and dysplastic neurons',
                'C': 'Cerebellar cyst with an intensely contrast-enhancing mural nodule',
                'D': 'Extra-axial collection of concentric whorled arachnoid cap cells',
                'E': 'Heterotopic cluster of mature histologically normal cortical neurons'
            }
        },
        47: {
            'options': {
                'A': 'Subependymal subcortical hamartomas; germline TSC1 mutation',
                'B': 'Cerebellar capillary hemangioblastomas; germline VHL mutation',
                'C': 'Leptomeningeal vascular angiomas; somatic mosaic GNAQ mutation',
                'D': 'Cutaneous peripheral neurofibromas; germline NF1 mutation',
                'E': 'Bilateral acoustic schwannomas; germline NF2 mutation'
            }
        },
        48: {
            'options': {
                'A': 'Whorled arachnoid cap cells; NF2 gene on chromosome 22q',
                'B': 'Piloid astrocytes with Rosenthal fibers; NF1 gene on chromosome 17q',
                'C': 'Dysplastic ganglion cells; TSC2 gene on chromosome 16p',
                'D': 'Spindle-shaped Schwann cells; NF2 gene on chromosome 22q',
                'E': 'Foamy stromal cells with vascular meshwork; VHL gene on chromosome 3p'
            }
        },

        # --- UNIT 4: Infections (Q49 - Q63) ---
        49: {
            'options': {
                'A': 'Neutrophilic abscess with fibrous pseudocapsule',
                'B': 'Caseating granulomas with Langhans giant cells',
                'C': 'Extensive demyelination with foamy macrophages',
                'D': 'Perivascular lymphocytic cuffs with microglial nodules',
                'E': 'Spongiform vacuolation without inflammatory infiltrate'
            }
        },
        51: {
            'options': {
                'A': 'Ingestion of cat oocysts or undercooked meat cysts',
                'B': 'Inhalation of aerosolized avian environmental droppings',
                'C': 'Direct inoculation via infected tsetse fly bite',
                'D': 'Cribriform mucosal invasion from freshwater swimming',
                'E': 'Percutaneous inoculation from infected raccoon saliva'
            }
        },
        52: {
            'options': {
                'A': 'Marked neutrophilic pleocytosis with Gram-positive diplococci',
                'B': 'Multiple contrast-enhancing ring lesions throughout basal ganglia',
                'C': 'Non-enhancing confluent white matter lesions without mass effect',
                'D': 'Asymmetric hemorrhagic necrosis of the inferomedial temporal lobe',
                'E': 'Mononuclear pleocytosis with positive India ink cryptococcal capsule'
            }
        },
        53: {
            'options': {
                'A': 'Bilateral retrobulbar optic neuritis',
                'B': 'Bilateral calcarine cortex infarctions',
                'C': 'Bilateral demyelination of optic radiations',
                'D': 'Bilateral rhegmatogenous retinal detachments',
                'E': 'Chiasmal compression by pituitary enlargement'
            }
        },
        54: {
            'options': {
                'A': 'Multiple basal ganglia lesions with positive Toxoplasma IgG',
                'B': 'Peripheral absolute CD4+ lymphocyte count greater than 200/µL',
                'C': 'Rapid radiographic resolution following pyrimethamine-sulfadiazine',
                'D': 'Solitary periventricular lesion with positive CSF EBV PCR',
                'E': 'Extensive direct environmental exposure to domestic feline feces'
            }
        },
        55: {
            'options': {
                'A': 'Toxoplasma gondii encephalitis',
                'B': 'Cytomegalovirus ventriculoencephalitis',
                'C': 'JC virus leukoencephalopathy',
                'D': 'Cryptococcus neoformans meningitis',
                'E': 'Herpes simplex type 1 encephalitis'
            }
        },
        56: {
            'options': {
                'A': 'Immune reconstitution inflammatory syndrome',
                'B': 'Treatment-refractory tuberculous meningitis',
                'C': 'Medication-induced aseptic meningitis',
                'D': 'Primary central nervous system lymphoma',
                'E': 'HIV-associated neurocognitive disorder'
            }
        },
        57: {
            'options': {
                'A': 'Hematogenous arterial embolization to cerebellar hemispheres',
                'B': 'Trans-cribriform mucosal extension from infected ethmoid sinuses',
                'C': 'Retrograde axonal transport via trigeminal or olfactory nerves',
                'D': 'Ascending trans-synaptic migration along the vagus nerve',
                'E': 'Direct retrograde extension along intraorbital optic nerve sheaths'
            }
        },
        58: {
            'stem': 'A 63-year-old man presents with fever, acute confusion, and temporal lobe seizures whose CSF PCR is positive for HSV-1. Brain biopsy of this patient is most likely to show which of the following?',
            'options': {
                'A': 'Intracellular Negri bodies within cerebellar Purkinje cells',
                'B': 'Foamy lipid-laden macrophages clearing myelin degradation products',
                'C': 'Narrow-based budding yeast cells demonstrating thick capsules',
                'D': 'Central liquefactive necrosis surrounded by a vascularized capsule',
                'E': 'Perivascular lymphocytic infiltrates with Cowdry type A inclusions'
            }
        },
        59: {
            'options': {
                'A': 'Direct mucocutaneous inoculation from active labial lesions',
                'B': 'Fomite contact transmission on non-intact epithelial surfaces',
                'C': 'Malignant transformation driven by latent Epstein-Barr virus',
                'D': 'Reactivation of latent varicella-zoster virus in dorsal root ganglia',
                'E': 'Hematogenous dissemination of superantigen-producing bacteria'
            }
        },
        61: {
            'options': {
                'A': 'Anterior horn lower motor neuron degeneration',
                'B': 'Autoimmune peripheral nerve demyelination',
                'C': 'Middle cerebral artery cortical infarction',
                'D': 'Postsynaptic neuromuscular junction blockade',
                'E': 'Anterior cerebellar vermis Purkinje loss'
            }
        },

        # --- UNIT 5: Blood Supply (Q64 - Q77) ---
        64: {
            'options': {
                'A': 'Leg representation lies on the lateral convexity supplied by the MCA',
                'B': 'Leg representation lies in the medial paracentral lobule supplied by the ACA',
                'C': 'Leg representation lies in the posterior calcarine cortex supplied by the PCA',
                'D': 'Leg representation lies in the anterior medulla supplied by the vertebral artery',
                'E': 'Leg representation lies in the posterior limb supplied by lenticulostriates'
            }
        },
        65: {
            'options': {
                'A': 'Lateral precentral gyrus, Broca area, and frontal operculum',
                'B': 'Striate cortex of the occipital pole and lateral geniculate nucleus',
                'C': 'Medial frontal cortex, corpus callosum, and anterior cingulate gyrus',
                'D': 'Posterior limb of internal capsule, hippocampus, and Meyer loop',
                'E': 'Inferior cerebellar vermis, flocculonodular lobe, and caudal pons'
            }
        },
        67: {
            'options': {
                'A': 'Ophthalmic artery branch of the internal carotid artery',
                'B': 'Cortical branches of the middle cerebral artery',
                'C': 'Calcarine branch of the posterior cerebral artery',
                'D': 'Callosomarginal branch of the anterior cerebral artery',
                'E': 'Superior cerebellar branch of the basilar artery'
            }
        },
        68: {
            'options': {
                'A': 'Right Meyer loop in the anterior temporal lobe',
                'B': 'Left parietal optic radiations along lateral ventricle',
                'C': 'Left Meyer loop in the anterior temporal lobe',
                'D': 'Left cuneus above the calcarine fissure',
                'E': 'Central decussation of the optic chiasm'
            }
        },
        69: {
            'options': {
                'A': 'Left anterior cerebral artery; paracentral lobule',
                'B': 'Left middle cerebral artery (inferior division); superior temporal lobe',
                'C': 'Left posterior cerebral artery; calcarine cortex',
                'D': 'Right middle cerebral artery; supramarginal gyrus',
                'E': 'Left lenticulostriate artery; posterior limb'
            }
        },
        70: {
            'options': {
                'A': 'Left superior temporal gyrus (Wernicke area); MCA inferior division',
                'B': 'Right frontal eye field; MCA superior division',
                'C': 'Left arcuate fasciculus; MCA cortical branches',
                'D': 'Left posterior inferior frontal gyrus (Broca area); MCA superior division',
                'E': 'Left angular gyrus; PCA parieto-occipital branches'
            }
        },
        71: {
            'options': {
                'A': 'Medial frontal cortex near Broca area (ACA/MCA watershed)',
                'B': 'Superior temporal gyrus (middle cerebral artery territory)',
                'C': 'Arcuate fasciculus (deep subcortical MCA territory)',
                'D': 'Cuneus and lingual gyri (posterior cerebral artery territory)',
                'E': 'Ventral posterolateral nucleus (thalamoperforating territory)'
            }
        },
        72: {
            'options': {
                'A': 'Inferior frontal gyrus (anterior watershed zone)',
                'B': 'Arcuate fasciculus (deep subcortical white matter)',
                'C': 'Paracentral lobule (anterior cerebral artery territory)',
                'D': 'Frontal eye field (middle cerebral artery territory)',
                'E': 'Parietotemporal junction (MCA/PCA watershed zone)'
            }
        },
        73: {
            'options': {
                'A': 'Conduction aphasia; disruption of arcuate fasciculus',
                'B': 'Anomic aphasia; angular gyrus dysfunction',
                'C': 'Global aphasia; extensive left perisylvian MCA infarction',
                'D': 'Transcortical motor aphasia; anterior watershed infarction',
                'E': 'Spastic dysarthria; bilateral corticobulbar lesion'
            }
        },
        74: {
            'options': {
                'A': 'Aphasia reflects motor coordination failure; dysarthria reflects cognitive deficits',
                'B': 'Aphasia is a multimodal language defect; dysarthria is a neuromuscular speech defect',
                'C': 'Aphasia selectively impairs reading; dysarthria selectively impairs comprehension',
                'D': 'Aphasia arises from cerebellar damage; dysarthria arises from cortical lesions',
                'E': 'Aphasia spares spoken output; dysarthria spares articulation and phonation'
            }
        },
        75: {
            'options': {
                'A': 'Midbrain: basilar artery; pons: PCA; medulla: AICA',
                'B': 'Midbrain: PICA; pons: anterior spinal artery; medulla: SCA',
                'C': 'Midbrain: AICA; pons: PICA; medulla: PCA',
                'D': 'Midbrain: PCA; rostral pons: SCA; caudal pons: AICA; medulla: PICA',
                'E': 'Midbrain: PCoA; pons: PCoA; medulla: PCoA'
            }
        },
        76: {
            'options': {
                'A': 'Superficial veins drain to superior sagittal sinus; deep veins drain to straight sinus',
                'B': 'Deep cerebral veins drain directly into cavernous segments of internal carotid arteries',
                'C': 'Superficial cerebral veins drain directly into straight sinus via superior cerebral veins',
                'D': 'Dural venous sinuses drain directly into anterior vertebral venous plexuses only',
                'E': 'Superior sagittal sinus empties directly into the cavernous sinus via petrosal sinuses'
            }
        },
        77: {
            'options': {
                'A': 'Saccular aneurysms occur in cerebellar fissures; hypertensive bleeds occur in cortex',
                'B': 'Saccular aneurysms occur at venous junctions; hypertensive bleeds occur in pituitary',
                'C': 'Saccular aneurysms occur in spinal arteries; hypertensive bleeds occur in chiasm',
                'D': 'Saccular aneurysms occur in optic nerves; hypertensive bleeds occur in hippocampus',
                'E': 'Saccular aneurysms occur at circle of Willis; hypertensive bleeds occur in basal ganglia'
            }
        },

        # --- UNIT 6: Cerebrovascular Disease (Q78 - Q92) ---
        78: {
            'options': {
                'A': 'It is an entirely benign event requiring only routine outpatient follow-up',
                'B': 'It carries zero subsequent risk of recurrent focal cerebral ischemia',
                'C': 'It is a medical emergency with up to 10% risk of stroke within 90 days',
                'D': 'It invariably produces definitive acute parenchymal infarction on CT',
                'E': 'It is restricted entirely to elderly patients with severe carotid stenosis'
            }
        },
        79: {
            'options': {
                'A': 'Intimal smooth muscle necrosis followed by extracellular lipid dissolution',
                'B': 'Fibrous cap formation followed by primary subendothelial lipid entrapment',
                'C': 'Occlusive luminal thrombosis followed by late macrophage recruitment',
                'D': 'Intimal lipid entry, inflammatory macrophage signaling, and smooth muscle hyperplasia',
                'E': 'Medial dystrophic calcification followed by diffuse adventitial inflammation'
            }
        },
        80: {
            'options': {
                'A': 'Atheroma; common carotid bifurcation; heavy tobacco smoking',
                'B': 'Lipohyalinosis; deep penetrating arterioles; chronic hypertension',
                'C': 'Thromboembolism; distal middle cerebral artery; atrial fibrillation',
                'D': 'Arterial dissection; extracranial vertebral artery; cervical trauma',
                'E': 'Immune vasculitis; superficial cortical venules; chronic viral infection'
            }
        },
        81: {
            'options': {
                'A': 'Renal arteries and hepatic portal vein',
                'B': 'Pulmonary capillaries and splenic sinusoids',
                'C': 'Deep venous plexus of the lower extremities',
                'D': 'Cutaneous arterioles and muscular venules',
                'E': 'Left cardiac chambers and internal carotid bifurcation'
            }
        },
        82: {
            'options': {
                'A': 'Intimal tearing with intramural hematoma dissecting the vessel wall',
                'B': 'Rupture of a thin-walled berry aneurysm into the subarachnoid space',
                'C': 'Transmural granulomatous inflammation destroying internal elastic lamina',
                'D': 'Concentric hyaline arteriolosclerosis narrowing deep penetrating vessels',
                'E': 'Luminal impaction of a calcified thromboembolus from the mitral valve'
            }
        },
        83: {
            'options': {
                'A': 'High fever and neutrophilic pleocytosis on CSF analysis',
                'B': 'Marked CSF hypoglycorrhachia with elevated opening pressure',
                'C': 'Non-clearing bloody CSF and hyperdensity in basal cisterns on CT',
                'D': 'Isolated bilateral papilledema without headache or nuchal rigidity',
                'E': 'Diffuse petechial skin eruption with low leukocyte counts'
            }
        },
        84: {
            'options': {
                'A': 'Expectant observation with serial noncontrast CT scans',
                'B': 'Surgical clipping or endovascular coiling with blood pressure control',
                'C': 'Intravenous recombinant tissue plasminogen activator infusion',
                'D': 'Fractionated stereotactic whole-brain radiation therapy',
                'E': 'Emergent surgical carotid endarterectomy'
            }
        },
        85: {
            'options': {
                'A': 'Flow varies linearly with mean arterial pressure across all ranges',
                'B': 'Flow exhibits prominent vasoconstrictive sensitivity to hypoxemia',
                'C': 'Flow decreases markedly in response to local hypercapnia',
                'D': 'Flow is tightly regulated by local PaCO2 and arterial pressure range',
                'E': 'Flow is completely insensitive to changes in cerebral arterial pH'
            }
        },
        86: {
            'options': {
                'A': 'Immediate lumbar puncture, followed by spine MRI',
                'B': 'Electroencephalography, followed by contrast MRI',
                'C': 'Conventional catheter angiography, followed by MRI',
                'D': 'Transesophageal echocardiography, followed by CT',
                'E': 'Noncontrast CT to rule out hemorrhage, followed by vascular imaging'
            }
        },
        87: {
            'options': {
                'A': 'Hippocampus, cerebellar Purkinje cells, and neocortex',
                'B': 'Dorsal vagal motor nucleus and pontine reticular formation',
                'C': 'Caudate nucleus head and internal globus pallidus',
                'D': 'Thoracic intermediate column and anterior horn cells',
                'E': 'Mammillary bodies and hypothalamic neurosecretory nuclei'
            }
        },
        88: {
            'options': {
                'A': 'Emergent decompressive hemicraniectomy',
                'B': 'Intravenous recombinant tPA administration',
                'C': 'Intensive vascular risk factor and medical management',
                'D': 'Continuous prolonged ambulatory EEG monitoring',
                'E': 'Discontinuation of all antiplatelet medications'
            }
        },
        89: {
            'options': {
                'A': 'Persistent bilateral absence of pupillary light reflexes only',
                'B': 'Isoelectric flat electroencephalographic recording only',
                'C': 'Complete flaccid quadriplegia without motor response only',
                'D': 'Irreversible coma, absent brainstem reflexes, and positive apnea test',
                'E': 'Persistent central hyperventilation on mechanical support only'
            }
        },
        90: {
            'stem': 'A 20-year-old comatose man is being evaluated for brain death following severe closed head trauma. Infusion of cold water into each ear produces no eye movement. Which of the following brainstem levels does this test assess, and what does the result suggest?',
            'options': {
                'A': 'Midbrain level; indicative of reversible metabolic coma',
                'B': 'Pontomedullary vestibulo-ocular pathway; indicative of irreversible damage',
                'C': 'Primary cerebral cortex; indicative of preserved brainstem reflexes',
                'D': 'Cervical spinal cord; indicative of reversible spinal shock',
                'E': 'Anterior cerebellar vermis; unrelated to brainstem viability'
            }
        },
        91: {
            'options': {
                'A': 'Midbrain: gag reflex; pons: pupillary reflex; medulla: corneal reflex',
                'B': 'Midbrain: corneal reflex; pons: gag reflex; medulla: pupillary reflex',
                'C': 'Midbrain: oculocephalic reflex; pons: gag reflex; medulla: corneal reflex',
                'D': 'Midbrain: caloric reflex; pons: cough reflex; medulla: pupillary reflex',
                'E': 'Midbrain: pupillary reflex; pons: corneal reflex; medulla: gag reflex'
            }
        },

        # --- UNIT 7: Brainstem Stroke (Q93 - Q108) ---
        93: {
            'options': {
                'A': 'Pure motor hemiparesis involving contralateral face, arm, and leg',
                'B': 'Pure hemisensory loss involving contralateral face, arm, and leg',
                'C': 'Cortical signs such as aphasia, neglect, or visual field deficits',
                'D': 'Alternating hemiplegia with ipsilateral cranial nerve palsy',
                'E': 'Isolated appendicular ataxia without cognitive or visual signs'
            }
        },
        94: {
            'options': {
                'A': 'Ipsilateral peripheral seventh cranial nerve palsy',
                'B': 'Contralateral peripheral seventh cranial nerve palsy',
                'C': 'Idiopathic Bell palsy involving stylomastoid foramen',
                'D': 'Contralateral corticobulbar upper motor neuron lesion',
                'E': 'Ipsilateral pontine facial motor nucleus degeneration'
            }
        },
        95: {
            'options': {
                'A': 'Distal MCA infarcts cause uniform hemiparesis affecting face, arm, and leg equally',
                'B': 'Proximal MCA infarcts involve lenticulostriates causing equal face/arm/leg weakness',
                'C': 'Proximal MCA infarcts selectively spare facial and branchial motor representations',
                'D': 'Both proximal and distal MCA occlusions yield identical motor deficit distributions',
                'E': 'Distal MCA infarcts produce isolated contralateral lower extremity paralysis'
            }
        },
        97: {
            'options': {
                'A': 'Left frontal lobe; anterior cerebral artery',
                'B': 'Left parietal lobe; middle cerebral artery',
                'C': 'Right occipital lobe; posterior cerebral artery',
                'D': 'Right frontal lobe; anterior cerebral artery',
                'E': 'Right parietal lobe; middle cerebral artery'
            }
        },
        98: {
            'options': {
                'A': 'Right rostral midbrain; posterior cerebral artery',
                'B': 'Left caudal pons; basilar paramedian branches',
                'C': 'Left rostral midbrain; posterior cerebral artery',
                'D': 'Right rostral medulla; anterior spinal artery',
                'E': 'Left rostral medulla; posterior inferior cerebellar artery'
            }
        },
        99: {
            'options': {
                'A': 'Ipsilateral CN III palsy and contralateral hemiplegia (Weber syndrome)',
                'B': 'Ipsilateral CN VI palsy and contralateral hemiplegia (Millard-Gubler)',
                'C': 'Ipsilateral CN XII palsy and contralateral hemiplegia (Dejerine)',
                'D': 'Ipsilateral ataxia, Horner syndrome, and crossed sensory loss (Wallenberg)',
                'E': 'Ipsilateral facial weakness, gaze palsy, and contralateral hemiplegia (Foville)'
            }
        },
        100: {
            'options': {
                'A': 'Left red nucleus only',
                'B': 'Right corticospinal tract',
                'C': 'Left medial lemniscus',
                'D': 'Right superior cerebellar peduncle and substantia nigra',
                'E': 'Left cerebellar hemisphere'
            }
        },
        101: {
            'options': {
                'A': 'Right middle pons involving CN V nuclei and cerebellar peduncle fibers',
                'B': 'Left middle pons involving abducens and corticospinal pathways',
                'C': 'Right rostral midbrain involving oculomotor and red nucleus fibers',
                'D': 'Right rostral medulla involving hypoglossal and corticospinal tracts',
                'E': 'Left caudal pons involving facial colliculus and medial lemniscus'
            }
        },
        102: {
            'options': {
                'A': 'Right medial midbrain ischemia involving oculomotor fibers',
                'B': 'Left lateral medulla ischemia involving the spinothalamic tract',
                'C': 'Right caudal pons ischemia involving the facial motor nucleus',
                'D': 'Left middle pons ischemia involving the corticospinal tract',
                'E': 'Right middle pons ischemia involving CN V, spinothalamic, and sympathetic fibers'
            }
        },
        103: {
            'options': {
                'A': 'Right rostral midbrain (oculomotor nerve, cerebral peduncle)',
                'B': 'Left rostral medulla (hypoglossal nerve, pyramid)',
                'C': 'Left caudal medial pons (abducens nerve, corticospinal tract)',
                'D': 'Right caudal lateral pons (vestibular nuclei, spinal V tract)',
                'E': 'Left lateral medulla (nucleus ambiguus, inferior peduncle)'
            }
        },
        104: {
            'options': {
                'A': 'Right lateral medulla; posterior inferior cerebellar artery',
                'B': 'Right lateral caudal pons; anterior inferior cerebellar artery',
                'C': 'Left lateral caudal pons; anterior inferior cerebellar artery',
                'D': 'Right medial caudal pons; basilar paramedian branches',
                'E': 'Right rostral midbrain; posterior cerebral artery'
            }
        },
        105: {
            'options': {
                'A': 'Left superior cerebellar peduncle; superior cerebellar artery',
                'B': 'Left middle cerebellar peduncle; anterior inferior cerebellar artery',
                'C': 'Right inferior cerebellar peduncle; posterior inferior cerebellar artery',
                'D': 'Left inferior cerebellar peduncle; posterior inferior cerebellar artery',
                'E': 'Left cerebellar hemisphere; anterior spinal artery'
            }
        },
        106: {
            'options': {
                'A': 'Right medial medulla (corticospinal tract, CN XII, medial lemniscus); ASA',
                'B': 'Left lateral medulla (spinothalamic tract, CN IX/X, inferior peduncle); PICA',
                'C': 'Right caudal pons (corticospinal tract, CN VI, PPRF); basilar artery',
                'D': 'Left rostral midbrain (corticospinal tract, CN III, red nucleus); PCA',
                'E': 'Right middle pons (corticospinal tract, CN V, cerebellar peduncle); AICA'
            }
        },
        107: {
            'options': {
                'A': 'Bilateral internal capsules; lenticulostriate arteries',
                'B': 'Bilateral medial medulla; anterior spinal artery',
                'C': 'Bilateral thalamic nuclei; posterior cerebral artery',
                'D': 'Bilateral cerebral peduncles; posterior cerebral artery',
                'E': 'Bilateral ventral pons; basilar artery'
            }
        },
        108: {
            'options': {
                'A': 'Right thalamus; sensory loss would be present in thalamic lacunes',
                'B': 'Left medial medulla; hypoglossal nerve involvement would be present',
                'C': 'Left posterior limb of internal capsule; brainstem lesions cause crossed findings',
                'D': 'Left cerebellar hemisphere; prominent appendicular ataxia would be present',
                'E': 'Left occipital lobe; contralateral homonymous hemianopia would be present'
            }
        },

        # --- UNIT 8: Dementia (Q109 - Q123) ---
        110: {
            'options': {
                'A': 'He loses ability to learn new motor skills and procedures',
                'B': 'He selectively loses previously acquired procedural memories',
                'C': 'He selectively loses short-term working memory capacity',
                'D': 'He can learn new procedural skills but cannot form new declarative memories',
                'E': 'He loses all memory modalities and cognitive abilities equally'
            }
        },
        111: {
            'options': {
                'A': 'Hyperorality, hypersexuality, and placidity (Klüver-Bucy syndrome)',
                'B': 'Anterograde amnesia with preserved social comportment',
                'C': 'Fluent paraphasic speech with impaired comprehension',
                'D': 'Violent unilateral choreiform flinging movements',
                'E': 'Inability to recognize familiar objects visually'
            }
        },
        112: {
            'options': {
                'A': 'Coordinates vestibulospinal reflexes for postural stability',
                'B': 'Consolidates declarative memories into long-term neocortical storage',
                'C': 'Synthesizes syntactic and grammatical components of expressive speech',
                'D': 'Generates slow-wave sleep rhythms via thalamocortical oscillations',
                'E': 'Mediates mesolimbic dopamine reward processing and reinforcement'
            }
        },
        113: {
            'options': {
                'A': 'Hippocampus -> amygdala -> dorsal thalamus -> mammillary body',
                'B': 'Fornix -> hippocampus -> cingulate cortex -> thalamic nuclei',
                'C': 'Hippocampus -> fornix -> mammillary body -> anterior thalamus -> cingulate',
                'D': 'Amygdala -> hypothalamus -> cingulate cortex -> dentate gyrus',
                'E': 'Thalamus -> caudate nucleus -> putamen -> parahippocampal gyrus'
            }
        },
        114: {
            'options': {
                'A': 'Gait apraxia, urinary incontinence, dementia; ventricular dilation',
                'B': 'Encephalopathy, oculomotor dysfunction, ataxia; mammillary hemorrhage',
                'C': 'Chorea, behavioral change, cognitive decline; caudate head atrophy',
                'D': 'Rapidly progressive dementia, startle myoclonus; 14-3-3 protein',
                'E': 'Fluctuating cognition, visual hallucinations; cortical Lewy bodies'
            }
        },
        115: {
            'options': {
                'A': 'Intracellular amyloid neurofibrillary tangles and extracellular tau plaques',
                'B': 'Normal amyloid clearance with selective microglial phagocytic deficiency',
                'C': 'Selective cerebellar amyloid deposition and neocortical tau clearance',
                'D': 'Extracellular beta-amyloid senile plaques and intracellular hyperphosphorylated tau',
                'E': 'Alpha-secretase cleavage generating neurotoxic amyloid beta oligomers'
            }
        },
        116: {
            'options': {
                'A': 'Hydrocephalus ex vacuo; nucleus basalis of Meynert',
                'B': 'Obstructive non-communicating hydrocephalus; caudate nucleus',
                'C': 'Impaired arachnoid granulation resorption; substantia nigra',
                'D': 'Excessive choroid plexus CSF production; locus coeruleus',
                'E': 'Recurrent deep parenchymal hemorrhage; red nucleus'
            }
        },
        117: {
            'options': {
                'A': 'Intraneuronal neurofibrillary tangles within the entorhinal cortex',
                'B': 'Extensive spongiform neuropil vacuolation throughout cerebral cortex',
                'C': 'Cytoplasmic alpha-synuclein Lewy bodies in cortex and substantia nigra',
                'D': 'Round argentophilic tau-positive Pick bodies in frontotemporal lobes',
                'E': 'Multiple cystic cavitary lacunes within the internal capsule'
            }
        },
        118: {
            'options': {
                'A': 'Amnestic syndrome with early selective hippocampal neurodegeneration',
                'B': 'Early visual hallucinations paired with spontaneous parkinsonian signs',
                'C': 'Startle myoclonus paired with rapid subacute cerebellar ataxia',
                'D': 'Magnetic shuffling gait paired with early urge urinary incontinence',
                'E': 'Behavioral variant and primary progressive aphasias with tau or TDP-43'
            }
        },
        119: {
            'options': {
                'A': 'Medial temporal atrophy, diffuse neuritic plaques, and amyloid PET uptake',
                'B': 'Cortical ribboning on MRI, periodic sharp waves on EEG, and CSF 14-3-3',
                'C': 'Ventriculomegaly out of proportion to sulcal enlargement on cranial MRI',
                'D': 'Asymmetric frontotemporal lobar atrophy with knife-edge gyral thinning',
                'E': 'Multiple punctate subcortical lacunar infarctions on T2-weighted MRI'
            }
        },
        120: {
            'options': {
                'A': 'Alzheimer disease; central acetylcholinesterase inhibitors',
                'B': 'Multi-infarct vascular dementia; aggressive antiplatelet therapy',
                'C': 'Dementia with Lewy bodies; low-dose typical antipsychotics',
                'D': 'Normal pressure hydrocephalus; ventriculoperitoneal shunting',
                'E': 'Sporadic Creutzfeldt-Jakob disease; compassionate supportive care'
            }
        },
        121: {
            'options': {
                'A': 'Stepwise cognitive deterioration associated with focal vascular lesions',
                'B': 'Insidious progressive short-term episodic memory loss',
                'C': 'Isolated bilateral anterior hippocampal volume loss',
                'D': 'Extracellular accumulation of fibrillar amyloid plaques',
                'E': 'Marked clinical responsiveness to central cholinesterase inhibitors'
            }
        },
        123: {
            'options': {
                'A': 'Autosomal recessive GAA trinucleotide expansion; frataxin deficiency',
                'B': 'X-linked dominant CGG trinucleotide expansion; FMR1 gene silencing',
                'C': 'Maternal mitochondrial DNA point mutation; heteroplasmic inheritance',
                'D': 'Sporadic infectious proteinaceous prion conversion; conformational change',
                'E': 'Autosomal dominant CAG repeat expansion; huntingtin gene on chromosome 4'
            }
        },

        # --- UNIT 9: CBIL: Epilepsy (Q124 - Q150) ---
        131: {
            'options': {
                'A': 'Both seizure types originate simultaneously from bilateral cerebral hemispheres',
                'B': 'Focal seizures invariably cause complete immediate loss of consciousness',
                'C': 'Focal seizures begin in one hemisphere; generalized involve both hemispheres',
                'D': 'Generalized seizures originate from a discrete circumscribed cortical focus',
                'E': 'Focal and generalized seizures display identical electroencephalographic patterns'
            }
        },
        132: {
            'options': {
                'A': 'Continuous seizure activity >=5 minutes or recurrent seizures without recovery',
                'B': 'Any generalized seizure accompanied by urinary or fecal incontinence',
                'C': 'A single self-limited convulsive seizure lasting less than 60 seconds',
                'D': 'Two separate unprovoked seizures occurring at least one week apart',
                'E': 'Any focal seizure preceded by an epigastric or experiential aura'
            }
        },
        133: {
            'options': {
                'A': 'Experiential aura, throbbing headache, fever, and maculopapular rash',
                'B': 'High fever, nuchal rigidity, petechial rash, and holocephalic headache',
                'C': 'Severe epigastric pain, projectile vomiting, diarrhea, and fever',
                'D': 'Episodic palpitations, facial pallor, diaphoresis, and presyncope',
                'E': 'Premonitory symptoms, abrupt consciousness loss, ictal event, postictal state'
            }
        },
        134: {
            'options': {
                'A': 'Adults: congenital malformations; children: ischemic stroke',
                'B': 'Adults: genetic channelopathies; children: malignant primary tumors',
                'C': 'Adults: bacterial infections only; children: embolic stroke',
                'D': 'Adults: cerebrovascular, tumors, trauma; children: infection, trauma, congenital',
                'E': 'Adults: metabolic derangements only; children: metabolic derangements only'
            }
        },
        136: {
            'options': {
                'A': 'Immediate initiation of dual antiseizure drug combination therapy',
                'B': 'Urgent surgical evaluation for anterior temporal lobectomy',
                'C': 'Identification and treatment of underlying causes without maintenance AEDs',
                'D': 'Lifelong driving and occupational prohibition regardless of EEG',
                'E': 'Mandatory continuous inpatient video-EEG monitoring for one week'
            }
        },
        137: {
            'options': {
                'A': 'Initiate maintenance antiseizure monotherapy',
                'B': 'Reassurance and observation without treatment',
                'C': 'Tilt-table autonomic testing',
                'D': 'Brain fluorodeoxyglucose-PET scan',
                'E': 'Repeat outpatient non-contrast head CT'
            }
        },
        138: {
            'options': {
                'A': 'Lifelong maintenance antiseizure polytherapy',
                'B': 'Resective epilepsy surgical evaluation',
                'C': 'Implantation of a vagus nerve stimulator',
                'D': 'Initiation of a strict ketogenic dietary regimen',
                'E': 'Acute treatment of the underlying systemic etiology'
            }
        },
        139: {
            'options': {
                'A': 'Ethosuximide; T-type calcium channel inhibition; gastrointestinal distress',
                'B': 'Lamotrigine; sodium channel inhibition; isolated skin eruption',
                'C': 'Valproate; GABA transaminase inhibition; weight loss and alopecia',
                'D': 'Carbamazepine; sodium channel inhibition; aplastic anemia and SIADH',
                'E': 'Phenytoin; GABAA receptor allosteric potentiation; sedation'
            }
        },
        141: {
            'options': {
                'A': 'Selective inhibition of low-threshold T-type thalamic calcium channels',
                'B': 'Selective fast inactivation of voltage-gated neuronal sodium channels',
                'C': 'Inactivation of sodium and T-type calcium channels and enhancement of GABA',
                'D': 'Allosteric potentiation of postsynaptic GABAA chloride conductance',
                'E': 'Non-competitive antagonism of postsynaptic ionotropic NMDA receptors'
            }
        },
        142: {
            'options': {
                'A': 'Hepatotoxicity, acute pancreatitis, and teratogenic neural tube defects',
                'B': 'Agranulocytosis, aplastic anemia, and syndrome of inappropriate ADH',
                'C': 'Gingival hyperplasia, hirsutism, and megaloblastic anemia',
                'D': 'Isolated morbilliform cutaneous eruption without systemic signs',
                'E': 'Irreversible concentric peripheral visual field constriction'
            }
        },
        144: {
            'options': {
                'A': 'Voltage-gated sodium channel blockade; agranulocytosis',
                'B': 'GABAA receptor chloride current potentiation; sedation',
                'C': 'Postsynaptic NMDA glutamate receptor blockade; psychosis',
                'D': 'Thalamic T-type calcium channel blockade; Stevens-Johnson syndrome',
                'E': 'GABA transaminase enzyme inhibition; fulminant hepatotoxicity'
            }
        },
        145: {
            'options': {
                'A': 'Calcarine cortex of the occipital lobe',
                'B': 'Medial temporal lobe uncus',
                'C': 'Precentral gyrus of the frontal lobe',
                'D': 'Lateral hemisphere of the cerebellum',
                'E': 'Dorsomedial nucleus of the thalamus'
            }
        },
        146: {
            'options': {
                'A': 'Voltage-gated potassium channelopathy',
                'B': 'Acute systemic metabolic derangement',
                'C': 'Structural focal lesion (oligodendroglioma)',
                'D': 'Benign familial febrile seizure syndrome',
                'E': 'Acute sedative-hypnotic substance withdrawal'
            }
        },
        147: {
            'options': {
                'A': 'Generalized 3-Hz spike-and-wave bursts with no postictal confusion',
                'B': 'Unilateral anterior temporal sharp waves with prolonged postictal confusion',
                'C': 'Chaotic, high-voltage, disorganized hypsarrhythmia on background',
                'D': 'Periodic synchronous triphasic sharp-wave discharges at 1–2 Hz',
                'E': 'Continuous generalized polymorphic delta slowing without spikes'
            }
        },
        148: {
            'options': {
                'A': 'Trans-synaptic synchronization through the dorsal thalamic nuclei',
                'B': 'Trans-hemispheric propagation through the anterior commissure',
                'C': 'Descending propagation through the intermediate spinal gray column',
                'D': 'Subcortical recruitment through the putamen and globus pallidus',
                'E': 'Contiguous somatotopic spread along the precentral motor strip'
            }
        },
        149: {
            'options': {
                'A': 'Immediate complete recovery of orientation within 5 to 10 seconds',
                'B': 'Isolated brief non-rhythmic myoclonic jerks at sleep onset',
                'C': 'Onset triggered predictably by prolonged upright quiet standing',
                'D': 'Lateral tongue laceration, incontinence, and postictal confusion',
                'E': 'Marked facial pallor, diaphoresis, and cold clammy extremities'
            }
        },
        150: {
            'options': {
                'A': 'Initiate multiple antiseizure drugs simultaneously at maximum target doses',
                'B': 'Initiate monotherapy at low dose, titrating to efficacy or tolerability',
                'C': 'Mandate surgical resection prior to any pharmacological trials',
                'D': 'Rely exclusively on dietary ketosis before initiating medications',
                'E': 'Maintain initial monotherapy at subtherapeutic doses regardless of control'
            }
        }
    }

    cleaned_questions = []
    for q in questions:
        qnum = int(q['q_num'])
        new_q = dict(q)
        
        # Apply stem override if present
        if qnum in overrides and 'stem' in overrides[qnum]:
            new_q['stem'] = overrides[qnum]['stem']

        # Apply options override if present
        if qnum in overrides and 'options' in overrides[qnum]:
            opt_map = overrides[qnum]['options']
            new_opts = []
            for o in q['options']:
                letter = o['letter']
                new_text = opt_map.get(letter, o['text'])
                new_opts.append({
                    'letter': letter,
                    'is_correct': o['is_correct'],
                    'text': new_text
                })
            new_q['options'] = new_opts
        
        cleaned_questions.append(new_q)

    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(cleaned_questions, f, indent=2, ensure_ascii=False)

    print(f"Successfully wrote {len(cleaned_questions)} cleaned questions to {out_path}")

if __name__ == '__main__':
    build_cleaned_questions()
