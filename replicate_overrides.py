#!/usr/bin/env python3
"""
Meticulously audited option and explanation overrides for Neuro Exam 2 "Replicate" Bank (100 Qs).
Eliminates option length bias, asymmetric parentheses/punctuation, and giveaway phrases.
"""

REPLICATE_OVERRIDES = {
    # Q2: Remove asymmetric parenthetical (Meyer loop)
    2: {
        'opts': {
            'A': 'Left optic tract',
            'B': 'Right parietal optic radiations',
            'C': 'Left temporal optic radiations',
            'D': 'Left parietal optic radiations',
            'E': 'Central optic chiasm'
        }
    },
    # Q3: Balance long correct answer with parallel distractor depth
    3: {
        'opts': {
            'A': 'Exclusive projection of macular visual streams to the contralateral lateral geniculate nucleus',
            'B': 'Complete bypass of primary occipital striate cortex by ascending geniculocalcarine fibers',
            'C': 'Selective decussation of central foveal photoreceptor axons at the central optic chiasm',
            'D': 'Dual collateral blood supply and large occipital pole cortical representation of the macula',
            'E': 'Collateral visual representation within tertiary sensory association areas of the parietal lobe'
        }
    },
    # Q5: Balance option lengths
    5: {
        'opts': {
            'A': 'Left optic tract',
            'B': 'Central optic chiasm',
            'C': 'Right lateral geniculate nucleus',
            'D': 'Left visual cortex',
            'E': 'Right optic nerve'
        }
    },
    # Q7: Balance short options A & B with parallel physiological mechanisms
    7: {
        'opts': {
            'A': 'Shortened axial length of the globe focusing near images behind the retina',
            'B': 'Elongated axial length of the globe focusing distant images in front of the retina',
            'C': 'Age-related loss of crystalline lens elasticity and decreased ciliary curvature change',
            'D': 'Asymmetrical irregular curvature of the anterior corneal refracting surface',
            'E': 'Separation of the posterior vitreous humor cortex from the internal limiting membrane'
        }
    },
    # Q8: Remove giveaway explanatory clause in correct answer by balancing all options
    8: {
        'opts': {
            'A': 'Left homonymous hemianopia with intact pupillary light reflexes',
            'B': 'Bitemporal hemianopia with absent pupillary light reflexes',
            'C': 'Right superior quadrantanopia with impaired pupillary accommodation',
            'D': 'Left monocular blindness with an afferent pupillary defect',
            'E': 'Right homonymous hemianopia with intact pupillary light reflexes'
        }
    },
    # Q9: Balance preganglionic sympathetic description
    9: {
        'opts': {
            'A': 'Preganglionic sympathetic fibers ascending over the lung apex to the superior cervical ganglion',
            'B': 'Postganglionic parasympathetic pupillomotor fibers traversing the inferior branch of CN III',
            'C': 'Preganglionic parasympathetic visceral motor neurons originating in the Edinger-Westphal nucleus',
            'D': 'Postganglionic sympathetic sudomotor fibers descending along the external carotid plexus',
            'E': 'Somatosensory primary afferent fibers traversing the ophthalmic division of cranial nerve V'
        }
    },
    # Q10: Balance lateral medullary finding with parallel neurological signs
    10: {
        'opts': {
            'A': 'Spastic hemiparesis involving the contralateral upper and lower extremities',
            'B': 'Loss of vibration sense and proprioception on the contralateral side of the body',
            'C': 'Impaired light touch and pinprick sensation on the contralateral side of the face',
            'D': 'Loss of pain and temperature sensation on the contralateral side of the body',
            'E': 'Sensorineural hearing loss accompanied by tinnitus in the ipsilateral ear'
        }
    },
    # Q11: Balance uncal herniation mechanism
    11: {
        'opts': {
            'A': 'Sympathetic fibers course superficially within the cavernous sinus segment of the carotid plexus',
            'B': 'Parasympathetic fibers run superficially on the outside of CN III and are compressed first',
            'C': 'Somatic motor fibers course peripherally within the midbrain tegmentum and are infarcted early',
            'D': 'Retinofugal afferent fibers course superficially along the lateral aspect of the optic tract',
            'E': 'Trochlear nerve fibers course externally along the free tentorial edge and are stretched early'
        }
    },
    # Q12: Balance diabetic CN III ischemia etiology
    12: {
        'opts': {
            'A': 'Posterior communicating artery saccular aneurysm compression',
            'B': 'Transtentorial uncal herniation mass effect compression',
            'C': 'Microvascular ischemic infarct of the oculomotor nerve',
            'D': 'Superior cervical ganglion sympathetic chain disruption',
            'E': 'Medial longitudinal fasciculus demyelinating plaque'
        }
    },
    # Q13: Standardize pupillary light reflex format (eliminate asymmetric semicolon and length disparity)
    13: {
        'opts': {
            'A': 'Right eye light: left pupil constricts; left eye light: right pupil constricts',
            'B': 'Right eye light: both pupils constrict; left eye light: neither pupil constricts',
            'C': 'Right eye light: neither pupil constricts; left eye light: neither pupil constricts',
            'D': 'Right eye light: right pupil constricts; left eye light: neither pupil constricts',
            'E': 'Right eye light: neither pupil constricts; left eye light: both pupils constrict'
        }
    },
    # Q14: Standardize CN III pupillary response format
    14: {
        'opts': {
            'A': 'Right eye light: left pupil constricts; left eye light: left pupil constricts',
            'B': 'Right eye light: both pupils constrict; left eye light: both pupils constrict',
            'C': 'Right eye light: right pupil constricts; left eye light: right pupil constricts',
            'D': 'Right eye light: neither pupil constricts; left eye light: neither pupil constricts',
            'E': 'Right eye light: both pupils constrict; left eye light: left pupil constricts'
        }
    },
    # Q15: Standardize cortical blindness pupil & accommodation reflexes
    15: {
        'opts': {
            'A': 'Absent pupillary light reflex; intact pupillary accommodation to visual near targets',
            'B': 'Absent pupillary light reflex; absent pupillary accommodation to visual near targets',
            'C': 'Intact pupillary light reflex; intact pupillary accommodation to visual near targets',
            'D': 'Intact pupillary light reflex; absent pupillary accommodation to visual near targets',
            'E': 'Intact pupillary light reflex; paradoxical pupillary dilation to visual near targets'
        }
    },
    # Q16: Remove giveaway parenthetical (Argyll Robertson pupil)
    16: {
        'opts': {
            'A': 'Marcus Gunn pupil',
            'B': 'Argyll Robertson pupil',
            'C': 'Adie tonic pupil',
            'D': 'Horner syndrome pupil',
            'E': 'Hutchinson pupil'
        }
    },
    # Q17: Spell out anatomical names to eliminate short outlier
    17: {
        'opts': {
            'A': 'Left medial longitudinal fasciculus',
            'B': 'Left paramedian pontine reticular formation',
            'C': 'Right abducens motor nucleus',
            'D': 'Right oculomotor motor nucleus',
            'E': 'Right medial longitudinal fasciculus'
        }
    },
    # Q18: Remove giveaway explanatory clause in correct answer
    18: {
        'opts': {
            'A': 'Conjugate deviation of both eyes toward the left',
            'B': 'Skew deviation with hypotropia of the left eye',
            'C': 'Monocular medial resting deviation of the left eye',
            'D': 'Conjugate resting deviation of both eyes downward',
            'E': 'Conjugate deviation of both eyes toward the right'
        }
    },
    # Q19: Remove giveaway parentheticals
    19: {
        'opts': {
            'A': 'Toward the right side of the lesion',
            'B': 'Toward the left side away from the lesion',
            'C': 'Directed upward toward the superior visual field',
            'D': 'Directed downward toward the inferior visual field',
            'E': 'Centered at midline with preserved convergence'
        }
    },
    # Q20: Remove giveaway parenthetical and balance options
    20: {
        'opts': {
            'A': 'Toward the right',
            'B': 'Directly upward',
            'C': 'Fixed in the midline',
            'D': 'Toward the left',
            'E': 'Directly downward'
        }
    },
    # Q21: Balance pineal tumor dorsal midbrain compression description
    21: {
        'opts': {
            'A': 'Neoplastic compression of the abducens motor nucleus in the dorsal caudal pons',
            'B': 'Demyelinating plaque involving the medial longitudinal fasciculus in the pons',
            'C': 'Pineal gland germinoma compressing the dorsal midbrain pretectal area',
            'D': 'Pituitary macroadenoma compressing crossing decussating fibers in the optic chiasm',
            'E': 'Ischemic lacunar stroke involving the paramedian pontine reticular formation'
        }
    },
    # Q23: Balance alpha-1 adrenergic mechanism
    23: {
        'opts': {
            'A': 'Antagonism of alpha-1 adrenergic receptors on the pupillary dilator muscle',
            'B': 'Direct pharmacologic stimulation of parasympathetic postganglionic fibers in CN III',
            'C': 'Selective excitotoxic destruction of cholinergic neurons in the Edinger-Westphal nucleus',
            'D': 'Competitive antagonism of muscarinic M3 receptors on the pupillary sphincter muscle',
            'E': 'Direct alpha-2 adrenergic stimulation suppressing central pretectal sympathetic outflow'
        }
    },
    # Q25: Balance acute angle-closure glaucoma pathophysiology
    25: {
        'opts': {
            'A': 'Excessive active secretion of aqueous humor by the bilayered ciliary body epithelium',
            'B': 'Neovascular proliferation across the anterior chamber angle inducing synechial closure',
            'C': 'Accumulation of extracellular drusen material beneath the retinal pigment epithelium',
            'D': 'Mydriasis-induced apposition of the iris against the trabecular meshwork outflow tract',
            'E': 'Cross-linking and oxidative aggregation of crystallin proteins in the crystalline lens'
        }
    },
    # Q26: Balance retinal detachment pathophysiology
    26: {
        'opts': {
            'A': 'Elevated intraocular pressure inducing ischemic optic nerve head cupping and axonal death',
            'B': 'Separation of the neurosensory retina from the underlying retinal pigment epithelium and choroid',
            'C': 'Progressive oxidative opacification and hydration of crystalline lens structural proteins',
            'D': 'Accumulation of lipid-rich basophilic drusen deposits between Bruch membrane and the pigment layer',
            'E': 'Autoimmune granulomatous inflammatory infiltration involving the uveal tract and ciliary body'
        }
    },
    # Q28: Balance retinitis pigmentosa pathophysiology
    28: {
        'opts': {
            'A': 'Progressive apoptotic degeneration of rod and cone photoreceptor cells',
            'B': 'Extracellular accumulation of drusen deposits beneath the retinal epithelium',
            'C': 'Impaired trabecular meshwork drainage causing elevated ocular pressure',
            'D': 'Mechanical separation of the neurosensory layer from the choroidal vascular bed',
            'E': 'Progressive stromal edema causing loss of optical corneal transparency'
        }
    },
    # Q29: Balance congenital cataract amblyopia explanation
    29: {
        'opts': {
            'A': 'Progressive intumescence of the infant lens will rapidly precipitate pupillary block glaucoma',
            'B': 'Capsular micro-perforation will release lens crystallins and trigger phacolytic endophthalmitis',
            'C': 'Congenital pediatric cataracts carry an immediate high risk of malignant retinoblastoma transformation',
            'D': 'Total visual deprivation will induce rapid ischemic coagulation necrosis of the distal optic nerve',
            'E': 'Deprivation of visual input during early critical development causes permanent cortical amblyopia'
        }
    },
    # Q30: Balance glaucoma pharmacology options
    30: {
        'opts': {
            'A': 'Decreases active aqueous humor secretion by the nonpigmented ciliary epithelium',
            'B': 'Increases uveoscleral outflow of aqueous humor through the ciliary muscle',
            'C': 'Induces pupillary constriction and opens the trabecular meshwork via muscarinic drive',
            'D': 'Inhibits carbonic anhydrase enzymes responsible for bicarbonate and aqueous production',
            'E': 'Antagonizes presynaptic alpha-2 adrenergic receptors to reduce sympathetic outflow'
        }
    },
    # Q33: Self-contained clinical stem & balanced Meniere disease pathophysiology
    33: {
        'stem': 'A 45-year-old factory worker presents with recurrent, episodic vertigo lasting about an hour per episode, accompanied by low-frequency buzzing tinnitus in his left ear and a persistent sensation of aural fullness. Tuning fork examination shows bone conduction greater than air conduction in neither ear, and the Weber test lateralizes to the right ear, consistent with left-sided sensorineural hearing loss. Which of the following best explains the underlying pathophysiologic mechanism of this patient\'s condition?',
        'opts': {
            'A': 'Excessive accumulation and elevated hydrostatic pressure of endolymph within the membranous labyrinth',
            'B': 'Dislodgement and free-floating migration of otoconia into the posterior semicircular canal ampulla',
            'C': 'Benign Schwann cell neoplasm originating along the vestibular division of cranial nerve VIII',
            'D': 'Post-viral inflammatory demyelination selectively involving the superior vestibular nerve branch',
            'E': 'Destructive expansion of keratinized stratified squamous epithelium within the middle ear cavity'
        }
    },
    # Q34: Balance Epley maneuver therapeutic mechanism
    34: {
        'opts': {
            'A': 'Facilitating drainage of excess endolymphatic fluid through the endolymphatic duct',
            'B': 'Increasing reflexive contraction of the stapedius and tensor tympani middle ear muscles',
            'C': 'Relieving microvascular pulsatile compression along the root entry zone of cranial nerve VIII',
            'D': 'Augmenting central vestibular compensation circuits within the medullary vestibular nuclei',
            'E': 'Repositioning dislodged canalith otoconia out of the semicircular canal into the utricular vestibule'
        }
    },
    # Q36: Balance vertigo diagnoses lengths
    36: {
        'opts': {
            'A': 'Benign paroxysmal positional vertigo',
            'B': 'Endolymphatic hydrops (Meniere disease)',
            'C': 'Acute isolated vestibular neuritis',
            'D': 'Acute infectious labyrinthitis',
            'E': 'Vestibular schwannoma (acoustic neuroma)'
        }
    },
    # Q37: Balance central vs peripheral vertigo findings
    37: {
        'opts': {
            'A': 'Intense fatigable vertigo with prominent hearing loss and tinnitus',
            'B': 'Direction-fixed horizontal nystagmus that suppresses with visual fixation',
            'C': 'Direction-changing nystagmus unsuppressed by fixation with limb ataxia and dysarthria',
            'D': 'Brief episodic vertigo triggered by head position changes fading within 60 seconds',
            'E': 'Isolated sudden-onset vertigo following an uncomplicated viral upper respiratory infection'
        }
    },
    # Q38: Remove giveaway parenthetical (high frequencies)
    38: {
        'opts': {
            'A': 'Basal turn of the cochlea',
            'B': 'Apical turn of the cochlea',
            'C': 'Middle turn of the cochlea',
            'D': 'Membranous labyrinth vestibule',
            'E': 'External osseous spiral lamina'
        }
    },
    # Q43: Balance saccule and utricle options
    43: {
        'opts': {
            'A': 'Macula of the saccule',
            'B': 'Macula of the utricle',
            'C': 'Crista of the semicircular canal',
            'D': 'Organ of Corti in the cochlea',
            'E': 'Dorsal cochlear nucleus in the pons'
        }
    },
    # Q45: Balance UMN spasticity mechanism
    45: {
        'opts': {
            'A': 'Direct excitotoxic apoptosis of spinal anterior horn alpha motor neurons',
            'B': 'Selective denervation atrophy of intrafusal muscle spindle dynamic fibers',
            'C': 'Impairment of retrograde neurotrophic transport in peripheral motor nerves',
            'D': 'Autoimmune receptor blockade at the postsynaptic neuromuscular junction',
            'E': 'Loss of descending inhibitory upper motor neuron input to spinal reflex arcs'
        }
    },
    # Q47: Balance ankle clonus mechanism
    47: {
        'opts': {
            'A': 'Intrinsic myofibrillar fatigue within fast-twitch gastrocnemius motor units',
            'B': 'Denervation supersensitivity of postsynaptic nicotinic acetylcholine receptors',
            'C': 'Intention tremor resulting from cerebellar dentatorubrothalamic tract dysfunction',
            'D': 'Hyperactive stretch reflex circuitry resulting from loss of descending inhibition',
            'E': 'Entrapment compression neuropathy affecting the distal tibial nerve in the tarsal tunnel'
        }
    },
    # Q48: Balance spinal cord transection reflexes
    48: {
        'opts': {
            'A': 'Hyperactive patellar reflex and an intact spinal flexor withdrawal reflex',
            'B': 'Absent patellar reflex and absent spinal flexor withdrawal reflex',
            'C': 'Absent patellar reflex and hyperactive spinal flexor withdrawal reflex',
            'D': 'Normal patellar reflex and absent spinal flexor withdrawal reflex',
            'E': 'Hypoactive patellar reflex and flaccid tone with absent withdrawal reflex'
        }
    },
    # Q49: Balance central facial weakness lesion location
    49: {
        'opts': {
            'A': 'Right peripheral facial nerve distal to the stylomastoid foramen',
            'B': 'Left corticobulbar tract rostral to the pontine facial motor nucleus',
            'C': 'Right facial motor nucleus within the caudal pontine tegmentum',
            'D': 'Right corticobulbar tract rostral to the pontine facial motor nucleus',
            'E': 'Right cerebellopontine angle mass compressing cranial nerve VII'
        }
    },
    # Q50: Balance Bell palsy vs stroke options
    50: {
        'opts': {
            'A': 'Drooping of the lower face on the affected side',
            'B': 'Deviation of the tongue on protrusion to the affected side',
            'C': 'Preserved voluntary smiling on the affected side',
            'D': 'Spastic hemiparesis involving the ipsilateral upper extremity',
            'E': 'Inability to wrinkle the forehead on the affected side'
        }
    },
    # Q51: Balance hypoglossal lesion location
    51: {
        'opts': {
            'A': 'Left hypoglossal motor nucleus in the medullary tegmentum',
            'B': 'Right corticobulbar tract within the posterior internal capsule',
            'C': 'Right hypoglossal nerve in the bony hypoglossal canal',
            'D': 'Right vagus nerve traversing the posterior jugular foramen',
            'E': 'Right glossopharyngeal nerve traversing the jugular foramen'
        }
    },
    # Q52: Remove parenthetical giveaway and balance medial medullary lesion
    52: {
        'opts': {
            'A': 'Right internal capsule posterior limb',
            'B': 'Left precentral motor cortex hand area',
            'C': 'Right medial medulla oblongata',
            'D': 'Left medial medulla oblongata',
            'E': 'Right midbrain cerebral peduncle'
        }
    },
    # Q54: Balance nucleus ambiguus deficit findings
    54: {
        'opts': {
            'A': 'Uvula deviation to the left with loss of the right-sided pharyngeal gag reflex',
            'B': 'Uvula deviation to the right with loss of the left-sided pharyngeal gag reflex',
            'C': 'Tongue deviation to the left with contralateral spastic hemiparesis of the body',
            'D': 'Tongue deviation to the right with contralateral spastic hemiparesis of the body',
            'E': 'Mandibular deviation to the left with loss of the ipsilateral corneal sensation'
        }
    },
    # Q55: Balance accessory nerve deficit findings
    55: {
        'opts': {
            'A': 'Weak left shoulder shrug and weak head turn to the right',
            'B': 'Weak left shoulder shrug and weak head turn to the left',
            'C': 'Weak right shoulder shrug and weak head turn to the right',
            'D': 'Bilateral shoulder shrug weakness with intact bilateral head turn',
            'E': 'Weak right shoulder shrug and weak head turn to the left'
        }
    },
    # Q56: Balance anterior spinal artery syndrome findings
    56: {
        'opts': {
            'A': 'Bilateral flaccid paralysis with loss of vibration sense and preserved pain sensation',
            'B': 'Right spastic paralysis with loss of proprioception and preserved pain sensation',
            'C': 'Bilateral spastic paraparesis with loss of pain and temperature sensation',
            'D': 'Complete bilateral sensory and motor loss below the level of the spinal cord lesion',
            'E': 'Preserved voluntary motor power with isolated bilateral loss of proprioception'
        }
    },
    # Q57: Balance Brown-Sequard syndrome findings
    57: {
        'opts': {
            'A': 'Left spasticity and vibration loss, with preserved pain and temperature sensation',
            'B': 'Bilateral spastic paraparesis, with bilateral loss of pain and temperature sensation',
            'C': 'Bilateral loss of vibration and proprioception, with intact voluntary motor power',
            'D': 'Right spasticity and vibration loss, with left loss of pain and temperature sensation',
            'E': 'Right flaccid paralysis and pain loss, with preserved left sensation and motor power'
        }
    },
    # Q58: Balance syringomyelia initial pathology description
    58: {
        'opts': {
            'A': 'Anterior white commissure decussating fibers of the spinothalamic tracts',
            'B': 'Cervical fasciculus cuneatus sensory axons within the posterior columns',
            'C': 'Lateral corticospinal descending motor tracts within the lateral funiculus',
            'D': 'Lumbosacral primary motor and sensory nerve roots of the cauda equina',
            'E': 'Dorsal root entry zone fibers traversing the tract of Lissauer'
        }
    },
    # Q59: Balance subacute combined degeneration tracts
    59: {
        'opts': {
            'A': 'Anterolateral spinothalamic tracts and anterior horn alpha motor neurons',
            'B': 'Posterior dorsal columns and lateral corticospinal descending motor tracts',
            'C': 'Anterior and posterior spinocerebellar ascending sensory tracts',
            'D': 'Anterior corticospinal motor tracts and medial longitudinal fasciculi',
            'E': 'Dorsolateral tracts of Lissauer and dorsal horn substantia gelatinosa'
        }
    },
    # Q60: Balance cauda equina option length
    60: {
        'opts': {
            'A': 'Thoracolumbar anterior spinal artery territory',
            'B': 'Hemisection of the thoracic spinal cord',
            'C': 'Central canal syrinx within the cervical cord',
            'D': 'Sacral cord segments of the conus medullaris',
            'E': 'Lumbosacral nerve roots of the cauda equina'
        }
    },
    # Q61: Balance parasagittal meningioma description
    61: {
        'opts': {
            'A': 'Intramedullary mass compressing the cervical spinal cord dorsal columns',
            'B': 'Subcortical glioma involving the posterior limb of the internal capsule',
            'C': 'Parasagittal falcine meningioma compressing bilateral paracentral lobules',
            'D': 'Degenerative mass compressing anterior horn cells of the lumbar enlargement',
            'E': 'Ischemic lesion involving the medullary pyramids at the decussation'
        }
    },
    # Q62: Balance internal capsule stroke findings
    62: {
        'opts': {
            'A': 'Left hemiparesis with left lower facial weakness and hyperreflexia',
            'B': 'Fluent aphasia with dense right superior homonymous quadrantanopia',
            'C': 'Paraparesis with bilateral extensor plantar responses and sensory loss',
            'D': 'Right hemiparesis with spasticity and right lower facial weakness',
            'E': 'Contralateral hemi-sensory loss with complete preservation of motor power'
        }
    },
    # Q63: Remove asymmetric parenthetical (Ia afferent)
    63: {
        'opts': {
            'A': 'Muscle spindle',
            'B': 'Golgi tendon organ',
            'C': 'Pacinian corpuscle',
            'D': 'Free nerve ending',
            'E': 'Meissner corpuscle'
        }
    },
    # Q64: Remove giveaway explanatory clause from spasticity
    64: {
        'opts': {
            'A': 'Rigidity',
            'B': 'Spasticity',
            'C': 'Flaccidity',
            'D': 'Fasciculations',
            'E': 'Chorea'
        }
    },
    # Q68: Balance olfactory uncus location lengths
    68: {
        'opts': {
            'A': 'Uncus of the temporal lobe',
            'B': 'Occipital pole striate cortex',
            'C': 'Postcentral gyrus sensory cortex',
            'D': 'Vermis of the cerebellum',
            'E': 'Frontal eye field motor cortex'
        }
    },
    # Q69: Balance solitary nucleus description
    69: {
        'opts': {
            'A': 'Ventral posteromedial nucleus of the thalamus',
            'B': 'Gustatory portion of the solitary nucleus',
            'C': 'Primary gustatory cortex within the insula',
            'D': 'Primary olfactory cortex within the uncus',
            'E': 'Branchial motor neurons of the nucleus ambiguus'
        }
    },
    # Q71: Balance dopaminergic cell loss descriptions
    71: {
        'opts': {
            'A': 'GABAergic neurons of the striatum and globus pallidus',
            'B': 'Cholinergic neurons of the basal nucleus of Meynert',
            'C': 'Dopaminergic neurons of the substantia nigra pars compacta',
            'D': 'Glutamatergic neurons of the subthalamic nucleus of Luys',
            'E': 'Inhibitory Purkinje cells of the cerebellar cortex'
        }
    },
    # Q72: Self-contained clinical stem & balanced Lewy body histopathology descriptions
    72: {
        'stem': "A 73-year-old man with a long-standing history of a resting pill-rolling hand tremor, cogwheel rigidity, bradykinesia, and a characteristic slow, shuffling gait dies of an acute myocardial infarction. Postmortem neuropathologic examination of this patient's brain would most likely reveal which of the following microscopic and macroscopic findings?",
        'opts': {
            'A': 'Severe caudate head atrophy with secondary enlargement of the lateral ventricles',
            'B': 'Intracytoplasmic neurofibrillary tangles and extracellular amyloid-beta plaques',
            'C': 'Spongiform neuronal vacuolation with extensive reactive astrocytic proliferation',
            'D': 'Eosinophilic alpha-synuclein Lewy bodies with loss of pigmented nigral neurons',
            'E': 'Ubiquitinated Bunina bodies and round inclusions within anterior horn cells'
        }
    },
    # Q73: Self-contained clinical stem & balanced laterality options (Question 15 in shuffled bank)
    73: {
        'stem': "A 73-year-old man presents with a low-frequency resting pill-rolling tremor that is predominantly localized to his left hand and arm. Neurologic examination also reveals left-sided cogwheel rigidity and bradykinesia, consistent with early Parkinson disease. Which brain structure is primarily responsible for the pathophysiology of this patient's left-hand motor symptoms?",
        'opts': {
            'A': 'Right substantia nigra pars compacta',
            'B': 'Left substantia nigra pars compacta',
            'C': 'Left cerebellar dentate nucleus',
            'D': 'Right cerebellar hemisphere cortex',
            'E': 'Bilateral subthalamic nuclei equally'
        }
    },
    # Q74: Balance direct and indirect dopamine modulation
    74: {
        'opts': {
            'A': 'Inhibits the direct pathway via D1 receptors and excites the indirect pathway via D2 receptors',
            'B': 'Excites the direct pathway via D1 receptors and inhibits the indirect pathway via D2 receptors',
            'C': 'Excites both the direct and indirect pathways through nonselective dopamine D1/D2 activation',
            'D': 'Inhibits both the direct and indirect pathways through tonic hyperpolarizing dopamine release',
            'E': 'Directly excites the subthalamic nucleus to increase pallidal inhibition of the motor thalamus'
        }
    },
    # Q75: Balance basal ganglia circuit pathophysiology
    75: {
        'opts': {
            'A': 'Excessive excitatory thalamocortical drive by the ventral lateral thalamus',
            'B': 'Widespread apoptotic loss of striatal GABAergic medium spiny neurons',
            'C': 'Pathologic hyperactivation of the direct basal ganglia motor pathway',
            'D': 'Complete functional failure of the glutamatergic subthalamic nucleus',
            'E': 'Increased inhibitory GABAergic output of the internal globus pallidus to the thalamus'
        }
    },
    # Q76: Balance carbidopa mechanism of action
    76: {
        'opts': {
            'A': 'It penetrates the central nervous system to augment striatal dopamine synthesis',
            'B': 'It selectively blocks postsynaptic D2 dopamine receptors in the limbic system',
            'C': 'It inhibits peripheral dopa decarboxylase without crossing the blood-brain barrier',
            'D': 'It selectively and irreversibly inhibits central monoamine oxidase type B',
            'E': 'It stimulates calcium-dependent vesicular dopamine release from terminal axons'
        }
    },
    # Q81: Balance anticholinergic side effect descriptions
    81: {
        'opts': {
            'A': 'Acute fulminant hepatic necrosis',
            'B': 'Severe symptomatic orthostatic hypotension',
            'C': 'Cognitive confusion and urinary retention',
            'D': 'Hyperpyrexic serotonin syndrome crisis',
            'E': 'Erythematous livedo reticularis rash'
        }
    },
    # Q83: Balance Huntington genetic descriptions
    83: {
        'opts': {
            'A': 'CAG trinucleotide repeat expansion in the HTT gene on chromosome 4',
            'B': 'ATP7B loss-of-function copper transport mutation on chromosome 13',
            'C': 'SOD1 superoxide dismutase missense mutation on chromosome 21',
            'D': 'Microdeletion of the paternal 15q11-q13 region on chromosome 15',
            'E': 'CTG trinucleotide repeat expansion in the DMPK gene on chromosome 19'
        }
    },
    # Q84: Self-contained clinical stem & balanced Huntington chorea neuropathology descriptions
    84: {
        'stem': "A 38-year-old man presents with progressive emotional lability, restlessness, cognitive decline, and sudden, involuntary, dance-like choreiform movements of his extremities. His father died in his mid-40s of a similar progressive neurodegenerative condition. Which of the following neuropathologic processes directly underlies the chorea observed in this patient?",
        'opts': {
            'A': 'Progressive loss of dopaminergic projection neurons within the substantia nigra',
            'B': 'Degeneration of striatal GABAergic neurons in the indirect pathway disinhibiting the thalamus',
            'C': 'Apoptosis of cerebellar Purkinje neurons leading to profound intention tremor',
            'D': 'Focal ischemic cavitation within the contralateral subthalamic nucleus of Luys',
            'E': 'Toxic hepatocellular and striatal copper accumulation with impaired ceruloplasmin'
        }
    },
    # Q85: Remove giveaway explanatory clause from tetrabenazine
    85: {
        'opts': {
            'A': 'Levodopa',
            'B': 'Amantadine',
            'C': 'Entacapone',
            'D': 'Benztropine',
            'E': 'Tetrabenazine'
        }
    },
    # Q86: Balance subthalamic nucleus anatomical names
    86: {
        'opts': {
            'A': 'Left caudate nucleus',
            'B': 'Left substantia nigra',
            'C': 'Right subthalamic nucleus',
            'D': 'Right putamen nucleus',
            'E': 'Left subthalamic nucleus'
        }
    },
    # Q87: Balance Wilson disease genetic descriptions
    87: {
        'opts': {
            'A': 'Trinucleotide repeat expansion in the HTT gene on chromosome 4',
            'B': 'Superoxide dismutase 1 missense mutation on chromosome 21',
            'C': 'Abnormal alpha-synuclein misfolding and Lewy body aggregation',
            'D': 'ATP7B copper-transporting ATPase gene mutation on chromosome 13',
            'E': 'Hereditary HFE gene missense mutation causing excessive iron absorption'
        }
    },
    # Q88: Remove parenthetical giveaway (Lewy bodies)
    88: {
        'opts': {
            'A': 'Neuronal alpha-synuclein aggregation',
            'B': 'Trinucleotide CAG repeat expansion',
            'C': 'Hyperphosphorylated TDP-43 inclusion bodies',
            'D': 'Hepatolenticular copper accumulation',
            'E': 'Extracellular amyloid-beta deposition'
        }
    },
    # Q89: Remove parenthetical giveaway (hypocretin)
    89: {
        'opts': {
            'A': 'Histaminergic neurons of the tuberomammillary nucleus',
            'B': 'Orexin-producing neurons of the lateral hypothalamus',
            'C': 'GABAergic neurons of the ventrolateral preoptic nucleus',
            'D': 'Melatonin-sensitive neurons of the suprachiasmatic nucleus',
            'E': 'Serotonergic neurons of the median and dorsal raphe nuclei'
        }
    },
    # Q90: Self-contained clinical stem & balanced narcolepsy diagnostic testing descriptions
    90: {
        'stem': "An 18-year-old college student presents with excessive daytime somnolence, falling asleep repeatedly during lectures and social conversations. She reports vivid, frightening visual hallucinations upon falling asleep, transient inability to move upon awakening in the morning, and sudden episodes of bilateral knee buckling and facial drooping provoked by laughter or surprise while remaining fully conscious. Which of the following diagnostic studies is best to definitively confirm the suspected diagnosis?",
        'opts': {
            'A': 'Overnight diagnostic polysomnogram demonstrating prolonged REM sleep latency',
            'B': 'Contrast-enhanced brain MRI evaluating for hypothalamic structural lesions',
            'C': 'Lumbar puncture CSF analysis measuring elevated hypocretin-1 neuropeptides',
            'D': 'Serum melatonin circadian profile assay measuring evening dim-light secretion',
            'E': 'Multiple sleep latency test demonstrating mean sleep latency under 8 minutes'
        }
    },
    # Q91: Self-contained clinical stem & balanced cataplexy pharmacotherapy
    91: {
        'stem': "A 24-year-old woman with a history of narcolepsy experiences frequent, disabling episodes of sudden bilateral muscle weakness and collapse provoked by laughter (cataplexy), as well as distressing sleep paralysis and hypnagogic hallucinations. In addition to daytime scheduled naps and modafinil for somnolence, which of the following medications is most effective for suppressing REM sleep and controlling her cataplexy?",
        'opts': {
            'A': 'Modafinil',
            'B': 'Zolpidem',
            'C': 'Venlafaxine',
            'D': 'Haloperidol',
            'E': 'Pramipexole'
        }
    },
    # Q94: Remove parenthetical giveaway (slow-wave sleep)
    94: {
        'opts': {
            'A': 'REM sleep',
            'B': 'NREM stage N3',
            'C': 'NREM stage N2',
            'D': 'NREM stage N1',
            'E': 'Sleep onset latency'
        }
    },
    # Q97: Balance riluzole mechanism of action
    97: {
        'opts': {
            'A': 'Free radical scavenger that decreases oxidative cellular damage',
            'B': 'Presynaptic GABA-B agonist that increases spinal motor inhibition',
            'C': 'Central alpha-2 adrenergic agonist that reduces spastic muscle tone',
            'D': 'Presynaptic glutamate release inhibitor and NMDA receptor antagonist',
            'E': 'Direct dopamine D2 receptor agonist that stimulates striatal pathways'
        }
    },
    # Q98: Balance preserved ALS functions
    98: {
        'opts': {
            'A': 'Extraocular motility and urinary bladder control',
            'B': 'Tongue protrusion and pharyngeal swallowing coordination',
            'C': 'Upper extremity distal intrinsic hand motor strength',
            'D': 'Diaphragmatic contraction and intercostal ventilation',
            'E': 'Proximal shoulder abduction and neck flexion power'
        }
    }
}
