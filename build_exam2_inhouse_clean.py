# -*- coding: utf-8 -*-
"""
Builder and Cleaner for Neuro Exam 2 In-House Question Bank (181 Questions).
Reads Neuro_Exam2_Step1_QBank.md, cleans all option biases (lengths, parentheses,
unique characters, giveaway clauses), verifies zero audit flags, and outputs
both JSON and review Markdown.
"""
import re
import json
import os

SOURCE_MD = "/Users/markyoussef_1/Downloads/Neuro_Exam2_Step1_QBank.md"

with open(SOURCE_MD, "r", encoding="utf-8") as f:
    text = f.read()

unit_splits = re.split(r'## (Unit \d+: [^\n]+)', text)

# Map raw unit to standardized category & clean unit number
unit_meta = {
    'Unit 1: Visual System (36 questions)': {'num': 1, 'category': 'Visual System'},
    'Unit 2: Visual Reflexes (36 questions)': {'num': 2, 'category': 'Visual Reflexes'},
    'Unit 3: Eye Disorders (36 questions)': {'num': 3, 'category': 'Eye Disorders'},
    'Unit 4: Auditory & Vestibular Systems (36 questions)': {'num': 4, 'category': 'Auditory & Vestibular Systems'},
    'Unit 5: UMN / LMN (37 questions)': {'num': 5, 'category': 'UMN / LMN'}
}

# We'll organize them in clean unit order: Unit 1, Unit 2, Unit 3, Unit 4, Unit 5
parsed_by_unit = {1: [], 2: [], 3: [], 4: [], 5: []}

for i in range(1, len(unit_splits), 2):
    raw_title = unit_splits[i]
    content = unit_splits[i+1]
    meta = unit_meta[raw_title]
    u_num = meta['num']
    cat = meta['category']
    
    q_part, a_part = re.split(r'### Answer Key & Explanations', content)
    
    # Parse answers
    ans_dict = {}
    ans_blocks = re.split(r'\n\*\*(\d+)\.\s*([A-E])\.\*\*\s*', a_part)
    for j in range(1, len(ans_blocks), 3):
        q_n = int(ans_blocks[j])
        corr_letter = ans_blocks[j+1]
        exp_text = ans_blocks[j+2].strip()
        ans_dict[q_n] = (corr_letter, exp_text)
        
    # Parse questions
    q_blocks = re.split(r'\n\*\*(\d+)\.\*\*\s*', q_part)
    for j in range(1, len(q_blocks), 2):
        q_n = int(q_blocks[j])
        q_body = q_blocks[j+1].strip()
        lines = q_body.split('\n')
        stem_lines = []
        options = []
        for line in lines:
            line_s = line.strip()
            opt_match = re.match(r'^[-*]\s*([A-E])\.\s*(.*)', line_s)
            if opt_match:
                options.append({'id': opt_match.group(1), 'text': opt_match.group(2).strip()})
            elif not options:
                stem_lines.append(line)
        stem = '\n'.join(stem_lines).strip()
        corr_letter, exp = ans_dict.get(q_n, ('', ''))
        
        parsed_by_unit[u_num].append({
            'unit_num': u_num,
            'unit_q_num': q_n,
            'category': cat,
            'source': f'In-House Unit 0{u_num} Step 1 QBank (Q{q_n})',
            'stem': stem,
            'options': options,
            'correct_answer': corr_letter,
            'explanation': exp
        })

print("Parsing complete:")
for u in range(1, 6):
    print(f"  Unit {u}: {len(parsed_by_unit[u])} questions")

# Replacement dictionary for biased questions: keyed by (unit_num, unit_q_num)
# Each entry provides replacement texts for [A, B, C, D, E]
REPLACEMENTS = {}

# --- UNIT 4 ---
REPLACEMENTS[(4, 1)] = [
    "Excess endolymph accumulating within the cochlear and vestibular spaces",
    "Calcium carbonate crystals displaced from the otolithic membrane into a canal",
    "Schwann cell tumor expanding along the acoustic and vestibular branches",
    "Post-viral inflammation of the membranous labyrinth and vestibular nerve",
    "Ischemic infarction of the vestibular nuclei in the dorsolateral brainstem"
]

REPLACEMENTS[(4, 4)] = [
    "Direct infiltrative invasion of the primary dorsal cochlear nucleus",
    "Compression of CN V and CN VII at the cerebellopontine angle by tumor",
    "Compression of CN IX and CN X at the posterior jugular foramen region",
    "Involvement of ophthalmic and maxillary branches within cavernous sinus",
    "Ischemic infarction of the lateral medullary tegmentum and tractus"
]

REPLACEMENTS[(4, 12)] = [
    "The base of the membrane is narrow and stiff, whereas the apex is wide and flexible",
    "The base contains outer hair cells only, whereas the apex contains inner hair cells",
    "The base is located near the helicotrema, whereas the apex borders the oval window",
    "The base receives facial nerve fibers, whereas the apex receives cochlear branches",
    "The base lacks a tectorial covering, whereas the apex has an anchored membrane"
]

