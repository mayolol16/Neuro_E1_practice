#!/usr/bin/env python3
"""
Meticulously audited option, stem, and explanation overrides for Neuro Exam 2 "Deep" Bank (150 Qs).
Eliminates option length bias, asymmetric parentheses/punctuation, and giveaway phrases.
"""

DEEP_OVERRIDES = {
    # Q6: Balance Meyer loop options with parietal radiation detail
    6: {
        'opts': {
            'A': "Left ventral Meyer loop fibers in the temporal lobe",
            'B': "Right dorsal optic radiations in the parietal lobe",
            'C': "Right ventral Meyer loop fibers in the temporal lobe",
            'D': "Left dorsal optic radiations in the parietal lobe"
        }
    },
    # Q8: Balance cuneus gyrus description
    8: {
        'opts': {
            'A': "Lingual gyrus of occipital lobe",
            'B': "Cuneus gyrus of occipital lobe",
            'C': "Parahippocampal gyrus cortex",
            'D': "Fusiform occipitotemporal gyrus"
        }
    },
    # Q11: Standardize pupillary light reflex response formats with symmetric semicolons
    11: {
        'opts': {
            'A': "Left eye has absent direct and intact consensual; right eye has intact direct and absent consensual",
            'B': "Right eye has absent direct and intact consensual; left eye has intact direct and absent consensual",
            'C': "Left eye has absent direct and consensual responses; right eye has intact direct and consensual responses",
            'D': "Both eyes have absent direct and consensual responses; light transmission pathways are bilaterally lost"
        }
    },
    # Q14: Balance oculomotor herniation etiology with parallel mechanisms
    14: {
        'opts': {
            'A': "Right oculomotor nerve compression from uncal herniation",
            'B': "Right abducens nerve microvascular ischemic compression",
            'C': "Right trochlear nerve stretch injury at tentorial incisura",
            'D': "Right sympathetic trunk cervical ganglion chain lesion"
        }
    },
    # Q15: Balance Pancoast tumor description
    15: {
        'opts': {
            'A': "Right internal carotid artery dissecting aneurysm",
            'B': "Right superior pulmonary sulcus Pancoast tumor",
            'C': "Right middle cerebral artery ischemic territory stroke",
            'D': "Right pontine dorsal tegmental vascular hemorrhage"
        }
    },
    # Q19: Balance posterior commissure anatomical phrasing
    19: {
        'opts': {
            'A': "Medial longitudinal fasciculus tract",
            'B': "Dorsal midbrain posterior commissure",
            'C': "Paramedian pontine reticular formation",
            'D': "Frontal eye field association cortex"
        }
    },
    # Q20: Balance PCom aneurysm anatomical phrasing
    20: {
        'opts': {
            'A': "Right posterior communicating artery",
            'B': "Right middle cerebral artery trunk",
            'C': "Right anterior choroidal artery",
            'D': "Basilar artery terminal bifurcation"
        }
    },
    # Q25: Clarify pupillary reflex finding for CN III efferent palsy
    25: {
        'stem': "A 62-year-old man presents with a right pupil that is dilated and unreactive to light. When light is shined in the left eye, the left pupil constricts normally, but the right pupil does not. When light is shined in the right eye, the left pupil constricts normally, but the right pupil does not constrict. Where is the lesion?",
        'opts': {
            'A': "Right optic nerve",
            'B': "Right oculomotor nerve",
            'C': "Left optic nerve",
            'D': "Left oculomotor nerve"
        },
        'expl': "Right oculomotor nerve (CN III) palsy produces an efferent pupillary defect in the right eye. The afferent limb (CN II) is intact bilaterally. Therefore, shining light in either eye triggers normal bilateral signals to both Edinger-Westphal nuclei, resulting in constriction of the normal left pupil (direct when left eye is illuminated, consensual when right eye is illuminated). However, the damaged right CN III cannot carry efferent parasympathetic signals to the right pupillary sphincter, so the right pupil remains dilated and non-reactive to both direct and consensual stimulation."
    },
    # Q27: Balance Horner carotid dissection descriptions
    27: {
        'opts': {
            'A': "Left Horner syndrome from internal carotid artery dissection",
            'B': "Left oculomotor nerve palsy from posterior aneurysm compression",
            'C': "Left Argyll Robertson pupil from dorsal midbrain syphilis lesion",
            'D': "Left optic nerve neuritis from demyelinating inflammatory disease"
        }
    },
    # Q28: Balance convergence descriptions
    28: {
        'opts': {
            'A': "Both eyes show complete failure to converge",
            'B': "Both eyes show normal, intact convergence",
            'C': "Only the right eye fails to converge normally",
            'D': "Only the left eye fails to converge normally"
        }
    },
    # Q29: Correct answer is A (Left uncal herniation) matching the author's clinical conclusion
    29: {
        'stem': "A 65-year-old man is brought to the emergency department after a fall. He is comatose. On examination, his left pupil is dilated and unreactive to light, and his left eye is deviated down and out. Which of the following is the most likely cause of his coma and eye findings?",
        'ans': 'A',
        'opts': {
            'A': "Left temporal uncal herniation",
            'B': "Right temporal uncal herniation",
            'C': "Left medial thalamic hemorrhage",
            'D': "Bilateral frontal lobe contusion"
        },
        'expl': "In uncal (transtentorial) herniation, the medial temporal lobe uncus herniates across the tentorial notch and directly compresses the ipsilateral (left) oculomotor nerve (CN III). This manifests as an ipsilateral fixed and dilated pupil with ptosis and a 'down-and-out' eye deviation, accompanied by progressive midbrain compression leading to coma."
    },
    # Q33: Balance Argyll Robertson pupil terminology
    33: {
        'opts': {
            'A': "Horner pupillary syndrome",
            'B': "Argyll Robertson pupil",
            'C': "Adie tonic pupil syndrome",
            'D': "Oculomotor nerve palsy"
        }
    },
    # Q36: Balance PPRF gaze center descriptions
    36: {
        'opts': {
            'A': "Left frontal eye field cortical center",
            'B': "Right frontal eye field cortical center",
            'C': "Right paramedian pontine reticular formation",
            'D': "Left paramedian pontine reticular formation"
        }
    },
    # Q38: Balance coloboma option lengths
    38: {
        'opts': {
            'A': "Congenital aniridia",
            'B': "Congenital coloboma",
            'C': "Severe microphthalmos",
            'D': "Infantile glaucoma"
        }
    },
    # Q40: Balance angle-closure glaucoma descriptions
    40: {
        'opts': {
            'A': "Chronic open-angle glaucoma",
            'B': "Acute angle-closure glaucoma",
            'C': "Acute anterior uveitis attack",
            'D': "Severe bacterial keratitis"
        }
    },
    # Q41: Balance dry macular degeneration descriptions
    41: {
        'opts': {
            'A': "Wet neovascular macular degeneration",
            'B': "Dry non-exudative macular degeneration",
            'C': "Non-proliferative diabetic retinopathy",
            'D': "Acute central retinal artery occlusion"
        }
    },
    # Q44: Remove giveaway parenthesis (stye) and balance eyelid pathologies
    44: {
        'opts': {
            'A': "Eyelid chalazion",
            'B': "External hordeolum",
            'C': "Preseptal cellulitis",
            'D': "Postseptal orbital cellulitis"
        }
    },
    # Q47: Balance presbycusis descriptions
    47: {
        'opts': {
            'A': "Age-related presbycusis",
            'B': "Noise-induced hearing loss",
            'C': "Idiopathic Meniere disease",
            'D': "Unilateral vestibular schwannoma"
        }
    },
    # Q48: Remove giveaway distractor parenthesis (BPPV)
    48: {
        'opts': {
            'A': "Benign paroxysmal positional vertigo",
            'B': "Recurrent episodic Meniere disease",
            'C': "Acute post-viral vestibular neuritis",
            'D': "Inner ear suppurative labyrinthitis"
        }
    },
    # Q50: Remove giveaway parenthesis (BPPV) from correct answer
    50: {
        'opts': {
            'A': "Episodic Meniere disease",
            'B': "Benign positional vertigo",
            'C': "Acute vestibular neuritis",
            'D': "Vestibular schwannoma tumor"
        }
    },
    # Q51: Balance vestibular schwannoma option lengths
    51: {
        'opts': {
            'A': "Cerebellopontine meningioma",
            'B': "Acoustic vestibular schwannoma",
            'C': "Posterior fossa epidermoid cyst",
            'D': "Congenital arachnoid cyst"
        }
    },
    # Q57: Balance vestibular neuritis option lengths
    57: {
        'opts': {
            'A': "Meniere disease",
            'B': "Vestibular neuritis",
            'C': "Acute labyrinthitis",
            'D': "Positional vertigo"
        }
    },
    # Q58: Remove giveaway parenthesis (BPPV) from correct answer
    58: {
        'opts': {
            'A': "Recurrent Meniere disease",
            'B': "Benign positional vertigo",
            'C': "Post-viral vestibular neuritis",
            'D': "Inflammatory labyrinthitis"
        }
    },
    # Q60: Balance CPA acoustic schwannoma descriptions
    60: {
        'opts': {
            'A': "Cerebellopontine angle meningioma",
            'B': "Vestibular acoustic schwannoma",
            'C': "Posterior fossa epidermoid cyst",
            'D': "Congenital arachnoid cyst"
        }
    },
    # Q64: Remove giveaway distractor parenthesis (BPPV)
    64: {
        'opts': {
            'A': "Benign paroxysmal positional vertigo",
            'B': "Recurrent episodic Meniere disease",
            'C': "Acute post-viral vestibular neuritis",
            'D': "Inner ear suppurative labyrinthitis"
        }
    },
    # Q67: Balance UMN corticospinal localization options
    67: {
        'opts': {
            'A': "Right corticospinal tract below the pyramidal decussation",
            'B': "Left corticospinal tract above the pyramidal decussation",
            'C': "Right anterior gray horn of the cervical spinal cord",
            'D': "Left anterior gray horn of the cervical spinal cord"
        }
    },
    # Q68: Balance LMN anterior horn localization options
    68: {
        'opts': {
            'A': "Left lateral corticospinal tract in the spinal cord",
            'B': "Right anterior gray horn of the cervical spinal cord",
            'C': "Left primary motor cortex in the precentral gyrus",
            'D': "Right corticobulbar tract within the internal capsule"
        }
    },
    # Q69: Balance UMN central facial droop options
    69: {
        'opts': {
            'A': "Right facial nerve fibers within the caudal pontine tegmentum",
            'B': "Left corticobulbar tract above the pontine facial motor nucleus",
            'C': "Right facial motor nucleus within the caudal pontine tegmentum",
            'D': "Left facial nerve fibers within the caudal pontine tegmentum"
        }
    },
    # Q70: Remove giveaway parenthesis (CN VII) from correct answer
    70: {
        'opts': {
            'A': "Left corticobulbar tract descending through the internal capsule",
            'B': "Right facial nerve fascicles within the caudal pontine tegmentum",
            'C': "Left facial motor nucleus within the caudal pontine tegmentum",
            'D': "Right primary motor cortex within the precentral gyrus area"
        }
    },
    # Q73: Balance UMN corticospinal localization options
    73: {
        'opts': {
            'A': "Right corticospinal tract below the pyramidal decussation",
            'B': "Left corticospinal tract above the pyramidal decussation",
            'C': "Right anterior gray horn of the cervical spinal cord",
            'D': "Left anterior gray horn of the cervical spinal cord"
        }
    },
    # Q76: Balance UMN central facial droop options
    76: {
        'opts': {
            'A': "Right facial nerve fibers within the caudal pontine tegmentum",
            'B': "Left corticobulbar tract above the pontine facial motor nucleus",
            'C': "Right facial motor nucleus within the caudal pontine tegmentum",
            'D': "Left facial nerve fibers within the caudal pontine tegmentum"
        }
    },
    # Q78: Balance LMN anterior horn localization options
    78: {
        'opts': {
            'A': "Left lateral corticospinal tract in the spinal cord",
            'B': "Right anterior gray horn of the cervical spinal cord",
            'C': "Left primary motor cortex in the precentral gyrus",
            'D': "Right corticobulbar tract within the internal capsule"
        }
    },
    # Q79: Balance UMN corticospinal localization options (left-sided weakness)
    79: {
        'opts': {
            'A': "Left corticospinal tract below the pyramidal decussation",
            'B': "Right corticospinal tract above the pyramidal decussation",
            'C': "Left anterior gray horn of the cervical spinal cord",
            'D': "Right anterior gray horn of the cervical spinal cord"
        }
    },
    # Q81: Balance UMN central facial droop options
    81: {
        'opts': {
            'A': "Right facial nerve fibers within the caudal pontine tegmentum",
            'B': "Left corticobulbar tract above the pontine facial motor nucleus",
            'C': "Right facial motor nucleus within the caudal pontine tegmentum",
            'D': "Left facial nerve fibers within the caudal pontine tegmentum"
        }
    },
    # Q83: Balance UMN corticospinal localization options
    83: {
        'opts': {
            'A': "Right corticospinal tract below the pyramidal decussation",
            'B': "Left corticospinal tract above the pyramidal decussation",
            'C': "Right anterior gray horn of the cervical spinal cord",
            'D': "Left anterior gray horn of the cervical spinal cord"
        }
    },
    # Q86: Balance UMN central facial droop options (left facial droop)
    86: {
        'opts': {
            'A': "Left facial nerve fibers within the caudal pontine tegmentum",
            'B': "Right corticobulbar tract above the pontine facial motor nucleus",
            'C': "Left facial motor nucleus within the caudal pontine tegmentum",
            'D': "Right facial nerve fibers within the caudal pontine tegmentum"
        }
    },
    # Q88: Balance UMN corticospinal localization options (left-sided weakness)
    88: {
        'opts': {
            'A': "Left corticospinal tract below the pyramidal decussation",
            'B': "Right corticospinal tract above the pyramidal decussation",
            'C': "Left anterior gray horn of the cervical spinal cord",
            'D': "Right anterior gray horn of the cervical spinal cord"
        }
    },
    # Q89: Balance LMN anterior horn localization options
    89: {
        'opts': {
            'A': "Left lateral corticospinal tract in the spinal cord",
            'B': "Right anterior gray horn of the cervical spinal cord",
            'C': "Left primary motor cortex in the precentral gyrus",
            'D': "Right corticobulbar tract within the internal capsule"
        }
    },
    # Q91: Balance UMN central facial droop options (left facial droop)
    91: {
        'opts': {
            'A': "Left facial nerve fibers within the caudal pontine tegmentum",
            'B': "Right corticobulbar tract above the pontine facial motor nucleus",
            'C': "Left facial motor nucleus within the caudal pontine tegmentum",
            'D': "Right facial nerve fibers within the caudal pontine tegmentum"
        }
    },
    # Q93: Balance UMN corticospinal localization options
    93: {
        'opts': {
            'A': "Right corticospinal tract below the pyramidal decussation",
            'B': "Left corticospinal tract above the pyramidal decussation",
            'C': "Right anterior gray horn of the cervical spinal cord",
            'D': "Left anterior gray horn of the cervical spinal cord"
        }
    },
    # Q96: Balance UMN central facial droop options
    96: {
        'opts': {
            'A': "Right facial nerve fibers within the caudal pontine tegmentum",
            'B': "Left corticobulbar tract above the pontine facial motor nucleus",
            'C': "Right facial motor nucleus within the caudal pontine tegmentum",
            'D': "Left facial nerve fibers within the caudal pontine tegmentum"
        }
    },
    # Q97: Balance hypothalamic nuclei anatomical descriptions
    97: {
        'opts': {
            'A': "Hypothalamic ventromedial satiety nucleus",
            'B': "Supraoptic and paraventricular nuclei",
            'C': "Hypothalamic lateral feeding hunger nucleus",
            'D': "Suprachiasmatic circadian pacemaker nucleus"
        }
    },
    # Q98: Balance cranial nerve trauma options
    98: {
        'opts': {
            'A': "Optic nerve axons at the optic canal",
            'B': "Olfactory nerve axons at the cribriform plate",
            'C': "Maxillary nerve branches at the foramen rotundum",
            'D': "Facial nerve branchial fibers at the stylomastoid"
        }
    },
    # Q106: Balance basal ganglia degenerate structure descriptions
    106: {
        'opts': {
            'A': "Subthalamic nucleus of Luys",
            'B': "Substantia nigra pars compacta",
            'C': "Caudate striatal nucleus head",
            'D': "Internal globus pallidus segment"
        }
    },
    # Q111: Balance Huntington basal ganglia circuit pathways
    111: {
        'opts': {
            'A': "Selective hyperactivation of the direct striatal pathway",
            'B': "Selective hypofunction of the direct striatal pathway",
            'C': "Selective degeneration and loss of the indirect pathway",
            'D': "Selective hyperactivation of the indirect striatal pathway"
        }
    },
    # Q123: Balance trihexyphenidyl adverse effect lengths
    123: {
        'opts': {
            'A': "Drug-induced acute hepatotoxicity",
            'B': "Anticholinergic peripheral dry mouth",
            'C': "Interstitial allergic nephrotoxicity",
            'D': "Sensorineural toxic ototoxicity"
        }
    },
    # Q129: Balance dopamine agonist adverse effect descriptions
    129: {
        'opts': {
            'A': "Severe peak-dose choreiform dyskinesias",
            'B': "Behavioral impulse control disorders",
            'C': "Idiosyncratic acute hepatotoxicity",
            'D': "Membranous drug-induced nephrotoxicity"
        }
    },
    # Q131: Balance benztropine adverse effect descriptions
    131: {
        'opts': {
            'A': "Chorea-like involuntary dyskinesias",
            'B': "Anticholinergic peripheral dry mouth",
            'C': "Hepatic parenchymal enzyme elevation",
            'D': "Interstitial acute allergic nephritis"
        }
    },
    # Q133: Balance sleep disorder diagnostic terms
    133: {
        'opts': {
            'A': "Type 1 narcolepsy disorder",
            'B': "Obstructive sleep apnea syndrome",
            'C': "Chronic psychophysiologic insomnia",
            'D': "Primary restless legs syndrome"
        }
    },
    # Q134: Balance sleep disorder diagnostic terms
    134: {
        'opts': {
            'A': "Type 1 narcolepsy disorder",
            'B': "Obstructive sleep apnea syndrome",
            'C': "Chronic psychophysiologic insomnia",
            'D': "Primary restless legs syndrome"
        }
    },
    # Q135: Balance sleep disorder diagnostic terms
    135: {
        'opts': {
            'A': "Type 1 narcolepsy disorder",
            'B': "Obstructive sleep apnea syndrome",
            'C': "Chronic psychophysiologic insomnia",
            'D': "Primary restless legs syndrome"
        }
    },
    # Q140: Balance modafinil mechanism options
    140: {
        'opts': {
            'A': "Agonism of central GABA-A receptor channels",
            'B': "Dopamine reuptake inhibition promoting wakefulness",
            'C': "Competitive blockade of hypocretin/orexin receptors",
            'D': "Selective agonism of suprachiasmatic melatonin receptors"
        }
    },
    # Q142: Remove giveaway parenthesis (ALS)
    142: {
        'opts': {
            'A': "Primary progressive multiple sclerosis",
            'B': "Amyotrophic lateral sclerosis disorder",
            'C': "Generalized autoimmune myasthenia gravis",
            'D': "Acute inflammatory Guillain-Barré polyneuropathy"
        }
    },
    # Q148: Balance dantrolene mechanism descriptions
    148: {
        'opts': {
            'A': "Acts as a presynaptic GABAB receptor agonist in the spinal cord",
            'B': "Inhibits ryanodine receptor calcium release from the sarcoplasmic reticulum",
            'C': "Acts as an uncompetitive antagonist at glutamate NMDA receptors",
            'D': "Functions as a free radical scavenger reducing motor neuron oxidative injury"
        }
    },
    # Q149: Balance cyclobenzaprine mechanism descriptions
    149: {
        'opts': {
            'A': "Acts as a presynaptic GABAB receptor agonist in the spinal cord",
            'B': "Inhibits central serotonergic and noradrenergic motor pathways in the brainstem",
            'C': "Acts as an uncompetitive antagonist at glutamate NMDA receptors",
            'D': "Functions as a free radical scavenger reducing motor neuron oxidative injury"
        }
    },
    # Q150: Balance botulinum toxin mechanism descriptions
    150: {
        'opts': {
            'A': "Acts as a presynaptic GABAB receptor agonist in the spinal cord",
            'B': "Cleaves SNARE proteins to inhibit acetylcholine release at the neuromuscular junction",
            'C': "Acts as an uncompetitive antagonist at glutamate NMDA receptors",
            'D': "Functions as a free radical scavenger reducing motor neuron oxidative injury"
        }
    }
}
