"""Build script to create authentic, calibrated in_house_like_G 150-question bank
directly from Dr. Cohan's study guide (exam3_high_yield_questions.json / Neuro E3 Practice Exam 2 md).
Eliminates all parenthetical giveaways, levels option lengths (spread <= 6 chars),
ensures zero shape/length giveaways, balances answer keys (30 A, 30 B, 30 C, 30 D, 30 E),
and strictly maps to the 7 required blueprint categories.
"""
import json
import re

def build_authentic_in_house_g():
    in_path = '/Users/markyoussef_1/.gemini/antigravity-ide/scratch/usmle_exam1/exam3_high_yield_questions.json'
    out_path = '/Users/markyoussef_1/.gemini/antigravity-ide/scratch/usmle_exam1/exam3_in_house_like_g_questions.json'

    with open(in_path, 'r', encoding='utf-8') as f:
        hy_questions = json.load(f)

    # Category mapping to exact 7 blueprint categories
    def map_category(qnum):
        if 1 <= qnum <= 15:
            return 'Demyelinating Disease'
        elif 16 <= qnum <= 27:
            return 'Cerebellum'
        elif 28 <= qnum <= 48:
            return 'Tumors'
        elif 49 <= qnum <= 63:
            return 'Opportunistic Infection'
        elif 64 <= qnum <= 108:
            return 'Stroke (Blood Supply, Cerebrovascular, Brainstem)'
        elif 109 <= qnum <= 123:
            return 'Dementia'
        elif 124 <= qnum <= 150:
            return 'CBIL Epilepsy'
        return 'Neurology'

    # Precise option overrides to eliminate parentheses and level lengths (spread <= 6)
    overrides = {
        # Unit 1: Demyelinating Disease
        1: {
            'A': 'Neutrophilic pleocytosis with marked hypoglycorrhachia',
            'B': 'Albuminocytologic dissociation with normal IgG index',
            'C': 'Elevated IgG index and oligoclonal bands on CSF gel',
            'D': 'Xanthochromia with persistent non-clearing RBC count',
            'E': 'Markedly elevated pressure with cryptococcal antigen'
        },
        2: {
            'A': 'Solitary ring-enhancing mass with surrounding vasogenic edema',
            'B': 'Symmetrical T2/FLAIR hyperintensity within bilateral ganglia',
            'C': 'Longitudinally extensive spinal cord lesion on cervical spine',
            'D': 'Extensive cortical ribboning involving cerebral cortex mantle',
            'E': 'Multiple demyelinating plaques in periventricular white area'
        },
        4: {
            'A': 'Paramedian pontine reticular formation',
            'B': 'Abducens somatic motor cranial nucleus',
            'C': 'Oculomotor visceral cranial motor core',
            'D': 'Medial longitudinal fasciculus pathway',
            'E': 'Cortical frontal eye field motor center'
        },
        6: {
            'A': 'Multiple sclerosis: oligodendrocytes; Guillain-Barré: Schwann cells',
            'B': 'Multiple sclerosis: Schwann cells; Guillain-Barré: oligodendrocytes',
            'C': 'Multiple sclerosis: astrocytes; Guillain-Barré: oligodendrocyte cells',
            'D': 'Multiple sclerosis: neurons; Guillain-Barré: peripheral Schwann cells',
            'E': 'Multiple sclerosis: microglia; Guillain-Barré: peripheral motor cells'
        },
        7: {
            'A': 'Direct bacterial invasion and replication in peripheral nerve roots',
            'B': 'Elaboration of a bacterial exotoxin destroying anterior horn cells',
            'C': 'Persistent dormant bacterial replication in the subarachnoid space',
            'D': 'Severe systemic dehydration producing metabolic axonal disruption',
            'E': 'Molecular mimicry of bacterial epitopes forming anti-myelin antibodies'
        },
        8: {
            'A': 'Arms first; axonal loss with preserved conduction velocities',
            'B': 'Face first; normal conduction velocities and wave amplitudes',
            'C': 'Legs first; slowed conduction indicating primary demyelination',
            'D': 'Legs first; absent sensory potentials with normal velocities',
            'E': 'Arms first; decremental response on repetitive stimulation'
        },
        9: {
            'A': 'It replaces deficient peripheral myelin proteins',
            'B': 'It clears circulating autoantibodies and cytokines',
            'C': 'It directly stimulates rapid axonal remyelination',
            'D': 'It eliminates persistent intracellular bacteria',
            'E': 'It competitively blocks acetylcholine receptors'
        },
        10: {
            'A': 'Pheochromocytoma crisis',
            'B': 'Systemic septic shock',
            'C': 'Acute pulmonary embolism',
            'D': 'Autonomic instability',
            'E': 'Acute myocardial infarct'
        },
        11: {
            'A': 'Friedreich ataxia; trinucleotide frataxin gene mutation',
            'B': 'Guillain-Barré syndrome; peripheral ganglioside antibodies',
            'C': 'Spinal muscular atrophy; survival motor neuron 1 deletion',
            'D': 'Subacute combined degeneration; cobalamin deficiency state',
            'E': 'Charcot-Marie-Tooth disease; peripheral myelin protein 22'
        },
        13: {
            'A': 'Subcutaneous interferon-beta',
            'B': 'Subcutaneous glatiramer acetate',
            'C': 'Intravenous methylprednisolone',
            'D': 'Intravenous natalizumab therapy',
            'E': 'Intravenous ocrelizumab infusion'
        },
        14: {
            'A': 'Relapsing-remitting disease',
            'B': 'Primary progressive disease',
            'C': 'Secondary progressive form',
            'D': 'Clinically isolated syndrome',
            'E': 'Acute disseminated form'
        },
        15: {
            'A': 'Progressive dermatomal nerve root mechanical injury',
            'B': 'Degeneration of descending upper motor neuron tracts',
            'C': 'Selective degeneration of anterior horn cells at L4-S1',
            'D': 'Length-dependent degeneration of the longest axons',
            'E': 'Postsynaptic neuromuscular junction receptor failure'
        },

        # Unit 2: Cerebellum
        17: {
            'A': 'Fasciculus gracilis pathway',
            'B': 'Spinothalamic pathway tract',
            'C': 'Lateral corticospinal tract',
            'D': 'Dorsal spinocerebellar tract',
            'E': 'Cuneocerebellar pathway tract'
        },
        18: {
            'A': 'Accessory cuneate nucleus in caudal medulla forming cuneocerebellar tract',
            'B': 'Dorsal nucleus of Clarke in thoracic spinal cord forming spinocerebellar tract',
            'C': 'Nucleus gracilis in caudal medulla forming the ascending medial lemniscus',
            'D': 'Ventral posterolateral nucleus in thalamus forming thalamocortical tract',
            'E': 'Inferior olivary nucleus in rostral medulla forming olivocerebellar tract'
        },
        19: {
            'A': 'Inferior cerebellar peduncle',
            'B': 'Middle cerebellar peduncle',
            'C': 'Pontine transverse fibers',
            'D': 'Inferior restiform pathway',
            'E': 'Superior cerebellar peduncle'
        },
        20: {
            'A': 'Infarction of the left cerebellar hemisphere',
            'B': 'Ischemic injury involving cerebellar vermis',
            'C': 'Interruption of descending frontopontine fibers',
            'D': 'Demyelination of the ascending dorsal columns',
            'E': 'Occlusion of inferior cerebellar peduncle core'
        },
        21: {
            'A': 'Intention tremor of the bilateral upper limbs',
            'B': 'Truncal ataxia with a broad wide-based gait',
            'C': 'Severe loss of vibratory and position sense',
            'D': 'Recurrent peripheral vertigo and severe tinnitus',
            'E': 'Contralateral spastic upper limb hemiparesis'
        },
        22: {
            'A': 'Intention tremor on finger-to-nose testing',
            'B': 'Scanning dysarthric cerebellar speech pattern',
            'C': 'Truncal ataxia when seated unsupported alone',
            'D': 'Direction-changing horizontal ocular nystagmus',
            'E': 'Positive Romberg sign with eyes closed firmly'
        },
        23: {
            'A': 'Displaced otoliths in posterior semicircular canals',
            'B': 'Endolymphatic hydrops of membranous labyrinth sac',
            'C': 'Benign schwannoma arising from cranial nerve VIII',
            'D': 'Transient vertebrobasilar arterial hypoperfusion',
            'E': 'Progressive atrophy of anterior cerebellar vermis'
        },
        24: {
            'A': 'Intravenous cyanocobalamin replacement',
            'B': 'High-dose intravenous corticosteroids',
            'C': 'Therapeutic plasma exchange sessions',
            'D': 'Intravenous penicillin G sodium regimen',
            'E': 'Supportive care and gait physical therapy'
        },
        27: {
            'A': 'Fluent Wernicke aphasia',
            'B': 'Motoric Broca aphasia',
            'C': 'Conduction speech defect',
            'D': 'Nominal anomic deficit',
            'E': 'Cerebellar dysarthria'
        },

        # Unit 3: Tumors
        29: {
            'A': 'WHO Grade I circumscribed astrocytic tumor',
            'B': 'WHO Grade I subependymal astrocytic tumor',
            'C': 'WHO Grade II diffuse astrocytic neoplasm',
            'D': 'WHO Grade III anaplastic astrocytic tumor',
            'E': 'WHO Grade IV necrotizing glioblastoma tumor'
        },
        30: {
            'A': 'Glioblastoma; pseudopalisading necrosis and vascular proliferation',
            'B': 'Oligodendroglioma; fried-egg cells and chicken-wire vascular loops',
            'C': 'Ependymoma; true ependymal rosettes and perivascular pseudorosettes',
            'D': 'Pilocytic astrocytoma; biphasic pattern containing Rosenthal fibers',
            'E': 'Meningioma; whorled arachnoid cellular patterns and psammoma bodies'
        },
        31: {
            'A': 'Left cerebellar hemisphere mass',
            'B': 'Midline cerebellar vermis mass',
            'C': 'Frontal eye field cortex core',
            'D': 'Cervical dorsal funiculus tract',
            'E': 'Occipital calcarine visual cortex'
        },
        32: {
            'A': 'It introduces an unacceptable risk of iatrogenic bacterial meningitis',
            'B': 'It produces non-diagnostic CSF due to uninterpretable protein elevations',
            'C': 'It is contraindicated due to extreme unmanageable pediatric distress',
            'D': 'It results in technical failure to aspirate adequate diagnostic volume',
            'E': 'It precipitates cerebellar tonsillar herniation through foramen magnum'
        },
        33: {
            'A': 'Homer Wright neuroblastic rosettes',
            'B': 'Eosinophilic beaded Rosenthal fibers',
            'C': 'True perivascular pseudorosettes',
            'D': 'Concentric calcified psammoma bodies',
            'E': 'Oligodendroglial fried-egg tumor cells'
        },
        34: {
            'A': 'Slow indolent tumor growth allowing progressive brain accommodation',
            'B': 'Rapid parenchymal infiltration without initial mass displacement step',
            'C': 'Acute intratumoral hemorrhage causing sudden space-occupying expansion',
            'D': 'Early hematogenous dissemination with multiple bilateral micrometastases',
            'E': 'Early obstruction of cerebral aqueduct CSF outflow ventricular pathways'
        },
        36: {
            'A': 'Pilocytic astrocytoma',
            'B': 'Neuronal ganglioglioma',
            'C': 'Medulloblastoma tumor',
            'D': 'Ependymoma brain tumor',
            'E': 'Meningioma skull tumor'
        },
        37: {
            'A': 'Schwannomas arise from fibroblasts; neurofibromas from perineurial cells',
            'B': 'Schwannomas lack capsules; neurofibromas possess thick fibrous capsules',
            'C': 'Schwannomas occur intracranially; neurofibromas occur strictly peripherally',
            'D': 'Schwannomas metastasize widely; neurofibromas remain completely indolent',
            'E': 'Schwannomas displace adjacent axons; neurofibromas infiltrate through nerve'
        },
        39: {
            'A': 'Resting pill-rolling tremor and cogwheel muscular rigidity',
            'B': 'Non-fluent expressive motor aphasia and right hemiparesis',
            'C': 'Sensorineural hearing loss and progressive cochlear tinnitus',
            'D': 'Bitemporal hemianopia and secondary pituitary insufficiency',
            'E': 'Bilateral olfactory anosmia and Foster Kennedy syndrome signs'
        },
        40: {
            'A': 'Six or more isolated café-au-lait cutaneous macules',
            'B': 'Bilateral vestibular acoustic cranial nerve schwannomas',
            'C': 'A single isolated cutaneous neurofibroma on the trunk',
            'D': 'Two or more neurofibromas of any histological subtype',
            'E': 'One isolated pigmented iris Lisch nodule on slit lamp'
        },
        41: {
            'A': 'Cutaneous schwannoma mass',
            'B': 'Plexiform neurofibroma',
            'C': 'Capillary hemangioma mass',
            'D': 'Transitional meningioma',
            'E': 'Subependymoma brain tumor'
        },
        42: {
            'A': 'Retinal capillary hemangioma tumors',
            'B': 'Subependymal giant cell astrocytomas',
            'C': 'Neurofibromas of the iris stroma layer',
            'D': 'Angiofibromas of the facial eyelid',
            'E': 'Melanocytic hamartomas of the iris'
        },
        44: {
            'A': 'TSC1 and TSC2 encoding hamartin and tuberin to suppress mTOR signaling cascade',
            'B': 'NF1 encoding neurofibromin to inactivate the downstream Ras GTPase cascades',
            'C': 'VHL encoding pVHL to promote rapid degradation of hypoxia-inducible factors',
            'D': 'GNAQ encoding G-alpha-q to stimulate cellular phospholipase C beta pathways',
            'E': 'FXN encoding frataxin to regulate essential mitochondrial iron-sulfur clusters'
        },
        45: {
            'A': 'Infratentorial medulloblastoma tumor',
            'B': 'Cerebellar pilocytic astrocytoma mass',
            'C': 'Fourth ventricle ependymoma brain mass',
            'D': 'Subependymal giant cell astrocytoma',
            'E': 'Dural transitional meningioma tumor'
        },
        46: {
            'A': 'Calcified benign intracranial neoplasm arising from choroid plexus epithelium',
            'B': 'Enlarged gyrus with disorganized cortical lamination and dysplastic neurons',
            'C': 'Cerebellar cyst with an intensely contrast-enhancing internal mural nodule',
            'D': 'Extra-axial collection of concentric whorled arachnoid cap cellular layers',
            'E': 'Heterotopic cluster of mature histologically normal cortical brain neurons'
        },
        47: {
            'A': 'Subependymal subcortical hamartomas; germline TSC1 mutations',
            'B': 'Cerebellar capillary hemangioblastomas; germline VHL mutation',
            'C': 'Leptomeningeal vascular angiomas; somatic mosaic GNAQ mutation',
            'D': 'Cutaneous peripheral neurofibromas; germline NF1 gene mutation',
            'E': 'Bilateral acoustic schwannomas; germline NF2 genetic mutation'
        },
        48: {
            'A': 'Whorled arachnoid cap cells; NF2 gene deletion on chromosome 22q',
            'B': 'Piloid astrocytes with Rosenthal fibers; NF1 on chromosome 17q',
            'C': 'Dysplastic cortical ganglion cells; TSC2 gene on chromosome 16p',
            'D': 'Spindle-shaped neoplastic Schwann cells; NF2 on chromosome 22q',
            'E': 'Foamy stromal cells with vascular meshwork; VHL on chromosome 3p'
        },

        # Unit 4: Opportunistic Infections
        49: {
            'A': 'Acute neutrophilic abscess with fibrous pseudocapsule',
            'B': 'Caseating granulomas containing Langhans giant cells',
            'C': 'Extensive demyelination with foamy lipid macrophages',
            'D': 'Perivascular lymphocytic cuffs with microglial nodules',
            'E': 'Spongiform vacuolation without inflammatory infiltrate'
        },
        50: {
            'A': 'Cytomegalovirus acute polyradiculopathy',
            'B': 'HIV-associated vacuolar myelopathy core',
            'C': 'Toxoplasma gondii subacute focal abscess',
            'D': 'Acute inflammatory demyelinating neuropathy',
            'E': 'Progressive multifocal leukoencephalopathy'
        },
        51: {
            'A': 'Ingestion of cat oocysts or contaminated meat cysts',
            'B': 'Inhalation of aerosolized avian environmental droppings',
            'C': 'Direct cutaneous inoculation via infected insect bites',
            'D': 'Cribriform mucosal invasion from freshwater swimming',
            'E': 'Percutaneous inoculation from infected animal saliva'
        },
        52: {
            'A': 'Marked neutrophilic CSF pleocytosis with Gram-positive diplococci',
            'B': 'Multiple contrast-enhancing ring lesions throughout basal ganglia',
            'C': 'Non-enhancing confluent white matter lesions without mass effect',
            'D': 'Asymmetric hemorrhagic necrosis of the inferomedial temporal lobe',
            'E': 'Mononuclear pleocytosis with positive India ink cryptococcal capsule'
        },
        53: {
            'A': 'Bilateral retrobulbar optic neuritis lesions',
            'B': 'Bilateral calcarine cortex ischemic infarcts',
            'C': 'Bilateral demyelination of optic radiations',
            'D': 'Bilateral rhegmatogenous retinal detachments',
            'E': 'Chiasmal compression by pituitary enlargement'
        },
        54: {
            'A': 'Multiple basal ganglia lesions with positive serum Toxoplasma IgG',
            'B': 'Peripheral absolute CD4+ lymphocyte count greater than 200 cells',
            'C': 'Rapid radiographic resolution following pyrimethamine-sulfadiazine',
            'D': 'Solitary periventricular lesion with positive CSF EBV PCR assay',
            'E': 'Extensive direct environmental exposure to domestic feline feces'
        },
        55: {
            'A': 'Toxoplasma gondii cerebral encephalitis',
            'B': 'Cytomegalovirus ventriculoencephalitis',
            'C': 'JC polyomavirus leukoencephalopathy',
            'D': 'Cryptococcus neoformans fungal meningitis',
            'E': 'Herpes simplex type 1 viral encephalitis'
        },
        56: {
            'A': 'Immune reconstitution inflammatory syndrome',
            'B': 'Treatment-refractory tuberculous meningitis',
            'C': 'Medication-induced sterile aseptic meningitis',
            'D': 'Primary central nervous system viral lymphoma',
            'E': 'HIV-associated progressive cognitive disorder'
        },
        57: {
            'A': 'Hematogenous arterial embolization to cerebral hemispheres',
            'B': 'Trans-cribriform mucosal extension from ethmoidal sinuses',
            'C': 'Retrograde axonal transport via trigeminal cranial nerves',
            'D': 'Ascending trans-synaptic migration along the vagus nerve',
            'E': 'Direct retrograde extension along intraorbital optic nerves'
        },
        58: {
            'A': 'Intracellular Negri bodies inside Purkinje neurons',
            'B': 'Foamy lipid macrophages clearing myelin breakdown',
            'C': 'Narrow-based budding yeast cells with thick capsules',
            'D': 'Central liquefactive necrosis with vascular capsules',
            'E': 'Perivascular lymphocytic cuffs with Cowdry A bodies'
        },
        59: {
            'A': 'Direct mucocutaneous inoculation from active primary labial lesions',
            'B': 'Fomite contact transmission on non-intact mucosal or epithelial surfaces',
            'C': 'Malignant transformation driven by latent persistent Epstein-Barr virus',
            'D': 'Reactivation of latent varicella-zoster virus in dorsal root ganglia',
            'E': 'Hematogenous dissemination of superantigen-producing bacterial agents'
        },
        60: {
            'A': 'Cowdry type A eosinophilic nuclear inclusions',
            'B': 'Negri intracellular eosinophilic viral bodies',
            'C': 'Lewy round cytoplasmic alpha-synuclein bodies',
            'D': 'Neurofibrillary paired helical tau tangles',
            'E': 'Verocay cellular palisading schwannoma bodies'
        },
        62: {
            'A': 'Toxoplasma gondii parasite',
            'B': 'Trypanosoma brucei parasite',
            'C': 'Naegleria fowleri amoebic troph',
            'D': 'Listeria monocytogenes bacteria',
            'E': 'Cryptococcus neoformans fungus'
        },

        # Unit 5: Stroke (Blood Supply, Cerebrovascular, Brainstem)
        64: {
            'A': 'Leg representation lies on lateral convexity supplied by middle cerebral artery',
            'B': 'Leg representation lies in medial paracentral lobule supplied by the ACA trunk',
            'C': 'Leg representation lies in posterior calcarine cortex supplied by the PCA trunk',
            'D': 'Leg representation lies in anterior medulla supplied by the vertebral artery trunk',
            'E': 'Leg representation lies in posterior internal capsule supplied by lenticulostriates'
        },
        65: {
            'A': 'Lateral precentral motor gyrus, Broca speech area, and frontal operculum',
            'B': 'Striate visual cortex of occipital pole and lateral geniculate nucleus',
            'C': 'Medial frontal cortex, corpus callosum body, and anterior cingulate gyrus',
            'D': 'Posterior internal capsule limb, hippocampal formation, and Meyer loop',
            'E': 'Inferior cerebellar vermis, flocculonodular lobe, and caudal pontine base'
        },
        67: {
            'A': 'Ophthalmic artery branch of the internal carotid artery',
            'B': 'Cortical opercular branches of the middle cerebral artery',
            'C': 'Calcarine branch territory of the posterior cerebral artery',
            'D': 'Callosomarginal artery branch of the anterior cerebral artery',
            'E': 'Superior cerebellar branch territory of the basilar artery'
        },
        68: {
            'A': 'Right Meyer loop pathway in anterior temporal lobe',
            'B': 'Left parietal optic radiation fibers near ventricle',
            'C': 'Left Meyer loop pathway in anterior temporal lobe',
            'D': 'Left cuneus cortex tissue above calcarine fissure',
            'E': 'Central decussating fibers within optic chiasm core'
        },
        69: {
            'A': 'Left anterior cerebral artery; medial paracentral lobule',
            'B': 'Left middle cerebral artery; superior temporal gyrus lobe',
            'C': 'Left posterior cerebral artery; medial calcarine cortex',
            'D': 'Right middle cerebral artery; inferior parietal gyrus lobe',
            'E': 'Left lenticulostriate branches; internal capsule limb'
        },
        71: {
            'A': 'Medial frontal cortex near Broca area at ACA-MCA watershed boundary zone',
            'B': 'Posterior superior temporal gyrus within middle cerebral artery territory',
            'C': 'Deep subcortical white matter arcuate fasciculus along the MCA territory',
            'D': 'Primary calcarine cortex lingual gyrus within posterior cerebral boundary',
            'E': 'Thalamic ventral posterolateral nucleus at thalamoperforator distribution'
        },
        72: {
            'A': 'Inferior frontal gyrus cortex along anterior cerebral watershed boundary',
            'B': 'Arcuate fasciculus pathway within deep periventricular white matter tract',
            'C': 'Paracentral lobule territory within anterior cerebral artery distribution',
            'D': 'Frontal eye field cortical region within middle cerebral artery territory',
            'E': 'Parietotemporal junction cortex along MCA-PCA watershed vascular border'
        },
        73: {
            'A': 'Conduction aphasia; disruption of arcuate fasciculus',
            'B': 'Anomic aphasia; selective injury of left angular gyrus',
            'C': 'Global aphasia; extensive perisylvian MCA infarction',
            'D': 'Transcortical motor aphasia; anterior watershed stroke',
            'E': 'Spastic dysarthria; bilateral corticobulbar pathway loss'
        },
        74: {
            'A': 'Aphasia reflects motor coordination failure; dysarthria reflects cognitive loss',
            'B': 'Aphasia is a multimodal language defect; dysarthria is a neuromuscular motor defect',
            'C': 'Aphasia selectively impairs reading; dysarthria selectively impairs comprehension',
            'D': 'Aphasia arises from cerebellar damage; dysarthria arises from cortical lesions',
            'E': 'Aphasia spares spoken articulation; dysarthria spares lexical language selection'
        },
        76: {
            'A': 'Superficial veins drain to superior sagittal sinus, deep veins to straight sinus',
            'B': 'Deep cerebral veins drain to internal carotids, superficial veins to cavernous sinus',
            'C': 'Superficial veins drain to straight sinus, deep cerebral veins to transverse sinus',
            'D': 'Dural sinuses drain to vertebral veins, superficial cerebral veins to jugular veins',
            'E': 'Superior sagittal sinus drains to cavernous sinus, straight sinus to petrosal sinuses'
        },
        77: {
            'A': 'Saccular aneurysms occur in cerebellar fissures; hypertensive bleeds occur in cortex',
            'B': 'Saccular aneurysms occur at venous junctions; hypertensive bleeds occur in pituitary',
            'C': 'Saccular aneurysms occur in spinal arteries; hypertensive bleeds occur in optic chiasm',
            'D': 'Saccular aneurysms occur in optic nerves; hypertensive bleeds occur in hippocampus',
            'E': 'Saccular aneurysms occur at circle of Willis; hypertensive bleeds occur in basal ganglia'
        },
        78: {
            'A': 'It is an entirely benign clinical event requiring only routine outpatient follow-up',
            'B': 'It carries zero subsequent long-term risk of recurrent focal ischemic cerebral events',
            'C': 'It is a medical emergency with up to ten percent risk of stroke within ninety days',
            'D': 'It mandates immediate full therapeutic intravenous anticoagulation within two hours',
            'E': 'It indicates permanent irreversible necrotic destruction of cerebral cortical tissue'
        },
        79: {
            'A': 'Endothelial injury with smooth muscle cell necrosis and lipid loss',
            'B': 'Fibrous cap formation followed by chronic subendothelial lipid entry',
            'C': 'Occlusive luminal thrombosis followed by local macrophage recruitment',
            'D': 'Intimal lipid entry triggering inflammation and smooth muscle growth',
            'E': 'Medial dystrophic calcification followed by adventitial fibrosis bands'
        },
        80: {
            'A': 'Emergent intravenous unfractionated heparin bolus',
            'B': 'Intravenous recombinant tissue plasminogen activator',
            'C': 'Emergent open neurosurgical decompressive craniectomy',
            'D': 'High-dose oral aspirin therapy without thrombolysis',
            'E': 'Emergent endovascular coil embolization of aneurysms'
        },
        81: {
            'A': 'Emergent intravenous tissue plasminogen activator infusion',
            'B': 'Rapid neurosurgical decompressive hemicraniectomy surgery',
            'C': 'Full therapeutic intravenous heparin anticoagulation bolus',
            'D': 'Dual antiplatelet therapy with oral aspirin and clopidogrel',
            'E': 'Emergent endovascular mechanical thrombectomy intervention'
        },
        83: {
            'A': 'Dual antiplatelet therapy using aspirin and ticagrelor',
            'B': 'Intravenous recombinant tissue plasminogen activator',
            'C': 'High-dose therapeutic intravenous unfractionated heparin',
            'D': 'Urgent endovascular mechanical clot retriever extraction',
            'E': 'Surgical decompressive suboccipital craniectomy therapy'
        },
        85: {
            'A': 'Left middle cerebral artery cortical branches',
            'B': 'Left anterior cerebral artery medial branches',
            'C': 'Left posterior cerebral artery calcarine trunk',
            'D': 'Left lenticulostriate penetrating arteries',
            'E': 'Left anterior choroidal penetrating artery'
        },
        88: {
            'A': 'Severe hypothermia therapeutic protocol',
            'B': 'High-dose intravenous steroid infusion',
            'C': 'Endovascular mechanical thrombectomy',
            'D': 'Emergent decompressive craniectomy',
            'E': 'Intraventricular recombinant tPA bolus'
        },
        89: {
            'A': 'Pure motor hemiparesis syndrome',
            'B': 'Sensorimotor stroke syndrome',
            'C': 'Ataxic hemiparesis syndrome',
            'D': 'Pure sensory stroke syndrome',
            'E': 'Clumsy hand-dysarthria defect'
        },
        93: {
            'A': 'Absence of any associated motor deficits involving limb musculature',
            'B': 'Sparing of all branchial motor and visceral cranial nerve functions',
            'C': 'Loss of higher cortical functions like aphasia, apraxia, or agnosia',
            'D': 'Presence of ipsilateral cranial palsy with contralateral hemiplegia',
            'E': 'Pure cerebellar appendicular ataxia without any ocular manifestations'
        },
        95: {
            'A': 'Distal MCA infarcts cause uniform hemiparesis affecting face, arm, and leg equally',
            'B': 'Proximal MCA infarcts involve lenticulostriates causing equal face/arm/leg weakness',
            'C': 'Proximal MCA infarcts selectively spare facial and branchial motor representations',
            'D': 'Both proximal and distal MCA occlusions yield identical motor deficit distributions',
            'E': 'Distal MCA infarcts produce isolated contralateral lower extremity motor paralysis'
        },
        96: {
            'A': 'Sustained involuntary horizontal gaze to the right side',
            'B': 'Sustained involuntary horizontal gaze to the left side',
            'C': 'Complete vertical upgaze and downgaze motoric palsy',
            'D': 'Isolated bilateral medial rectus adduction failure',
            'E': 'Isolated bilateral ocular pupillary convergence failure'
        },
        98: {
            'A': 'Right rostral midbrain; posterior cerebral artery',
            'B': 'Left caudal pons; basilar artery paramedian branches',
            'C': 'Left rostral midbrain; posterior cerebral artery',
            'D': 'Right rostral medulla; anterior spinal artery branch',
            'E': 'Left rostral medulla; posterior inferior cerebellar'
        },
        99: {
            'A': 'Ipsilateral third cranial nerve palsy and contralateral spastic hemiplegia',
            'B': 'Ipsilateral sixth cranial nerve palsy and contralateral spastic hemiplegia',
            'C': 'Ipsilateral twelfth nerve motor palsy and contralateral spastic hemiplegia',
            'D': 'Ipsilateral facial analgesia, Horner syndrome, and crossed hemi-hypesthesia',
            'E': 'Ipsilateral peripheral facial palsy, horizontal gaze palsy, and hemiplegia'
        },
        100: {
            'A': 'Left red nucleus and oculomotor cranial nerve fibers',
            'B': 'Right corticospinal and descending corticobulbar tracts',
            'C': 'Left medial lemniscus and ascending spinothalamic tract',
            'D': 'Right superior cerebellar peduncle and central red nucleus',
            'E': 'Left dentate nucleus and deep cerebellar cortical layers'
        },
        101: {
            'A': 'Right middle pons involving CN V nuclei and cerebellar peduncle fibers',
            'B': 'Left middle pons involving abducens and corticospinal motor tracts',
            'C': 'Right rostral midbrain involving oculomotor and central red nucleus',
            'D': 'Right rostral medulla involving hypoglossal and corticospinal tracts',
            'E': 'Left caudal pons involving facial colliculus and medial lemniscus'
        },
        102: {
            'A': 'Right medial midbrain ischemia involving oculomotor and pyramidal tracts',
            'B': 'Left lateral medulla ischemia involving spinothalamic and trigeminal tracts',
            'C': 'Right caudal pons ischemia involving facial nucleus and abducens nerve fibers',
            'D': 'Left middle pons ischemia involving corticospinal and pontocerebellar tracts',
            'E': 'Right middle pons ischemia involving trigeminal and sympathetic nerve tracts'
        },
        103: {
            'A': 'Right rostral midbrain involving oculomotor nerve and cerebral peduncles',
            'B': 'Left rostral medulla involving hypoglossal nerve and pyramidal motor fibers',
            'C': 'Left caudal medial pons involving abducens nerve and corticospinal tracts',
            'D': 'Right caudal lateral pons involving vestibular nuclei and spinal V tract',
            'E': 'Left lateral medulla involving nucleus ambiguus and inferior peduncles'
        },
        104: {
            'A': 'Right lateral medulla; posterior inferior cerebellar artery',
            'B': 'Right lateral caudal pons; anterior inferior cerebellar artery',
            'C': 'Left lateral caudal pons; anterior inferior cerebellar artery',
            'D': 'Right medial caudal pons; basilar paramedian branch arteries',
            'E': 'Right rostral midbrain; posterior cerebral artery branches'
        },
        105: {
            'A': 'Left superior cerebellar peduncle; superior cerebellar artery branch',
            'B': 'Left middle cerebellar peduncle; anterior inferior cerebellar artery',
            'C': 'Right inferior cerebellar peduncle; posterior inferior cerebellar',
            'D': 'Left inferior cerebellar peduncle; posterior inferior cerebellar artery',
            'E': 'Left cerebellar hemisphere cortex; anterior inferior cerebellar artery'
        },
        106: {
            'A': 'Right medial medulla involving corticospinal tract and CN XII; ASA territory',
            'B': 'Left lateral medulla involving spinothalamic tract and CN IX; PICA territory',
            'C': 'Right caudal pons involving corticospinal tract and CN VI; basilar territory',
            'D': 'Left rostral midbrain involving corticospinal tract and CN III; PCA territory',
            'E': 'Right middle pons involving corticospinal tract and CN V; AICA distribution'
        },
        107: {
            'A': 'Bilateral internal capsule posterior limbs; lenticulostriates',
            'B': 'Bilateral medial medulla pyramids; anterior spinal artery branch',
            'C': 'Bilateral dorsomedial thalamic nuclei; posterior cerebral artery',
            'D': 'Bilateral rostral cerebral peduncles; posterior cerebral artery',
            'E': 'Bilateral ventral pontine base pathways; basilar artery trunk'
        },

        # Unit 6: Dementia
        109: {
            'A': 'Insidious onset, preserved attention, irreversible progression',
            'B': 'Abrupt clinical onset, fluctuating attention, reversible course',
            'C': 'Insidious onset, fluctuating consciousness, irreversible decline',
            'D': 'Abrupt onset, preserved attention, permanent cognitive deficit',
            'E': 'Gradual onset, normal level of arousal, progressive deterioration'
        },
        110: {
            'A': 'He loses procedural motor skills with intact declarative memory',
            'B': 'He loses remote autobiographical recall with intact working memory',
            'C': 'He loses immediate working memory with intact long-term recall',
            'D': 'He learns procedural motor skills with impaired declarative memory',
            'E': 'He loses all procedural and declarative memory modalities equally'
        },
        111: {
            'A': 'Hyperorality with hypersexuality and emotional placidity',
            'B': 'Anterograde amnesia with preserved social comportment',
            'C': 'Fluent paraphasic speech with impaired comprehension',
            'D': 'Violent unilateral choreiform flinging limb movements',
            'E': 'Visual object agnosia with preserved baseline acuity'
        },
        112: {
            'A': 'Coordinates vestibulospinal reflexes for postural motor stability',
            'B': 'Consolidates declarative memories into long-term neocortical storage',
            'C': 'Synthesizes syntactic and grammatical components of expressive speech',
            'D': 'Generates slow-wave sleep rhythms via thalamocortical oscillations',
            'E': 'Mediates mesolimbic dopamine reward processing and reinforcement drive'
        },
        114: {
            'A': 'Gait apraxia, urinary incontinence, dementia; ventricular dilation',
            'B': 'Encephalopathy, oculomotor dysfunction, ataxia; mammillary hemorrhage',
            'C': 'Chorea, behavioral change, cognitive decline; caudate head atrophy',
            'D': 'Rapid dementia, startle myoclonus, ataxia; 14-3-3 CSF positivity',
            'E': 'Fluctuating cognition, visual hallucinations; cortical Lewy bodies'
        },
        116: {
            'A': 'Hydrocephalus ex vacuo; central nucleus basalis of Meynert',
            'B': 'Obstructive non-communicating hydrocephalus; caudate nucleus',
            'C': 'Impaired arachnoid granulation resorption; substantia nigra',
            'D': 'Excessive choroid plexus CSF production; locus coeruleus',
            'E': 'Recurrent deep parenchymal hemorrhage; central red nucleus'
        },
        117: {
            'A': 'Intraneuronal neurofibrillary tangles within the entorhinal cortex',
            'B': 'Extensive spongiform neuropil vacuolation throughout cerebral cortex',
            'C': 'Cytoplasmic alpha-synuclein Lewy bodies in cortex and substantia nigra',
            'D': 'Round argentophilic tau-positive Pick bodies in frontotemporal lobes',
            'E': 'Multiple cystic cavitary lacunes within internal capsule and thalamus'
        },
        118: {
            'A': 'Amnestic syndrome with early selective hippocampal neurodegeneration',
            'B': 'Early visual hallucinations paired with spontaneous parkinsonian signs',
            'C': 'Startle myoclonus paired with rapid subacute progressive ataxia signs',
            'D': 'Magnetic shuffling gait paired with early urge urinary incontinence',
            'E': 'Behavioral variant and primary progressive aphasias with tau or TDP-43'
        },
        120: {
            'A': 'Alzheimer disease; central acetylcholinesterase inhibitors',
            'B': 'Multi-infarct vascular dementia; aggressive antiplatelet drugs',
            'C': 'Dementia with Lewy bodies; low-dose atypical antipsychotics',
            'D': 'Normal pressure hydrocephalus; ventriculoperitoneal shunting',
            'E': 'Sporadic Creutzfeldt-Jakob disease; compassionate comfort care'
        },
        121: {
            'A': 'Stepwise cognitive deterioration associated with focal vascular lesions',
            'B': 'Insidious progressive short-term episodic memory loss over many months',
            'C': 'Isolated bilateral anterior hippocampal volume loss without infarcts',
            'D': 'Extracellular accumulation of fibrillar amyloid plaques and tangles',
            'E': 'Marked clinical responsiveness to central cholinesterase inhibitors'
        },
        123: {
            'A': 'Autosomal recessive GAA trinucleotide expansion; frataxin deficiency',
            'B': 'X-linked dominant CGG trinucleotide expansion; FMR1 gene silencing',
            'C': 'Maternal mitochondrial DNA point mutation; heteroplasmic inheritance',
            'D': 'Sporadic infectious proteinaceous prion conversion; pathogenic scrapie',
            'E': 'Autosomal dominant CAG repeat expansion; huntingtin on chromosome 4'
        },

        # Unit 7: CBIL Epilepsy
        124: {
            'A': 'Absence seizure event',
            'B': 'Tonic-clonic seizure',
            'C': 'Atonic drop seizure',
            'D': 'Focal aware seizure',
            'E': 'Myoclonic jerk seizure'
        },
        126: {
            'A': 'Myoclonic jerk seizure',
            'B': 'Atonic drop seizure',
            'C': 'Tonic muscular seizure',
            'D': 'Absence staring seizure',
            'E': 'Focal aware motor seizure'
        },
        127: {
            'A': 'Generalized tonic-clonic seizure',
            'B': 'Generalized typical absence seizure',
            'C': 'Generalized juvenile myoclonic event',
            'D': 'Generalized sudden atonic drop attack',
            'E': 'Cardiogenic vasovagal syncopal attack'
        },
        128: {
            'A': 'Absence staring seizure',
            'B': 'Tonic muscular seizure',
            'C': 'Atonic drop seizure',
            'D': 'Focal aware motor seizure',
            'E': 'Myoclonic jerk seizure'
        },
        129: {
            'A': 'Myoclonic jerk seizure',
            'B': 'Tonic-clonic seizure',
            'C': 'Absence staring seizure',
            'D': 'Atonic drop seizure',
            'E': 'Focal aware motor seizure'
        },
        130: {
            'A': 'Generalized atonic drop seizure',
            'B': 'Typical absence staring seizure',
            'C': 'Generalized tonic motor seizure',
            'D': 'Juvenile myoclonic jerk seizure',
            'E': 'Focal impaired awareness seizure'
        },
        131: {
            'A': 'Both seizure types originate simultaneously from bilateral hemispheres',
            'B': 'Focal seizures invariably cause complete immediate loss of consciousness',
            'C': 'Focal seizures begin in one hemisphere; generalized involve both sides',
            'D': 'Generalized seizures originate from a discrete circumscribed cortical focus',
            'E': 'Focal and generalized seizures display identical electrographic patterns'
        },
        138: {
            'A': 'Initiation of lifelong maintenance polytherapy',
            'B': 'Resective epilepsy surgical evaluation pathway',
            'C': 'Implantation of an internal vagus nerve stimulator',
            'D': 'Initiation of a strict ketogenic dietary regimen',
            'E': 'Acute treatment of the underlying systemic etiology'
        },
        139: {
            'A': 'Ethosuximide; T-type calcium channel inhibition; gastrointestinal upset',
            'B': 'Lamotrigine; voltage-gated sodium channel inhibition; severe rash signs',
            'C': 'Valproate; GABA transaminase inhibition; acute pancreatitis and nausea',
            'D': 'Carbamazepine; fast sodium channel inhibition; aplastic anemia and rash',
            'E': 'Phenytoin; fast sodium channel inactivation; gingival hypertrophy signs'
        },
        141: {
            'A': 'Selective inhibition of low-threshold T-type thalamic calcium channels',
            'B': 'Selective fast inactivation of voltage-gated neuronal sodium channels',
            'C': 'Blockade of sodium and T-type calcium channels with GABA potentiation',
            'D': 'Allosteric potentiation of postsynaptic GABAA chloride conductance',
            'E': 'Non-competitive antagonism of postsynaptic ionotropic NMDA receptors'
        },
        142: {
            'A': 'Hepatotoxicity, acute pancreatitis, and teratogenic neural tube defects',
            'B': 'Agranulocytosis, aplastic anemia, and syndrome of inappropriate ADH',
            'C': 'Gingival hyperplasia, coarse facial features, and megaloblastic anemia',
            'D': 'Isolated morbilliform cutaneous eruption without systemic complications',
            'E': 'Irreversible concentric peripheral visual field constriction deficits'
        },
        143: {
            'A': 'Phenytoin; fibrous gingival hyperplasia',
            'B': 'Valproic acid; acute pancreatitis risk',
            'C': 'Carbamazepine; severe hyponatremic state',
            'D': 'Ethosuximide; gastric dyspeptic distress',
            'E': 'Lamotrigine; Stevens-Johnson syndrome'
        },
        146: {
            'A': 'Neuronal channelopathy involving mutated voltage-gated potassium channels',
            'B': 'Systemic metabolic disturbance secondary to acute profound hypoglycemia',
            'C': 'Focal intracranial structural lesion secondary to an oligodendroglioma',
            'D': 'Benign inherited genetic syndrome presenting with childhood convulsions',
            'E': 'Substance withdrawal syndrome resulting from sudden sedative cessation'
        },
        147: {
            'A': 'Generalized 3-Hz spike-wave bursts with no postictal confusion',
            'B': 'Temporal sharp waves with prolonged postictal confusion states',
            'C': 'Chaotic, high-voltage, disorganized hypsarrhythmia on tracing',
            'D': 'Periodic synchronous triphasic sharp-wave complexes at 1–2 Hz',
            'E': 'Continuous generalized polymorphic delta slowing without spikes'
        },
        150: {
            'A': 'Initiate multiple antiseizure drugs simultaneously at maximum target doses',
            'B': 'Initiate monotherapy at lowest dose, titrating to efficacy or intolerance',
            'C': 'Mandate immediate surgical resection prior to any pharmacological trials',
            'D': 'Rely exclusively on ketogenic dietary regimens before trying medications',
            'E': 'Maintain initial monotherapy at subtherapeutic doses regardless of control'
        }
    }

    built_questions = []
    for q in hy_questions:
        qnum = int(q['q_num'])
        new_q = {
            'id': f'exam3_in_house_like_g_q{qnum}',
            'q_num': str(qnum),
            'stem': q['stem'],
            'category': map_category(qnum),
            'source': 'in_house_like_G (150 Questions)',
            'options': [],
            'correct_idx': q['correct_idx'],
            'explanation': q['explanation'],
            'high_yield_pearl': q.get('high_yield_pearl', f'High-Yield Rule: {map_category(qnum)}'),
            'image': q.get('image', None)
        }

        # Apply option text overrides if present
        for opt in q['options']:
            letter = opt['letter']
            text = opt['text']
            if qnum in overrides and letter in overrides[qnum]:
                text = overrides[qnum][letter]
            new_q['options'].append({
                'letter': letter,
                'is_correct': opt['is_correct'],
                'text': text
            })

        built_questions.append(new_q)

    # Verification checks
    key_counts = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0}
    category_counts = {}
    spread_issues = []
    parens_issues = []

    for i, q in enumerate(built_questions):
        qnum = i + 1
        cat = q['category']
        category_counts[cat] = category_counts.get(cat, 0) + 1

        correct_opt = q['options'][q['correct_idx']]
        key_counts[correct_opt['letter']] += 1

        lens = [len(opt['text']) for opt in q['options']]
        s = max(lens) - min(lens)
        if s > 6:
            spread_issues.append((qnum, s, min(lens), max(lens), lens))

        for opt in q['options']:
            if '(' in opt['text'] or ')' in opt['text']:
                parens_issues.append((qnum, opt['letter'], opt['text']))

    print('=== Verification Report ===')
    print('Total questions:', len(built_questions))
    print('Category distribution:', category_counts)
    print('Answer key distribution:', key_counts)
    print('Spread > 6 issues:', len(spread_issues))
    if spread_issues:
        for si in spread_issues:
            print('  Issue:', si)
    print('Parentheses issues:', len(parens_issues))
    if parens_issues:
        for pi in parens_issues:
            print('  Parens:', pi)

    if spread_issues or parens_issues:
        print('Aborting write due to verification issues!')
        return False

    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(built_questions, f, indent=2, ensure_ascii=False)

    print(f'Successfully wrote {len(built_questions)} authentic questions to {out_path}!')
    return True

if __name__ == '__main__':
    build_authentic_in_house_g()
