import json

in_path = '/Users/markyoussef_1/.gemini/antigravity-ide/scratch/usmle_exam1/exam3_high_yield_questions.json'
with open(in_path, 'r', encoding='utf-8') as f:
    questions = json.load(f)

overrides = {
    4: {
        'A': 'Paramedian pontine reticular formation',
        'B': 'Abducens somatic motor nucleus',
        'C': 'Oculomotor visceral motor nucleus',
        'D': 'Medial longitudinal fasciculus',
        'E': 'Cortical frontal eye field center'
    },
    5: {
        'A': 'Primary progressive multiple sclerosis',
        'B': 'Relapsing-remitting multiple sclerosis',
        'C': 'Secondary progressive multiple sclerosis',
        'D': 'Clinically isolated demyelinating syndrome',
        'E': 'Neuromyelitis optica spectrum disease'
    },
    9: {
        'A': 'It replaces deficient peripheral myelin proteins',
        'B': 'It clears circulating autoantibodies and cytokines',
        'C': 'It directly stimulates axonal remyelination',
        'D': 'It eliminates persistent bacterial antigens',
        'E': 'It competitively blocks acetylcholine receptors'
    },
    10: {
        'A': 'Pheochromocytoma',
        'B': 'Systemic sepsis',
        'C': 'Pulmonary embolism',
        'D': 'Autonomic instability',
        'E': 'Myocardial infarction'
    },
    11: {
        'A': 'Friedreich ataxia; trinucleotide frataxin gene mutation',
        'B': 'Guillain-Barré syndrome; peripheral ganglioside antibodies',
        'C': 'Spinal muscular atrophy; survival motor neuron 1 deletion',
        'D': 'Subacute combined degeneration; cobalamin deficiency',
        'E': 'Charcot-Marie-Tooth disease; peripheral myelin protein 22'
    },
    13: {
        'A': 'Subcutaneous interferon-beta',
        'B': 'Subcutaneous glatiramer acetate',
        'C': 'Intravenous corticosteroids',
        'D': 'Intravenous natalizumab',
        'E': 'Intravenous ocrelizumab'
    },
    16: {
        'A': 'Resting tremor and muscular rigidity',
        'B': 'Truncal ataxia and prominent nystagmus',
        'C': 'Intention tremor and limb dysmetria',
        'D': 'Contralateral spastic hemiparesis',
        'E': 'Expressive motor dysphasic speech'
    },
    18: {
        'A': 'Accessory cuneate nucleus in caudal medulla (cuneocerebellar tract)',
        'B': 'Dorsal nucleus of Clarke in the spinal cord (spinocerebellar tract)',
        'C': 'Nucleus gracilis in the caudal medulla (ascending medial lemniscus)',
        'D': 'Ventral posterolateral nucleus in thalamus (thalamocortical tract)',
        'E': 'Inferior olivary nucleus in rostral medulla (olivocerebellar tract)'
    },
    21: {
        'A': 'Intention tremor of the upper limbs',
        'B': 'Truncal ataxia with a wide-based gait',
        'C': 'Loss of vibratory and position sense',
        'D': 'Peripheral vertigo and tinnitus',
        'E': 'Contralateral spastic hemiparesis'
    },
    25: {
        'A': 'Lysosome; basal ganglia and internal globus pallidus',
        'B': 'Peroxisome; lateral hemisphere and dentate nucleus',
        'C': 'Mitochondria; dorsal columns and spinocerebellar tracts',
        'D': 'Golgi apparatus; primary motor cortex and pyramids',
        'E': 'Nucleus; ventral anterior and ventral lateral thalamus'
    },
    29: {
        'A': 'WHO Grade I (circumscribed pediatric astrocytoma)',
        'B': 'WHO Grade I (subependymal giant cell astrocytoma)',
        'C': 'WHO Grade II (diffuse low-grade oligodendroglioma)',
        'D': 'WHO Grade III (anaplastic malignant astrocytoma)',
        'E': 'WHO Grade IV (glioblastoma with microvascular necrosis)'
    },
    33: {
        'A': 'Homer Wright neural rosettes',
        'B': 'Eosinophilic Rosenthal fibers',
        'C': 'Perivascular pseudorosettes',
        'D': 'Calcified psammoma bodies',
        'E': 'Oligodendroglial fried-egg cells'
    },
    35: {
        'A': 'Infratentorial pediatric tumor; cystic with Rosenthal fibers',
        'B': 'Intraventricular pediatric tumor; perivascular pseudorosettes',
        'C': 'Extra-axial adult dural tumor; psammoma bodies and whorls',
        'D': 'Supratentorial adult tumor; fried-egg cells and capillaries',
        'E': 'Cerebellopontine angle tumor; biphasic Antoni A and B pattern'
    },
    39: {
        'A': 'Resting pill-rolling tremor and cogwheel rigidity',
        'B': 'Non-fluent expressive aphasia and right hemiparesis',
        'C': 'Sensorineural hearing loss and progressive tinnitus',
        'D': 'Bitemporal hemianopia and pituitary insufficiency',
        'E': 'Bilateral anosmia and Foster Kennedy syndrome'
    },
    42: {
        'A': 'Retinal capillary hemangiomas',
        'B': 'Subependymal giant cell astrocytomas',
        'C': 'Neurofibromas of the iris stroma',
        'D': 'Angiofibromas of the malar eyelid',
        'E': 'Melanocytic hamartomas of the iris'
    },
    43: {
        'A': 'Neurofibromatosis type 1; chromosome 17',
        'B': 'Tuberous sclerosis complex; chromosome 9',
        'C': 'Neurofibromatosis type 2; chromosome 22',
        'D': 'Von Hippel-Lindau disease; chromosome 3',
        'E': 'Sturge-Weber syndrome; chromosome 9q'
    },
    45: {
        'A': 'Infratentorial medulloblastoma',
        'B': 'Cerebellar pilocytic astrocytoma',
        'C': 'Fourth ventricle ependymoma',
        'D': 'Subependymal giant cell astrocytoma',
        'E': 'Dural transitional meningioma'
    },
    48: {
        'A': 'Whorled arachnoid cap cells; NF2 gene on chromosome 22q',
        'B': 'Piloid astrocytes with Rosenthal fibers; NF1 on chromosome 17q',
        'C': 'Dysplastic ganglion cells; TSC2 gene on chromosome 16p',
        'D': 'Spindle-shaped Schwann cells; NF2 gene on chromosome 22q',
        'E': 'Foamy stromal cells with vascular meshwork; VHL on chromosome 3p'
    },
    50: {
        'A': 'Cytomegalovirus polyradiculopathy',
        'B': 'HIV-associated vacuolar myelopathy',
        'C': 'Toxoplasma gondii myelitis abscess',
        'D': 'Acute inflammatory demyelinating neuropathy',
        'E': 'Progressive multifocal leukoencephalopathy'
    },
    63: {
        'A': 'Thick mucopolysaccharide capsule',
        'B': 'Acid-fast filamentous branching',
        'C': 'Gram-negative encapsulated rods',
        'D': 'Intranuclear viral inclusions',
        'E': 'Characteristic tumbling motility'
    },
    66: {
        'A': 'It traverses horizontally through the sylvian fissure',
        'B': 'It ascends vertically over the lateral cerebral convexity',
        'C': 'It supplies the deep insular and opercular neocortex',
        'D': 'It arises directly from the extracranial vertebral artery',
        'E': 'It curves anteriorly and arching around corpus callosum'
    },
    69: {
        'A': 'Left anterior cerebral artery; medial paracentral lobule',
        'B': 'Left middle cerebral artery; superior temporal gyrus',
        'C': 'Left posterior cerebral artery; medial calcarine cortex',
        'D': 'Right middle cerebral artery; inferior parietal lobule',
        'E': 'Left lenticulostriate artery; internal capsule posterior limb'
    },
    70: {
        'A': 'Left superior temporal gyrus; MCA inferior division',
        'B': 'Right frontal eye field cortex; MCA superior division',
        'C': 'Left arcuate fasciculus tract; MCA cortical branches',
        'D': 'Left inferior frontal gyrus; MCA superior division',
        'E': 'Left angular parietal gyrus; PCA cortical branches'
    },
    73: {
        'A': 'Conduction aphasia; disruption of arcuate fasciculus',
        'B': 'Anomic aphasia; disruption of left angular gyrus',
        'C': 'Global aphasia; extensive perisylvian MCA infarction',
        'D': 'Transcortical motor aphasia; anterior watershed stroke',
        'E': 'Spastic dysarthria; bilateral corticobulbar damage'
    },
    75: {
        'A': 'Midbrain: basilar artery; pons: PCA; medulla: AICA',
        'B': 'Midbrain: PICA; pons: anterior spinal; medulla: SCA',
        'C': 'Midbrain: AICA; pons: PICA branch; medulla: PCA',
        'D': 'Midbrain: PCA; pons: SCA and AICA; medulla: PICA',
        'E': 'Midbrain: PCoA; pons: PCoA branch; medulla: PCoA'
    },
    79: {
        'A': 'Intimal smooth muscle necrosis followed by lipid dissolution',
        'B': 'Fibrous cap formation followed by subendothelial lipid entrapment',
        'C': 'Occlusive luminal thrombosis followed by macrophage recruitment',
        'D': 'Intimal lipid entry triggering inflammation and smooth muscle growth',
        'E': 'Medial dystrophic calcification followed by adventitial fibrosis'
    },
    81: {
        'A': 'Renal arterial branches and hepatic portal system',
        'B': 'Pulmonary capillary bed and splenic red pulp sinusoids',
        'C': 'Deep venous plexus of the lower extremities',
        'D': 'Cutaneous terminal arterioles and muscular venules',
        'E': 'Left cardiac chambers and internal carotid bifurcation'
    },
    84: {
        'A': 'Expectant observation with serial noncontrast CT scans',
        'B': 'Surgical clipping or endovascular coiling of aneurysm',
        'C': 'Intravenous recombinant tissue plasminogen activator',
        'D': 'Fractionated stereotactic whole-brain radiation beam',
        'E': 'Emergent surgical carotid endarterectomy procedure'
    },
    86: {
        'A': 'Immediate lumbar puncture, followed by urgent spine MRI',
        'B': 'Electroencephalography, followed by contrast brain MRI',
        'C': 'Catheter angiography, followed by magnetic resonance',
        'D': 'Transesophageal echo, followed by noncontrast head CT',
        'E': 'Noncontrast cranial CT, followed by CT angiography'
    },
    87: {
        'A': 'Hippocampal pyramidal cells and cerebellar Purkinje neurons',
        'B': 'Dorsal vagal motor nucleus and pontine reticular formation',
        'C': 'Caudate nucleus head and internal globus pallidus neurons',
        'D': 'Thoracic intermediate column and anterior horn motor cells',
        'E': 'Mammillary bodies and hypothalamic neurosecretory neurons'
    },
    89: {
        'A': 'Persistent bilateral absence of pupillary light reflexes',
        'B': 'Isoelectric flat electroencephalographic recording',
        'C': 'Complete flaccid quadriplegia without motor response',
        'D': 'Irreversible coma with absent brainstem reflexes and apnea',
        'E': 'Persistent hyperventilation on mechanical ventilatory support'
    },
    90: {
        'A': 'Midbrain level; indicative of reversible metabolic stupor',
        'B': 'Pontomedullary vestibulo-ocular tract; irreversible injury',
        'C': 'Primary cerebral cortex; indicative of preserved reflexes',
        'D': 'Cervical spinal cord; indicative of reversible shock state',
        'E': 'Anterior cerebellar vermis; unrelated to brainstem function'
    },
    92: {
        'A': 'III, IV, V1, V2, and VI',
        'B': 'I, II, III, IV, and VII',
        'C': 'V3, VII, VIII, IX, and X',
        'D': 'II, III, V3, VII, and XI',
        'E': 'III, V3, VIII, XI, and XII'
    },
    100: {
        'A': 'Left red nucleus and oculomotor nerve fibers',
        'B': 'Right corticospinal and corticobulbar tracts',
        'C': 'Left medial lemniscus and spinothalamic tract',
        'D': 'Right superior cerebellar peduncle and red nucleus',
        'E': 'Left dentate nucleus and cerebellar cortex'
    },
    102: {
        'A': 'Right medial midbrain ischemia involving oculomotor and pyramidal tracts',
        'B': 'Left lateral medulla ischemia involving spinothalamic and trigeminal tracts',
        'C': 'Right caudal pons ischemia involving facial nucleus and abducens fibers',
        'D': 'Left middle pons ischemia involving corticospinal and pontocerebellar tracts',
        'E': 'Right middle pons ischemia involving trigeminal and descending sympathetic tracts'
    },
    105: {
        'A': 'Left superior cerebellar peduncle; superior cerebellar artery',
        'B': 'Left middle cerebellar peduncle; anterior inferior cerebellar artery',
        'C': 'Right inferior cerebellar peduncle; posterior inferior cerebellar artery',
        'D': 'Left inferior cerebellar peduncle; posterior inferior cerebellar artery',
        'E': 'Left cerebellar hemisphere cortex; anterior inferior cerebellar artery'
    },
    107: {
        'A': 'Bilateral internal capsules; lenticulostriate arteries',
        'B': 'Bilateral medial medulla; anterior spinal artery',
        'C': 'Bilateral thalamic nuclei; posterior cerebral artery',
        'D': 'Bilateral cerebral peduncles; posterior cerebral artery',
        'E': 'Bilateral ventral pontine base; basilar artery trunk'
    },
    108: {
        'A': 'Right thalamus; sensory loss would be present in thalamic lesions',
        'B': 'Left medial medulla; tongue deviation would occur from CN XII lesion',
        'C': 'Left internal capsule posterior limb; brainstem causes crossed signs',
        'D': 'Left cerebellar hemisphere; limb dysmetria and ataxia would occur',
        'E': 'Left occipital calcarine cortex; homonymous hemianopia would occur'
    },
    109: {
        'A': 'Insidious onset, preserved attention, irreversible progression',
        'B': 'Abrupt onset, fluctuating attention, reversible disturbance',
        'C': 'Insidious onset, fluctuating consciousness, irreversible decline',
        'D': 'Abrupt onset, preserved attention, permanent cognitive deficit',
        'E': 'Gradual onset, normal level of arousal, progressive deterioration'
    },
    110: {
        'A': 'He loses procedural motor skills with preservation of declarative memory',
        'B': 'He selectively loses remote childhood memory with preserved working memory',
        'C': 'He selectively loses short-term working memory with preserved recall',
        'D': 'He learns new procedural skills with inability to form declarative memory',
        'E': 'He loses both procedural and declarative memory modalities equally'
    },
    111: {
        'A': 'Hyperorality with hypersexuality and emotional placidity',
        'B': 'Anterograde amnesia with preserved social comportment',
        'C': 'Fluent paraphasic speech with impaired comprehension',
        'D': 'Violent unilateral choreiform flinging movements',
        'E': 'Visual object agnosia with preserved visual acuity'
    },
    113: {
        'A': 'Hippocampus -> amygdala -> dorsal thalamus -> mammillary body',
        'B': 'Fornix -> hippocampus -> cingulate cortex -> thalamic nuclei',
        'C': 'Hippocampus -> fornix -> mammillary body -> anterior thalamus',
        'D': 'Amygdala -> hypothalamus -> cingulate cortex -> dentate gyrus',
        'E': 'Thalamus -> caudate nucleus -> putamen -> parahippocampal gyrus'
    },
    115: {
        'A': 'Intracellular amyloid tangles and extracellular tau plaques',
        'B': 'Defective amyloid clearance with absent microglial response',
        'C': 'Cerebellar amyloid deposition and neocortical tau clearance',
        'D': 'Extracellular beta-amyloid plaques and intracellular tau tangles',
        'E': 'Alpha-secretase cleavage generating neurotoxic amyloid oligomers'
    },
    119: {
        'A': 'Medial temporal atrophy on MRI, neuritic plaques, and amyloid PET',
        'B': 'Cortical ribboning on MRI, periodic sharp waves, and CSF 14-3-3',
        'C': 'Ventriculomegaly out of proportion to sulci on brain MRI and LP',
        'D': 'Frontotemporal lobar atrophy on MRI, tau bodies, and behavioral loss',
        'E': 'Subcortical lacunes on MRI, stepwise decline, and focal deficits'
    },
    121: {
        'A': 'Stepwise cognitive deterioration associated with focal vascular lesions',
        'B': 'Insidious progressive short-term episodic memory loss over months',
        'C': 'Isolated bilateral anterior hippocampal volume loss without infarcts',
        'D': 'Extracellular accumulation of fibrillar amyloid plaques and tangles',
        'E': 'Marked clinical responsiveness to central cholinesterase inhibitors'
    },
    127: {
        'A': 'Generalized tonic-clonic seizure',
        'B': 'Generalized typical absence seizure',
        'C': 'Generalized juvenile myoclonic seizure',
        'D': 'Generalized sudden atonic seizure',
        'E': 'Cardiogenic vasovagal syncopal attack'
    },
    130: {
        'A': 'Generalized atonic seizure',
        'B': 'Typical absence seizure',
        'C': 'Generalized tonic seizure',
        'D': 'Juvenile myoclonic seizure',
        'E': 'Focal impaired awareness seizure'
    },
    132: {
        'A': 'Continuous seizure activity >=5 minutes or recurrent without recovery',
        'B': 'Any generalized tonic-clonic convulsion with urinary incontinence',
        'C': 'A single self-limited convulsive episode lasting under 60 seconds',
        'D': 'Two separate unprovoked convulsive episodes occurring weeks apart',
        'E': 'Any focal onset seizure preceded by experiential epigastric aura'
    },
    133: {
        'A': 'Aura, holocephalic headache, high fever, and petechial cutaneous rash',
        'B': 'High fever, nuchal rigidity, petechial rash, and persistent headache',
        'C': 'Epigastric pain, projectile vomiting, profuse diarrhea, and high fever',
        'D': 'Palpitations, cutaneous facial pallor, diaphoresis, and presyncope',
        'E': 'Premonitory prodrome, abrupt consciousness loss, ictus, and postictal'
    },
    134: {
        'A': 'Adults: stroke and congenital lesions; children: hypoxia and tumors',
        'B': 'Adults: genetic channelopathies; children: stroke and head trauma',
        'C': 'Adults: central nervous infections; children: embolic stroke events',
        'D': 'Adults: stroke and brain tumors; children: infection and head trauma',
        'E': 'Adults: metabolic derangements; children: metabolic disorders only'
    },
    135: {
        'A': 'Comprehensive urine toxicology screen',
        'B': 'Routine outpatient electroencephalogram',
        'C': 'Comprehensive serum electrolyte panel',
        'D': 'Noncontrast cranial computed tomography',
        'E': 'Autonomic tilt-table diagnostic testing'
    },
    136: {
        'A': 'Immediate initiation of dual antiseizure drug combination therapy',
        'B': 'Urgent surgical evaluation for anterior temporal lobe resection',
        'C': 'Treat identified acute causes without maintenance antiseizure drugs',
        'D': 'Lifelong driving prohibition regardless of electroencephalography',
        'E': 'Continuous inpatient video-EEG monitoring for one complete week'
    },
    137: {
        'A': 'Initiate maintenance antiseizure monotherapy',
        'B': 'Reassurance and observation without treatment',
        'C': 'Perform autonomic tilt-table reflex testing',
        'D': 'Order brain fluorodeoxyglucose-PET scanning',
        'E': 'Repeat noncontrast cranial computed tomography'
    },
    140: {
        'A': 'Valproic acid; GABA transaminase inhibition',
        'B': 'Phenytoin; voltage-gated sodium channel blockade',
        'C': 'Ethosuximide; T-type calcium channel blockade',
        'D': 'Lamotrigine; high-voltage calcium channel block',
        'E': 'Carbamazepine; postsynaptic GABA enhancement'
    },
    143: {
        'A': 'Phenytoin; gingival hyperplasia',
        'B': 'Valproic acid; acute pancreatitis',
        'C': 'Carbamazepine; severe hyponatremia',
        'D': 'Ethosuximide; gastrointestinal distress',
        'E': 'Lamotrigine; Stevens-Johnson syndrome'
    },
    144: {
        'A': 'Voltage-gated sodium channel blockade; acute agranulocytosis',
        'B': 'GABAA receptor chloride current potentiation; profound sedation',
        'C': 'Postsynaptic NMDA receptor blockade; acute florid psychosis',
        'D': 'Thalamic T-type calcium channel block; Stevens-Johnson syndrome',
        'E': 'GABA transaminase enzyme inhibition; fulminant hepatotoxicity'
    },
    145: {
        'A': 'Calcarine visual cortex of the occipital lobe',
        'B': 'Uncus and amygdala of the medial temporal lobe',
        'C': 'Primary motor cortex of the precentral gyrus',
        'D': 'Lateral hemisphere cortex of the cerebellum',
        'E': 'Dorsomedial sensory nucleus of the thalamus'
    },
    146: {
        'A': 'Neuronal channelopathy (voltage-gated potassium channel mutation)',
        'B': 'Systemic metabolic disturbance (acute profound hypoglycemia)',
        'C': 'Focal intracranial structural lesion (oligodendroglioma)',
        'D': 'Benign genetic syndrome (familial febrile convulsions)',
        'E': 'Substance withdrawal syndrome (acute sedative cessation)'
    },
    149: {
        'A': 'Immediate complete recovery of orientation within 5 to 10 seconds',
        'B': 'Isolated brief non-rhythmic myoclonic jerks at sleep transition',
        'C': 'Onset triggered predictably by prolonged upright quiet standing',
        'D': 'Lateral tongue laceration with incontinence and postictal state',
        'E': 'Marked facial pallor with diaphoresis and lightheaded presyncope'
    }
}

for q in questions:
    qnum = int(q['q_num'])
    if qnum in overrides:
        for opt in q['options']:
            if opt['letter'] in overrides[qnum]:
                opt['text'] = overrides[qnum][opt['letter']]

with open(in_path, 'w', encoding='utf-8') as f:
    json.dump(questions, f, indent=2, ensure_ascii=False)

print("Applied apply_shape_and_length_balance.py successfully")