REPLACEMENTS[(4, 13)] = [
    "Depolarization and increased neurotransmitter release from the hair cell",
    "Hyperpolarization and decreased firing of the afferent neuron at rest",
    "Calcium influx producing no net alteration in cellular membrane potential",
    "Immediate all-or-none action potential propagation along the stereocilia",
    "Inhibitory GABA release onto postsynaptic spiral ganglion dendrites"
]

REPLACEMENTS[(4, 19)] = [
    "Complete sensorineural deafness affecting the left ear",
    "Complete sensorineural deafness affecting the right ear",
    "Total bilateral deafness across all audible frequencies",
    "Impaired sound localization with preserved bilateral hearing",
    "Severe conductive hearing loss with bone-conduction sparing"
]

REPLACEMENTS[(4, 20)] = [
    "Pseudomonas aeruginosa and Aspergillus fumigatus",
    "Streptococcus pneumoniae and Haemophilus influenzae",
    "Staphylococcus epidermidis and Candida albicans",
    "Neisseria meningitidis and Listeria monocytogenes",
    "Bordetella pertussis and Mycoplasma pneumoniae"
]

REPLACEMENTS[(4, 22)] = [
    "Keratinizing squamous epithelial cyst that erodes middle ear ossicles",
    "Benign Schwann cell neoplasm expanding along the internal acoustic canal",
    "Sclerotic bony overgrowth producing progressive fixation of the stapes",
    "Endolymphatic hydrops distending the membranous labyrinth compartments",
    "Suppurative bacterial furuncle involving the external cartilaginous canal"
]

REPLACEMENTS[(4, 23)] = [
    "Ossicular chain in the middle ear cavity",
    "Tympanic membrane in the auditory canal",
    "Cochlear hair cells in the organ of Corti",
    "Cranial nerve VIII at the pontine angle",
    "Stapedius muscle within the tympanic wall"
]

REPLACEMENTS[(4, 24)] = [
    "Lateralization to the left ear; Rinne positive bilaterally",
    "Lateralization to the right ear; Rinne negative on the right",
    "Midline Weber sensation; Rinne positive in both ears",
    "Lateralization to the right ear; Rinne positive bilaterally",
    "Lateralization to the left ear; Rinne negative on the left"
]

REPLACEMENTS[(4, 25)] = [
    "Macula of the utricle in the vestibule",
    "Macula of the saccule in the vestibule",
    "Crista ampullaris of semicircular canals",
    "Organ of Corti in the cochlear duct",
    "Tectorial membrane of the cochlea"
]

REPLACEMENTS[(4, 27)] = [
    "Embedded calcium carbonate crystals that increase membrane density",
    "Extremely high potassium ion concentration within the surrounding fluid",
    "Rigid fibrous attachments directly anchoring to the basilar membrane",
    "Concentric myelin sheaths surrounding the protruding kinocilia shafts",
    "High density of mechanically gated sodium channels across the apex"
]

REPLACEMENTS[(4, 30)] = [
    "Normal physiological function of the vestibulo-ocular arc",
    "Dysfunction of the brainstem vestibulo-ocular reflex pathway",
    "Bilateral hemispheric frontal lobe metabolic encephalopathy",
    "Isolated unilateral peripheral vestibular ganglion neuritis",
    "Bilateral lens opacification from advanced mature cataracts"
]

REPLACEMENTS[(4, 31)] = [
    "Horizontal nystagmus with fast phase beating toward the left ear",
    "Horizontal nystagmus with fast phase beating toward the right ear",
    "Vertical downbeat nystagmus that persists despite visual fixation",
    "Complete absence of spontaneous or gaze-evoked ocular nystagmus",
    "Torsional nystagmus provoked exclusively by rapid head positioning"
]

REPLACEMENTS[(4, 33)] = [
    "Anterior spinal artery",
    "Posterior cerebral artery",
    "Basilar artery bifurcation",
    "Posterior inferior cerebellar artery",
    "Middle cerebral artery"
]

REPLACEMENTS[(4, 36)] = [
    "Vertigo resulting from peripheral vestibular dysfunction",
    "Vertigo resulting from central pontomedullary dysfunction",
    "Presyncope resulting from non-vestibular systemic causes",
    "Oscillopsia resulting from bilateral vestibular loss",
    "Tinnitus resulting from cochlear sensorineural damage"
]

# --- UNIT 5 ---
REPLACEMENTS[(5, 3)] = [
    "Disruption of primary afferent sensory fibers within lumbar dorsal roots",
    "Loss of descending supraspinal inhibition onto lumbar motor neurons",
    "Direct degenerative destruction of lumbar anterior horn motor neurons",
    "Aberrant uninhibited synaptic transmission through lumbar dorsal columns",
    "Post-synaptic denervation hypersensitivity of quadriceps muscle fibers"
]

