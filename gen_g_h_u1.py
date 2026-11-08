# gen_g_h_u1.py
# Unit 01: Demyelinating Diseases (20 Higher-Order MCQs)

U1_QUESTIONS = [
    {
        "id": "gh_u1_q1",
        "category": "Unit 01: Demyelinating Diseases",
        "stem": "A 28-year-old woman with relapsing-remitting multiple sclerosis presents with 4 days of painful right eye movements, central scotoma, and 4/5 left leg weakness. Visual acuity is 20/200 in the right eye, and swinging-flashlight testing reveals a right afferent pupillary defect. Intravenous high-dose methylprednisolone is initiated. What is the primary cellular mechanism by which this acute therapy accelerates neurological recovery?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Direct induction of rapid Schwann cell proliferation and axonal remyelination"},
            {"letter": "B", "is_correct": True, "text": "Reduction of capillary endothelial permeability and suppression of inflammatory cytokines"},
            {"letter": "C", "is_correct": False, "text": "Selective cytotoxicity and irreversible clonal deletion of memory B-lymphocytes"},
            {"letter": "D", "is_correct": False, "text": "Competitive blockade of sphingosine-1-phosphate receptors on circulating leukocytes"},
            {"letter": "E", "is_correct": False, "text": "Neutralization of circulating autoantibodies against aquaporin-4 water channels"}
        ],
        "correct_idx": 1,
        "explanation": "High-dose intravenous corticosteroids (methylprednisolone 1,000 mg daily for 3-5 days) treat acute MS relapses by rapidly stabilizing the blood-brain barrier (decreasing endothelial capillary permeability), downregulating pro-inflammatory cytokines (TNF-alpha, IFN-gamma), and inhibiting T-cell activation and trafficking. Corticosteroids do not stimulate remyelination, delete B-cells (unlike anti-CD20 agents), or block S1P receptors (fingolimod mechanism).",
        "high_yield_pearl": "High-Yield Rule: Acute MS relapses are treated with high-dose IV methylprednisolone to rapidly restore the blood-brain barrier and reduce vasogenic edema; corticosteroids accelerate recovery time but do not alter long-term disability progression.",
        "image": None
    },
    {
        "id": "gh_u1_q2",
        "category": "Unit 01: Demyelinating Diseases",
        "stem": "A 34-year-old woman with highly active relapsing-remitting multiple sclerosis is evaluated for disease-modifying therapy. Before prescribing natalizumab, her neurologist orders serum anti-JC virus antibody testing. What is the molecular mechanism of natalizumab that creates an elevated risk for progressive multifocal leukoencephalopathy?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Depletion of surface CD20 on pre-B cells preventing immunoglobulin G synthesis"},
            {"letter": "B", "is_correct": False, "text": "Internalization of sphingosine-1-phosphate receptors trapping T-cells in lymph nodes"},
            {"letter": "C", "is_correct": True, "text": "Blockade of alpha-4 beta-1 integrin preventing leukocyte transmigration across the blood-brain barrier"},
            {"letter": "D", "is_correct": False, "text": "Inhibition of dihydroorotate dehydrogenase arresting pyrimidine nucleotide synthesis"},
            {"letter": "E", "is_correct": False, "text": "Selective antagonism of complement factor C5 preventing membrane attack complex formation"}
        ],
        "correct_idx": 2,
        "explanation": "Natalizumab is a humanized monoclonal antibody directed against the alpha-4 subunit of alpha-4-beta-1 (VLA-4) integrin on leukocytes. By blocking VLA-4 interaction with VCAM-1 on vascular endothelial cells, it prevents leukocytes from crossing the blood-brain barrier. While highly effective in MS, this prevents normal central nervous system immune surveillance, allowing latent JC polyomavirus in oligodendrocytes to reactivate and produce opportunistic progressive multifocal leukoencephalopathy (PML).",
        "high_yield_pearl": "High-Yield Rule: Natalizumab blocks alpha-4 integrin, preventing immune cell extravasation into the CNS; the resulting lack of CNS immune surveillance creates a major risk of PML in patients seropositive for JC virus.",
        "image": None
    },
    {
        "id": "gh_u1_q3",
        "category": "Unit 01: Demyelinating Diseases",
        "stem": "A 29-year-old woman presents with horizontal diplopia. On neurological examination, during attempted leftward conjugate gaze, the right eye fails to adduct past the midline, and the left abducting eye exhibits horizontal nystagmus. However, when the patient focuses on an approaching target at the nose, both eyes converge symmetrically and both pupils constrict. Which anatomical feature explains the preservation of adduction during convergence?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Convergence pathways travel exclusively through the contralateral abducens nucleus"},
            {"letter": "B", "is_correct": True, "text": "Convergence signals project directly from pretectal inputs to the oculomotor nucleus bypassing the MLF"},
            {"letter": "C", "is_correct": False, "text": "Convergence relies on cortical innervation from the frontal eye fields traveling in the pyramid"},
            {"letter": "D", "is_correct": False, "text": "The medial longitudinal fasciculus only carries autonomic pupillary fibers from the midbrain"},
            {"letter": "E", "is_correct": False, "text": "The abducens motor neurons provide primary innervation to the medial rectus during near fixation"}
        ],
        "correct_idx": 1,
        "explanation": "This patient has right internuclear ophthalmoplegia (INO) due to a demyelinating lesion of the right medial longitudinal fasciculus (MLF). Conjugate horizontal saccades require abducens interneurons in the pons to send axons through the contralateral MLF to the oculomotor nucleus in the midbrain. In contrast, the vergence pathway arises in the visual association cortex and midbrain pretectal area, projecting directly to both oculomotor nuclear complexes without traversing the MLF. Thus, convergence and pupillary near-response are preserved.",
        "high_yield_pearl": "High-Yield Rule: In internuclear ophthalmoplegia (INO), the MLF lesion impairs adduction during horizontal conjugate saccades, but adduction is fully preserved during convergence because vergence signals bypass the MLF.",
        "image": None
    },
    {
        "id": "gh_u1_q4",
        "category": "Unit 01: Demyelinating Diseases",
        "stem": "A 41-year-old woman presents with bilateral sequential visual loss and severe paraparesis. Spinal MRI demonstrates a continuous T2 hyperintensity extending from C2 to T1, and serum testing reveals high-titer autoantibodies against aquaporin-4 (AQP4). Which disease-modifying therapy commonly prescribed for multiple sclerosis is contraindicated because it can precipitate catastrophic, fulminant relapses in this condition?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Eculizumab targeting the terminal complement protein C5"},
            {"letter": "B", "is_correct": False, "text": "Rituximab directed against the CD20 surface antigen on B-lymphocytes"},
            {"letter": "C", "is_correct": True, "text": "Fingolimod sequestering lymphocytes within secondary lymphoid organs"},
            {"letter": "D", "is_correct": False, "text": "Mycophenolate mofetil inhibiting inosine monophosphate dehydrogenase"},
            {"letter": "E", "is_correct": False, "text": "Intravenous methylprednisolone administered during acute exacerbations"}
        ],
        "correct_idx": 2,
        "explanation": "The patient has neuromyelitis optica spectrum disorder (NMOSD), characterized by anti-AQP4 autoantibodies and longitudinally extensive transverse myelitis (LETM >=3 vertebral segments). Standard MS therapies such as fingolimod, natalizumab, and interferon-beta can paradoxically trigger severe, life-threatening exacerbations in NMOSD by augmenting humoral and astrocytic inflammation. NMOSD maintenance therapy relies on B-cell depletion (rituximab), IL-6 receptor blockade (satralizumab), complement C5 inhibition (eculizumab), or immunosuppressants (mycophenolate mofetil).",
        "high_yield_pearl": "High-Yield Rule: Multiple sclerosis disease-modifying agents (fingolimod, natalizumab, interferon-beta) can cause severe, fatal relapses in neuromyelitis optica (NMO); NMO requires targeted B-cell or complement-directed therapies.",
        "image": None
    },
    {
        "id": "gh_u1_q5",
        "category": "Unit 01: Demyelinating Diseases",
        "stem": "A 36-year-old woman experiences 3 weeks of intractable nausea, projectile vomiting, and continuous hiccups that fail to respond to antiemetic and prokinetic medications. Thorough gastroenterological evaluation is negative. Two weeks later, she develops bilateral optic neuritis. Which neuroanatomical region lacks an intact blood-brain barrier, permitting circulating anti-AQP4 antibodies to initiate her initial presentation?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Nucleus ambiguus located in the rostral ventrolateral medulla"},
            {"letter": "B", "is_correct": True, "text": "Area postrema situated in the caudal floor of the fourth ventricle"},
            {"letter": "C", "is_correct": False, "text": "Nucleus tractus solitarius receiving visceral sensory vagal afferents"},
            {"letter": "D", "is_correct": False, "text": "Dorsal motor nucleus of the vagus nerve mediating parasympathetic tone"},
            {"letter": "E", "is_correct": False, "text": "Inferior salivatory nucleus situated in the pontomedullary junction"}
        ],
        "correct_idx": 1,
        "explanation": "The patient exhibits area postrema syndrome, a classic initial manifestation of neuromyelitis optica spectrum disorder (NMOSD). The area postrema is a circumventricular organ located in the caudal floor of the fourth ventricle. Because it lacks a blood-brain barrier and has fenestrated capillaries, it serves as the emetic chemoreceptor trigger zone and is uniquely exposed to circulating anti-AQP4 IgG antibodies, leading to astrocytopathy, intractable nausea, vomiting, and hiccups.",
        "high_yield_pearl": "High-Yield Rule: Area postrema syndrome (intractable hiccups, nausea, and vomiting) is a hallmark of NMO spectrum disorder; the area postrema lacks a blood-brain barrier, allowing circulating anti-AQP4 IgG direct access to astrocyte end-feet.",
        "image": None
    },
    {
        "id": "gh_u1_q6",
        "category": "Unit 01: Demyelinating Diseases",
        "stem": "A 7-year-old boy is brought to the emergency department with fever, lethargy, confusion, ataxia, and new-onset seizures 10 days after recovering from a viral upper respiratory illness. Brain MRI reveals widespread, bilateral, asymmetric, poorly demarcated hyperintensities in the subcortical white matter and deep basal ganglia, all demonstrating homogeneous gadolinium enhancement. Which feature most reliably differentiates this condition from multiple sclerosis?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Detection of elevated cerebrospinal fluid protein concentration above 100 mg/dL"},
            {"letter": "B", "is_correct": True, "text": "Monophasic course with simultaneous inflammatory lesions of identical chronological age and encephalopathy"},
            {"letter": "C", "is_correct": False, "text": "Presence of multiple white matter lesions involving the posterior fossa and spinal cord"},
            {"letter": "D", "is_correct": False, "text": "Favorable clinical improvement following a short course of high-dose corticosteroids"},
            {"letter": "E", "is_correct": False, "text": "Development of focal neurological motor deficits affecting the appendicular musculature"}
        ],
        "correct_idx": 1,
        "explanation": "Acute disseminated encephalomyelitis (ADEM) is a post-infectious, immune-mediated demyelinating encephalopathy primarily affecting children. Unlike multiple sclerosis, which requires dissemination in time and space with lesions of varying ages (some enhancing, some non-enhancing), ADEM is characteristically monophasic, features prominent early encephalopathy (lethargy, delirium, coma), and shows multifocal lesions that are all of identical age (all enhancing simultaneously on MRI).",
        "high_yield_pearl": "High-Yield Rule: ADEM is distinguished from multiple sclerosis by its monophasic post-viral course, prominent encephalopathy/altered mental status, and simultaneous dissemination in space where all lesions enhance simultaneously (no dissemination in time).",
        "image": None
    },
    {
        "id": "gh_u1_q7",
        "category": "Unit 01: Demyelinating Diseases",
        "stem": "A 44-year-old man develops rapidly progressive symmetric leg weakness and difficulty climbing stairs 3 weeks after an episode of bloody diarrhea. Physical examination shows flaccid quadriparesis and generalized areflexia, but sensation is intact. Nerve conduction studies show markedly reduced compound muscle action potential (CMAP) amplitudes with preserved conduction velocities and normal distal latencies. What is the molecular target of the autoantibodies driving this presentation?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Schwann cell peripheral myelin protein 22 located in compact internodal myelin"},
            {"letter": "B", "is_correct": True, "text": "GM1 and GD1a gangliosides localized at the axolemma of motor nodes of Ranvier"},
            {"letter": "C", "is_correct": False, "text": "GQ1b gangliosides concentrated within the oculomotor and abducens nerve sheaths"},
            {"letter": "D", "is_correct": False, "text": "Postsynaptic nicotinic acetylcholine receptors situated at the motor endplate"},
            {"letter": "E", "is_correct": False, "text": "Presynaptic P/Q-type voltage-gated calcium channels at the neuromuscular junction"}
        ],
        "correct_idx": 1,
        "explanation": "This patient has the acute motor axonal neuropathy (AMAN) variant of Guillain-Barre syndrome, classic following Campylobacter jejuni enteritis. Lipooligosaccharides on C. jejuni share molecular mimicry with gangliosides GM1 and GD1a. Antibodies bind directly to the axolemma at the nodes of Ranvier, recruiting complement and macrophages that disrupt voltage-gated sodium channels. This produces pure motor axonal injury characterized electrodiagnostically by reduced CMAP amplitudes without conduction slowing or prolonged latencies.",
        "high_yield_pearl": "High-Yield Rule: AMAN variant of GBS involves autoantibodies against GM1 and GD1a gangliosides at nodes of Ranvier (not myelin), producing reduced CMAPs with preserved conduction velocities, often after Campylobacter jejuni infection.",
        "image": None
    },
    {
        "id": "gh_u1_q8",
        "category": "Unit 01: Demyelinating Diseases",
        "stem": "A 53-year-old man presents with acute-onset diplopia and marked unsteadiness on his feet. Neurological examination reveals bilateral symmetric external ophthalmoplegia, bilateral ptosis, severe gait and limb ataxia, and generalized absence of deep tendon reflexes. Muscle strength is 5/5 in all four extremities, and sensory examination is normal. Serum testing is most likely to identify high-titer autoantibodies against which antigen?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Presynaptic voltage-gated potassium channels expressed on central interneurons"},
            {"letter": "B", "is_correct": False, "text": "GM1 gangliosides expressed on the motor axons of the lumbosacral plexus"},
            {"letter": "C", "is_correct": True, "text": "GQ1b gangliosides densely expressed on ocular motor cranial nerves and sensory spindles"},
            {"letter": "D", "is_correct": False, "text": "Myelin oligodendrocyte glycoprotein localized to central oligodendroglial membranes"},
            {"letter": "E", "is_correct": False, "text": "Aquaporin-4 water channels enriched on astrocytic foot processes surrounding capillaries"}
        ],
        "correct_idx": 2,
        "explanation": "The clinical triad of ophthalmoplegia, ataxia, and areflexia with preserved motor strength defines Miller Fisher syndrome, a localized variant of Guillain-Barre syndrome. It is caused by molecular mimicry leading to high-titer IgG autoantibodies against GQ1b ganglioside. GQ1b is enriched in the paranodal regions of cranial nerves III, IV, and VI, as well as the large-diameter group Ia primary afferent fibers supplying muscle spindles, explaining the ophthalmoplegia, ataxia, and areflexia.",
        "high_yield_pearl": "High-Yield Rule: Miller Fisher syndrome presents with the classic triad of ophthalmoplegia, ataxia, and areflexia, and is pathognomonic for anti-GQ1b ganglioside antibodies targeting cranial nerves III/IV/VI and muscle spindle afferents.",
        "image": None
    },
    {
        "id": "gh_u1_q9",
        "category": "Unit 01: Demyelinating Diseases",
        "stem": "A 49-year-old man hospitalized with acute inflammatory demyelinating polyneuropathy (GBS) requires mechanical ventilation. On hospital day 4, telemetry captures episodes of sinus bradycardia down to 32 bpm alternating with sinus tachycardia of 145 bpm. Blood pressure fluctuates between 75/40 mmHg and 215/115 mmHg without administration of vasoactive agents. What is the fundamental pathological cause of these hemodynamic fluctuations?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Ischemic necrosis of the solitary tract nucleus caused by vertebrobasilar occlusion"},
            {"letter": "B", "is_correct": True, "text": "Demyelination of afferent baroreceptor nerves and efferent autonomic sympathetic and parasympathetic fibers"},
            {"letter": "C", "is_correct": False, "text": "Acute catecholamine surge secondary to underlying undiagnosed adrenal pheochromocytoma"},
            {"letter": "D", "is_correct": False, "text": "Autoantibody-mediated cross-reactivity directly destroying sinoatrial nodal pacemaker cells"},
            {"letter": "E", "is_correct": False, "text": "Severe hypovolemia resulting from syndrome of inappropriate antidiuretic hormone secretion"}
        ],
        "correct_idx": 1,
        "explanation": "Dysautonomia occurs in approximately two-thirds of patients with Guillain-Barre syndrome and is a major cause of sudden mortality. The mechanism is demyelination of both afferent baroreceptor pathways (carotid sinus and aortic arch fibers via CN IX and X) and efferent postganglionic sympathetic and parasympathetic autonomic fibers. This results in loss of central baroreflex buffering, producing dramatic swings in blood pressure, labile heart rate, sinus arrest, and tachyarrhythmias.",
        "high_yield_pearl": "High-Yield Rule: Dysautonomia in GBS results from demyelination of visceral afferent baroreceptors and autonomic outflow fibers; it manifests as extreme hemodynamic lability, cardiac arrhythmias, and is a leading cause of mortality in GBS.",
        "image": None
    },
    {
        "id": "gh_u1_q10",
        "category": "Unit 01: Demyelinating Diseases",
        "stem": "A 32-year-old woman is admitted with acute ascending motor weakness and areflexia that began 48 hours ago. Vital capacity is declining, and lumbar puncture demonstrates albuminocytologic dissociation. The family inquires why high-dose oral or intravenous corticosteroids should not be added to her treatment regimen of intravenous immunoglobulin. What is the evidence-based rationale for avoiding corticosteroids in acute GBS?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Corticosteroids trigger sudden conversion of demyelinating neuropathy into axonal motor neuron disease"},
            {"letter": "B", "is_correct": False, "text": "Corticosteroids induce irreversible autoimmune glomerulonephritis when combined with intravenous immunoglobulin"},
            {"letter": "C", "is_correct": True, "text": "Corticosteroids fail to confer clinical efficacy in randomized trials and can impair peripheral nerve remyelination"},
            {"letter": "D", "is_correct": False, "text": "Corticosteroids accelerate the enzymatic clearance and metabolic degradation of intravenous immunoglobulin"},
            {"letter": "E", "is_correct": False, "text": "Corticosteroids directly stimulate bacterial proliferation in previously infected gastrointestinal tracts"}
        ],
        "correct_idx": 2,
        "explanation": "Multiple large randomized controlled trials (including Cochrane systematic reviews) have demonstrated that corticosteroids (oral or intravenous) are ineffective in acute Guillain-Barre syndrome and may actually delay motor recovery and impede axonal remyelination. In contrast, intravenous immunoglobulin (IVIG) and therapeutic plasma exchange (plasmapheresis) are proven, equally effective first-line disease-modifying therapies for GBS.",
        "high_yield_pearl": "High-Yield Rule: Corticosteroids are ineffective and contraindicated in acute Guillain-Barre syndrome because they do not improve outcomes and may impede nerve remyelination; first-line therapy is IVIG or plasma exchange.",
        "image": None
    },
    {
        "id": "gh_u1_q11",
        "category": "Unit 01: Demyelinating Diseases",
        "stem": "An 18-year-old man presents with progressive difficulty walking, frequent ankle sprains, and bilateral foot deformities since early adolescence. Examination shows high arching of the foot (pes cavus), claw toes, atrophy of the intrinsic foot muscles and distal calves (\"stork leg\" appearance), and bilateral absent ankle reflexes. Sural nerve biopsy reveals prominent \"onion-bulb\" formations. What is the genetic mechanism responsible for this autosomal dominant condition?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Trinucleotide GAA repeat expansion in the first intron of the frataxin gene"},
            {"letter": "B", "is_correct": True, "text": "Duplication of a 1.4-megabase segment containing the PMP22 gene on chromosome 17p11.2"},
            {"letter": "C", "is_correct": False, "text": "Homozygous deletion of the survival motor neuron 1 (SMN1) gene on chromosome 5q"},
            {"letter": "D", "is_correct": False, "text": "Trinucleotide CTG expansion in the 3-prime untranslated region of the DMPK gene"},
            {"letter": "E", "is_correct": False, "text": "Frameshift mutation in the dystrophin gene resulting in premature stop codon termination"}
        ],
        "correct_idx": 1,
        "explanation": "Charcot-Marie-Tooth disease type 1A (CMT1A) is the most common hereditary motor and sensory neuropathy. It is inherited in an autosomal dominant fashion and caused by a 1.4-Mb duplication on chromosome 17p11.2 encompassing the peripheral myelin protein 22 (PMP22) gene. PMP22 overexpression disrupts compact myelin maintenance, leading to repeated cycles of demyelination and remyelination that produce redundant concentric Schwann cell cytoplasmic layers resembling 'onion bulbs' on biopsy.",
        "high_yield_pearl": "High-Yield Rule: CMT1A is caused by PMP22 gene duplication on chromosome 17p11.2; biopsy shows 'onion-bulb' Schwann cell hyperplasia surrounding demyelinated axons.",
        "image": None
    },
    {
        "id": "gh_u1_q12",
        "category": "Unit 01: Demyelinating Diseases",
        "stem": "A 52-year-old man with severe alcohol use disorder and malnutrition is admitted with stupor and a serum sodium of 104 mEq/L. Over the next 20 hours, intravenous hypertonic saline administration raises his serum sodium to 130 mEq/L. Three days later, he becomes mute, quadriplegic, and dysphagic, communicating only through vertical eye movements. What cellular biophysical mechanism directly initiates the demyelination in the basis pontis?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Intracellular brain edema resulting from rapid water influx into hypertonic astrocyte cell bodies"},
            {"letter": "B", "is_correct": True, "text": "Acute cell shrinkage and oligodendrocyte apoptosis caused by rapid extracellular hyperosmotic fluid shift"},
            {"letter": "C", "is_correct": False, "text": "Selective thrombotic occlusion of paramedian penetrating branches of the basilar artery"},
            {"letter": "D", "is_correct": False, "text": "Excitotoxic excessive glutamate stimulation triggering neuronal calcium overload in pontine nuclei"},
            {"letter": "E", "is_correct": False, "text": "Immune complex deposition inducing classical complement cascade activation along myelin sheaths"}
        ],
        "correct_idx": 1,
        "explanation": "In chronic hyponatremia (>48 hours), brain cells adapt by extruding organic osmolytes (glutamate, myoinositol, taurine) to prevent cerebral edema. When serum sodium is corrected too rapidly (>8-10 mEq/L in 24 hours), the extracellular fluid becomes hyperosmolar relative to brain cells. Water shifts rapidly out of cells, causing severe dehydration and apoptosis of oligodendrocytes. The basis pontis is exquisitely vulnerable because intersecting transverse pontocerebellar and longitudinal corticospinal fibers create a rigid anatomic meshwork with little room for shrinkage without mechanical shear.",
        "high_yield_pearl": "High-Yield Rule: Rapid correction of chronic hyponatremia causes central pontine myelinolysis (osmotic demyelination) due to rapid cellular shrinkage and apoptosis of pontine oligodendrocytes in the basis pontis.",
        "image": None
    },
    {
        "id": "gh_u1_q13",
        "category": "Unit 01: Demyelinating Diseases",
        "stem": "In the patient described with central pontine myelinolysis, neurological examination reveals intact alertness, flaccid quadriparesis, bilateral facial paralysis, complete loss of horizontal saccades, but intact vertical gaze and voluntary eyelid elevation. Which anatomical region's preservation allows maintenance of vertical eye movements and consciousness in this locked-in state?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Paramedian pontine reticular formation and bilateral abducens nuclei in the dorsal caudal pons"},
            {"letter": "B", "is_correct": True, "text": "Rostral interstitial nucleus of the MLF, oculomotor nuclei, and ascending reticular activating system in the midbrain"},
            {"letter": "C", "is_correct": False, "text": "Inferior cerebellar peduncles and bilateral vestibular nuclei within the rostral medulla oblongata"},
            {"letter": "D", "is_correct": False, "text": "Corticobulbar tracts traversing the middle cerebellar peduncles to the trigeminal motor nuclei"},
            {"letter": "E", "is_correct": False, "text": "Descending tectospinal and vestibulospinal tracts traversing the anterior funiculus of the spinal cord"}
        ],
        "correct_idx": 1,
        "explanation": "Central pontine myelinolysis destroys the basis pontis (corticospinal and corticobulbar tracts) and can involve horizontal gaze centers in the pontine tegmentum (PPRF and CN VI). However, vertical eye movements are mediated by the rostral interstitial nucleus of the medial longitudinal fasciculus (riMLF) and the oculomotor/trochlear complexes in the midbrain tegmentum, which receive blood from the posterior cerebral artery and are anatomically rostral to the pontine lesion. The midbrain reticular activating system is also spared, preserving alertness (locked-in syndrome).",
        "high_yield_pearl": "High-Yield Rule: Locked-in syndrome from CPM preserves consciousness and vertical eye movements/eyelid opening because the midbrain tegmentum (reticular activating system, riMLF, and CN III/IV) is spared above the pontine lesion.",
        "image": None
    },
    {
        "id": "gh_u1_q14",
        "category": "Unit 01: Demyelinating Diseases",
        "stem": "A 26-year-old woman with multiple sclerosis presents with a sudden electric-shock-like sensation that shoots down her neck and spine into her legs whenever she bends her head forward to tie her shoes (Lhermitte sign). This symptom localizes to a demyelinating plaque in which spinal cord pathway?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Anterior corticospinal tract mediating axial motor tone and postural stability"},
            {"letter": "B", "is_correct": True, "text": "Cervical dorsal columns producing mechanosensitive ectopic action potential discharge"},
            {"letter": "C", "is_correct": False, "text": "Lateral spinothalamic tract conducting pain and temperature sensation from the trunk"},
            {"letter": "D", "is_correct": False, "text": "Ventral spinocerebellar tract conveying unconscious proprioception from the limbs"},
            {"letter": "E", "is_correct": False, "text": "Intermediolateral cell column supplying preganglionic sympathetic outflow to viscera"}
        ],
        "correct_idx": 1,
        "explanation": "Lhermitte sign (a paroxysmal electric shock sensation triggered by neck flexion radiating down the spine and extremities) is a classic finding in multiple sclerosis. It indicates demyelination within the cervical spinal cord posterior columns (fasciculus gracilis and cuneatus). Neck flexion exerts mechanical traction on demyelinated, hyperexcitable primary sensory axons lacking their normal insulating myelin sheath, triggering ectopic mechanosensitive action potential discharge.",
        "high_yield_pearl": "High-Yield Rule: Lhermitte sign localizes to demyelination within the cervical spinal cord dorsal columns, where neck flexion mechanically stretches hyperexcitable, demyelinated sensory axons.",
        "image": None
    },
    {
        "id": "gh_u1_q15",
        "category": "Unit 01: Demyelinating Diseases",
        "stem": "A 31-year-old woman with a history of optic neuritis 2 years ago reports that whenever she takes a hot bath or exercises vigorously, her vision in the right eye becomes markedly blurry and washed-out. After resting in an air-conditioned room for 30 minutes, her vision returns completely to baseline. Which biophysical principle explains this transient phenomenon?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Thermal vasodilation shunting blood away from the ophthalmic artery causing retinal ischemia"},
            {"letter": "B", "is_correct": True, "text": "Temperature elevation accelerates sodium channel inactivation, reducing the action potential safety factor in demyelinated axons"},
            {"letter": "C", "is_correct": False, "text": "Heat-induced breakdown of the blood-retinal barrier permitting acute complement infiltration"},
            {"letter": "D", "is_correct": False, "text": "Hyperthermia stimulates aberrant cross-talk and ephaptic transmission between adjacent motor nerves"},
            {"letter": "E", "is_correct": False, "text": "Thermal denaturation of myelin basic protein causing temporary structural dissolution of lamellae"}
        ],
        "correct_idx": 1,
        "explanation": "This patient is demonstrating Uhthoff phenomenon, where heat or physical exertion transiently worsens pre-existing demyelinating deficits. Along demyelinated nerve segments, voltage-gated sodium channels are dispersed, lowering the safety factor for action potential propagation. Modest temperature elevations (even 0.5 degrees C) accelerate the kinetics of sodium channel inactivation and shorten action potential duration, causing conduction block across demyelinated optic nerve segments that reverses upon cooling.",
        "high_yield_pearl": "High-Yield Rule: Uhthoff phenomenon is caused by heat-induced acceleration of voltage-gated sodium channel inactivation, dropping the safety factor below conduction threshold along previously demyelinated axons.",
        "image": None
    },
    {
        "id": "gh_u1_q16",
        "category": "Unit 01: Demyelinating Diseases",
        "stem": "A 30-year-old woman is evaluated for subacute gait unsteadiness and sensory loss. Lumbar puncture is performed. Which of the following cerebrospinal fluid findings would most strongly argue AGAINST a primary diagnosis of multiple sclerosis and point toward an active infectious process?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Presence of five distinct oligoclonal immunoglobulin G bands absent in matched serum"},
            {"letter": "B", "is_correct": False, "text": "Mild lymphocytic pleocytosis of 14 leukocytes per microliter with normal glucose"},
            {"letter": "C", "is_correct": True, "text": "Marked neutrophilic pleocytosis of 850 cells per microliter with a CSF to serum glucose ratio of 0.25"},
            {"letter": "D", "is_correct": False, "text": "Moderately elevated cerebrospinal fluid immunoglobulin G index of 0.85"},
            {"letter": "E", "is_correct": False, "text": "Total cerebrospinal fluid protein concentration of 55 milligrams per deciliter"}
        ],
        "correct_idx": 2,
        "explanation": "Multiple sclerosis typically demonstrates normal opening pressure, normal glucose (>60% of serum), mildly elevated protein (<100 mg/dL), mild lymphocytic pleocytosis (<50 cells/uL, usually <20), elevated IgG index (>0.7), and oligoclonal IgG bands on isoelectric focusing. A marked neutrophilic pleocytosis (>500-1000 cells/uL) with hypoglycorrhachia (CSF:serum glucose <0.4) is virtually never seen in MS and strongly indicates acute bacterial, fungal, or tuberculous meningitis.",
        "high_yield_pearl": "High-Yield Rule: In MS, CSF shows mild lymphocytic pleocytosis (<50/uL), normal glucose, and oligoclonal bands; marked neutrophilic pleocytosis or low glucose excludes typical MS and indicates infection.",
        "image": None
    },
    {
        "id": "gh_u1_q17",
        "category": "Unit 01: Demyelinating Diseases",
        "stem": "A 24-year-old man presents with progressive weakness in both legs, distal muscle wasting, and pes cavus. Electrodiagnostic testing reveals motor nerve conduction velocities of 52 m/s (normal >50 m/s), but compound muscle action potential (CMAP) amplitudes are severely reduced to 1.2 mV (normal >5.0 mV). Which fundamental histopathologic feature distinguishes this axonal hereditary neuropathy (CMT2) from the demyelinating form (CMT1)?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Concentric hypertrophy of Schwann cells forming prominent onion bulbs surrounding myelinated axons"},
            {"letter": "B", "is_correct": True, "text": "Wallerian-like degeneration and loss of large myelinated axons without prominent Schwann cell hyperplasia"},
            {"letter": "C", "is_correct": False, "text": "Segmental breakdown of myelin sheaths with marked sparing of underlying neurofilament integrity"},
            {"letter": "D", "is_correct": False, "text": "Perivascular CD8-positive lymphocytic infiltration into the endoneurium with microglial nodules"},
            {"letter": "E", "is_correct": False, "text": "Extracellular deposition of transthyretin amyloid fibrils within the epineurial connective tissue"}
        ],
        "correct_idx": 1,
        "explanation": "Charcot-Marie-Tooth disease is divided into demyelinating (CMT1) and axonal (CMT2) forms. CMT1 is characterized by severe slowing of conduction velocities (<38 m/s) and 'onion-bulb' Schwann cell hyperplasia secondary to repeated demyelination and remyelination. In contrast, CMT2 is a primary axonal neuropathy characterized by preserved or mildly reduced conduction velocities (>38-50 m/s), markedly reduced CMAP/SNAP amplitudes, and biopsy evidence of Wallerian-like axonal loss without Schwann cell proliferation.",
        "high_yield_pearl": "High-Yield Rule: CMT1 is demyelinating (slowed conduction <38 m/s, onion-bulb Schwann cell hyperplasia); CMT2 is axonal (normal conduction velocity >38 m/s, reduced action potential amplitudes, axonal loss).",
        "image": None
    },
    {
        "id": "gh_u1_q18",
        "category": "Unit 01: Demyelinating Diseases",
        "stem": "A 35-year-old woman with relapsing-remitting multiple sclerosis is initiated on fingolimod. Baseline electrocardiography is obtained prior to the first dose because of transient bradycardia risks. What is the cellular pharmacological mechanism by which fingolimod reduces clinical relapse rates in multiple sclerosis?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Inhibition of dihydroorotate dehydrogenase arresting activated lymphocyte proliferation in S-phase"},
            {"letter": "B", "is_correct": True, "text": "Internalization and degradation of sphingosine-1-phosphate receptors sequestering lymphocytes in lymph nodes"},
            {"letter": "C", "is_correct": False, "text": "Selective antibody-dependent cytotoxicity against CD20-expressing mature circulating B-cells"},
            {"letter": "D", "is_correct": False, "text": "Blockade of leukocyte alpha-4 integrins preventing vascular endothelial cell adhesion and migration"},
            {"letter": "E", "is_correct": False, "text": "Alkylating DNA guanine residues to cross-link strands and trigger mature T-cell apoptosis"}
        ],
        "correct_idx": 1,
        "explanation": "Fingolimod is an oral sphingosine-1-phosphate (S1P) receptor modulator. It is phosphorylated in vivo and binds to S1P receptors (S1PR1, 3, 4, 5) on lymphocytes, causing receptor internalization and degradation. Without functional surface S1P1 receptors, lymphocytes cannot sense the S1P gradient between lymph nodes (low S1P) and plasma (high S1P) and are trapped within secondary lymphoid organs, preventing auto-reactive T and B cells from circulating into the central nervous system.",
        "high_yield_pearl": "High-Yield Rule: Fingolimod binds and internalizes S1P receptors on lymphocytes, sequestering auto-reactive T and B cells inside lymph nodes and preventing their entry into the central nervous system.",
        "image": None
    },
    {
        "id": "gh_u1_q19",
        "category": "Unit 01: Demyelinating Diseases",
        "stem": "A student compares a patient who achieves full motor recovery after severe Guillain-Barre syndrome to a patient who remains paraplegic after spinal cord multiple sclerosis. Which physiological difference between central and peripheral nervous system environments primarily explains why central remyelination fails following injury?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Central oligodendrocytes completely lack the metabolic machinery to synthesize galactocerebroside"},
            {"letter": "B", "is_correct": True, "text": "CNS myelin debris and astrocytic glial scars express potent inhibitors of axonal outgrowth and remyelination"},
            {"letter": "C", "is_correct": False, "text": "Schwann cells are permanently immune-privileged and cannot be recognized by circulating cytotoxic T-cells"},
            {"letter": "D", "is_correct": False, "text": "The blood-brain barrier permanently excludes glucose and ATP from injured central axon cylinders"},
            {"letter": "E", "is_correct": False, "text": "Peripheral axons are entirely unmyelinated and do not require neuroglial sheath replacement after trauma"}
        ],
        "correct_idx": 1,
        "explanation": "In the PNS, Schwann cells readily proliferate, express neurotrophic factors, produce a basement membrane rich in laminin, and macrophages rapidly clear myelin debris, permitting vigorous remyelination. In the CNS, remyelination is severely impeded because central myelin debris contains potent neurite outgrowth inhibitors (Nogo-A, MAG, OMgp), microglial clearance is slow, and reactive astrocytes form a dense chondroitin sulfate proteoglycan-rich glial scar that physically blocks oligodendrocyte precursor migration and remyelination.",
        "high_yield_pearl": "High-Yield Rule: Central remyelination is poor compared to the PNS because CNS myelin debris contains inhibitory molecules (Nogo-A), microglial clearance is slow, and reactive astrocytes form a physical glial scar.",
        "image": None
    },
    {
        "id": "gh_u1_q20",
        "category": "Unit 01: Demyelinating Diseases",
        "stem": "A 33-year-old woman presents with progressive left hemiparesis and mild headache over 2 weeks. Brain MRI reveals a solitary 4-cm subcortical white matter lesion with surrounding vasogenic edema. Contrast administration demonstrates an incomplete, open 'horseshoe-shaped' ring of enhancement whose open border faces the cerebral cortex. Stereotactic biopsy of the lesion is most likely to reveal which histopathologic finding?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Florid pseudopalisading necrosis surrounded by glomeruloid microvascular endothelial proliferation"},
            {"letter": "B", "is_correct": True, "text": "Sheets of lipid-laden foamy macrophages with marked loss of myelin but relative preservation of axons"},
            {"letter": "C", "is_correct": False, "text": "Biphasic architecture showing Rosenthal fibers and eosinophilic granular bodies in hair-like astrocytes"},
            {"letter": "D", "is_correct": False, "text": "Abundant intracellular tachyzoites with central coagulative necrosis and ring-like fibrous encasement"},
            {"letter": "E", "is_correct": False, "text": "Perivascular pseudorosettes with ependymal blepharoplasts protruding into the ventricular system"}
        ],
        "correct_idx": 1,
        "explanation": "This patient has tumefactive multiple sclerosis, a solitary demyelinating plaque >2 cm that can clinically and radiologically mimic a high-grade neoplasm (glioblastoma) or cerebral abscess. A key diagnostic radiologic sign is an 'open-ring' or 'horseshoe' enhancement, where the non-enhancing open arc points toward the cortical gray matter. Biopsy confirms demyelination: abundant myelin-clearing foamy macrophages (foamy histiocytes), reactive gliosis (Creutzfeldt-Peters cells), and critical relative preservation of underlying neurofilament axons (unlike GBM, which destroys both axons and myelin).",
        "high_yield_pearl": "High-Yield Rule: Tumefactive MS presents as a large tumor-like mass with characteristic open-ring (horseshoe) enhancement facing the cortex; biopsy shows abundant lipid-laden foamy macrophages with preserved axonal architecture.",
        "image": None
    }
]

if __name__ == '__main__':
    from test_gen_structure import check_q
    for q in U1_QUESTIONS:
        check_q(q)
    print(f"gen_g_h_u1.py: All {len(U1_QUESTIONS)} questions passed validation!")
