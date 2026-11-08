import json
from test_gen_structure import check_q

u2_questions = [
    {
        "id": "exam3_g_h_u2_q1",
        "category": "Unit 02: Cerebellum",
        "subcategory": "Cerebellar Syndromes",
        "question_type": "clinical_vignette",
        "stem": "A 58-year-old chronic alcohol user presents with severe broad-based gait ataxia and impaired heel-to-shin testing. Testing reveals normal finger-to-nose coordination, normal rapid alternating hand movements, and crisp speech articulation without dysarthria. Which cerebellar region and afferent tract have undergone selective neurodegeneration?",
        "options": [
            {"label": "A", "text": "Anterior superior vermis and dorsal spinocerebellar afferents", "is_correct": True},
            {"label": "B", "text": "Flocculonodular cortex and primary labyrinthine afferents", "is_correct": False},
            {"label": "C", "text": "Lateral hemisphere cortex and corticopontine afferents", "is_correct": False},
            {"label": "D", "text": "Posterior inferior vermis and olivocerebellar afferents", "is_correct": False},
            {"label": "E", "text": "Dentate projection nucleus and rubrospinal afferents", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "Chronic alcohol neurotoxicity causes selective degeneration of Purkinje cells in the anterior and superior vermis (spinocerebellum), which receives lower extremity somatosensory inputs via dorsal spinocerebellar tracts. This selectively disrupts lower extremity coordination and gait while sparing the lateral cerebrocerebellar hemispheres that coordinate upper extremity fine motor movements and speech articulation.",
        "high_yield_takeaway": "Alcoholic cerebellar degeneration selectively affects the anterior superior vermis, leading to truncal and lower limb gait ataxia with relative sparing of upper limb coordination and speech."
    },
    {
        "id": "exam3_g_h_u2_q2",
        "category": "Unit 02: Cerebellum",
        "subcategory": "Cerebellar Examination",
        "question_type": "clinical_vignette",
        "stem": "A 42-year-old woman with multiple sclerosis is evaluated for upper extremity incoordination. The examiner asks her to flex her right elbow against manual resistance, then suddenly releases his grip. Her right forearm recoils forcefully and strikes her anterior chest before arresting. What physiologic defect accounts for this examination finding?",
        "options": [
            {"label": "A", "text": "Delayed activation of antagonist triceps braking contractions", "is_correct": True},
            {"label": "B", "text": "Hyperactive monosynaptic stretch reflexes in the bicep tendon", "is_correct": False},
            {"label": "C", "text": "Denervation hypersensitivity within neuromuscular endplates", "is_correct": False},
            {"label": "D", "text": "Loss of recurrent Renshaw cell inhibition in anterior horns", "is_correct": False},
            {"label": "E", "text": "Impaired gamma motor neuron efferent tone to muscle spindles", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "This demonstrates Holmes rebound phenomenon, a hallmark of ipsilateral cerebellar hemisphere disease. Normally, the cerebellum rapidly computes the sudden drop in load and immediately activates antagonist muscles (triceps) while shutting off agonists (biceps) to brake the limb. Cerebellar dysfunction delays this antagonist braking loop, causing overshoot.",
        "high_yield_takeaway": "The Holmes rebound phenomenon is caused by delayed activation of antagonist muscle braking due to ipsilateral cerebellar intermediate or hemispheric pathology."
    },
    {
        "id": "exam3_g_h_u2_q3",
        "category": "Unit 02: Cerebellum",
        "subcategory": "Functional Localization",
        "question_type": "clinical_vignette",
        "stem": "A 34-year-old man exhibits an intention tremor, past-pointing on finger-to-nose testing, and impaired rapid alternating hand movements on the right side only. Strength and sensation are completely intact bilaterally. A focal lesion is identified in the right deep cerebellum. Which deep nucleus and output peduncle are responsible for these motor planning deficits?",
        "options": [
            {"label": "A", "text": "Dentate nucleus projecting via the superior peduncle", "is_correct": True},
            {"label": "B", "text": "Fastigial nucleus projecting via the inferior peduncle", "is_correct": False},
            {"label": "C", "text": "Emboliform nucleus projecting via the middle peduncle", "is_correct": False},
            {"label": "D", "text": "Globose nucleus projecting via the stria medullaris", "is_correct": False},
            {"label": "E", "text": "Interposed nucleus projecting via the dorsal column", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "The lateral cerebellar hemisphere coordinates multi-joint voluntary limb movements and motor planning through the dentate nucleus. Dentate efferents exit through the superior cerebellar peduncle (brachium conjunctivum), decussate in the lower midbrain to reach the contralateral ventrolateral (VL) thalamus, and project to motor cortex. Corticospinal fibers then cross back at the medullary decussation, resulting in ipsilateral cerebellar deficits.",
        "high_yield_takeaway": "The lateral cerebrocerebellar hemisphere projects via the dentate nucleus and superior cerebellar peduncle to coordinate ipsilateral limb motor planning."
    },
    {
        "id": "exam3_g_h_u2_q4",
        "category": "Unit 02: Cerebellum",
        "subcategory": "Pediatric Posterior Fossa",
        "question_type": "clinical_vignette",
        "stem": "A 6-year-old boy presents with progressive morning headaches, vomiting, severe truncal instability, and downbeat nystagmus. When seated with his back fully supported against a wall, his finger-to-nose coordination and rapid alternating movements are completely normal. Neuroimaging reveals a mass invading the cerebellar vermis and roof of the fourth ventricle. Which functional division and deep nucleus are primary sites of compression?",
        "options": [
            {"label": "A", "text": "Vestibulocerebellar flocculonodular lobe and fastigial nucleus", "is_correct": True},
            {"label": "B", "text": "Cerebrocerebellar lateral hemisphere and dentate projection nucleus", "is_correct": False},
            {"label": "C", "text": "Spinocerebellar intermediate hemisphere and emboliform nucleus", "is_correct": False},
            {"label": "D", "text": "Paleocerebellar paralaminar cortex and globose projection nucleus", "is_correct": False},
            {"label": "E", "text": "Neocerebellar ventral cortex and lateral vestibular nucleus complex", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "Midline cerebellar lesions (such as medulloblastoma) compress the vestibulocerebellum (flocculonodular lobe and vermis) and the fastigial nucleus. This results in truncal ataxia, titubation, dysequilibrium, and downbeat nystagmus, while sparing appendicular coordination (lateral hemisphere/dentate), so limb testing remains intact when trunk support is provided.",
        "high_yield_takeaway": "Vermis and flocculonodular lobe lesions cause truncal ataxia, dysequilibrium, and nystagmus with preserved limb coordination when the trunk is supported."
    },
    {
        "id": "exam3_g_h_u2_q5",
        "category": "Unit 02: Cerebellum",
        "subcategory": "Hereditary Ataxias",
        "question_type": "clinical_vignette",
        "stem": "A 16-year-old girl is evaluated for worsening clumsiness and progressive gait unsteadiness over two years. Physical examination shows bilateral pes cavus, hammer toes, severe thoracic kyphoscoliosis, absent lower extremity deep tendon reflexes, and bilateral upward Babinski signs. What underlying cardiac pathology represents the primary cause of premature death in patients with this disorder?",
        "options": [
            {"label": "A", "text": "Hypertrophic cardiomyopathy with asymmetric septal hypertrophy", "is_correct": True},
            {"label": "B", "text": "Dilated cardiomyopathy secondary to chronic viral myocarditis", "is_correct": False},
            {"label": "C", "text": "Fibromuscular dysplasia involving proximal coronary arteries", "is_correct": False},
            {"label": "D", "text": "Myxomatous mitral valve prolapse with chordal rupture", "is_correct": False},
            {"label": "E", "text": "Constrictive pericarditis with progressive fibrocalcification", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "Friedreich ataxia is an autosomal recessive disorder caused by GAA trinucleotide repeat expansion in the FXN gene on chromosome 9, encoding frataxin. Frataxin deficiency impairs mitochondrial iron homeostasis and respiration. Hypertrophic cardiomyopathy (asymmetric septal hypertrophy and arrhythmia) occurs in >90% of patients and is the leading cause of death.",
        "high_yield_takeaway": "Friedreich ataxia (GAA repeat in FXN) presents with spinocerebellar ataxia, absent DTRs, extensor plantars, pes cavus, and hypertrophic cardiomyopathy (leading cause of death)."
    },
    {
        "id": "exam3_g_h_u2_q6",
        "category": "Unit 02: Cerebellum",
        "subcategory": "Cerebellar Microcircuitry",
        "question_type": "clinical_vignette",
        "stem": "In an electrophysiologic study of cerebellar motor learning, microelectrodes in the Purkinje cell layer record all-or-none complex spikes featuring a high-amplitude primary action potential followed by small high-frequency wavelets. Which brainstem structure provides the monosynaptic excitatory climbing fiber inputs that generate these specific complex spikes?",
        "options": [
            {"label": "A", "text": "Contralateral inferior olivary nucleus in the medullary tegmentum", "is_correct": True},
            {"label": "B", "text": "Ipsilateral basal pontine nuclei within the ventral pontine bulge", "is_correct": False},
            {"label": "C", "text": "Bilateral vestibular nuclear complex adjacent to fourth ventricle", "is_correct": False},
            {"label": "D", "text": "Contralateral red nucleus within the rostral midbrain tegmentum", "is_correct": False},
            {"label": "E", "text": "Ipsilateral dorsal motor vagal nucleus in the floor of fourth ventricle", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "Climbing fibers originate exclusively from the contralateral inferior olivary nucleus in the medulla. Each Purkinje cell receives synaptic input from a single climbing fiber that wraps extensively around its dendritic tree, releasing aspartate/glutamate to evoke a powerful, prolonged all-or-none complex spike (error signal in motor learning).",
        "high_yield_takeaway": "Climbing fibers originate exclusively from the contralateral inferior olivary nucleus and generate all-or-none complex spikes in Purkinje cells."
    },
    {
        "id": "exam3_g_h_u2_q7",
        "category": "Unit 02: Cerebellum",
        "subcategory": "Cerebellar Microcircuitry",
        "question_type": "clinical_vignette",
        "stem": "A neuroscientist records baseline high-frequency simple spikes from cerebellar Purkinje cells during repetitive limb movements. Targeted application of a glutamate receptor antagonist to parallel fibers completely abolishes these simple spikes while sparing climbing fiber input. From which interneurons do these parallel fibers originate?",
        "options": [
            {"label": "A", "text": "Granule cells located within the cerebellar internal granular layer", "is_correct": True},
            {"label": "B", "text": "Golgi interneurons providing feedback to mossy fiber glomeruli", "is_correct": False},
            {"label": "C", "text": "Basket cells providing feedforward axosomatic inhibition", "is_correct": False},
            {"label": "D", "text": "Stellate interneurons distributing axodendritic inhibition", "is_correct": False},
            {"label": "E", "text": "Unipolar brush cells amplifying vestibular mossy fiber signals", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "Mossy fibers terminate on granule cells within cerebellar glomeruli. Granule cell axons ascend to the molecular layer, bifurcate into T-shaped parallel fibers, and synapse on dendrites of hundreds of Purkinje cells, driving high-frequency simple spikes. Golgi cells inhibit granule cells, while basket and stellate cells inhibit Purkinje cells.",
        "high_yield_takeaway": "Mossy fibers excite granule cells whose parallel fibers ascend and bifurcate to excite Purkinje cells, generating high-frequency simple spikes."
    },
    {
        "id": "exam3_g_h_u2_q8",
        "category": "Unit 02: Cerebellum",
        "subcategory": "Peduncular Anatomy",
        "question_type": "clinical_vignette",
        "stem": "A 28-year-old woman develops a solitary demyelinating plaque selectively interrupting the left superior cerebellar peduncle. Neurophysiological testing demonstrates impaired unconscious proprioceptive feedback from Golgi tendon organs of the left lower extremity. By which pathway did this proprioceptive signal traverse the neuroaxis to reach this peduncle?",
        "options": [
            {"label": "A", "text": "Ventral spinocerebellar tract crossing in cord and recrossing in peduncle", "is_correct": True},
            {"label": "B", "text": "Dorsal spinocerebellar tract ascending uncrossed through the restiform body", "is_correct": False},
            {"label": "C", "text": "Cuneocerebellar tract ascending uncrossed from lateral cuneate nucleus", "is_correct": False},
            {"label": "D", "text": "Corticopontocerebellar pathway crossing within the ventral pontine tegmentum", "is_correct": False},
            {"label": "E", "text": "Olivocerebellar pathway crossing within the medullary interolivary space", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "The ventral spinocerebellar tract transmits lower extremity Golgi tendon organ inputs (whole-limb motor feedback). It decussates in the anterior white commissure of the spinal cord, ascends to the rostral pons/midbrain, enters the cerebellum via the superior cerebellar peduncle, and decussates a second time to terminate in the ipsilateral cerebellar cortex (double cross).",
        "high_yield_takeaway": "The ventral spinocerebellar tract double-crosses (first in spinal cord, second in superior cerebellar peduncle), conveying proprioceptive feedback to the ipsilateral cerebellum."
    },
    {
        "id": "exam3_g_h_u2_q9",
        "category": "Unit 02: Cerebellum",
        "subcategory": "Paraneoplastic Disorders",
        "question_type": "clinical_vignette",
        "stem": "A 62-year-old woman develops subacute, rapidly progressive truncal and limb ataxia, vertigo, and scanning dysarthria over four weeks. Brain MRI reveals no focal mass or stroke, but cerebrospinal fluid shows mild lymphocytic pleocytosis. Serum testing is strongly positive for anti-Yo antibodies (anti-Purkinje cell cytoplasmic antibodies). Which neoplasm is most likely occult in this patient?",
        "options": [
            {"label": "A", "text": "Ovarian adenocarcinoma or high-grade serous carcinoma", "is_correct": True},
            {"label": "B", "text": "Small cell lung carcinoma expressing neuroendocrine antigens", "is_correct": False},
            {"label": "C", "text": "Thymoma associated with acetylcholine receptor autoantibodies", "is_correct": False},
            {"label": "D", "text": "Hodgkin lymphoma expressing Reed-Sternberg cytoplasmic markers", "is_correct": False},
            {"label": "E", "text": "Renal clear cell carcinoma with paraneoplastic erythrocytosis", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "Anti-Yo (PCA-1) antibodies target Purkinje cell cytoplasmic antigens CDR2 and CDR2L and are strongly associated with paraneoplastic cerebellar degeneration in women with gynecologic malignancies (ovarian, fallopian, uterine) or breast carcinoma. Anti-Hu is associated with small cell lung cancer; anti-Tr is associated with Hodgkin lymphoma.",
        "high_yield_takeaway": "Anti-Yo paraneoplastic cerebellar degeneration causes rapid Purkinje cell loss and is most commonly associated with ovarian and breast carcinomas."
    },
    {
        "id": "exam3_g_h_u2_q10",
        "category": "Unit 02: Cerebellum",
        "subcategory": "Clinical Examination",
        "question_type": "clinical_vignette",
        "stem": "A 55-year-old man presents with persistent gait instability. On examination, when asked to stand with his feet together and eyes open, he immediately sways violently and requires examiner support to prevent falling. Closing his eyes does not significantly alter the severity of his severe postural swaying. Where is the lesion most likely localized?",
        "options": [
            {"label": "A", "text": "Cerebellar midline vermis impairing central motor coordination", "is_correct": True},
            {"label": "B", "text": "Cervical dorsal columns causing proprioceptive deafferentation", "is_correct": False},
            {"label": "C", "text": "Bilateral peripheral large-fiber sensory polyneuropathy", "is_correct": False},
            {"label": "D", "text": "Bilateral vestibular end-organs within membranous semicircular canals", "is_correct": False},
            {"label": "E", "text": "Posterior root entry zones in the lumbar spinal cord", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "A true positive Romberg sign occurs when a patient is steady with eyes open but loses balance when eyes are closed, indicating sensory ataxia (dorsal column or peripheral proprioceptive loss). In cerebellar vermis lesions, patients exhibit cerebellar ataxia: they are unsteady with eyes open AND eyes closed because visual compensation cannot overcome central cerebellar motor incoordination.",
        "high_yield_takeaway": "Cerebellar ataxia causes unsteadiness with eyes open and closed; sensory ataxia causes unsteadiness only after eyes are closed (positive Romberg)."
    },
    {
        "id": "exam3_g_h_u2_q11",
        "category": "Unit 02: Cerebellum",
        "subcategory": "Brainstem & Tract Decussation",
        "question_type": "clinical_vignette",
        "stem": "A 64-year-old man suffers an ischemic stroke involving the caudal midbrain tegmentum at the level of the inferior colliculi, directly transecting the decussation of the superior cerebellar peduncles. Which clinical manifestation would be expected on neurological examination?",
        "options": [
            {"label": "A", "text": "Bilateral intention tremor and severe appendicular ataxia", "is_correct": True},
            {"label": "B", "text": "Contralateral hemiparesis and ipsilateral oculomotor palsy", "is_correct": False},
            {"label": "C", "text": "Isolated ipsilateral Horner syndrome and hoarseness", "is_correct": False},
            {"label": "D", "text": "Loss of pain and temperature on the contralateral body only", "is_correct": False},
            {"label": "E", "text": "Isolated vertical gaze palsy with preserved convergence", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "The superior cerebellar peduncles carry dentatorubrothalamic projections from both cerebellar hemispheres. They decussate completely in the caudal midbrain tegmentum at the level of the inferior colliculus. A focal lesion directly across this decussation transects efferents from BOTH hemispheres, causing bilateral intention tremor and severe bilateral appendicular ataxia.",
        "high_yield_takeaway": "A lesion transecting the decussation of the superior cerebellar peduncles in the caudal midbrain causes bilateral intention tremor and limb ataxia."
    },
    {
        "id": "exam3_g_h_u2_q12",
        "category": "Unit 02: Cerebellum",
        "subcategory": "Neurogenetic Syndromes",
        "question_type": "clinical_vignette",
        "stem": "A 4-year-old boy presents with progressive cerebellar ataxia, choreoathetosis, recurrent severe sinopulmonary bacterial infections, and prominent conjunctival telangiectasias. Laboratory evaluation reveals marked deficiency of serum IgA and significantly elevated alpha-fetoprotein. What molecular cellular defect is responsible for this patient's disease?",
        "options": [
            {"label": "A", "text": "Defective ATM kinase signaling in double-strand DNA break repair", "is_correct": True},
            {"label": "B", "text": "Impaired nucleotide excision repair of ultraviolet DNA photoproducts", "is_correct": False},
            {"label": "C", "text": "Trinucleotide GAA expansion impairing mitochondrial iron-sulfur biogenesis", "is_correct": False},
            {"label": "D", "text": "Peroxisomal ATP-binding cassette transporter assembly failure", "is_correct": False},
            {"label": "E", "text": "Lysosomal sphingomyelinase deficiency causing lipid storage in neurons", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "Ataxia-telangiectasia is an autosomal recessive disorder caused by mutations in the ATM gene on chromosome 11q22. ATM encodes a serine/threonine protein kinase involved in sensing double-stranded DNA breaks and initiating cell-cycle checkpoint arrest/repair. Defective repair causes cerebellar Purkinje cell loss, immunodeficiency (low IgA), telangiectasias, elevated AFP, and sensitivity to ionizing radiation.",
        "high_yield_takeaway": "Ataxia-telangiectasia (ATM mutation) impairs double-strand DNA break repair, causing cerebellar ataxia, telangiectasias, recurrent infections, low IgA, and high AFP."
    },
    {
        "id": "exam3_g_h_u2_q13",
        "category": "Unit 02: Cerebellum",
        "subcategory": "Peduncular Anatomy",
        "question_type": "clinical_vignette",
        "stem": "A 61-year-old hypertensive man develops acute right-sided dysmetria and dysdiadochokinesia without motor weakness or sensory loss. Diffusion-weighted MRI reveals an acute ischemic infarction isolated to the right middle cerebellar peduncle (brachium pontis). Which afferent fiber tract has been directly transected by this lesion?",
        "options": [
            {"label": "A", "text": "Transverse pontocerebellar fibers from contralateral pontine nuclei", "is_correct": True},
            {"label": "B", "text": "Dorsal spinocerebellar fibers ascending from Clarke column", "is_correct": False},
            {"label": "C", "text": "Dentatothalamic projection fibers directed to the ventral thalamus", "is_correct": False},
            {"label": "D", "text": "Primary vestibular fibers emerging from scarpa ganglion", "is_correct": False},
            {"label": "E", "text": "Rubrospinal motor projections descending to the cervical spinal cord", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "The middle cerebellar peduncle (brachium pontis) is the largest cerebellar peduncle and contains exclusively afferent fibers: the transverse pontocerebellar tract. Corticopontine fibers from the contralateral cerebral cortex synapse in the basal pontine nuclei, whose axons cross the midline and travel via the MCP to enter the cerebellar hemisphere.",
        "high_yield_takeaway": "The middle cerebellar peduncle consists exclusively of afferent transverse pontocerebellar fibers arising from the contralateral pontine nuclei."
    },
    {
        "id": "exam3_g_h_u2_q14",
        "category": "Unit 02: Cerebellum",
        "subcategory": "Structural Malformations",
        "question_type": "clinical_vignette",
        "stem": "A 26-year-old woman presents with severe suboccipital throbbing headaches worsened by coughing and sneezing, downbeat nystagmus, and progressive bilateral hand muscle wasting with loss of pinprick and temperature sensation across her shoulders and arms. Brain MRI confirms 8 mm herniation of cerebellar tonsils below the foramen magnum. What spinal cord finding is most likely present?",
        "options": [
            {"label": "A", "text": "Central fluid-filled syringomyelia cavity in cervical cord", "is_correct": True},
            {"label": "B", "text": "Extensive demyelination isolated to the dorsal funiculi", "is_correct": False},
            {"label": "C", "text": "Anterior spinal artery occlusion with bilateral anterior horn infarction", "is_correct": False},
            {"label": "D", "text": "Extramedullary schwannoma compressing the lumbar thecal sac", "is_correct": False},
            {"label": "E", "text": "Subacute combined degeneration involving corticospinal tracts", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "Chiari I malformation is characterized by downward herniation of cerebellar tonsils (>5 mm) through the foramen magnum, often asymptomatic until adulthood. It disrupts normal CSF flow dynamics at the craniocervical junction, strongly associating with cervical syringomyelia. Syringomyelia expands to compress anterior white commissure fibers, producing a 'cape-like' loss of pain and temperature sensation.",
        "high_yield_takeaway": "Chiari I malformation (tonsillar ectopia >5 mm) commonly presents in young adults with cough headaches, downbeat nystagmus, and syringomyelia (cape-like thermoanalgesia)."
    },
    {
        "id": "exam3_g_h_u2_q15",
        "category": "Unit 02: Cerebellum",
        "subcategory": "Cerebellar Reflexes",
        "question_type": "clinical_vignette",
        "stem": "A 48-year-old woman recovering from a cerebellar stroke is evaluated in the clinic. When the examiner taps her patellar tendon, her leg extends and then continues swinging back and forth like a pendulum for six oscillations before coming to rest. What neuromuscular physiological abnormality produces this pendular reflex?",
        "options": [
            {"label": "A", "text": "Loss of cerebellar tonic facilitatory drive to muscle stretch receptors", "is_correct": True},
            {"label": "B", "text": "Hyperactivity of upper motor neuron corticospinal tract efferents", "is_correct": False},
            {"label": "C", "text": "Loss of primary afferent depolarization within spinal interneurons", "is_correct": False},
            {"label": "D", "text": "Persistent tetanic recruitment of slow-twitch motor units", "is_correct": False},
            {"label": "E", "text": "Selective destruction of Renshaw inhibitory spinal interneurons", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "Pendular reflexes are a classic sign of cerebellar hypotonia. The cerebellum normally maintains baseline gamma motor neuron efferent tone and coordinates antagonist damping. With cerebellar lesions, reduced muscle tone and lack of antagonist muscle damping allow the limb to swing passively back and forth under the influence of gravity alone.",
        "high_yield_takeaway": "Pendular reflexes result from cerebellar hypotonia and loss of antagonist muscle damping, allowing the limb to swing passively like a pendulum."
    },
    {
        "id": "exam3_g_h_u2_q16",
        "category": "Unit 02: Cerebellum",
        "subcategory": "Brainstem Stroke Syndromes",
        "question_type": "clinical_vignette",
        "stem": "A 59-year-old man presents with sudden acute vertigo, nausea, hoarseness, left facial numbness, and severe left-sided limb ataxia. Physical examination reveals left-sided Horner syndrome, left vocal cord paralysis, and decreased pinprick sensation over the right arm and leg. What specific cerebellar input structure damaged in the dorsolateral medulla explains his left limb ataxia?",
        "options": [
            {"label": "A", "text": "Inferior cerebellar peduncle within the dorsolateral medullary rim", "is_correct": True},
            {"label": "B", "text": "Middle cerebellar peduncle transversing the ventral pons", "is_correct": False},
            {"label": "C", "text": "Superior cerebellar peduncle descending from midbrain tegmentum", "is_correct": False},
            {"label": "D", "text": "Medial longitudinal fasciculus adjacent to the median raphe", "is_correct": False},
            {"label": "E", "text": "Ventral tegmental decussation of rubrospinal motor fibers", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "This patient has lateral medullary (Wallenberg) syndrome due to occlusion of the posterior inferior cerebellar artery (PICA) or vertebral artery. The ipsilateral limb ataxia is caused by infarction of the inferior cerebellar peduncle (restiform body), which carries spinocerebellar and olivocerebellar inputs into the cerebellum.",
        "high_yield_takeaway": "In Wallenberg syndrome (PICA infarct), ipsilateral limb ataxia is caused by damage to the inferior cerebellar peduncle (restiform body)."
    },
    {
        "id": "exam3_g_h_u2_q17",
        "category": "Unit 02: Cerebellum",
        "subcategory": "Cerebellar Non-Motor Functions",
        "question_type": "clinical_vignette",
        "stem": "A 52-year-old accountant recovers from surgical resection of a right cerebellar hemisphere hemangioblastoma. While his motor coordination recovers completely, his family notes striking changes: he exhibits concrete thinking, severe planning deficits, flattened affect, and impaired verbal fluency. Neuropsychological evaluation confirms Cerebellar Cognitive Affective Syndrome. Through which thalamic relay does the neocerebellum normally communicate with prefrontal cortex to support these executive functions?",
        "options": [
            {"label": "A", "text": "Ventrolateral and mediodorsal nuclei of the contralateral thalamus", "is_correct": True},
            {"label": "B", "text": "Ventral posteromedial nucleus carrying facial sensory information", "is_correct": False},
            {"label": "C", "text": "Lateral geniculate nucleus mediating visual spatial attention", "is_correct": False},
            {"label": "D", "text": "Medial geniculate body coordinating auditory working memory", "is_correct": False},
            {"label": "E", "text": "Anterior thalamic nucleus coordinating mamillothalamic memory circuits", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "The posterior neocerebellar lobes connect reciprocally with the prefrontal cortex via the dentatothalamocortical pathway, synapsing in the ventrolateral (VL) and mediodorsal (MD) thalamic nuclei. Lesions here cause Cerebellar Cognitive Affective Syndrome (Schmahmann syndrome), presenting with executive dysfunction, spatial cognition deficits, personality change/blunting, and language impairment.",
        "high_yield_takeaway": "The posterior neocerebellum projects via the dentate nucleus to ventrolateral and mediodorsal thalamic nuclei to regulate executive cognitive functions and affect."
    },
    {
        "id": "exam3_g_h_u2_q18",
        "category": "Unit 02: Cerebellum",
        "subcategory": "Deep Cerebellar Nuclei",
        "question_type": "clinical_vignette",
        "stem": "An experimental neurophysiology protocol selectively microinjects a GABA-A receptor agonist into the interposed nuclei (emboliform and globose) of non-human primates. Which physiological motor deficit is selectively elicited during ongoing voluntary target-directed limb movements?",
        "options": [
            {"label": "A", "text": "Impaired real-time execution and error correction of limb trajectories", "is_correct": True},
            {"label": "B", "text": "Severe resting tremor that completely abolishes upon voluntary initiation", "is_correct": False},
            {"label": "C", "text": "Isolated loss of vestibulo-ocular reflex without limb dysmetria", "is_correct": False},
            {"label": "D", "text": "Complete flaccid paralysis of all distal extremity musculature", "is_correct": False},
            {"label": "E", "text": "Bilateral cogwheel rigidity with preserved movement velocity", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "The intermediate cerebellar hemisphere (spinocerebellum) projects to the interposed nuclei (emboliform and globose). Unlike the dentate nucleus (which handles motor planning prior to movement), the interposed nuclei project to the red nucleus and motor cortex to regulate ongoing movement execution and correct ongoing movement trajectory errors.",
        "high_yield_takeaway": "The interposed nuclei (emboliform and globose) receive spinocerebellar input and modulate ongoing voluntary limb movement execution and trajectory correction."
    },
    {
        "id": "exam3_g_h_u2_q19",
        "category": "Unit 02: Cerebellum",
        "subcategory": "Differential Diagnosis of Ataxia",
        "question_type": "clinical_vignette",
        "stem": "A 22-year-old collegiate runner develops progressive sensory ataxia, bilateral extensor plantar responses, marked loss of vibration and joint position sense, absent ankle and knee reflexes, and bilateral high-arched feet. Serum cobalamin and methylmalonic acid levels are normal, and rapid plasma reagin (RPR) is non-reactive. Which molecular diagnostic test is most likely to confirm the etiology?",
        "options": [
            {"label": "A", "text": "Targeted gene sequencing for GAA repeat expansions in the FXN gene", "is_correct": True},
            {"label": "B", "text": "Polymerase chain reaction for CAG repeat expansion in huntingtin gene", "is_correct": False},
            {"label": "C", "text": "Multiplex ligation probe amplification for PMP22 duplication", "is_correct": False},
            {"label": "D", "text": "Southern blot analysis for CGG repeat expansion in the FMR1 gene", "is_correct": False},
            {"label": "E", "text": "Fluorescence in situ hybridization for deletion on chromosome 22q11", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "This patient presents with classic Friedreich ataxia: combination of dorsal column loss (sensory ataxia), corticospinal involvement (extensor plantars), peripheral neuropathy (absent DTRs), and skeletal abnormalities (pes cavus). Testing for GAA repeat expansion in the FXN gene (encoding frataxin) on chromosome 9 confirms the diagnosis. Normal cobalamin rules out subacute combined degeneration, and negative RPR rules out tabes dorsalis.",
        "high_yield_takeaway": "Friedreich ataxia is confirmed by detecting GAA trinucleotide repeat expansion in the FXN gene on chromosome 9."
    },
    {
        "id": "exam3_g_h_u2_q20",
        "category": "Unit 02: Cerebellum",
        "subcategory": "Cerebellar Speech Pathology",
        "question_type": "clinical_vignette",
        "stem": "A 39-year-old woman with advanced spinocerebellar ataxia produces speech that is slow, slurred, and fragmented into unnatural pauses between syllables, with explosive variations in vocal volume and pitch (scanning speech). Which functional anatomical zone of the cerebellum is primarily responsible for coordinating the rhythm and articulation of speech?",
        "options": [
            {"label": "A", "text": "Superior cerebellar vermis and adjacent intermediate paravermis", "is_correct": True},
            {"label": "B", "text": "Bilateral flocculonodular lobes coordinating oculomotor vergence", "is_correct": False},
            {"label": "C", "text": "Lateral neocerebellar cortex of the posterior inferior lobules", "is_correct": False},
            {"label": "D", "text": "Fastigial projection pathways to the lateral vestibular nuclei", "is_correct": False},
            {"label": "E", "text": "Dentatothalamic decussation within the caudal red nucleus capsule", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "Cerebellar dysarthria (scanning speech or ataxic dysarthria) is characterized by slow, disjointed, syllabic articulation with irregular stress and loudness. It results from damage to the superior cerebellar vermis and adjacent intermediate zone (paravermis), particularly in the left or bilateral hemispheres, which coordinate orofacial and respiratory muscles during speech articulation.",
        "high_yield_takeaway": "Scanning speech (ataxic dysarthria) results from lesions involving the superior cerebellar vermis and adjacent intermediate cortex."
    }
]

if __name__ == "__main__":
    for q in u2_questions:
        check_q(q)
    print("gen_g_h_u2.py: All 20 questions passed validation!")