REPLACEMENTS[(5, 4)] = [
    "Posterior limbs of both internal capsules",
    "Sacral segments of the conus medullaris",
    "Medial parasagittal cortex of both frontal lobes",
    "Lateral convexities of both precentral gyri",
    "Lumbosacral nerve roots of the cauda equina"
]

REPLACEMENTS[(5, 11)] = [
    "Spastic paraparesis with hyperactive patellar reflexes and extensor plantars",
    "Dissociated sensory loss with preserved proprioception and intact reflexes",
    "Loss of vibration and joint position sense with preserved motor strength",
    "Flaccid paraparesis with diminished Achilles reflexes and decreased anal tone",
    "Contralateral loss of pain and temperature sensation below the lumbar level"
]

REPLACEMENTS[(5, 12)] = [
    "Lateral rubrospinal tract",
    "Lateral corticospinal tract",
    "Anterior corticospinal tract",
    "Lateral vestibulospinal tract",
    "Descending corticobulbar tract"
]

REPLACEMENTS[(5, 13)] = [
    "Corticospinal fibers decussate in the anterior white commissure of the cord",
    "Corticospinal fibers decussate within the posterior limb of internal capsule",
    "Corticospinal fibers synapse on lower motor neurons before exiting the brain",
    "Corticospinal fibers decussate in the medulla prior to entering the cord",
    "Corticospinal fibers descend ipsilaterally through the entire spinal cord"
]

REPLACEMENTS[(5, 14)] = [
    "Velocity-dependent spasticity with loss of stretch reflex inhibition",
    "Velocity-independent lead-pipe rigidity from extrapyramidal disease",
    "Flaccid muscle hypotonia from anterior horn lower motor neuron loss",
    "Cogwheel rigidity with tremor from substantia nigra degeneration",
    "Paratonic Gegenhalten resistance from diffuse frontal lobe disease"
]

REPLACEMENTS[(5, 17)] = [
    "Lower motor neuron lesion with loss of anterior horn cells",
    "Sensory polyneuropathy with loss of large myelinated fibers",
    "Upper motor neuron lesion with a hyperactive stretch reflex",
    "Neuromuscular junction disorder with impaired acetylcholine",
    "Cerebellar hemisphere lesion with ipsilateral kinetic tremor"
]

REPLACEMENTS[(5, 23)] = [
    "Precentral gyrus motor cortex; anterior cerebral artery branches",
    "Midbrain cerebral peduncle; posterior cerebral artery branches",
    "Medullary pyramid; anterior spinal artery and vertebral branches",
    "Posterior limb of internal capsule; lenticulostriate arteries",
    "Cervical spinal cord; anterior spinal artery penetrating branches"
]

REPLACEMENTS[(5, 25)] = [
    "Cavernous sinus involving oculomotor and ophthalmic divisions",
    "Superior orbital fissure involving oculomotor and abducens nerves",
    "Midbrain tegmentum involving red nucleus and medial lemniscus",
    "Substantia nigra and oculomotor nucleus in dorsal midbrain",
    "Ventral midbrain involving CN III fascicles and cerebral peduncle"
]

REPLACEMENTS[(5, 30)] = [
    "Left hypoglossal nerve lower motor neuron lesion",
    "Right hypoglossal nerve lower motor neuron lesion",
    "Right corticobulbar tract upper motor neuron lesion",
    "Left corticobulbar tract upper motor neuron lesion",
    "Left glossopharyngeal nerve lower motor neuron lesion"
]

REPLACEMENTS[(5, 33)] = [
    "Right glossopharyngeal nerve afferents",
    "Right vagus nerve motor efferents",
    "Left glossopharyngeal nerve afferents",
    "Left vagus nerve motor efferents",
    "Right hypoglossal nerve efferents"
]

REPLACEMENTS[(5, 34)] = [
    "Dorsal columns and lateral corticospinal tracts",
    "Posterior dorsal roots and dorsal column tracts",
    "Posterior inferior cerebellar artery territory",
    "Anterior white commissure and anterior horns",
    "Anterior spinal roots and cauda equina fibers"
]

REPLACEMENTS[(5, 35)] = [
    "Dorsal columns and lateral corticospinal tracts",
    "Anterior horn cells and ventral spinal rootlets",
    "Spinothalamic tracts and dorsal horn laminae",
    "Cauda equina and lumbosacral spinal roots",
    "Conus medullaris and anterior spinal artery"
]

REPLACEMENTS[(5, 37)] = [
    "Upper motor neuron lesion with loss of cortical inhibition",
    "Lower motor neuron lesion interrupting spinal reflex arcs",
    "Cerebellar vermis lesion with midline postural instability",
    "Basal ganglia lesion with impaired striatal dopaminergic tone",
    "Dorsal column lesion with loss of large proprioceptive fibers"
]

