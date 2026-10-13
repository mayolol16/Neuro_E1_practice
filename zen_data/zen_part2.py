# zen_part2.py - Topics 5 to 8 (80 Questions total)
import json

part2_questions = [
    # =========================================================================
    # 5. ACETYLCHOLINE / NEUROMUSCULAR JUNCTION DISORDER (20 Questions: Q1 - Q20)
    # =========================================================================
    {
        "q_num": "ACH-01",
        "category": "Acetylcholine / Neuromuscular Junction Disorder",
        "stem": "A 32-year-old woman presents with progressive double vision and drooping of both upper eyelids that worsens toward the evening and improves after a night's rest. She also notes difficulty chewing tough foods at dinner. Physical examination demonstrates bilateral asymmetric ptosis that worsens on sustained upward gaze for 60 seconds. An ice pack placed over her closed eyelids for two minutes results in dramatic improvement of the ptosis. What is the molecular target of the autoantibodies responsible for this patient's condition?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Presynaptic P/Q-type voltage-gated calcium channels"},
            {"letter": "B", "is_correct": True, "text": "Postsynaptic nicotinic acetylcholine receptors"},
            {"letter": "C", "is_correct": False, "text": "Postsynaptic muscarinic M3 receptors"},
            {"letter": "D", "is_correct": False, "text": "Presynaptic synaptobrevin (VAMP)"},
            {"letter": "E", "is_correct": False, "text": "Acetylcholinesterase catalytic subunit"}
        ],
        "explanation": "Correct Answer: B. Postsynaptic nicotinic acetylcholine receptors.\n\nThis patient has Myasthenia Gravis (MG), an autoimmune disorder characterized by autoantibodies directed against postsynaptic nicotinic acetylcholine receptors (AChR) at the motor endplate. \n• Key features: Fluctuating, fatiguable weakness affecting extraocular, bulbar, and proximal limb muscles, with diurnal worsening.\n• Ice pack test: Lowering temperature inhibits local acetylcholinesterase enzyme kinetics, increasing synaptic ACh concentrations and temporarily reversing ptosis.\n• Pathology: Complement-mediated lysis and endocytosis of ACh receptors flatten the postjunctional junctional folds and widen the synaptic cleft.\n• Association: Strongly associated with thymic hyperplasia (~65%) or thymoma (~10-15%)."
    },
    {
        "q_num": "ACH-02",
        "category": "Acetylcholine / Neuromuscular Junction Disorder",
        "stem": "A 64-year-old man with a 45 pack-year smoking history presents with progressive proximal leg weakness. He has difficulty rising from a low chair and climbing stairs. He also complains of persistent dry mouth and erectile dysfunction. On examination, proximal lower extremity strength is 3/5 initially, but improves to 5/5 after 15 seconds of sustained isometric quadriceps contraction. Deep tendon reflexes are absent at rest but become brisk following exercise. A chest CT reveals a central hilar lung mass. Autoantibodies against which of the following structures are diagnostic for this condition?",
        "options": [
            {"letter": "A", "is_correct": True, "text": "Presynaptic P/Q-type voltage-gated calcium channels"},
            {"letter": "B", "is_correct": False, "text": "Postsynaptic acetylcholine receptors"},
            {"letter": "C", "is_correct": False, "text": "Muscle-specific kinase (MuSK)"},
            {"letter": "D", "is_correct": False, "text": "Ryanodine receptors (RYR1)"},
            {"letter": "E", "is_correct": False, "text": "Voltage-gated potassium channels (VGKC)"}
        ],
        "explanation": "Correct Answer: A. Presynaptic P/Q-type voltage-gated calcium channels.\n\nLambert-Eaton Myasthenic Syndrome (LEMS) is a paraneoplastic autoimmune disorder caused by autoantibodies against presynaptic P/Q-type voltage-gated Ca2+ channels at the neuromuscular junction (most commonly associated with small cell lung cancer / SCLC).\n• Clinical hallmarks:\n  1. Proximal muscle weakness that IMPROVES with repetitive muscle use (post-exercise facilitation due to intracellular calcium accumulation in the presynaptic terminal).\n  2. Autonomic dysfunction (dry mouth, erectile dysfunction, constipation, orthostatic hypotension).\n  3. Hyporeflexia or areflexia that enhances following exercise.\nIn contrast, Myasthenia Gravis worsens with use, has normal autonomic function, and normal reflexes."
    },
    {
        "q_num": "ACH-03",
        "category": "Acetylcholine / Neuromuscular Junction Disorder",
        "stem": "A 5-month-old infant is brought to the emergency department because of poor feeding, weak suck, feeble cry, and progressive constipation over the past 3 days. Physical examination reveals marked hypotonia ('floppy baby'), ptosis, sluggish pupillary light reflexes, and head lag. The parents report feeding the infant organic wildflower honey mixed into milk. The toxin responsible for this infant's condition acts by which of the following cellular mechanisms?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Inhibits presynaptic choline uptake"},
            {"letter": "B", "is_correct": True, "text": "Cleaves SNARE proteins to block acetylcholine exocytosis"},
            {"letter": "C", "is_correct": False, "text": "Blocks postsynaptic nicotinic receptors"},
            {"letter": "D", "is_correct": False, "text": "Inhibits acetylcholinesterase irreversibly"},
            {"letter": "E", "is_correct": False, "text": "Inhibits choline acetyltransferase"}
        ],
        "explanation": "Correct Answer: B. Cleaves SNARE proteins to block acetylcholine exocytosis.\n\nInfant botulism occurs following the ingestion of Clostridium botulinum spores (commonly from raw honey or contaminated soil/dust), which germinate in the immature infant gastrointestinal tract and produce botulinum neurotoxin. Botulinum toxin (a zinc endopeptidase) cleaves SNARE proteins (synaptobrevin/VAMP, SNAP-25, or syntaxin) in presynaptic cholinergic terminals, preventing vesicle docking and exocytosis of acetylcholine. This results in symmetric, descending flaccid paralysis, autonomic dysfunction, constipation, and hypotonia."
    },
    {
        "q_num": "ACH-04",
        "category": "Acetylcholine / Neuromuscular Junction Disorder",
        "stem": "A 45-year-old agricultural worker is brought to the emergency department after accidentally spraying himself with an organophosphate insecticide (parathion). He is diaphoresis, salivating copiously, vomiting, wheezing, and has pinpoint pupils (miosis). Heart rate is 42 bpm and blood pressure is 88/50 mm Hg. Extensive muscle fasciculations are noted across his chest and arms, followed by diaphragmatic weakness. Which of the following dual-drug regimens provides the most comprehensive treatment for this toxic exposure?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Physostigmine and epinephrine"},
            {"letter": "B", "is_correct": True, "text": "Atropine and pralidoxime (2-PAM)"},
            {"letter": "C", "is_correct": False, "text": "Neostigmine and diphenhydramine"},
            {"letter": "D", "is_correct": False, "text": "Edrophonium and dantrolene"},
            {"letter": "E", "is_correct": False, "text": "Naloxone and flumazenil"}
        ],
        "explanation": "Correct Answer: B. Atropine and pralidoxime (2-PAM).\n\nOrganophosphates irreversibly inhibit acetylcholinesterase (AChE) by phosphorylating the active serine site, resulting in massive acetylcholine accumulation at both muscarinic and nicotinic synapses:\n• Muscarinic toxicity (DUMBBELSS: Diarrhea, Urination, Miosis, Bronchospasm/bronchorrhea, Bradycardia, Emesis, Lacrimation, Salivation) is treated with Atropine (competitive muscarinic antagonist). Atropine crosses the blood-brain barrier but does NOT reverse nicotinic muscle weakness.\n• Nicotinic toxicity (muscle fasciculations, flaccid paralysis of respiratory muscles) requires Pralidoxime (2-PAM), an oxime compound that regenerates functional acetylcholinesterase by hydrolyzing the organophosphate-enzyme covalent bond before 'aging' occurs."
    },
    {
        "q_num": "ACH-05",
        "category": "Acetylcholine / Neuromuscular Junction Disorder",
        "stem": "A 40-year-old woman with generalized myasthenia gravis who takes pyridostigmine presents with acute shortness of breath and diffuse muscle weakness. On examination, she is sweating profusely, has diffuse abdominal cramping, diarrhea, pinpoint pupils, and prominent muscle fasciculations. Her tidal volume is critically low. Which of the following conditions is the patient experiencing?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Myasthenic crisis due to inadequate pyridostigmine dosing"},
            {"letter": "B", "is_correct": True, "text": "Cholinergic crisis due to pyridostigmine overdose"},
            {"letter": "C", "is_correct": False, "text": "Guillain-Barré syndrome"},
            {"letter": "D", "is_correct": False, "text": "Lambert-Eaton myasthenic syndrome"},
            {"letter": "E", "is_correct": False, "text": "Malignant hyperthermia"}
        ],
        "explanation": "Correct Answer: B. Cholinergic crisis due to pyridostigmine overdose.\n\nIn patients with myasthenia gravis, sudden respiratory deterioration can represent either:\n1. Myasthenic crisis (under-medication / disease flare): Insufficient ACh, muscle weakness without muscarinic excess.\n2. Cholinergic crisis (over-medication): Excessive AChE inhibition causes persistent endplate depolarization (depolarization block) AND obvious muscarinic signs (hyperhidrosis, miosis, diarrhea, salivation, fasciculations, bradycardia).\nHistorically, the short-acting AChE inhibitor edrophonium (Tensilon test) differentiated the two (improving myasthenic crisis, worsening cholinergic crisis). In this patient with prominent muscarinic hyperactivity, cholinergic crisis is diagnosed, and pyridostigmine should be withheld."
    },
    {
        "q_num": "ACH-06",
        "category": "Acetylcholine / Neuromuscular Junction Disorder",
        "stem": "A 35-year-old woman with recently diagnosed myasthenia gravis undergoes contrast-enhanced chest CT. The scan demonstrates an anterior mediastinal mass measuring 4.5 cm in diameter. The embryological tissue that gave rise to this tumor also gives rise to which of the following structures?",
        "options": [
            {"letter": "A", "is_correct": True, "text": "Inferior parathyroid glands"},
            {"letter": "B", "is_correct": False, "text": "Superior parathyroid glands"},
            {"letter": "C", "is_correct": False, "text": "Thyroid follicular cells"},
            {"letter": "D", "is_correct": False, "text": "Adrenal medulla"},
            {"letter": "E", "is_correct": False, "text": "External auditory meatus"}
        ],
        "explanation": "Correct Answer: A. Inferior parathyroid glands.\n\nThis patient has a thymoma (anterior mediastinal mass derived from thymic epithelial cells), which is found in ~10-15% of patients with myasthenia gravis (and thymic hyperplasia in ~65%). The thymus develops embryologically from the third pharyngeal pouch, along with the inferior parathyroid glands. (In contrast, the 4th pharyngeal pouch gives rise to the superior parathyroid glands and ultimopharyngeal body/parafollicular C cells)."
    },
    {
        "q_num": "ACH-07",
        "category": "Acetylcholine / Neuromuscular Junction Disorder",
        "stem": "During general anesthesia for an abdominal laparotomy, a 50-year-old patient receives the nondepolarizing neuromuscular blocking drug rocuronium. At the conclusion of surgery, the anesthesiologist administers neostigmine to reverse muscle paralysis. Why must glycopyrrolate or atropine be co-administered with neostigmine?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "To prevent neostigmine from crossing the blood-brain barrier"},
            {"letter": "B", "is_correct": True, "text": "To prevent muscarinic side effects such as severe bradycardia and bronchospasm"},
            {"letter": "C", "is_correct": False, "text": "To accelerate the clearance of rocuronium in the kidneys"},
            {"letter": "D", "is_correct": False, "text": "To antagonize nicotinic receptors at autonomic ganglia"},
            {"letter": "E", "is_correct": False, "text": "To stimulate the release of endogenous acetylcholine"}
        ],
        "explanation": "Correct Answer: B. To prevent muscarinic side effects such as severe bradycardia and bronchospasm.\n\nNeostigmine is an acetylcholinesterase inhibitor used to reverse non-depolarizing neuromuscular blockers by increasing acetylcholine concentrations at the neuromuscular junction (nicotinic receptors). However, neostigmine also elevates acetylcholine at parasympathetic muscarinic receptors (heart, lungs, GI tract), which can cause profound bradycardia, asystole, bronchoconstriction, and excessive secretions. Therefore, an antimuscarinic agent like glycopyrrolate (or atropine) is always co-administered to block unwanted muscarinic effects."
    },
    {
        "q_num": "ACH-08",
        "category": "Acetylcholine / Neuromuscular Junction Disorder",
        "stem": "Which of the following neuromuscular blocking drugs is a selective, cyclodextrin-based chelating agent that directly binds and encapsulates rocuronium and vecuronium in plasma with high affinity to achieve rapid reversal of neuromuscular blockade without requiring acetylcholinesterase inhibition?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Pralidoxime"},
            {"letter": "B", "is_correct": False, "text": "Dantrolene"},
            {"letter": "C", "is_correct": True, "text": "Sugammadex"},
            {"letter": "D", "is_correct": False, "text": "Edrophonium"},
            {"letter": "E", "is_correct": False, "text": "Physostigmine"}
        ],
        "explanation": "Correct Answer: C. Sugammadex.\n\nSugammadex is a modified gamma-cyclodextrin that acts as a selective relaxant binding agent. It encapsulates steroidal non-depolarizing neuromuscular blocking agents (specifically rocuronium and vecuronium) in a 1:1 ratio within the intravascular space, rapidly decreasing free drug concentration and reversing neuromuscular blockade within 1-3 minutes. Because it does not inhibit acetylcholinesterase, it does not cause cholinergic side effects and does not require co-administration of an antimuscarinic drug."
    },
    {
        "q_num": "ACH-09",
        "category": "Acetylcholine / Neuromuscular Junction Disorder",
        "stem": "A 24-year-old woman with severe, seronegative myasthenia gravis does not have antibodies against the nicotinic acetylcholine receptor (AChR). Serum testing demonstrates autoantibodies against a transmembrane receptor tyrosine kinase essential for agrin-mediated clustering of acetylcholine receptors during synaptogenesis. Which autoantibody is present?",
        "options": [
            {"letter": "A", "is_correct": True, "text": "Anti-MuSK (Muscle-specific kinase) antibody"},
            {"letter": "B", "is_correct": False, "text": "Anti-LRP4 antibody"},
            {"letter": "C", "is_correct": False, "text": "Anti-voltage-gated calcium channel antibody"},
            {"letter": "D", "is_correct": False, "text": "Anti-ryanodine receptor antibody"},
            {"letter": "E", "is_correct": False, "text": "Anti-titin antibody"}
        ],
        "explanation": "Correct Answer: A. Anti-MuSK (Muscle-specific kinase) antibody.\n\nApproximately 40-50% of patients with generalized myasthenia gravis who test negative for anti-AChR antibodies have autoantibodies directed against Muscle-Specific Kinase (MuSK). MuSK is a receptor tyrosine kinase on the postjunctional muscle membrane that interacts with agrin (secreted by the motor nerve terminal) via LRP4 to organize and maintain high-density clustering of AChRs at the neuromuscular junction. Anti-MuSK MG is more common in young females, typically presents with predominant bulbar, facial, and neck weakness, and responds poorly to anticholinesterase inhibitors."
    },
    {
        "q_num": "ACH-10",
        "category": "Acetylcholine / Neuromuscular Junction Disorder",
        "stem": "In skeletal muscle, binding of two acetylcholine molecules to the postjunctional nicotinic receptor causes opening of an integral ion channel. The resulting miniature endplate potential (MEPP) and endplate potential (EPP) are primarily driven by which ionic movement across the channel pore?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Chloride influx"},
            {"letter": "B", "is_correct": False, "text": "Potassium influx"},
            {"letter": "C", "is_correct": True, "text": "Sodium influx exceeding potassium efflux"},
            {"letter": "D", "is_correct": False, "text": "Calcium efflux into the synaptic cleft"},
            {"letter": "E", "is_correct": False, "text": "Active extrusion of sodium by Na+/K+ ATPase"}
        ],
        "explanation": "Correct Answer: C. Sodium influx exceeding potassium efflux.\n\nThe nicotinic acetylcholine receptor at the neuromuscular junction is a non-selective cation channel permeable to both Na+ and K+ (and to a lesser degree Ca2+). At the resting membrane potential of skeletal muscle (-90 mV), the electrochemical driving force for Na+ (Vrest - ENa ≈ -90 - (+60) = -150 mV) is vastly greater than the driving force for K+ (Vrest - EK ≈ -90 - (-95) = +5 mV). Therefore, opening of the channel causes a massive influx of Na+ that far exceeds the modest efflux of K+, producing net inward depolarizing current that generates the endplate potential (EPP)."
    },
    {
        "q_num": "ACH-11",
        "category": "Acetylcholine / Neuromuscular Junction Disorder",
        "stem": "Which of the following tertiary amine acetylcholinesterase inhibitors can readily cross the blood-brain barrier into the central nervous system, making it the drug of choice for treating acute central and peripheral anticholinergic toxicity caused by atropine or deadly nightshade (Atropa belladonna)?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Neostigmine"},
            {"letter": "B", "is_correct": False, "text": "Pyridostigmine"},
            {"letter": "C", "is_correct": False, "text": "Edrophonium"},
            {"letter": "D", "is_correct": True, "text": "Physostigmine"},
            {"letter": "E", "is_correct": False, "text": "Echothiophate"}
        ],
        "explanation": "Correct Answer: D. Physostigmine.\n\n• Physostigmine is a tertiary amine; it is uncharged, lipophilic, and readily crosses the blood-brain barrier to reverse both central ('mad as a hatter' delirium, hallucinations) and peripheral anticholinergic toxicity ('blind as a bat, hot as a hare, dry as a bone, red as a beet').\n• In contrast, Neostigmine, Pyridostigmine, and Edrophonium are quaternary amines; they carry a permanent positive charge, cannot cross the blood-brain barrier, and act only peripherally."
    },
    {
        "q_num": "ACH-12",
        "category": "Acetylcholine / Neuromuscular Junction Disorder",
        "stem": "During repetitive nerve stimulation (RNS) at low frequencies (2-3 Hz), electrophysiological testing in a patient with untreated myasthenia gravis reveals which characteristic finding on compound muscle action potential (CMAP) recording?",
        "options": [
            {"letter": "A", "is_correct": True, "text": "Progressive decremental response (>10% drop in CMAP amplitude)"},
            {"letter": "B", "is_correct": False, "text": "Significant incremental response (>100% increase in CMAP amplitude)"},
            {"letter": "C", "is_correct": False, "text": "Complete absence of sensory nerve action potentials"},
            {"letter": "D", "is_correct": False, "text": "Prolonged distal motor latencies with severe conduction block"},
            {"letter": "E", "is_correct": False, "text": "Fibrillation potentials and positive sharp waves only at rest"}
        ],
        "explanation": "Correct Answer: A. Progressive decremental response (>10% drop in CMAP amplitude).\n\nIn Myasthenia Gravis, low-frequency (2-3 Hz) repetitive nerve stimulation causes a decremental response (>10% reduction in CMAP amplitude from the 1st to the 4th/5th stimulus). Because the safety factor of neuromuscular transmission is reduced (fewer functional AChRs), normal physiological depletion of presynaptic ACh vesicles during repetitive firing results in subthreshold EPPs, failure of muscle fiber action potentials, and a falling CMAP amplitude. Conversely, Lambert-Eaton syndrome shows an incremental response (>100% increase in CMAP) at high-frequency stimulation (20-50 Hz) or post-exercise."
    },
    {
        "q_num": "ACH-13",
        "category": "Acetylcholine / Neuromuscular Junction Disorder",
        "stem": "A 16-year-old boy presents with sudden symmetric flaccid paralysis following ingestion of home-canned green beans. Electrophysiological testing confirms botulism. Which of the following components of the SNARE protein complex is specifically cleaved by Botulinum toxin serotype A?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Synaptobrevin (VAMP-1/2)"},
            {"letter": "B", "is_correct": True, "text": "SNAP-25"},
            {"letter": "C", "is_correct": False, "text": "Syntaxin-1"},
            {"letter": "D", "is_correct": False, "text": "Synaptotagmin"},
            {"letter": "E", "is_correct": False, "text": "Complexin"}
        ],
        "explanation": "Correct Answer: B. SNAP-25.\n\nBotulinum toxin serotypes cleave different components of the SNARE complex:\n• Serotypes A and E cleave SNAP-25 (synaptosome-associated protein 25, a t-SNARE on the plasma membrane).\n• Serotypes B, D, F, and G (and Tetanus toxin) cleave Synaptobrevin / VAMP (a v-SNARE on the vesicle membrane).\n• Serotype C cleaves Syntaxin and SNAP-25.\nCleavage prevents the assembly of the tight four-helix bundle required to bring the vesicle membrane into direct contact with the presynaptic plasma membrane for exocytosis."
    },
    {
        "q_num": "ACH-14",
        "category": "Acetylcholine / Neuromuscular Junction Disorder",
        "stem": "A 3-year-old child presents to the emergency department after ingesting his grandmother's eye drops containing atropine. He is flushed, febrile (39.2°C), agitated, and picking at imaginary objects. His skin and mucous membranes are dry, pupils are 8 mm and nonreactive, and heart rate is 160 bpm. Physical examination shows a palpable, distended urinary bladder. Which of the following is the most appropriate antidote to administer?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Pralidoxime"},
            {"letter": "B", "is_correct": True, "text": "Physostigmine"},
            {"letter": "C", "is_correct": False, "text": "Neostigmine"},
            {"letter": "D", "is_correct": False, "text": "Dantrolene"},
            {"letter": "E", "is_correct": False, "text": "Flumazenil"}
        ],
        "explanation": "Correct Answer: B. Physostigmine.\n\nThis child has classic Anticholinergic Toxicity (antimuscarinic syndrome). Atropine competitively blocks muscarinic receptors throughout the body and CNS. Physostigmine is the indicated antidote because it is a tertiary amine that crosses the blood-brain barrier to increase acetylcholine at both central and peripheral muscarinic receptors, reversing delirium, tachycardia, hyperthermia, and urinary retention. (Quaternary amines like Neostigmine cannot cross into the CNS to reverse central toxicity)."
    },
    {
        "q_num": "ACH-15",
        "category": "Acetylcholine / Neuromuscular Junction Disorder",
        "stem": "Which of the following enzymes is responsible for the single-step synthesis of acetylcholine from choline and acetyl-CoA within the presynaptic cholinergic nerve terminal?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Acetylcholinesterase"},
            {"letter": "B", "is_correct": True, "text": "Choline acetyltransferase (ChAT)"},
            {"letter": "C", "is_correct": False, "text": "Pseudocholinesterase"},
            {"letter": "D", "is_correct": False, "text": "Choline kinase"},
            {"letter": "E", "is_correct": False, "text": "Carnitine acetyltransferase"}
        ],
        "explanation": "Correct Answer: B. Choline acetyltransferase (ChAT).\n\nAcetylcholine is synthesized in the presynaptic cytoplasm by Choline Acetyltransferase (ChAT), which transfers an acetyl group from mitochondrial Acetyl-CoA to Choline (transported into the terminal by a high-affinity Na+/choline cotransporter, CHT1). Acetylcholine is subsequently pumped into synaptic vesicles by the vesicular acetylcholine transporter (VAChT)."
    },
    {
        "q_num": "ACH-16",
        "category": "Acetylcholine / Neuromuscular Junction Disorder",
        "stem": "A 28-year-old woman with ocular myasthenia gravis is started on pyridostigmine. Pyridostigmine inhibits acetylcholinesterase primarily through which chemical mechanism?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Irreversible organophosphorylation of the active serine residue"},
            {"letter": "B", "is_correct": True, "text": "Reversible carbamylation of the active serine residue"},
            {"letter": "C", "is_correct": False, "text": "Non-competitive allosteric inhibition of the peripheral anionic site"},
            {"letter": "D", "is_correct": False, "text": "Competitive antagonism at the post-synaptic nicotinic receptor"},
            {"letter": "E", "is_correct": False, "text": "Chelation of zinc in the catalytic pocket"}
        ],
        "explanation": "Correct Answer: B. Reversible carbamylation of the active serine residue.\n\nCarbamate acetylcholinesterase inhibitors (pyridostigmine, neostigmine, physostigmine) transfer a carbamyl group to the serine-203 residue in the catalytic triad of acetylcholinesterase. Carbamylated acetylcholinesterase is hydrolyzed slowly (half-life of hours) compared to acetylated enzyme (fractions of a millisecond), providing reversible competitive inhibition that wears off as the enzyme regenerates. In contrast, organophosphates cause irreversible phosphorylation."
    },
    {
        "q_num": "ACH-17",
        "category": "Acetylcholine / Neuromuscular Junction Disorder",
        "stem": "A 70-year-old man with small cell lung cancer presents with lower extremity weakness that improves after exercise. Electromyography reveals Lambert-Eaton myasthenic syndrome. In addition to treating the underlying malignancy, which potassium channel blocker is approved as first-line symptomatic medical therapy to increase presynaptic acetylcholine release?",
        "options": [
            {"letter": "A", "is_correct": True, "text": "Amifampridine (3,4-diaminopyridine)"},
            {"letter": "B", "is_correct": False, "text": "Pyridostigmine"},
            {"letter": "C", "is_correct": False, "text": "Dantrolene"},
            {"letter": "D", "is_correct": False, "text": "Baclofen"},
            {"letter": "E", "is_correct": False, "text": "Riluzole"}
        ],
        "explanation": "Correct Answer: A. Amifampridine (3,4-diaminopyridine).\n\nAmifampridine (3,4-diaminopyridine / 3,4-DAP) is the first-line symptomatic treatment for Lambert-Eaton Myasthenic Syndrome. By blocking presynaptic voltage-gated K+ channels, it prolongs action potential duration and membrane depolarization in the nerve terminal. This prolonged depolarization keeps voltage-gated Ca2+ channels open longer, enhancing Ca2+ influx and promoting exocytosis of acetylcholine vesicles to overcome the autoantibody blockade."
    },
    {
        "q_num": "ACH-18",
        "category": "Acetylcholine / Neuromuscular Junction Disorder",
        "stem": "An experimental drug is developed that selectively blocks the vesicular acetylcholine transporter (VAChT). Which of the following compounds is the classic pharmacological research agent that inhibits VAChT, preventing acetylcholine packaging into synaptic vesicles?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Hemicholinium-3"},
            {"letter": "B", "is_correct": True, "text": "Vesamicol"},
            {"letter": "C", "is_correct": False, "text": "Reserpine"},
            {"letter": "D", "is_correct": False, "text": "Tubocurarine"},
            {"letter": "E", "is_correct": False, "text": "Botulinum toxin"}
        ],
        "explanation": "Correct Answer: B. Vesamicol.\n\n• Vesamicol inhibits the vesicular acetylcholine transporter (VAChT), preventing newly synthesized acetylcholine from being loaded into synaptic vesicles.\n• Hemicholinium-3 (Option A) blocks the high-affinity presynaptic choline transporter (CHT1), inhibiting the uptake of choline into the terminal (the rate-limiting step in ACh synthesis).\n• Reserpine (Option C) blocks the vesicular monoamine transporter (VMAT), depleting dopamine, norepinephrine, and serotonin."
    },
    {
        "q_num": "ACH-19",
        "category": "Acetylcholine / Neuromuscular Junction Disorder",
        "stem": "Which of the following clinical tests for myasthenia gravis utilizes a short-acting acetylcholinesterase inhibitor with an onset of 30 seconds and a duration of 5-10 minutes, historically used to confirm diagnosis by demonstrating immediate temporary resolution of muscle weakness?",
        "options": [
            {"letter": "A", "is_correct": True, "text": "Tensilon test (edrophonium)"},
            {"letter": "B", "is_correct": False, "text": "Pralidoxime challenge"},
            {"letter": "C", "is_correct": False, "text": "Methacholine bronchoprovocation test"},
            {"letter": "D", "is_correct": False, "text": "Atropine provocative test"},
            {"letter": "E", "is_correct": False, "text": "Dexamethasone suppression test"}
        ],
        "explanation": "Correct Answer: A. Tensilon test (edrophonium).\n\nThe Tensilon test uses edrophonium, an ultra-short-acting acetylcholinesterase inhibitor that binds reversibly to the anionic site of AChE via non-covalent electrostatic interactions. In patients with myasthenia gravis, IV administration produces rapid (within 30-60 seconds) but brief (5-10 minutes) improvement in ptosis, diplopia, or motor weakness. Due to risks of severe bradycardia and bronchospasm, it has largely been superseded by serological antibody testing and repetitive nerve stimulation."
    },
    {
        "q_num": "ACH-20",
        "category": "Acetylcholine / Neuromuscular Junction Disorder",
        "stem": "A 48-year-old farmer is exposed to an insecticide and arrives with signs of acute cholinergic excess. The physician notes that the patient's symptoms can be remembered by the mnemonic SLUDGE. Which of the following manifestations is mediated by postganglionic parasympathetic stimulation of muscarinic M3 receptors on exocrine glands?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Tachycardia and hypertension"},
            {"letter": "B", "is_correct": False, "text": "Skeletal muscle twitching and fasciculations"},
            {"letter": "C", "is_correct": True, "text": "Profuse salivation and lacrimation"},
            {"letter": "D", "is_correct": False, "text": "Mydriasis and blurred near vision"},
            {"letter": "E", "is_correct": False, "text": "Constipation and urinary retention"}
        ],
        "explanation": "Correct Answer: C. Profuse salivation and lacrimation.\n\nMuscarinic M3 receptors are coupled to Gq proteins (activating phospholipase C → IP3 and DAG → increased intracellular Ca2+). In exocrine glands (salivary, lacrimal, bronchial, sweat glands), M3 activation stimulates copious watery secretion, resulting in salivation (S), lacrimation (L), and diaphoresis. In smooth muscle, M3 activation causes urination (U, detrusor contraction), diarrhea (D, GI hypermotility), and bronchospasm (B). Skeletal muscle fasciculations (Option B) are mediated by nicotinic receptors (Nm) at the motor endplate."
    },

    # =========================================================================
    # 6. NEUROIMAGING (20 Questions: Q21 - Q40)
    # =========================================================================
    {
        "q_num": "IMG-01",
        "category": "Neuroimaging",
        "stem": "A 21-year-old college student sustains a blow to the side of his head during a rugby match. He experiences a brief 2-minute loss of consciousness followed by complete recovery ('lucid interval'). Three hours later, he develops severe headache, nausea, progressive lethargy, and a dilated, non-reactive pupil on the right side. Non-contrast head CT demonstrates a hyperdense, biconvex (lens-shaped) extra-axial collection that does not cross cranial suture lines. Rupture of which vessel caused this hemorrhage, and through which cranial foramen does it enter the skull?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Bridging veins; Jugular foramen"},
            {"letter": "B", "is_correct": True, "text": "Middle meningeal artery; Foramen spinosum"},
            {"letter": "C", "is_correct": False, "text": "Superficial temporal artery; Foramen ovale"},
            {"letter": "D", "is_correct": False, "text": "Anterior communicating artery; Optic canal"},
            {"letter": "E", "is_correct": False, "text": "Posterior inferior cerebellar artery; Foramen magnum"}
        ],
        "explanation": "Correct Answer: B. Middle meningeal artery; Foramen spinosum.\n\nThis patient has an acute Epidural Hematoma (EDH):\n• Mechanism: Fracture of the pterion (where the frontal, parietal, temporal, and sphenoid bones meet) lacerates the underlying middle meningeal artery (a branch of the maxillary artery that enters the skull through the foramen spinosum).\n• Clinical course: Classic 'lucid interval' followed by rapid neurologic deterioration from uncal herniation (ipsilateral CN III compression causing mydriasis).\n• CT appearance: High-density, biconvex/lentiform extra-axial collection limited by cranial suture lines where the periosteal dura is firmly adherent to the calvarium."
    },
    {
        "q_num": "IMG-02",
        "category": "Neuroimaging",
        "stem": "An 82-year-old man with a history of alcohol use disorder is brought to the clinic by his family for progressive confusion, apathy, and unsteady gait over the past 3 weeks. His daughter recalls that he bumped his head against a cabinet 1 month ago. Non-contrast head CT demonstrates a crescent-shaped (concave-convex) fluid collection along the right cerebral convexity that crosses cranial sutures but is restricted by dural reflections (falx cerebri). The density of the collection is hypodense compared to the brain parenchyma. What is the source of bleeding in this lesion?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Middle meningeal artery"},
            {"letter": "B", "is_correct": True, "text": "Bridging cortical veins"},
            {"letter": "C", "is_correct": False, "text": "Basilar tip aneurysm"},
            {"letter": "D", "is_correct": False, "text": "Lenticulostriate arteries"},
            {"letter": "E", "is_correct": False, "text": "Superior ophthalmic vein"}
        ],
        "explanation": "Correct Answer: B. Bridging cortical veins.\n\nThis patient has a Chronic Subdural Hematoma (SDH):\n• Pathophysiology: Tearing of bridging cortical veins as they traverse the subdural space from the cerebral cortex to the superior sagittal sinus. Cerebral atrophy (in elderly and alcoholics) stretches these bridging veins, making them susceptible to rupture from minor head trauma.\n• CT appearance: Crescent-shaped collection spreading along the entire hemisphere, crossing suture lines (since the subdural space is continuous over the cortex) but bounded by dural reflections (falx and tentorium). Chronic SDH appears hypodense (dark) on CT as blood degrades over weeks."
    },
    {
        "q_num": "IMG-03",
        "category": "Neuroimaging",
        "stem": "A 52-year-old woman presents to the emergency department screaming from the sudden onset of the 'worst headache of my life' (thunderclap headache) that began during sexual intercourse. She has marked nuchal rigidity, vomiting, and photophobia. Non-contrast head CT shows hyperdense blood casting the basal cisterns, sylvian fissures, and ambient cisterns in a 'starfish' pattern. What is the most common cause of non-traumatic hemorrhage in this anatomical compartment?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Arteriovenous malformation rupture"},
            {"letter": "B", "is_correct": True, "text": "Rupture of a saccular (berry) aneurysm"},
            {"letter": "C", "is_correct": False, "text": "Hypertensive Charcot-Bouchard microaneurysm rupture"},
            {"letter": "D", "is_correct": False, "text": "Cerebral amyloid angiopathy"},
            {"letter": "E", "is_correct": False, "text": "Venous sinus thrombosis"}
        ],
        "explanation": "Correct Answer: B. Rupture of a saccular (berry) aneurysm.\n\nThis patient has a Subarachnoid Hemorrhage (SAH):\n• The most common cause of non-traumatic SAH is rupture of a congenital saccular (berry) aneurysm in the Circle of Willis (most commonly at the anterior communicating artery > posterior communicating artery > MCA bifurcation).\n• Clinical features: Sudden, instantaneous maximal headache ('thunderclap'), meningismus, photophobia.\n• CT appearance: High-density blood tracking through the subarachnoid spaces and basal cisterns ('starfish' sign).\n• If head CT is negative within 6 hours, lumbar puncture is mandatory to detect xanthochromia (yellow CSF from hemoglobin breakdown to bilirubin)."
    },
    {
        "q_num": "IMG-04",
        "category": "Neuroimaging",
        "stem": "On magnetic resonance imaging (MRI) of the brain, different pulse sequences emphasize specific tissue properties. On a T1-weighted image, cerebrospinal fluid (CSF) appears dark (hypointense) while subcutaneous fat and myelin appear bright (hyperintense). In contrast, what are the signal intensities of CSF and cortical gray matter on a conventional T2-weighted brain MRI?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "CSF is dark (hypointense); gray matter is dark (hypointense)"},
            {"letter": "B", "is_correct": True, "text": "CSF is bright (hyperintense); gray matter is bright/intermediate compared to white matter"},
            {"letter": "C", "is_correct": False, "text": "CSF is bright (hyperintense); gray matter is completely black"},
            {"letter": "D", "is_correct": False, "text": "CSF is dark (hypointense); gray matter is bright (hyperintense)"},
            {"letter": "E", "is_correct": False, "text": "CSF and brain parenchyma have identical signal intensity"}
        ],
        "explanation": "Correct Answer: B. CSF is bright (hyperintense); gray matter is bright/intermediate compared to white matter.\n\nPrinciples of MRI tissue weighting:\n• T1-weighted: Water/CSF is DARK (hypointense); fat/myelin is BRIGHT (hyperintense). White matter appears brighter than gray matter ('anatomy sequence').\n• T2-weighted: Water/CSF is BRIGHT (hyperintense, long T2 relaxation time); gray matter has higher water content than white matter, so gray matter appears hyperintense/intermediate relative to darker white matter ('pathology sequence' because edema, inflammation, and ischemia are bright).\n• FLAIR (Fluid-Attenuated Inversion Recovery): T2-weighted image where free water (CSF) is suppressed to DARK, making periventricular pathology (like MS plaques) conspicuous."
    },
    {
        "q_num": "IMG-05",
        "category": "Neuroimaging",
        "stem": "A 65-year-old man presents with sudden left-sided weakness that began 90 minutes ago. Non-contrast head CT shows no hemorrhage or early ischemic changes. Diffusion-Weighted Imaging (DWI) MRI demonstrates a bright hyperintense signal in the right MCA territory, with corresponding low signal (hypointensity) on the Apparent Diffusion Coefficient (ADC) map. What physiological cellular process causes this diffusion restriction in acute cerebral ischemia?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Disruption of endothelial tight junctions causing vasogenic extracellular edema"},
            {"letter": "B", "is_correct": True, "text": "Failure of Na+/K+ ATPase causing intracellular cytotoxic edema and restricted water motion"},
            {"letter": "C", "is_correct": False, "text": "Accelerated bulk flow of interstitial fluid into venous sinuses"},
            {"letter": "D", "is_correct": False, "text": "Rapid demyelination of axons exposing water molecules"},
            {"letter": "E", "is_correct": False, "text": "Microglial proliferation and phagocytosis of lipid debris"}
        ],
        "explanation": "Correct Answer: B. Failure of Na+/K+ ATPase causing intracellular cytotoxic edema and restricted water motion.\n\nDiffusion-Weighted Imaging (DWI) detects the Brownian motion of water molecules:\n• In acute ischemic stroke, energy failure depletes ATP, causing failure of the Na+/K+ ATPase pump.\n• Sodium, chloride, and water rush into neurons and astrocytes, causing cytotoxic (intracellular) edema.\n• Trapped inside swollen cells, the microscopic random movement of water is physically restricted by cell membranes and organelles.\n• Restricted diffusion appears BRIGHT (hyperintense) on DWI and DARK (hypointense) on ADC maps within minutes of stroke onset (long before changes appear on conventional CT)."
    },
    {
        "q_num": "IMG-06",
        "category": "Neuroimaging",
        "stem": "A 60-year-old man presents with headaches and progressive personality changes. Brain MRI demonstrates an irregularly shaped, heterogeneously enhancing mass with a thick, nodular ring of enhancement and central non-enhancing necrosis. The mass crosses the corpus callosum into both frontal lobes ('butterfly' distribution) with extensive surrounding T2/FLAIR hyperintensity. Which of the following is the most likely diagnosis?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Primary CNS lymphoma"},
            {"letter": "B", "is_correct": True, "text": "Glioblastoma (WHO grade 4)"},
            {"letter": "C", "is_correct": False, "text": "Meningioma"},
            {"letter": "D", "is_correct": False, "text": "Oligodendroglioma"},
            {"letter": "E", "is_correct": False, "text": "Pilocytic astrocytoma"}
        ],
        "explanation": "Correct Answer: B. Glioblastoma (WHO grade 4).\n\nGlioblastoma (GBM) is the most common malignant primary brain tumor in adults:\n• Classic MRI findings: Heterogeneous, ring-enhancing mass with thick, irregular walls, central necrosis, marked mass effect, and finger-like vasogenic edema. A hallmark is crossing the corpus callosum to involve both cerebral hemispheres ('butterfly glioma').\n• Histopathology: Pseudopalisading necrosis, microvascular proliferation, pleomorphic astrocytes expressing GFAP (glial fibrillary acidic protein).\n• Molecular genetics: EGFR amplification, TERT promoter mutations, wild-type IDH (isocitrate dehydrogenase)."
    },
    {
        "q_num": "IMG-07",
        "category": "Neuroimaging",
        "stem": "A 28-year-old woman with a high-speed motor vehicle collision remains in a coma (GCS 5). Initial non-contrast head CT is remarkably normal, showing only mild cerebral edema and no large hematoma or midline shift. However, a T2*-weighted Gradient-Recall Echo (GRE) and Susceptibility-Weighted Imaging (SWI) MRI reveals numerous punctate foci of signal loss ('blooming' hypointensities) located at the gray-white matter junction and the splenium of the corpus callosum. What is the diagnosis?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Cerebral contusions"},
            {"letter": "B", "is_correct": True, "text": "Diffuse axonal injury (DAI)"},
            {"letter": "C", "is_correct": False, "text": "Hypertensive microangiopathy"},
            {"letter": "D", "is_correct": False, "text": "Cerebral amyloid angiopathy"},
            {"letter": "E", "is_correct": False, "text": "Fat embolism syndrome"}
        ],
        "explanation": "Correct Answer: B. Diffuse axonal injury (DAI).\n\nDiffuse Axonal Injury (DAI) results from rapid rotational acceleration-deceleration forces that generate shear stress at interfaces of differing tissue density (classically the gray-white matter junction, corpus callosum, and dorsolateral brainstem tegmentum):\n• Clinical presentation: Immediate coma disproportionate to initial normal or near-normal non-contrast CT.\n• MRI findings: SWI and GRE sequences demonstrate multiple tiny punctate foci of hypointensity ('blooming artifact') representing microhemorrhages from sheared small vessels alongside sheared axons.\n• Histopathology: Axonal spheroids / retraction bulbs positive for beta-amyloid precursor protein (beta-APP)."
    },
    {
        "q_num": "IMG-08",
        "category": "Neuroimaging",
        "stem": "A 72-year-old man with poorly controlled hypertension presents with acute-onset right hemiparesis and hemisensory loss. Head CT reveals a 3 cm hyperdense hematoma located within the left putamen and internal capsule with surrounding edema. This classic hypertensive intraparenchymal hemorrhage is caused by rupture of which microvascular lesion?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Saccular (berry) aneurysm"},
            {"letter": "B", "is_correct": True, "text": "Charcot-Bouchard microaneurysms"},
            {"letter": "C", "is_correct": False, "text": "Arteriovenous malformation"},
            {"letter": "D", "is_correct": False, "text": "Cavernous hemangioma"},
            {"letter": "E", "is_correct": False, "text": "Capillary telangiectasia"}
        ],
        "explanation": "Correct Answer: B. Charcot-Bouchard microaneurysms.\n\nHypertensive intraparenchymal (intracerebral) hemorrhage most commonly affects deep brain structures: the basal ganglia (putamen ~50%), thalamus, pons, and cerebellum. Chronic systemic hypertension induces lipohyalinosis and fibrinoid necrosis of small penetrating lenticulostriate arteries (branches of the MCA), forming microscopic outpouchings called Charcot-Bouchard microaneurysms (<1 mm diameter) that rupture under high pressure. (In contrast, berry aneurysms occur at Circle of Willis bifurcations and cause subarachnoid hemorrhage)."
    },
    {
        "q_num": "IMG-09",
        "category": "Neuroimaging",
        "stem": "An 80-year-old woman with mild dementia presents with acute left-sided arm and leg weakness. Head CT demonstrates a lobar intraparenchymal hemorrhage in the right parietal cortex, sparing the basal ganglia. An MRI gradient-echo sequence reveals multiple prior tiny cortical microbleeds confined exclusively to the cerebral cortex and subcortical white matter. Systemic blood pressure is normal. What is the underlying vascular etiology of this patient's lobar hemorrhage?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Hypertensive arteriolosclerosis"},
            {"letter": "B", "is_correct": True, "text": "Cerebral amyloid angiopathy (CAA)"},
            {"letter": "C", "is_correct": False, "text": "Polyarteritis nodosa"},
            {"letter": "D", "is_correct": False, "text": "Granulomatosis with polyangiitis"},
            {"letter": "E", "is_correct": False, "text": "Fibromuscular dysplasia"}
        ],
        "explanation": "Correct Answer: B. Cerebral amyloid angiopathy (CAA).\n\nCerebral Amyloid Angiopathy (CAA) is the most common cause of spontaneous lobar (superficial cortical/subcortical) hemorrhage in normotensive elderly patients (frequently associated with Alzheimer disease). Beta-amyloid (Aβ40/42) deposits in the media and adventitia of small-to-medium leptomeningeal and cortical arteries, weakening the vessel wall and predisposing to recurrent lobar hemorrhages and superficial siderosis. Deep structures (basal ganglia, pons) are typically spared."
    },
    {
        "q_num": "IMG-10",
        "category": "Neuroimaging",
        "stem": "A 48-year-old woman presents with progressive headache and a new-onset generalized tonic-clonic seizure. Contrast-enhanced MRI reveals a well-circumscribed, extra-axial, homogeneously enhancing mass along the parasagittal convexity. The mass is attached to the dura mater with a characteristic 'dural tail' sign and exerts mass effect on the adjacent brain without parenchymal invasion. Which of the following is the most likely diagnosis?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Glioblastoma"},
            {"letter": "B", "is_correct": True, "text": "Meningioma"},
            {"letter": "C", "is_correct": False, "text": "Schwannoma"},
            {"letter": "D", "is_correct": False, "text": "Metastatic adenocarcinoma"},
            {"letter": "E", "is_correct": False, "text": "Medulloblastoma"}
        ],
        "explanation": "Correct Answer: B. Meningioma.\n\nMeningiomas are the most common benign primary intracranial tumors in adults (higher incidence in females due to estrogen/progesterone receptor expression):\n• Imaging features: Extra-axial, well-demarcated, homogeneously enhancing mass abutting the dura with a distinct 'dural tail' (reactive dural thickening) and hyperostosis of adjacent bone.\n• Histology: Arise from arachnoid cap cells; characterized by whorled patterns of spindle cells and laminated calcifications called psammoma bodies."
    },
    {
        "q_num": "IMG-11",
        "category": "Neuroimaging",
        "stem": "A 62-year-old man with a history of small cell lung cancer presents with progressive headaches and gait ataxia. Brain MRI with gadolinium demonstrates multiple well-circumscribed, round, ring-enhancing lesions located at the gray-white matter junction of both cerebral hemispheres with extensive surrounding vasogenic edema. What feature best explains why hematogenous brain metastases preferentially localize to the gray-white junction?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Lack of a blood-brain barrier at this interface"},
            {"letter": "B", "is_correct": True, "text": "Sudden narrowing of caliber and branching of penetrating arterioles trapping tumor emboli"},
            {"letter": "C", "is_correct": False, "text": "High local concentration of neural crest chemokines"},
            {"letter": "D", "is_correct": False, "text": "Absence of perivascular astrocytic end-feet"},
            {"letter": "E", "is_correct": False, "text": "Direct communication with the subarachnoid CSF space"}
        ],
        "explanation": "Correct Answer: B. Sudden narrowing of caliber and branching of penetrating arterioles trapping tumor emboli.\n\nBrain metastases (most commonly from lung cancer > breast cancer > melanoma > renal cell > colorectal) travel hematogenously via arterial blood. At the junction of the cerebral cortex (gray matter) and subcortical white matter, penetrating arterioles experience an abrupt reduction in caliber and acute branching. Circulating tumor cell emboli become trapped in these microvessels, extravasate, and grow as discrete, spherical, well-circumscribed lesions surrounded by disproportionate vasogenic edema."
    },
    {
        "q_num": "IMG-12",
        "category": "Neuroimaging",
        "stem": "A 55-year-old man presents with right-sided hearing loss, tinnitus, and unsteadiness. Contrast-enhanced MRI demonstrates an intensely enhancing mass at the right cerebellopontine angle that extends into and widens the internal acoustic meatus ('ice cream cone' appearance). Biopsy demonstrates alternating cellular areas (Antoni A) with Verocay bodies and hypocellular myxoid areas (Antoni B). The tumor arises from which cranial nerve?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Trigeminal nerve (CN V)"},
            {"letter": "B", "is_correct": False, "text": "Facial nerve (CN VII)"},
            {"letter": "C", "is_correct": True, "text": "Vestibulocochlear nerve (CN VIII)"},
            {"letter": "D", "is_correct": False, "text": "Glossopharyngeal nerve (CN IX)"},
            {"letter": "E", "is_correct": False, "text": "Hypoglossal nerve (CN XII)"}
        ],
        "explanation": "Correct Answer: C. Vestibulocochlear nerve (CN VIII).\n\nThis patient has a Vestibular Schwannoma (acoustic neuroma):\n• Anatomical location: Cerebellopontine angle (CPA), arising from Schwann cells of the vestibular division of CN VIII. As it grows, it widens the internal acoustic meatus, giving an 'ice cream cone' appearance.\n• Histology: S-100 positive spindle cells exhibiting dense cellular regions with nuclear palisading around acellular eosinophilic zones (Antoni A with Verocay bodies) and loose myxoid tissue (Antoni B).\n• Association: Bilateral vestibular schwannomas are pathognomonic for Neurofibromatosis type 2 (NF2, Merlin gene mutation on chromosome 22)."
    },
    {
        "q_num": "IMG-13",
        "category": "Neuroimaging",
        "stem": "A 28-year-old woman presents with sudden, painful monocular visual loss in her left eye (optic neuritis). Contrast-enhanced MRI of the brain reveals multiple oval, periventricular white matter hyperintensities oriented perpendicular to the lateral ventricles on sagittal FLAIR images ('Dawson fingers'). What is the pathological basis of these radiographic lesions?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Arteriolosclerotic lacunar infarctions"},
            {"letter": "B", "is_correct": True, "text": "Perivenular inflammation and autoimmune demyelination"},
            {"letter": "C", "is_correct": False, "text": "Microabscesses from fungal emboli"},
            {"letter": "D", "is_correct": False, "text": "Perivascular accumulation of amyloid-beta"},
            {"letter": "E", "is_correct": False, "text": "Diffuse axonal shearing from head trauma"}
        ],
        "explanation": "Correct Answer: B. Perivenular inflammation and autoimmune demyelination.\n\nThis patient has Multiple Sclerosis (MS):\n• Dawson fingers are classic demyelinating plaques seen on sagittal T2/FLAIR MRI. They are flame-shaped, periventricular lesions oriented perpendicularly along the long axis of medullary venules.\n• Pathophysiology: Autoreactive CD4+ T lymphocytes cross the blood-brain barrier and orchestrate perivenular inflammation, activating microglia and macrophages to strip myelin sheaths from CNS axons while relatively sparing the underlying axons."
    },
    {
        "q_num": "IMG-14",
        "category": "Neuroimaging",
        "stem": "An 8-year-old boy presents with progressive clumsiness and morning vomiting. Brain MRI demonstrates a cystic lesion in the cerebellar hemisphere with an intensely enhancing mural nodule. Histological evaluation shows bipolar cells with long, hair-like processes and Rosenthal fibers (eosinophilic, corkscrew-shaped intracellular inclusions). What is the diagnosis?",
        "options": [
            {"letter": "A", "is_correct": True, "text": "Pilocytic astrocytoma"},
            {"letter": "B", "is_correct": False, "text": "Medulloblastoma"},
            {"letter": "C", "is_correct": False, "text": "Ependymoma"},
            {"letter": "D", "is_correct": False, "text": "Craniopharyngioma"},
            {"letter": "E", "is_correct": False, "text": "Atypical teratoid/rhabdoid tumor"}
        ],
        "explanation": "Correct Answer: A. Pilocytic astrocytoma.\n\nPilocytic astrocytoma (WHO grade 1) is the most common primary brain tumor in children:\n• Location: Most commonly arises in the cerebellum.\n• MRI appearance: Well-circumscribed cystic lesion with a brightly enhancing solid mural nodule.\n• Histology: GFAP-positive astrocytic neoplasm containing bipolar hair-like piloid cells, microcysts, and Rosenthal fibers (eosinophilic corkscrew-shaped inclusions representing degraded heat shock proteins and ubiquitin). Excellent prognosis after surgical resection."
    },
    {
        "q_num": "IMG-15",
        "category": "Neuroimaging",
        "stem": "A 5-year-old boy presents with morning headaches, vomiting, and severe truncal ataxia. MRI reveals a solid, hyperdense, homogeneously enhancing mass in the cerebellar vermis that compresses the fourth ventricle, causing non-communicating hydrocephalus. Histology demonstrates sheets of small, round blue cells with hyperchromatic nuclei, scant cytoplasm, and Homer Wright rosettes. What is the diagnosis?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Pilocytic astrocytoma"},
            {"letter": "B", "is_correct": True, "text": "Medulloblastoma"},
            {"letter": "C", "is_correct": False, "text": "Schwannoma"},
            {"letter": "D", "is_correct": False, "text": "Choroid plexus carcinoma"},
            {"letter": "E", "is_correct": False, "text": "Craniopharyngioma"}
        ],
        "explanation": "Correct Answer: B. Medulloblastoma.\n\nMedulloblastoma (WHO grade 4) is the most common malignant pediatric brain tumor:\n• Origin: Arises from neuroectodermal primitive cells in the cerebellar vermis (midline/roof of 4th ventricle), causing early truncal ataxia and obstructive hydrocephalus.\n• Histology: Highly cellular sheets of primitive small round blue cells with high mitotic index and pseudorosettes (Homer Wright rosettes where tumor cells surround central neuropil).\n• Complication: Prone to 'drop metastases' along the spinal neuraxis via CSF seeding; requires craniospinal irradiation."
    },
    {
        "q_num": "IMG-16",
        "category": "Neuroimaging",
        "stem": "A 9-year-old girl presents with short stature, bitemporal hemianopia, and headaches. Skull radiograph and CT scan demonstrate a cystic, lobulated suprasellar mass with prominent rim calcifications. Grossly, the cyst fluid resembles motor oil ('crankcase oil') and is rich in cholesterol crystals. The tumor is derived from remnants of which embryological structure?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Optic vesicle"},
            {"letter": "B", "is_correct": True, "text": "Rathke pouch (surface ectoderm)"},
            {"letter": "C", "is_correct": False, "text": "Neural crest of the first arch"},
            {"letter": "D", "is_correct": False, "text": "Infundibulum of the diencephalon"},
            {"letter": "E", "is_correct": False, "text": "Notochord"}
        ],
        "explanation": "Correct Answer: B. Rathke pouch (surface ectoderm).\n\nCraniopharyngioma is a benign suprasellar pediatric tumor derived from remnants of Rathke pouch (an invagination of the oral surface ectoderm that normally forms the anterior pituitary / adenohypophysis):\n• Clinical triad: Visual field defects (bitemporal hemianopia from optic chiasm compression), endocrinopathies (growth failure from GH deficiency, diabetes insipidus), and headache/elevated ICP.\n• Imaging & Gross: Calcified, cystic suprasellar mass containing brownish-yellow 'motor oil' / 'crankcase oil' fluid rich in cholesterol crystals.\n• Histology: Wet keratin, squamous epithelium, and calcifications (adamantinomatous subtype)."
    },
    {
        "q_num": "IMG-17",
        "category": "Neuroimaging",
        "stem": "Which of the following pulse sequences on brain MRI uses a specific radiofrequency prepulse to selectively null (suppress) the high signal of free cerebrospinal fluid, allowing T2-hyperintense inflammatory plaques, periventricular edema, and subcortical ischemic lesions to stand out with high contrast?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Gradient-Recall Echo (GRE)"},
            {"letter": "B", "is_correct": True, "text": "Fluid-Attenuated Inversion Recovery (FLAIR)"},
            {"letter": "C", "is_correct": False, "text": "Diffusion-Weighted Imaging (DWI)"},
            {"letter": "D", "is_correct": False, "text": "Magnetic Resonance Angiography (MRA)"},
            {"letter": "E", "is_correct": False, "text": "Susceptibility-Weighted Imaging (SWI)"}
        ],
        "explanation": "Correct Answer: B. Fluid-Attenuated Inversion Recovery (FLAIR).\n\nFLAIR (Fluid-Attenuated Inversion Recovery) is an inversion recovery MRI sequence that sets the inversion time (TI) specifically to null the signal of pure water/CSF. This causes the bright signal of ventricular and sulcal CSF to turn completely black/dark. As a result, T2-hyperintense pathological processes (such as multiple sclerosis demyelinating plaques, vasogenic edema, subarachnoid hemorrhage, or stroke) that border the ventricles or subarachnoid space become immediately visible without being obscured by CSF brightness."
    },
    {
        "q_num": "IMG-18",
        "category": "Neuroimaging",
        "stem": "A 35-year-old woman on oral contraceptive pills presents with severe headache, papilledema, and a left-sided focal seizure. Non-contrast head CT demonstrates an 'empty delta sign' (triangular non-filling defect) in the posterior superior sagittal sinus on post-contrast CT venogram. What is the diagnosis?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Arteriovenous malformation"},
            {"letter": "B", "is_correct": True, "text": "Cerebral venous sinus thrombosis (CVST)"},
            {"letter": "C", "is_correct": False, "text": "Carotid cavernous fistula"},
            {"letter": "D", "is_correct": False, "text": "Subdural empyema"},
            {"letter": "E", "is_correct": False, "text": "Middle cerebral artery dissection"}
        ],
        "explanation": "Correct Answer: B. Cerebral venous sinus thrombosis (CVST).\n\nCerebral Venous Sinus Thrombosis (CVST) occurs in hypercoagulable states (pregnancy, postpartum, oral contraceptives, factor V Leiden, malignancy):\n• Thrombosis of the superior sagittal sinus or transverse sinus blocks venous drainage, causing increased intracranial pressure and venous infarction.\n• Imaging sign: The 'empty delta sign' on contrast-enhanced CT or MR venography represents a non-enhancing intraluminal thrombus surrounded by brightly enhancing collateral dural collateral channels in the walls of the sinus.\n• Treatment: Therapeutic anticoagulation (e.g., low-molecular-weight heparin or unfractionated heparin), even if hemorrhagic venous infarction is present."
    },
    {
        "q_num": "IMG-19",
        "category": "Neuroimaging",
        "stem": "A 40-year-old man presents with progressive seizures. Brain MRI shows a well-demarcated cortical mass in the frontal lobe with prominent calcifications ('brain stones'). Histological examination demonstrates uniform sheets of rounded cells with perinuclear clear halos ('fried egg' appearance) surrounded by a fine network of delicate, branching capillaries ('chicken-wire' pattern). A codeletion of which chromosome arms is characteristic and predicts favorable response to therapy?",
        "options": [
            {"letter": "A", "is_correct": True, "text": "1p and 19q co-deletion (1p/19q codeletion)"},
            {"letter": "B", "is_correct": False, "text": "Chromosome 22q deletion"},
            {"letter": "C", "is_correct": False, "text": "Chromosome 17p deletion (TP53)"},
            {"letter": "D", "is_correct": False, "text": "Chromosome 9p deletion (CDKN2A)"},
            {"letter": "E", "is_correct": False, "text": "Chromosome 10q loss (PTEN)"}
        ],
        "explanation": "Correct Answer: A. 1p and 19q co-deletion (1p/19q codeletion).\n\nThis patient has an Oligodendroglioma (WHO grade 2/3):\n• Imaging: Well-demarcated frontal lobe mass with prominent coarse calcifications (seen on CT) and cortical thickening.\n• Histopathology: Cells with round, central nuclei and artifactual perinuclear clear halos ('fried egg' appearance) embedded in a dense capillary network ('chicken-wire' vasculature).\n• Genetics: Defined by IDH1/2 mutation AND whole-arm 1p/19q co-deletion (an unbalanced translocation t(1;19)(q10;p10)). The 1p/19q codeletion is strongly predictive of excellent chemotherapy sensitivity (PCV regimen) and prolonged overall survival."
    },
    {
        "q_num": "IMG-20",
        "category": "Neuroimaging",
        "stem": "An unconscious trauma patient is evaluated for an acute epidural hematoma. On non-contrast head CT, acute intracranial hemorrhage appears hyperdense (bright white) compared to normal brain tissue. What physical property of acute extravasated blood is responsible for this high X-ray attenuation?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "High lipid content of erythrocyte membranes"},
            {"letter": "B", "is_correct": True, "text": "High protein concentration of globin chains in concentrated hemoglobin"},
            {"letter": "C", "is_correct": False, "text": "Rapid calcification of fibrin clots within minutes"},
            {"letter": "D", "is_correct": False, "text": "Paramagnetic iron atoms in methemoglobin"},
            {"letter": "E", "is_correct": False, "text": "Low water content of plasma"}
        ],
        "explanation": "Correct Answer: B. High protein concentration of globin chains in concentrated hemoglobin.\n\nOn CT, X-ray attenuation is measured in Hounsfield Units (HU):\n• Water = 0 HU; Brain parenchyma = ~30-40 HU; Acute blood = ~60-80 HU; Bone = +1000 HU.\n• The high attenuation of acute hematoma on CT is primarily due to the high protein density of hemoglobin (specifically the protein concentration of globin molecules, which is ~34 g/dL inside packed erythrocytes), as clot retraction squeezes out serum and concentrates red blood cells. (Iron contributes only ~5-8% of the attenuation)."
    },

    # =========================================================================
    # 7. TACTILE PATHWAY (20 Questions: Q41 - Q60)
    # =========================================================================
    {
        "q_num": "TAC-01",
        "category": "Tactile Pathway",
        "stem": "A 45-year-old man presents with progressive sensory loss in his legs. Neurological testing reveals absent vibration sense in both ankles when tested with a 128-Hz tuning fork and impaired conscious proprioception in both great toes. Sensation to pinprick and temperature is normal. Which ascending spinal cord pathway is selectively damaged, and where does its primary afferent neuron synapse with the second-order neuron?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Lateral spinothalamic tract; Dorsal horn substantia gelatinosa"},
            {"letter": "B", "is_correct": True, "text": "Fasciculus gracilis; Nucleus gracilis in the caudal medulla"},
            {"letter": "C", "is_correct": False, "text": "Fasciculus cuneatus; Nucleus cuneatus in the caudal medulla"},
            {"letter": "D", "is_correct": False, "text": "Anterior spinocerebellar tract; Clarke nucleus"},
            {"letter": "E", "is_correct": False, "text": "Lateral corticospinal tract; Ventral horn alpha motor neurons"}
        ],
        "explanation": "Correct Answer: B. Fasciculus gracilis; Nucleus gracilis in the caudal medulla.\n\nThe dorsal column-medial lemniscal (DCML) pathway conveys fine touch, conscious proprioception, and vibration:\n• Lower body (below T6, including legs): Primary afferents ascend medially in the fasciculus gracilis without synapsing in the spinal cord, reaching their first synapse in the nucleus gracilis in the caudal medulla.\n• Upper body (at and above T6, including arms): Primary afferents ascend laterally in the fasciculus cuneatus to synapse in the nucleus cuneatus.\n• Second-order axons then decussate as internal arcuate fibers to form the medial lemniscus, ascending to the VPL nucleus of the thalamus."
    },
    {
        "q_num": "TAC-02",
        "category": "Tactile Pathway",
        "stem": "A 35-year-old man undergoes sensory testing. With his eyes closed, a key is placed in his right hand. He is unable to identify the object by touch alone, although he can feel the metal and appreciate its shape. His vision, speech, and basic primary touch thresholds are completely intact. What is the clinical term for this deficit, and where is the responsible cortical lesion?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Agraphesthesia; Left primary motor cortex (Brodmann area 4)"},
            {"letter": "B", "is_correct": True, "text": "Astereognosis; Left somatosensory association cortex (Brodmann area 5/7)"},
            {"letter": "C", "is_correct": False, "text": "Prosopagnosia; Bilateral fusiform gyri"},
            {"letter": "D", "is_correct": False, "text": "Anosognosia; Right parietal association cortex"},
            {"letter": "E", "is_correct": False, "text": "Apraxia; Left supplementary motor area"}
        ],
        "explanation": "Correct Answer: B. Astereognosis; Left somatosensory association cortex (Brodmann area 5/7).\n\nStereognosis is the ability to recognize an object by touch using shape, texture, and size without visual or auditory input. Inability to recognize objects despite intact primary sensory modalities (touch, temperature, pain) is called astereognosis (tactile agnosia). It indicates a cortical lesion in the contralateral somatosensory association area (superior parietal lobule, Brodmann areas 5 and 7). Agraphesthesia (inability to recognize numbers drawn on the hand) is another cortical sensory modality mediated by the parietal association cortex."
    },
    {
        "q_num": "TAC-03",
        "category": "Tactile Pathway",
        "stem": "A 58-year-old man presents with a history of untreated syphilis. On physical examination, he has a wide-based, stomping gait and walks with his eyes fixed on the ground. When asked to stand with his feet together and eyes open, he is steady; however, within seconds of closing his eyes, he sways violently and falls (positive Romberg test). Neuropathological examination would most likely show demyelination of which spinal cord region?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Lateral corticospinal tracts"},
            {"letter": "B", "is_correct": False, "text": "Anterior spinothalamic tracts"},
            {"letter": "C", "is_correct": True, "text": "Dorsal columns (fasciculus gracilis and cuneatus)"},
            {"letter": "D", "is_correct": False, "text": "Ventral horn motor neurons"},
            {"letter": "E", "is_correct": False, "text": "Anterior white commissure"}
        ],
        "explanation": "Correct Answer: C. Dorsal columns (fasciculus gracilis and cuneatus).\n\nThis patient has Tabes Dorsalis (tertiary neurosyphilis):\n• Pathophysiology: Treponema pallidum invades and destroys the dorsal root ganglia and dorsal columns (fasciculus gracilis > cuneatus), leading to severe loss of proprioception, vibration, and fine touch.\n• Romberg test: Balance requires at least 2 of 3 sensory inputs (vision, proprioception, vestibular). Patients with dorsal column damage maintain balance with eyes open by compensating visually; when eyes are closed, loss of proprioceptive input produces severe unsteadiness (positive Romberg test = sensory ataxia).\n• Associated features: 'Lightning' pains, Argyll Robertson pupils (accommodate but do not react to light), Charcot joints."
    },
    {
        "q_num": "TAC-04",
        "category": "Tactile Pathway",
        "stem": "In the dorsal column-medial lemniscal system, second-order axons arise from the nucleus gracilis and nucleus cuneatus in the caudal medulla. At what specific anatomical landmark do these second-order fibers cross the midline as internal arcuate fibers?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Pyramidal decussation in the caudal medulla"},
            {"letter": "B", "is_correct": True, "text": "Sensory decussation in the caudal medulla"},
            {"letter": "C", "is_correct": False, "text": "Ventral tegmental decussation in the rostral midbrain"},
            {"letter": "D", "is_correct": False, "text": "Basilar pons at the level of the middle cerebellar peduncles"},
            {"letter": "E", "is_correct": False, "text": "Anterior white commissure in the spinal cord"}
        ],
        "explanation": "Correct Answer: B. Sensory decussation in the caudal medulla.\n\nAxons of second-order neurons in the nucleus gracilis and nucleus cuneatus curve ventromedially as internal arcuate fibers and cross the midline at the sensory decussation in the caudal medulla (just rostral to the motor/pyramidal decussation). Once crossed, they ascend rostrally through the brainstem as the medial lemniscus to terminate in the ventral posterolateral (VPL) nucleus of the thalamus."
    },
    {
        "q_num": "TAC-05",
        "category": "Tactile Pathway",
        "stem": "Which specialized cutaneous mechanoreceptor is encapsulated, rapidly adapting, located within the dermal papillae of glabrous (hairless) skin such as fingertips and lips, and is primarily responsible for detecting low-frequency dynamic vibrations (30-50 Hz) and transient touch during grip adjustment?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Merkel nerve endings"},
            {"letter": "B", "is_correct": True, "text": "Meissner corpuscles"},
            {"letter": "C", "is_correct": False, "text": "Pacinian corpuscles"},
            {"letter": "D", "is_correct": False, "text": "Ruffini endings"},
            {"letter": "E", "is_correct": False, "text": "Free nerve endings"}
        ],
        "explanation": "Correct Answer: B. Meissner corpuscles.\n\nCutaneous mechanoreceptors:\n• Meissner corpuscles: Rapidly adapting, encapsulated, located in dermal papillae of glabrous skin; sense low-frequency vibration (30-50 Hz), light flutter, and slip/grip changes.\n• Merkel discs: Slowly adapting, unencapsulated, basal epidermis; sense sustained pressure, edges, and fine tactile spatial discrimination (braille).\n• Pacinian corpuscles: Rapidly adapting, deep dermis/subcutis (onion-like); sense high-frequency vibration (200-300 Hz) and deep pressure.\n• Ruffini endings: Slowly adapting, deep dermis; sense skin stretch and joint angle."
    },
    {
        "q_num": "TAC-06",
        "category": "Tactile Pathway",
        "stem": "A 66-year-old strict vegan presents with paresthesias, numbness in both feet, and progressive gait unsteadiness. Examination shows absent vibration and position sense in both lower extremities, spastic paraparesis, hyperreflexia, and bilateral extensor plantar responses. Serum vitamin B12 level is 95 pg/mL (normal >200 pg/mL). This condition, subacute combined degeneration (SCD), involves demyelination of which combination of spinal cord tracts?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Anterior horn motor neurons and anterior corticospinal tracts"},
            {"letter": "B", "is_correct": True, "text": "Dorsal columns, lateral corticospinal tracts, and spinocerebellar tracts"},
            {"letter": "C", "is_correct": False, "text": "Spinothalamic tracts and anterior horn motor neurons"},
            {"letter": "D", "is_correct": False, "text": "Fasciculus cuneatus and anterior white commissure"},
            {"letter": "E", "is_correct": False, "text": "Rubrospinal and tectospinal tracts"}
        ],
        "explanation": "Correct Answer: B. Dorsal columns, lateral corticospinal tracts, and spinocerebellar tracts.\n\nSubacute Combined Degeneration (SCD) of the spinal cord is caused by Vitamin B12 (cobalamin) deficiency (which impairs methylmalonyl-CoA mutase, causing buildup of methylmalonic acid and abnormal myelin fatty acid incorporation). It characteristically damages:\n1. Dorsal columns (loss of vibration, fine touch, and proprioception → sensory ataxia).\n2. Lateral corticospinal tracts (spastic paraparesis, hyperreflexia, Babinski sign).\n3. Spinocerebellar tracts (ataxia).\nPinprick and temperature sensation (spinothalamic tracts) are typically preserved."
    },
    {
        "q_num": "TAC-07",
        "category": "Tactile Pathway",
        "stem": "A sensory physiologist records the electrical activity of primary afferent axons in a peripheral nerve during skin indentation. A-beta fibers convey fine touch and vibration. Which of the following lists correctly orders peripheral nerve fibers from largest to smallest axonal diameter and from fastest to slowest conduction velocity?",
        "options": [
            {"letter": "A", "is_correct": True, "text": "A-alpha > A-beta > A-delta > C"},
            {"letter": "B", "is_correct": False, "text": "A-alpha > A-delta > A-beta > C"},
            {"letter": "C", "is_correct": False, "text": "A-beta > A-alpha > C > A-delta"},
            {"letter": "D", "is_correct": False, "text": "C > A-delta > A-beta > A-alpha"},
            {"letter": "E", "is_correct": False, "text": "A-delta > A-beta > A-alpha > C"}
        ],
        "explanation": "Correct Answer: A. A-alpha > A-beta > A-delta > C.\n\nPeripheral nerve fiber classification:\n• A-alpha (13-20 μm, 80-120 m/s): Heavily myelinated; proprioception (muscle spindles, Golgi tendon organs) and alpha motor neurons.\n• A-beta (6-12 μm, 35-75 m/s): Heavily myelinated; touch, vibration, pressure (Meissner, Merkel, Pacinian).\n• A-gamma (3-6 μm): Intrafusal motor fibers.\n• A-delta (1-5 μm, 5-30 m/s): Lightly myelinated; fast/sharp pain, cold temperature.\n• C fibers (0.2-1.5 μm, 0.5-2 m/s): Unmyelinated; slow/dull burning pain, warm temperature, postganglionic sympathetics."
    },
    {
        "q_num": "TAC-08",
        "category": "Tactile Pathway",
        "stem": "A 50-year-old man who suffered an ischemic stroke is found to have lost tactile sensation and conscious proprioception on the right side of his face. Sensation on the left side of his face and the rest of his body is normal. Ascending sensory projections from the face relay in which thalamic nucleus before projecting to the primary somatosensory cortex?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Ventral posterolateral nucleus (VPL)"},
            {"letter": "B", "is_correct": True, "text": "Ventral posteromedial nucleus (VPM)"},
            {"letter": "C", "is_correct": False, "text": "Lateral geniculate nucleus (LGN)"},
            {"letter": "D", "is_correct": False, "text": "Medial geniculate nucleus (MGN)"},
            {"letter": "E", "is_correct": False, "text": "Ventral anterior nucleus (VA)"}
        ],
        "explanation": "Correct Answer: B. Ventral posteromedial nucleus (VPM).\n\nThalamic relay nuclei:\n• VPM (Ventral posteromedial): Relays sensory information from the face via trigeminal pathway and taste from solitary nucleus ('Make-up goes on the Face').\n• VPL (Ventral posterolateral): Relays sensory information from the body (DCML and spinothalamic tracts) ('Legs/arms go to Lateral').\n• LGN (Lateral geniculate): Relays visual information from the optic tract to visual cortex ('Light goes to LGN').\n• MGN (Medial geniculate): Relays auditory information from inferior colliculus to auditory cortex ('Music goes to MGN')."
    },
    {
        "q_num": "TAC-09",
        "category": "Tactile Pathway",
        "stem": "A 40-year-old woman is tested for tactile spatial resolution using a caliper with two adjustable tips. On the fingertip, she can distinguish two distinct points separated by only 2 mm. In contrast, on the mid-back, the tips must be separated by at least 40 mm before she can perceive two distinct points. What neuroanatomical factor accounts for this dramatic difference in two-point discrimination threshold?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Larger receptive fields and higher convergence of primary afferents on the fingertips"},
            {"letter": "B", "is_correct": True, "text": "Higher density of mechanoreceptors with smaller receptive fields and a disproportionately large cortical representation"},
            {"letter": "C", "is_correct": False, "text": "Presence of unmyelinated C-fibers in the fingertips"},
            {"letter": "D", "is_correct": False, "text": "Thicker stratum corneum on the back amplifying mechanical waves"},
            {"letter": "E", "is_correct": False, "text": "Lack of lateral inhibition in the spinal cord dorsal horn for fingertip afferents"}
        ],
        "explanation": "Correct Answer: B. Higher density of mechanoreceptors with smaller receptive fields and a disproportionately large cortical representation.\n\nTwo-point discrimination threshold is finest on the fingertips and lips (~2-3 mm) and coarsest on the back and thighs (~40-50 mm). This is determined by:\n1. Receptive field size: Fingertips have tiny, densely packed receptive fields (Merkel and Meissner corpuscles) with minimal convergence on central neurons.\n2. Lateral inhibition: Sharpening of edges by inhibitory interneurons in the dorsal column nuclei and cortex.\n3. Cortical magnification: The sensory homunculus in the primary somatosensory cortex (postcentral gyrus) devotes a vastly disproportionate cortical surface area to the hands, fingers, and lips."
    },
    {
        "q_num": "TAC-10",
        "category": "Tactile Pathway",
        "stem": "A 62-year-old man undergoes a neurological examination. When a 128-Hz tuning fork is placed over his right medial malleolus, he perceives no vibration, whereas he perceives vibration normally over his left medial malleolus. Vibration sense in the upper extremities is symmetric and normal. This deficit localizes to which of the following tracts and levels?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Left fasciculus cuneatus in the cervical cord"},
            {"letter": "B", "is_correct": True, "text": "Right fasciculus gracilis in the lumbar/thoracic cord"},
            {"letter": "C", "is_correct": False, "text": "Left spinothalamic tract in the thoracic cord"},
            {"letter": "D", "is_correct": False, "text": "Right lateral corticospinal tract in the lumbar cord"},
            {"letter": "E", "is_correct": False, "text": "Left medial lemniscus in the midbrain"}
        ],
        "explanation": "Correct Answer: B. Right fasciculus gracilis in the lumbar/thoracic cord.\n\nPrimary afferents for vibration and proprioception from the lower extremity ascend ipsilaterally in the fasciculus gracilis without crossing until they reach the caudal medulla. Therefore, an isolated unilateral loss of vibration sensation in the right leg localizes to the ipsilateral (right) fasciculus gracilis below T6. (A lesion of the left medial lemniscus in the midbrain [Option E] would cause contralateral loss affecting both the right arm and right leg)."
    },
    {
        "q_num": "TAC-11",
        "category": "Tactile Pathway",
        "stem": "Which of the following mechanoreceptors is an unencapsulated disc-like sensory ending located in the stratum basale of the epidermis, exhibits slow adaptation to sustained mechanical indentation, and provides high spatial resolution for reading braille?",
        "options": [
            {"letter": "A", "is_correct": True, "text": "Merkel disc"},
            {"letter": "B", "is_correct": False, "text": "Meissner corpuscle"},
            {"letter": "C", "is_correct": False, "text": "Pacinian corpuscle"},
            {"letter": "D", "is_correct": False, "text": "Ruffini ending"},
            {"letter": "E", "is_correct": False, "text": "Hair follicle receptor"}
        ],
        "explanation": "Correct Answer: A. Merkel disc.\n\nMerkel discs (slowly adapting type 1 / SA1 mechanoreceptors) consist of a specialized Merkel cell in the basal layer of the epidermis intimately associated with an expanded terminal unmyelinated disc of a myelinated A-beta axon. They respond to sustained indentation with sustained firing and have the highest spatial resolution of all mechanoreceptors (0.5 mm), allowing the perception of form, texture, sharp edges, and Braille characters."
    },
    {
        "q_num": "TAC-12",
        "category": "Tactile Pathway",
        "stem": "The primary somatosensory cortex (S1) is located in the postcentral gyrus of the parietal lobe. Which Brodmann area within S1 receives the densest direct thalamic projections from the VPL and VPM nuclei representing slow-adapting and rapidly-adapting cutaneous tactile receptors?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Brodmann area 1"},
            {"letter": "B", "is_correct": False, "text": "Brodmann area 2"},
            {"letter": "C", "is_correct": True, "text": "Brodmann area 3b"},
            {"letter": "D", "is_correct": False, "text": "Brodmann area 4"},
            {"letter": "E", "is_correct": False, "text": "Brodmann area 6"}
        ],
        "explanation": "Correct Answer: C. Brodmann area 3b.\n\nThe primary somatosensory cortex (S1) comprises four cytoarchitectonic Brodmann areas (3a, 3b, 1, and 2):\n• Area 3b receives the dense direct thalamocortical input from VPL/VPM conveying cutaneous tactile information (from both slowly and rapidly adapting mechanoreceptors) and exhibits a complete somatotopic map.\n• Area 3a receives proprioceptive input from muscle stretch receptors.\n• Areas 1 and 2 receive processed inputs from areas 3a and 3b to detect complex texture (area 1) and size/shape/stereognosis (area 2)."
    },
    {
        "q_num": "TAC-13",
        "category": "Tactile Pathway",
        "stem": "A 55-year-old man presents with loss of fine touch and conscious proprioception in his left upper extremity. His lower extremities are completely unaffected. An MRI reveals an isolated lesion of the cervical dorsal columns. Which specific tract within the dorsal column conveys touch and vibration exclusively from the upper extremity and upper trunk (above T6)?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Fasciculus gracilis"},
            {"letter": "B", "is_correct": True, "text": "Fasciculus cuneatus"},
            {"letter": "C", "is_correct": False, "text": "Lissauer tract"},
            {"letter": "D", "is_correct": False, "text": "Lateral spinothalamic tract"},
            {"letter": "E", "is_correct": False, "text": "Rubrospinal tract"}
        ],
        "explanation": "Correct Answer: B. Fasciculus cuneatus.\n\nIn the cervical spinal cord, the posterior funiculus is divided into two distinct fasciculi:\n• Fasciculus gracilis (medial): Conveys fibers from the lower body (T7 through S5).\n• Fasciculus cuneatus (lateral): Conveys fibers from the upper body (C2 through T6, including the upper extremity). The fasciculus cuneatus is absent below T6, appearing only at upper thoracic and cervical levels."
    },
    {
        "q_num": "TAC-14",
        "category": "Tactile Pathway",
        "stem": "Which encapsulated mechanoreceptor is located in the deep dermis and subcutaneous tissue, contains concentric lamellae of flattened Schwann-related cells surrounding a single central unmyelinated axon terminal, and acts as a biological high-pass mechanical filter for detecting high-frequency vibrations (200-300 Hz)?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Meissner corpuscle"},
            {"letter": "B", "is_correct": True, "text": "Pacinian corpuscle"},
            {"letter": "C", "is_correct": False, "text": "Merkel disc"},
            {"letter": "D", "is_correct": False, "text": "Ruffini ending"},
            {"letter": "E", "is_correct": False, "text": "Krause end bulb"}
        ],
        "explanation": "Correct Answer: B. Pacinian corpuscle.\n\nPacinian corpuscles (lamellar corpuscles) are large (1-2 mm), onion-shaped encapsulated mechanoreceptors located in the deep dermis, hypodermis, interosseous membranes, and mesentery. The concentric fluid-filled lamellae act as a mechanical filter that absorbs steady slow pressure while transmitting rapid transient mechanical distortions to the central nerve terminal. This makes them extraordinarily sensitive to high-frequency vibrations (200-300 Hz), such as the vibration of a tuning fork or texture changes during tool use."
    },
    {
        "q_num": "TAC-15",
        "category": "Tactile Pathway",
        "stem": "In the somatotopic organization of the primary somatosensory cortex (postcentral gyrus), which of the following body parts is represented on the medial surface of the hemisphere within the longitudinal cerebral fissure, supplied by the anterior cerebral artery?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Face and lips"},
            {"letter": "B", "is_correct": False, "text": "Hand and fingers"},
            {"letter": "C", "is_correct": False, "text": "Tongue and pharynx"},
            {"letter": "D", "is_correct": True, "text": "Foot, toes, and perineum"},
            {"letter": "E", "is_correct": False, "text": "Forearm and elbow"}
        ],
        "explanation": "Correct Answer: D. Foot, toes, and perineum.\n\nOn the somatosensory homunculus in the postcentral gyrus:\n• Medial surface (paracentral lobule, supplied by the ACA): Lower extremity (foot, toes, leg) and genitalia/perineum.\n• Lateral convexity (superior to inferior, supplied by the MCA): Trunk, arm, hand, fingers, face, lips, tongue, and intra-abdominal viscera."
    },
    {
        "q_num": "TAC-16",
        "category": "Tactile Pathway",
        "stem": "During a neurophysiological study of sensory processing, stimulation of an inhibitory interneuron adjacent to an active primary sensory pathway suppresses the firing of neighboring secondary neurons. This contrast-enhancement mechanism, which sharpens tactile borders and improves two-point discrimination, is known as:",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Recurrent inhibition"},
            {"letter": "B", "is_correct": True, "text": "Lateral inhibition"},
            {"letter": "C", "is_correct": False, "text": "Feedforward excitation"},
            {"letter": "D", "is_correct": False, "text": "Long-term depression"},
            {"letter": "E", "is_correct": False, "text": "Autogenic inhibition"}
        ],
        "explanation": "Correct Answer: B. Lateral inhibition.\n\nLateral inhibition is a fundamental mechanism throughout sensory systems (vision, touch, hearing) in which strongly activated central neurons inhibit neighboring parallel neurons via GABAergic interneurons. This sharpens spatial acuity and contrast by exaggerating differences in firing rates at edges and boundaries, enabling precise localization and two-point discrimination."
    },
    {
        "q_num": "TAC-17",
        "category": "Tactile Pathway",
        "stem": "A 48-year-old woman presents with progressive sensory ataxia. Nerve conduction studies demonstrate loss of large myelinated sensory fibers. Which of the following sensory modalities is conveyed exclusively by large myelinated (A-beta) fibers and would be earliest affected in this patient?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Sharp pinprick sensation"},
            {"letter": "B", "is_correct": False, "text": "Warmth sensation (40°C)"},
            {"letter": "C", "is_correct": True, "text": "Vibration sensation (128 Hz tuning fork)"},
            {"letter": "D", "is_correct": False, "text": "Slow burning pain"},
            {"letter": "E", "is_correct": False, "text": "Cold sensation (15°C)"}
        ],
        "explanation": "Correct Answer: C. Vibration sensation (128 Hz tuning fork).\n\n• Large myelinated fibers (A-alpha and A-beta) convey proprioception, vibration, and fine discrimative touch via the DCML pathway. Large-fiber neuropathies present with loss of ankle vibration and position sense, sensory ataxia, and hyporeflexia.\n• Small fibers (A-delta and unmyelinated C fibers) convey temperature and pain; small-fiber neuropathies present with burning pain and paresthesias with preserved vibration and reflexes."
    },
    {
        "q_num": "TAC-18",
        "category": "Tactile Pathway",
        "stem": "A 70-year-old man suffers an ischemic stroke resulting in a selective infarct of the medial lemniscus within the right rostral pons. Which of the following sensory deficits will be observed on physical examination?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Ipsilateral loss of pain and temperature on the body"},
            {"letter": "B", "is_correct": False, "text": "Ipsilateral loss of fine touch and vibration on the body"},
            {"letter": "C", "is_correct": True, "text": "Contralateral loss of fine touch, vibration, and proprioception on the body"},
            {"letter": "D", "is_correct": False, "text": "Contralateral loss of facial pain and temperature"},
            {"letter": "E", "is_correct": False, "text": "Bilateral loss of all sensory modalities"}
        ],
        "explanation": "Correct Answer: C. Contralateral loss of fine touch, vibration, and proprioception on the body.\n\nThe medial lemniscus contains second-order sensory axons that have already crossed the midline at the caudal medulla. Therefore, a lesion of the medial lemniscus anywhere above the medullary sensory decussation (in the rostral medulla, pons, or midbrain) produces CONTRALATERAL loss of fine touch, vibration, and proprioception on the body."
    },
    {
        "q_num": "TAC-19",
        "category": "Tactile Pathway",
        "stem": "In the dorsal root ganglion, primary sensory neurons that convey tactile information possess which morphological classification of neuronal architecture?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Multipolar neurons"},
            {"letter": "B", "is_correct": False, "text": "Bipolar neurons"},
            {"letter": "C", "is_correct": True, "text": "Pseudounipolar neurons"},
            {"letter": "D", "is_correct": False, "text": "Anaxonic neurons"},
            {"letter": "E", "is_correct": False, "text": "Pyramidal neurons"}
        ],
        "explanation": "Correct Answer: C. Pseudounipolar neurons.\n\nPrimary sensory neurons in the dorsal root ganglia (and sensory cranial nerve ganglia V, VII, IX, X) are pseudounipolar neurons. They begin embryologically as bipolar cells, but their two processes fuse into a single stalk that bifurcates into a peripheral process (extending to cutaneous receptors) and a central process (entering the spinal cord via the dorsal root). Action potentials propagate directly from the peripheral terminal to the central terminal without requiring synaptic transmission through the soma."
    },
    {
        "q_num": "TAC-20",
        "category": "Tactile Pathway",
        "stem": "A patient is asked to close her eyes while the examiner uses a blunt probe to trace the number '8' on the palm of her hand. She correctly identifies the number. This clinical test evaluates graphesthesia. Successful performance requires intact transmission through the DCML pathway and processing by which cortical area?",
        "options": [
            {"letter": "A", "is_correct": True, "text": "Contralateral primary somatosensory cortex and superior parietal lobule"},
            {"letter": "B", "is_correct": False, "text": "Ipsilateral motor cortex and premotor area"},
            {"letter": "C", "is_correct": False, "text": "Contralateral inferior temporal gyrus"},
            {"letter": "D", "is_correct": False, "text": "Bilateral anterior cingulate cortex"},
            {"letter": "E", "is_correct": False, "text": "Contralateral prefrontal association cortex"}
        ],
        "explanation": "Correct Answer: A. Contralateral primary somatosensory cortex and superior parietal lobule.\n\nGraphesthesia is a complex cortical sensory modality that requires primary sensory input (fine touch via DCML) to be integrated in the contralateral primary somatosensory cortex (postcentral gyrus) and secondary parietal association cortex (superior parietal lobule, Brodmann areas 5 and 7). Agraphesthesia indicates contralateral parietal lobe dysfunction."
    },

    # =========================================================================
    # 8. SPINAL CORD (20 Questions: Q61 - Q80)
    # =========================================================================
    {
        "q_num": "SC-01",
        "category": "Spinal Cord",
        "stem": "A 24-year-old man is stabbed in the back. Neurological examination reveals a hemisection of the spinal cord on the right side at the level of T8 (Brown-Séquard syndrome). Which of the following sets of neurological findings is expected below the level of the lesion?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Ipsilateral loss of pain/temperature; contralateral motor paralysis and vibration loss"},
            {"letter": "B", "is_correct": True, "text": "Ipsilateral spastic motor paralysis and vibration/proprioception loss; contralateral pain and temperature loss"},
            {"letter": "C", "is_correct": False, "text": "Bilateral flaccid paraplegia and bilateral pain/temperature loss"},
            {"letter": "D", "is_correct": False, "text": "Bilateral loss of vibration and proprioception with preserved pain/temperature and motor strength"},
            {"letter": "E", "is_correct": False, "text": "Contralateral spastic paralysis; ipsilateral pain and temperature loss"}
        ],
        "explanation": "Correct Answer: B. Ipsilateral spastic motor paralysis and vibration/proprioception loss; contralateral pain and temperature loss.\n\nBrown-Séquard syndrome (spinal cord hemisection):\n• Lateral corticospinal tract: Ipsilateral spastic paresis below the lesion (tract crosses at caudal medulla).\n• Dorsal columns: Ipsilateral loss of vibration, proprioception, and fine touch below the lesion (tract crosses at caudal medulla).\n• Spinothalamic tract: Contralateral loss of pain and temperature sensation starting 1-2 dermatomes below the lesion (fibers cross 1-2 segments above in the anterior white commissure).\n• At the level of the lesion: Ipsilateral complete sensory loss and LMN paralysis."
    },
    {
        "q_num": "SC-02",
        "category": "Spinal Cord",
        "stem": "A 56-year-old man presents with progressive weakness and muscle wasting. Physical examination reveals asymmetric fasciculations and atrophy of the intrinsic hand muscles, along with hyperactive biceps and patellar reflexes, sustained ankle clonus, and positive Hoffman and Babinski signs. Sensory examination is completely normal. No bowel or bladder dysfunction is present. Genetic testing in familial cases frequently identifies mutations in SOD1 or C9orf72. What is the diagnosis?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Myasthenia gravis"},
            {"letter": "B", "is_correct": False, "text": "Guillain-Barré syndrome"},
            {"letter": "C", "is_correct": True, "text": "Amyotrophic lateral sclerosis (ALS)"},
            {"letter": "D", "is_correct": False, "text": "Poliomyelitis"},
            {"letter": "E", "is_correct": False, "text": "Multiple sclerosis"}
        ],
        "explanation": "Correct Answer: C. Amyotrophic lateral sclerosis (ALS).\n\nAmyotrophic Lateral Sclerosis (ALS / Lou Gehrig disease) is characterized by combined Upper Motor Neuron (UMN) and Lower Motor Neuron (LMN) degeneration without sensory or autonomic deficits:\n• LMN signs: Muscle atrophy, weakness, fasciculations (anterior horn degeneration).\n• UMN signs: Hyperreflexia, spasticity, clonus, extensor plantar response (corticospinal tract degeneration).\n• Pathology: Cytoplasmic aggregates of TDP-43 (TAR DNA-binding protein 43). In familial cases, mutations involve SOD1 (superoxide dismutase 1) or C9orf72 hexanucleotide repeat expansions.\n• Treatment: Riluzole (decreases glutamate excitotoxicity) and Edaravone (free radical scavenger)."
    },
    {
        "q_num": "SC-03",
        "category": "Spinal Cord",
        "stem": "A 68-year-old man with severe cervical spondylosis is involved in a rear-end motor vehicle collision resulting in hyperextension of his neck. Following the accident, he exhibits severe weakness of both upper extremities (strength 1/5 in hands and arms), while strength in both lower extremities is relatively preserved (strength 4/5). Sensation to pinprick and temperature is diminished across his shoulders and arms, but intact in his legs. MRI reveals an acute central cervical cord hematoma/contusion. What spinal cord syndrome is present?",
        "options": [
            {"letter": "A", "is_correct": True, "text": "Central cord syndrome"},
            {"letter": "B", "is_correct": False, "text": "Anterior cord syndrome"},
            {"letter": "C", "is_correct": False, "text": "Posterior cord syndrome"},
            {"letter": "D", "is_correct": False, "text": "Brown-Séquard syndrome"},
            {"letter": "E", "is_correct": False, "text": "Conus medullaris syndrome"}
        ],
        "explanation": "Correct Answer: A. Central cord syndrome.\n\nCentral cord syndrome is the most common incomplete spinal cord injury, typically occurring in elderly patients with pre-existing cervical spondylosis following a hyperextension injury:\n• Pathophysiology: Compression damages the central gray matter and medial aspects of the lateral corticospinal tracts.\n• Clinical presentation: Motor deficits are vastly more severe in the upper extremities than in the lower extremities. This occurs because fibers in the corticospinal tract are somatotopically laminated from medial to lateral: cervical fibers are most medial (closest to the central lesion), while thoracic, lumbar, and sacral fibers are situated laterally.\n• Variable sensory loss (cape-like distribution) occurs from anterior white commissure disruption."
    },
    {
        "q_num": "SC-04",
        "category": "Spinal Cord",
        "stem": "A 16-year-old boy presents with progressive gait unsteadiness, frequent falls, and scoliosis. Examination reveals marked sensory ataxia, absent deep tendon reflexes in the lower extremities, bilateral extensor plantar responses, and dysarthria. He has prominent pes cavus (high arched feet) and hammer toes. Echocardiogram reveals hypertrophic cardiomyopathy. Genetic testing demonstrates an expanded GAA trinucleotide repeat in the FXN gene on chromosome 9. What is the diagnosis?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Huntington disease"},
            {"letter": "B", "is_correct": True, "text": "Friedreich ataxia"},
            {"letter": "C", "is_correct": False, "text": "Charcot-Marie-Tooth disease"},
            {"letter": "D", "is_correct": False, "text": "Ataxia-telangiectasia"},
            {"letter": "E", "is_correct": False, "text": "Spinal muscular atrophy"}
        ],
        "explanation": "Correct Answer: B. Friedreich ataxia.\n\nFriedreich Ataxia is an autosomal recessive neurodegenerative disease caused by a GAA trinucleotide repeat expansion in the FXN gene (encoding frataxin, an iron-binding mitochondrial protein). Impaired iron handling causes mitochondrial dysfunction and oxidative stress:\n• Spinal cord pathology: Demyelination of the dorsal columns (sensory ataxia, loss of vibration/proprioception), lateral corticospinal tracts (spasticity, Babinski sign), and spinocerebellar tracts (ataxia, dysmetria).\n• Systemic features: Hypertrophic cardiomyopathy (leading cause of death), diabetes mellitus (beta-cell dysfunction), kyphoscoliosis, and pes cavus with hammer toes."
    },
    {
        "q_num": "SC-05",
        "category": "Spinal Cord",
        "stem": "A 45-year-old man presents with acute-onset bilateral lower extremity weakness, severe lower back pain, saddle anesthesia (numbness in the perineal region, perianal area, and inner thighs), and acute urinary retention with overflow incontinence. Examination shows lax anal sphincter tone and absent bulbocavernosus reflex. MRI confirms a massive herniated L4-L5 intervertebral disc compressing the nerve roots in the lumbar thecal sac. What condition is present, and what is the urgent management?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Conus medullaris syndrome; Conservative management with physical therapy"},
            {"letter": "B", "is_correct": True, "text": "Cauda equina syndrome; Urgent surgical decompressive laminectomy"},
            {"letter": "C", "is_correct": False, "text": "Anterior spinal artery syndrome; Intravenous thrombolysis"},
            {"letter": "D", "is_correct": False, "text": "Guillain-Barré syndrome; Plasma exchange"},
            {"letter": "E", "is_correct": False, "text": "Transverse myelitis; High-dose intravenous methylprednisolone"}
        ],
        "explanation": "Correct Answer: B. Cauda equina syndrome; Urgent surgical decompressive laminectomy.\n\nCauda Equina Syndrome (CES) is a surgical emergency caused by compression of the spinal nerve roots (L2 through coccygeal) below the conus medullaris (most commonly a massive midline disc herniation):\n• Hallmarks: Severe lower back/radicular pain, asymmetric lower extremity LMN weakness, saddle anesthesia (S3-S5 dermatomes), loss of rectal tone/incontinence, and urinary retention.\n• Management: Immediate MRI followed by emergent surgical decompression within 24-48 hours to prevent permanent paraplegia and permanent bladder/bowel incontinence."
    },
    {
        "q_num": "SC-06",
        "category": "Spinal Cord",
        "stem": "Differentiating cauda equina syndrome from conus medullaris syndrome is a classic clinical challenge. Which of the following clinical features is most characteristic of conus medullaris syndrome compared to cauda equina syndrome?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Marked asymmetrical radicular pain radiating down one leg"},
            {"letter": "B", "is_correct": False, "text": "Pure lower motor neuron flaccid paralysis of the legs with areflexia"},
            {"letter": "C", "is_correct": True, "text": "Early, symmetric bilateral perineal numbness with sudden urinary and fecal incontinence and mixed UMN/LMN signs"},
            {"letter": "D", "is_correct": False, "text": "Complete absence of sphincter disturbance"},
            {"letter": "E", "is_correct": False, "text": "Gradual onset over several months"}
        ],
        "explanation": "Correct Answer: C. Early, symmetric bilateral perineal numbness with sudden urinary and fecal incontinence and mixed UMN/LMN signs.\n\nComparison of Conus Medullaris vs Cauda Equina:\n• Conus Medullaris (injury to sacral cord segments at L1-L2 vertebra): Sudden onset, bilateral and SYMMETRICAL saddle sensory loss, early severe urinary/fecal incontinence, mild symmetrical motor weakness, and mixed UMN/LMN signs (e.g., hyperreflexia or Babinski sign combined with absent ankle reflexes).\n• Cauda Equina (injury to lumbosacral nerve roots below L2): Gradual onset, severe ASYMMETRICAL radicular pain, asymmetric flaccid LMN weakness with areflexia, and late sphincter dysfunction."
    },
    {
        "q_num": "SC-07",
        "category": "Spinal Cord",
        "stem": "A 3-month-old infant is evaluated for profound generalized hypotonia, weakness, and poor feeding. Physical examination demonstrates marked muscle wasting, absent deep tendon reflexes, and prominent tongue fasciculations. Sensation appears normal. The infant rests in a 'frog-leg' posture and cannot lift his head. Genetic testing confirms a homozygous deletion of the SMN1 gene on chromosome 5q. What is the diagnosis?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Duchenne muscular dystrophy"},
            {"letter": "B", "is_correct": True, "text": "Spinal muscular atrophy type 1 (Werdnig-Hoffmann disease)"},
            {"letter": "C", "is_correct": False, "text": "Infant botulism"},
            {"letter": "D", "is_correct": False, "text": "Charcot-Marie-Tooth disease"},
            {"letter": "E", "is_correct": False, "text": "Pompe disease"}
        ],
        "explanation": "Correct Answer: B. Spinal muscular atrophy type 1 (Werdnig-Hoffmann disease).\n\nSpinal Muscular Atrophy (SMA) type 1 (Werdnig-Hoffmann disease) is an autosomal recessive disorder caused by homozygous deletion or mutation of the SMN1 (survival motor neuron 1) gene on chromosome 5q13:\n• Pathophysiology: Splicing defect leads to degeneration of anterior horn alpha motor neurons in the spinal cord and cranial nerve motor nuclei.\n• Manifestations: Severe symmetrical proximal hypotonia ('floppy infant'), tongue fasciculations, bell-shaped chest from intercostal muscle weakness (sparing diaphragm), and death from respiratory failure before age 2 without treatment.\n• Treatment: Nusinersen (antisense oligonucleotide promoting inclusion of exon 7 in SMN2 pre-mRNA) or Onasemnogene abeparvovec (gene replacement therapy)."
    },
    {
        "q_num": "SC-08",
        "category": "Spinal Cord",
        "stem": "During a neurological exam, deep tendon reflexes are tested to evaluate the integrity of the spinal reflex arc. Testing the Achilles tendon reflex (ankle jerk) primarily evaluates which spinal nerve root?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "L2-L3"},
            {"letter": "B", "is_correct": False, "text": "L3-L4"},
            {"letter": "C", "is_correct": False, "text": "L4-L5"},
            {"letter": "D", "is_correct": True, "text": "S1-S2"},
            {"letter": "E", "is_correct": False, "text": "S3-S4"}
        ],
        "explanation": "Correct Answer: D. S1-S2.\n\nSpinal reflex arc nerve roots (remember the counting mnemonic: 1, 2, 3, 4, 5, 6, 7, 8):\n• S1, S2: Achilles reflex (ankle jerk)\n• L3, L4: Patellar reflex (knee jerk)\n• C5, C6: Biceps and Brachioradialis reflexes\n• C7, C8: Triceps reflex"
    },
    {
        "q_num": "SC-09",
        "category": "Spinal Cord",
        "stem": "An adult male sustains an acute spinal cord transection at the T4 level following a motor vehicle crash. Immediately following the injury, he exhibits spinal shock. Which of the following sets of physiological findings characterizes the phase of acute spinal shock?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Spastic paralysis, hyperreflexia, and sustained ankle clonus"},
            {"letter": "B", "is_correct": True, "text": "Flaccid paralysis, absent deep tendon reflexes, loss of autonomic tone, and urinary retention with overflow incontinence"},
            {"letter": "C", "is_correct": False, "text": "Hyperactive deep tendon reflexes with preserved sensation"},
            {"letter": "D", "is_correct": False, "text": "Severe hypertension and tachycardia from sympathetic storm"},
            {"letter": "E", "is_correct": False, "text": "Fasciculations and spastic bladder"}
        ],
        "explanation": "Correct Answer: B. Flaccid paralysis, absent deep tendon reflexes, loss of autonomic tone, and urinary retention with overflow incontinence.\n\nImmediately following acute traumatic spinal cord transection, the patient enters spinal shock, characterized by temporary loss of all cord functions below the lesion:\n• Complete flaccid paralysis and areflexia (due to sudden loss of descending facilitatory supraspinal drive).\n• Loss of autonomic tone (neurogenic shock: hypotension, bradycardia from loss of sympathetic output T1-L2).\n• Atonic, flaccid bladder with overflow incontinence and absent anal sphincter tone.\nAfter several days to weeks, spinal shock resolves and transitions into chronic upper motor neuron findings: spasticity, hyperreflexia, Babinski sign, and a hyperreflexic/spastic neurogenic bladder."
    },
    {
        "q_num": "SC-10",
        "category": "Spinal Cord",
        "stem": "A 32-year-old woman presents with subacute onset of bilateral lower extremity weakness, numbness from her umbilicus down to her toes, and urinary urgency. Sensation to pinprick, temperature, and light touch is completely absent below the T10 dermatome. Spinal MRI shows a focal, high-signal T2 lesion with gadolinium enhancement spanning more than two vertebral segments across the thoracic cord. Cerebrospinal fluid analysis shows mild lymphocytic pleocytosis and elevated IgG index. What is the diagnosis?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Tabes dorsalis"},
            {"letter": "B", "is_correct": True, "text": "Acute transverse myelitis"},
            {"letter": "C", "is_correct": False, "text": "Amyotrophic lateral sclerosis"},
            {"letter": "D", "is_correct": False, "text": "Spinal epidural hematoma"},
            {"letter": "E", "is_correct": False, "text": "Poliomyelitis"}
        ],
        "explanation": "Correct Answer: B. Acute transverse myelitis.\n\nAcute Transverse Myelitis is an inflammatory, immune-mediated demyelinating disorder affecting the entire cross-section of the spinal cord (most commonly thoracic):\n• Clinical presentation: Rapidly progressive bilateral motor weakness, a sharply defined sensory level (umbilicus = T10 dermatome), and sphincter dysfunction (urinary urgency/retention).\n• Etiology: Idiopathic post-infectious, or associated with multiple sclerosis, neuromyelitis optica (anti-AQP4), or systemic lupus erythematosus.\n• MRI: T2 hyperintensity with patchy gadolinium enhancement extending across the spinal cord cross-section."
    },
    {
        "q_num": "SC-11",
        "category": "Spinal Cord",
        "stem": "The spinal cord ends caudally as the conus medullaris. At which vertebral level does the conus medullaris terminate in the normal adult?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "T10–T11"},
            {"letter": "B", "is_correct": False, "text": "T12–L1"},
            {"letter": "C", "is_correct": True, "text": "L1–L2"},
            {"letter": "D", "is_correct": False, "text": "L3–L4"},
            {"letter": "E", "is_correct": False, "text": "S1–S2"}
        ],
        "explanation": "Correct Answer: C. L1–L2.\n\nIn adults, the conus medullaris (the tapered lower end of the spinal cord) typically terminates at the level of the L1-L2 intervertebral disc space (range: T12 to lower L2). The dural sac and subarachnoid space continue down to the level of S2. This anatomical arrangement creates the lumbar cistern (between L2 and S2), which contains only the cauda equina and CSF, allowing safe insertion of a lumbar puncture needle at L3-L4 or L4-L5 without injuring the spinal cord."
    },
    {
        "q_num": "SC-12",
        "category": "Spinal Cord",
        "stem": "Which fibrous strand of connective tissue is derived from the pia mater, extends from the tip of the conus medullaris through the lumbar cistern, and fuses with the dura mater at S2 to anchor the spinal cord to the coccyx?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Denticulate ligament"},
            {"letter": "B", "is_correct": True, "text": "Filum terminale"},
            {"letter": "C", "is_correct": False, "text": "Ligamentum flavum"},
            {"letter": "D", "is_correct": False, "text": "Posterior longitudinal ligament"},
            {"letter": "E", "is_correct": False, "text": "Tectorial membrane"}
        ],
        "explanation": "Correct Answer: B. Filum terminale.\n\nThe filum terminale is a delicate filament of fibrous tissue extending from the apex of the conus medullaris to the coccyx:\n• Filum terminale internum: Upper portion within the dural sac, composed of pia mater bathed in CSF.\n• Filum terminale externum (coccygeal ligament): Lower portion outside the dural sac (below S2), composed of fused pia and dura mater, anchoring the spinal cord to the dorsum of the coccyx.\nTethered cord syndrome occurs when an abnormally thick or tight filum terminale restricts physiological motion of the spinal cord."
    },
    {
        "q_num": "SC-13",
        "category": "Spinal Cord",
        "stem": "In the spinal cord white matter, the lateral corticospinal tract contains descending motor axons organized somatotopically. Which of the following correctly describes the somatotopic arrangement of fibers in the lateral corticospinal tract from medial to lateral?",
        "options": [
            {"letter": "A", "is_correct": True, "text": "Cervical → Thoracic → Lumbar → Sacral"},
            {"letter": "B", "is_correct": False, "text": "Sacral → Lumbar → Thoracic → Cervical"},
            {"letter": "C", "is_correct": False, "text": "Lumbar → Sacral → Cervical → Thoracic"},
            {"letter": "D", "is_correct": False, "text": "Thoracic → Cervical → Sacral → Lumbar"},
            {"letter": "E", "is_correct": False, "text": "Sacral fibers are medial; Cervical fibers are lateral"}
        ],
        "explanation": "Correct Answer: A. Cervical → Thoracic → Lumbar → Sacral.\n\nIn both the lateral corticospinal tract and the spinothalamic tract, fibers are laminated somatotopically:\n• Lateral corticospinal tract: Cervical fibers lie most MEDIALLY (nearest the gray matter), while Sacral fibers lie most LATERALLY (nearest the cord surface). This explains why a central cord injury (hyperextension) selectively damages medial/cervical fibers, paralyzing the arms while sparing the legs.\n• Spinothalamic tract: Cervical fibers are MEDIAL, while sacral fibers are LATERAL. Extrinsic compression of the cord (e.g., meningioma) compresses the superficial sacral fibers first, causing sensory loss starting at the feet and ascending."
    },
    {
        "q_num": "SC-14",
        "category": "Spinal Cord",
        "stem": "A 5-year-old unvaccinated boy in a developing country develops a febrile illness followed by asymmetric flaccid paralysis of his right leg. Physical examination shows 0/5 strength in the right quadriceps and tibialis anterior with absent patellar and Achilles reflexes. Sensation is completely intact throughout both legs. Cerebrospinal fluid analysis reveals a positive enterovirus PCR. Poliovirus causes pure motor deficits by selectively infecting and destroying which cells?",
        "options": [
            {"letter": "A", "is_correct": True, "text": "Alpha motor neurons in the anterior (ventral) horns of the spinal cord"},
            {"letter": "B", "is_correct": False, "text": "Dorsal root ganglion sensory pseudounipolar neurons"},
            {"letter": "C", "is_correct": False, "text": "Schwann cells in the peripheral motor nerves"},
            {"letter": "D", "is_correct": False, "text": "Oligodendrocytes in the lateral funiculus"},
            {"letter": "E", "is_correct": False, "text": "Pyramidal neurons in the primary motor cortex"}
        ],
        "explanation": "Correct Answer: A. Alpha motor neurons in the anterior (ventral) horns of the spinal cord.\n\nPoliovirus (a single-stranded, positive-sense, non-enveloped RNA picornavirus) selectively targets and replicates in the anterior (ventral) horn alpha motor neurons of the spinal cord (and motor nuclei of the brainstem). Destruction of these lower motor neurons results in asymmetric flaccid paralysis, severe muscle atrophy, and areflexia, with complete preservation of sensory pathways."
    },
    {
        "q_num": "SC-15",
        "category": "Spinal Cord",
        "stem": "Which specialized ligament consists of 21 pairs of tooth-like triangular lateral extensions of pia mater that pass through the arachnoid to anchor the spinal cord to the dura mater, separating the anterior and posterior nerve roots?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Ligamentum nuchae"},
            {"letter": "B", "is_correct": True, "text": "Denticulate ligament"},
            {"letter": "C", "is_correct": False, "text": "Ligamentum flavum"},
            {"letter": "D", "is_correct": False, "text": "Interspinous ligament"},
            {"letter": "E", "is_correct": False, "text": "Cruciate ligament of the atlas"}
        ],
        "explanation": "Correct Answer: B. Denticulate ligament.\n\nThe denticulate ligaments (ligamenta denticulata) are bilateral, ribbon-like lateral shelves of pia mater with 21 tooth-like pointed processes extending from the foramen magnum down to T12-L1. They pierce the arachnoid to attach to the inner surface of the dura mater, suspending the spinal cord within the thecal sac and serving as a crucial surgical landmark separating dorsal sensory roots from ventral motor roots."
    },
    {
        "q_num": "SC-16",
        "category": "Spinal Cord",
        "stem": "A 62-year-old man presents with chronic neck pain and numbness radiating down his right thumb. Examination shows weakness of right elbow flexion and forearm supination, along with a diminished right biceps and brachioradialis reflex. Sensation to pinprick is diminished over the right lateral forearm and thumb. Which cervical intervertebral disc herniation and nerve root is involved?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "C4-C5 disc compressing C4 root"},
            {"letter": "B", "is_correct": False, "text": "C4-C5 disc compressing C5 root"},
            {"letter": "C", "is_correct": True, "text": "C5-C6 disc compressing C6 root"},
            {"letter": "D", "is_correct": False, "text": "C6-C7 disc compressing C7 root"},
            {"letter": "E", "is_correct": False, "text": "C7-T1 disc compressing C8 root"}
        ],
        "explanation": "Correct Answer: C. C5-C6 disc compressing C6 root.\n\nCervical radiculopathy features:\n• In the cervical spine, spinal nerves exit ABOVE their corresponding vertebrae (C1 exits above C1, C6 exits between C5 and C6, C8 exits between C7 and T1). Thus, a C5-C6 herniation compresses the exiting C6 nerve root.\n• C6 radiculopathy findings: Sensory loss in the lateral forearm and thumb; motor weakness of biceps and brachioradialis (elbow flexion); diminished biceps and brachioradialis reflexes.\n• In comparison, C7 radiculopathy causes numbness of the middle finger, triceps weakness, and diminished triceps reflex."
    },
    {
        "q_num": "SC-17",
        "category": "Spinal Cord",
        "stem": "In the spinal cord, preganglionic sympathetic cell bodies are located in the intermediolateral (IML) cell column of the lateral horn. Across which spinal cord segments is the intermediolateral cell column present?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "C1 to C8"},
            {"letter": "B", "is_correct": True, "text": "T1 to L2"},
            {"letter": "C", "is_correct": False, "text": "L1 to S4"},
            {"letter": "D", "is_correct": False, "text": "S2 to S4"},
            {"letter": "E", "is_correct": False, "text": "Entire length of the spinal cord (C1 to Co1)"}
        ],
        "explanation": "Correct Answer: B. T1 to L2.\n\nThe autonomic nervous system anatomy:\n• Sympathetic division (thoracolumbar outflow): Preganglionic cell bodies reside in the intermediolateral (IML) nucleus of the lateral horn from T1 to L2 (or L3).\n• Parasympathetic division (craniosacral outflow): Preganglionic cell bodies reside in cranial nerve nuclei (CN III, VII, IX, X) and sacral cord segments S2, S3, S4."
    },
    {
        "q_num": "SC-18",
        "category": "Spinal Cord",
        "stem": "A 52-year-old woman presents with severe shooting pain down her right buttock, posterior thigh, calf, and sole of the foot. Examination shows weakness of right foot plantarflexion (inability to stand on tiptoes) and an absent right Achilles tendon reflex. Sensation to pinprick is diminished over the lateral border of the right foot and fifth digit. An MRI will most likely demonstrate a herniated disc compressing which nerve root?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "L3"},
            {"letter": "B", "is_correct": False, "text": "L4"},
            {"letter": "C", "is_correct": False, "text": "L5"},
            {"letter": "D", "is_correct": True, "text": "S1"},
            {"letter": "E", "is_correct": False, "text": "S3"}
        ],
        "explanation": "Correct Answer: D. S1.\n\nS1 radiculopathy (typically caused by an L5-S1 posterolateral disc herniation):\n• Motor: Weakness of gastrocnemius/soleus (plantarflexion of the foot; patient cannot stand on toes).\n• Reflex: Absent Achilles tendon (ankle jerk) reflex.\n• Sensory: Numbness/pain along the posterior calf, sole of the foot, lateral foot, and little toe.\n• In contrast, L5 radiculopathy affects foot dorsiflexion / heel walking (extensor hallucis longus) and sensation over the dorsum of the foot and big toe, with normal reflexes."
    },
    {
        "q_num": "SC-19",
        "category": "Spinal Cord",
        "stem": "A 22-year-old athlete sustains a severe spinal cord injury at T1. Several weeks later, full bladder distension triggers paroxysmal episodes of severe hypertension (blood pressure 210/115 mm Hg), pounding headache, profuse diaphoresis and flushing above the level of T1, and cold, pale skin with piloerection below T1. The heart rate is 45 bpm. What life-threatening syndrome is this patient experiencing?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Spinal shock"},
            {"letter": "B", "is_correct": True, "text": "Autonomic dysreflexia (hyperreflexia)"},
            {"letter": "C", "is_correct": False, "text": "Neurogenic shock"},
            {"letter": "D", "is_correct": False, "text": "Pheochromocytoma crisis"},
            {"letter": "E", "is_correct": False, "text": "Malignant hyperthermia"}
        ],
        "explanation": "Correct Answer: B. Autonomic dysreflexia (hyperreflexia).\n\nAutonomic Dysreflexia occurs in patients with spinal cord lesions at or above T6:\n• Trigger: Noxious visceral stimuli below the lesion (most commonly bladder distension, catheter obstruction, or fecal impaction).\n• Mechanism: Massive, uninhibited sympathetic discharge from the isolated splanchnic vascular bed causes severe vasoconstriction and acute hypertension.\n• Response: Carotid baroreceptors detect severe hypertension and stimulate parasympathetic vagal output (producing reflex bradycardia) and cutaneous vasodilation above the lesion (flushing, sweating). However, inhibitory descending central signals cannot cross the T6 cord lesion, leaving uninhibited sympathetic vasoconstriction below the lesion."
    },
    {
        "q_num": "SC-20",
        "category": "Spinal Cord",
        "stem": "Which nucleus in the spinal cord gray matter extends from C8 to L3 (Rexed lamina VII), contains cell bodies of second-order neurons that receive unconscious proprioceptive information from muscle spindles and Golgi tendon organs of the lower body, and gives rise to the dorsal spinocerebellar tract?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Substantia gelatinosa"},
            {"letter": "B", "is_correct": True, "text": "Clarke column (nucleus dorsalis)"},
            {"letter": "C", "is_correct": False, "text": "Nucleus proprius"},
            {"letter": "D", "is_correct": False, "text": "Intermediolateral cell column"},
            {"letter": "E", "is_correct": False, "text": "Accessory nucleus"}
        ],
        "explanation": "Correct Answer: B. Clarke column (nucleus dorsalis).\n\nClarke column (nucleus dorsalis / thoracicus) is located in the medial base of the dorsal horn (Rexed lamina VII) between spinal levels C8 and L3:\n• Function: Relays unconscious proprioceptive signals from lower limb muscle spindles and Golgi tendon organs.\n• Axons project ipsilaterally to form the Dorsal Spinocerebellar Tract, ascending to the cerebellum via the inferior cerebellar peduncle to coordinate lower extremity motor execution."
    }
]

if __name__ == '__main__':
    print(f'Part 2 loaded successfully with {len(part2_questions)} questions.')
