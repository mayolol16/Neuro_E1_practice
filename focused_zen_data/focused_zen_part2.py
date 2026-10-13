# focused_zen_part2.py
# 80 Board-Style USMLE Step 1 Questions directly aligned with
# "Copy of Long NeuroPsych Exam 1 Study Guide.docx"
# Topics 5-8 (20 Questions each, IDs FZ_Q081 to FZ_Q160)

focused_questions_part2 = [
    # =========================================================================
    # TOPIC 5: Acetylcholine / Neuromuscular Junction Disorder (FZ_Q081 - FZ_Q100)
    # =========================================================================
    {
        "id": "FZ_Q081",
        "question_number": 81,
        "category": "Acetylcholine / Neuromuscular Junction Disorder",
        "stem": "A 32-year-old woman presents to the clinic with fluctuating drooping of her left upper eyelid and horizontal diplopia that worsens toward the end of the day or after prolonged reading. She notes that taking a cold shower or placing an ice pack over her closed eyes for two minutes noticeably improves her ptosis. Repetitive low-frequency nerve stimulation of the facial nerve reveals a progressive decremental decline in compound muscle action potential (CMAP) amplitude. Autoantibodies in this patient are most commonly directed against which of the following proteins?",
        "options": [
            {"text": "Presynaptic P/Q-type voltage-gated calcium channels", "is_correct": False},
            {"text": "Postsynaptic nicotinic acetylcholine receptors (nAChR)", "is_correct": True},
            {"text": "Ryanodine receptors in the sarcoplasmic reticulum", "is_correct": False},
            {"text": "Voltage-gated sodium channels in the sarcolemma", "is_correct": False},
            {"text": "Synaptobrevin (VAMP-2) on synaptic vesicles", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. Postsynaptic nicotinic acetylcholine receptors (nAChR).\n\nThis patient has Myasthenia Gravis (MG), an autoimmune disorder caused by autoantibodies directed against postsynaptic nicotinic acetylcholine receptors (anti-AChR) on the motor endplate (or against muscle-specific kinase / MuSK in ~5-10% of cases). Clinical hallmarks:\n• Fluctuating, fatiguable weakness that worsens with repetitive muscle use throughout the day.\n• Ocular symptoms (ptosis, diplopia) are the initial manifestation in >50% of patients.\n• Positive ice pack test: Lower temperature decreases acetylcholinesterase enzymatic activity, increasing ACh availability in the synaptic cleft and temporarily reversing ptosis.\n• Repetitive nerve stimulation (RNS) demonstrates a diagnostic decremental response in CMAP amplitude due to progressive failure of endplate potentials to reach threshold.\n\n• Option A is incorrect: Lambert-Eaton myasthenic syndrome involves autoantibodies against presynaptic P/Q-type VGCCs."
    },
    {
        "id": "FZ_Q082",
        "question_number": 82,
        "category": "Acetylcholine / Neuromuscular Junction Disorder",
        "stem": "A 34-year-old woman with generalized myasthenia gravis is evaluated prior to starting maintenance therapy. A chest CT scan reveals a well-circumscribed, homogeneous anterior mediastinal mass measuring 4.5 cm. In addition to medical management with acetylcholinesterase inhibitors, thymectomy is recommended. Which of the following pathological abnormalities of the thymus gland is most frequently found in patients with acetylcholine receptor antibody-positive myasthenia gravis?",
        "options": [
            {"text": "Thymic follicular lymphoid hyperplasia", "is_correct": True},
            {"text": "Malignant thymoma", "is_correct": False},
            {"text": "Thymic aplasia", "is_correct": False},
            {"text": "Thymic lipoma", "is_correct": False},
            {"text": "Thymic atrophy and involution", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Thymic follicular lymphoid hyperplasia.\n\nThe thymus plays an essential role in the immunopathogenesis of myasthenia gravis (MG). In AChR-antibody positive MG:\n• Approximately 65% to 75% of patients have thymic follicular lymphoid hyperplasia (active germinal centers containing B and T cells that drive autoantibody production).\n• Approximately 10% to 15% of patients have a thymoma (neoplastic proliferation of thymic epithelial cells).\nThymectomy removes the source of autosensitization and is recommended in all patients with thymoma, as well as in non-thymomatous generalized AChR-positive MG to induce long-term clinical remission.\n\n• Option B is incorrect: Thymomas occur in 10-15% of MG patients, whereas thymic hyperplasia is much more common (65-75%).\n• Option C is incorrect: Thymic aplasia is seen in DiGeorge syndrome."
    },
    {
        "id": "FZ_Q083",
        "question_number": 83,
        "category": "Acetylcholine / Neuromuscular Junction Disorder",
        "stem": "A 64-year-old man with a 40 pack-year smoking history presents with progressive proximal leg weakness. He reports extreme difficulty standing from a seated chair in the morning; however, after walking around for 15 minutes, his strength noticeably improves. He also complains of a dry mouth and erectile dysfunction. On physical examination, his patellar and Achilles deep tendon reflexes are 0/4 bilaterally, but reflex amplitude increases significantly immediately after 10 seconds of maximal isometric quadriceps contraction. Which of the following is the most likely underlying malignancy associated with this syndrome?",
        "options": [
            {"text": "Thymoma", "is_correct": False},
            {"text": "Small cell lung carcinoma (SCLC)", "is_correct": True},
            {"text": "Renal cell carcinoma", "is_correct": False},
            {"text": "Colorectal adenocarcinoma", "is_correct": False},
            {"text": "Squamous cell carcinoma of the larynx", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. Small cell lung carcinoma (SCLC).\n\nThis patient presents with Lambert-Eaton Myasthenic Syndrome (LEMS), a paraneoplastic autoimmune channelopathy caused by antibodies against presynaptic P/Q-type voltage-gated calcium channels (VGCC). Key characteristics:\n• Proximal lower extremity weakness that paradoxically IMPROVES with repeated muscle contraction or exercise (post-exercise facilitation, caused by accumulation of intracellular calcium in presynaptic boutons during rapid firing, facilitating ACh vesicle release).\n• Autonomic dysfunction: Dry mouth (xerostomia), erectile dysfunction, constipation, hypohidrosis.\n• Hyporeflexia or areflexia that transiently normalizes after exercise.\n• Over 50% to 60% of cases occur as a paraneoplastic manifestation of Small Cell Lung Carcinoma (SCLC, a high-grade neuroendocrine tumor expressing surface voltage-gated calcium channels).\n\n• Option A is incorrect: Thymoma is associated with Myasthenia Gravis."
    },
    {
        "id": "FZ_Q084",
        "question_number": 84,
        "category": "Acetylcholine / Neuromuscular Junction Disorder",
        "stem": "A 5-month-old infant is brought to the emergency department because of weak crying, poor suckling, and severe constipation over the past 48 hours. Physical examination reveals an afebrile, alert infant who appears markedly hypotonic ('floppy baby') with ptosis, sluggish pupillary light reflexes, weak head control, and generalized hyporeflexia. The mother mentions that she began sweetening the baby's formula with raw organic honey last week. By which of the following molecular mechanisms does the offending neurotoxin cause this flaccid paralysis?",
        "options": [
            {"text": "Cleavage of presynaptic SNARE proteins (SNAP-25 or synaptobrevin), blocking acetylcholine exocytosis", "is_correct": True},
            {"text": "Competitive antagonism of postsynaptic nicotinic receptors", "is_correct": False},
            {"text": "Irreversible inhibition of acetylcholinesterase, leading to receptor desensitization", "is_correct": False},
            {"text": "Cleavage of synaptobrevin in inhibitory Renshaw cells, preventing glycine release", "is_correct": False},
            {"text": "Antibody-mediated blockade of presynaptic P/Q-type calcium channels", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Cleavage of presynaptic SNARE proteins (SNAP-25 or synaptobrevin), blocking acetylcholine exocytosis.\n\nThis infant has infant botulism ('floppy baby syndrome'), caused by the ingestion of Clostridium botulinum spores (commonly from raw honey or environmental dust). Unlike adult botulism (which results from ingesting preformed toxin in canned food), infants ingest spores that germinate, colonize the immature gut, and produce botulinum neurotoxin in vivo. The toxin is a zinc-dependent metalloprotease that is endocytosed into presynaptic cholinergic terminals and cleaves SNARE complex proteins (SNAP-25 or synaptobrevin/VAMP), completely blocking exocytosis of acetylcholine into the neuromuscular junction and autonomic synapses. This causes descending flaccid paralysis, cranial nerve deficits (ptosis, sluggish pupils), constipation, and poor feeding.\n\n• Option D is incorrect: Tetanus toxin cleaves synaptobrevin in spinal cord inhibitory Renshaw interneurons, causing spastic paralysis."
    },
    {
        "id": "FZ_Q085",
        "question_number": 85,
        "category": "Acetylcholine / Neuromuscular Junction Disorder",
        "stem": "A 45-year-old farm worker is brought to the emergency department after accidentally spilling a concentrated organophosphate insecticide across his bare chest and arms. On examination, he is diaphoretic, confused, and salivating heavily. His pupils are pinpoint (1 mm bilaterally), his heart rate is 38 beats/min, his blood pressure is 88/50 mmHg, and lung auscultation reveals diffuse wheezing with copious rhonchi. Furthermore, he exhibits widespread muscle fasciculations and progressive diaphragm weakness. Which of the following two medications should be administered immediately to treat both his muscarinic and nicotinic toxicity?",
        "options": [
            {"text": "Atropine and Pralidoxime (2-PAM)", "is_correct": True},
            {"text": "Physostigmine and Neostigmine", "is_correct": False},
            {"text": "Edrophonium and Pyridostigmine", "is_correct": False},
            {"text": "Scopolamine and Flumazenil", "is_correct": False},
            {"text": "Dantrolene and Naloxone", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Atropine and Pralidoxime (2-PAM).\n\nOrganophosphates irreversibly inhibit acetylcholinesterase by phosphorylating the esteratic serine residue at its active site, causing toxic accumulation of acetylcholine at both muscarinic and nicotinic synapses:\n• Muscarinic hyperstimulation (DUMBBELLS: Diarrhea, Urination, Miosis, Bronchospasm/bronchorrhea, Bradycardia, Emesis, Lacrimation, Salivation).\n• Nicotinic hyperstimulation: Muscle fasciculations, cramping, followed by depolarizing paralysis and diaphragmatic failure.\nTreatment requires two drugs:\n1. Atropine: A competitive antimuscarinic that crosses the blood-brain barrier and reverses central and peripheral muscarinic symptoms (specifically reversing bradycardia and life-threatening bronchorrhea). It has NO effect on nicotinic receptors.\n2. Pralidoxime (2-PAM): A cholinesterase reactivator that cleaves the organophosphate bond from the enzyme active site, regenerating functional acetylcholinesterase at BOTH muscarinic and nicotinic neuromuscular junctions. Must be given before 'aging' (irreversible dealkylation of the organophosphate-enzyme complex) occurs."
    },
    {
        "id": "FZ_Q086",
        "question_number": 86,
        "category": "Acetylcholine / Neuromuscular Junction Disorder",
        "stem": "A 40-year-old woman with a history of myasthenia gravis is taking high-dose oral pyridostigmine. Over the past 2 days, she increased her dose because of persistent weakness. She presents to the emergency department in acute respiratory distress with extreme muscle weakness, diaphoresis, severe abdominal cramping, loose diarrhea, pinpoint pupils, and diffuse muscle fasciculations. The physician must distinguish between a myasthenic crisis and a cholinergic crisis. Which of the following mechanisms explains why excessive pyridostigmine causes profound skeletal muscle paralysis in a cholinergic crisis?",
        "options": [
            {"text": "Persistent accumulation of acetylcholine produces continuous depolarization of the motor endplate, rendering voltage-gated sodium channels inexcitable (depolarizing block)", "is_correct": True},
            {"text": "Direct competitive blockade of nicotinic acetylcholine receptors by pyridostigmine metabolites", "is_correct": False},
            {"text": "Depletion of presynaptic choline acetyltransferase preventing acetylcholine synthesis", "is_correct": False},
            {"text": "Immune-mediated complement activation destroying the sarcoplasmic reticulum", "is_correct": False},
            {"text": "Precipitation of malignant hyperthermia via ryanodine receptor overactivation", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Persistent accumulation of acetylcholine produces continuous depolarization of the motor endplate, rendering voltage-gated sodium channels inexcitable (depolarizing block).\n\nA cholinergic crisis occurs from excessive acetylcholinesterase inhibitor (pyridostigmine) administration. When AChE is excessively inhibited, acetylcholine cannot be hydrolyzed and accumulates in the synaptic cleft. Continuous binding of excess ACh keeps nicotinic receptor channels open, causing persistent depolarization of the motor endplate. This continuous depolarization locks adjacent perijunctional voltage-gated Na+ channels into their slow inactivated state (h-gates closed). Because Na+ channels cannot reset, no further muscle action potentials can be generated, resulting in profound flaccid paralysis (depolarizing neuromuscular block) accompanied by classic muscarinic hyperactivity (diarrhea, miosis, salivation, fasciculations).\n\n• Administration of edrophonium (Tensilon) worsens a cholinergic crisis, but transiently improves a myasthenic crisis."
    },
    {
        "id": "FZ_Q087",
        "question_number": 87,
        "category": "Acetylcholine / Neuromuscular Junction Disorder",
        "stem": "In the physiological activation of skeletal muscle at the neuromuscular junction, acetylcholine binding to post-junctional nicotinic acetylcholine receptors (nAChR) triggers opening of an integral ion channel. Which of the following structural and electrophysiological characteristics best describes the adult skeletal muscle nicotinic acetylcholine receptor?",
        "options": [
            {"text": "Pentameric ligand-gated non-selective cation channel permeable to Na+ and K+", "is_correct": True},
            {"text": "Seven-transmembrane GPCR coupled to Gq and phospholipase C", "is_correct": False},
            {"text": "Voltage-gated chloride channel blocked by tetrodotoxin", "is_correct": False},
            {"text": "Ionotropic receptor selectively permeable exclusively to calcium ions", "is_correct": False},
            {"text": "Monomeric receptor with intrinsic tyrosine kinase catalytic activity", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Pentameric ligand-gated non-selective cation channel permeable to Na+ and K+.\n\nThe adult skeletal muscle nicotinic acetylcholine receptor (nAChR) is a pentameric ligand-gated ion channel composed of five glycoprotein subunits: two alpha-1, one beta-1, one delta, and one epsilon (2α:1β:1δ:1ε). Simultaneous binding of two acetylcholine molecules to the extracellular alpha subunits induces a conformational change that opens the central channel pore. The open pore is a non-selective cation channel permeable to both Na+ and K+. Because the electrochemical driving force for Na+ influx is much greater than that for K+ efflux at resting membrane potential (-90 mV), net Na+ influx predominates, generating the depolarizing endplate potential (EPP).\n\n• Option B is incorrect: Muscarinic M1, M3, and M5 receptors are Gq-coupled GPCRs."
    },
    {
        "id": "FZ_Q088",
        "question_number": 88,
        "category": "Acetylcholine / Neuromuscular Junction Disorder",
        "stem": "A 28-year-old woman is treated for myasthenia gravis with oral pyridostigmine. While her muscle strength improves substantially, she complains of intolerable abdominal cramping, frequent loose bowel movements, and excessive salivation. The physician prescribes a medication to selectively block these muscarinic side effects without impairing the therapeutic action of pyridostigmine on skeletal muscle nicotinic receptors. Which of the following drugs is most appropriate?",
        "options": [
            {"text": "Glycopyrrolate", "is_correct": True},
            {"text": "Physostigmine", "is_correct": False},
            {"text": "Succinylcholine", "is_correct": False},
            {"text": "Pilocarpine", "is_correct": False},
            {"text": "Edrophonium", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Glycopyrrolate.\n\nPyridostigmine is an acetylcholinesterase inhibitor that increases ACh at both nicotinic receptors (therapeutic target in skeletal muscle) and muscarinic receptors (causing adverse GI hypermotility, cramps, diarrhea, and salivation). To control these muscarinic side effects, an antimuscarinic agent such as glycopyrrolate, propantheline, or hyoscyamine is prescribed. Glycopyrrolate is a quaternary antimuscarinic that selectively blocks peripheral muscarinic receptors (M1-M5), relieving cramps and secretions without crossing the blood-brain barrier and without blocking skeletal muscle nicotinic receptors.\n\n• Option B is incorrect: Physostigmine is an AChE inhibitor that would worsen symptoms.\n• Option C is incorrect: Succinylcholine is a depolarizing neuromuscular blocker.\n• Option D is incorrect: Pilocarpine is a muscarinic agonist."
    },
    {
        "id": "FZ_Q089",
        "question_number": 89,
        "category": "Acetylcholine / Neuromuscular Junction Disorder",
        "stem": "A clinical neurophysiologist performs repetitive nerve stimulation (RNS) testing at 3 Hz on a patient with severe fatiguable limb weakness. In a normal individual, compound muscle action potential (CMAP) amplitudes remain constant with repetitive stimulation. In this patient, however, the CMAP amplitude exhibits a progressive decremental decline exceeding 10% from the first to the fourth stimulus. Which of the following pathophysiological mechanisms accounts for this decremental response in myasthenia gravis?",
        "options": [
            {"text": "Normal presynaptic depletion of immediately releasable acetylcholine vesicles fails to evoke endplate potentials that reach threshold across autoantibody-depleted postsynaptic receptors", "is_correct": True},
            {"text": "Progressive accumulation of extracellular potassium inactivates all sarcolemmal sodium channels", "is_correct": False},
            {"text": "Rapid exhaustion of intracellular ATP prevents actin-myosin cross-bridge cycling", "is_correct": False},
            {"text": "Autoantibodies physically block the propagation of action potentials down T-tubules", "is_correct": False},
            {"text": "Immediate upregulation of acetylcholinesterase enzyme clears acetylcholine before it can bind", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Normal presynaptic depletion of immediately releasable acetylcholine vesicles fails to evoke endplate potentials that reach threshold across autoantibody-depleted postsynaptic receptors.\n\nWith repetitive nerve stimulation at low frequency (2-3 Hz), every normal neuromuscular junction experiences a physiological rundown in the number of ACh quanta released per action potential (due to temporary depletion of the readily releasable vesicle pool). In a healthy individual, the high 'safety factor' of transmission ensures that the endplate potential (EPP) still far exceeds the threshold to trigger a muscle action potential. In myasthenia gravis, autoantibodies have destroyed or blocked >70% of postsynaptic nAChRs, drastically lowering the safety factor. As presynaptic ACh release naturally declines with successive stimuli, EPPs drop below threshold in an increasing proportion of muscle fibers, producing a progressive drop in total CMAP amplitude (decremental response).\n\n• Options B, C, and D do not represent the mechanism of CMAP decrement in MG."
    },
    {
        "id": "FZ_Q090",
        "question_number": 90,
        "category": "Acetylcholine / Neuromuscular Junction Disorder",
        "stem": "A 58-year-old man undergoes electrodiagnostic testing for progressive proximal weakness. High-frequency repetitive nerve stimulation (RNS) at 50 Hz, or brief voluntary isometric contraction for 10 seconds, produces a dramatic >100% incremental increase in compound muscle action potential (CMAP) amplitude (facilitation). Which of the following underlying molecular mechanisms explains this post-exercise facilitation in Lambert-Eaton myasthenic syndrome?",
        "options": [
            {"text": "Rapid accumulation of intracellular calcium in the presynaptic terminal overcomes impaired calcium channel influx, enhancing acetylcholine vesicle exocytosis", "is_correct": True},
            {"text": "Rapid upregulation of postsynaptic nicotinic acetylcholine receptor expression", "is_correct": False},
            {"text": "Complete enzymatic inhibition of acetylcholinesterase by intracellular calcium", "is_correct": False},
            {"text": "Depletion of glycine inhibitory transmission in spinal cord anterior horns", "is_correct": False},
            {"text": "Hyperpolarization of muscle fiber membranes via increased potassium conductance", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Rapid accumulation of intracellular calcium in the presynaptic terminal overcomes impaired calcium channel influx, enhancing acetylcholine vesicle exocytosis.\n\nIn Lambert-Eaton Myasthenic Syndrome (LEMS), autoantibodies block presynaptic P/Q-type voltage-gated Ca2+ channels, severely reducing single-action-potential Ca2+ influx and basal ACh release, leading to very low baseline CMAP amplitudes. During high-frequency repetitive nerve stimulation (20-50 Hz) or maximal voluntary isometric contraction, Ca2+ enters the nerve terminal faster than it can be sequestered or extruded by calcium pumps. This build-up of residual intracellular Ca2+ increases the probability of vesicle fusion, causing a massive surge in ACh release that successfully brings endplate potentials above threshold across all muscle fibers, producing a diagnostic incremental response (>100% facilitation)."
    },
    {
        "id": "FZ_Q091",
        "question_number": 91,
        "category": "Acetylcholine / Neuromuscular Junction Disorder",
        "stem": "A 2-year-old boy presents to the emergency department after ingesting several berries from an ornamental shrub identified as Atropa belladonna (deadly nightshade), a potent antimuscarinic containing atropine and scopolamine. On examination, he is agitated, delirious, flushed, febrile, his skin is dry, and his pupils are widely dilated. The emergency physician prepares to administer an antidote. Which of the following acetylcholinesterase inhibitors is a tertiary amine capable of crossing the blood-brain barrier to reverse both central and peripheral antimuscarinic toxicity?",
        "options": [
            {"text": "Physostigmine", "is_correct": True},
            {"text": "Neostigmine", "is_correct": False},
            {"text": "Pyridostigmine", "is_correct": False},
            {"text": "Edrophonium", "is_correct": False},
            {"text": "Echothiophate", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Physostigmine.\n\nPhysostigmine is a naturally occurring plant alkaloid that acts as a reversible acetylcholinesterase inhibitor. Chemically, physostigmine is a non-polar, lipid-soluble tertiary amine. Because it has no permanent positive charge, it readily crosses the blood-brain barrier into the central nervous system. It is the specific antidote for severe anticholinergic / antimuscarinic toxicity ('blind as a bat, mad as a hatter, red as a beet, hot as a hare, dry as a bone') caused by atropine, scopolamine, or jimsonweed, reversing both central delirium and peripheral autonomic blockade.\n\n• Options B, C, and D are incorrect: Neostigmine, pyridostigmine, and edrophonium are quaternary ammonium compounds with permanent positive charges. They are hydrophilic, cannot cross the blood-brain barrier, and treat only peripheral symptoms."
    },
    {
        "id": "FZ_Q092",
        "question_number": 92,
        "category": "Acetylcholine / Neuromuscular Junction Disorder",
        "stem": "An experimental neurotoxin isolated from the venom of a marine cone snail (omega-conotoxin) is applied to an in vitro neuromuscular junction preparation. Recording electrodes demonstrate that somatic motor nerve action potentials propagate normally to the nerve terminal, but calcium influx into the terminal is completely abolished, and no endplate potentials are generated. Which of the following voltage-gated calcium channels is selectively targeted by this toxin at mammalian synapses?",
        "options": [
            {"text": "N-type and P/Q-type voltage-gated calcium channels", "is_correct": True},
            {"text": "L-type voltage-gated calcium channels (dihydropyridine receptors)", "is_correct": False},
            {"text": "T-type low-voltage-activated calcium channels", "is_correct": False},
            {"text": "Ryanodine receptor channels", "is_correct": False},
            {"text": "IP3-gated calcium channels", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. N-type and P/Q-type voltage-gated calcium channels.\n\nPresynaptic neurotransmitter release at fast chemical synapses (including the neuromuscular junction and central synapses) is mediated primarily by high-voltage-activated N-type (Cav2.2) and P/Q-type (Cav2.1) voltage-gated calcium channels. These channels are clustered at active zones immediately adjacent to docked synaptic vesicles. Conotoxins (from cone snails) and agatoxins (from funnel-web spiders) selectively block these channels, preventing Ca2+ influx and exocytosis.\n\n• Option B is incorrect: L-type calcium channels (Cav1) are found in cardiac/smooth muscle and skeletal muscle T-tubules (dihydropyridine receptors).\n• Option C is incorrect: T-type calcium channels (Cav3) mediate rhythmic burst firing in thalamic relay neurons."
    },
    {
        "id": "FZ_Q093",
        "question_number": 93,
        "category": "Acetylcholine / Neuromuscular Junction Disorder",
        "stem": "A 46-year-old man presents with progressive weakness and muscle fatigue. A diagnosis of myasthenia gravis is confirmed by positive anti-AChR antibody titers. He is prescribed pyridostigmine. By which of the following molecular mechanisms does pyridostigmine increase synaptic transmission at the neuromuscular junction?",
        "options": [
            {"text": "Reversible carbamylation of the active site of acetylcholinesterase, slowing acetylcholine hydrolysis", "is_correct": True},
            {"text": "Irreversible phosphorylation of the esteratic site of acetylcholinesterase", "is_correct": False},
            {"text": "Direct agonist activation of nicotinic and muscarinic receptors", "is_correct": False},
            {"text": "Stimulation of presynaptic choline acetyltransferase (ChAT)", "is_correct": False},
            {"text": "Blockade of presynaptic high-affinity choline uptake transporters", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Reversible carbamylation of the active site of acetylcholinesterase, slowing acetylcholine hydrolysis.\n\nPyridostigmine, neostigmine, and physostigmine are carbamate acetylcholinesterase inhibitors. They serve as alternative substrates for acetylcholinesterase: the enzyme cleaves the drug and transfers a carbamoyl group to the active-site serine. This carbamylated enzyme is hydrolyzed very slowly (taking minutes to hours, compared to microseconds for acetylated enzyme formed during ACh hydrolysis). By temporarily occupying and inhibiting acetylcholinesterase, pyridostigmine prolongs the lifetime of endogenous acetylcholine in the synaptic cleft, increasing the likelihood that ACh will bind the remaining postsynaptic receptors to generate a threshold endplate potential.\n\n• Option B is incorrect: Irreversible phosphorylation is the mechanism of toxic organophosphates."
    },
    {
        "id": "FZ_Q094",
        "question_number": 94,
        "category": "Acetylcholine / Neuromuscular Junction Disorder",
        "stem": "A 37-year-old woman presents to the clinic with diplopia and bilateral ptosis. A clinical test using edrophonium (Tensilon) is considered. Historically, the Tensilon test was used to support a diagnosis of myasthenia gravis because edrophonium has a rapid onset (<1 minute) and a very short duration of action (~5-10 minutes). What molecular characteristic accounts for edrophonium's short duration of action compared to pyridostigmine?",
        "options": [
            {"text": "It binds non-covalently and reversibly via electrostatic hydrogen bonds to the anionic site of acetylcholinesterase without forming a covalent intermediate", "is_correct": True},
            {"text": "It irreversibly phosphorylates the active site followed by rapid enzymatic reactivation", "is_correct": False},
            {"text": "It is destroyed by plasma pseudocholinesterases within seconds", "is_correct": False},
            {"text": "It undergoes instantaneous Hofmann elimination in the serum", "is_correct": False},
            {"text": "It is rapidly sequestered into adipose tissue via high lipid solubility", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. It binds non-covalently and reversibly via electrostatic hydrogen bonds to the anionic site of acetylcholinesterase without forming a covalent intermediate.\n\nEdrophonium is a synthetic quaternary ammonium compound that acts as a simple competitive, non-covalent inhibitor of acetylcholinesterase. Unlike carbamates (pyridostigmine, neostigmine) which transfer a carbamoyl group and form a covalent intermediate that takes hours to hydrolyze, edrophonium binds reversibly through ionic and hydrogen bonding at the catalytic site. As free drug is cleared, it readily dissociates from the enzyme, giving it a rapid onset (30-60 seconds) and a brief duration of action (5-10 minutes).\n\n• Option D is incorrect: Hofmann elimination is the spontaneous non-enzymatic degradation of cisatracurium and atracurium."
    },
    {
        "id": "FZ_Q095",
        "question_number": 95,
        "category": "Acetylcholine / Neuromuscular Junction Disorder",
        "stem": "A 52-year-old man who consumed home-canned asparagus 24 hours ago presents with acute blurred vision, bilateral ptosis, fixed dilated pupils, dry mouth, difficulty swallowing, and bilateral symmetrical descending motor weakness. Sensation is intact and he is afebrile. His condition is diagnosed as foodborne botulism. Which of the following is the most important immediate therapeutic intervention to prevent disease progression?",
        "options": [
            {"text": "Administration of equine-derived botulinum antitoxin", "is_correct": True},
            {"text": "High-dose intravenous pyridostigmine", "is_correct": False},
            {"text": "Urgent plasma exchange with intravenous immunoglobulin", "is_correct": False},
            {"text": "Administration of pralidoxime (2-PAM)", "is_correct": False},
            {"text": "Intravenous edrophonium", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Administration of equine-derived botulinum antitoxin.\n\nIn foodborne botulism, the definitive treatment is early administration of botulinum antitoxin (equine heptavalent antitoxin for adults; Botulism Immune Globulin Intravenous / BabyBIG for infants). The antitoxin neutralizes free circulating neurotoxin in the bloodstream, preventing further uptake into nerve terminals. It does NOT reverse paralysis in nerve terminals where toxin has already cleaved SNARE proteins; recovery at those synapses requires slow regeneration of new motor nerve terminals (sprouting). Supportive mechanical ventilation is essential.\n\n• Option B is incorrect: Pyridostigmine has minimal efficacy because presynaptic ACh release is blocked.\n• Option D is incorrect: Pralidoxime treats organophosphate poisoning, not botulism."
    },
    {
        "id": "FZ_Q096",
        "question_number": 96,
        "category": "Acetylcholine / Neuromuscular Junction Disorder",
        "stem": "In the presynaptic synthesis of acetylcholine within somatic motor neurons, choline acetyltransferase (ChAT) synthesizes acetylcholine from which of the following two precursors?",
        "options": [
            {"text": "Choline and Acetyl-CoA", "is_correct": True},
            {"text": "Ethanolamine and Succinyl-CoA", "is_correct": False},
            {"text": "Serine and Pyruvate", "is_correct": False},
            {"text": "Carnitine and Acetoacetyl-CoA", "is_correct": False},
            {"text": "Glycine and Malonyl-CoA", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Choline and Acetyl-CoA.\n\nAcetylcholine is synthesized in the presynaptic cytoplasm by the enzyme Choline Acetyltransferase (ChAT). ChAT catalyzes the transfer of an acetyl group from mitochondrial Acetyl-CoA (derived from glucose/pyruvate metabolism) to free Choline (taken up from the extracellular fluid via high-affinity Na+-dependent choline transporters, ChT). Newly synthesized acetylcholine is then pumped into synaptic vesicles by the vesicular acetylcholine transporter (VAChT) in exchange for protons (H+)."
    },
    {
        "id": "FZ_Q097",
        "question_number": 97,
        "category": "Acetylcholine / Neuromuscular Junction Disorder",
        "stem": "During physiological excitation-contraction coupling in skeletal muscle, the muscle action potential travels deep into the fiber along transverse tubules (T-tubules). Depolarization activates a voltage-sensitive dihydropyridine receptor (DHPR), which mechanically triggers the opening of which of the following channels on the terminal cisternae of the sarcoplasmic reticulum to release calcium into the myoplasm?",
        "options": [
            {"text": "Ryanodine receptor type 1 (RyR1)", "is_correct": True},
            {"text": "SERCA calcium ATPase", "is_correct": False},
            {"text": "Calsequestrin channel", "is_correct": False},
            {"text": "Inositol 1,4,5-trisphosphate (IP3) receptor", "is_correct": False},
            {"text": "Sodium-calcium exchanger (NCX)", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Ryanodine receptor type 1 (RyR1).\n\nIn skeletal muscle excitation-contraction coupling:\n1. Action potential travels down the sarcolemma and invaginates along T-tubules.\n2. Depolarization activates the L-type voltage-gated Ca2+ channel / Dihydropyridine receptor (DHPR).\n3. In skeletal muscle, DHPR is mechanically coupled directly to the Ryanodine receptor type 1 (RyR1) on the sarcoplasmic reticulum (SR) terminal cisternae.\n4. Conformational change in DHPR pulls RyR1 open, releasing massive stored Ca2+ from the SR into the myoplasm.\n5. Ca2+ binds Troponin C, moving tropomyosin off actin active sites and allowing myosin cross-bridge cycling.\n\n• Option B is incorrect: SERCA pumps Ca2+ back into the SR during muscle relaxation."
    },
    {
        "id": "FZ_Q098",
        "question_number": 98,
        "category": "Acetylcholine / Neuromuscular Junction Disorder",
        "stem": "A 40-year-old woman with ocular myasthenia gravis tests negative for antibodies against the nicotinic acetylcholine receptor (anti-AChR seronegative). Testing for which of the following autoantibodies is most likely to be positive, identifying a distinct clinical subtype of myasthenia gravis characterized by prominent facial, bulbar, and respiratory muscle involvement?",
        "options": [
            {"text": "Muscle-specific kinase (MuSK) autoantibodies", "is_correct": True},
            {"text": "Voltage-gated potassium channel (VGKC) antibodies", "is_correct": False},
            {"text": "Aquaporin-4 (AQP4) autoantibodies", "is_correct": False},
            {"text": "Glutamic acid decarboxylase (GAD) autoantibodies", "is_correct": False},
            {"text": "Anti-Jo-1 autoantibodies", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Muscle-specific kinase (MuSK) autoantibodies.\n\nApproximately 40% to 70% of patients with generalized myasthenia gravis who test negative for standard anti-AChR antibodies are seropositive for antibodies against Muscle-Specific Kinase (MuSK). MuSK is a receptor tyrosine kinase essential for agrin-mediated clustering and anchoring of nicotinic ACh receptors at the postsynaptic motor endplate. MuSK-positive MG predominantly affects females and presents with prominent bulbar, facial, neck, and respiratory weakness, often with tongue and facial muscle atrophy. MuSK-MG patients often respond poorly to pyridostigmine and have normal thymus pathology (thymectomy is generally not beneficial)."
    },
    {
        "id": "FZ_Q099",
        "question_number": 99,
        "category": "Acetylcholine / Neuromuscular Junction Disorder",
        "stem": "An experimental drug is developed that selectively blocks the vesicular acetylcholine transporter (VAChT). Administration of this drug to an isolated nerve-muscle preparation will produce which of the following primary cellular effects in presynaptic motor nerve terminals?",
        "options": [
            {"text": "Failure of newly synthesized acetylcholine to be loaded into synaptic vesicles", "is_correct": True},
            {"text": "Complete inhibition of choline uptake across the plasma membrane", "is_correct": False},
            {"text": "Permanent blockade of voltage-gated calcium channels", "is_correct": False},
            {"text": "Irreversible inhibition of choline acetyltransferase (ChAT)", "is_correct": False},
            {"text": "Immediate spontaneous fusion of all synaptic vesicles with the active zone", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Failure of newly synthesized acetylcholine to be loaded into synaptic vesicles.\n\nThe vesicular acetylcholine transporter (VAChT) is an antiporter located on the membrane of synaptic vesicles that transports acetylcholine from the cytoplasm into the vesicle lumen in exchange for protons (driven by a vacuolar H+-ATPase proton gradient). Pharmacological inhibition of VAChT (e.g., by vesamicol) prevents the loading of ACh into vesicles. Consequently, when an action potential depolarizes the terminal, exocytosis releases empty vesicles, abolishing synaptic transmission.\n\n• Option B is incorrect: Choline uptake across the plasma membrane is mediated by the high-affinity choline transporter (ChT-1), which is inhibited by hemicholinium-3."
    },
    {
        "id": "FZ_Q100",
        "question_number": 100,
        "category": "Acetylcholine / Neuromuscular Junction Disorder",
        "stem": "A 29-year-old woman with a history of myasthenia gravis delivers a healthy-appearing term infant. At 24 hours of life, the newborn develops a weak cry, poor suckling, facial weakness, and generalized hypotonia. Over the next 3 weeks, with supportive feeding, the infant's muscle strength gradually improves, and by 6 weeks of life, all neurological findings have completely resolved without long-term recurrence. Which of the following processes explains this transient neonatal myasthenia gravis?",
        "options": [
            {"text": "Transplacental transfer of maternal IgG autoantibodies against the acetylcholine receptor", "is_correct": True},
            {"text": "Inheritance of an autosomal dominant mutation in the CHRNE gene", "is_correct": False},
            {"text": "Transient neonatal thymic hyperplasia producing endogenous autoantibodies", "is_correct": False},
            {"text": "Perinatal ingestion of Clostridium botulinum spores", "is_correct": False},
            {"text": "Neonatal magnesium toxicity from maternal tocolytic therapy", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Transplacental transfer of maternal IgG autoantibodies against the acetylcholine receptor.\n\nTransient neonatal myasthenia gravis occurs in approximately 10% to 15% of infants born to mothers with myasthenia gravis. Maternal anti-AChR antibodies are of the IgG class and cross the placenta via the neonatal Fc receptor (FcRn) during the third trimester. Circulating maternal antibodies bind the infant's motor endplate receptors, producing transient hypotonia, poor feeding, and weak cry. As the infant naturally catabolizes maternal IgG over the first several weeks of life (half-life of IgG is ~21 days), antibody titers drop and the condition completely resolves without recurrence."
    },

    # =========================================================================
    # TOPIC 6: Neuroimaging (FZ_Q101 - FZ_Q120)
    # =========================================================================
    {
        "id": "FZ_Q101",
        "question_number": 101,
        "category": "Neuroimaging",
        "stem": "A 65-year-old man presents to the emergency department 45 minutes after the sudden onset of right facial droop and right-sided arm and leg weakness. His National Institutes of Health Stroke Scale (NIHSS) score is 14. Which of the following imaging modalities is the immediate first-line diagnostic investigation required to rule out intracranial hemorrhage prior to considering intravenous thrombolytic therapy?",
        "options": [
            {"text": "Non-contrast head CT", "is_correct": True},
            {"text": "Contrast-enhanced brain MRI", "is_correct": False},
            {"text": "Digital subtraction catheter angiography (DSA)", "is_correct": False},
            {"text": "Positron emission tomography (PET)", "is_correct": False},
            {"text": "Single-photon emission computed tomography (SPECT)", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Non-contrast head CT.\n\nIn acute stroke triage, an immediate non-contrast head CT is the mandatory first-line imaging modality. It is universally accessible, takes under 60 seconds to perform, and has near 100% sensitivity for identifying acute intracranial hemorrhage (which appears hyperdense/bright white). Excluding acute hemorrhage is the critical requirement before administering intravenous thrombolytic therapy (alteplase/tenecteplase). In hyperacute ischemic stroke (<3-6 hours), the non-contrast CT is typically normal or may show early subtle signs of ischemia (loss of insular ribbon, obscuration of the lentiform nucleus, dense MCA sign).\n\n• Option B is incorrect: While MRI DWI is most sensitive for hyperacute ischemia, MRI takes longer to acquire, is less universally accessible, and has screening contraindications (pacemakers, metallic implants)."
    },
    {
        "id": "FZ_Q102",
        "question_number": 102,
        "category": "Neuroimaging",
        "stem": "In diagnostic computed tomography (CT), tissue radiodensity is quantified using Hounsfield Units (HU), defined relative to distilled water (0 HU) and air (-1000 HU). On an unenhanced head CT, which of the following physiological or pathological substances typically measures between +60 and +80 Hounsfield Units, appearing distinctly hyperdense (bright white)?",
        "options": [
            {"text": "Acute clotted blood (hematoma)", "is_correct": True},
            {"text": "Subcutaneous adipose tissue (fat)", "is_correct": False},
            {"text": "Normal cerebrospinal fluid (CSF)", "is_correct": False},
            {"text": "Normal cerebral white matter", "is_correct": False},
            {"text": "Dense calvarial cortical bone", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Acute clotted blood (hematoma).\n\nHounsfield Units (HU) of cranial tissues on CT:\n• Air: -1000 HU (pure black)\n• Fat: -100 to -50 HU (dark gray/black)\n• Water / CSF: 0 to +10 HU (dark gray)\n• Brain parenchyma: +20 to +40 HU (white matter ~+30, gray matter ~+40)\n• Acute clotted blood / hematoma: +60 to +80 HU (hyperdense / bright white, due to high protein/globin concentration)\n• Calcification / Cortical bone: +1000 to +3000 HU (dense white).\nAs a hematoma ages and hemoglobin breaks down, its density decreases: subacute blood is isodense (+30-40 HU), and chronic blood is hypodense (<+20 HU)."
    },
    {
        "id": "FZ_Q103",
        "question_number": 103,
        "category": "Neuroimaging",
        "stem": "A 28-year-old woman presents with optic neuritis and paresthesias. A brain MRI is performed using multiple pulse sequences. On T1-weighted images, cerebrospinal fluid in the ventricles appears dark (hypointense), whereas on T2-weighted images, CSF appears bright (hyperintense). Which of the following MRI pulse sequences is specifically designed to suppress the bright signal of free water/CSF while preserving T2 hyperintensity, making periventricular demyelinating multiple sclerosis plaques stand out clearly?",
        "options": [
            {"text": "Fluid-Attenuated Inversion Recovery (FLAIR)", "is_correct": True},
            {"text": "Diffusion-Weighted Imaging (DWI)", "is_correct": False},
            {"text": "Gradient Echo (GRE)", "is_correct": False},
            {"text": "Apparent Diffusion Coefficient (ADC)", "is_correct": False},
            {"text": "Susceptibility-Weighted Imaging (SWI)", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Fluid-Attenuated Inversion Recovery (FLAIR).\n\nFLAIR (Fluid-Attenuated Inversion Recovery) is an inversion recovery MRI sequence that sets the inversion time (TI) specifically to nullify the signal from free fluid (cerebrospinal fluid). On standard T2-weighted images, CSF is bright white ('T2 is H2O'), which can obscure hyperintense pathology immediately adjacent to ventricles. By suppressing the bright ventricular CSF signal to black, FLAIR allows periventricular pathology — such as multiple sclerosis demyelinating plaques (Dawson fingers), subarachnoid hemorrhage, meningitis exudate, and vasogenic edema — to stand out brightly with high contrast.\n\n• Option B is incorrect: DWI detects restricted diffusion in acute ischemic stroke or abscesses."
    },
    {
        "id": "FZ_Q104",
        "question_number": 104,
        "category": "Neuroimaging",
        "stem": "A 62-year-old man presents with sudden-onset left hemiparesis 90 minutes ago. Brain MRI is performed. Diffusion-Weighted Imaging (DWI) reveals a prominent bright hyperintense lesion in the right middle cerebral artery territory, and the corresponding Apparent Diffusion Coefficient (ADC) map shows marked hypointensity (dark signal) in the exact same region. Which of the following cellular events directly produces this restricted diffusion of water molecules in hyperacute ischemic stroke?",
        "options": [
            {"text": "Failure of the Na+/K+ ATPase leads to intracellular accumulation of sodium and water (cytotoxic edema), restricting extracellular water diffusion", "is_correct": True},
            {"text": "Disruption of endothelial tight junctions causes leakage of plasma proteins into the extracellular space (vasogenic edema)", "is_correct": False},
            {"text": "Accumulation of paramagnetic hemosiderin causes local magnetic field inhomogeneities", "is_correct": False},
            {"text": "Proliferation of reactive astrocytes forming a dense fibrous glial scar", "is_correct": False},
            {"text": "Rapid apoptosis of oligodendrocytes with compensatory myelin hypertrophy", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Failure of the Na+/K+ ATPase leads to intracellular accumulation of sodium and water (cytotoxic edema), restricting extracellular water diffusion.\n\nDiffusion-Weighted Imaging (DWI) measures the Brownian motion (random microscopic diffusion) of water molecules. In hyperacute cerebral ischemia:\n1. Oxygen and glucose deprivation depletes ATP within minutes.\n2. The energy-dependent Na+/K+ ATPase fails, allowing Na+ to accumulate intracellularly.\n3. Water rushes into neurons and glia down osmotic gradients, causing cellular swelling (cytotoxic edema).\n4. Swollen cells compress the extracellular space and trap water inside cell membranes, severely restricting water mobility.\nRestricted water diffusion appears BRIGHT on DWI and DARK on the ADC map. Confirming hypointensity on the ADC map is essential to confirm true restricted diffusion and rule out 'T2 shine-through'.\n\n• Option B is incorrect: Vasogenic edema occurs days later due to BBB breakdown, showing increased extracellular diffusion (dark on DWI, bright on ADC)."
    },
    {
        "id": "FZ_Q105",
        "question_number": 105,
        "category": "Neuroimaging",
        "stem": "A 78-year-old man with Alzheimer disease experiences progressive cognitive decline and two transient episodes of left arm weakness. A non-contrast head CT is unremarkable. Brain MRI using Gradient Recalled Echo (GRE) and Susceptibility-Weighted Imaging (SWI) demonstrates multiple punctate, round hypointense foci with prominent 'blooming artifact' scattered throughout the peripheral cerebral cortex at the gray-white junction. Which of the following conditions is most likely responsible for these cortical microbleeds?",
        "options": [
            {"text": "Cerebral amyloid angiopathy (CAA)", "is_correct": True},
            {"text": "Hypertensive arteriopathy (Charcot-Bouchard microaneurysms)", "is_correct": False},
            {"text": "Subacute bacterial endocarditis", "is_correct": False},
            {"text": "Cavernous sinus thrombosis", "is_correct": False},
            {"text": "Primary central nervous system lymphoma", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Cerebral amyloid angiopathy (CAA).\n\nCerebral amyloid angiopathy (CAA) is caused by the deposition of beta-amyloid in the media and adventitia of small-to-medium cortical and leptomeningeal arteries, weakening vessel walls. It is a common cause of spontaneous lobar hemorrhage in the elderly and is strongly associated with Alzheimer disease. \n• On GRE and SWI pulse sequences, paramagnetic blood breakdown products (hemosiderin and deoxyhemoglobin) distort local magnetic fields, creating a prominent dark signal loss known as 'blooming artifact'.\n• In CAA, microbleeds are characteristically LOBAR and peripheral (cortex and gray-white junction, especially parietal and occipital lobes).\n\n• Option B is incorrect: Hypertensive microbleeds occur in deep structures (basal ganglia, thalamus, internal capsule, pons, cerebellum)."
    },
    {
        "id": "FZ_Q106",
        "question_number": 106,
        "category": "Neuroimaging",
        "stem": "An 81-year-old woman with a history of frequent falls is brought to the clinic because of worsening apathy, slow walking, and mild confusion over the past 3 weeks. A head CT scan without contrast reveals a crescent-shaped extra-axial hypodense collection overlying the right cerebral convexity that crosses cranial suture lines and produces mild midline shift. Which of the following vascular structures was torn to cause this chronic subdural hematoma?",
        "options": [
            {"text": "Bridging cortical veins", "is_correct": True},
            {"text": "Middle meningeal artery", "is_correct": False},
            {"text": "Posterior communicating artery aneurysm", "is_correct": False},
            {"text": "Lenticulostriate perforating arteries", "is_correct": False},
            {"text": "Anterior inferior cerebellar artery", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Bridging cortical veins.\n\nSubdural hematomas (SDH) result from tearing of bridging cortical veins as they traverse the subdural space between the arachnoid mater and the dural venous sinuses (superior sagittal sinus). In elderly individuals, age-related cerebral atrophy increases the distance the bridging veins must span, making them taut and susceptible to tearing even after minor, forgotten head trauma. \n• On CT, subdural hematomas appear crescent-shaped, concave along the inner calvarium, and can cross cranial suture lines (bounded only by dural reflections like the falx and tentorium).\n• Acute blood is hyperdense; over 2-3 weeks, enzymatic breakdown turns the collection isodense and eventually hypodense (chronic SDH).\n\n• Option B is incorrect: Middle meningeal artery laceration causes epidural hematoma (biconvex/lenticular, does not cross sutures)."
    },
    {
        "id": "FZ_Q107",
        "question_number": 107,
        "category": "Neuroimaging",
        "stem": "A 54-year-old woman presents with a sudden, excruciating headache that peaked within seconds, which she describes as the 'worst headache of my life.' A non-contrast head CT demonstrates high-attenuation hyperdensity filling the basal cisterns, sylvian fissures, and interhemispheric fissure. Rupture of a saccular (berry) aneurysm at which of the following Circle of Willis junctions is the most common cause of this subarachnoid hemorrhage?",
        "options": [
            {"text": "Anterior communicating artery (AComA)", "is_correct": True},
            {"text": "Basilar artery bifurcation", "is_correct": False},
            {"text": "Posterior inferior cerebellar artery (PICA)", "is_correct": False},
            {"text": "Superior cerebellar artery (SCA)", "is_correct": False},
            {"text": "Ophthalmic artery origin", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Anterior communicating artery (AComA).\n\nSubarachnoid hemorrhage (SAH) is most commonly caused by rupture of a saccular (berry) aneurysm in the Circle of Willis (associated with autosomal dominant polycystic kidney disease, Marfan syndrome, Ehlers-Danlos syndrome, hypertension, and smoking). The most common sites of berry aneurysms are:\n1. Anterior communicating artery (AComA) junction (~85% occur in anterior circulation).\n2. Posterior communicating artery (PComA) junction (causes CN III palsy).\n3. Middle cerebral artery (MCA) bifurcation.\nNon-contrast head CT shows hyperdense blood layering within the subarachnoid space (basal cisterns and sulci). If CT is negative within 6-12 hours but clinical suspicion remains high, lumbar puncture must be performed to assess for xanthochromia."
    },
    {
        "id": "FZ_Q108",
        "question_number": 108,
        "category": "Neuroimaging",
        "stem": "A 60-year-old man with a 30 pack-year smoking history and newly diagnosed lung adenocarcinoma presents with headaches and an unprovoked generalized seizure. A contrast-enhanced brain MRI reveals multiple well-circumscribed, ring-enhancing lesions located at the gray-white matter junctions of both cerebral hemispheres, surrounded by extensive vasogenic edema. Which of the following imaging and pathophysiological features is most characteristic of hematogenous brain metastases?",
        "options": [
            {"text": "Multiple lesions clustering at the junction of the cortex and subcortical white matter where caliber-narrowing arterioles trap tumor emboli", "is_correct": True},
            {"text": "Single extra-axial mass with a hyperostotic skull base and dural tail", "is_correct": False},
            {"text": "Infiltration of the corpus callosum forming a butterfly-shaped lesion", "is_correct": False},
            {"text": "Well-circumscribed cystic lesion with an enhancing mural nodule in the cerebellar hemisphere", "is_correct": False},
            {"text": "Restricted diffusion within the cavernous sinus lumen", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Multiple lesions clustering at the junction of the cortex and subcortical white matter where caliber-narrowing arterioles trap tumor emboli.\n\nBrain metastases are the most common brain tumors in adults (surpassing primary CNS neoplasms by 10:1). Primary origins in descending order: Lung > Breast > Melanoma > Renal cell carcinoma > Colon. Metastatic tumor emboli travel hematogenously and become lodged at points where branching vessels abruptly narrow, which characteristically occurs at the junction of gray and white matter. Metastases appear as multiple, discrete, rounded, ring-enhancing masses surrounded by extensive digitating finger-like vasogenic edema (hyperintense on T2/FLAIR).\n\n• Option B is incorrect: Meningioma.\n• Option C is incorrect: Glioblastoma multiforme (GBM).\n• Option D is incorrect: Pilocytic astrocytoma (childhood cerebellar tumor)."
    },
    {
        "id": "FZ_Q109",
        "question_number": 109,
        "category": "Neuroimaging",
        "stem": "A 58-year-old man presents with progressive headaches and left-sided hemiparesis. Brain MRI demonstrates an irregular, thick ring-enhancing mass measuring 5 cm in the right frontoparietal lobe. The mass invades across the corpus callosum into the left hemisphere ('butterfly glioma') and exhibits central non-enhancing hypointensity representing coagulative necrosis. Histological biopsy reveals pleomorphic GFAP-positive cells with pseudopalisading necrosis and florid microvascular proliferation. Which of the following is the diagnosis?",
        "options": [
            {"text": "Glioblastoma (WHO grade 4 astrocytoma)", "is_correct": True},
            {"text": "Oligodendroglioma", "is_correct": False},
            {"text": "Pilocytic astrocytoma", "is_correct": False},
            {"text": "Primary CNS lymphoma", "is_correct": False},
            {"text": "Cerebral abscess", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Glioblastoma (WHO grade 4 astrocytoma).\n\nGlioblastoma (formerly glioblastoma multiforme / GBM) is the most common and aggressive primary malignant brain tumor in adults. Characteristic neuroimaging:\n• Large, heterogeneously enhancing mass with a thick, irregular, nodular ring of enhancement surrounding a central dark core of necrosis.\n• High propensity to cross the white matter commissure of the corpus callosum into the opposite hemisphere ('butterfly glioma').\nHistological hallmarks:\n• Pseudopalisading pleomorphic tumor cells lining up along borders of serpentine necrosis.\n• Florid microvascular (glomeruloid) proliferation driven by VEGF.\n• GFAP (glial fibrillary acidic protein) positivity confirming astrocytic lineage."
    },
    {
        "id": "FZ_Q110",
        "question_number": 110,
        "category": "Neuroimaging",
        "stem": "A 49-year-old woman presents with a single generalized seizure. A contrast-enhanced brain MRI reveals a 3.5 cm, sharply circumscribed, intensely and homogeneously enhancing extra-axial mass abutting the inner surface of the parietal calvarium. The mass compresses the underlying cerebral cortex without invading it, and exhibits a linear tapering edge of contrast enhancement extending along the dura mater ('dural tail'). Which of the following histological features is diagnostic of this benign tumor (meningioma)?",
        "options": [
            {"text": "Spindle-shaped cells arranged in concentric whorls with laminated calcified psammoma bodies", "is_correct": True},
            {"text": "Pseudopalisading pleomorphic cells surrounding central necrosis", "is_correct": False},
            {"text": "Round nuclei with clear halos ('fried egg' cells) and chicken-wire capillaries", "is_correct": False},
            {"text": "Eosinophilic Rosenthal fibers with corkscrew morphology", "is_correct": False},
            {"text": "Perivascular pseudorosettes with ependymal canals", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Spindle-shaped cells arranged in concentric whorls with laminated calcified psammoma bodies.\n\nMeningiomas are the most common benign intracranial tumors in adults, originating from arachnoid cap cells of the meninges. Radiographic hallmarks:\n• Extra-axial, well-demarcated, dural-based mass that compresses (does not invade) adjacent brain parenchyma.\n• Dense, homogeneous contrast enhancement with a prominent 'dural tail'.\n• May cause hyperostosis (reactive thickening) of the overlying skull bone.\nHistological hallmarks:\n• Elongated spindle-shaped cells arranged in concentric whorls.\n• Psammoma bodies (concentric laminated calcifications formed by degenerating whorled tumor cells).\n• Often express progesterone receptors (explaining increased growth during pregnancy)."
    },
    {
        "id": "FZ_Q111",
        "question_number": 111,
        "category": "Neuroimaging",
        "stem": "A 35-year-old woman presents with progressive unilateral hearing loss, tinnitus, and unsteadiness. Brain MRI reveals a 2.5 cm enhancing mass located in the cerebellopontine angle, extending into the internal acoustic meatus. Biopsy demonstrates alternating areas of dense cellularity with nuclear palisading around acellular eosinophilic zones (Antoni A areas and Verocay bodies) and loose, hypocellular myxoid tissue (Antoni B areas). The tumor is strongly immunoreactive for S100. From which of the following cells does this vestibular schwannoma arise?",
        "options": [
            {"text": "Schwann cells of cranial nerve VIII", "is_correct": True},
            {"text": "Oligodendrocytes of the brainstem", "is_correct": False},
            {"text": "Arachnoid cap cells of the dura mater", "is_correct": False},
            {"text": "Ependymal cells of the fourth ventricle", "is_correct": False},
            {"text": "Microglia of the cerebellum", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Schwann cells of cranial nerve VIII.\n\nVestibular schwannoma (acoustic neuroma) is a benign peripheral nerve sheath tumor arising from neural crest-derived Schwann cells of the vestibular division of cranial nerve VIII (at the cerebellopontine angle / internal acoustic meatus). Histological characteristics:\n• Biphasic growth pattern:\n  - Antoni A areas: Dense cellular zones with spindle cells and nuclear palisading around Verocay bodies.\n  - Antoni B areas: Hypocellular, loose, myxoid tissue.\n• Strong, diffuse S100 protein positivity (confirming neural crest origin).\nBilateral vestibular schwannomas are pathognomonic for Neurofibromatosis type 2 (NF2, mutation in merlin/schwannomin on chromosome 22q)."
    },
    {
        "id": "FZ_Q112",
        "question_number": 112,
        "category": "Neuroimaging",
        "stem": "A 30-year-old man presents with fever, severe headache, and focal seizures. Contrast-enhanced MRI reveals a well-defined, smooth, thin ring-enhancing lesion in the frontal lobe with extensive surrounding vasogenic edema. On Diffusion-Weighted Imaging (DWI), the central non-enhancing core of the lesion shows intensely bright hyperintensity with corresponding dark hypointensity on the ADC map (marked restricted diffusion). Which of the following is the most likely diagnosis?",
        "options": [
            {"text": "Bacterial brain abscess", "is_correct": True},
            {"text": "High-grade glioblastoma", "is_correct": False},
            {"text": "Metastatic melanoma", "is_correct": False},
            {"text": "Radiation necrosis", "is_correct": False},
            {"text": "Resolving subacute hematoma", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Bacterial brain abscess.\n\nA bacterial brain abscess appears on contrast MRI as a smooth, uniformly thin, ring-enhancing capsule surrounded by prominent vasogenic edema. The definitive imaging feature that distinguishes an abscess from a necrotic tumor (glioblastoma or metastasis) is Diffusion-Weighted Imaging (DWI):\n• Abscess core contains viscous pus composed of dense, packed neutrophils, necrotic debris, and cellular macromolecules, which severely restricts the Brownian motion of water molecules.\n• This produces marked central restricted diffusion (bright on DWI, dark on ADC map).\n• In contrast, the necrotic core of a glioblastoma is serous fluid that does NOT restrict diffusion (dark on DWI, bright on ADC)."
    },
    {
        "id": "FZ_Q113",
        "question_number": 113,
        "category": "Neuroimaging",
        "stem": "A 48-year-old woman presents with bilateral lower extremity weakness and visual disturbances. MRI of the brain and spine reveals multiple demyelinating lesions. On sagittal T2/FLAIR sequences of the brain, several linear, finger-like hyperintense plaques are observed extending perpendicularly outward from the ependymal surface of the lateral ventricles into the corpus callosum ('Dawson fingers'). Which of the following histological processes is responsible for these characteristic MRI findings?",
        "options": [
            {"text": "Perivenular lymphocytic inflammation and demyelination surrounding deep medullary veins", "is_correct": True},
            {"text": "Arterial microinfarctions within the territory of lenticulostriate perforators", "is_correct": False},
            {"text": "Amyloid angiopathy of subcortical U-fibers", "is_correct": False},
            {"text": "Hyaline arteriolosclerosis of long circumferential pontine arteries", "is_correct": False},
            {"text": "Metastatic tumor seeding through the Virchow-Robin spaces", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Perivenular lymphocytic inflammation and demyelination surrounding deep medullary veins.\n\n'Dawson fingers' are a classic radiographic hallmark of multiple sclerosis on sagittal FLAIR or T2 MRI sequences. They appear as ovoid or linear demyelinating plaques oriented perpendicularly to the ventricular margins, extending into the corpus callosum and centrum semiovale. Neuropathologically, MS is a perivenular inflammatory disease: autoreactive T-cell infiltration and complement-mediated myelin destruction occur along the path of deep medullary venules that drain perpendicularly into the subependymal veins of the lateral ventricles."
    },
    {
        "id": "FZ_Q114",
        "question_number": 114,
        "category": "Neuroimaging",
        "stem": "A 72-year-old man with a history of poorly controlled hypertension presents to the emergency department with sudden severe right hemiparesis and stupor. A non-contrast head CT reveals a 4.5 cm hyperdense (65 HU) collection centered in the left putamen and posterior limb of the internal capsule, with surrounding hypodense edema and mass effect compressing the left lateral ventricle. Rupture of Charcot-Bouchard microaneurysms involving which of the following arterial branches is the most common cause of this hypertensive intraparenchymal hemorrhage?",
        "options": [
            {"text": "Lenticulostriate arteries (branches of the middle cerebral artery)", "is_correct": True},
            {"text": "Cortical branches of the anterior cerebral artery", "is_correct": False},
            {"text": "Posterior inferior cerebellar artery (PICA)", "is_correct": False},
            {"text": "Anterior communicating artery", "is_correct": False},
            {"text": "Ophthalmic artery", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Lenticulostriate arteries (branches of the middle cerebral artery).\n\nChronic hypertension causes hyaline arteriolosclerosis and lipohyalinosis of small, deep penetrating arterioles, leading to the formation of Charcot-Bouchard microaneurysms. Rupture of these microaneurysms causes spontaneous intraparenchymal (intracerebral) hemorrhage. The most common anatomical site is the basal ganglia / putamen (~50-60% of cases), supplied by the lenticulostriate branches of the middle cerebral artery (MCA). Other common sites include the thalamus, pons, and cerebellar hemispheres.\n\n• Option D is incorrect: Berry aneurysms of the anterior communicating artery rupture into the subarachnoid space (causing subarachnoid hemorrhage), not the deep basal ganglia."
    },
    {
        "id": "FZ_Q115",
        "question_number": 115,
        "category": "Neuroimaging",
        "stem": "A 21-year-old unrestrained driver is involved in a high-speed rollover motor vehicle collision. In the trauma bay, his Glasgow Coma Scale score is 4 (E1V1M2), and he is intubated. Initial non-contrast head CT reveals no skull fractures, no epidural or subdural hematomas, and only a tiny punctate petechial hyperdensity at the gray-white matter interface of the frontal lobe. An urgent MRI using Gradient Echo (GRE) and Susceptibility-Weighted Imaging (SWI) reveals numerous punctate hypointense blooming lesions distributed throughout the gray-white junction and the splenium of the corpus callosum. Which of the following traumatic injuries is present?",
        "options": [
            {"text": "Diffuse axonal injury (DAI)", "is_correct": True},
            {"text": "Acute epidural hematoma", "is_correct": False},
            {"text": "Subarachnoid hemorrhage", "is_correct": False},
            {"text": "Cerebral amyloid angiopathy", "is_correct": False},
            {"text": "Transtentorial herniation", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Diffuse axonal injury (DAI).\n\nDiffuse axonal injury (DAI) is caused by high-velocity rotational acceleration-deceleration forces that generate shear stress at interfaces between tissues of differing density (most prominently the gray-white matter junction, corpus callosum, and dorsal brainstem). Axons stretch and shear, disrupting the axoskeleton and axonal transport, causing axonal retraction balls (beta-APP immunoreactive). Patients present in immediate coma that is strikingly disproportionate to early CT findings (which may appear normal or show subtle punctate hemorrhages). GRE and SWI sequences on MRI are diagnostic, revealing punctate hypointense microbleeds ('blooming artifact') from sheared microvessels."
    },
    {
        "id": "FZ_Q116",
        "question_number": 116,
        "category": "Neuroimaging",
        "stem": "An 8-year-old boy presents with progressive morning headaches, vomiting, and gait ataxia. Contrast-enhanced MRI of the brain reveals a well-circumscribed cystic lesion in the right cerebellar hemisphere containing an intensely enhancing mural nodule. The surrounding brain parenchyma shows minimal vasogenic edema. Surgical resection is performed. Histopathology reveals bipolar cells with long, thin 'hair-like' cytoplasmic processes and corkscrew-shaped eosinophilic Rosenthal fibers. Which of the following is the diagnosis?",
        "options": [
            {"text": "Pilocytic astrocytoma", "is_correct": True},
            {"text": "Medulloblastoma", "is_correct": False},
            {"text": "Ependymoma", "is_correct": False},
            {"text": "Craniopharyngioma", "is_correct": False},
            {"text": "Glioblastoma", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Pilocytic astrocytoma.\n\nPilocytic astrocytoma (WHO grade 1) is the most common primary brain tumor in children. It most frequently arises in the cerebellum. Radiographic appearance:\n• Well-circumscribed, cystic lesion with an intensely enhancing mural nodule on contrast MRI.\nHistological hallmarks:\n• Bipolar astrocytic cells with long, thin processes ('hair-like' / pilocytic).\n• Rosenthal fibers: Corkscrew-shaped, brightly eosinophilic intracytoplasmic inclusions composed of alpha-B-crystallin and heat shock proteins.\n• Excellent prognosis following surgical resection.\n\n• Option B is incorrect: Medulloblastoma is a solid, poorly differentiated embryonal tumor (small round blue cells with Homer Wright rosettes) in the cerebellar vermis."
    },
    {
        "id": "FZ_Q117",
        "question_number": 117,
        "category": "Neuroimaging",
        "stem": "A 6-year-old boy presents with unsteady gait, frequent falls, and morning vomiting. Brain MRI demonstrates a solid, contrast-enhancing mass originating from the cerebellar vermis in the midline, compressing the fourth ventricle and causing obstructive hydrocephalus. Histopathological evaluation reveals sheets of densely packed small round blue cells with hyperchromatic nuclei, high mitotic index, and Homer Wright rosettes (tumor cells surrounding a central neuropil). Which of the following is the diagnosis?",
        "options": [
            {"text": "Medulloblastoma", "is_correct": True},
            {"text": "Pilocytic astrocytoma", "is_correct": False},
            {"text": "Schwannoma", "is_correct": False},
            {"text": "Oligodendroglioma", "is_correct": False},
            {"text": "Craniopharyngioma", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Medulloblastoma.\n\nMedulloblastoma is the most common malignant brain tumor in childhood (WHO grade 4). It is a primitive neuroectodermal embryonal tumor that characteristically arises in the midline cerebellar vermis (in the roof of the 4th ventricle). It can obstruct the 4th ventricle causing non-communicating hydrocephalus and has a propensity to 'drop metastasize' via CSF pathways to the cauda equina in the spinal cord. Histology reveals small, poorly differentiated cells with high nuclear-to-cytoplasmic ratio ('small round blue cell tumor') forming Homer Wright pseudorosettes."
    },
    {
        "id": "FZ_Q118",
        "question_number": 118,
        "category": "Neuroimaging",
        "stem": "A 12-year-old girl is evaluated for short stature and delayed puberty. Visual field testing reveals bitemporal hemianopia. Contrast CT of the head reveals a cystic, lobulated suprasellar mass with prominent ring-like peripheral calcifications. When aspirating the cyst during surgery, the neurosurgeon notes thick, viscous fluid with glistening cholesterol crystals resembling 'motor oil.' From which of the following embryological structures does this craniopharyngioma derive?",
        "options": [
            {"text": "Rathke pouch (surface ectoderm outpouching of the stomodeum)", "is_correct": True},
            {"text": "Neurohypophysis (infundibulum of the diencephalon)", "is_correct": False},
            {"text": "Notochord remnants", "is_correct": False},
            {"text": "Pineal gland neuroectoderm", "is_correct": False},
            {"text": "Neural crest cells of the optic cup", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Rathke pouch (surface ectoderm outpouching of the stomodeum).\n\nCraniopharyngioma is a benign, epithelial suprasellar tumor derived from remnants of Rathke pouch (an embryonic diverticulum of stomodeal surface ectoderm that gives rise to the anterior pituitary / adenohypophysis). It displays a bimodal age distribution (peaks at 5-14 years and 50-75 years). Classic triad:\n1. Bitemporal hemianopia (suprasellar mass compressing the optic chiasm from above).\n2. Endocrine deficiencies: Growth hormone deficiency causing short stature; hypopituitarism; diabetes insipidus.\n3. Imaging: Suprasellar cystic mass with prominent peripheral calcification.\nPathology: Cyst fluid rich in cholesterol crystals resembling dark 'motor oil'; wet keratin and squamous epithelium."
    },
    {
        "id": "FZ_Q119",
        "question_number": 119,
        "category": "Neuroimaging",
        "stem": "A 42-year-old man presents with chronic headaches. Contrast-enhanced MRI reveals a 3 cm, well-circumscribed, extra-axial mass arising from the right middle cranial fossa. The radiologist notes that the tumor demonstrates uniform T1 hypointensity, T2 hyperintensity, and intense, uniform enhancement. Intravenous Gadolinium-based contrast agents are used routinely in clinical neuroimaging. Which of the following principles explains how gadolinium creates contrast enhancement on T1-weighted MRI sequences?",
        "options": [
            {"text": "Paramagnetic gadolinium shortens the T1 relaxation time of surrounding water protons, producing bright hyperintensity wherever the blood-brain barrier is disrupted", "is_correct": True},
            {"text": "Gadolinium directly blocks X-ray photon penetration via high atomic density", "is_correct": False},
            {"text": "Gadolinium induces radiofrequency emissions by decaying via beta-plus emission", "is_correct": False},
            {"text": "Gadolinium binds permanently to neuronal cell membranes, increasing sodium permeability", "is_correct": False},
            {"text": "Gadolinium cools local brain tissue, slowing proton spin precession", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Paramagnetic gadolinium shortens the T1 relaxation time of surrounding water protons, producing bright hyperintensity wherever the blood-brain barrier is disrupted.\n\nGadolinium (Gd3+) is a rare earth metal with seven unpaired electrons, making it strongly paramagnetic. When chelated (to prevent toxicity) and injected intravenously, it remains within intravascular spaces unless the blood-brain barrier is compromised. Gadolinium does not emit signal itself; instead, its fluctuating magnetic field dramatically accelerates the spin-lattice (T1) relaxation rate of adjacent hydrogen nuclei (water protons). Shortening T1 relaxation causes tissues to recover longitudinal magnetization much faster, resulting in high signal intensity (BRIGHT enhancement) on T1-weighted images in areas of vascular breakdown (tumors, infections, inflammation)."
    },
    {
        "id": "FZ_Q120",
        "question_number": 120,
        "category": "Neuroimaging",
        "stem": "A 68-year-old woman presents to the clinic with memory loss and difficulty managing finances. A brain MRI is ordered to differentiate Alzheimer disease from vascular dementia. The scan demonstrates diffuse cerebral cortical atrophy, predominantly affecting the entorhinal cortex and temporal lobes. Which of the following specific temporal lobe structures exhibits the earliest and most severe atrophy in early-stage Alzheimer disease?",
        "options": [
            {"text": "Hippocampus", "is_correct": True},
            {"text": "Substantia nigra", "is_correct": False},
            {"text": "Caudate nucleus", "is_correct": False},
            {"text": "Cerebellar tonsils", "is_correct": False},
            {"text": "Medial geniculate nucleus", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Hippocampus.\n\nIn Alzheimer disease, neurodegeneration and neurofibrillary tangle pathology begin in the transentorhinal cortex and spread directly to the hippocampus (CA1 subfield and subiculum) before involving diffuse association neocortex. High-resolution volumetric MRI demonstrates progressive, disproportionate atrophy of the hippocampus and parahippocampal gyrus, accompanied by compensatory enlargement of the temporal horns of the lateral ventricles, correlating closely with the severity of early episodic anterograde memory impairment.\n\n• Option B is incorrect: Substantia nigra atrophy occurs in Parkinson disease.\n• Option C is incorrect: Caudate atrophy occurs in Huntington disease."
    },

    # =========================================================================
    # TOPIC 7: Tactile Pathway (FZ_Q121 - FZ_Q140)
    # =========================================================================
    {
        "id": "FZ_Q121",
        "question_number": 121,
        "category": "Tactile Pathway",
        "stem": "A 52-year-old man presents with progressive loss of sensation in both legs. Neurological examination reveals severe impairment of vibration sense (tested with a 128-Hz tuning fork) and conscious proprioception in his feet and ankles, while pain and temperature sensation remain completely intact. Which of the following anatomical pathways conveys vibratory sense, two-point discrimination, and conscious proprioception from the lower extremities to the brain?",
        "options": [
            {"text": "Fasciculus gracilis of the dorsal column-medial lemniscal pathway", "is_correct": True},
            {"text": "Fasciculus cuneatus of the dorsal column-medial lemniscal pathway", "is_correct": False},
            {"text": "Lateral spinothalamic tract", "is_correct": False},
            {"text": "Ventral spinocerebellar tract", "is_correct": False},
            {"text": "Rubrospinal tract", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Fasciculus gracilis of the dorsal column-medial lemniscal pathway.\n\nThe Dorsal Column-Medial Lemniscal (DCML) pathway conveys discriminative touch, vibration, and conscious proprioception. The dorsal funiculus is divided into two white matter tracts:\n• Fasciculus Gracilis: Located medially; carries fibers from the lower body (lower extremities and trunk below spinal level T6; 'gracilis = grass/ground').\n• Fasciculus Cuneatus: Located laterally; carries fibers from the upper body (upper extremities and neck above spinal level T6; 'cuneatus = clouds/arms').\nBoth tracts ascend ipsilaterally in the spinal cord without decussating until reaching the medulla.\n\n• Option C is incorrect: The lateral spinothalamic tract carries pain and temperature."
    },
    {
        "id": "FZ_Q122",
        "question_number": 122,
        "category": "Tactile Pathway",
        "stem": "In the dorsal column-medial lemniscal (DCML) pathway, primary afferent axons ascend uncrossed in the posterior funiculus of the spinal cord to the lower brainstem. Where do these first-order sensory axons synapse with the cell bodies of second-order neurons, and where do the second-order axons decussate across the midline?",
        "options": [
            {"text": "Synapse in Nucleus Gracilis and Nucleus Cuneatus in the caudal medulla; decussate as internal arcuate fibers in the caudal medulla", "is_correct": True},
            {"text": "Synapse in the substantia gelatinosa of the spinal cord; decussate via the anterior white commissure", "is_correct": False},
            {"text": "Synapse in the ventral posterolateral (VPL) nucleus of the thalamus; decussate in the midbrain", "is_correct": False},
            {"text": "Synapse in the inferior olivary nucleus; decussate in the pons", "is_correct": False},
            {"text": "Synapse in the red nucleus; decussate in the ventral tegmental decussation", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Synapse in Nucleus Gracilis and Nucleus Cuneatus in the caudal medulla; decussate as internal arcuate fibers in the caudal medulla.\n\nThe DCML pathway consists of a three-neuron chain:\n1. First-order neuron: Cell bodies in the dorsal root ganglion (DRG); large myelinated axons enter the cord and ascend ipsilaterally in the fasciculus gracilis or cuneatus.\n2. Second-order neuron: Synapse in the Nucleus Gracilis (lower limb) or Nucleus Cuneatus (upper limb) in the closed caudal medulla. Axons exit these nuclei as internal arcuate fibers, DECUSSATE across the midline (sensory decussation) in the caudal medulla, and ascend as the Medial Lemniscus through the brainstem.\n3. Third-order neuron: Synapse in the Ventral Posterolateral (VPL) nucleus of the thalamus, projecting via the posterior limb of the internal capsule to the primary somatosensory cortex (postcentral gyrus)."
    },
    {
        "id": "FZ_Q123",
        "question_number": 123,
        "category": "Tactile Pathway",
        "stem": "A 44-year-old man presents with unsteady gait, particularly when walking in the dark. On physical examination, when he stands with his feet together and eyes open, he is steady and maintains his balance. However, when he is instructed to close his eyes, he immediately begins to sway violently and would fall without support. This positive Romberg sign indicates pathology in which of the following sensory systems?",
        "options": [
            {"text": "Conscious proprioception mediated by the dorsal column-medial lemniscal pathway", "is_correct": True},
            {"text": "Cerebellar hemisphere coordination", "is_correct": False},
            {"text": "Spinothalamic tract pain transmission", "is_correct": False},
            {"text": "Lateral corticospinal motor execution", "is_correct": False},
            {"text": "Reticulospinal postural modulation", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Conscious proprioception mediated by the dorsal column-medial lemniscal pathway.\n\nMaintaining balance requires at least two of three sensory modalities: (1) Vision, (2) Vestibular function, and (3) Proprioception (joint position sense via DCML). \n• In the Romberg test, the patient stands with feet together. Opening the eyes allows visual compensation for defective proprioception.\n• Closing the eyes removes visual input. If proprioception is impaired (sensory ataxia), the patient sways and loses balance (positive Romberg test).\n• In contrast, a patient with cerebellar ataxia sways and falls with eyes open AND closed because the motor coordinating center itself is damaged."
    },
    {
        "id": "FZ_Q124",
        "question_number": 124,
        "category": "Tactile Pathway",
        "stem": "A sensory physiologist records action potentials from cutaneous mechanoreceptors in human fingertips. A vibrating mechanical probe vibrating at high frequency (200-300 Hz) is placed against the skin. The receptor responds with rapid, transient action potentials at the onset and offset of the stimulus, adapting within milliseconds. Histological examination reveals a large, ovoid encapsulated structure composed of concentric lamellae of flattened Schwann cells surrounding a central unmyelinated axon terminal ('onion-skin' appearance). Which mechanoreceptor is being tested?",
        "options": [
            {"text": "Pacinian corpuscle", "is_correct": True},
            {"text": "Meissner corpuscle", "is_correct": False},
            {"text": "Merkel disc", "is_correct": False},
            {"text": "Ruffini ending", "is_correct": False},
            {"text": "Free nerve ending", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Pacinian corpuscle.\n\nPacinian corpuscles are rapidly adapting (phasic) mechanoreceptors located deep in the dermis, subcutaneous tissue, ligaments, and periosteum. Histologically, they consist of a single myelinated axon terminating in a large, encapsulated structure of concentric lamellae (resembling a sliced onion). They are tuned to detect deep pressure and high-frequency vibration (optimal at 200-300 Hz). The outer fluid-filled lamellae act as a mechanical filter: sustained pressure deforms the capsule transiently, but the fluid rapidly redistributes, ending receptor potential firing unless the stimulus changes frequency."
    },
    {
        "id": "FZ_Q125",
        "question_number": 125,
        "category": "Tactile Pathway",
        "stem": "A blind individual reads Braille text by gliding their fingertips across raised dots. Which of the following cutaneous mechanoreceptors, located in the basal layer of the epidermis, is slowly adapting (type 1) and provides the high spatial resolution necessary for distinguishing static shapes, sharp edges, and fine surface textures?",
        "options": [
            {"text": "Merkel disc (Merkel cell-neurite complex)", "is_correct": True},
            {"text": "Pacinian corpuscle", "is_correct": False},
            {"text": "Meissner corpuscle", "is_correct": False},
            {"text": "Ruffini cylinder", "is_correct": False},
            {"text": "Hair follicle receptor", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Merkel disc (Merkel cell-neurite complex).\n\nMerkel discs (slowly adapting type 1 mechanoreceptors) are unencapsulated nerve endings associated with specialized neuroendocrine Merkel cells in the stratum basale of the epidermis. They have small, distinct receptive fields with sharp borders. Because they adapt slowly, they fire continuously during sustained mechanical contact. They provide the highest tactile spatial acuity of all mechanoreceptors, enabling humans to resolve points separated by <1 mm, detect fine edges, and read Braille.\n\n• Option C is incorrect: Meissner corpuscles are rapidly adapting, detecting dynamic light touch and low-frequency flutter."
    },
    {
        "id": "FZ_Q126",
        "question_number": 126,
        "category": "Tactile Pathway",
        "stem": "Which of the following encapsulated mechanoreceptors is situated within the dermal papillae of hairless (glabrous) skin (such as the fingertips, palms, and soles), adapting rapidly to detect dynamic light flutter, low-frequency vibration (30-50 Hz), and minute slips across the skin to facilitate grip control?",
        "options": [
            {"text": "Meissner corpuscle", "is_correct": True},
            {"text": "Pacinian corpuscle", "is_correct": False},
            {"text": "Merkel disc", "is_correct": False},
            {"text": "Ruffini ending", "is_correct": False},
            {"text": "Golgi tendon organ", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Meissner corpuscle.\n\nMeissner corpuscles are rapidly adapting (phasic) encapsulated mechanoreceptors located in the dermal papillae of glabrous (hairless) skin, oriented perpendicular to the skin surface. They have small receptive fields and are exquisitely sensitive to dynamic light touch, motion, low-frequency flutter (30-50 Hz), and slip between the fingers and a held object. Rapid feedback from Meissner corpuscles triggers immediate reflex adjustments of grip force to prevent dropping objects."
    },
    {
        "id": "FZ_Q127",
        "question_number": 127,
        "category": "Tactile Pathway",
        "stem": "A 56-year-old man presents with a history of untreated syphilis contracted 25 years ago. He complains of sudden, lancinating, lightning-like pains shooting down his legs and extreme difficulty walking in the dark. Physical examination reveals a wide-based, stomping gait, loss of vibratory and position sense in both lower extremities, a positive Romberg test, absent knee and ankle reflexes, and bilateral pupils that constrict to accommodation but do not react to light (Argyll Robertson pupils). Which of the following pathological processes characterizes this patient's tabes dorsalis?",
        "options": [
            {"text": "Progressive demyelination and degeneration of dorsal roots and dorsal columns (fasciculus gracilis and cuneatus)", "is_correct": True},
            {"text": "Infarction of the anterior spinal artery territory", "is_correct": False},
            {"text": "Expansion of a syrinx within the anterior white commissure", "is_correct": False},
            {"text": "Degeneration of upper and lower motor neurons without sensory involvement", "is_correct": False},
            {"text": "Selective autoimmune demyelination of the spinothalamic tracts", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Progressive demyelination and degeneration of dorsal roots and dorsal columns (fasciculus gracilis and cuneatus).\n\nTabes dorsalis is a late manifestation of tertiary neurosyphilis (Treponema pallidum infection). Pathogenesis:\n• Progressive spirochetal destruction, chronic inflammation, and demyelination of dorsal nerve roots and the dorsal columns (fasciculus gracilis and cuneatus) of the spinal cord.\nClinical presentation:\n• Impaired vibration and conscious proprioception -> sensory ataxia (high-stepping, stomping gait, positive Romberg sign).\n• Loss of deep tendon reflexes (hyporeflexia/areflexia).\n• Severe, paroxysmal, lancinating (lightning) pains in the limbs.\n• Argyll Robertson pupils ('Prostitute's pupil': Accommodates to near vision but does not React to light).\n• Charcot (neuropathic) arthropathy due to loss of joint position sense."
    },
    {
        "id": "FZ_Q128",
        "question_number": 128,
        "category": "Tactile Pathway",
        "stem": "A 62-year-old woman with a history of Crohn disease and ileal resection presents with progressive tingling in her feet, unsteadiness when walking, and cognitive slowing. Physical examination reveals spastic paraparesis in both lower extremities, brisk 3+ patellar reflexes, bilateral extensor plantar responses (positive Babinski sign), and profound loss of vibration and joint position sense in both feet and shins. Pain and temperature sensation are normal. Laboratory testing reveals megaloblastic anemia with elevated serum methylmalonic acid and homocysteine levels. Degeneration of which of the following spinal cord white matter tracts occurs in subacute combined degeneration (SCD)?",
        "options": [
            {"text": "Dorsal columns and lateral corticospinal tracts", "is_correct": True},
            {"text": "Anterolateral spinothalamic tracts and anterior horn motor neurons", "is_correct": False},
            {"text": "Anterior white commissure alone", "is_correct": False},
            {"text": "Ventral corticospinal tracts and rubrospinal tracts", "is_correct": False},
            {"text": "Spinothalamic tracts and anterior corticospinal tracts", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Dorsal columns and lateral corticospinal tracts.\n\nSubacute combined degeneration (SCD) is caused by Vitamin B12 (cobalamin) deficiency (marked by elevated methylmalonic acid and homocysteine, unlike folate deficiency which elevates homocysteine only). Impaired myelin maintenance results in bilateral, symmetrical vacuolar demyelination of:\n1. Dorsal columns (fasciculus gracilis and cuneatus): Loss of vibration and conscious proprioception, sensory ataxia, positive Romberg test.\n2. Lateral corticospinal tracts: Upper motor neuron signs (spastic paraparesis, hyperreflexia, positive Babinski signs).\n3. Spinocerebellar tracts: Limb ataxia.\nPain and temperature sensations are typically spared."
    },
    {
        "id": "FZ_Q129",
        "question_number": 129,
        "category": "Tactile Pathway",
        "stem": "A 70-year-old man undergoes sensory testing. The neurologist uses an aesthesiometer (two-point discriminator) to touch the skin simultaneously at two points. On the patient's fingertips, he can reliably distinguish two distinct points separated by only 2 to 3 mm. However, on his upper back, he cannot perceive two points until they are separated by more than 40 mm. Which of the following neuroanatomical principles explains this dramatic difference in tactile spatial resolution?",
        "options": [
            {"text": "Fingertips have a much higher density of mechanoreceptors with small receptive fields, and disproportionately large cortical representation on the primary somatosensory homunculus", "is_correct": True},
            {"text": "The back has only unmyelinated C fibers that transmit discriminative touch", "is_correct": False},
            {"text": "Mechanoreceptors on the back bypass the thalamus and project directly to the insula", "is_correct": False},
            {"text": "Fingertip sensory fibers do not decussate in the medulla", "is_correct": False},
            {"text": "The fasciculus gracilis carries fibers from the fingertips with faster conduction velocities", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Fingertips have a much higher density of mechanoreceptors with small receptive fields, and disproportionately large cortical representation on the primary somatosensory homunculus.\n\nTwo-point discrimination threshold is determined by two factors:\n1. Peripheral receptor density and receptive field size: The fingertips and lips possess an exceptionally high density of Merkel discs and Meissner corpuscles, each with tiny receptive fields (<2-3 mm) and minimal overlap. The back has sparse mechanoreceptors with large receptive fields (>40 mm).\n2. Central cortical magnification: In the primary somatosensory cortex (postcentral gyrus), the somatotopic homunculus is non-linear: body regions with high receptor density (fingers, hands, lips, tongue) occupy disproportionately vast areas of cortical processing tissue."
    },
    {
        "id": "FZ_Q130",
        "question_number": 130,
        "category": "Tactile Pathway",
        "stem": "A 61-year-old man presents with sudden loss of sensation over the entire left side of his body, including his face, arm, trunk, and leg. Testing demonstrates complete loss of discriminative touch, vibration, joint position sense, and pinprick sensation on the left, with no motor weakness. A head MRI reveals a small lacunar stroke in the thalamus. In which of the following thalamic nuclei do third-order sensory neurons of the DCML and spinothalamic pathways (from the body) synapse?",
        "options": [
            {"text": "Ventral posterolateral (VPL) nucleus", "is_correct": True},
            {"text": "Ventral posteromedial (VPM) nucleus", "is_correct": False},
            {"text": "Lateral geniculate nucleus (LGN)", "is_correct": False},
            {"text": "Medial geniculate nucleus (MGN)", "is_correct": False},
            {"text": "Ventral anterior (VA) nucleus", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Ventral posterolateral (VPL) nucleus.\n\nThe Ventral Posterolateral (VPL) nucleus of the thalamus receives ascending second-order sensory fibers from the body:\n• Medial lemniscus (DCML: vibration, proprioception, fine touch).\n• Spinothalamic tract (ALS: pain and temperature).\nVPL third-order neurons project via the posterior limb of the internal capsule to the primary somatosensory cortex.\n\n• Option B is incorrect: The Ventral Posteromedial (VPM) nucleus receives trigeminal sensory inputs from the FACE ('VPM = Make-up on face; VPL = Legs/body').\n• Option C is incorrect: LGN relays vision (Light).\n• Option D is incorrect: MGN relays hearing (Music)."
    },
    {
        "id": "FZ_Q131",
        "question_number": 131,
        "category": "Tactile Pathway",
        "stem": "In the brainstem, second-order axons of the DCML pathway ascend as the medial lemniscus. How are body parts somatotopically organized within the medial lemniscus as it traverses the medulla oblongata compared to the midbrain?",
        "options": [
            {"text": "In the medulla, lower extremity fibers are situated ventrally; as the tract ascends to the pons and midbrain, lower extremity fibers rotate to a lateral position", "is_correct": True},
            {"text": "Upper extremity fibers are situated medially throughout the entire brainstem", "is_correct": False},
            {"text": "Facial sensory fibers run within the medial lemniscus", "is_correct": False},
            {"text": "Lower extremity fibers are situated dorsally in the medulla and medially in the midbrain", "is_correct": False},
            {"text": "There is no somatotopic arrangement within brainstem white matter tracts", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. In the medulla, lower extremity fibers are situated ventrally; as the tract ascends to the pons and midbrain, lower extremity fibers rotate to a lateral position.\n\nSomatotopy of the Medial Lemniscus:\n• In the rostral medulla: The medial lemniscus is vertically oriented along the midline. Fibers representing the lower body (from nucleus gracilis) lie ventrally (adjacent to the pyramids), while upper body fibers (from nucleus cuneatus) lie dorsally ('standing upright on the pyramids').\n• In the pons and midbrain: The medial lemniscus rotates into a horizontal ribbon. Lower body fibers shift laterally, while upper body fibers shift medially ('reclining on the tegmentum').\nThis ensures that as fibers enter the thalamus, lower extremity fibers enter lateral VPL and upper extremity fibers enter medial VPL."
    },
    {
        "id": "FZ_Q132",
        "question_number": 132,
        "category": "Tactile Pathway",
        "stem": "Which of the following slowly adapting (type 2) encapsulated mechanoreceptors, located deep within the dermis and joint capsules, responds maximally to sustained lateral skin stretch and joint rotation, playing a key role in perceiving finger position and hand conformation?",
        "options": [
            {"text": "Ruffini endings (corpuscles)", "is_correct": True},
            {"text": "Meissner corpuscles", "is_correct": False},
            {"text": "Pacinian corpuscles", "is_correct": False},
            {"text": "Merkel discs", "is_correct": False},
            {"text": "Free nerve endings", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Ruffini endings (corpuscles).\n\nRuffini endings (slowly adapting type 2 mechanoreceptors) are spindle-shaped, encapsulated structures located deep within the reticular dermis, subcutaneous tissue, and fibrous joint capsules. They consist of branched nerve terminals intertwined with bundles of collagen fibers. When skin is stretched laterally or a joint rotates, the collagen fibers tighten and squeeze the nerve endings. Because they adapt slowly, they fire continuously to signal directional skin stretch, finger conformation, and joint kinematics."
    },
    {
        "id": "FZ_Q133",
        "question_number": 133,
        "category": "Tactile Pathway",
        "stem": "A 38-year-old woman with multiple sclerosis presents with a newly developed 'numb, clumsy hand.' Neurological examination reveals normal motor strength and normal light touch perception. However, when an object (such as a key or a coin) is placed into her right hand with her eyes closed, she cannot recognize or name the object by touch alone (astereognosis). She also cannot identify numbers traced on her right palm (agraphesthesia). This deficit (tactile agnosia) localizes to which of the following cortical structures?",
        "options": [
            {"text": "Contralateral primary somatosensory and somatosensory association cortex (parietal lobe)", "is_correct": True},
            {"text": "Ipsilateral motor cortex (precentral gyrus)", "is_correct": False},
            {"text": "Occipital primary visual cortex (calcarine sulcus)", "is_correct": False},
            {"text": "Anterior cingulate gyrus", "is_correct": False},
            {"text": "Superior temporal gyrus (Wernicke area)", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Contralateral primary somatosensory and somatosensory association cortex (parietal lobe).\n\nAstereognosis (inability to identify an object by touch alone) and agraphesthesia (inability to identify numbers traced on the skin) are complex cortical sensory modalities (discriminative cortical sensation). While basic tactile sensation requires an intact peripheral nerve, DCML tract, and VPL thalamus, the higher-order synthesis of texture, shape, size, and weight requires the primary somatosensory cortex (postcentral gyrus, Brodmann areas 3, 1, 2) and the posterior parietal association cortex (Brodmann areas 5 and 7) of the contralateral hemisphere."
    },
    {
        "id": "FZ_Q134",
        "question_number": 134,
        "category": "Tactile Pathway",
        "stem": "Primary somatosensory afferent fibers conveying touch and vibration from peripheral receptors are classified according to the Erlanger-Gasser nerve fiber classification system. Which of the following nerve fiber types mediates fine discriminative touch, vibration, and conscious proprioception?",
        "options": [
            {"text": "A-alpha and A-beta fibers (large diameter, heavily myelinated, fast conduction velocity)", "is_correct": True},
            {"text": "A-delta fibers (small diameter, thinly myelinated)", "is_correct": False},
            {"text": "C fibers (unmyelinated, slowest conduction velocity)", "is_correct": False},
            {"text": "B fibers (preganglionic autonomic)", "is_correct": False},
            {"text": "Gamma motor fibers", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. A-alpha and A-beta fibers (large diameter, heavily myelinated, fast conduction velocity).\n\nNerve fiber classification:\n• A-alpha fibers (Group I): Largest diameter (13-20 um), heavily myelinated, fastest conduction (80-120 m/s); convey proprioception from muscle spindles (Ia) and Golgi tendon organs (Ib).\n• A-beta fibers (Group II): Large diameter (6-12 um), heavily myelinated (35-75 m/s); convey fine discriminative touch, vibration, and pressure from cutaneous mechanoreceptors (Meissner, Pacinian, Merkel, Ruffini).\n• A-delta fibers (Group III): Small diameter (1-5 um), thinly myelinated (5-30 m/s); convey fast, sharp pain and cold temperature.\n• C fibers (Group IV): Smallest diameter (0.2-1.5 um), unmyelinated, slowest conduction (0.5-2 m/s); convey slow, burning/dull pain, warm temperature, and itch."
    },
    {
        "id": "FZ_Q135",
        "question_number": 135,
        "category": "Tactile Pathway",
        "stem": "A 50-year-old man undergoes neurological testing. A tuning fork vibrating at 128 Hz is placed over his right medial malleolus. Sensation is perceived normally. In the dorsal column of the spinal cord, where is the fasciculus gracilis located relative to the fasciculus cuneatus?",
        "options": [
            {"text": "Medial to the fasciculus cuneatus", "is_correct": True},
            {"text": "Lateral to the fasciculus cuneatus", "is_correct": False},
            {"text": "Anterior to the anterior horn", "is_correct": False},
            {"text": "Within the lateral funiculus", "is_correct": False},
            {"text": "Inside the central canal", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Medial to the fasciculus cuneatus.\n\nIn the dorsal funiculus of the spinal cord:\n• Fasciculus gracilis occupies the medial portion, immediately adjacent to the posterior median septum. It carries ascending fibers from lower sacral, lumbar, and lower thoracic levels (T7 and below).\n• Fasciculus cuneatus is added laterally as upper thoracic and cervical roots enter the cord (T6 and above). Therefore, cuneatus lies lateral to gracilis.\nAt cervical spinal cord levels, the dorsal column contains both tracts (gracilis medially, cuneatus laterally)."
    },
    {
        "id": "FZ_Q136",
        "question_number": 136,
        "category": "Tactile Pathway",
        "stem": "A 45-year-old woman presents with numbness in her left arm. Testing shows impaired vibration and proprioception in her left fingers and wrist, with normal sensation in her legs. A focal demyelinating plaque in the cervical spinal cord is suspected. Which of the following tracts in the left cervical posterior funiculus is damaged?",
        "options": [
            {"text": "Left fasciculus cuneatus", "is_correct": True},
            {"text": "Left fasciculus gracilis", "is_correct": False},
            {"text": "Right fasciculus gracilis", "is_correct": False},
            {"text": "Left spinothalamic tract", "is_correct": False},
            {"text": "Right spinothalamic tract", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Left fasciculus cuneatus.\n\nSensory fibers from the upper extremity (C2-T6) enter the spinal cord and ascend ipsilaterally in the fasciculus cuneatus (the lateral subdivision of the dorsal column). Because the fibers have not yet reached the caudal medulla, they have not decussated; therefore, a lesion in the left fasciculus cuneatus produces IPSILATERAL loss of vibration, fine touch, and conscious proprioception in the left upper extremity.\n\n• Option B is incorrect: Left fasciculus gracilis carries fibers from the left lower extremity."
    },
    {
        "id": "FZ_Q137",
        "question_number": 137,
        "category": "Tactile Pathway",
        "stem": "Which of the following sensory structures acts as a specialized proprioceptor embedded in parallel with skeletal muscle extrafusal fibers, detecting changes in muscle length (stretch) to mediate the monosynaptic deep tendon reflex?",
        "options": [
            {"text": "Muscle spindle (intrafusal muscle fibers innervated by Group Ia sensory afferents)", "is_correct": True},
            {"text": "Golgi tendon organ (innervated by Group Ib sensory afferents)", "is_correct": False},
            {"text": "Pacinian corpuscle", "is_correct": False},
            {"text": "Ruffini ending", "is_correct": False},
            {"text": "Free nerve ending", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Muscle spindle (intrafusal muscle fibers innervated by Group Ia sensory afferents).\n\nMuscle spindles are specialized stretch receptors encapsulated in parallel with skeletal muscle extrafusal fibers. They consist of intrafusal fibers (nuclear bag and chain fibers) innervated by Group Ia sensory afferents (detecting rate of stretch) and Group II afferents (detecting static length). Tapping a tendon stretches the muscle spindle, activating Ia afferents that enter the spinal cord and monosynaptically excite alpha motor neurons to cause reflexive contraction (the myotatic / deep tendon reflex). Gamma motor neurons adjust the sensitivity of the spindle.\n\n• Option B is incorrect: Golgi tendon organs are arranged in SERIES at the musculotendinous junction, innervated by Group Ib afferents, and sense muscle TENSION (mediating the inverse myotatic reflex)."
    },
    {
        "id": "FZ_Q138",
        "question_number": 138,
        "category": "Tactile Pathway",
        "stem": "A neurophysiologist investigates the inverse myotatic reflex (autogenic inhibition). When a muscle generates extreme contractile force, this proprioceptive receptor activates Group Ib afferents that synapse on inhibitory interneurons in the spinal cord, relaxing the contracting muscle to prevent tendon avulsion. Which receptor is responsible?",
        "options": [
            {"text": "Golgi tendon organ (GTO)", "is_correct": True},
            {"text": "Muscle spindle", "is_correct": False},
            {"text": "Meissner corpuscle", "is_correct": False},
            {"text": "Pacinian corpuscle", "is_correct": False},
            {"text": "Merkel disc", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Golgi tendon organ (GTO).\n\nGolgi tendon organs (GTOs) are encapsulated sensory receptors arranged in SERIES with extrafusal muscle fibers at the musculotendinous junction. They are innervated by fast Group Ib sensory axons. GTOs are exquisitely sensitive to changes in muscle TENSION (contractile force). When excessive contraction threatens to tear the tendon, GTO firing activates Ib inhibitory interneurons in the spinal cord, which inhibit alpha motor neurons to the homonymous muscle, causing it to relax (the inverse myotatic reflex / autogenic inhibition)."
    },
    {
        "id": "FZ_Q139",
        "question_number": 139,
        "category": "Tactile Pathway",
        "stem": "A 75-year-old man presents with chronic sensory loss in his feet. Examination reveals loss of vibratory perception up to his mid-shins, with preserved pinprick sensation. Which of the following tuning forks is the standard clinical instrument used to evaluate vibratory threshold in the dorsal column pathway?",
        "options": [
            {"text": "128-Hz tuning fork", "is_correct": True},
            {"text": "512-Hz tuning fork", "is_correct": False},
            {"text": "1024-Hz tuning fork", "is_correct": False},
            {"text": "2048-Hz tuning fork", "is_correct": False},
            {"text": "4096-Hz tuning fork", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. 128-Hz tuning fork.\n\nA 128-Hz tuning fork is the standard instrument for assessing vibratory sense in a neurological examination. Vibratory sense is mediated by Pacinian corpuscles and transmitted via large myelinated A-beta fibers in the DCML pathway. Vibratory sensation is typically the earliest sensory modality lost in peripheral neuropathies (e.g., diabetic neuropathy) and subacute combined degeneration.\n\n• Option B is incorrect: A 512-Hz tuning fork is used for auditory acuity testing (Rinne and Weber tests)."
    },
    {
        "id": "FZ_Q140",
        "question_number": 140,
        "category": "Tactile Pathway",
        "stem": "A 58-year-old woman with a subacute brainstem stroke exhibits loss of vibration, fine touch, and proprioception over the entire right side of her body (arms and legs), with completely normal facial sensation and normal pain and temperature sensation throughout. A discrete ischemic lesion in which of the following brainstem structures on the left side explains this isolated deficit?",
        "options": [
            {"text": "Medial lemniscus in the left pons", "is_correct": True},
            {"text": "Spinal trigeminal tract in the left medulla", "is_correct": False},
            {"text": "Spinothalamic tract in the right medulla", "is_correct": False},
            {"text": "Left corticospinal tract in the crus cerebri", "is_correct": False},
            {"text": "Right inferior cerebellar peduncle", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Medial lemniscus in the left pons.\n\nThe medial lemniscus contains second-order axons from the contralateral nucleus gracilis and cuneatus that have already decussated in the caudal medulla. As it ascends through the pons and midbrain, it carries discriminative touch, vibration, and proprioception from the contralateral hemibody (right side). Because trigeminal sensory fibers (from the face) ascend separately in the trigeminothalamic tract and spinothalamic fibers (pain/temp) ascend laterally, an isolated lesion of the left medial lemniscus in the pons causes contralateral (right-sided) loss of touch/vibration/proprioception while sparing facial sensation and pain/temperature."
    },

    # =========================================================================
    # TOPIC 8: Spinal Cord (FZ_Q141 - FZ_Q160)
    # =========================================================================
    {
        "id": "FZ_Q141",
        "question_number": 141,
        "category": "Spinal Cord",
        "stem": "A 24-year-old man is brought to the trauma bay after being stabbed in the right thoracic back. Neurological examination reveals right-sided spastic paralysis of his leg with hyperreflexia and a positive Babinski sign, right-sided loss of vibratory sense and joint position sense below the level of the umbilicus, and left-sided loss of pain and temperature sensation starting at the level of the groin (L1). What is the name of this spinal cord hemisection syndrome?",
        "options": [
            {"text": "Brown-Séquard syndrome", "is_correct": True},
            {"text": "Anterior spinal artery syndrome", "is_correct": False},
            {"text": "Central cord syndrome", "is_correct": False},
            {"text": "Cauda equina syndrome", "is_correct": False},
            {"text": "Tabes dorsalis", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Brown-Séquard syndrome.\n\nBrown-Séquard syndrome results from hemisection of the spinal cord (e.g., from penetrating trauma). The neurological findings reflect the decussation patterns of spinal tracts:\n1. Ipsilateral UMN weakness below the lesion (due to transection of the uncrossed descending lateral corticospinal tract).\n2. Ipsilateral loss of vibration, fine touch, and proprioception below the lesion (due to transection of the uncrossed ascending dorsal columns).\n3. Contralateral loss of pain and temperature sensation starting 1 to 2 segments below the lesion (due to transection of the ascending spinothalamic tract, whose fibers cross the anterior white commissure 1-2 segments above their entry level).\n4. Complete ipsilateral sensory loss and flaccid LMN paralysis at the level of the lesion (destruction of local dorsal and ventral horn cells)."
    },
    {
        "id": "FZ_Q142",
        "question_number": 142,
        "category": "Spinal Cord",
        "stem": "A 68-year-old man undergoes surgical repair of a large thoracoabdominal aortic aneurysm. Postoperatively, he is noted to have complete flaccid paralysis of both lower extremities with absent deep tendon reflexes, urinary retention, and bilateral loss of pain and temperature sensation below the T10 dermatome. Remarkably, his vibratory sensation and conscious proprioception in both feet and legs are completely normal. Ischemia of which of the following arterial vessels is responsible for this anterior spinal artery syndrome?",
        "options": [
            {"text": "Artery of Adamkiewicz (great anterior radiculomedullary artery)", "is_correct": True},
            {"text": "Posterior spinal arteries", "is_correct": False},
            {"text": "Vertebral arteries at the foramen magnum", "is_correct": False},
            {"text": "Ascending pharyngeal artery", "is_correct": False},
            {"text": "Posterior inferior cerebellar artery", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Artery of Adamkiewicz (great anterior radiculomedullary artery).\n\nAnterior spinal artery syndrome (Beck syndrome) results from infarction of the anterior two-thirds of the spinal cord. In the lower thoracic and lumbosacral cord, the single anterior spinal artery depends heavily on radicular feeding arteries, most notably the Artery of Adamkiewicz (great anterior radiculomedullary artery), which typically arises from a left posterior intercostal or lumbar artery between T9 and T12. Clamping or resection during thoracic/abdominal aortic aneurysm surgery can precipitate ischemia of the anterior 2/3 of the cord. Hallmarks:\n• Bilateral corticospinal tract infarction: Spastic paraplegia.\n• Bilateral spinothalamic tract infarction: Loss of pain and temperature below the lesion.\n• Bilateral anterior horn destruction: LMN signs at the level, urinary retention.\n• Sparing of dorsal columns: Vibration and proprioception remain completely intact because the posterior 1/3 of the cord is perfused by the paired posterior spinal arteries."
    },
    {
        "id": "FZ_Q143",
        "question_number": 143,
        "category": "Spinal Cord",
        "stem": "A 72-year-old man with severe cervical spondylosis is involved in a rear-end motor vehicle collision, suffering a hyperextension injury to his neck. Physical examination demonstrates marked weakness and flaccidity in his arms and hands (1/5 strength), while his legs exhibit only mild weakness (4/5 strength). He also has patchy sensory loss over his shoulders and arms. Brain and spine MRI demonstrates acute contusion centered in the middle of the cervical spinal cord. Which of the following syndromes is present?",
        "options": [
            {"text": "Central cord syndrome", "is_correct": True},
            {"text": "Brown-Séquard syndrome", "is_correct": False},
            {"text": "Anterior cord syndrome", "is_correct": False},
            {"text": "Posterior cord syndrome", "is_correct": False},
            {"text": "Conus medullaris syndrome", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Central cord syndrome.\n\nCentral cord syndrome is the most common incomplete spinal cord injury syndrome. It characteristically occurs in elderly patients with pre-existing cervical spondylosis and canal stenosis who suffer a hyperextension injury to the neck. The center of the cervical spinal cord is contused. Hallmarks:\n• Disproportionately greater motor impairment in the UPPER extremities than in the lower extremities. In the lateral corticospinal tract, fibers are organized somatotopically from medial to lateral: Cervical fibers are located medially (closest to the central canal), while lumbar/sacral fibers are situated laterally. A central lesion damages the medial cervical hand/arm fibers first.\n• Patchy sensory loss in the upper extremities due to disruption of decussating spinothalamic fibers."
    },
    {
        "id": "FZ_Q144",
        "question_number": 144,
        "category": "Spinal Cord",
        "stem": "A 56-year-old man presents with progressive muscle weakness and fasciculations. Physical examination reveals atrophy and fasciculations of the tongue, wasting of the intrinsic muscles of the hands, brisk 3+ biceps and patellar reflexes, spasticity in the legs, and bilateral extensor plantar responses (positive Babinski signs). Sensation to pinprick, vibration, and temperature is completely normal, and bowel and bladder sphincter control is preserved. Denervation and loss of both upper and lower motor neurons characterizes which of the following fatal neurodegenerative diseases?",
        "options": [
            {"text": "Amyotrophic lateral sclerosis (ALS)", "is_correct": True},
            {"text": "Poliomyelitis", "is_correct": False},
            {"text": "Multiple sclerosis", "is_correct": False},
            {"text": "Werdnig-Hoffmann disease", "is_correct": False},
            {"text": "Guillain-Barré syndrome", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Amyotrophic lateral sclerosis (ALS).\n\nAmyotrophic lateral sclerosis (ALS / Lou Gehrig disease) is a progressive neurodegenerative disease characterized by the combined degeneration of both Upper Motor Neurons (UMNs: Betz cells in the motor cortex, corticospinal tracts) and Lower Motor Neurons (LMNs: cranial nerve motor nuclei in the brainstem and anterior horn alpha motor neurons in the spinal cord).\n• LMN signs: Muscle atrophy, fasciculations, flaccid weakness.\n• UMN signs: Spasticity, hyperreflexia, positive Babinski sign, pseudobulbar affect.\n• Pure motor disorder: Sensory, autonomic, and sphincter functions are characteristically spared.\n• Associated with mutations in SOD1 (superoxide dismutase 1), C9orf72 hexanucleotide repeat expansions, and cytoplasmic TDP-43 inclusions. Pharmacotherapy includes riluzole (glutamate release inhibitor) and edaravone."
    },
    {
        "id": "FZ_Q145",
        "question_number": 145,
        "category": "Spinal Cord",
        "stem": "A 48-year-old woman with chronic back pain suddenly develops severe low back pain, numbness in her perineum and buttocks ('saddle anesthesia'), bilateral asymmetric leg weakness, and overflow urinary incontinence. Physical examination reveals absent Achilles tendon reflexes bilaterally and poor anal sphincter tone. Emergency lumbar spine MRI reveals a massive herniated L4-L5 intervertebral disc compressing multiple lumbosacral nerve roots. Compression of which of the following anatomical structures defines cauda equina syndrome?",
        "options": [
            {"text": "Lumbosacral nerve roots in the lumbar cistern below the termination of the conus medullaris (L2)", "is_correct": True},
            {"text": "Sacral spinal cord segments S1 to S5 within the conus medullaris", "is_correct": False},
            {"text": "Thoracic spinal cord white matter at the T10 level", "is_correct": False},
            {"text": "Filum terminale internum alone", "is_correct": False},
            {"text": "Denticulate ligaments of the cervical dura", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Lumbosacral nerve roots in the lumbar cistern below the termination of the conus medullaris (L2).\n\nCauda equina syndrome is a neurosurgical emergency caused by compression of the cauda equina (the collection of intradural lumbosacral nerve roots L2 through S5 descending through the lumbar cistern below the termination of the conus medullaris at L1-L2). Causes include massive midline disc herniation, spinal canal stenosis, trauma, or epidural tumors. Clinical hallmarks:\n• Severe radicular pain shooting into the legs.\n• Asymmetric flaccid paraparesis of the lower extremities with hyporeflexia/areflexia (pure LMN lesion, since nerve roots are peripheral nerves).\n• 'Saddle anesthesia' (sensory loss in dermatomes S3-S5: perineum, perianal, buttocks, inner thighs).\n• Bowel and bladder dysfunction: Urinary retention with overflow incontinence and decreased anal sphincter tone.\nImmediate surgical decompression is required to prevent permanent paraplegia and incontinence."
    },
    {
        "id": "FZ_Q146",
        "question_number": 146,
        "category": "Spinal Cord",
        "stem": "A 35-year-old man presents with sudden urinary and fecal incontinence. Neurological examination reveals bilateral, symmetrical perianal numbness (S3-S5), preserved patellar and Achilles reflexes with extensor plantar responses (positive Babinski signs), and mild, symmetrical leg weakness. In distinguishing this from cauda equina syndrome, the physician recognizes conus medullaris syndrome. At which of the following vertebral levels is the conus medullaris normally situated in an adult?",
        "options": [
            {"text": "L1-L2 vertebral disc space", "is_correct": True},
            {"text": "T8-T9 vertebral disc space", "is_correct": False},
            {"text": "L4-L5 vertebral disc space", "is_correct": False},
            {"text": "S1-S2 sacral level", "is_correct": False},
            {"text": "C7-T1 vertebral disc space", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. L1-L2 vertebral disc space.\n\nThe conus medullaris is the tapered caudal termination of the spinal cord, located at the L1-L2 vertebral level in adults. \n• Conus medullaris syndrome results from injury to the sacral cord segments and conus (at L1-L2). It is characterized by sudden, early, severe bilateral bladder and bowel incontinence, bilateral symmetrical saddle numbness (perianal), and mixed UMN (hyperreflexia, Babinski) and LMN signs.\n• Cauda equina syndrome, by contrast, is compression of nerve roots below L2, resulting in asymmetric radicular pain, flaccid LMN weakness, hyporeflexia, and later-onset incontinence."
    },
    {
        "id": "FZ_Q147",
        "question_number": 147,
        "category": "Spinal Cord",
        "stem": "An anesthesiologist performs a diagnostic lumbar puncture on an adult patient. The needle is inserted in the midline at the L3-L4 intervertebral space, guided by the supracristal plane (Tuffier line connecting the superior borders of the iliac crests). As the needle advances, it encounters a sudden release of resistance ('pop') as it traverses which of the following ligaments immediately before entering the epidural space?",
        "options": [
            {"text": "Ligamentum flavum", "is_correct": True},
            {"text": "Supraspinous ligament", "is_correct": False},
            {"text": "Interspinous ligament", "is_correct": False},
            {"text": "Posterior longitudinal ligament", "is_correct": False},
            {"text": "Anterior longitudinal ligament", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Ligamentum flavum.\n\nLayers traversed during a lumbar puncture (from superficial to deep):\n1. Skin\n2. Subcutaneous tissue\n3. Supraspinous ligament (connects tips of spinous processes)\n4. Interspinous ligament (connects adjacent spinous processes)\n5. Ligamentum flavum (dense, yellow elastic ligament connecting laminae; gives a characteristic tactile 'pop' as the needle pierces it)\n6. Epidural space (contains internal vertebral venous plexus and fat)\n7. Dura mater ('second pop')\n8. Arachnoid mater\n9. Subarachnoid space (contains CSF and cauda equina nerve roots)."
    },
    {
        "id": "FZ_Q148",
        "question_number": 148,
        "category": "Spinal Cord",
        "stem": "A 30-year-old woman presents with band-like numbness around her abdomen at the level of her umbilicus. Sensory mapping confirms loss of pinprick and light touch sensation across a circular dermatome that corresponds precisely to the umbilicus. Which of the following spinal nerves innervates this landmark dermatome?",
        "options": [
            {"text": "T10 spinal nerve", "is_correct": True},
            {"text": "T4 spinal nerve", "is_correct": False},
            {"text": "T7 spinal nerve", "is_correct": False},
            {"text": "L1 spinal nerve", "is_correct": False},
            {"text": "C6 spinal nerve", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. T10 spinal nerve.\n\nKey landmark dermatomes:\n• C2: Occiput / back of head\n• C3: High neck\n• C4: Low neck / supraclavicular\n• C6: Thumb ('six-shooter')\n• C7: Middle finger\n• C8: Pinky finger (little finger)\n• T4: Nipples ('T4 at the teat-pore')\n• T7: Xiphoid process\n• T10: Umbilicus ('belly-but-TEN')\n• L1: Inguinal ligament / groin\n• L4: Patella / knee\n• L5: Big toe / dorsum of foot\n• S1: Little toe / lateral foot / Achilles\n• S2-S4: Perineum / saddle area ('sits on S2-S4')."
    },
    {
        "id": "FZ_Q149",
        "question_number": 149,
        "category": "Spinal Cord",
        "stem": "A 42-year-old man presents with sharp, shooting pain radiating down his right leg to the lateral border of his foot and little toe. Neurological examination reveals an absent right Achilles tendon (ankle-jerk) reflex and weakness when asked to walk on his tiptoes (plantarflexion of the foot). Sensation to pinprick is diminished over the lateral foot and sole. Herniation of the intervertebral disc compressing which of the following nerve roots is responsible?",
        "options": [
            {"text": "S1 nerve root (L5-S1 disc herniation)", "is_correct": True},
            {"text": "L4 nerve root (L3-L4 disc herniation)", "is_correct": False},
            {"text": "L5 nerve root (L4-L5 disc herniation)", "is_correct": False},
            {"text": "S3 nerve root (S2-S3 disc herniation)", "is_correct": False},
            {"text": "L2 nerve root (L1-L2 disc herniation)", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. S1 nerve root (L5-S1 disc herniation).\n\nLumbosacral radiculopathies:\n• S1 radiculopathy (typically L5-S1 disc herniation): Pain and sensory loss along the posterior leg, lateral malleolus, and little toe. Motor weakness in plantarflexion (gastrocnemius/soleus, inability to walk on toes). Absent Achilles tendon reflex (S1-S2: 'ankle jerk').\n• L5 radiculopathy (L4-L5 disc): Pain and sensory loss on the lateral leg and dorsum of the foot / big toe. Weakness in foot dorsiflexion and big toe extension (extensor hallucis longus, difficulty heel-walking). Reflexes are typically normal.\n• L4 radiculopathy (L3-L4 disc): Pain and sensory loss across the anterior knee and medial lower leg. Weakness in knee extension (quadriceps). Diminished patellar reflex (L3-L4)."
    },
    {
        "id": "FZ_Q150",
        "question_number": 150,
        "category": "Spinal Cord",
        "stem": "A 50-year-old carpenter presents with shooting pain from his neck down his right arm into his thumb and index finger. Neurological examination reveals weakness during forearm flexion and supination, and his right brachioradialis reflex is completely absent. Sensory testing demonstrates loss of sensation over the lateral forearm, thumb, and index finger. Compression of which of the following cervical spinal nerve roots is responsible?",
        "options": [
            {"text": "C6 nerve root", "is_correct": True},
            {"text": "C5 nerve root", "is_correct": False},
            {"text": "C7 nerve root", "is_correct": False},
            {"text": "C8 nerve root", "is_correct": False},
            {"text": "T1 nerve root", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. C6 nerve root.\n\nCervical radiculopathies:\n• C6 radiculopathy (C5-C6 disc herniation): Radiating pain and sensory loss over the lateral forearm, thumb, and index finger. Motor weakness of biceps and brachioradialis (forearm flexion and wrist extension). Diminished brachioradialis and biceps reflexes.\n• C5 radiculopathy: Deltoid weakness (arm abduction), sensory loss over lateral shoulder. Diminished biceps reflex.\n• C7 radiculopathy: Triceps weakness (elbow extension), sensory loss over middle finger. Diminished triceps reflex.\n• C8 radiculopathy: Weakness of intrinsic hand muscles, sensory loss over little finger (pinky). Normal reflexes."
    },
    {
        "id": "FZ_Q151",
        "question_number": 151,
        "category": "Spinal Cord",
        "stem": "A 3-month-old infant is brought to the clinic because of generalized weakness and poor motor development. On physical examination, the infant is hypotonic, lies in a 'frog-leg' posture, and has tongue fasciculations and symmetric flaccid paralysis with absent deep tendon reflexes. Sensation is intact and mental status is normal. Genetic testing reveals a homozygous deletion of the SMN1 (survival motor neuron) gene on chromosome 5q. Degeneration of which of the following spinal cord structures occurs in Spinal Muscular Atrophy (Werdnig-Hoffmann disease)?",
        "options": [
            {"text": "Anterior (ventral) horn alpha motor neurons", "is_correct": True},
            {"text": "Dorsal root ganglia", "is_correct": False},
            {"text": "Lateral spinothalamic tracts", "is_correct": False},
            {"text": "Substantia gelatinosa", "is_correct": False},
            {"text": "Fasciculus cuneatus", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Anterior (ventral) horn alpha motor neurons.\n\nSpinal Muscular Atrophy (SMA Type 1 / Werdnig-Hoffmann disease) is an autosomal recessive disorder caused by homozygous deletion or loss-of-function mutations in the SMN1 gene on chromosome 5q. SMN protein is required for the assembly of spliceosomal snRNPs. Deficiency causes selective degeneration and apoptosis of lower motor neurons in the anterior (ventral) horns of the spinal cord and brainstem motor nuclei. Hallmarks:\n• 'Floppy baby' syndrome with severe generalized hypotonia and symmetric flaccid paralysis.\n• Tongue fasciculations and weak cry/suck.\n• Areflexia.\n• Normal sensation and normal intellect."
    },
    {
        "id": "FZ_Q152",
        "question_number": 152,
        "category": "Spinal Cord",
        "stem": "A 6-year-old unimmunized child living in a region with endemic poliovirus develops fever, headache, vomiting, and stiff neck, followed 4 days later by acute, asymmetric flaccid paralysis of his right lower extremity. Deep tendon reflexes in the right leg are absent, but sensation is entirely normal. Destruction of which of the following cell types by the poliovirus enterovirus causes this pure motor flaccid paralysis?",
        "options": [
            {"text": "Somatic motor neurons of the anterior (ventral) horns", "is_correct": True},
            {"text": "Pseudounipolar neurons of the dorsal root ganglia", "is_correct": False},
            {"text": "Oligodendrocytes in the lateral funiculus", "is_correct": False},
            {"text": "Ependymal cells lining the central canal", "is_correct": False},
            {"text": "Preganglionic sympathetic neurons of the intermediolateral horn", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Somatic motor neurons of the anterior (ventral) horns.\n\nPoliomyelitis is caused by poliovirus (an enterovirus, positive-sense single-stranded RNA virus). After replication in the oropharyngeal and gastrointestinal mucosa and Peyer patches, the virus disseminates hematogenously to the central nervous system. Poliovirus has selective tropism for alpha motor neurons located in the anterior (ventral) horns of the spinal cord and motor nuclei of the brainstem. Lysis of anterior horn cells produces asymmetric flaccid paralysis, muscle atrophy, fasciculations, and areflexia, with completely spared sensory function."
    },
    {
        "id": "FZ_Q153",
        "question_number": 153,
        "category": "Spinal Cord",
        "stem": "An adult human spinal cord contains 31 pairs of spinal nerves. How do the spinal nerves exit the vertebral column relative to their corresponding pedicles in the cervical region compared to the thoracic and lumbar regions?",
        "options": [
            {"text": "Cervical nerves C1-C7 exit ABOVE their corresponding vertebrae; C8 exits between C7 and T1; thoracic and lumbar nerves exit BELOW their corresponding vertebrae", "is_correct": True},
            {"text": "All spinal nerves exit below their corresponding numbered vertebrae", "is_correct": False},
            {"text": "All spinal nerves exit above their corresponding numbered vertebrae", "is_correct": False},
            {"text": "Cervical nerves exit below their vertebrae; thoracic and lumbar nerves exit above", "is_correct": False},
            {"text": "Spinal nerves exit through the anterior longitudinal ligament", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Cervical nerves C1-C7 exit ABOVE their corresponding vertebrae; C8 exits between C7 and T1; thoracic and lumbar nerves exit BELOW their corresponding vertebrae.\n\nAnatomy of spinal nerve exit:\n• There are 7 cervical vertebrae but 8 cervical spinal nerves.\n• Nerves C1 through C7 exit the vertebral canal ABOVE their numerically corresponding vertebrae (e.g., C1 nerve exits above C1 vertebra; C7 nerve exits above C7 vertebra).\n• Nerve C8 exits BELOW the C7 vertebra (between C7 and T1 vertebrae).\n• From T1 downward, every spinal nerve exits BELOW its numerically corresponding vertebra (e.g., T1 nerve exits below T1 vertebra; L4 nerve exits below L4 vertebra)."
    },
    {
        "id": "FZ_Q154",
        "question_number": 154,
        "category": "Spinal Cord",
        "stem": "A 16-year-old boy presents with progressive clumsiness, frequent falls, and difficulty walking. Neurological examination reveals bilateral limb ataxia, loss of vibratory and position sense in both feet, absent deep tendon reflexes, bilateral extensor plantar responses (Babinski sign), and marked pes cavus (high arched feet) with hammer toes. Echocardiogram reveals hypertrophic cardiomyopathy. Genetic testing demonstrates an expanded GAA trinucleotide repeat on chromosome 9q in the frataxin gene. Which of the following conditions is present?",
        "options": [
            {"text": "Friedreich ataxia", "is_correct": True},
            {"text": "Ataxia-telangiectasia", "is_correct": False},
            {"text": "Huntington disease", "is_correct": False},
            {"text": "Spinocerebellar ataxia type 1", "is_correct": False},
            {"text": "Charcot-Marie-Tooth disease", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Friedreich ataxia.\n\nFriedreich ataxia is an autosomal recessive neurodegenerative disorder caused by an expanded GAA trinucleotide repeat in the FXN gene (chromosome 9q), encoding frataxin (an iron-binding mitochondrial protein). Frataxin deficiency leads to iron accumulation, reactive oxygen species, and mitochondrial dysfunction. Degeneration involves:\n• Spinocerebellar tracts: Progressive gait and limb ataxia.\n• Dorsal columns: Loss of vibration and proprioception, areflexia.\n• Lateral corticospinal tracts: Spastic weakness, positive Babinski signs.\n• Peripheral sensory nerves.\nAssociated non-neurological features include hypertrophic cardiomyopathy (leading cause of death in ~50% of patients), diabetes mellitus, and skeletal deformities (pes cavus, kyphoscoliosis)."
    },
    {
        "id": "FZ_Q155",
        "question_number": 155,
        "category": "Spinal Cord",
        "stem": "A 22-year-old man undergoes a routine physical examination. The physician lightly strokes the inner aspect of the patient's upper thigh with a tongue depressor, observing immediate reflexive elevation of the ipsilateral testicle. Which of the following spinal cord segments mediates this normal cremasteric reflex?",
        "options": [
            {"text": "L1-L2 spinal segments", "is_correct": True},
            {"text": "S2-S4 spinal segments", "is_correct": False},
            {"text": "T10-T11 spinal segments", "is_correct": False},
            {"text": "L4-L5 spinal segments", "is_correct": False},
            {"text": "S1-S2 spinal segments", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. L1-L2 spinal segments.\n\nThe cremasteric reflex tests spinal cord segments L1 and L2:\n• Afferent limb: Ilioinguinal nerve (L1) or femoral branch of the genitofemoral nerve detects tactile stimulation of the upper medial thigh.\n• Central integration: L1-L2 spinal cord segments.\n• Efferent limb: Genital branch of the genitofemoral nerve (L1-L2) stimulates contraction of the cremaster muscle, pulling the ipsilateral testis superiorly.\n\n• Option B is incorrect: S2-S4 mediates the anal wink reflex (pudendal nerve) and bulbocavernosus reflex."
    },
    {
        "id": "FZ_Q156",
        "question_number": 156,
        "category": "Spinal Cord",
        "stem": "During a neurological exam, the physician gently strokes the perianal skin with a cotton swab, observing a reflexive contraction of the external anal sphincter muscle (anal wink reflex). Which of the following nerve roots and peripheral nerves mediates this reflex?",
        "options": [
            {"text": "S3-S4 nerve roots via the pudendal nerve", "is_correct": True},
            {"text": "L1-L2 nerve roots via the genitofemoral nerve", "is_correct": False},
            {"text": "L4-L5 nerve roots via the femoral nerve", "is_correct": False},
            {"text": "S1-S2 nerve roots via the tibial nerve", "is_correct": False},
            {"text": "T10-T12 nerve roots via the iliohypogastric nerve", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. S3-S4 nerve roots via the pudendal nerve.\n\nThe anal wink (anal sphincter) reflex evaluates the integrity of the lowest sacral spinal cord segments (S3, S4, and S5):\n• Light scratching of the perianal skin stimulates afferent sensory fibers of the pudendal nerve (S2-S4).\n• Efferent motor fibers travel back via the inferior rectal branch of the pudendal nerve (S3-S4) to cause reflexive contraction of the external anal sphincter.\nLoss of the anal wink reflex indicates a lesion of the sacral spinal cord (conus medullaris) or lumbosacral nerve roots (cauda equina)."
    },
    {
        "id": "FZ_Q157",
        "question_number": 157,
        "category": "Spinal Cord",
        "stem": "A 25-year-old man who sustained a complete spinal cord transection at the T2 level 6 months ago presents to the emergency department with a pounding headache, facial flushing, profuse sweating above the chest, and severe hypertension (220/115 mmHg) accompanied by bradycardia (48 beats/min). The episode was triggered by an obstructed urinary catheter with bladder distension. Which of the following life-threatening conditions is occurring?",
        "options": [
            {"text": "Autonomic dysreflexia (hyperreflexia)", "is_correct": True},
            {"text": "Neurogenic shock", "is_correct": False},
            {"text": "Spinal shock", "is_correct": False},
            {"text": "Malignant hyperthermia", "is_correct": False},
            {"text": "Serotonin syndrome", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Autonomic dysreflexia (hyperreflexia).\n\nAutonomic dysreflexia occurs in patients with chronic spinal cord injuries AT OR ABOVE the T6 level. Mechanism:\n1. Noxious stimulus below the lesion (most commonly bladder distension or fecal impaction) triggers visceral afferents entering the spinal cord.\n2. This evokes massive sympathetic preganglionic output from the splanchnic sympathetic chain (T6-L2).\n3. Intense peripheral vasoconstriction causes severe hypertension.\n4. Carotid and aortic baroreceptors detect hypertension and stimulate the brainstem vagus nerve (CN X), causing reflex bradycardia.\n5. Descending inhibitory signals from the brainstem cannot cross the cord transection (at T2) to turn off sympathetic outflow below the lesion.\nNet result: Profuse vasodilation/flushing/sweating ABOVE the lesion, severe vasoconstriction/goosebumps/pale skin BELOW the lesion, and malignant hypertension."
    },
    {
        "id": "FZ_Q158",
        "question_number": 158,
        "category": "Spinal Cord",
        "stem": "Immediately following an acute traumatic transection of the cervical spinal cord, a patient enters the phase of 'spinal shock.' Which of the following neurological examination findings is characteristically present during acute spinal shock, prior to the eventual emergence of spastic paraplegia?",
        "options": [
            {"text": "Transient flaccid paralysis, complete loss of all sensation, and complete absence of deep tendon and autonomic reflexes below the lesion", "is_correct": True},
            {"text": "Immediate severe hyperreflexia with clonus and clasp-knife spasticity", "is_correct": False},
            {"text": "Isolated loss of pain sensation with intact motor tone", "is_correct": False},
            {"text": "Severe hypertension and hyperthermia", "is_correct": False},
            {"text": "Decerebrate extensor posturing", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Transient flaccid paralysis, complete loss of all sensation, and complete absence of deep tendon and autonomic reflexes below the lesion.\n\nSpinal shock refers to the immediate, transient state of complete loss of spinal cord function distal to an acute spinal cord injury. Despite damage to descending upper motor neuron pathways (which eventually produces spasticity and hyperreflexia weeks later), the acute sudden withdrawal of tonic descending facilitatory input causes spinal neurons to become completely hyperpolarized and unresponsive. Hallmarks of spinal shock:\n• Flaccid paralysis of all muscles below the lesion.\n• Complete areflexia (absent deep tendon reflexes, absent bulbocavernosus and anal wink reflexes).\n• Loss of autonomic vasomotor tone (hypotension/bradycardia = neurogenic shock).\nAs spinal neurons develop denervation supersensitivity over weeks, reflexes return and transition to chronic spasticity."
    },
    {
        "id": "FZ_Q159",
        "question_number": 159,
        "category": "Spinal Cord",
        "stem": "In the spinal cord, preganglionic sympathetic autonomic neurons originate in the intermediolateral cell column (IML). Across which of the following spinal cord segments is the intermediolateral cell column anatomically present?",
        "options": [
            {"text": "T1 to L2 spinal segments", "is_correct": True},
            {"text": "C1 to C8 spinal segments", "is_correct": False},
            {"text": "S2 to S4 spinal segments", "is_correct": False},
            {"text": "L3 to S1 spinal segments", "is_correct": False},
            {"text": "Throughout all 31 spinal segments", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. T1 to L2 spinal segments.\n\nThe intermediolateral (IML) cell column forms the lateral horn of gray matter in the spinal cord and contains the cell bodies of preganglionic sympathetic neurons. It is present exclusively from spinal segments T1 through L2 (the thoracolumbar outflow of the sympathetic nervous system). Their myelinated axons exit through ventral roots as white rami communicantes to enter the sympathetic paravertebral chain.\n\n• Option C is incorrect: S2 to S4 contains the sacral parasympathetic nucleus (craniosacral outflow), which innervates pelvic viscera via pelvic splanchnic nerves."
    },
    {
        "id": "FZ_Q160",
        "question_number": 160,
        "category": "Spinal Cord",
        "stem": "A 45-year-old man presents with progressive bilateral spastic weakness in his legs and arms. Neurological examination reveals that when his arm is passively flexed, there is initial high resistance that suddenly gives way, allowing the joint to collapse into full flexion ('clasp-knife spasticity'). Clasp-knife rigidity is a hallmark of upper motor neuron lesions and is mediated by which of the following proprioceptors?",
        "options": [
            {"text": "Golgi tendon organs activating Ib inhibitory interneurons in response to high tension", "is_correct": True},
            {"text": "Muscle spindles activating Ia excitatory afferents", "is_correct": False},
            {"text": "Pacinian corpuscles in the joint capsule", "is_correct": False},
            {"text": "Ruffini endings detecting joint rotation", "is_correct": False},
            {"text": "Meissner corpuscles detecting dermal flutter", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Golgi tendon organs activating Ib inhibitory interneurons in response to high tension.\n\nClasp-knife spasticity is a classic sign of an Upper Motor Neuron (UMN) corticospinal tract lesion. When a spastic muscle is passively stretched, exaggerated muscle spindle sensitivity (hyperactive stretch reflex) initially causes marked resistance to movement. However, as passive stretch continues, contractile tension within the tendon reaches a high threshold that vigorously activates Golgi tendon organs (GTOs). Group Ib afferents from GTOs stimulate inhibitory interneurons in the spinal cord, which suddenly inhibit alpha motor neurons, causing the muscle to instantly relax ('give way') like the closing blade of a pocketknife."
    }
]