# --- UNIT 3 (Eye Disorders) ---
REPLACEMENTS[(3, 1)] = [
    "Hypersecretion of aqueous humor by the ciliary body epithelium",
    "Pupillary dilation with peripheral iris occlusion of the angle",
    "Neovascularization of the anterior chamber angle from ischemia",
    "Posterior vitreous traction inducing a neurosensory tear",
    "Fluid accumulation between Bruch membrane and pigment layer"
]

REPLACEMENTS[(3, 4)] = [
    "Separation of neurosensory retina from pigment epithelium",
    "Impaired trabecular meshwork aqueous outflow with high IOP",
    "Accumulation of extracellular drusen beneath the epithelium",
    "Apoptotic loss of rod photoreceptors with peripheral pigment",
    "Insoluble cross-linking and aggregation of lens crystallins"
]

REPLACEMENTS[(3, 5)] = [
    "Surgical delay causing contiguous spread into the contralateral lens",
    "Rapid progression of lens tumescence producing acute closed glaucoma",
    "Ischemic degeneration of perifoveal photoreceptors within few days",
    "Cortical visual deprivation during development causing amblyopia",
    "Chronic mechanical vitreous traction predisposing to retinal tear"
]

REPLACEMENTS[(3, 13)] = [
    "Autoimmune antibody destruction targeting capillary basement membrane",
    "Excessive ciliary body aqueous production causing ocular hypertension",
    "Premature denaturation and aggregation of cytoplasmic alpha-crystallins",
    "Failure of physiological apoptosis and regression of hyaloid vessels",
    "Hyperoxia vessel arrest followed by hypoxia-driven VEGF proliferation"
]

REPLACEMENTS[(3, 15)] = [
    "Painless peripheral visual field loss with optic disc cupping",
    "Severe ocular pain, conjunctival injection, and rainbow halos",
    "Progressive central scotoma with distortion on the Amsler grid",
    "Sudden onset of flashes, multiple dark floaters, and a curtain",
    "Bilateral visual blur with nighttime headlight glare and haze"
]

REPLACEMENTS[(3, 18)] = [
    "Reversible hypertrichosis with eyelash lengthening",
    "Sinus bradycardia and acute reactive bronchospasm",
    "Heterochromia with hyperpigmentation of the iris",
    "Non-anion-gap metabolic acidosis with paresthesias",
    "Accommodative ciliary spasm with periorbital aches"
]

REPLACEMENTS[(3, 19)] = [
    "Pupillary mydriasis with cycloplegic loss of near focus",
    "Progressive hyperpigmentation of the iris and lashes",
    "Enhanced uveoscleral outflow without ciliary alteration",
    "Transient systemic hypotension with compensatory tachycardia",
    "Pupillary miosis with dim-light blur and ciliary spasm"
]

REPLACEMENTS[(3, 20)] = [
    "Parasympathomimetic miotics like pilocarpine",
    "Anticholinergic mydriatics like scopolamine",
    "Beta-adrenergic antagonists like timolol",
    "Prostaglandin F2-alpha analogues like latanoprost",
    "Carbonic anhydrase inhibitors like acetazolamide"
]

REPLACEMENTS[(3, 23)] = [
    "Topical non-selective beta-blockers like timolol",
    "Intravitreal anti-VEGF monoclonal antibody injections",
    "Argon laser panretinal scatter photocoagulation",
    "Phacoemulsification with intraocular lens replacement",
    "Topical parasympathomimetic miotics like pilocarpine"
]

REPLACEMENTS[(3, 24)] = [
    "Proliferative neovascularization across the optic nerve disc",
    "Extracellular drusen beneath the retinal pigment epithelium",
    "Perivascular bone-spicule pigment deposits in the periphery",
    "Marked retinal pallor with a prominent cherry-red foveal spot",
    "Diffuse cotton-wool spots and flame-shaped microhemorrhages"
]

REPLACEMENTS[(3, 28)] = [
    "Hypertensive emergency with accelerated retinopathy",
    "Primary open-angle glaucoma with optic disc cupping",
    "Diabetic macular edema with microvascular exudates",
    "Central retinal artery occlusion with foveal pallor",
    "Demyelinating optic neuritis with papillar swelling"
]

REPLACEMENTS[(3, 29)] = [
    "Retinal vein thrombosis with extensive hemorrhages",
    "Vitreous hemorrhage from neovascular vessel rupture",
    "Autoimmune demyelinating optic neuritis episodes",
    "Carotid atheroembolus occluding the retinal artery",
    "Pupillary block with acute closed angle glaucoma"
]

REPLACEMENTS[(3, 34)] = [
    "Topical broad-spectrum fluoroquinolone antibiotic drops",
    "Topical parasympathomimetic miotics such as pilocarpine",
    "Topical dual-action mast cell stabilizer antihistamines",
    "Topical corticosteroids and cycloplegic-mydriatic agents",
    "Intravitreal vascular endothelial growth factor blockers"
]

