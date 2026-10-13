# -*- coding: utf-8 -*-
# inhouse_section2.py
# Section 2: Motor & Anesthetic Pharmacology
# Covers:
# - Neuromuscular Junction Disorders (LOs 1-3)
# - Myasthenia Gravis, Lambert-Eaton, Botulism, Organophosphate poisoning (Content & Cases)
# - General Anesthesia Principles (MAC, Blood:Gas partition, Lipid:Gas partition)
# - Malignant Hyperthermia (Pathophysiology, RYR1, Dantrolene)
# - Intravenous Anesthetics (Propofol, Etomidate, Ketamine, Midazolam, Dexmedetomidine)
# - Neuromuscular Blockers (Succinylcholine, Rocuronium, Cisatracurium, Hoffman elimination, Reversal)

questions_section2 = [
    # ==========================================
    # NMJ PHYSIOLOGY & MYASTHENIA GRAVIS
    # ==========================================
    {
        "id": "IH_Q076",
        "question_number": 76,
        "category": "In House: Neuromuscular Junction Disorders",
        "stem": "A 32-year-old woman presents with fluctuating double vision and drooping of both eyelids that becomes progressively worse toward the evening, especially after long hours reading or working at her computer. Physical examination reveals bilateral ptosis that worsens after 60 seconds of sustained upward gaze. Applying an ice pack over her closed eyelids for 2 minutes produces significant resolution of the ptosis (positive ice pack test). Repetitive nerve stimulation at 3 Hz demonstrates a progressive decrement in compound muscle action potential (CMAP) amplitude. What is the primary molecular target of the autoantibodies causing this condition?",
        "options": [
            {"text": "Presynaptic P/Q-type voltage-gated calcium channels", "is_correct": False},
            {"text": "Postsynaptic nicotinic acetylcholine receptors (AChR) on the motor end plate", "is_correct": True},
            {"text": "Synaptic acetylcholinesterase enzyme molecules", "is_correct": False},
            {"text": "Presynaptic vesicle-associated membrane protein (synaptobrevin)", "is_correct": False},
            {"text": "Ryanodine receptor type 1 on the sarcoplasmic reticulum", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. Postsynaptic nicotinic acetylcholine receptors (AChR) on the motor end plate.\n\nMyasthenia gravis (MG) is an autoimmune disorder caused by autoantibodies directed against the nicotinic acetylcholine receptors (AChR) on the postsynaptic motor end plate (found in ~85% of generalized cases; the remainder frequently target muscle-specific kinase, MuSK). Binding of antibodies causes complement-mediated destruction and simplification of postsynaptic junctional folds, along with receptor cross-linking and internalization. This reduces the number of functional AChRs, lowering the amplitude of end plate potentials (EPP) below the threshold needed to trigger muscle action potentials. Fatigability occurs because physiological depletion of presynaptic ACh stores with repetitive use further drops EPP below threshold, producing the classic decremental response on slow (3 Hz) repetitive nerve stimulation.\n\n• Option A is incorrect: Antibodies against presynaptic P/Q-type VGCC cause Lambert-Eaton myasthenic syndrome (LEMS).\n• Option C is incorrect: Acetylcholinesterase is inhibited by drugs like pyridostigmine or toxins like organophosphates, not targeted in MG.\n• Option D is incorrect: Synaptobrevin is cleaved by botulinum neurotoxins B, D, F, G.\n• Option E is incorrect: Ryanodine receptor mutations cause malignant hyperthermia."
    },
    {
        "id": "IH_Q077",
        "question_number": 77,
        "category": "In House: Neuromuscular Junction Disorders",
        "stem": "A 35-year-old woman is newly diagnosed with generalized myasthenia gravis after presenting with ptosis, diplopia, and difficulty chewing. Contrast-enhanced CT of the chest is ordered as part of the initial diagnostic evaluation. What mediastinal pathology is most commonly associated with myasthenia gravis, for which surgical thymectomy offers a high probability of clinical improvement or complete remission?",
        "options": [
            {"text": "Posterior mediastinal schwannoma", "is_correct": False},
            {"text": "Thymic follicular hyperplasia (65-75%) or Thymoma (10-15%) in the anterior mediastinum", "is_correct": True},
            {"text": "Middle mediastinal bronchogenic cyst", "is_correct": False},
            {"text": "Substernal thyroid goiter extending into the tracheoesophageal groove", "is_correct": False},
            {"text": "Small cell lung carcinoma with subcarinal lymphadenopathy", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. Thymic follicular hyperplasia (65-75%) or Thymoma (10-15%) in the anterior mediastinum.\n\nThe thymus plays an essential role in the pathogenesis of myasthenia gravis. The normal thymus contains myoid cells that express nicotinic AChRs. In MG, the anterior mediastinum frequently harbors thymic abnormalities: approximately 65–75% of patients have thymic follicular hyperplasia (germinal center B-cell proliferation), and 10–15% have a thymoma (epithelial neoplasm of the thymus). Chest CT or MRI is mandatory in all newly diagnosed patients with MG. Surgical thymectomy removes the source of autoantigen sensitization and autoreactive T/B cells, leading to substantial clinical improvement or long-term medication-free remission.\n\n• Option A is incorrect: Schwannomas are benign nerve sheath tumors located in the posterior mediastinum, not associated with MG.\n• Option C is incorrect: Bronchogenic cysts are congenital anomalies of the middle mediastinum.\n• Option D is incorrect: Substernal goiters arise from the thyroid gland; while autoimmune thyroiditis can co-occur with MG, thymic pathology is the primary driver.\n• Option E is incorrect: Small cell lung cancer is associated with Lambert-Eaton syndrome, not MG."
    },
    {
        "id": "IH_Q078",
        "question_number": 78,
        "category": "In House: Neuromuscular Junction Disorders",
        "stem": "A 68-year-old man with a 40-pack-year smoking history presents with progressive weakness in his thighs and hips. He has significant difficulty rising from a low chair and climbing stairs. He also reports dry mouth, constipation, and erectile dysfunction. On physical examination, his proximal lower extremity strength is initially 3/5, but after he performs maximum isometric knee extension for 10 seconds, his muscle strength temporarily increases to 5/5. Deep tendon reflexes are absent at rest but reappear immediately following brief exercise. High-frequency (20-50 Hz) repetitive nerve stimulation shows a dramatic incremental increase (>100% CMAP facilitation). What is the underlying pathophysiology of this disorder?",
        "options": [
            {"text": "Autoantibodies against postsynaptic acetylcholine receptors", "is_correct": False},
            {"text": "Autoantibodies against presynaptic P/Q-type voltage-gated calcium channels (VGCC)", "is_correct": True},
            {"text": "Zinc metalloprotease cleavage of presynaptic SNAP-25", "is_correct": False},
            {"text": "Degeneration of lower motor neurons in the spinal cord anterior horn", "is_correct": False},
            {"text": "Toxin-mediated ADP-ribosylation of elongation factor 2", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. Autoantibodies against presynaptic P/Q-type voltage-gated calcium channels (VGCC).\n\nLambert-Eaton Myasthenic Syndrome (LEMS) is an autoimmune disorder caused by autoantibodies directed against presynaptic P/Q-type voltage-gated calcium channels (VGCC) at the motor end plate and autonomic synapses. This blocks action-potential triggered calcium influx, preventing acetylcholine vesicle exocytosis and reducing baseline quantal release. Hallmark features include: (1) Proximal lower limb weakness (difficulty rising from chairs), (2) Autonomic dysfunction (dry mouth, erectile dysfunction, constipation) due to impaired parasympathetic/sympathetic transmission, (3) Hyporeflexia/areflexia, and (4) Post-exercise facilitation: brief muscle contraction or high-frequency repetitive nerve stimulation accumulates residual intracellular calcium in the presynaptic terminal, overcoming the block and triggering an INCREMENTAL recruitment of CMAP (>100% increase). Over 50-60% of LEMS cases occur as a paraneoplastic syndrome associated with Small Cell Lung Cancer (SCLC).\n\n• Option A is incorrect: MG features postsynaptic anti-AChR antibodies, decremental response, ocular weakness, and worsens with use.\n• Option C is incorrect: Cleavage of SNAP-25 is the mechanism of botulinum toxin A and E.\n• Option D is incorrect: Anterior horn cell loss characterizes Amyotrophic Lateral Sclerosis (ALS) and Spinal Muscular Atrophy (SMA).\n• Option E is incorrect: Inactivation of EF-2 is the mechanism of Diphtheria and Pseudomonas exotoxins."
    },
    {
        "id": "IH_Q079",
        "question_number": 79,
        "category": "In House: Neuromuscular Junction Disorders",
        "stem": "A 4-month-old infant is brought to the emergency department with severe constipation for 3 days, followed by poor feeding, a weak feeble cry, and inability to hold up her head. The parents report giving the infant small amounts of raw unpasteurized honey to soothe teething. On examination, the infant is lethargic, markedly hypotonic ('floppy baby'), with bilateral ptosis, sluggish pupillary light reflexes, and absent gag reflex. What is the cellular mechanism of the neurotoxin responsible for this infant's paralysis?",
        "options": [
            {"text": "Blocks postsynaptic glycine receptors in spinal interneurons", "is_correct": False},
            {"text": "Cleaves SNARE proteins (such as synaptobrevin and SNAP-25), preventing acetylcholine exocytosis at peripheral cholinergic synapses", "is_correct": True},
            {"text": "Irreversibly inhibits acetylcholinesterase, leading to cholinergic exhaustion", "is_correct": False},
            {"text": "Permanently opens voltage-gated sodium channels, preventing repolarization", "is_correct": False},
            {"text": "Selectively destroys Schwann cells along motor cranial nerves", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. Cleaves SNARE proteins (such as synaptobrevin and SNAP-25), preventing acetylcholine exocytosis at peripheral cholinergic synapses.\n\nInfant botulism results from ingestion of Clostridium botulinum spores (commonly found in raw honey or soil) that germinate in the immature infant gastrointestinal tract and produce botulinum neurotoxin in vivo. The toxin is a zinc metalloprotease consisting of a heavy chain (mediating endocytosis into cholinergic terminals) and a light chain. The light chain cleaves specific SNARE proteins (SNAP-25, synaptobrevin/VAMP, syntaxin) required for synaptic vesicle docking and fusion. This completely blocks acetylcholine release at the neuromuscular junction (causing descending flaccid paralysis and hypotonia, 'floppy baby') and at parasympathetic autonomic ganglia/end organs (causing constipation, mydriasis, sluggish pupils, dry mouth). In contrast to foodborne botulism in adults (where preformed toxin is ingested), infant botulism involves active intraluminal bacterial colonization and toxin production; it is treated with human-derived botulism immune globulin (BabyBIG).\n\n• Option A is incorrect: Tetanus toxin (tetanospasmin) cleaves synaptobrevin in Renshaw cells and spinal inhibitory interneurons, blocking glycine and GABA release to cause spastic paralysis (trismus, risus sardonicus).\n• Option C is incorrect: Acetylcholinesterase inhibition is the mechanism of organophosphates.\n• Option D is incorrect: Opening voltage-gated Na+ channels is the mechanism of ciguatoxin and batrachotoxin.\n• Option E is incorrect: Botulinum toxin does not damage Schwann cells."
    },
    {
        "id": "IH_Q080",
        "question_number": 80,
        "category": "In House: Neuromuscular Junction Disorders",
        "stem": "A 42-year-old farm worker is rushed to the emergency department after accidentally spraying himself with an undiluted organophosphate insecticide. He presents with diaphoresis, constricted pinpoint pupils (miosis), excessive salivation, lacrimation, vomiting, profuse watery diarrhea, wheezing with bilateral diffuse rales (bronchorrhea), and bradycardia. In addition, his extremities show diffuse muscle fasciculations and severe weakness. Which of the following two pharmacological agents must be administered immediately to reverse both his muscarinic and nicotinic toxic manifestations?",
        "options": [
            {"text": "Physostigmine and Naloxone", "is_correct": False},
            {"text": "Atropine (to block muscarinic receptors) and Pralidoxime (2-PAM, to regenerate phosphorylated acetylcholinesterase at nicotinic and muscarinic synapses)", "is_correct": True},
            {"text": "Scopolamine and Pyridostigmine", "is_correct": False},
            {"text": "Epinephrine and Diphenhydramine", "is_correct": False},
            {"text": "Flumazenil and Dantrolene", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. Atropine (to block muscarinic receptors) and Pralidoxime (2-PAM, to regenerate phosphorylated acetylcholinesterase at nicotinic and muscarinic synapses).\n\nOrganophosphates (e.g., malathion, parathion, sarin) are potent, irreversible inhibitors of acetylcholinesterase (AChE). They covalently phosphorylate the active-site serine residue of AChE, preventing acetylcholine hydrolysis and causing massive acetylcholine accumulation at: (1) Muscarinic receptors: leading to DUMBBELSS (Diarrhea, Urination, Miosis, Bronchospasm/Bronchorrhea, Bradycardia, Emesis, Lacrimation, Salivation/Sweating); (2) Nicotinic receptors at the NMJ: leading to muscle fasciculations, cramping, and depolarizing flaccid muscle weakness/paralysis (including the diaphragm); and (3) CNS receptors: confusion, seizures, coma.\n\nManagement requires two complementary drugs: (1) Atropine: a competitive muscarinic receptor antagonist that rapidly crosses into the CNS, reverses bronchorrhea, bronchospasm, bradycardia, and salivation (titrated until lung secretions clear; does NOT reverse muscle weakness/nicotinic effects); and (2) Pralidoxime (2-PAM): a nucleophilic oxime agent that binds to organophosphate-inhibited AChE and cleaves the phosphate-enzyme bond, regenerating active acetylcholinesterase at both nicotinic neuromuscular junctions (reversing skeletal muscle weakness and fasciculations) and muscarinic sites. Pralidoxime must be given early before chemical 'aging' (spontaneous dealkylation of the organophosphate-enzyme complex) permanently inactivates the enzyme.\n\n• Option A is incorrect: Physostigmine is an AChE inhibitor and would worsen toxicity; naloxone treats opioids.\n• Option C is incorrect: Pyridostigmine is an AChE inhibitor and would exacerbate organophosphate poisoning.\n• Option D is incorrect: Epinephrine and diphenhydramine treat anaphylaxis, not cholinergic poisoning.\n• Option E is incorrect: Flumazenil treats benzodiazepines; dantrolene treats malignant hyperthermia."
    },
    {
        "id": "IH_Q081",
        "question_number": 81,
        "category": "In House: Neuromuscular Junction Disorders",
        "stem": "A 40-year-old woman with known myasthenia gravis maintained on oral pyridostigmine experiences a viral upper respiratory infection. Over 24 hours, she develops severe shortness of breath, inability to clear secretions, tachypnea, paradoxical abdominal breathing, and an inability to count past 10 in a single breath. Negative Inspiratory Force (NIF) is -15 cm H2O (normal < -60 cm H2O) and Forced Vital Capacity (FVC) is 12 mL/kg (critical < 15 mL/kg), indicating impending neuromuscular respiratory failure (myasthenic crisis). What is the most appropriate acute, life-saving disease-modifying treatment protocol?",
        "options": [
            {"text": "Immediate escalation of pyridostigmine to quadruple the daily dose", "is_correct": False},
            {"text": "Emergent intubation/ventilatory support combined with Plasma Exchange (Plasmapheresis) or Intravenous Immunoglobulin (IVIg)", "is_correct": True},
            {"text": "Immediate administration of high-dose succinylcholine to facilitate elective tracheostomy", "is_correct": False},
            {"text": "Subcutaneous injection of edrophonium every 4 hours", "is_correct": False},
            {"text": "Complete cessation of all medications without airway management", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. Emergent intubation/ventilatory support combined with Plasma Exchange (Plasmapheresis) or Intravenous Immunoglobulin (IVIg).\n\nMyasthenic crisis is a life-threatening complication of myasthenia gravis defined by severe respiratory muscle weakness (diaphragm and intercostal muscles) and bulbar failure requiring mechanical ventilatory support. It is commonly precipitated by systemic infections, surgery, emotional stress, or medications (e.g., fluoroquinolones, aminoglycosides, beta-blockers, magnesium). Bedside pulmonary function tests (FVC < 15-20 mL/kg, NIF worse than -20 to -30 cm H2O) indicate the need for prompt elective endotracheal intubation. The acute disease-modifying treatments of choice are: (1) Plasma exchange (plasmapheresis, which physically removes pathogenic anti-AChR autoantibodies from the plasma) or (2) High-dose Intravenous Immunoglobulin (IVIg). High-dose corticosteroids are also initiated, but anticholinesterase inhibitors (pyridostigmine) are often temporarily paused or held while intubated to reduce airway secretions and avoid confusion with cholinergic crisis.\n\n• Option A is incorrect: Escalating pyridostigmine during intubation causes excessive bronchial secretions and risks triggering a cholinergic crisis.\n• Option C is incorrect: Succinylcholine is contraindicated; patients with MG are resistant to depolarizing blockers but prone to phase II block, and intubation is performed with careful airway management.\n• Option D is incorrect: Edrophonium (Tensilon) is ultra-short acting (minutes) and used purely for diagnostic testing, not therapeutic maintenance.\n• Option E is incorrect: Failing to manage the airway in impending respiratory arrest is fatal."
    },
    {
        "id": "IH_Q082",
        "question_number": 82,
        "category": "In House: Anesthetic Pharmacology",
        "stem": "An anesthesiologist is evaluating five different inhalational anesthetics for a surgical procedure. Anesthetic potency is defined by the Minimum Alveolar Concentration (MAC). Which of the following statements correctly defines MAC, and how does MAC relate to the lipid:gas partition coefficient (oil:gas partition coefficient)?",
        "options": [
            {"text": "MAC is the alveolar concentration that induces surgical anesthesia in 99% of patients; MAC is directly proportional to lipid solubility", "is_correct": False},
            {"text": "MAC is the minimum alveolar concentration at 1 atmosphere that prevents movement in response to a standard surgical incision in 50% of patients; MAC is inversely proportional to lipid solubility (1/MAC = potency)", "is_correct": True},
            {"text": "MAC represents the concentration of gas that dissolves in blood; high MAC indicates high blood solubility", "is_correct": False},
            {"text": "MAC is the dose required to eliminate spontaneous breathing in 100% of patients; unrelated to lipid solubility", "is_correct": False},
            {"text": "MAC is inversely proportional to the speed of induction; high MAC means fastest induction", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. MAC is the minimum alveolar concentration at 1 atmosphere that prevents movement in response to a standard surgical incision in 50% of patients; MAC is inversely proportional to lipid solubility (1/MAC = potency).\n\nMinimum Alveolar Concentration (MAC) is the standardized measure of inhalational anesthetic potency. It is defined as the alveolar partial pressure (percentage of 1 atmosphere) of an inhaled anesthetic at steady state that prevents purposeful skeletal muscle movement in response to a standardized noxious surgical stimulus (skin incision) in 50% of subjects. According to the Meyer-Overton correlation, anesthetic potency is directly determined by lipid solubility: drugs with high lipid:gas (oil:gas) partition coefficients easily cross the hydrophobic neuronal lipid bilayer, requiring very low alveolar concentrations to achieve anesthesia (LOW MAC = HIGH POTENCY). Conversely, drugs with low lipid solubility (e.g., Nitrous Oxide, MAC = 104%) have very LOW potency and a HIGH MAC.\n\n• Option A is incorrect: MAC represents the ED50 (50% of patients), not 99%; and MAC is inversely (not directly) related to lipid solubility.\n• Option C is incorrect: Blood solubility is measured by the blood:gas partition coefficient, not MAC.\n• Option D is incorrect: MAC measures somatic movement to pain in 50% of patients, not apnea.\n• Option E is incorrect: Speed of induction is governed by the blood:gas partition coefficient, not MAC."
    },
    {
        "id": "IH_Q083",
        "question_number": 83,
        "category": "In House: Anesthetic Pharmacology",
        "stem": "During an operative case, an anesthesia resident needs an inhalational anesthetic that provides the most rapid rate of induction and the fastest, cleanest emergence (wake-up) from anesthesia, particularly in a morbidly obese patient. Which physical property of an inhaled gas determines the speed of anesthetic induction and emergence, and which commonly used volatile anesthetic possesses the lowest blood:gas partition coefficient?",
        "options": [
            {"text": "Lipid:gas partition coefficient; Halothane", "is_correct": False},
            {"text": "Blood:gas partition coefficient; Desflurane (0.42)", "is_correct": True},
            {"text": "Molecular weight of the gas; Isoflurane", "is_correct": False},
            {"text": "Vapor pressure at 20°C; Sevoflurane", "is_correct": False},
            {"text": "Renal clearance rate; Enflurane", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. Blood:gas partition coefficient; Desflurane (0.42).\n\nThe speed of induction and recovery (emergence) of an inhalational anesthetic is governed strictly by its solubility in blood, represented by the Blood:Gas Partition Coefficient:\n1. Low blood:gas coefficient (insoluble in blood, e.g., Desflurane = 0.42, Nitrous Oxide = 0.47, Sevoflurane = 0.65): Very little gas dissolves in the blood reservoir. Consequently, the blood becomes saturated almost immediately, allowing alveolar partial pressure to rise rapidly and equilibrate quickly with brain partial pressure. This produces RAPID induction and RAPID emergence.\n2. High blood:gas coefficient (highly soluble in blood, e.g., Halothane = 2.4, Isoflurane = 1.4): Blood acts as a large sponge that soaks up the gas. The alveolar and arterial partial pressures rise very slowly, delaying brain saturation and resulting in SLOW induction and SLOW emergence.\nIn morbidly obese patients, lipophilic gases also accumulate in adipose tissue; therefore, Desflurane's extremely low blood:gas coefficient (0.42) ensures the quickest emergence with minimal hangover.\n\n• Option A is incorrect: Lipid:gas determines POTENCY (MAC), not speed of induction; halothane has very slow induction (blood:gas = 2.4).\n• Option C is incorrect: Molecular weight does not determine induction speed.\n• Option D is incorrect: Vapor pressure dictates vaporizer calibration, not induction velocity.\n• Option E is incorrect: Inhalational agents are eliminated through alveolar exhalation, not renal clearance."
    },
    {
        "id": "IH_Q084",
        "question_number": 84,
        "category": "In House: Anesthetic Pharmacology",
        "stem": "A 22-year-old healthy man undergoes an emergency exploratory laparotomy following a blunt abdominal trauma. General anesthesia is induced with intravenous propofol, fentanyl, and succinylcholine, followed by endotracheal intubation. Anesthesia is maintained with inhaled sevoflurane. Fifteen minutes into the operation, the patient suddenly develops severe masseter muscle rigidity, sinus tachycardia (145 bpm), marked hypertension, and an alarming rise in end-tidal CO2 (EtCO2 from 38 to 92 mm Hg) refractory to increased minute ventilation. His core body temperature begins rising rapidly at a rate of 1°C every 5 minutes, reaching 40.5°C (104.9°F). Arterial blood gas reveals severe mixed metabolic and respiratory acidosis (pH 7.08, pCO2 78 mm Hg, lactate 9.2 mmol/L), and serum potassium is 6.8 mEq/L. What is the diagnosis, and what inherited gene mutation is most commonly responsible?",
        "options": [
            {"text": "Neuroleptic malignant syndrome; Dopamine D2 receptor deletion", "is_correct": False},
            {"text": "Malignant Hyperthermia; Autosomal dominant mutation in the skeletal muscle Ryanodine Receptor 1 (RYR1) gene", "is_correct": True},
            {"text": "Serotonin syndrome; 5-HT2A receptor gene duplication", "is_correct": False},
            {"text": "Thyroid storm; TSH receptor activating mutation", "is_correct": False},
            {"text": "Pheochromocytoma crisis; RET proto-oncogene mutation", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. Malignant Hyperthermia; Autosomal dominant mutation in the skeletal muscle Ryanodine Receptor 1 (RYR1) gene.\n\nMalignant Hyperthermia (MH) is a life-threatening, pharmacogenetic hypermetabolic crisis of skeletal muscle triggered by exposure to volatile halogenated anesthetics (sevoflurane, desflurane, isoflurane, halothane) and/or the depolarizing paralytic succinylcholine. It is inherited in an autosomal dominant pattern with variable penetrance, most commonly caused by gain-of-function mutations in the Ryanodine Receptor type 1 (RYR1) gene located on chromosome 19q13.1 (or less commonly CACNA1S, encoding the L-type voltage-gated calcium channel / dihydropyridine receptor). Exposure to triggering agents causes uncontrolled, massive calcium release from the sarcoplasmic reticulum into the myoplasm. This drives persistent actin-myosin cross-bridging, causing generalized muscle rigidity (masseter spasm), massive ATP consumption, aerobic and anaerobic hypermetabolism, extreme hypercapnia (rising EtCO2, the earliest and most sensitive sign), severe metabolic acidosis, rhabdomyolysis, hyperkalemia, and dangerous hyperthermia.\n\n• Option A is incorrect: Neuroleptic malignant syndrome (NMS) is caused by dopamine antagonists (antipsychotics) over days, not acute volatile anesthetics during surgery.\n• Option C is incorrect: Serotonin syndrome is triggered by serotonergic agents and features clonus, hyperreflexia, and tremor, without masseter spasm.\n• Option D is incorrect: Thyroid storm causes hyperthermia and tachycardia, but not acute masseter rigidity or extreme CO2 production from volatile gases.\n• Option E is incorrect: Pheochromocytoma causes paroxysmal hypertension, not acute rigid hypermetabolism triggered by halogenated gases."
    },
    {
        "id": "IH_Q085",
        "question_number": 85,
        "category": "In House: Anesthetic Pharmacology",
        "stem": "In the patient described with acute Malignant Hyperthermia, which of the following interventions represents the specific, definitive pharmacological antidote, and what is its molecular mechanism of action?",
        "options": [
            {"text": "Dantrolene; binds to the Ryanodine Receptor 1 (RYR1) and blocks calcium release from the sarcoplasmic reticulum into the skeletal muscle myoplasm", "is_correct": True},
            {"text": "Bromocriptine; stimulates central dopamine D2 receptors to reset hypothalamic set-point", "is_correct": False},
            {"text": "Cyproheptadine; blocks 5-HT2A serotonin receptors", "is_correct": False},
            {"text": "Pralidoxime; regenerates phosphorylated acetylcholinesterase", "is_correct": False},
            {"text": "Sugammadex; encapsulates and inactivates free volatile anesthetic molecules", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Dantrolene; binds to the Ryanodine Receptor 1 (RYR1) and blocks calcium release from the sarcoplasmic reticulum into the skeletal muscle myoplasm.\n\nDantrolene is the specific, life-saving antidote for Malignant Hyperthermia. It is a skeletal muscle relaxant that binds directly to the Ryanodine Receptor 1 (RYR1) channel complex on the sarcoplasmic reticulum membrane, blocking channel opening and preventing further calcium efflux into the myoplasm. This uncouples excitation-contraction coupling, halts hypermetabolism, resolves muscle rigidity, normalizes EtCO2, and stops heat production. Immediate management steps for MH: (1) Discontinue triggering volatile agents and succinylcholine, (2) Hyperventilate with 100% O2 at high flows, (3) Administer IV Dantrolene (2.5 mg/kg bolus, repeated until signs abate), (4) Active cooling, and (5) Treat hyperkalemia and acidosis (calcium chloride, sodium bicarbonate, insulin/glucose).\n\n• Option B is incorrect: Bromocriptine is a dopamine agonist used to treat Neuroleptic Malignant Syndrome.\n• Option C is incorrect: Cyproheptadine is a serotonin antagonist used to treat Serotonin Syndrome.\n• Option D is incorrect: Pralidoxime treats organophosphate poisoning.\n• Option E is incorrect: Sugammadex encapsulates aminosteroid neuromuscular blockers (rocuronium/vecuronium); it has no effect on volatile anesthetics or MH."
    },
    {
        "id": "IH_Q086",
        "question_number": 86,
        "category": "In House: Anesthetic Pharmacology",
        "stem": "A 4-year-old girl is scheduled for bilateral myringotomy and tympanostomy tube placement (ear tubes). The pediatric anesthesiologist elects to use intramuscular ketamine for conscious sedation. Which of the following constellations of cardiovascular, respiratory, and central nervous system effects is characteristic of ketamine?",
        "options": [
            {"text": "Profound respiratory depression, severe bradycardia, and anterograde amnesia without analgesia", "is_correct": False},
            {"text": "NMDA receptor antagonism producing 'dissociative anesthesia', potent somatic analgesia, bronchodilation, sympathomimetic stimulation (increased BP and HR), and potential emergence delirium with vivid hallucinations", "is_correct": True},
            {"text": "GABA-A agonism with severe peripheral vasodilation, blunted airway reflexes, and adrenocortical suppression", "is_correct": False},
            {"text": "Alpha-2 adrenergic agonism causing bradycardia, sedation with easy arousability, and profound hypothermia", "is_correct": False},
            {"text": "Mu-opioid agonism producing chest wall rigidity, miosis, and delayed gastric emptying", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. NMDA receptor antagonism producing 'dissociative anesthesia', potent somatic analgesia, bronchodilation, sympathomimetic stimulation (increased BP and HR), and potential emergence delirium with vivid hallucinations.\n\nKetamine is a phencyclidine (PCP) derivative that acts as a non-competitive antagonist at NMDA glutamate receptors. It induces 'dissociative anesthesia', characterized by a cataleptic state where the patient appears awake (eyes may remain open with slow nystagmus) but is profoundly detached from the environment, completely amnestic, and experiencing potent somatic analgesia. Key clinical properties include: (1) Airway and respiration: Preserves spontaneous respiration, maintains protective pharyngeal/laryngeal airway reflexes, and acts as a potent bronchodilator (ideal for patients with active asthma); (2) Hemodynamics: Centrally stimulates sympathetic outflow, inhibiting catecholamine reuptake, resulting in increased heart rate, blood pressure, and cardiac output; (3) Emergence delirium: Adults and older children can experience vivid, disturbing dreams, hallucinations, and agitation upon emergence (preventable by co-administering a benzodiazepine such as midazolam).\n\n• Option A is incorrect: Ketamine preserves spontaneous respiration and stimulates, rather than depresses, the cardiovascular system.\n• Option C is incorrect: GABA agonism with adrenocortical suppression is characteristic of etomidate.\n• Option D is incorrect: Alpha-2 agonism with arousable sedation describes dexmedetomidine.\n• Option E is incorrect: Mu-opioid agonism with chest wall rigidity describes fentanyl."
    },
    {
        "id": "IH_Q087",
        "question_number": 87,
        "category": "In House: Anesthetic Pharmacology",
        "stem": "A 58-year-old trauma victim with severe hemorrhagic shock from a ruptured spleen requires emergent endotracheal intubation. His blood pressure is 74/42 mm Hg and heart rate is 132 bpm. The anesthesiologist chooses etomidate for rapid sequence induction rather than propofol. What is the major hemodynamic advantage of etomidate, and what specific endocrine adverse effect must clinicians monitor following its administration?",
        "options": [
            {"text": "It causes massive catecholamine release; causes thyroid hormone depletion", "is_correct": False},
            {"text": "It preserves cardiovascular hemodynamic stability (minimal effect on blood pressure and heart rate); causes transient inhibition of 11-beta-hydroxylase, suppressing adrenal cortisol synthesis", "is_correct": True},
            {"text": "It stimulates cardiac beta-1 receptors; causes acute insulin resistance", "is_correct": False},
            {"text": "It prevents bronchospasm; causes acute parathyroid hormone suppression", "is_correct": False},
            {"text": "It selectively stimulates alpha-1 adrenergic receptors; causes hyperaldosteronism", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. It preserves cardiovascular hemodynamic stability (minimal effect on blood pressure and heart rate); causes transient inhibition of 11-beta-hydroxylase, suppressing adrenal cortisol synthesis.\n\nEtomidate is an imidazole derivative that acts as a positive allosteric modulator of GABA-A receptors. Its primary clinical advantage is remarkable hemodynamic stability: it causes minimal to no myocardial depression or peripheral vasodilation, maintaining blood pressure and cardiac output even in critically ill patients with hypovolemia, shock, or severe cardiac disease. In sharp contrast, propofol causes significant peripheral vasodilation and myocardial depression, triggering dangerous hypotension in unstable patients. The classic adverse effect of etomidate is dose-dependent, reversible inhibition of 11β-hydroxylase (the mitochondrial cytochrome P450 enzyme that converts 11-deoxycortisol to cortisol and 11-deoxycorticosterone to corticosterone), which causes transient adrenocortical suppression and blunted cortisol response to stress.\n\n• Option A is incorrect: Etomidate does not stimulate catecholamines and does not inhibit thyroid hormone.\n• Option C is incorrect: Etomidate does not stimulate beta-1 receptors.\n• Option D is incorrect: Ketamine is the primary bronchodilator, and etomidate does not suppress PTH.\n• Option E is incorrect: Etomidate reduces aldosterone and cortisol by inhibiting 11β-hydroxylase, not causing hyperaldosteronism."
    },
    {
        "id": "IH_Q088",
        "question_number": 88,
        "category": "In House: Anesthetic Pharmacology",
        "stem": "A 36-year-old man undergoing shoulder arthroscopy receives intravenous propofol for induction and maintenance of total intravenous anesthesia (TIVA). Propofol is widely used because of its rapid onset and exceptionally smooth, clear-headed recovery. What is the cellular mechanism of action of propofol, and how is its ultrashort duration of action following a single induction bolus terminated?",
        "options": [
            {"text": "NMDA receptor blockade; terminated by rapid glomerular filtration", "is_correct": False},
            {"text": "Potentiation of GABA-A receptor chloride conductance; terminated by rapid redistribution from high-blood-flow vessel-rich organs (brain) to muscle and fat tissues", "is_correct": True},
            {"text": "Inhibition of voltage-gated potassium channels; terminated by pulmonary exhalation", "is_correct": False},
            {"text": "Glycine receptor antagonism; terminated by plasma ester hydrolysis", "is_correct": False},
            {"text": "Direct muscarinic M3 receptor stimulation; terminated by biliary secretion", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. Potentiation of GABA-A receptor chloride conductance; terminated by rapid redistribution from high-blood-flow vessel-rich organs (brain) to muscle and fat tissues.\n\nPropofol (2,6-diisopropylphenol) is an intravenous anesthetic that enhances inhibitory neurotransmission by binding to β-subunits of the GABA-A receptor, prolonging channel open time and increasing chloride conductance to hyperpolarize postsynaptic neurons. Like thiopental, the rapid recovery (<8–10 minutes) following a single intravenous bolus of propofol is governed by REDISTRIBUTION: the drug initially enters vessel-rich organs with high perfusion (brain, heart, kidneys), but quickly redistributes down its concentration gradient into less well-perfused muscle and adipose tissue, dropping brain levels below anesthetic threshold long before hepatic metabolism (CYP2B6 and glucuronidation) clears the drug from the body. Propofol also possesses potent antiemetic properties, making postoperative nausea and vomiting rare.\n\n• Option A is incorrect: NMDA blockade is the mechanism of ketamine; redistribution, not renal filtration, terminates effect.\n• Option C is incorrect: Inhaled anesthetics, not propofol, are cleared via pulmonary exhalation.\n• Option D is incorrect: Ester hydrolysis terminates aminoester local anesthetics, remifentanil, and succinylcholine.\n• Option E is incorrect: Propofol does not stimulate muscarinic receptors."
    },
    {
        "id": "IH_Q089",
        "question_number": 89,
        "category": "In House: Anesthetic Pharmacology",
        "stem": "A 72-year-old woman with end-stage renal disease (ESRD on hemodialysis) and severe cirrhosis with hepatic failure requires general endotracheal anesthesia for repair of a strangulated incisional hernia. The surgical team requires complete skeletal muscle paralysis. Which of the following neuromuscular blocking drugs is the agent of choice because its elimination is completely independent of renal or hepatic function?",
        "options": [
            {"text": "Rocuronium", "is_correct": False},
            {"text": "Vecuronium", "is_correct": False},
            {"text": "Pancuronium", "is_correct": False},
            {"text": "Cisatracurium", "is_correct": True},
            {"text": "Succinylcholine", "is_correct": False}
        ],
        "explanation": "Correct Answer: D. Cisatracurium.\n\nCisatracurium (an isomer of atracurium) is an intermediate-acting non-depolarizing benzylisoquinolinium neuromuscular blocking agent. It possesses a unique, organ-independent route of clearance: it undergoes spontaneous, non-enzymatic chemical degradation in plasma and tissue fluid at normal body temperature and physiological pH via Hofmann elimination (breaking into laudanosine and a monoquaternary acrylate metabolite), as well as non-specific plasma ester hydrolysis. Because its clearance does not rely on renal excretion or hepatic biotransformation, cisatracurium is the premier muscle relaxant of choice in patients with severe renal failure, hepatic cirrhosis, or multiorgan dysfunction in the intensive care unit.\n\n• Option A is incorrect: Rocuronium undergoes significant hepatic uptake and biliary excretion (>70%); its duration is significantly prolonged in liver failure.\n• Option B is incorrect: Vecuronium depends heavily on both hepatic metabolism (50%) and renal excretion (30-40%); active metabolites accumulate in renal failure.\n• Option C is incorrect: Pancuronium is primarily eliminated unchanged by the kidneys (80%); prolonged paralysis occurs in ESRD.\n• Option E is incorrect: Succinylcholine is contraindicated in ESRD due to unpredictable, potentially lethal hyperkalemic release."
    },
    {
        "id": "IH_Q090",
        "question_number": 90,
        "category": "In House: Anesthetic Pharmacology",
        "stem": "A 28-year-old man who sustained third-degree burns covering 45% of his body surface area 10 days ago requires urgent surgical debridement of his wounds. The surgical intern suggests using succinylcholine to facilitate rapid endotracheal intubation. The attending anesthesiologist immediately intervenes and selects rocuronium instead. What life-threatening electrolyte abnormality can occur if succinylcholine is administered to patients with extensive burn injuries, denervation, or prolonged immobilization?",
        "options": [
            {"text": "Severe hypocalcemia leading to tetany and laryngospasm", "is_correct": False},
            {"text": "Massive hyperkalemia leading to peaked T waves, ventricular fibrillation, and cardiac arrest", "is_correct": True},
            {"text": "Severe hypernatremia triggering pontine myelinolysis", "is_correct": False},
            {"text": "Profound hypokalemia causing U waves and torsades de pointes", "is_correct": False},
            {"text": "Hypermagnesemia leading to loss of deep tendon reflexes", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. Massive hyperkalemia leading to peaked T waves, ventricular fibrillation, and cardiac arrest.\n\nSuccinylcholine is a depolarizing neuromuscular blocker that stimulates nicotinic acetylcholine receptors (nAChR), opening non-selective cation channels that allow Na+ influx and K+ efflux. In healthy patients, this transient K+ efflux produces a benign serum potassium increase of ~0.5 mEq/L. However, following extensive burns, crush injuries, denervation (e.g., spinal cord injury, stroke, ALS), severe sepsis, or prolonged ICU immobilization, skeletal muscle fibers undergo widespread up-regulation and extrasynaptic proliferation of immature embryonic nicotinic receptors (containing the gamma instead of epsilon subunit) across the entire sarcolemma. Administration of succinylcholine triggers massive, synchronous, prolonged opening of these ubiquitous extrasynaptic channels, resulting in catastrophic efflux of potassium into the circulation. Serum potassium can surge to 8–10 mEq/L within minutes, precipitating refractory ventricular fibrillation and asystole. Succinylcholine is contraindicated after 24–48 hours post-injury until full tissue healing.\n\n• Option A is incorrect: Succinylcholine causes hyperkalemia, not hypocalcemia.\n• Option C is incorrect: Succinylcholine does not cause hypernatremia.\n• Option D is incorrect: It causes massive HYPERkalemia, not hypokalemia.\n• Option E is incorrect: Succinylcholine does not alter magnesium concentrations."
    },
    {
        "id": "IH_Q091",
        "question_number": 91,
        "category": "In House: Anesthetic Pharmacology",
        "stem": "During a surgical procedure under general anesthesia, a patient receives the non-depolarizing neuromuscular blocking agent rocuronium. Neuromuscular monitoring using a peripheral nerve stimulator at the adductor pollicis muscle (Train-of-Four, TOF stimulation at 2 Hz) displays a characteristic pattern. How does the Train-of-Four response differentiate a non-depolarizing block (e.g., rocuronium) from a Phase I depolarizing block (e.g., succinylcholine)?",
        "options": [
            {"text": "Non-depolarizing block exhibits no fade (all 4 twitches equal in height), whereas Phase I depolarizing block exhibits marked fade", "is_correct": False},
            {"text": "Non-depolarizing block exhibits marked 'fade' (progressive reduction in twitch height from T1 to T4, TOF ratio < 0.7), whereas Phase I depolarizing block exhibits equal reduction in amplitude across all 4 twitches without fade (TOF ratio = 1.0)", "is_correct": True},
            {"text": "Non-depolarizing block produces muscle fasciculations prior to paralysis, whereas Phase I block produces flaccid paralysis immediately", "is_correct": False},
            {"text": "Administration of neostigmine augments a non-depolarizing block, but reverses a Phase I block", "is_correct": False},
            {"text": "Post-tetanic potentiation is absent in non-depolarizing block and present in Phase I depolarizing block", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. Non-depolarizing block exhibits marked 'fade' (progressive reduction in twitch height from T1 to T4, TOF ratio < 0.7), whereas Phase I depolarizing block exhibits equal reduction in amplitude across all 4 twitches without fade (TOF ratio = 1.0).\n\nTrain-of-Four (TOF) monitoring delivers 4 electrical impulses at 2 Hz:\n1. Non-depolarizing block (competitive antagonism: rocuronium, vecuronium, cisatracurium): Shows marked 'FADE' (progressive decrement in amplitude from twitch 1 to twitch 4, TOF ratio T4/T1 < 0.7). Fade occurs because competitive blockers also antagonize presynaptic nicotinic ACh receptors that normally mobilize acetylcholine vesicles during rapid repetitive firing. It exhibits post-tetanic potentiation and is reversed by acetylcholinesterase inhibitors (neostigmine) or sugammadex.\n2. Phase I depolarizing block (succinylcholine): Binds and persistently depolarizes the end plate. It exhibits NO FADE (all 4 twitches are equally reduced in height, TOF ratio remains ~1.0), is preceded by transient muscle fasciculations, lacks post-tetanic facilitation, and is PROLONGED (augmented) if an AChE inhibitor is administered.\n(Note: Prolonged or high-dose succinylcholine transitions to a Phase II block, which resembles a non-depolarizing block and exhibits fade).\n\n• Option A is incorrect: It reverses the classic electrophysiological features.\n• Option C is incorrect: Phase I depolarizing block produces fasciculations; non-depolarizing blockers prevent fasciculations.\n• Option D is incorrect: Neostigmine reverses non-depolarizing blockers, but worsens/augments Phase I depolarizing block.\n• Option E is incorrect: Post-tetanic potentiation is present in non-depolarizing block and absent in Phase I."
    },
    {
        "id": "IH_Q092",
        "question_number": 92,
        "category": "In House: Anesthetic Pharmacology",
        "stem": "At the conclusion of an abdominal surgery, the surgical team requests reversal of rocuronium-induced neuromuscular blockade. The anesthesiologist administers neostigmine intravenously. Why must an antimuscarinic agent (such as glycopyrrolate or atropine) always be co-administered whenever neostigmine is given to reverse neuromuscular blockade?",
        "options": [
            {"text": "To prevent neostigmine from crossing the blood-brain barrier", "is_correct": False},
            {"text": "To prevent severe muscarinic side effects (bradycardia, severe bronchorrhea, bronchospasm, and salivation) caused by non-selective acetylcholine accumulation", "is_correct": True},
            {"text": "To accelerate renal elimination of rocuronium", "is_correct": False},
            {"text": "To prevent hyperkalemia from neostigmine metabolism", "is_correct": False},
            {"text": "To directly stimulate nicotinic receptors on the diaphragm", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. To prevent severe muscarinic side effects (bradycardia, severe bronchorrhea, bronchospasm, and salivation) caused by non-selective acetylcholine accumulation.\n\nNeostigmine is a reversible acetylcholinesterase (AChE) inhibitor. By preventing acetylcholine breakdown at the neuromuscular junction, it increases acetylcholine concentration to compete against and displace non-depolarizing blockers (e.g., rocuronium) from nicotinic receptors on skeletal muscle. However, AChE inhibition occurs throughout the body, flooding both nicotinic AND muscarinic receptors with acetylcholine. Unopposed muscarinic stimulation produces profound, potentially life-threatening adverse effects: profound bradycardia / asystole, excessive salivation, severe bronchorrhea, bronchospasm, abdominal cramping, and miosis. To prevent these muscarinic complications without blocking nicotinic reversal at the NMJ, an antimuscarinic drug—specifically Glycopyrrolate (which, like neostigmine, is a quaternary ammonium compound that does not cross the BBB) or Atropine—is co-administered simultaneously.\n\n• Option A is incorrect: Neostigmine has a quaternary amine structure that inherently prevents significant BBB penetration.\n• Option C is incorrect: Glycopyrrolate does not enhance renal clearance of rocuronium.\n• Option D is incorrect: Neostigmine does not cause hyperkalemia.\n• Option E is incorrect: Antimuscarinics block muscarinic receptors; they do not stimulate nicotinic receptors."
    },
    {
        "id": "IH_Q093",
        "question_number": 93,
        "category": "In House: Anesthetic Pharmacology",
        "stem": "A 48-year-old woman undergoing laparoscopic cholecystectomy receives rocuronium. Immediately after induction, the anesthesiologist encounters a 'cannot intubate, cannot ventilate' emergency. The team needs immediate, complete reversal of rocuronium within 2 to 3 minutes to restore spontaneous diaphragmatic breathing. Which novel pharmacological agent acts as a modified gamma-cyclodextrin that selectively binds, encapsulates, and inactivates rocuronium in plasma with high affinity?",
        "options": [
            {"text": "Edrophonium", "is_correct": False},
            {"text": "Sugammadex", "is_correct": True},
            {"text": "Pralidoxime", "is_correct": False},
            {"text": "Physostigmine", "is_correct": False},
            {"text": "Flumazenil", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. Sugammadex.\n\nSugammadex is a synthetic, modified γ-cyclodextrin molecule with a lipophilic core and negatively charged hydrophilic exterior. It acts via a revolutionary 'chelation/encapsulation' mechanism: it directly binds free aminosteroid neuromuscular blocking agents in the plasma—exhibiting highest affinity for Rocuronium (and moderate affinity for Vecuronium)—in a 1:1 ratio. By encapsulating rocuronium, it rapidly reduces free drug concentration in the bloodstream, creating a steep gradient that draws rocuronium away from the neuromuscular junction into the vascular space, achieving complete reversal of even deep neuromuscular blockade within 2 to 3 minutes. Unlike neostigmine, sugammadex does not inhibit acetylcholinesterase, producing no muscarinic side effects and eliminating the need for co-administered antimuscarinics.\n\n• Option A is incorrect: Edrophonium is a short-acting AChE inhibitor that cannot reverse deep rocuronium block within 2 minutes.\n• Option C is incorrect: Pralidoxime reactivates organophosphate-inhibited AChE.\n• Option D is incorrect: Physostigmine crosses the BBB and treats anticholinergic toxicity (e.g., atropine overdose).\n• Option E is incorrect: Flumazenil reverses benzodiazepines."
    },
    {
        "id": "IH_Q094",
        "question_number": 94,
        "category": "In House: Neuromuscular Junction Disorders",
        "stem": "A 45-year-old woman with a 3-year history of myasthenia gravis is taking pyridostigmine 60 mg every 4 hours. Thinking her medications are losing effectiveness after a minor cold, she accidentally doubles her dose over two days. She arrives at the emergency clinic with severe generalized muscle weakness, marked difficulty breathing, profuse sweating, salivation, pinpoint pupils, and diffuse muscle fasciculations. The medical resident suspects an acute crisis. How does a 'cholinergic crisis' differ from a 'myasthenic crisis', and what test was historically used to differentiate them?",
        "options": [
            {"text": "A cholinergic crisis results from insufficient medication and improves with edrophonium; a myasthenic crisis results from overdose and worsens with edrophonium", "is_correct": False},
            {"text": "A cholinergic crisis results from excessive acetylcholinesterase inhibitor overdose, causing persistent depolarizing block and prominent muscarinic signs (SLUDGEM, miosis, fasciculations) that worsen if edrophonium is administered; a myasthenic crisis results from disease under-treatment, improves with edrophonium, and lacks muscarinic toxicity", "is_correct": True},
            {"text": "Both crises present with identical muscarinic symptoms and respond identically to high-dose atropine", "is_correct": False},
            {"text": "Cholinergic crisis only affects extraocular muscles, while myasthenic crisis only affects the diaphragm", "is_correct": False},
            {"text": "Myasthenic crisis is caused by antibodies against presynaptic calcium channels, while cholinergic crisis is postsynaptic", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. A cholinergic crisis results from excessive acetylcholinesterase inhibitor overdose, causing persistent depolarizing block and prominent muscarinic signs (SLUDGEM, miosis, fasciculations) that worsen if edrophonium is administered; a myasthenic crisis results from disease under-treatment, improves with edrophonium, and lacks muscarinic toxicity.\n\nDifferentiating myasthenic crisis from cholinergic crisis is a classic neuropharmacology dilemma:\n1. Myasthenic Crisis: Due to undermedication, infection, or disease exacerbation. There is insufficient ACh at the postsynaptic end plate. Symptoms: severe flaccid weakness, respiratory failure, NO muscarinic excess (pupils normal/dilated, dry skin). Historically, administering intravenous edrophonium (Tensilon test, an ultra-short-acting AChE inhibitor) produced rapid, dramatic TEMPORARY IMPROVEMENT in muscle strength.\n2. Cholinergic Crisis: Due to overmedication with AChE inhibitors (pyridostigmine). Excessive acetylcholine accumulates at the NMJ, causing persistent depolarization and refractoriness of the motor end plate (similar to a Phase I block with fasciculations and profound flaccid weakness). Crucially, acetylcholine also floods muscarinic receptors, producing prominent DUMBBELSS/SLUDGEM symptoms (miosis, profuse sweating, salivation, diarrhea, bradycardia). Administering edrophonium provides even more ACh, dangerously WORSENING muscle weakness and respiratory arrest. Treatment is immediate cessation of pyridostigmine and administration of atropine.\n\n• Option A is incorrect: It reverses the definitions.\n• Option C is incorrect: Myasthenic crisis lacks muscarinic excess.\n• Option D is incorrect: Both crises cause life-threatening diaphragmatic weakness.\n• Option E is incorrect: Presynaptic calcium channel antibodies cause Lambert-Eaton syndrome."
    },
    {
        "id": "IH_Q095",
        "question_number": 95,
        "category": "In House: Anesthetic Pharmacology",
        "stem": "An anesthesiologist performs a deep tendon reflex test on a patient who has been induced and maintained on sevoflurane alone without the administration of any paralytic or neuromuscular blocking agent. When the patellar tendon is sharply tapped with a reflex hammer, what is the expected physiological response, and why?",
        "options": [
            {"text": "The reflex is completely abolished because volatile anesthetics destroy gamma motor neurons", "is_correct": False},
            {"text": "The knee-jerk reflex is intact and elicited because monosynaptic spinal stretch reflex arcs operate autonomously at the spinal cord level without requiring conscious cortical participation, as long as peripheral neuromuscular transmission is not blocked by a paralytic", "is_correct": True},
            {"text": "A clonus of 10 beats occurs due to loss of medullary reticulospinal tracts", "is_correct": False},
            {"text": "The contralateral leg extends due to crossed extensor reflex activation", "is_correct": False},
            {"text": "Severe masseter muscle spasm occurs immediately", "is_correct": False}
        ],
        "explanation": "Correct Answer: B. The knee-jerk reflex is intact and elicited because monosynaptic spinal stretch reflex arcs operate autonomously at the spinal cord level without requiring conscious cortical participation, as long as peripheral neuromuscular transmission is not blocked by a paralytic.\n\nDeep tendon reflexes (such as the patellar stretch reflex) are primitive, autonomous monosynaptic spinal reflex arcs: tapping the patellar tendon stretches quadriceps muscle spindles (Ia afferents), which enter the dorsal horn of the spinal cord (L2-L4) and make direct excitatory monosynaptic connections with alpha motor neurons in the ventral horn, triggering quadriceps contraction. General inhalational anesthetics (such as sevoflurane) act primarily on the cerebral cortex, thalamus, and reticular activating system to induce unconsciousness, amnesia, and analgesia. Unless a neuromuscular blocking agent (paralytic like rocuronium or succinylcholine) is administered to pharmacologically block acetylcholine receptors at the motor end plate, the spinal reflex arc remains intact, and tapping the tendon will evoke the knee-jerk reflex. This demonstrates why muscle relaxants are required when surgical immobility and areflexia are essential.\n\n• Option A is incorrect: Sevoflurane does not destroy gamma motor neurons.\n• Option C is incorrect: Clonus is an upper motor neuron sign requiring chronic corticospinal tract lesion.\n• Option D is incorrect: Crossed extensor reflex occurs with pain/withdrawal stimuli, not simple patellar tap.\n• Option E is incorrect: Masseter spasm is a sign of malignant hyperthermia in susceptible individuals."
    }
]

questions_section2.extend([
    {'category': 'In House: Anesthetic Pharmacology',
 'explanation': 'Correct Answer: B. Highly selective alpha-2 adrenergic receptor agonist; provides sedation with '
                'preserved patient arousability and cooperativeness with minimal depression of spontaneous respiratory '
                'drive.\n'
                '\n'
                'Dexmedetomidine is a potent, centrally acting selective α2-adrenergic receptor agonist (possessing an '
                'α2:α1 selectivity ratio of 1600:1, roughly 8 times higher than clonidine). By stimulating presynaptic '
                'α2-adrenoceptors in the locus coeruleus, it inhibits adenylate cyclase and reduces norepinephrine '
                "release. This produces a unique form of 'cooperative sedation' or 'conscious sedation' that mimics "
                'natural non-REM sleep: patients remain calm, can be easily aroused to follow verbal commands or '
                'answer questions, and quickly fall back to sleep when undisturbed. Crucially, unlike opioids, '
                'benzodiazepines, or propofol, dexmedetomidine produces minimal respiratory depression and does not '
                'blunt ventilatory responses to carbon dioxide, making it ideal for ICU extubation trials and awake '
                'fiberoptic intubation. Common hemodynamic side effects include dose-dependent bradycardia and '
                'hypotension.\n'
                '\n'
                '• Option A is incorrect: NMDA antagonism is the mechanism of ketamine.\n'
                '• Option C is incorrect: Dexmedetomidine is an alpha-2 agonist, not an opioid.\n'
                '• Option D is incorrect: It is not a dopamine agonist.\n'
                '• Option E is incorrect: It does not act via GABA receptors and frequently causes hypotension.',
 'id': 'IH_Q096',
 'options': [{'is_correct': False,
              'text': 'Potent antagonist at NMDA glutamate receptors; produces profound amnesia with increased blood '
                      'pressure'},
             {'is_correct': True,
              'text': 'Highly selective alpha-2 adrenergic receptor agonist; provides sedation with preserved patient '
                      'arousability and cooperativeness with minimal depression of spontaneous respiratory drive'},
             {'is_correct': False,
              'text': 'Selective mu-opioid receptor agonist; produces deep analgesia without any risk of constipation'},
             {'is_correct': False,
              'text': 'Selective dopamine D2 receptor agonist; prevents delirium without altering cardiac '
                      'hemodynamics'},
             {'is_correct': False,
              'text': 'Positive allosteric modulator of GABA-A receptors; eliminates the risk of hypotension'}],
 'question_number': 96,
 'stem': 'A 62-year-old mechanically ventilated patient in the intensive care unit requires light sedation to '
         'facilitate weaning from the ventilator. The intensivist selects an intravenous infusion of dexmedetomidine. '
         'What is the receptor mechanism of dexmedetomidine, and what is its major clinical advantage over GABAergic '
         'sedatives in this setting?'},
    {'category': 'In House: Anesthetic Pharmacology',
 'explanation': 'Correct Answer: B. Immune-mediated hypersensitivity reaction triggered by hepatic CYP2E1 oxidative '
                'metabolism of halothane into trifluoroacetyl chloride, which acetylates hepatocyte proteins into '
                'foreign neoantigens recognized by host antibodies.\n'
                '\n'
                'Halothane undergoes significant oxidative hepatic metabolism (up to 20% metabolized via cytochrome '
                'P450 2E1). This generates a reactive, electrophilic intermediate: trifluoroacetyl (TFA) chloride. TFA '
                'covalently binds to microsomal proteins on the surface of hepatocytes, creating foreign '
                "'hapten-protein' complexes (neoantigens). In genetically susceptible individuals—particularly upon "
                'repeat exposure within short time intervals—the host immune system generates anti-TFA antibodies and '
                'cytotoxic T-cell responses that attack the hepatocytes, producing severe autoimmune-mediated '
                'centrilobular necrosis (halothane hepatitis). Manifestations include fever, eosinophilia, jaundice, '
                'massive transaminitis, and fulminant hepatic failure with an 80% mortality rate. Modern halogenated '
                'volatile anesthetics (such as sevoflurane, which is fluorinated without chlorine and does not form '
                'TFA adducts, and desflurane, which is metabolized <0.02%) have virtually eliminated this '
                'complication.\n'
                '\n'
                '• Option A is incorrect: Halothane does not release significant inorganic fluoride (methoxyflurane '
                'causes fluoride-induced polyuric nephrogenic diabetes insipidus).\n'
                '• Option C is incorrect: Halothane does not cause endothelin-mediated vasospasm.\n'
                '• Option D is incorrect: Halothane hepatitis targets trifluoroacetylated proteins, not BSEP.\n'
                '• Option E is incorrect: Halothane hepatitis is a cell-mediated/antibody-directed type II/IV '
                'hypersensitivity, not type I IgE anaphylaxis.',
 'id': 'IH_Q097',
 'options': [{'is_correct': False, 'text': 'Direct cytotoxic destruction of hepatocytes by inorganic fluoride ions'},
             {'is_correct': True,
              'text': 'Immune-mediated hypersensitivity reaction triggered by hepatic CYP2E1 oxidative metabolism of '
                      'halothane into trifluoroacetyl chloride, which acetylates hepatocyte proteins into foreign '
                      'neoantigens recognized by host antibodies'},
             {'is_correct': False, 'text': 'Microvascular spasm of the hepatic artery mediated by endothelin release'},
             {'is_correct': False, 'text': 'Autoantibodies directed against the bile salt export pump (BSEP)'},
             {'is_correct': False,
              'text': 'Type I IgE-mediated anaphylactic mast cell degranulation in portal triads'}],
 'question_number': 97,
 'stem': 'A 44-year-old woman undergoes elective hysterectomy. General anesthesia is maintained with halothane. She '
         'had previously received halothane 3 months earlier for an ankle fracture. Six days postoperatively, she '
         'develops anorexia, fever, nausea, and jaundice. Laboratory tests reveal serum AST 2,400 U/L, ALT 2,150 U/L, '
         'total bilirubin 9.8 mg/dL, and prothrombin time 28 seconds (INR 2.6). Viral hepatitis serologies are '
         'negative. Liver biopsy shows massive centrilobular (zone 3) hepatic necrosis. What is the immunological '
         'mechanism of halothane hepatitis?'},
    {'category': 'In House: Anesthetic Pharmacology',
 'explanation': 'Correct Answer: B. Nitrous oxide is approximately 34 times more soluble in blood than nitrogen, '
                'diffusing into compliant, closed air-filled spaces far faster than nitrogen can diffuse out, leading '
                'to rapid, dangerous expansion of space volume or pressure.\n'
                '\n'
                "Nitrous oxide (N2O, 'laughing gas') has a blood:gas partition coefficient of 0.47, whereas molecular "
                'nitrogen (N2) has a blood:gas partition coefficient of only 0.014. Because N2O is roughly 34 times '
                'more soluble in blood than nitrogen, when blood containing dissolved N2O reaches a closed '
                'gas-containing cavity (which contains air that is 78% nitrogen), N2O diffuses down its partial '
                'pressure gradient INTO the cavity much faster than nitrogen can diffuse OUT into the bloodstream. In '
                'compliant structures (such as a pneumothorax or obstructed loops of bowel), this causes massive, '
                'rapid volume expansion (e.g., doubling the size of a pneumothorax into a life-threatening tension '
                'pneumothorax within 10–20 minutes). In non-compliant spaces (such as the middle ear or intracranial '
                'cavity following craniotomy), it creates dramatic, dangerous pressure spikes. N2O is therefore '
                'strictly contraindicated in pneumothorax, bowel obstruction, middle ear surgery, intraocular gas '
                'bubbles, and venous air embolism.\n'
                '\n'
                '• Option A is incorrect: N2O does not cause severe vasodilation; it mildly stimulates sympathetic '
                'tone.\n'
                '• Option C is incorrect: N2O does not cause methemoglobinemia (prilocaine and benzocaine do).\n'
                '• Option D is incorrect: N2O does not stimulate histamine release.\n'
                '• Option E is incorrect: N2O does not convert into nitrogen dioxide in vivo.',
 'id': 'IH_Q098',
 'options': [{'is_correct': False,
              'text': 'Nitrous oxide causes severe systemic arterial vasodilation that lowers coronary perfusion '
                      'pressure'},
             {'is_correct': True,
              'text': 'Nitrous oxide is approximately 34 times more soluble in blood than nitrogen, diffusing into '
                      'compliant, closed air-filled spaces far faster than nitrogen can diffuse out, leading to rapid, '
                      'dangerous expansion of space volume or pressure'},
             {'is_correct': False,
              'text': 'Nitrous oxide precipitates methemoglobinemia in the presence of pleural air'},
             {'is_correct': False,
              'text': 'Nitrous oxide directly stimulates histamine release from pulmonary mast cells'},
             {'is_correct': False,
              'text': 'Nitrous oxide reacts with atmospheric nitrogen to form toxic nitrogen dioxide'}],
 'question_number': 98,
 'stem': 'A 26-year-old trauma patient with a known right-sided pneumothorax is undergoing urgent open reduction and '
         'internal fixation of a femur fracture. The surgical resident suggests adding nitrous oxide (N2O) to the '
         'inhalational gas mixture to reduce the required concentration of volatile anesthetic. The attending '
         'anesthesiologist explicitly forbids the use of nitrous oxide in this patient. Why is nitrous oxide strictly '
         'contraindicated in patients with closed gas-containing body cavities (such as pneumothorax, bowel '
         'obstruction, or air embolism)?'},
    {'category': 'In House: Anesthetic Pharmacology',
 'explanation': 'Correct Answer: B. Diffusional hypoxia: rapid outpouring of large volumes of nitrous oxide from blood '
                'into the alveoli dilutes alveolar oxygen and carbon dioxide concentrations.\n'
                '\n'
                'Diffusional hypoxia (Fink effect) occurs at the cessation of nitrous oxide (N2O) administration. '
                'Because N2O has low blood solubility, vast volumes of N2O dissolved in the bloodstream rapidly rush '
                'out of pulmonary capillary blood into the alveoli down a steep concentration gradient. This massive '
                'influx of N2O into the alveoli substantially dilutes the partial pressure of alveolar oxygen (PAO2) '
                'and alveolar carbon dioxide (PACO2). Dilution of PAO2 reduces arterial oxygen saturation, while '
                'dilution of PACO2 decreases the central respiratory drive to breathe, causing hypoventilation. To '
                'prevent diffusional hypoxia, patients must routinely be administered 100% oxygen for at least 5 to 10 '
                'minutes upon discontinuation of nitrous oxide.\n'
                '\n'
                '• Option A is incorrect: Volatile anesthetics are bronchodilators, and cessation does not trigger '
                'reflex bronchospasm.\n'
                '• Option C is incorrect: Diffusional hypoxia is an alveolar gas exchange phenomenon, not a pulmonary '
                'embolism.\n'
                '• Option D is incorrect: N2O does not paralyze diaphragmatic motor units.\n'
                '• Option E is incorrect: N2O does not alter surfactant function.',
 'id': 'IH_Q099',
 'options': [{'is_correct': False, 'text': 'Acute reflex bronchospasm triggered by sevoflurane withdrawal'},
             {'is_correct': True,
              'text': 'Diffusional hypoxia: rapid outpouring of large volumes of nitrous oxide from blood into the '
                      'alveoli dilutes alveolar oxygen and carbon dioxide concentrations'},
             {'is_correct': False, 'text': 'Delayed pulmonary embolism from pelvic venodilation'},
             {'is_correct': False, 'text': 'Acute paralysis of diaphragmatic motor units'},
             {'is_correct': False, 'text': 'Inactivation of pulmonary surfactant by nitrous oxide'}],
 'question_number': 99,
 'stem': 'A 35-year-old woman undergoes an uncomplicated ambulatory procedure under general anesthesia with nitrous '
         'oxide and sevoflurane. At the conclusion of the case, the vaporizers are turned off, and the patient is '
         'allowed to breathe room air. Within 3 minutes, the pulse oximeter shows her oxygen saturation dropping from '
         '99% to 84%. Administration of 100% supplemental oxygen rapidly restores saturation to 100%. What '
         'physiological phenomenon caused this acute drop in oxygen saturation?'},
    {'category': 'In House: Anesthetic Pharmacology',
 'explanation': 'Correct Answer: B. Pseudocholinesterase (Butyrylcholinesterase / BCHE) in plasma.\n'
                '\n'
                'Succinylcholine has an exceptionally short clinical duration of action (5 to 10 minutes) because it '
                'is rapidly hydrolyzed in the bloodstream and liver by plasma pseudocholinesterase '
                '(butyrylcholinesterase / plasma cholinesterase) before reaching the neuromuscular junction; only ~10% '
                'of an administered dose actually reaches the NMJ. In patients with hereditary Pseudocholinesterase '
                'Deficiency (an autosomal recessive condition caused by mutations in the BCHE gene, such as the '
                "atypical 'A' variant or silent allele), or acquired deficiency (liver disease, malnutrition, "
                'pregnancy), succinylcholine is not degraded in plasma. Consequently, therapeutic concentrations '
                'persist at the motor end plate, producing prolonged neuromuscular blockade, flaccid paralysis, and '
                'apnea lasting 2 to 8 hours. The atypical enzyme is diagnosed by the Dibucaine Number test: dibucaine '
                'inhibits normal pseudocholinesterase by >80%, but inhibits atypical pseudocholinesterase by only '
                '~20%. Treatment is supportive: continued mechanical ventilation and sedation until the drug is '
                'cleared via non-specific pathways.\n'
                '\n'
                '• Option A is incorrect: True acetylcholinesterase is located at synapses and erythrocyte membranes; '
                'it does not metabolize succinylcholine efficiently.\n'
                '• Option C is incorrect: CYP2D6 metabolizes codeine, beta-blockers, and antidepressants, not '
                'succinylcholine.\n'
                '• Option D is incorrect: G6PD deficiency causes oxidative hemolytic anemia with sulfa drugs/fava '
                'beans, not prolonged paralysis.\n'
                '• Option E is incorrect: RYR1 mutations cause malignant hyperthermia (hyperthermia, rigidity, '
                'hypercapnia), which is absent in this patient.',
 'id': 'IH_Q100',
 'options': [{'is_correct': False, 'text': 'Acetylcholinesterase (AChE) at the motor end plate'},
             {'is_correct': True, 'text': 'Pseudocholinesterase (Butyrylcholinesterase / BCHE) in plasma'},
             {'is_correct': False, 'text': 'Hepatic Cytochrome P450 2D6'},
             {'is_correct': False, 'text': 'Glucose-6-phosphate dehydrogenase (G6PD)'},
             {'is_correct': False, 'text': 'Ryanodine receptor type 1 (RYR1)'}],
 'question_number': 100,
 'stem': 'A 27-year-old healthy man undergoes general anesthesia for an open reduction of a forearm fracture. Rapid '
         'sequence intubation is performed using intravenous succinylcholine 1.5 mg/kg. The endotracheal tube is '
         'placed without incident. At the conclusion of the 45-minute surgery, the patient remains completely '
         'paralyzed, unable to move his extremities, trigger spontaneous breaths on the ventilator, or open his eyes. '
         'Peripheral nerve stimulation reveals persistent, dense neuromuscular blockade. His vital signs and '
         'temperature are entirely normal. A family history inquiry reveals that his maternal uncle experienced '
         'prolonged mechanical ventilation following an elective surgery. Deficiency or genetic mutation in which of '
         "the following enzymes is responsible for this patient's prolonged paralysis?"},
    {'category': 'In House: Anesthetic Pharmacology',
 'explanation': 'Correct Answer: B. Methemoglobinemia (oxidation of ferrous Fe2+ to ferric Fe3+ in heme); treat with '
                'intravenous Methylene Blue.\n'
                '\n'
                'Methemoglobinemia is a well-documented adverse effect of oxidizing agents, prominently including '
                'topical local anesthetics such as Benzocaine (frequently used in mucosal numbing sprays for endoscopy '
                'or dental work) and Prilocaine (EMLA cream metabolite o-toluidine), as well as dapsone and nitrites. '
                'These agents oxidize the iron within hemoglobin from its normal ferrous state (Fe2+) to the ferric '
                'state (Fe3+). Ferric iron cannot bind oxygen, and it allosterically shifts the oxygen-hemoglobin '
                'dissociation curve of remaining normal heme groups to the left, impeding oxygen unloading to '
                'peripheral tissues (tissue hypoxia). Hallmarks include: (1) Cyanosis unresponsive to 100% O2, (2) '
                "'Chocolate-brown' arterial blood, (3) 'Pulse oximetry saturation gap' (pulse oximeter locks near 85% "
                'because methemoglobin absorbs both 660 nm and 940 nm light equally, while true PaO2 on ABG is '
                'normal). The specific antidote is intravenous Methylene Blue, which acts as an electron acceptor for '
                'NADPH-methemoglobin reductase, reducing ferric iron (Fe3+) back to ferrous iron (Fe2+).\n'
                '\n'
                "• Option A is incorrect: Carbon monoxide poisoning features 'cherry-red' skin, normal PaO2, and "
                'carboxyhemoglobin on co-oximetry, treated with 100% O2/hyperbarics.\n'
                '• Option C is incorrect: Cyanide blocks cytochrome c oxidase without causing chocolate blood or pulse '
                'ox locking at 85%.\n'
                '• Option D is incorrect: Benzocaine causes methemoglobinemia, not immediate immune hemolysis.\n'
                '• Option E is incorrect: Benzocaine does not cause coronary spasm.',
 'id': 'IH_Q101',
 'options': [{'is_correct': False, 'text': 'Carbon monoxide poisoning; treat with hyperbaric oxygen'},
             {'is_correct': True,
              'text': 'Methemoglobinemia (oxidation of ferrous Fe2+ to ferric Fe3+ in heme); treat with intravenous '
                      'Methylene Blue'},
             {'is_correct': False, 'text': 'Cyanide poisoning; treat with hydroxocobalamin'},
             {'is_correct': False, 'text': 'Acute hemolytic anemia; treat with washed packed red blood cells'},
             {'is_correct': False,
              'text': 'Lidocaine-induced coronary vasospasm; treat with intravenous nitroglycerin'}],
 'question_number': 101,
 'stem': 'A 52-year-old man undergoes an elective upper endoscopy under conscious sedation. Prior to the procedure, '
         'his pharynx is sprayed generously with topical 20% benzocaine aerosol to suppress the gag reflex. Twenty '
         'minutes later, in the recovery area, the patient becomes fatigued and confused. His lips, nail beds, and '
         'skin appear distinctly slate-gray / cyanotic. Pulse oximetry reads 85% and does not change despite '
         'administration of 100% oxygen via a non-rebreather mask. An arterial blood gas reveals a normal arterial '
         'partial pressure of oxygen (PaO2 98 mm Hg), but the blood drawn into the syringe is dark chocolate-brown in '
         "appearance. What is the mechanism of this patient's hypoxemia, and what is the specific intravenous "
         'antidote?'},
    {'category': 'In House: Anesthetic Pharmacology',
 'explanation': 'Correct Answer: C. Sevoflurane.\n'
                '\n'
                'Sevoflurane is the volatile anesthetic of choice for pediatric inhalational mask induction. Unlike '
                'other modern volatile agents, sevoflurane has a pleasant, sweet, non-pungent odor and does not '
                'irritate the tracheobronchial tree. It possesses potent bronchodilating properties without triggering '
                'coughing, breath-holding, copious airway secretions, or laryngospasm. Additionally, its relatively '
                'low blood:gas partition coefficient (0.65) ensures rapid induction and emergence. In contrast, '
                'Desflurane and Isoflurane are intensely pungent and irritate the respiratory mucosa, causing '
                'coughing, breath-holding, and laryngospasm, making them contraindicated for inhalational mask '
                'induction.\n'
                '\n'
                '• Option A is incorrect: Desflurane is extremely pungent and irritating to the airway, frequently '
                'inducing laryngospasm during mask induction.\n'
                '• Option B is incorrect: Isoflurane is pungent and provokes coughing during induction.\n'
                '• Option D is incorrect: Enflurane can induce epileptiform EEG patterns and is rarely used.\n'
                '• Option E is incorrect: Halothane was historically used for pediatric induction, but has been '
                'abandoned due to risks of halothane hepatitis, severe bradycardia, and myocardial sensitization to '
                'catecholamines.',
 'id': 'IH_Q102',
 'options': [{'is_correct': False, 'text': 'Desflurane'},
             {'is_correct': False, 'text': 'Isoflurane'},
             {'is_correct': True, 'text': 'Sevoflurane'},
             {'is_correct': False, 'text': 'Enflurane'},
             {'is_correct': False, 'text': 'Halothane'}],
 'question_number': 102,
 'stem': 'A 3-year-old child presents with frequent episodes of unprovoked wheezing and reactive airway disease. He '
         'requires general anesthesia for repair of an umbilical hernia. The pediatric anesthesiologist plans an '
         'inhalational induction via face mask before intravenous access is established. Which of the following '
         'volatile anesthetics is the preferred agent of choice for pediatric mask induction because it does not cause '
         'airway irritation, pungent odor, coughing, or breath-holding?'},
    {'category': 'In House: Anesthetic Pharmacology',
 'explanation': 'Correct Answer: B. Propofol Infusion Syndrome (PRIS); disruption of mitochondrial oxidative '
                'phosphorylation, inhibition of the electron transport chain (complexes I, II, IV), and impairment of '
                'fatty acid beta-oxidation.\n'
                '\n'
                'Propofol Infusion Syndrome (PRIS) is a rare but highly lethal (>30-50% mortality) complication of '
                'prolonged (>48 hours), high-dose (>4-5 mg/kg/hr or >67-83 mcg/kg/min) propofol administration, '
                'particularly in pediatric or critically ill adult ICU patients. Propofol impairs cellular energy '
                'metabolism by: (1) Inhibiting the mitochondrial electron transport chain (specifically complexes I, '
                'II, and IV), uncoupling oxidative phosphorylation, and (2) Impairing mitochondrial fatty acid '
                'oxidation by blocking entry of long-chain acylcarnitines. This induces acute cellular energy '
                'starvation, leading to severe lactic acidosis, widespread rhabdomyolysis with hyperkalemia, acute '
                'renal failure, hepatomegaly with hypertriglyceridemia, and myocardial failure presenting as '
                'refractory bradyarrhythmias, Brugada-like ECG patterns, and cardiogenic shock. Management requires '
                'immediate discontinuation of propofol, hemodialysis/hemofiltration, and ECMO if cardiogenic shock '
                'ensues.\n'
                '\n'
                '• Option A is incorrect: Malignant hyperthermia occurs acutely with volatile gases/succinylcholine, '
                'not prolonged propofol infusions.\n'
                '• Option C is incorrect: NMS is caused by antipsychotics.\n'
                '• Option D is incorrect: Anticholinergic syndrome presents with hyperthermia, mydriasis, delirium, '
                'and urinary retention.\n'
                '• Option E is incorrect: Reye syndrome occurs in children given aspirin during viral infections.',
 'id': 'IH_Q103',
 'options': [{'is_correct': False, 'text': 'Malignant hyperthermia; unchecked calcium release through RYR1'},
             {'is_correct': True,
              'text': 'Propofol Infusion Syndrome (PRIS); disruption of mitochondrial oxidative phosphorylation, '
                      'inhibition of the electron transport chain (complexes I, II, IV), and impairment of fatty acid '
                      'beta-oxidation'},
             {'is_correct': False, 'text': 'Neuroleptic malignant syndrome; acute striatal dopamine blockade'},
             {'is_correct': False, 'text': 'Central anticholinergic syndrome; muscarinic receptor antagonism'},
             {'is_correct': False, 'text': 'Reye syndrome; microvesicular steatosis from aspirin therapy'}],
 'question_number': 103,
 'stem': 'A 45-year-old man in the intensive care unit with severe head trauma receives a continuous high-dose '
         'infusion of propofol (80 mcg/kg/min) for 5 days to control refractory intracranial hypertension. On day 5, '
         'he develops severe refractory metabolic acidosis (pH 7.12, lactate 11 mmol/L), hyperkalemia (6.7 mEq/L), '
         'rhabdomyolysis (creatine kinase 65,000 U/L), hypertriglyceridemia, hepatomegaly, and wide-complex refractory '
         'ventricular arrhythmias with acute cardiogenic shock. What is this life-threatening syndrome, and what is '
         'its underlying mitochondrial pathophysiology?'},
    {'category': 'In House: Neuromuscular Junction Disorders',
 'explanation': 'Correct Answer: A. Muscle-Specific Kinase (MuSK).\n'
                '\n'
                'Approximately 10–15% of patients with generalized myasthenia gravis test negative for classic '
                "anti-AChR antibodies ('seronegative MG'). In this population, up to 40% harbor IgG4 autoantibodies "
                'against Muscle-Specific Kinase (MuSK). MuSK is a receptor tyrosine kinase on the postsynaptic '
                'membrane that is activated by neural agrin via LRP4 to maintain clustering of AChRs at the '
                'neuromuscular junction. Anti-MuSK MG displays distinct clinical characteristics: (1) Overwhelming '
                'female predominance, (2) Prominent bulbar, facial, neck, and respiratory weakness, often with '
                "prominent neck extensor weakness ('dropped head syndrome') and sparing of ocular muscles, (3) Lack of "
                'thymic pathology (thymectomy is NOT beneficial in anti-MuSK MG), (4) Poor or variable response to '
                'acetylcholinesterase inhibitors (pyridostigmine often worsens symptoms or causes cholinergic '
                'hyperactivity), and (5) Dramatic therapeutic responsiveness to B-cell depletion with Rituximab.\n'
                '\n'
                '• Option B is incorrect: Anti-VGKC antibodies cause Morvan syndrome and neuromyotonia.\n'
                '• Option C is incorrect: Dystrophin mutations cause Duchenne and Becker muscular dystrophies.\n'
                '• Option D is incorrect: Anti-RYR1 is associated with malignant hyperthermia or thymoma-associated '
                'severe MG, not MuSK-type.\n'
                '• Option E is incorrect: Caspr2 antibodies cause autoimmune encephalitis and peripheral nerve '
                'hyperexcitability.',
 'id': 'IH_Q104',
 'options': [{'is_correct': True, 'text': 'Muscle-Specific Kinase (MuSK)'},
             {'is_correct': False, 'text': 'Voltage-gated potassium channel (VGKC)'},
             {'is_correct': False, 'text': 'Dystrophin-glycoprotein complex'},
             {'is_correct': False, 'text': 'Ryanodine receptor type 1 (RYR1)'},
             {'is_correct': False, 'text': 'Neuromuscular agrin coreceptor (Caspr2)'}],
 'question_number': 104,
 'stem': 'A 34-year-old woman is evaluated for fluctuating muscle weakness. She has severe weakness of the neck '
         "extensors ('dropped head syndrome') and bulbar muscles (dysarthria and dysphagia), with relative sparing of "
         'extraocular muscles. Repeated testing for serum anti-AChR antibodies is negative. A specialized autoantibody '
         'panel is sent. Autoantibodies directed against which of the following postsynaptic receptor tyrosine kinases '
         'are found in up to 40% of patients with seronegative generalized myasthenia gravis?'},
    {'category': 'In House: Anesthetic Pharmacology',
 'explanation': 'Correct Answer: B. Aminoglycosides inhibit presynaptic voltage-gated calcium channels, decreasing '
                'acetylcholine release from the motor nerve terminal.\n'
                '\n'
                'Aminoglycoside antibiotics (e.g., gentamicin, tobramycin, amikacin) and polymyxins exhibit '
                'neuromuscular blocking properties. They act by competing with calcium ions at presynaptic P/Q-type '
                'voltage-gated calcium channels, blocking calcium influx into the motor nerve terminal and '
                'significantly reducing the quantal release of acetylcholine. When administered concurrently with '
                'non-depolarizing (or depolarizing) neuromuscular blocking agents, aminoglycosides synergistically '
                'potentiate the paralysis, causing prolonged neuromuscular blockade and postoperative '
                'hypoventilation/apnea. Intravenous calcium gluconate can partially antagonize this antibiotic-induced '
                'presynaptic block by competing with aminoglycosides at the presynaptic calcium channels.\n'
                '\n'
                '• Option A is incorrect: Aminoglycosides act primarily presynaptically by inhibiting Ca2+ entry, not '
                'by directly blocking postsynaptic nicotinic receptors.\n'
                '• Option C is incorrect: Aminoglycosides do not stimulate AChE.\n'
                '• Option D is incorrect: They do not alter Na+/K+ pump activity.\n'
                '• Option E is incorrect: Rocuronium is eliminated primarily via biliary excretion, not CYP3A4.',
 'id': 'IH_Q105',
 'options': [{'is_correct': False,
              'text': 'Aminoglycosides competitively displace acetylcholine from postsynaptic nicotinic receptors'},
             {'is_correct': True,
              'text': 'Aminoglycosides inhibit presynaptic voltage-gated calcium channels, decreasing acetylcholine '
                      'release from the motor nerve terminal'},
             {'is_correct': False,
              'text': 'Aminoglycosides accelerate the enzymatic degradation of acetylcholine by acetylcholinesterase'},
             {'is_correct': False, 'text': 'Aminoglycosides induce massive upregulation of the Na+/K+-ATPase pump'},
             {'is_correct': False,
              'text': 'Aminoglycosides prevent hepatic clearance of rocuronium by inhibiting cytochrome P450 3A4'}],
 'question_number': 105,
 'stem': 'A 64-year-old man in the intensive care unit is being treated for a severe Pseudomonas aeruginosa pneumonia '
         'with high-dose intravenous tobramycin (an aminoglycoside). Following an emergency bedside abdominal '
         'procedure where he received a standard dose of rocuronium, he experiences profound, prolonged neuromuscular '
         'blockade with respiratory failure lasting several hours beyond the expected duration. What pharmacodynamic '
         'interaction explains why aminoglycoside antibiotics potentiate neuromuscular blockade?'},
])

if __name__ == "__main__":
    print(f"Section 2 Question Count: {len(questions_section2)}")
    ids = [q["id"] for q in questions_section2]
    assert len(ids) == len(set(ids)), "Duplicate IDs found!"
    print("Section 2 validated successfully!")