REPLACEMENTS[(3, 36)] = [
    "Superficial erythema localized across the eyelid",
    "Mild edema confined anterior to the orbital septum",
    "High-grade fever with systemic peripheral malaise",
    "Recent upper respiratory tract bacterial sinusitis",
    "Proptosis with painful, restricted ocular movements"
]

# --- UNIT 2 (Visual Reflexes) ---
REPLACEMENTS[(2, 1)] = [
    "Right oculomotor nerve in cavernous sinus",
    "Right postganglionic ciliary ganglion",
    "Right cervical sympathetic chain at lung apex",
    "Right pretectal Edinger-Westphal nucleus",
    "Right intraorbital optic nerve trunk"
]

REPLACEMENTS[(2, 2)] = [
    "Right oculomotor nucleus lesion with adjacent corticospinal tract involvement",
    "Right lateral brainstem lesion involving descending sympathetic and spinothalamic tracts",
    "Right superior cervical ganglion lesion with sympathetic postganglionic denervation",
    "Right cavernous sinus mass lesion involving oculomotor and ophthalmic divisions",
    "Right midbrain tegmental lesion affecting the visceral Edinger-Westphal nucleus"
]

REPLACEMENTS[(2, 3)] = [
    "Pupillary parasympathetic fibers travel via the trochlear nerve rather than CN III",
    "Sympathetic pupillomotor tone actively constricts the pupil during ischemic events",
    "Visceral Edinger-Westphal preganglionic neurons lie isolated from midbrain complexes",
    "Superficial parasympathetic pupillomotor fibers are relatively spared by core ischemia",
    "Pupillary constriction is mediated directly by optic nerve collaterals bypassing CN III"
]

REPLACEMENTS[(2, 8)] = [
    "Optic nerve, LGN, visual cortex, contralateral Edinger-Westphal, CN III",
    "Optic nerve, pretectal area, both Edinger-Westphal nuclei, CN III, ciliary ganglion",
    "Optic nerve, superior colliculus, contralateral CN IV, sphincter pupillae",
    "Optic nerve, hypothalamus, thoracic IML, superior cervical ganglion, dilator",
    "Optic nerve, ipsilateral Edinger-Westphal only, ipsilateral ciliary ganglion"
]

REPLACEMENTS[(2, 9)] = [
    "The pupillary light reflex requires only direct motor CN III input",
    "The pupillary light reflex is mediated entirely by superior colliculus",
    "Pupillary afferents exit before the LGN to synapse in pretectal nuclei",
    "The sympathetic pupillary dilator pathway compensates for the loss",
    "Crossing decussating fibers from the contralateral retina compensate"
]

REPLACEMENTS[(2, 10)] = [
    "Right afferent pupillary defect from reduced optic nerve conduction",
    "Right oculomotor nerve palsy with complete internal ophthalmoplegia",
    "Left Horner syndrome from disruption of sympathetic innervation",
    "Right Adie tonic pupil with denervation cholinergic sensitivity",
    "Normal physiological pupillary response with symmetric light reflex"
]

REPLACEMENTS[(2, 11)] = [
    "Ischemic infarction of the optic nerve head",
    "Pituitary adenoma compressing chiasmal crossing fibers",
    "Rhegmatogenous retinal detachment across the macula",
    "Demyelinating optic neuritis linked to multiple sclerosis",
    "Acute closed-angle glaucoma with severe corneal edema"
]

REPLACEMENTS[(2, 12)] = [
    "Superior cervical sympathetic ganglion",
    "Ciliary ganglion and short ciliary nerves",
    "Optic nerve fibers at the orbital apex",
    "Oculomotor trunk within the cavernous sinus",
    "Cervical paravertebral sympathetic chain"
]

REPLACEMENTS[(2, 13)] = [
    "Zonular fibers tighten and the lens flattens for distance",
    "Iris dilator contracts producing pupillary mydriasis",
    "Zonular fibers relax and the lens rounds up for near focus",
    "Ciliary epithelium increases aqueous humor secretion",
    "Vitreous gel contracts reducing internal ocular volume"
]

REPLACEMENTS[(2, 14)] = [
    "Accommodation requires visual cortical processing, whereas light reflex bypasses cortex",
    "Direct light reflex requires cortical occipital processing, whereas near reflex does not",
    "Both oculomotor nerve trunks suffered incomplete partial axonal shearing injuries",
    "Bilateral ciliary ganglia suffered ischemic postganglionic parasympathetic damage",
    "Sympathetic pupillary pathways suffered traumatic injury along the cervical cord"
]

REPLACEMENTS[(2, 17)] = [
    "Cocaine acts as a direct alpha-1 adrenergic agonist on dilator pupillae",
    "Cocaine acts as a competitive muscarinic antagonist on sphincter pupillae",
    "Cocaine directly stimulates nicotinic and muscarinic cholinergic receptors",
    "Cocaine blocks norepinephrine reuptake, requiring intact tonic basal release",
    "Cocaine directly stimulates rapid release of vesicular norepinephrine pools"
]

REPLACEMENTS[(2, 19)] = [
    "Pharmacologic blockade by muscarinic antagonist drops",
    "Parasympathetic denervation with Adie tonic pupil",
    "Mechanical uncal herniation with compressive CN III palsy",
    "Oculosympathetic disruption causing Horner syndrome",
    "Demyelinating inflammation causing acute optic neuritis"
]

REPLACEMENTS[(2, 21)] = [
    "Compression of CN III parasympathetic fibers by uncal herniation",
    "Direct ischemic infarction of the contralateral oculomotor nucleus",
    "Traumatic transection of sympathetic fibers in the cavernous sinus",
    "Severe contusion of the ipsilateral optic nerve at the orbital canal",
    "Contralateral uncal herniation compressing the cerebral peduncle"
]

REPLACEMENTS[(2, 24)] = [
    "Left dorsal pons involving medial longitudinal fasciculus",
    "Right dorsal pons involving CN VI nucleus/PPRF and MLF",
    "Right rostral midbrain involving CN III and red nucleus",
    "Left cavernous sinus involving abducens and trochlear",
    "Bilateral frontal eye fields in frontal motor cortex"
]

REPLACEMENTS[(2, 25)] = [
    "Ventral caudal pons involving corticospinal fibers",
    "Medullary pyramids and hypoglossal nerve rootlets",
    "Dorsal rostral midbrain pretectum and commissure",
    "Frontal eye fields within middle frontal gyri",
    "Occipital striate visual cortex bordering calcarine"
]

REPLACEMENTS[(2, 26)] = [
    "Pupillary light reflex to direct illumination",
    "Reflex orienting of eyes and head toward visual cues",
    "Near triad accommodation and pupillary miosis",
    "Sound localization and auditory spatial mapping",
    "Sympathetic pupillary dilation in darkness"
]

REPLACEMENTS[(2, 30)] = [
    "Oculomotor nerve (CN III)",
    "Trochlear nerve (CN IV)",
    "Maxillary nerve (V2)",
    "Mandibular nerve (V3)",
    "Abducens nerve (CN VI)"
]

REPLACEMENTS[(2, 31)] = [
    "Facial vein to superior ophthalmic vein to cavernous sinus",
    "Facial artery to internal carotid artery to cavernous sinus",
    "Facial lymphatic drainage into deep cervical lymph nodes",
    "Retromandibular vein to external jugular to sigmoid sinus",
    "Direct retrograde bacterial transit via arachnoid spaces"
]

REPLACEMENTS[(2, 33)] = [
    "Eye deviated up and in from superior rectus action",
    "Eye deviated down and in from inferior rectus action",
    "Eye deviated down and out from superior oblique and CN VI",
    "Eye maintained in central position without strabismus",
    "Eye deviated up and out from inferior oblique action"
]

REPLACEMENTS[(2, 34)] = [
    "Horner syndrome paralyzes only the levator palpebrae superioris muscle",
    "Horner syndrome selectively impairs orbicularis oculi eyelid closure",
    "Horner syndrome disrupts third cranial nerve somatic motor output",
    "Horner syndrome spares both the superior tarsal and levator muscles",
    "Horner syndrome paralyzes superior tarsal muscle while levator remains intact"
]

REPLACEMENTS[(2, 35)] = [
    "Muscarinic M3 receptor antagonism producing passive pupillary dilation",
    "Alpha-1 adrenergic agonism producing active pupillary dilator contraction",
    "Beta-2 adrenergic receptor agonism promoting ciliary muscle relaxation",
    "Muscarinic M3 receptor agonism producing active pupillary constriction",
    "Inhibition of presynaptic norepinephrine reuptake in the ciliary body"
]

# --- UNIT 1 (Visual System) ---
REPLACEMENTS[(1, 3)] = [
    "Left Meyer loop in the temporal lobe",
    "Left optic tract bordering crus cerebri",
    "Left superior optic radiations in parietal lobe",
    "Right superior optic radiations in parietal lobe",
    "Left lingual gyrus bordering calcarine sulcus"
]

REPLACEMENTS[(1, 7)] = [
    "Eye too long or refractive power too strong; concave lens",
    "Eye too short or refractive power too weak; convex lens",
    "Unequal corneal curvature across meridians; cylindrical lens",
    "Age-related lens stiffening; positive reading glasses",
    "Rhegmatogenous retinal detachment; pneumatic retinopexy"
]

REPLACEMENTS[(1, 8)] = [
    "Eye too short with focal point behind retina; convex lens",
    "Unequal corneal curvature across meridians; cylindrical lens",
    "Eye too long with focal point in front of retina; concave lens",
    "Stiff crystalline lens with decreased near focus; bifocals",
    "Autoimmune optic nerve demyelination; intravenous steroids"
]

REPLACEMENTS[(1, 9)] = [
    "Asymmetric corneal curvature across principal meridians",
    "Shortened axial eyeball length focusing behind the fovea",
    "Drusen deposition in the macular retinal pigment layer",
    "Age-related lens stiffening with loss of accommodation",
    "Elongated axial globe length focusing anterior to retina"
]

REPLACEMENTS[(1, 10)] = [
    "Excess axial globe length; concave spherical lens",
    "Shortened axial globe length; convex spherical lens",
    "Loss of crystalline lens elasticity; bifocal reading lenses",
    "Peripheral retinal tear; argon laser barrier retinopexy",
    "Unequal curvature across meridians; cylindrical lens"
]

REPLACEMENTS[(1, 11)] = [
    "Crystalline lens",
    "Corneal surface",
    "Vitreous humor",
    "Aqueous humor",
    "Retinal layer"
]

REPLACEMENTS[(1, 13)] = [
    "Fovea centralis",
    "Macula lutea",
    "Ora serrata",
    "Vitreous base",
    "Optic nerve disc"
]

REPLACEMENTS[(1, 14)] = [
    "Elevated intracranial pressure transmitted along optic nerve sheath",
    "Autoimmune demyelinating inflammation of intraorbital optic nerve",
    "Acute embolic occlusion of the central retinal artery bifurcation",
    "Extracellular drusen accumulation beneath retinal pigment layer",
    "Glaucomatous axonal death with progressive optic nerve cupping"
]

REPLACEMENTS[(1, 15)] = [
    "Sustained elevation in cytoplasmic cGMP levels opening cation channels",
    "Activation of transducin and PDE, closing cGMP-gated sodium channels",
    "Opening of voltage-dependent L-type calcium channels across terminal",
    "Increased tonic release of glutamate onto postsynaptic bipolar cells",
    "Direct dephosphorylation and opening of cGMP-activated sodium channels"
]

REPLACEMENTS[(1, 18)] = [
    "Secreting aqueous humor into the posterior chamber",
    "Phagocytosing shed outer segments and recycling retinal",
    "Propagating all-or-none action potentials to optic chiasm",
    "Refracting incident light rays directly onto the fovea",
    "Synthesizing hyaluronic acid for the vitreous matrix"
]

REPLACEMENTS[(1, 20)] = [
    "Right optic nerve prior to chiasm",
    "Central crossing optic chiasm",
    "Contralateral left optic tract",
    "Right parietal optic radiations",
    "Right calcarine occipital cortex"
]

REPLACEMENTS[(1, 25)] = [
    "Right Meyer loop in the temporal lobe",
    "Right dorsal optic radiations in parietal lobe",
    "Left dorsal optic radiations in parietal lobe",
    "Right lingual gyrus along the calcarine",
    "Left optic tract bordering cerebral peduncle"
]

REPLACEMENTS[(1, 28)] = [
    "The fovea projects exclusively through the ipsilateral optic tract",
    "Direct destruction of occipital pole foveal visual representation",
    "Foveal ganglion axons project bilaterally to both occipital lobes",
    "Total ischemic necrosis of the lateral geniculate relay nucleus",
    "Traumatic complete transection of the ipsilateral optic nerve"
]

REPLACEMENTS[(1, 29)] = [
    "Cortical blindness from bilateral calcarine sulcus infarction",
    "Hemispatial neglect from non-dominant parietal lobe injury",
    "Prosopagnosia from bilateral fusiform gyrus damage",
    "Anton visual anosognosia from striate cortex infarction",
    "Pure alexia without agraphia from splenium infarction"
]

REPLACEMENTS[(1, 30)] = [
    "Superior altitudinal visual defect in the left eye",
    "Inferior altitudinal visual defect in the left eye",
    "Bitemporal hemianopic visual field defect in both eyes",
    "Monocular central scotoma in the affected left eye",
    "Homonymous hemianopia affecting the right visual field"
]

REPLACEMENTS[(1, 33)] = [
    "Photoreceptor outer segments",
    "Retinal bipolar interneurons",
    "Retinal ganglion projection cells",
    "Lateral geniculate relay neurons",
    "Pretectal olivary nucleus cells"
]

REPLACEMENTS[(1, 35)] = [
    "Deprived eye loses cortical synaptic territory in ocular dominance columns",
    "Extensive apoptotic death of retinal ganglion cells in the deprived eye",
    "Selective proliferative sprouting of LGN neurons serving the closed eye",
    "Total preservation of physiological binocular cortical response profiles",
    "Permanent irreversible crystalline lens clouding from lack of light"
]

# Apply replacements and audit
compiled_181 = []
global_id = 1

for u_num in range(1, 6):
    unit_qs = parsed_by_unit[u_num]
    for q in unit_qs:
        key = (u_num, q['unit_q_num'])
        if key in REPLACEMENTS:
            rep_texts = REPLACEMENTS[key]
            new_opts = []
            for idx, letter in enumerate(['A', 'B', 'C', 'D', 'E']):
                new_opts.append({'id': letter, 'text': rep_texts[idx]})
            q['options'] = new_opts
        
        q['id'] = global_id
        q['q_num'] = global_id
        compiled_181.append(q)
        global_id += 1

print(f"\nCompiled {len(compiled_181)} total questions.")

# RUN FULL AUDIT ON COMPILED 181
audit_flags = []
for q in compiled_181:
    corr = next(o for o in q['options'] if o['id'] == q['correct_answer'])
    dists = [o for o in q['options'] if o['id'] != q['correct_answer']]
    c_text = corr['text']
    c_len = len(c_text)
    d_lens = [len(d['text']) for d in dists]
    max_d = max(d_lens)
    min_d = min(d_lens)
    
    issues = []
    # Paren check
    c_p = '(' in c_text and ')' in c_text
    d_p = sum(1 for d in dists if '(' in d['text'] and ')' in d['text'])
    if c_p and d_p == 0:
        issues.append('PAREN_ONLY_IN_CORRECT')
    elif not c_p and d_p == len(dists):
        issues.append('PAREN_IN_ALL_DISTRACTORS_ONLY')
    elif c_p and d_p == 1:
        issues.append('PAREN_ASYMMETRY')
        
    # Length check
    if c_len > 1.35 * max_d and c_len > max_d + 12:
        issues.append(f'CORRECT_TOO_LONG (c={c_len}, max_d={max_d})')
    elif c_len < 0.65 * min_d and min_d - c_len > 12:
        issues.append(f'CORRECT_TOO_SHORT (c={c_len}, min_d={min_d})')
        
    # Semicolon / colon check
    if ';' in c_text and not any(';' in d['text'] for d in dists):
        issues.append('SEMICOLON_ONLY_IN_CORRECT')
    if ':' in c_text and not any(':' in d['text'] for d in dists):
        issues.append('COLON_ONLY_IN_CORRECT')
        
    for giveaway in [', which ', ' because ', ', leading to ', ', resulting in ']:
        if giveaway in c_text and not any(giveaway in d['text'] for d in dists):
            issues.append(f'GIVEAWAY_CLAUSE ({giveaway.strip()})')
            break
            
    if issues:
        audit_flags.append((q['id'], q['category'], q['unit_q_num'], issues, c_text))

print(f"\nAudit completed. Flags found: {len(audit_flags)}")
for f in audit_flags:
    print(f"  Q{f[0]} ({f[1]} Q{f[2]}): {f[3]}")
    print(f"    Correct text: {f[4]}")

# If clean, save questions to JSON and Markdown review doc
if len(audit_flags) == 0:
    out_json = "/Users/markyoussef_1/.gemini/antigravity-ide/scratch/usmle_exam1/exam2_inhouse_questions.json"
    with open(out_json, "w", encoding="utf-8") as f:
        json.dump(compiled_181, f, indent=2, ensure_ascii=False)
    print(f"Saved cleaned JSON to {out_json}")
    
    # Save review markdown
    out_md = "/Users/markyoussef_1/.gemini/antigravity-ide/scratch/usmle_exam1/exam2_inhouse_questions_review.md"
    md_lines = [
        "# Neuroscience Exam 2: In-House Step 1 Question Bank (181 Questions)",
        "",
        "Cleaned, balanced, and verified USMLE Step 1 single-best-answer questions from `Neuro_Exam2_Step1_QBank.md`.",
        "",
        "| Unit | Topic | Question Range | Count |",
        "|------|-------|----------------|-------|",
        "| 1 | Visual System | Q1 – Q36 | 36 Qs |",
        "| 2 | Visual Reflexes | Q37 – Q72 | 36 Qs |",
        "| 3 | Eye Disorders | Q73 – Q108 | 36 Qs |",
        "| 4 | Auditory & Vestibular Systems | Q109 – Q144 | 36 Qs |",
        "| 5 | UMN / LMN | Q145 – Q181 | 37 Qs |",
        "",
        "---",
        ""
    ]
    for q in compiled_181:
        md_lines.append(f"### Q{q['id']}: [{q['category']}] Unit {q['unit_num']} Q{q['unit_q_num']}")
        md_lines.append(q['stem'] + "\n")
        for o in q['options']:
            md_lines.append(f"- **{o['id']}.** {o['text']}")
        md_lines.append(f"\n<details><summary>Click to view Answer &amp; Explanation</summary>\n\n"
                        f"**Correct Answer: {q['correct_answer']}**\n\n"
                        f"{q['explanation']}\n\n</details>\n\n---\n")
    with open(out_md, "w", encoding="utf-8") as f:
        f.write("\n".join(md_lines))
    print(f"Saved review Markdown to {out_md}")
