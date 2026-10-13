# zen_part4.py - Topics 13 to 16 (80 Questions total)
import json

part4_questions = [
    # =========================================================================
    # 13. CANNABIS MANAGEMENT (20 Questions: Q1 - Q20)
    # =========================================================================
    {
        "q_num": "CAN-01",
        "category": "Cannabis Management",
        "stem": "A 23-year-old college student presents to the emergency department with acute intoxication after ingesting a high-dose cannabis edible. Physical examination reveals bilateral conjunctival injection, dry oral mucosa, resting tachycardia (heart rate 118 bpm), orthostatic lightheadedness, and increased appetite ('the munchies'). Delta-9-tetrahydrocannabinol (THC) produces these psychoactive and physiological manifestations primarily by acting as a partial agonist at which receptor subtype?",
        "options": [
            {"letter": "A", "is_correct": True, "text": "Cannabinoid receptor type 1 (CB1)"},
            {"letter": "B", "is_correct": False, "text": "Cannabinoid receptor type 2 (CB2)"},
            {"letter": "C", "is_correct": False, "text": "Serotonin 5-HT2A receptor"},
            {"letter": "D", "is_correct": False, "text": "Mu-opioid receptor (MOR)"},
            {"letter": "E", "is_correct": False, "text": "Dopamine D2 receptor"}
        ],
        "explanation": "Correct Answer: A. Cannabinoid receptor type 1 (CB1).\n\nDelta-9-tetrahydrocannabinol (THC) is the primary psychoactive cannabinoid in marijuana:\n• Receptors: THC acts as a partial agonist at CB1 receptors (predominantly localized in the CNS—cortex, hippocampus, basal ganglia, cerebellum, and hypothalamic appetite centers) and CB2 receptors (primarily on peripheral immune cells and lymphoid tissues).\n• Signaling: CB1 is a Gi/o-protein coupled receptor that inhibits adenylyl cyclase, closes presynaptic voltage-gated Ca2+ channels, and opens inwardly rectifying K+ channels, decreasing presynaptic release of GABA and glutamate.\n• Acute physiological signs: Bilateral conjunctival injection (ciliary vasodilation), tachycardia, dry mouth, increased appetite, and impaired short-term memory."
    },
    {
        "q_num": "CAN-02",
        "category": "Cannabis Management",
        "stem": "A 26-year-old man with a 6-year history of heavy, daily cannabis use presents with recurrent episodes of intractable nausea, cyclic vomiting, and severe diffuse abdominal pain over the past 3 months. Extensive gastrointestinal workup, including upper endoscopy, abdominal CT, and gastric emptying studies, is completely normal. The patient notes that his nausea and pain are temporarily relieved only when he takes prolonged, extremely hot showers or baths multiple times a day. What is the diagnosis, and what is the definitive cure?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Cyclic vomiting syndrome; Oral sumatriptan"},
            {"letter": "B", "is_correct": True, "text": "Cannabinoid hyperemesis syndrome (CHS); Complete cessation of cannabis"},
            {"letter": "C", "is_correct": False, "text": "Gastroparesis; Oral metoclopramide"},
            {"letter": "D", "is_correct": False, "text": "Acute pancreatitis; Intravenous fluid resuscitation"},
            {"letter": "E", "is_correct": False, "text": "Biliary colic; Laparoscopic cholecystectomy"}
        ],
        "explanation": "Correct Answer: B. Cannabinoid hyperemesis syndrome (CHS); Complete cessation of cannabis.\n\nCannabinoid Hyperemesis Syndrome (CHS) occurs in chronic, heavy, long-term cannabis users:\n• Clinical triad: Severe cyclic vomiting, colicky abdominal pain, and learned compulsive hot water bathing/showering (which transiently alleviates symptoms).\n• Pathophysiology: Chronic overstimulation causes downregulation of central CB1 receptors and paradoxical pro-emetic effects, as well as desensitization of peripheral enteric TRPV1 heat-sensitive channels (hot water activates cutaneous TRPV1 to restore thermoregulatory and visceral balance).\n• Acute relief: Topical capsaicin cream applied to the abdomen or IV haloperidol.\n• Definitive cure: Permanent cessation of all cannabis consumption."
    },
    {
        "q_num": "CAN-03",
        "category": "Cannabis Management",
        "stem": "A 29-year-old daily cannabis user abruptly discontinues marijuana use before starting a new job. Three days later, he presents with irritability, marked anxiety, insomnia, vivid disturbing dreams, tremors, sweating, and decreased appetite with weight loss. What condition is this patient experiencing, and at what time point do these symptoms typically peak?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Cannabis-induced psychosis; Peaks at 24 hours"},
            {"letter": "B", "is_correct": True, "text": "Cannabis withdrawal syndrome; Peaks at 2 to 6 days"},
            {"letter": "C", "is_correct": False, "text": "Delirium tremens; Peaks at 48 hours"},
            {"letter": "D", "is_correct": False, "text": "Panic disorder; Peaks immediately upon cessation"},
            {"letter": "E", "is_correct": False, "text": "Serotonin syndrome; Peaks at 12 hours"}
        ],
        "explanation": "Correct Answer: B. Cannabis withdrawal syndrome; Peaks at 2 to 6 days.\n\nCannabis Withdrawal Syndrome (DSM-5 criteria):\n• Onset: Symptoms develop within 24-48 hours of cessation in heavy, daily users.\n• Symptoms: Irritability, anger/aggression, nervousness/anxiety, sleep disturbance (insomnia, vivid strange dreams), decreased appetite/weight loss, restlessness, depressed mood, and physical symptoms (tremors, sweating, chills, headache).\n• Time course: Symptoms typically peak at 2 to 6 days after stopping and gradually resolve over 1 to 2 weeks as lipophilic cannabinoids clear the body."
    },
    {
        "q_num": "CAN-04",
        "category": "Cannabis Management",
        "stem": "Endocannabinoids act as unconventional retrograde neurotransmitters in the central nervous system. Which of the following molecules is an endogenous lipid-derived cannabinoid that is synthesized 'on demand' from membrane phospholipids by phospholipase D and acts as an agonist at CB1 and CB2 receptors?",
        "options": [
            {"letter": "A", "is_correct": True, "text": "Anandamide (N-arachidonoylethanolamine)"},
            {"letter": "B", "is_correct": False, "text": "Leukotriene B4"},
            {"letter": "C", "is_correct": False, "text": "Thromboxane A2"},
            {"letter": "D", "is_correct": False, "text": "Prostaglandin F2-alpha"},
            {"letter": "E", "is_correct": False, "text": "Sphingosine-1-phosphate"}
        ],
        "explanation": "Correct Answer: A. Anandamide (N-arachidonoylethanolamine).\n\nThe two primary endogenous cannabinoids (endocannabinoids) are:\n1. Anandamide (AEA / N-arachidonoylethanolamine, derived from N-arachidonoyl phosphatidylethanolamine).\n2. 2-Arachidonoylglycerol (2-AG, synthesized from diacylglycerol by DAG lipase).\nEndocannabinoids are not stored in vesicles; upon postsynaptic depolarization and Ca2+ influx, they are synthesized on demand from membrane lipids, diffuse retrogradely across the synaptic cleft, and bind to presynaptic CB1 receptors to inhibit further neurotransmitter exocytosis (depolarization-induced suppression of inhibition or excitation / DSI/DSE)."
    },
    {
        "q_num": "CAN-05",
        "category": "Cannabis Management",
        "stem": "A 3-year-old child with severe Dravet syndrome (severe myoclonic epilepsy of infancy) experiences multiple daily refractory seizures. The pediatric neurologist prescribes Epidiolex, an FDA-approved pharmaceutical formulation of a non-psychoactive phytocannabinoid. What is the active pharmaceutical agent in this medication?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Delta-9-tetrahydrocannabinol (THC)"},
            {"letter": "B", "is_correct": True, "text": "Cannabidiol (CBD)"},
            {"letter": "C", "is_correct": False, "text": "Dronabinol"},
            {"letter": "D", "is_correct": False, "text": "Nabilone"},
            {"letter": "E", "is_correct": False, "text": "Rimonabant"}
        ],
        "explanation": "Correct Answer: B. Cannabidiol (CBD).\n\nEpidiolex is a plant-derived, highly purified oral formulation of Cannabidiol (CBD):\n• Non-intoxicating: CBD has low affinity for CB1/CB2 receptors and does not cause intoxication or euphoria.\n• Indications: FDA-approved for refractory seizures associated with Dravet syndrome, Lennox-Gastaut syndrome, and Tuberous Sclerosis Complex.\n• Proposed mechanisms: Antagonism of GPR55 receptors, TRPV1 desensitization, and modulation of intracellular calcium."
    },
    {
        "q_num": "CAN-06",
        "category": "Cannabis Management",
        "stem": "Synthetic cannabinoids (such as 'K2' or 'Spice') are chemically distinct from natural plant-derived phytocannabinoids. In contrast to natural THC, synthetic cannabinoids frequently produce life-threatening toxicities including extreme agitation, delirium, severe psychosis, acute renal failure, and seizures. What pharmacological property accounts for their markedly increased toxicity?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "They act as partial antagonists at CB1 receptors with slow receptor binding"},
            {"letter": "B", "is_correct": True, "text": "They are high-potency, full agonists at CB1 receptors with up to 100-fold higher affinity than THC"},
            {"letter": "C", "is_correct": False, "text": "They selectively activate peripheral CB2 receptors without CNS penetration"},
            {"letter": "D", "is_correct": False, "text": "They are irreversible inhibitors of monoamine oxidase"},
            {"letter": "E", "is_correct": False, "text": "They act purely as competitive antagonists at dopamine D2 receptors"}
        ],
        "explanation": "Correct Answer: B. They are high-potency, full agonists at CB1 receptors with up to 100-fold higher affinity than THC.\n\nPharmacological differences between natural THC and synthetic cannabinoids:\n• Natural THC is a low-efficacy PARTIAL agonist at the CB1 receptor.\n• Synthetic cannabinoids (e.g., JWH-018, AB-PINACA) are FULL, high-affinity agonists at CB1 receptors (often 50-100 times more potent than THC). Furthermore, natural cannabis contains cannabidiol (CBD), which modulates and buffers the adverse effects of THC; synthetic blends lack CBD and contain unregulated, highly toxic full agonists that cause profound hyperpyrexia, seizures, psychosis, and death."
    },
    {
        "q_num": "CAN-07",
        "category": "Cannabis Management",
        "stem": "Anandamide is degraded and cleared from the synaptic cleft primarily through enzymatic hydrolysis by which membrane-bound intracellular enzyme?",
        "options": [
            {"letter": "A", "is_correct": True, "text": "Fatty acid amide hydrolase (FAAH)"},
            {"letter": "B", "is_correct": False, "text": "Monoacylglycerol lipase (MAGL)"},
            {"letter": "C", "is_correct": False, "text": "Acetylcholinesterase"},
            {"letter": "D", "is_correct": False, "text": "Catechol-O-methyltransferase (COMT)"},
            {"letter": "E", "is_correct": False, "text": "Phospholipase A2"}
        ],
        "explanation": "Correct Answer: A. Fatty acid amide hydrolase (FAAH).\n\nEndocannabinoid degradation:\n• Anandamide (AEA) is degraded primarily by Fatty Acid Amide Hydrolase (FAAH) into arachidonic acid and ethanolamine.\n• 2-Arachidonoylglycerol (2-AG) is degraded primarily by Monoacylglycerol Lipase (MAGL) into arachidonic acid and glycerol.\nPharmacological inhibition of FAAH or MAGL increases endogenous cannabinoid tone and is an active area of investigation for non-opioid analgesia."
    },
    {
        "q_num": "CAN-08",
        "category": "Cannabis Management",
        "stem": "Dronabinol is an FDA-approved oral medication identical to synthetic delta-9-THC. For which of the following clinical indications is dronabinol approved in modern medical practice?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Major depressive disorder and generalized anxiety"},
            {"letter": "B", "is_correct": True, "text": "Chemotherapy-induced nausea/vomiting and anorexia/cachexia associated with AIDS"},
            {"letter": "C", "is_correct": False, "text": "Parkinson disease motor fluctuations"},
            {"letter": "D", "is_correct": False, "text": "Acute ischemic stroke neuroprotection"},
            {"letter": "E", "is_correct": False, "text": "Chronic obstructive pulmonary disease"}
        ],
        "explanation": "Correct Answer: B. Chemotherapy-induced nausea/vomiting and anorexia/cachexia associated with AIDS.\n\nDronabinol (and nabilone) are oral cannabinoid agonists approved for:\n1. Prevention and treatment of chemotherapy-induced nausea and vomiting (CINV) in patients who have failed conventional antiemetics.\n2. Anorexia associated with weight loss in patients with AIDS (appetite stimulation / orexigenic effect via hypothalamic CB1 stimulation)."
    },
    {
        "q_num": "CAN-09",
        "category": "Cannabis Management",
        "stem": "Which cannabinoid receptor antagonist was previously developed as an anti-obesity drug but was withdrawn from the market worldwide due to severe adverse psychiatric effects, including profound depression, severe anxiety, and increased risk of suicide?",
        "options": [
            {"letter": "A", "is_correct": True, "text": "Rimonabant"},
            {"letter": "B", "is_correct": False, "text": "Sativex"},
            {"letter": "C", "is_correct": False, "text": "Nabilone"},
            {"letter": "D", "is_correct": False, "text": "Cannabinol"},
            {"letter": "E", "is_correct": False, "text": "Beta-caryophyllene"}
        ],
        "explanation": "Correct Answer: A. Rimonabant.\n\nRimonabant is a selective CB1 receptor inverse agonist. By blocking CB1 receptors in the hypothalamus and mesolimbic reward system, it suppressed appetite and promoted weight loss. However, it also blocked endogenous endocannabinoid tone necessary for mood regulation and reward, causing severe depressive symptoms, severe anxiety, and suicidal ideation, leading to its global withdrawal."
    },
    {
        "q_num": "CAN-10",
        "category": "Cannabis Management",
        "stem": "A 19-year-old man undergoes urine drug testing for employment. He last smoked cannabis 2 weeks ago and has not consumed any since. His urine immunoassay test returns strongly positive for cannabinoids. What pharmacokinetic property of THC accounts for its prolonged detection window in urine for weeks after the last use in chronic users?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Irreversible covalent binding to serum albumin"},
            {"letter": "B", "is_correct": True, "text": "High lipophilicity with extensive sequestration in adipose tissue and slow terminal elimination"},
            {"letter": "C", "is_correct": False, "text": "Absence of hepatic metabolism by cytochrome P450 enzymes"},
            {"letter": "D", "is_correct": False, "text": "Active reabsorption across renal collecting duct aquaporin channels"},
            {"letter": "E", "is_correct": False, "text": "Permanent storage within erythrocytes"}
        ],
        "explanation": "Correct Answer: B. High lipophilicity with extensive sequestration in adipose tissue and slow terminal elimination.\n\nTHC is extraordinarily lipophilic (octanol-water partition coefficient > 6000):\n• After inhalation or ingestion, it rapidly distributes into highly vascular tissues, followed by extensive accumulation and storage in body fat (adipose tissue).\n• In chronic users, THC slowly leaches back from adipose stores into the bloodstream over days to weeks.\n• The primary inactive metabolite, 11-nor-9-carboxy-THC (THC-COOH), is conjugated with glucuronic acid and excreted in urine, remaining detectable for 30 days or longer in chronic heavy users."
    },
    {
        "q_num": "CAN-11",
        "category": "Cannabis Management",
        "stem": "Which of the following brain regions exhibits the highest density of cannabinoid CB1 receptors, explaining why acute cannabis intoxication produces significant impairments in working memory, attention, and executive cognitive functioning?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Medullary respiratory center"},
            {"letter": "B", "is_correct": True, "text": "Hippocampus, prefrontal cortex, and basal ganglia"},
            {"letter": "C", "is_correct": False, "text": "Inferior olivary nucleus"},
            {"letter": "D", "is_correct": False, "text": "Ventral tegmental area dopaminergic cell bodies"},
            {"letter": "E", "is_correct": False, "text": "Primary visual cortex"}
        ],
        "explanation": "Correct Answer: B. Hippocampus, prefrontal cortex, and basal ganglia.\n\nCB1 receptor distribution in the brain:\n• High density: Hippocampus (impairs short-term memory consolidation), prefrontal cortex (impairs executive decision-making and attention), basal ganglia and cerebellum (causes psychomotor slowing and impaired coordination).\n• Strikingly LOW density: Brainstem cardiorespiratory centers (pons and medulla). This physiological absence of CB1 receptors in the respiratory control centers explains why fatal respiratory depression does not occur with cannabis overdose alone (unlike opioids or barbiturates)."
    },
    {
        "q_num": "CAN-12",
        "category": "Cannabis Management",
        "stem": "A 21-year-old woman presents to the ED with severe anxiety and panic attacks after using cannabis. She reports seeing shadows moving and hearing whispering voices. Her brother has schizophrenia. Epidemiological studies demonstrate that heavy adolescent cannabis use is associated with a significant increase in the risk of developing which psychiatric disorder in genetically susceptible individuals?",
        "options": [
            {"letter": "A", "is_correct": True, "text": "Schizophrenia (chronic psychotic disorder)"},
            {"letter": "B", "is_correct": False, "text": "Bipolar disorder type 2 only"},
            {"letter": "C", "is_correct": False, "text": "Obsessive-compulsive disorder"},
            {"letter": "D", "is_correct": False, "text": "Anorexia nervosa"},
            {"letter": "E", "is_correct": False, "text": "Autism spectrum disorder"}
        ],
        "explanation": "Correct Answer: A. Schizophrenia (chronic psychotic disorder).\n\nExtensive epidemiological and genetic evidence shows that heavy cannabis use during adolescence (a critical period of neurodevelopment and synaptic pruning) is a dose-dependent environmental risk factor for the earlier onset and development of Schizophrenia and chronic psychotic disorders in genetically predisposed individuals (e.g., carrying polymorphisms in the COMT or AKT1 genes)."
    },
    {
        "q_num": "CAN-13",
        "category": "Cannabis Management",
        "stem": "Delta-9-THC is primarily metabolized in the liver by cytochrome P450 enzymes. Which active metabolite is formed by hepatic CYP2C9 and CYP3A4 oxidation, penetrates the blood-brain barrier rapidly, and has equal or greater psychoactive potency than parent THC?",
        "options": [
            {"letter": "A", "is_correct": True, "text": "11-hydroxy-THC (11-OH-THC)"},
            {"letter": "B", "is_correct": False, "text": "11-nor-9-carboxy-THC (THC-COOH)"},
            {"letter": "C", "is_correct": False, "text": "Cannabinol"},
            {"letter": "D", "is_correct": False, "text": "Cannabigerol"},
            {"letter": "E", "is_correct": False, "text": "Tetrahydrocannabivarin"}
        ],
        "explanation": "Correct Answer: A. 11-hydroxy-THC (11-OH-THC).\n\nWhen cannabis is ingested orally (edibles), THC undergoes extensive first-pass hepatic metabolism by CYP2C9 and CYP3A4 to form 11-hydroxy-THC (11-OH-THC). 11-OH-THC is highly potent, readily crosses the blood-brain barrier, and contributes significantly to the delayed, intense, and prolonged psychoactive effects characteristic of oral edibles compared to inhalation."
    },
    {
        "q_num": "CAN-14",
        "category": "Cannabis Management",
        "stem": "Which of the following physiological effects on the cardiovascular system is most consistently observed following acute cannabis smoking in healthy adults?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Severe bradycardia and systemic hypertension"},
            {"letter": "B", "is_correct": True, "text": "Tachycardia and peripheral vasodilation with potential orthostatic hypotension"},
            {"letter": "C", "is_correct": False, "text": "Complete atrioventricular heart block"},
            {"letter": "D", "is_correct": False, "text": "Pronounced coronary vasodilation without changes in heart rate"},
            {"letter": "E", "is_correct": False, "text": "Decreased cardiac output and reduced myocardial oxygen demand"}
        ],
        "explanation": "Correct Answer: B. Tachycardia and peripheral vasodilation with potential orthostatic hypotension.\n\nAcute cardiovascular effects of cannabis:\n• Dose-dependent resting tachycardia (heart rate increases by 20-50 bpm within minutes, mediated by sympathetic stimulation and parasympathetic withdrawal).\n• Peripheral vasodilation (causing conjunctival injection and facial flushing).\n• Orthostatic hypotension upon standing (which can precipitate syncope in naive users).\n• In patients with pre-existing coronary artery disease, increased myocardial oxygen demand can trigger acute myocardial infarction."
    },
    {
        "q_num": "CAN-15",
        "category": "Cannabis Management",
        "stem": "A 25-year-old patient in the emergency department with severe, intractable cannabinoid hyperemesis syndrome has failed ondansetron, metoclopramide, and promethazine. Which of the following topical therapies applied to the abdomen or back provides rapid symptomatic relief by acting on TRPV1 receptors?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Lidocaine 5% patch"},
            {"letter": "B", "is_correct": True, "text": "Capsaicin 0.025%–0.075% cream"},
            {"letter": "C", "is_correct": False, "text": "Hydrocortisone 1% cream"},
            {"letter": "D", "is_correct": False, "text": "Nitroglycerin paste"},
            {"letter": "E", "is_correct": False, "text": "Diphenhydramine topical gel"}
        ],
        "explanation": "Correct Answer: B. Capsaicin 0.025%–0.075% cream.\n\nTopical capsaicin cream is a highly effective, evidence-based rescue treatment for acute Cannabinoid Hyperemesis Syndrome (CHS) in the ED:\n• Capsaicin binds to and activates Transient Receptor Potential Vanilloid 1 (TRPV1) receptors in the skin, mimicking the sensation of heat provided by hot showers.\n• TRPV1 activation normalizes hypothalamic thermoregulatory signaling and decreases substance P release, breaking the cycle of nausea and vomiting."
    },
    {
        "q_num": "CAN-16",
        "category": "Cannabis Management",
        "stem": "In addition to delta-9-THC and CBD, the Cannabis sativa plant contains more than 100 other phytocannabinoids and aromatic terpenes. Which of the following terpenes is commonly found in cannabis, mangoes, and hops, and is believed to contribute to the sedative effects of certain cannabis strains?",
        "options": [
            {"letter": "A", "is_correct": True, "text": "Myrcene"},
            {"letter": "B", "is_correct": False, "text": "Limonene"},
            {"letter": "C", "is_correct": False, "text": "Pinene"},
            {"letter": "D", "is_correct": False, "text": "Caryophyllene"},
            {"letter": "E", "is_correct": False, "text": "Linalool"}
        ],
        "explanation": "Correct Answer: A. Myrcene.\n\nMyrcene (beta-myrcene) is the most abundant terpene found in Cannabis sativa (as well as mangoes, hops, and lemongrass). It produces a characteristic earthy, musky aroma and contributes to muscle relaxation, sedation ('couch-lock'), and enhanced blood-brain barrier permeability via the proposed 'entourage effect.'"
    },
    {
        "q_num": "CAN-17",
        "category": "Cannabis Management",
        "stem": "Cannabinoid receptor type 2 (CB2) is structurally homologous to CB1 but exhibits a completely different anatomical distribution. CB2 receptors are primarily localized to which of the following tissues?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Cerebral cortical pyramidal neurons"},
            {"letter": "B", "is_correct": True, "text": "Cells of the immune system (spleen, tonsils, B-cells, macrophages, and microglia)"},
            {"letter": "C", "is_correct": False, "text": "Hippocampal CA1 pyramidal neurons"},
            {"letter": "D", "is_correct": False, "text": "Cerebellar Purkinje cells"},
            {"letter": "E", "is_correct": False, "text": "Renal proximal tubular epithelial cells"}
        ],
        "explanation": "Correct Answer: B. Cells of the immune system (spleen, tonsils, B-cells, macrophages, and microglia).\n\nCB2 receptors are predominantly peripheral cannabinoid receptors expressed at high levels in immune and hematopoietic cells (macrophages, B-cells, T-cells, spleen, tonsils) and activated CNS microglia. Unlike CB1 receptors, activation of CB2 receptors modulates cytokine release and immune responses without producing psychoactive effects or intoxication."
    },
    {
        "q_num": "CAN-18",
        "category": "Cannabis Management",
        "stem": "Which of the following behavioral interventions has the strongest clinical evidence base for the treatment of Cannabis Use Disorder (CUD)?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "High-dose pharmacotherapy with naltrexone"},
            {"letter": "B", "is_correct": True, "text": "Cognitive Behavioral Therapy (CBT), Motivational Enhancement Therapy (MET), and Contingency Management (CM)"},
            {"letter": "C", "is_correct": False, "text": "Subcutaneous buprenorphine depot"},
            {"letter": "D", "is_correct": False, "text": "Electroconvulsive therapy"},
            {"letter": "E", "is_correct": False, "text": "Disulfiram maintenance therapy"}
        ],
        "explanation": "Correct Answer: B. Cognitive Behavioral Therapy (CBT), Motivational Enhancement Therapy (MET), and Contingency Management (CM).\n\nThere are currently no FDA-approved medications for the treatment of Cannabis Use Disorder. The gold standard evidence-based treatments are psychosocial and behavioral interventions:\n• Cognitive Behavioral Therapy (CBT): Teaches coping strategies, craving management, and relapse prevention.\n• Motivational Enhancement Therapy (MET): Resolves ambivalence regarding quitting.\n• Contingency Management (CM): Provides tangible rewards for confirmed negative toxicology screens."
    },
    {
        "q_num": "CAN-19",
        "category": "Cannabis Management",
        "stem": "What is the primary cellular signaling cascade initiated when delta-9-THC binds to the Gi/o-protein coupled CB1 receptor on a presynaptic nerve terminal?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Activation of adenylyl cyclase, increased cAMP, and opening of L-type calcium channels"},
            {"letter": "B", "is_correct": True, "text": "Inhibition of adenylyl cyclase, decreased cAMP, inhibition of voltage-gated calcium channels, and activation of inwardly rectifying potassium channels"},
            {"letter": "C", "is_correct": False, "text": "Activation of phospholipase C, generation of IP3 and DAG, and intracellular calcium surge"},
            {"letter": "D", "is_correct": False, "text": "Direct opening of a non-selective cation channel pore conducting sodium and calcium"},
            {"letter": "E", "is_correct": False, "text": "Stimulation of tyrosine kinase phosphorylation"}
        ],
        "explanation": "Correct Answer: B. Inhibition of adenylyl cyclase, decreased cAMP, inhibition of voltage-gated calcium channels, and activation of inwardly rectifying potassium channels.\n\nCB1 receptor downstream signaling:\n• Coupling: Pertussis toxin-sensitive inhibitory Gi/o protein.\n• Alpha-subunit: Inhibits adenylyl cyclase, decreasing cyclic AMP (cAMP) and protein kinase A (PKA) activity.\n• Beta-gamma subunit: Directly inhibits presynaptic voltage-gated N-type and P/Q-type Ca2+ channels (reducing exocytotic neurotransmitter release) and stimulates G-protein inwardly rectifying potassium (GIRK) channels, causing membrane hyperpolarization."
    },
    {
        "q_num": "CAN-20",
        "category": "Cannabis Management",
        "stem": "A 17-year-old driver is involved in a motor vehicle collision. Blood testing confirms acute delta-9-THC intoxication. Which of the following psychomotor impairments is most directly responsible for the increased risk of vehicular crashes associated with acute cannabis consumption?",
        "options": [
            {"letter": "A", "is_correct": True, "text": "Impaired divided attention, delayed reaction time, and lane-weaving (decreased tracking ability)"},
            {"letter": "B", "is_correct": False, "text": "Complete loss of color vision"},
            {"letter": "C", "is_correct": False, "text": "Generalized spastic muscle rigidity"},
            {"letter": "D", "is_correct": False, "text": "Severe irreversible bilateral hearing loss"},
            {"letter": "E", "is_correct": False, "text": "Catatonic stupor"}
        ],
        "explanation": "Correct Answer: A. Impaired divided attention, delayed reaction time, and lane-weaving (decreased tracking ability).\n\nAcute cannabis-induced driving impairment:\n• Psychomotor effects: Increased reaction time, impaired divided attention (inability to process multiple visual inputs simultaneously), impaired tracking/lane-keeping ability, and distorted perception of speed and time.\n• Risk: Increases crash risk approximately 2-fold, and synergistically increases risk when combined with alcohol."
    },

    # =========================================================================
    # 14. PATHWAYS AND OPIOIDS (20 Questions: Q21 - Q40)
    # =========================================================================
    {
        "q_num": "OPIOID-01",
        "category": "Pathways and Opioids",
        "stem": "A 28-year-old man is found unresponsive in an alley. Physical examination reveals a respiratory rate of 4 breaths/minute, pinpoint pupils (miosis, 1 mm bilaterally), cold clammy skin, and cyanosis. Intravenous naloxone is administered, and within 90 seconds, the patient awakens, his pupils dilate, and his respiratory rate increases to 16 breaths/minute. What is the mechanism of action of naloxone?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Partial agonist at mu-opioid receptors"},
            {"letter": "B", "is_correct": True, "text": "Competitive antagonist at mu-, kappa-, and delta-opioid receptors with highest affinity for mu"},
            {"letter": "C", "is_correct": False, "text": "Allosteric inhibitor of GABA-A receptors"},
            {"letter": "D", "is_correct": False, "text": "Direct stimulant of the medullary pre-Bötzinger respiratory complex"},
            {"letter": "E", "is_correct": False, "text": "Selective inhibitor of acetylcholinesterase"}
        ],
        "explanation": "Correct Answer: B. Competitive antagonist at mu-, kappa-, and delta-opioid receptors with highest affinity for mu.\n\nNaloxone is a pure, short-acting competitive opioid receptor antagonist with high affinity for mu-opioid receptors (and lower affinity for kappa and delta receptors). It rapidly displaces opioid agonists from the receptor, reversing life-threatening opioid overdose signs (respiratory depression, coma, miosis). Because naloxone has a short half-life (~30-90 minutes), patients who ingested long-acting opioids (e.g., methadone) must be monitored closely for recurrent respiratory arrest."
    },
    {
        "q_num": "OPIOID-02",
        "category": "Pathways and Opioids",
        "stem": "Opioid receptors (mu, delta, kappa) are G-protein coupled receptors coupled to Gi/o proteins. When an opioid agonist binds to the mu-opioid receptor, which two downstream ion channel events occur in the presynaptic terminal and postsynaptic neuron, respectively, to inhibit pain transmission?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Presynaptic: Opening of calcium channels; Postsynaptic: Closure of potassium channels"},
            {"letter": "B", "is_correct": True, "text": "Presynaptic: Closure of voltage-gated calcium channels; Postsynaptic: Opening of inwardly rectifying potassium channels"},
            {"letter": "C", "is_correct": False, "text": "Presynaptic: Influx of sodium; Postsynaptic: Efflux of chloride"},
            {"letter": "D", "is_correct": False, "text": "Presynaptic: Opening of chloride channels; Postsynaptic: Influx of calcium"},
            {"letter": "E", "is_correct": False, "text": "Presynaptic: Inhibition of Na+/K+ ATPase; Postsynaptic: Activation of NMDA receptors"}
        ],
        "explanation": "Correct Answer: B. Presynaptic: Closure of voltage-gated calcium channels; Postsynaptic: Opening of inwardly rectifying potassium channels.\n\nCellular mechanism of opioid action:\n• Presynaptic inhibition: Activation of Gi/o-coupled mu-opioid receptors closes voltage-gated Ca2+ channels in primary nociceptive terminals, preventing Ca2+ influx and blocking the exocytosis of excitatory neurotransmitters (substance P, glutamate, CGRP).\n• Postsynaptic inhibition: In postsynaptic projection neurons, beta-gamma subunits directly open G-protein coupled inwardly rectifying K+ (GIRK) channels, allowing K+ efflux. This hyperpolarizes the postsynaptic membrane, rendering it refractory to excitatory input."
    },
    {
        "q_num": "OPIOID-03",
        "category": "Pathways and Opioids",
        "stem": "A 52-year-old woman with metastatic breast cancer has been taking escalating doses of oral morphine for 6 months. She has developed significant pharmacological tolerance to most of the analgesic and adverse effects of morphine. Which of the following physiological effects of opioids NEVER develops tolerance, regardless of treatment duration?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Analgesia and euphoria"},
            {"letter": "B", "is_correct": False, "text": "Respiratory depression and sedation"},
            {"letter": "C", "is_correct": True, "text": "Miosis (pupillary constriction) and constipation"},
            {"letter": "D", "is_correct": False, "text": "Nausea and vomiting"},
            {"letter": "E", "is_correct": False, "text": "Biliary colic"}
        ],
        "explanation": "Correct Answer: C. Miosis (pupillary constriction) and constipation.\n\nOpioid tolerance development:\n• High tolerance develops rapidly to: Analgesia, euphoria, sedation, respiratory depression, nausea, and vomiting.\n• Minimal or NO tolerance develops to:\n  1. Miosis (pinpoint pupils via Edinger-Westphal parasympathetic nucleus stimulation).\n  2. Constipation (decreased peristalsis and secretomotor inhibition in enteric nervous system).\nTherefore, all patients on chronic opioid therapy require prophylactic bowel regimens (e.g., senna, docusate, polyethylene glycol, or peripheral mu-antagonists like methylnaltrexone)."
    },
    {
        "q_num": "OPIOID-04",
        "category": "Pathways and Opioids",
        "stem": "Which of the following endogenous opioid peptides is derived from the prohormone pro-opiomelanocortin (POMC), possesses the highest affinity for mu-opioid receptors, and is synthesized in the anterior pituitary alongside adrenocorticotropic hormone (ACTH) and melanocyte-stimulating hormone (MSH)?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Leu-enkephalin"},
            {"letter": "B", "is_correct": False, "text": "Met-enkephalin"},
            {"letter": "C", "is_correct": True, "text": "Beta-endorphin"},
            {"letter": "D", "is_correct": False, "text": "Dynorphin A"},
            {"letter": "E", "is_correct": False, "text": "Nociceptin"}
        ],
        "explanation": "Correct Answer: C. Beta-endorphin.\n\nEndogenous opioid peptides and precursors:\n• Pro-opiomelanocortin (POMC): Cleaved to produce Beta-endorphin (potent mu-agonist), ACTH, and alpha-MSH in the pituitary and arcuate nucleus.\n• Proenkephalin: Cleaved to produce Met-enkephalin and Leu-enkephalin (preferential delta-opioid receptor agonists).\n• Prodynorphin: Cleaved to produce Dynorphin A and B (preferential kappa-opioid receptor agonists, which mediate dysphoria)."
    },
    {
        "q_num": "OPIOID-05",
        "category": "Pathways and Opioids",
        "stem": "A 35-year-old man with opioid use disorder who is dependent on intravenous heroin is given an injection of buprenorphine. Within 45 minutes, he develops severe gooseflesh (piloerection), pupillary dilation (mydriasis), diarrhea, lacrimation, severe abdominal cramping, and muscle aches. Why did buprenorphine precipitate acute opioid withdrawal in this patient?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Buprenorphine is an irreversible antagonist at all opioid receptors"},
            {"letter": "B", "is_correct": True, "text": "Buprenorphine is a partial mu-opioid agonist with high receptor affinity that displaces full agonists"},
            {"letter": "C", "is_correct": False, "text": "Buprenorphine blocks dopamine D2 receptors in the nucleus accumbens"},
            {"letter": "D", "is_correct": False, "text": "Buprenorphine accelerates renal clearance of heroin"},
            {"letter": "E", "is_correct": False, "text": "Buprenorphine is metabolized into naloxone in vivo"}
        ],
        "explanation": "Correct Answer: B. Buprenorphine is a partial mu-opioid agonist with high receptor affinity that displaces full agonists.\n\nBuprenorphine has two critical pharmacological properties:\n1. Extremely high binding affinity for the mu-opioid receptor (higher than heroin, morphine, or methadone).\n2. Low intrinsic activity (partial agonist).\nWhen administered to a patient who has active full mu-opioid agonists on their receptors, buprenorphine avidly binds and displaces the full agonist. Because its intrinsic efficacy is lower, the net level of mu-opioid receptor activation abruptly drops, precipitating acute precipitated withdrawal. Therefore, buprenorphine must only be initiated when the patient is already in mild-to-moderate spontaneous withdrawal (COWS score ≥ 8-12)."
    },
    {
        "q_num": "OPIOID-06",
        "category": "Pathways and Opioids",
        "stem": "Suboxone is a combination medication used for the maintenance treatment of opioid use disorder. It contains buprenorphine and naloxone in a 4:1 ratio. What is the clinical rationale for including naloxone in this sublingual formulation?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "To increase the oral absorption of buprenorphine"},
            {"letter": "B", "is_correct": True, "text": "To prevent intravenous abuse; naloxone has poor sublingual bioavailability but precipitates withdrawal if injected"},
            {"letter": "C", "is_correct": False, "text": "To enhance buprenorphine-induced analgesia synergistically"},
            {"letter": "D", "is_correct": False, "text": "To prevent buprenorphine from crossing the blood-brain barrier"},
            {"letter": "E", "is_correct": False, "text": "To treat underlying depression simultaneously"}
        ],
        "explanation": "Correct Answer: B. To prevent intravenous abuse; naloxone has poor sublingual bioavailability but precipitates withdrawal if injected.\n\nPharmacological design of Suboxone (buprenorphine/naloxone):\n• When taken sublingually as prescribed: Buprenorphine is absorbed across the oral mucosa, while naloxone has near-zero sublingual bioavailability (<5%) and undergoes extensive first-pass hepatic metabolism, producing therapeutic buprenorphine maintenance without interference.\n• If crushed and injected intravenously: Naloxone becomes 100% bioavailable, immediately blocking opioid receptors and precipitating severe, unpleasant withdrawal, thereby strongly deterring intravenous diversion and abuse."
    },
    {
        "q_num": "OPIOID-07",
        "category": "Pathways and Opioids",
        "stem": "A 45-year-old man with chronic severe pain is prescribed methadone. In addition to serving as a potent, long-acting full mu-opioid receptor agonist, methadone possesses which additional unique pharmacological property that makes it effective for neuropathic pain but warrants routine baseline electrocardiograms?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "GABA-A agonist; PR interval shortening"},
            {"letter": "B", "is_correct": True, "text": "NMDA receptor antagonist and serotonin/norepinephrine reuptake inhibitor; hERG channel block causing QT prolongation"},
            {"letter": "C", "is_correct": False, "text": "Alpha-1 adrenergic agonist; ST-segment elevation"},
            {"letter": "D", "is_correct": False, "text": "Dopamine reuptake inhibitor; Delta wave on ECG"},
            {"letter": "E", "is_correct": False, "text": "Muscarinic M2 receptor agonist; Ventricular pre-excitation"}
        ],
        "explanation": "Correct Answer: B. NMDA receptor antagonist and serotonin/norepinephrine reuptake inhibitor; hERG channel block causing QT prolongation.\n\nMethadone unique pharmacology:\n• Full mu-opioid agonist with long elimination half-life (24-60 hours).\n• Non-competitive NMDA receptor antagonist: Prevents central sensitization and opioid tolerance, making it uniquely effective in refractory neuropathic pain.\n• Inhibits serotonin and norepinephrine reuptake.\n• Cardiotoxicity: Blocks cardiac hERG potassium channels, causing QT interval prolongation and torsades de pointes (ventricular tachycardia). Baseline and follow-up ECG monitoring is recommended."
    },
    {
        "q_num": "OPIOID-08",
        "category": "Pathways and Opioids",
        "stem": "Which of the following synthetic opioids is 50 to 100 times more potent than morphine, is highly lipophilic with a rapid onset (within 1–2 minutes), and can cause fatal wooden chest syndrome (thoracoabdominal muscle rigidity preventing mechanical ventilation) when administered rapidly as an intravenous bolus?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Codeine"},
            {"letter": "B", "is_correct": False, "text": "Meperidine"},
            {"letter": "C", "is_correct": True, "text": "Fentanyl"},
            {"letter": "D", "is_correct": False, "text": "Hydrocodone"},
            {"letter": "E", "is_correct": False, "text": "Morphine-6-glucuronide"}
        ],
        "explanation": "Correct Answer: C. Fentanyl.\n\nFentanyl is a synthetic phenylpiperidine opioid:\n• Potency: ~100 times more potent than morphine due to high lipophilicity.\n• Rapid bolus adverse effect: 'Wooden chest syndrome' (severe chest wall and abdominal muscle rigidity mediated by central striatal and locus coeruleus pathways), which impairs chest expansion and prevents bag-valve-mask ventilation. Treatment is immediate administration of naloxone and/or a neuromuscular blocker."
    },
    {
        "q_num": "OPIOID-09",
        "category": "Pathways and Opioids",
        "stem": "A 58-year-old woman with end-stage renal disease receives multiple doses of meperidine (pethidine) for post-surgical pain. Two days later, she develops severe myoclonus, hyperreflexia, agitation, and generalized tonic-clonic seizures. Accumulation of which neurotoxic metabolite caused her seizures?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Morphine-6-glucuronide"},
            {"letter": "B", "is_correct": True, "text": "Normeperidine"},
            {"letter": "C", "is_correct": False, "text": "Hydromorphone"},
            {"letter": "D", "is_correct": False, "text": "6-monoacetylmorphine"},
            {"letter": "E", "is_correct": False, "text": "Oxycodone-N-oxide"}
        ],
        "explanation": "Correct Answer: B. Normeperidine.\n\nMeperidine is metabolized in the liver via N-demethylation to Normeperidine, an active metabolite with a long half-life (15-30 hours). Normeperidine has minimal analgesic effect but is a potent central nervous system convulsant. In renal impairment or with repeated dosing, normeperidine accumulates, causing tremors, myoclonus, hyperreflexia, and grand mal seizures. Naloxone does not reverse (and may worsen) normeperidine-induced seizures."
    },
    {
        "q_num": "OPIOID-10",
        "category": "Pathways and Opioids",
        "stem": "Which of the following peripheral mu-opioid receptor antagonists is quaternary and permanently charged, preventing it from crossing the blood-brain barrier, allowing it to treat opioid-induced constipation without reversing central analgesia or precipitating opioid withdrawal?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Naloxone"},
            {"letter": "B", "is_correct": False, "text": "Naltrexone"},
            {"letter": "C", "is_correct": True, "text": "Methylnaltrexone"},
            {"letter": "D", "is_correct": False, "text": "Buprenorphine"},
            {"letter": "E", "is_correct": False, "text": "Nalmefene"}
        ],
        "explanation": "Correct Answer: C. Methylnaltrexone.\n\nMethylnaltrexone (and naloxegol) is a peripherally acting mu-opioid receptor antagonist (PAMORA). The addition of a methyl group to the amine ring confers a permanent positive charge, preventing the molecule from crossing the blood-brain barrier. It selectively blocks gastrointestinal mu-opioid receptors, restoring bowel motility in opioid-induced constipation without reversing central analgesia or causing withdrawal."
    },
    {
        "q_num": "OPIOID-11",
        "category": "Pathways and Opioids",
        "stem": "Morphine undergoes phase II hepatic glucuronidation to produce two major metabolites: morphine-3-glucuronide (M3G) and morphine-6-glucuronide (M6G). Which statement regarding M6G is pharmacologically correct?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "M6G is an inactive metabolite with no biological activity"},
            {"letter": "B", "is_correct": True, "text": "M6G is a potent analgesic that accumulates in renal failure to cause prolonged sedation and respiratory depression"},
            {"letter": "C", "is_correct": False, "text": "M6G is a pure antagonist that precipitates acute withdrawal"},
            {"letter": "D", "is_correct": False, "text": "M6G is primarily excreted in expired air via the lungs"},
            {"letter": "E", "is_correct": False, "text": "M6G produces neuroexcitation and hyperalgesia without analgesia"}
        ],
        "explanation": "Correct Answer: B. M6G is a potent analgesic that accumulates in renal failure to cause prolonged sedation and respiratory depression.\n\nMorphine metabolism:\n• Morphine-6-glucuronide (M6G, ~10%): Active metabolite with high mu-opioid affinity and potent analgesic efficacy (more potent than morphine itself). It is cleared by the kidneys; in renal insufficiency, M6G accumulates, causing prolonged sedation and life-threatening respiratory depression.\n• Morphine-3-glucuronide (M3G, ~60%): Lacks opioid analgesic activity and causes neuroexcitation, allodynia, and myoclonus."
    },
    {
        "q_num": "OPIOID-12",
        "category": "Pathways and Opioids",
        "stem": "A 22-year-old man presents with acute abdominal pain and diarrhea. He takes loperamide. Loperamide is an effective antidiarrheal agent that acts as a mu-opioid agonist in the myenteric plexus. Why does loperamide not produce central euphoria or analgesia at therapeutic doses?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "It is an antagonist at central mu-opioid receptors"},
            {"letter": "B", "is_correct": True, "text": "It is actively extruded from the brain across the blood-brain barrier by P-glycoprotein efflux pumps"},
            {"letter": "C", "is_correct": False, "text": "It is completely destroyed by gastric acid"},
            {"letter": "D", "is_correct": False, "text": "It binds exclusively to kappa-opioid receptors"},
            {"letter": "E", "is_correct": False, "text": "It cannot dissolve in plasma"}
        ],
        "explanation": "Correct Answer: B. It is actively extruded from the brain across the blood-brain barrier by P-glycoprotein efflux pumps.\n\nLoperamide is a potent mu-opioid receptor agonist in the gastrointestinal myenteric plexus (slowing peristalsis and extending transit time). Although lipophilic, any drug that crosses into brain capillary endothelial cells is actively and efficiently pumped back into the blood by the P-glycoprotein (MDR1) efflux transporter. Consequently, brain levels remain negligible at standard therapeutic doses, preventing euphoria and addiction. (Massive supratherapeutic doses saturate P-glycoprotein, causing CNS opioid effects and fatal QTc prolongation/cardiac arrest)."
    },
    {
        "q_num": "OPIOID-13",
        "category": "Pathways and Opioids",
        "stem": "Which of the following prodrug opioids must be metabolized in the liver by Cytochrome P450 2D6 (CYP2D6) into morphine to achieve its primary analgesic effect, explaining why CYP2D6 'ultra-rapid metabolizers' are at high risk of fatal respiratory depression?",
        "options": [
            {"letter": "A", "is_correct": True, "text": "Codeine"},
            {"letter": "B", "is_correct": False, "text": "Fentanyl"},
            {"letter": "C", "is_correct": False, "text": "Hydromorphone"},
            {"letter": "D", "is_correct": False, "text": "Buprenorphine"},
            {"letter": "E", "is_correct": False, "text": "Methadone"}
        ],
        "explanation": "Correct Answer: A. Codeine.\n\nCodeine (3-methylmorphine) is a weak prodrug with low intrinsic affinity for mu-receptors (~200-fold less than morphine). It requires O-demethylation to active Morphine by CYP2D6:\n• Poor metabolizers (~7-10% of Caucasians): Lack functional CYP2D6 and experience little to no pain relief.\n• Ultra-rapid metabolizers (gene duplication, up to 30% in North African/Middle Eastern populations): Rapidly convert codeine into high, toxic concentrations of morphine. Nursing mothers who are ultra-rapid metabolizers pass lethal concentrations of morphine in breast milk to their infants."
    },
    {
        "q_num": "OPIOID-14",
        "category": "Pathways and Opioids",
        "stem": "Tramadol provides analgesia through a dual mechanism: weak agonism at mu-opioid receptors and inhibition of the reuptake of which two neurotransmitters?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Dopamine and GABA"},
            {"letter": "B", "is_correct": True, "text": "Serotonin and norepinephrine"},
            {"letter": "C", "is_correct": False, "text": "Acetylcholine and glycine"},
            {"letter": "D", "is_correct": False, "text": "Glutamate and substance P"},
            {"letter": "E", "is_correct": False, "text": "Histamine and adenosine"}
        ],
        "explanation": "Correct Answer: B. Serotonin and norepinephrine.\n\nTramadol is an atypical centrally acting analgesic with a dual mechanism:\n1. Its active metabolite (O-desmethyltramadol / M1, formed via CYP2D6) is a mu-opioid receptor agonist.\n2. The parent drug inhibits the neuronal reuptake of both Serotonin (5-HT) and Norepinephrine (NE), potentiating descending spinal pain-inhibitory pathways.\n• Risks: Lowers the seizure threshold and can precipitate Serotonin Syndrome when combined with SSRIs, SNRIs, or triptans."
    },
    {
        "q_num": "OPIOID-15",
        "category": "Pathways and Opioids",
        "stem": "Which opioid receptor subtype, when selectively stimulated by dynorphins or synthetic agonists such as pentazocine and salvinorin A, produces spinal analgesia accompanied by dysphoria, hallucinations, and depersonalization rather than euphoria?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Mu-opioid receptor (MOR)"},
            {"letter": "B", "is_correct": False, "text": "Delta-opioid receptor (DOR)"},
            {"letter": "C", "is_correct": True, "text": "Kappa-opioid receptor (KOR)"},
            {"letter": "D", "is_correct": False, "text": "Nociceptin receptor (NOP)"},
            {"letter": "E", "is_correct": False, "text": "Sigma-1 receptor"}
        ],
        "explanation": "Correct Answer: C. Kappa-opioid receptor (KOR).\n\n• Mu receptors (MOR): Mediate supraspinal analgesia, euphoria, physical dependence, miosis, constipation, and respiratory depression.\n• Kappa receptors (KOR): Mediate spinal analgesia, miosis, sedation, and characteristically DYSPHORIA, psychotomimetic hallucinations, and anxiety (by inhibiting dopamine release in the nucleus accumbens). Dynorphins are the endogenous ligands.\n• Delta receptors (DOR): Mediate analgesia and modulate emotional responses."
    },
    {
        "q_num": "OPIOID-16",
        "category": "Pathways and Opioids",
        "stem": "Following intravenous administration of morphine, a patient develops localized pruritus, flushing, warm skin, and mild bronchospasm. Blood pressure drops slightly. This reaction is non-immunologic (not IgE-mediated) and occurs through which mechanism?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Direct activation of H1 receptors by morphine"},
            {"letter": "B", "is_correct": True, "text": "Direct non-allergic mast cell degranulation via MRGPRX2 receptors with histamine release"},
            {"letter": "C", "is_correct": False, "text": "Anaphylactic Type I hypersensitivity reaction"},
            {"letter": "D", "is_correct": False, "text": "Inhibition of complement factor H"},
            {"letter": "E", "is_correct": False, "text": "Excessive bradykinin synthesis"}
        ],
        "explanation": "Correct Answer: B. Direct non-allergic mast cell degranulation via MRGPRX2 receptors with histamine release.\n\nNatural and semi-synthetic phenanthrene opioids (morphine, codeine, meperidine) can directly stimulate cutaneous mast cells via Mas-related G protein-coupled receptor X2 (MRGPRX2), triggering non-IgE-mediated histamine release. This pseudo-allergic reaction causes pruritus, urticaria, facial flushing, hypotension, and mild bronchospasm. In contrast, synthetic opioids (such as fentanyl) do not trigger histamine release."
    },
    {
        "q_num": "OPIOID-17",
        "category": "Pathways and Opioids",
        "stem": "Naltrexone is an orally bioavailable, long-acting opioid receptor antagonist with a half-life of approximately 10 hours. In addition to preventing relapse in detoxified opioid-dependent individuals, naltrexone is FDA-approved for the treatment of which other substance use disorder?",
        "options": [
            {"letter": "A", "is_correct": True, "text": "Alcohol use disorder"},
            {"letter": "B", "is_correct": False, "text": "Cocaine use disorder"},
            {"letter": "C", "is_correct": False, "text": "Cannabis use disorder"},
            {"letter": "D", "is_correct": False, "text": "Tobacco use disorder"},
            {"letter": "E", "is_correct": False, "text": "Benzodiazepine dependence"}
        ],
        "explanation": "Correct Answer: A. Alcohol use disorder.\n\nNaltrexone is FDA-approved for Alcohol Use Disorder (AUD):\n• Mechanism: Alcohol consumption stimulates endogenous beta-endorphin release, which disinhibits dopamine neurons in the ventral tegmental area (VTA) to produce reinforcing euphoria. Naltrexone blocks mu-opioid receptors, eliminating the positive reinforcing reward and euphoria of alcohol, thereby reducing cravings and heavy drinking days."
    },
    {
        "q_num": "OPIOID-18",
        "category": "Pathways and Opioids",
        "stem": "In the brainstem, which neural region is responsible for the blunting of hypercapnic and hypoxic ventilatory drive during opioid-induced respiratory depression?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Locus coeruleus"},
            {"letter": "B", "is_correct": True, "text": "Pre-Bötzinger complex and medullary respiratory rhythm generator"},
            {"letter": "C", "is_correct": False, "text": "Pneumotaxic center in the rostral pons"},
            {"letter": "D", "is_correct": False, "text": "Area postrema"},
            {"letter": "E", "is_correct": False, "text": "Nucleus ambiguus"}
        ],
        "explanation": "Correct Answer: B. Pre-Bötzinger complex and medullary respiratory rhythm generator.\n\nOpioid-induced respiratory depression (OIRD) is the leading cause of death in opioid overdose:\n• Mu-opioid receptors are densely expressed in the Pre-Bötzinger complex (the pacemaker for inspiratory rhythm) and ventral respiratory group in the medulla.\n• Agonist binding hyperpolarizes rhythm-generating neurons, decreasing respiratory frequency and blunting the medullary chemoreceptor response to rising PaCO2."
    },
    {
        "q_num": "OPIOID-19",
        "category": "Pathways and Opioids",
        "stem": "A 40-year-old patient who had been taking high-dose oxycodone for 6 months stops abruptly. Within 24 hours, he develops severe autonomic hyperarousal, diaphoresis, rhinorrhea, lacrimation, piloerection ('cold turkey'), tachycardia, and hypertension. This physical withdrawal syndrome is driven primarily by rebound hyperactivity of which central noradrenergic nucleus?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Substantia nigra pars compacta"},
            {"letter": "B", "is_correct": True, "text": "Locus coeruleus in the rostral pons"},
            {"letter": "C", "is_correct": False, "text": "Nucleus raphe magnus"},
            {"letter": "D", "is_correct": False, "text": "Red nucleus"},
            {"letter": "E", "is_correct": False, "text": "Caudate nucleus"}
        ],
        "explanation": "Correct Answer: B. Locus coeruleus in the rostral pons.\n\nPathophysiology of opioid withdrawal:\n• Chronic opioid exposure chronically inhibits the noradrenergic Locus Coeruleus (LC). In response, LC neurons homeostatically upregulate adenylyl cyclase, cAMP, and protein kinase A.\n• When the opioid is abruptly withdrawn, this chronic inhibition is lifted, causing massive rebound noradrenergic hyperactivity from the locus coeruleus.\n• Alpha-2 adrenergic agonists (Clonidine or Lofexidine) bind to inhibitory presynaptic alpha-2 receptors on LC neurons, suppressing this sympathetic outflow and relieving withdrawal symptoms."
    },
    {
        "q_num": "OPIOID-20",
        "category": "Pathways and Opioids",
        "stem": "Which of the following mixed opioid agonist-antagonists acts as a kappa-opioid receptor agonist and a weak mu-opioid receptor partial agonist/antagonist, and is used for moderate pain or labor analgesia with a lower ceiling for respiratory depression?",
        "options": [
            {"letter": "A", "is_correct": True, "text": "Butorphanol (or Nalbuphine)"},
            {"letter": "B", "is_correct": False, "text": "Methadone"},
            {"letter": "C", "is_correct": False, "text": "Fentanyl"},
            {"letter": "D", "is_correct": False, "text": "Hydromorphone"},
            {"letter": "E", "is_correct": False, "text": "Oxymorphone"}
        ],
        "explanation": "Correct Answer: A. Butorphanol (or Nalbuphine).\n\nButorphanol and Nalbuphine are mixed opioid agonist-antagonists:\n• Kappa agonist: Produces analgesia.\n• Mu partial agonist or antagonist: Exhibits a 'ceiling effect' for respiratory depression (less lethal overdose risk), but can precipitate acute withdrawal if administered to patients physically dependent on full mu-opioid agonists."
    },

    # =========================================================================
    # 15. TRAUMATIC BRAIN INJURIES (20 Questions: Q41 - Q60)
    # =========================================================================
    {
        "q_num": "TBI-01",
        "category": "Traumatic Brain Injuries",
        "stem": "A 22-year-old man involved in a high-speed motor vehicle collision is brought to the trauma bay. On examination, he opens his eyes only in response to painful sternal rub, utters inappropriate disorganized words, and flexes his elbows and wrists abnormally (decorticate posturing) in response to pain. What is his Glasgow Coma Scale (GCS) score?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "GCS 6"},
            {"letter": "B", "is_correct": True, "text": "GCS 8 (Severe TBI)"},
            {"letter": "C", "is_correct": False, "text": "GCS 10"},
            {"letter": "D", "is_correct": False, "text": "GCS 12"},
            {"letter": "E", "is_correct": False, "text": "GCS 4"}
        ],
        "explanation": "Correct Answer: B. GCS 8 (Severe TBI).\n\nGlasgow Coma Scale (GCS) calculation (E + V + M):\n• Eye opening (E, max 4): Opens eyes to pain = 2 points.\n• Verbal response (V, max 5): Inappropriate words = 3 points.\n• Motor response (M, max 6): Abnormal flexion (decorticate posturing) = 3 points.\nTotal Score = 2 + 3 + 3 = 8.\n• A GCS of ≤ 8 defines Severe Traumatic Brain Injury and represents an indication for definitive endotracheal intubation ('GCS of 8, intubate')."
    },
    {
        "q_num": "TBI-02",
        "category": "Traumatic Brain Injuries",
        "stem": "An unconscious patient with severe traumatic brain injury displays abnormal decerebrate (extensor) posturing (arms adducted and internally rotated, elbows rigidly extended, wrists pronated and flexed). Decerebrate posturing indicates a compressive lesion or herniation disrupting the brainstem at which level?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Cerebral cortex above the thalamus"},
            {"letter": "B", "is_correct": False, "text": "Internal capsule with intact midbrain"},
            {"letter": "C", "is_correct": True, "text": "Brainstem below the red nucleus (upper pons or lower midbrain)"},
            {"letter": "D", "is_correct": False, "text": "Cervical spinal cord at C5"},
            {"letter": "E", "is_correct": False, "text": "Cerebellar cortex"}
        ],
        "explanation": "Correct Answer: C. Brainstem below the red nucleus (upper pons or lower midbrain).\n\nPosturing in brain herniation and coma:\n• Decorticate posturing (flexor posturing): Lesions ABOVE the red nucleus (cerebral cortex or internal capsule). Rubrospinal tract is intact, maintaining flexor tone in upper extremities.\n• Decerebrate posturing (extensor posturing): Lesions AT OR BELOW the red nucleus (midbrain-pons junction). Rubrospinal facilitatory flexor drive is lost, leaving unopposed vestibulospinal and reticulospinal drive that causes rigid extension of all extremities. Decerebrate carries a worse prognosis."
    },
    {
        "q_num": "TBI-03",
        "category": "Traumatic Brain Injuries",
        "stem": "A 30-year-old construction worker falls from a scaffolding and strikes his head. In the emergency department, his blood pressure increases from 125/80 to 195/105 mm Hg, his heart rate drops from 82 to 44 bpm, and his breathing pattern becomes irregular with periods of apnea (Cheyne-Stokes respirations). What physiological phenomenon is this patient exhibiting, and what does it indicate?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Bezold-Jarisch reflex; Acute inferior wall myocardial infarction"},
            {"letter": "B", "is_correct": True, "text": "Cushing triad; Severe intracranial hypertension with impending brain herniation"},
            {"letter": "C", "is_correct": False, "text": "Brown-Séquard syndrome; High cervical cord transection"},
            {"letter": "D", "is_correct": False, "text": "Spinal shock; Loss of sympathetic vasomotor tone"},
            {"letter": "E", "is_correct": False, "text": "Horner syndrome; Carotid artery dissection"}
        ],
        "explanation": "Correct Answer: B. Cushing triad; Severe intracranial hypertension with impending brain herniation.\n\nCushing Triad is a late, ominous physiological response to severely elevated intracranial pressure (ICP):\n1. Hypertension with widened pulse pressure (cerebral ischemia triggers massive sympathetic outflow to maintain cerebral perfusion pressure [CPP = MAP - ICP]).\n2. Bradycardia (carotid baroreceptors sense severe systemic hypertension and trigger vagal parasympathetic reflex slowing of heart rate).\n3. Irregular respirations (brainstem compression disrupts respiratory rhythm generators in the medulla).\nIt signals imminent life-threatening cerebral herniation."
    },
    {
        "q_num": "TBI-04",
        "category": "Traumatic Brain Injuries",
        "stem": "In uncal (transtentorial) herniation, the medial temporal lobe (uncus) herniates downward over the free edge of the tentorium cerebelli. Which cranial nerve is compressed earliest by the herniating uncus, and what is the characteristic clinical finding?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Abducens nerve (CN VI); Inability to abduct the contralateral eye"},
            {"letter": "B", "is_correct": True, "text": "Oculomotor nerve (CN III); Ipsilateral pupillary dilation and unresponsiveness to light ('blown pupil')"},
            {"letter": "C", "is_correct": False, "text": "Trochlear nerve (CN IV); Diplopia on downgaze"},
            {"letter": "D", "is_correct": False, "text": "Facial nerve (CN VII); Ipsilateral complete facial paralysis"},
            {"letter": "E", "is_correct": False, "text": "Trigeminal nerve (CN V); Loss of sensation on the cheek"}
        ],
        "explanation": "Correct Answer: B. Oculomotor nerve (CN III); Ipsilateral pupillary dilation and unresponsiveness to light ('blown pupil').\n\nUncal (transtentorial) herniation sequence:\n1. The herniating medial temporal uncus compresses the ipsilateral CN III against the tentorial edge. Because parasympathetic pupilloconstrictor fibers travel superficially on the outside of CN III, they are compressed first, causing ipsilateral fixed, dilated pupil ('blown pupil').\n2. Progressive compression knocks out somatic motor fibers of CN III ('down-and-out' eye).\n3. Compression of the posterior cerebral artery (PCA) produces contralateral homonymous hemianopia with macular sparing.\n4. Midbrain compression causes coma and secondary Duret flame-shaped hemorrhages."
    },
    {
        "q_num": "TBI-05",
        "category": "Traumatic Brain Injuries",
        "stem": "In severe uncal herniation, downward displacement of the midbrain can push the CONTRALATERAL cerebral peduncle against the opposite tentorial edge, causing ipsilateral hemiparesis (a false localizing motor sign). What is the anatomical term for this indentation in the contralateral cerebral peduncle?",
        "options": [
            {"letter": "A", "is_correct": True, "text": "Kernohan notch (Kernohan phenomenon)"},
            {"letter": "B", "is_correct": False, "text": "Lissauer tract"},
            {"letter": "C", "is_correct": False, "text": "Duret groove"},
            {"letter": "D", "is_correct": False, "text": "Monro fissure"},
            {"letter": "E", "is_correct": False, "text": "Sylvian notch"}
        ],
        "explanation": "Correct Answer: A. Kernohan notch (Kernohan phenomenon).\n\nNormally, a supratentorial mass on the left produces right-sided hemiparesis. However, in Kernohan phenomenon:\n• Massive left uncal herniation shifts the midbrain laterally across the incisura, crushing the CONTRALATERAL (right) cerebral peduncle against the rigid right tentorial notch (creating 'Kernohan notch').\n• Because the corticospinal fibers in the right peduncle cross downstream in the medulla to supply the left side of the body, the patient presents with hemiparesis IPSILATERAL to the mass (left-sided hemiparesis). This is a classic 'false-localizing' sign."
    },
    {
        "q_num": "TBI-06",
        "category": "Traumatic Brain Injuries",
        "stem": "A 19-year-old hockey player sustains a forceful check into the boards. He does not lose consciousness, but reports immediate headache, dizziness, disorientation, and retrograde amnesia for the game. Standard non-contrast head CT is completely normal. What is the fundamental cellular pathophysiology of concussion (mild traumatic brain injury)?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Macroscopic parenchymal shearing and intraparenchymal hematoma formation"},
            {"letter": "B", "is_correct": True, "text": "Functional neurometabolic cascade characterized by ionic flux, indiscriminate glutamate release, and a cellular energy crisis"},
            {"letter": "C", "is_correct": False, "text": "Primary demyelination of the corpus callosum"},
            {"letter": "D", "is_correct": False, "text": "Rupture of the middle meningeal artery"},
            {"letter": "E", "is_correct": False, "text": "Immune-mediated destruction of oligodendrocytes"}
        ],
        "explanation": "Correct Answer: B. Functional neurometabolic cascade characterized by ionic flux, indiscriminate glutamate release, and a cellular energy crisis.\n\nConcussion (mild TBI) is a functional neuronal disturbance rather than a structural lesion (explaining normal routine CT/MRI):\n• Biomechanical shearing stretches axonal membranes, causing unregulated opening of ion channels and massive indiscriminate glutamate release.\n• Widespread ionic flux occurs: efflux of K+ and influx of Ca2+.\n• In an attempt to restore ionic equilibrium, Na+/K+ ATPase pumps work at maximum capacity, accelerating glycolysis (hyperglycolysis).\n• This coincides with impaired cerebral blood flow, resulting in an acute cellular 'energy crisis' (ATP depletion and lactate accumulation)."
    },
    {
        "q_num": "TBI-07",
        "category": "Traumatic Brain Injuries",
        "stem": "A 16-year-old football player sustains a concussion during a game on Friday. Against medical advice, he returns to play the following Tuesday while still experiencing mild headaches and dizziness. During the second game, he suffers a relatively minor tackle to the head. Within 2 minutes, he collapses, loses consciousness, displays rapidly expanding bilateral pupillary dilation, and develops respiratory arrest due to massive brain herniation. What catastrophic syndrome occurred?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Post-concussion syndrome"},
            {"letter": "B", "is_correct": True, "text": "Second impact syndrome"},
            {"letter": "C", "is_correct": False, "text": "Chronic traumatic encephalopathy"},
            {"letter": "D", "is_correct": False, "text": "Subacute sclerosing panencephalitis"},
            {"letter": "E", "is_correct": False, "text": "Fat embolism syndrome"}
        ],
        "explanation": "Correct Answer: B. Second impact syndrome.\n\nSecond Impact Syndrome occurs when a second head impact is sustained before the brain has fully recovered from a prior concussion (while the brain is still in a vulnerable metabolic state):\n• Pathophysiology: Loss of cerebral autoregulation leads to massive, uncontrollable cerebral vascular engorgement, malignant intracranial hypertension, and fatal brain herniation within minutes.\n• Mortality exceeds 50%, emphasizing the strict rule that no athlete should return to play while symptomatic from a concussion."
    },
    {
        "q_num": "TBI-08",
        "category": "Traumatic Brain Injuries",
        "stem": "An autopsy performed on a 48-year-old former professional NFL player who suffered from severe depression, memory loss, emotional instability, and dementia reveals prominent cerebral cortical atrophy, cavum septum pellucidum, and extensive perivascular neurofibrillary tangles. Immunohistochemistry demonstrates patchy deposition of hyperphosphorylated tau in neurons and astrocytes concentrated at the depths of cortical sulci. What is the neuropathological diagnosis?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Alzheimer disease"},
            {"letter": "B", "is_correct": True, "text": "Chronic traumatic encephalopathy (CTE)"},
            {"letter": "C", "is_correct": False, "text": "Frontotemporal lobar degeneration (Pick disease)"},
            {"letter": "D", "is_correct": False, "text": "Creutzfeldt-Jakob disease"},
            {"letter": "E", "is_correct": False, "text": "Progressive supranuclear palsy"}
        ],
        "explanation": "Correct Answer: B. Chronic traumatic encephalopathy (CTE).\n\nChronic Traumatic Encephalopathy (CTE) is a progressive neurodegenerative tauopathy triggered by repetitive head impacts (subconcussive blows or concussions in boxers, football players, combat veterans):\n• Diagnostic pathognomonic feature: Perivascular accumulation of hyperphosphorylated tau (p-tau) neurofibrillary tangles in neurons and astrocytes located preferentially at the depths of cerebral sulci (unlike Alzheimer disease, which begins in the entorhinal cortex/hippocampus and features diffuse beta-amyloid plaques)."
    },
    {
        "q_num": "TBI-09",
        "category": "Traumatic Brain Injuries",
        "stem": "A 25-year-old man presents with head trauma following an assault. Examination reveals ecchymosis over the mastoid process behind the ear (Battle sign), bilateral periorbital ecchymoses without local eye trauma ('raccoon eyes'), hemotympanum on otoscopy, and clear fluid dripping from his nose. What type of skull fracture has occurred?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Linear calvarial vault fracture"},
            {"letter": "B", "is_correct": True, "text": "Basilar skull fracture"},
            {"letter": "C", "is_correct": False, "text": "Depressed frontal bone fracture"},
            {"letter": "D", "is_correct": False, "text": "Zygomaticomaxillary complex fracture"},
            {"letter": "E", "is_correct": False, "text": "Mandibular symphysis fracture"}
        ],
        "explanation": "Correct Answer: B. Basilar skull fracture.\n\nBasilar skull fracture (fracture involving the floor of the anterior, middle, or posterior cranial fossa):\n• Classic clinical signs:\n  1. Battle sign: Ecchymosis over the mastoid process (indicates temporal/petrous bone fracture).\n  2. Raccoon eyes: Bilateral periorbital ecchymosis (indicates anterior cranial fossa fracture).\n  3. CSF rhinorrhea or otorrhea (tearing of the adherent dura mater and arachnoid).\n  4. Hemotympanum: Blood behind the tympanic membrane.\n• Nasogastric tubes are strictly contraindicated (can enter the intracranial cavity through a fractured cribriform plate)."
    },
    {
        "q_num": "TBI-10",
        "category": "Traumatic Brain Injuries",
        "stem": "A patient with suspected basilar skull fracture has persistent clear drainage from the right nostril. To definitively differentiate cerebrospinal fluid (CSF) from normal nasal mucus, laboratory analysis of the fluid should test for the presence of which highly specific biomarker?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Alkaline phosphatase"},
            {"letter": "B", "is_correct": True, "text": "Beta-2 transferrin (asialotransferrin)"},
            {"letter": "C", "is_correct": False, "text": "Creatine kinase-MB"},
            {"letter": "D", "is_correct": False, "text": "Alpha-1 antitrypsin"},
            {"letter": "E", "is_correct": False, "text": "Myoglobin"}
        ],
        "explanation": "Correct Answer: B. Beta-2 transferrin (asialotransferrin).\n\nBeta-2 transferrin (tau transferrin) is a desialylated isoform of transferrin produced exclusively within the central nervous system through neuraminidase activity in the brain. It is found uniquely in cerebrospinal fluid, perilymph, and aqueous humor, and is completely ABSENT from tears, nasal mucus, saliva, or blood. Testing for beta-2 transferrin via immunofixation electrophoresis is the gold standard for diagnosing CSF rhinorrhea or otorrhea."
    },
    {
        "q_num": "TBI-11",
        "category": "Traumatic Brain Injuries",
        "stem": "In subfalcine (cingulate) herniation, a unilateral hemispheric mass displaces the cingulate gyrus beneath the rigid free lower edge of the falx cerebri. Compression of which cerebral artery during subfalcine herniation leads to ischemic infarction of the leg representation in the primary motor and sensory cortex?",
        "options": [
            {"letter": "A", "is_correct": True, "text": "Anterior cerebral artery (ACA)"},
            {"letter": "B", "is_correct": False, "text": "Middle cerebral artery (MCA)"},
            {"letter": "C", "is_correct": False, "text": "Posterior cerebral artery (PCA)"},
            {"letter": "D", "is_correct": False, "text": "Superior cerebellar artery (SCA)"},
            {"letter": "E", "is_correct": False, "text": "Basilar artery"}
        ],
        "explanation": "Correct Answer: A. Anterior cerebral artery (ACA).\n\nSubfalcine (cingulate) herniation occurs when a unilateral mass shifts the cingulate gyrus across the midline under the rigid falx cerebri. As the tissue shifts, it compresses the ipsilateral (or both) Anterior Cerebral Artery (ACA) against the falx, resulting in frontal lobe ischemia and infarction of the paracentral lobule, clinically manifesting as contralateral lower extremity weakness and abulia."
    },
    {
        "q_num": "TBI-12",
        "category": "Traumatic Brain Injuries",
        "stem": "Which brain herniation syndrome involves downward herniation of the cerebellar tonsils through the foramen magnum, resulting in direct compression of the medulla oblongata, respiratory arrest, cardiac collapse, and rapid death?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Subfalcine herniation"},
            {"letter": "B", "is_correct": False, "text": "Uncal herniation"},
            {"letter": "C", "is_correct": False, "text": "Central transtentorial herniation"},
            {"letter": "D", "is_correct": True, "text": "Tonsillar herniation"},
            {"letter": "E", "is_correct": False, "text": "Transcalvarial herniation"}
        ],
        "explanation": "Correct Answer: D. Tonsillar herniation.\n\nTonsillar herniation involves the downward displacement of the cerebellar tonsils through the foramen magnum into the upper cervical spinal canal. This directly compresses the vital cardiorespiratory centers in the medulla oblongata, leading to abrupt apnea, bradycardia, hemodynamic collapse, and immediate death."
    },
    {
        "q_num": "TBI-13",
        "category": "Traumatic Brain Injuries",
        "stem": "In patients with acute severe traumatic brain injury and intracranial hypertension, Cerebral Perfusion Pressure (CPP) must be maintained above 60 mm Hg. What is the mathematical definition of Cerebral Perfusion Pressure?",
        "options": [
            {"letter": "A", "is_correct": True, "text": "CPP = Mean Arterial Pressure (MAP) − Intracranial Pressure (ICP)"},
            {"letter": "B", "is_correct": False, "text": "CPP = Systolic Blood Pressure + ICP"},
            {"letter": "C", "is_correct": False, "text": "CPP = Diastolic Blood Pressure − Central Venous Pressure"},
            {"letter": "D", "is_correct": False, "text": "CPP = MAP / ICP"},
            {"letter": "E", "is_correct": False, "text": "CPP = ICP − MAP"}
        ],
        "explanation": "Correct Answer: A. CPP = Mean Arterial Pressure (MAP) − Intracranial Pressure (ICP).\n\nCerebral Perfusion Pressure (CPP) is the net pressure gradient driving cerebral blood flow to the brain:\nCPP = MAP - ICP (or CVP, whichever is higher).\n• Under normal conditions, ICP is ≤ 15 mm Hg and CPP is 70-90 mm Hg.\n• In severe TBI, if ICP rises to 35 mm Hg and MAP is 85 mm Hg, CPP falls to 50 mm Hg (below the critical threshold of 60 mm Hg), causing secondary ischemic brain injury. Guidelines recommend maintaining CPP between 60 and 70 mm Hg."
    },
    {
        "q_num": "TBI-14",
        "category": "Traumatic Brain Injuries",
        "stem": "An intubated patient with severe traumatic brain injury develops an acute spike in intracranial pressure to 35 mm Hg. The physician temporarily hyperventilates the patient to an end-tidal PaCO2 of 30 mm Hg. By what physiological mechanism does acute hypercapnia versus hypocapnia alter intracranial pressure?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Hypocapnia causes cerebral arteriolar vasodilation; hypercapnia causes vasoconstriction"},
            {"letter": "B", "is_correct": True, "text": "Hypocapnia causes cerebral arteriolar vasoconstriction (decreasing cerebral blood volume); hypercapnia causes vasodilation"},
            {"letter": "C", "is_correct": False, "text": "Hypocapnia increases CSF secretion by the choroid plexus"},
            {"letter": "D", "is_correct": False, "text": "Carbon dioxide has no effect on cerebral microvasculature"},
            {"letter": "E", "is_correct": False, "text": "Hypocapnia causes systemic venous pooling in the extremities"}
        ],
        "explanation": "Correct Answer: B. Hypocapnia causes cerebral arteriolar vasoconstriction (decreasing cerebral blood volume); hypercapnia causes vasodilation.\n\nCerebral blood flow (CBF) is exquisitely sensitive to arterial PaCO2:\n• Rising PaCO2 (hypercapnia) drops perivascular pH, causing profound cerebral arteriolar vasodilation, increasing cerebral blood volume and dramatically raising ICP.\n• Lowering PaCO2 (hypocapnia via hyperventilation, PaCO2 30-35 mm Hg) induces rapid cerebral arteriolar vasoconstriction, reducing intracranial blood volume and rapidly lowering ICP. (Excessive hyperventilation to PaCO2 < 30 mm Hg is avoided because severe vasoconstriction causes secondary brain ischemia)."
    },
    {
        "q_num": "TBI-15",
        "category": "Traumatic Brain Injuries",
        "stem": "Which osmotic agent is an inert polysaccharide hexitol that is administered intravenously to treat acute cerebral edema by creating an intravascular osmotic gradient that draws free water from the brain parenchyma into the vascular compartment across an intact blood-brain barrier?",
        "options": [
            {"letter": "A", "is_correct": True, "text": "Mannitol"},
            {"letter": "B", "is_correct": False, "text": "Lactulose"},
            {"letter": "C", "is_correct": False, "text": "Dextrose 50%"},
            {"letter": "D", "is_correct": False, "text": "Albumin 5%"},
            {"letter": "E", "is_correct": False, "text": "Heparin"}
        ],
        "explanation": "Correct Answer: A. Mannitol.\n\nMannitol is an osmotic diuretic (administered as 20% solution at 0.5-1.0 g/kg) used to reduce elevated ICP:\n• Mechanism: Mannitol does not cross the intact blood-brain barrier. It creates an osmotic gradient that draws water out of swollen parenchymal brain cells into the intravascular space, shrinking brain volume.\n• Secondary rheological effect: Decreases blood viscosity, promoting microvascular cerebral perfusion.\n• Monitor: Serum osmolality (hold if >320 mOsm/kg) and renal function."
    },
    {
        "q_num": "TBI-16",
        "category": "Traumatic Brain Injuries",
        "stem": "In addition to mannitol, hypertonic saline (3% or 23.4% NaCl) is widely used for acute intracranial pressure crises. What is the major advantage of hypertonic saline over mannitol in a hypotensive trauma patient?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Hypertonic saline induces profound diuresis to lower blood pressure"},
            {"letter": "B", "is_correct": True, "text": "Hypertonic saline expands intravascular volume and supports blood pressure without causing osmotic diuresis"},
            {"letter": "C", "is_correct": False, "text": "Hypertonic saline easily crosses the blood-brain barrier"},
            {"letter": "D", "is_correct": False, "text": "Hypertonic saline is metabolized in the liver into glucose"},
            {"letter": "E", "is_correct": False, "text": "Hypertonic saline directly inhibits NMDA receptors"}
        ],
        "explanation": "Correct Answer: B. Hypertonic saline expands intravascular volume and supports blood pressure without causing osmotic diuresis.\n\nHypertonic Saline (HTS) vs Mannitol in TBI:\n• While mannitol causes significant osmotic diuresis that can precipitate hypovolemia and hypotension (which reduces cerebral perfusion pressure), hypertonic saline draws water into the intravascular space to expand circulating plasma volume, supporting mean arterial pressure (MAP) while simultaneously reducing cerebral edema and lowering ICP. It is especially preferred in multitrauma patients with hypovolemic shock."
    },
    {
        "q_num": "TBI-17",
        "category": "Traumatic Brain Injuries",
        "stem": "During rapid deceleration in a motor vehicle collision, the moving head strikes the steering wheel. The brain sustains a contusion at the site of impact, as well as a second contusion directly opposite the impact site as the brain rebounds within the skull. What are the terms for the impact injury and the opposite rebound injury, respectively?",
        "options": [
            {"letter": "A", "is_correct": True, "text": "Coup injury and Contrecoup injury"},
            {"letter": "B", "is_correct": False, "text": "Contrecoup injury and Coup injury"},
            {"letter": "C", "is_correct": False, "text": "Linear injury and Depressed injury"},
            {"letter": "D", "is_correct": False, "text": "Primary injury and Secondary injury"},
            {"letter": "E", "is_correct": False, "text": "Axonal shear and Cortical bleed"}
        ],
        "explanation": "Correct Answer: A. Coup injury and Contrecoup injury.\n\nCerebral contusions (bruising of the brain surface):\n• Coup injury: Occurs directly beneath the point of skull impact as the inward-bending calvarium compresses the underlying cortical crests.\n• Contrecoup injury: Occurs on the brain surface directly opposite the site of impact as the brain decelerates and rebounds violently against the opposing bony inner surface of the skull (often against the irregular sphenoid wings or cribriform plate)."
    },
    {
        "q_num": "TBI-18",
        "category": "Traumatic Brain Injuries",
        "stem": "Following severe closed head trauma, secondary brain injury develops over hours to days. Which of the following systemic secondary insults is the most potent contributor to secondary neuronal death and must be rigorously prevented in neurotrauma resuscitation?",
        "options": [
            {"letter": "A", "is_correct": True, "text": "Hypotension (Systolic BP < 90 mm Hg) and Hypoxemia (PaO2 < 60 mm Hg)"},
            {"letter": "B", "is_correct": False, "text": "Mild hypernatremia"},
            {"letter": "C", "is_correct": False, "text": "Slightly elevated hematocrit"},
            {"letter": "D", "is_correct": False, "text": "Transient hyperthermia below 37.5°C"},
            {"letter": "E", "is_correct": False, "text": "Normal blood glucose levels"}
        ],
        "explanation": "Correct Answer: A. Hypotension (Systolic BP < 90 mm Hg) and Hypoxemia (PaO2 < 60 mm Hg).\n\nPrimary TBI occurs at the moment of impact and cannot be reversed. Resuscitation focuses entirely on preventing secondary brain injury:\n• A single episode of hypotension (SBP < 90 mm Hg) in severe TBI doubles mortality.\n• Hypoxemia (PaO2 < 60 mm Hg or SpO2 < 90%) significantly worsens neurological outcomes.\n• When combined, hypotension and hypoxemia result in a greater than 75% mortality rate, making airway stabilization and hemodynamic volume resuscitation the highest clinical priorities."
    },
    {
        "q_num": "TBI-19",
        "category": "Traumatic Brain Injuries",
        "stem": "Which of the following monitoring devices is considered the gold standard for continuous intracranial pressure (ICP) measurement because it allows both accurate pressure monitoring and therapeutic drainage of cerebrospinal fluid?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Subdural bolt"},
            {"letter": "B", "is_correct": True, "text": "Intraventricular catheter / External ventricular drain (EVD)"},
            {"letter": "C", "is_correct": False, "text": "Intraparenchymal fiberoptic probe"},
            {"letter": "D", "is_correct": False, "text": "Epidural transducer"},
            {"letter": "E", "is_correct": False, "text": "Transcranial Doppler sonography alone"}
        ],
        "explanation": "Correct Answer: B. Intraventricular catheter / External ventricular drain (EVD).\n\nAn external ventricular drain (EVD / ventriculostomy) is the gold standard for ICP monitoring because it is inserted directly into the lateral ventricle, providing highly accurate global intracranial pressure readings while uniquely offering therapeutic capability: draining CSF to immediately reduce elevated ICP."
    },
    {
        "q_num": "TBI-20",
        "category": "Traumatic Brain Injuries",
        "stem": "Secondary flame-shaped, linear hemorrhages occurring in the midline of the midbrain and upper pons in patients with rapidly progressing descending central or uncal transtentorial herniation are known eponymously as:",
        "options": [
            {"letter": "A", "is_correct": True, "text": "Duret hemorrhages"},
            {"letter": "B", "is_correct": False, "text": "Charcot-Bouchard hemorrhages"},
            {"letter": "C", "is_correct": False, "text": "Kernohan hemorrhages"},
            {"letter": "D", "is_correct": False, "text": "Spiller hemorrhages"},
            {"letter": "E", "is_correct": False, "text": "Gower hemorrhages"}
        ],
        "explanation": "Correct Answer: A. Duret hemorrhages.\n\nDuret hemorrhages are secondary brainstem hemorrhages (linear or flame-shaped) located in the paramedian midbrain and upper pons. As descending transtentorial herniation shifts the brainstem caudally, the basilar artery (fixed to the skull base) remains tethered, stretching and tearing small penetrating paramedian branches of the basilar artery, leading to fatal brainstem necrosis."
    },

    # =========================================================================
    # 16. MENINGITIS (20 Questions: Q61 - Q80)
    # =========================================================================
    {
        "q_num": "MEN-01",
        "category": "Meningitis",
        "stem": "A 22-year-old college student is brought to the emergency department with a 12-hour history of high fever, severe headache, confusion, and vomiting. Physical examination shows temperature 39.4°C, heart rate 124 bpm, blood pressure 85/55 mm Hg, marked nuchal rigidity, and petechial purpuric skin lesions on his trunk and lower extremities. What is the most likely causative organism, and what is its Gram-stain morphology?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Streptococcus pneumoniae; Gram-positive lancet-shaped diplococci"},
            {"letter": "B", "is_correct": True, "text": "Neisseria meningitidis; Gram-negative kidney bean-shaped diplococci"},
            {"letter": "C", "is_correct": False, "text": "Listeria monocytogenes; Gram-positive tumbling bacilli"},
            {"letter": "D", "is_correct": False, "text": "Haemophilus influenzae; Gram-negative pleomorphic coccobacilli"},
            {"letter": "E", "is_correct": False, "text": "Cryptococcus neoformans; Budding encapsulated yeast"}
        ],
        "explanation": "Correct Answer: B. Neisseria meningitidis; Gram-negative kidney bean-shaped diplococci.\n\nNeisseria meningitidis (meningococcus):\n• Demographics: Common cause of epidemic bacterial meningitis in young adults living in crowded quarters (dorms, military barracks).\n• Hallmark: Petechial or purpuric rash (due to meningococcemia and lipooligosaccharide / LOS endotoxin-mediated endothelial injury and DIC).\n• Morphology: Gram-negative, kidney-bean-shaped diplococci found intracellularly within neutrophils.\n• Complication: Waterhouse-Friderichsen syndrome (bilateral adrenal hemorrhage, acute adrenal failure, and circulatory collapse)."
    },
    {
        "q_num": "MEN-02",
        "category": "Meningitis",
        "stem": "A 6-day-old neonate presents with lethargy, poor feeding, hypothermia (35.6°C), and a bulging anterior fontanelle. Cerebrospinal fluid culture grows Gram-positive, beta-hemolytic, bacitracin-resistant cocci in chains that produce a positive CAMP test (augmented hemolysis with Staphylococcus aureus). Which organism is the most common cause of neonatal bacterial meningitis?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Streptococcus pneumoniae"},
            {"letter": "B", "is_correct": True, "text": "Streptococcus agalactiae (Group B Streptococcus / GBS)"},
            {"letter": "C", "is_correct": False, "text": "Escherichia coli (K1 capsule)"},
            {"letter": "D", "is_correct": False, "text": "Listeria monocytogenes"},
            {"letter": "E", "is_correct": False, "text": "Enterococcus faecalis"}
        ],
        "explanation": "Correct Answer: B. Streptococcus agalactiae (Group B Streptococcus / GBS).\n\nStreptococcus agalactiae (Group B Strep / GBS) is the #1 cause of neonatal meningitis and sepsis (<1 month of age), followed by Escherichia coli (K1 capsular antigen) and Listeria monocytogenes:\n• Microbiological characteristics: Gram-positive cocci in chains, narrow zone of beta-hemolysis, bacitracin resistant, and CAMP test positive (CAMP factor enlarges the area of hemolysis formed by S. aureus beta-hemolysin into an arrow-head shape).\n• Prevention: Universal maternal screening at 36-37 weeks with intrapartum IV penicillin/ampicillin prophylaxis."
    },
    {
        "q_num": "MEN-03",
        "category": "Meningitis",
        "stem": "A 68-year-old renal transplant recipient on immunosuppressive therapy presents with fever, headache, and neck stiffness. Gram stain of the CSF reveals Gram-positive rods with tumbling motility at room temperature (22°C) and cold enrichment growth. Which empiric antimicrobial agent MUST be added to the standard vancomycin and ceftriaxone regimen to cover this pathogen in patients >50 years or immunocompromised?",
        "options": [
            {"letter": "A", "is_correct": True, "text": "Ampicillin"},
            {"letter": "B", "is_correct": False, "text": "Gentamicin alone"},
            {"letter": "C", "is_correct": False, "text": "Metronidazole"},
            {"letter": "D", "is_correct": False, "text": "Azithromycin"},
            {"letter": "E", "is_correct": False, "text": "Ciprofloxacin"}
        ],
        "explanation": "Correct Answer: A. Ampicillin.\n\nThis patient has Listeria monocytogenes meningitis:\n• Demographics: Neonates, adults >50 years, and immunocompromised patients.\n• Microbiology: Facultative intracellular Gram-positive rod; exhibits 'tumbling motility' on wet mount at 22-25°C and can grow at refrigerator temperatures ('cold enrichment').\n• Crucial therapeutic pearl: Listeria is intrinsically RESISTANT to all cephalosporins (including 3rd-generation cephalosporins like ceftriaxone) due to low affinity for penicillin-binding proteins. Therefore, AMPICILLIN must be added to empiric vancomycin + ceftriaxone in patients >50 years, neonates, or immunocompromised individuals."
    },
    {
        "q_num": "MEN-04",
        "category": "Meningitis",
        "stem": "Lumbar puncture analysis in a 45-year-old man with fever and nuchal rigidity yields the following CSF results:\n• Opening pressure: 310 mm H2O (normal 70–180)\n• Leukocytes: 4,500/mm³ with 92% neutrophils\n• Glucose: 18 mg/dL (serum glucose 110 mg/dL; ratio 0.16)\n• Protein: 320 mg/dL (normal 15–45)\nWhich type of meningitis is unequivocally diagnosed by this CSF profile?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Viral (aseptic) meningitis"},
            {"letter": "B", "is_correct": True, "text": "Acute bacterial meningitis"},
            {"letter": "C", "is_correct": False, "text": "Fungal meningitis"},
            {"letter": "D", "is_correct": False, "text": "Tuberculous meningitis"},
            {"letter": "E", "is_correct": False, "text": "Multiple sclerosis flare"}
        ],
        "explanation": "Correct Answer: B. Acute bacterial meningitis.\n\nCSF Profiles in Meningitis:\n• Acute Bacterial: Opening pressure markedly ELEVATED (>200-300 mm H2O); WBC markedly ELEVATED (>1,000-10,000/μL) with Neutrophil predominance (>80%); Protein markedly ELEVATED (>100-500 mg/dL); Glucose markedly DECREASED (<40 mg/dL or CSF:serum ratio < 0.4).\n• Viral (Aseptic): Normal or mildly elevated opening pressure; WBC 10-500/μL with Lymphocyte predominance; Protein mildly elevated (50-100 mg/dL); Glucose NORMAL (>60% of serum).\n• Fungal/TB: Elevated opening pressure; WBC 100-500/μL (lymphocytic); Protein markedly elevated; Glucose DECREASED."
    },
    {
        "q_num": "MEN-05",
        "category": "Meningitis",
        "stem": "An adult with suspected acute bacterial meningitis requires empiric antibiotic therapy. Randomized trials have demonstrated that administering intravenous dexamethasone either before or with the first dose of antibiotics significantly reduces hearing loss and neurological sequelae, particularly when the infection is caused by which pathogen?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Neisseria meningitidis"},
            {"letter": "B", "is_correct": True, "text": "Streptococcus pneumoniae"},
            {"letter": "C", "is_correct": False, "text": "Listeria monocytogenes"},
            {"letter": "D", "is_correct": False, "text": "Haemophilus influenzae in adults"},
            {"letter": "E", "is_correct": False, "text": "Escherichia coli"}
        ],
        "explanation": "Correct Answer: B. Streptococcus pneumoniae.\n\nIn acute bacterial meningitis, antibiotic-induced bacterial lysis releases cell wall fragments (peptidoglycan and teichoic acid), triggering a massive inflammatory cytokine cascade (TNF-alpha and IL-1beta) in the subarachnoid space that worsens cerebral edema and sensorineural hearing loss. Administration of IV Dexamethasone (10 mg) before or simultaneously with the first dose of antibiotics blunts this inflammatory cascade, significantly reducing mortality and sensorineural hearing loss in adults with Streptococcus pneumoniae meningitis."
    },
    {
        "q_num": "MEN-06",
        "category": "Meningitis",
        "stem": "A 40-year-old HIV-positive patient (CD4 count 42 cells/mm³) presents with insidious headache, mild fever, and malaise. Lumbar puncture reveals elevated opening pressure (280 mm H2O). India ink staining of the CSF reveals round budding yeast cells surrounded by a wide, clear halo. What is the organism, and what is its capsule composed of?",
        "options": [
            {"letter": "A", "is_correct": True, "text": "Cryptococcus neoformans; Glucuronoxylomannan polysaccharide capsule"},
            {"letter": "B", "is_correct": False, "text": "Candida albicans; Beta-glucan capsule"},
            {"letter": "C", "is_correct": False, "text": "Histoplasma capsulatum; Glycoprotein capsule"},
            {"letter": "D", "is_correct": False, "text": "Coccidioides immitis; Spherule wall"},
            {"letter": "E", "is_correct": False, "text": "Blastomyces dermatitidis; Broad-based bud wall"}
        ],
        "explanation": "Correct Answer: A. Cryptococcus neoformans; Glucuronoxylomannan polysaccharide capsule.\n\nCryptococcus neoformans (encapsulated opportunistic environmental yeast found in pigeon droppings):\n• Clinical presentation: Subacute meningoencephalitis in immunocompromised patients (HIV CD4 < 100/μL).\n• Microbiology: Thick antiphagocytic polysaccharide capsule composed of Glucuronoxylomannan (GXM). \n• Diagnostics: India ink staining repels the capsule, producing a clear halo around the yeast; Cryptococcal Antigen (CrAg) latex agglutination or lateral flow assay has >95% sensitivity.\n• Treatment: Induction with Amphotericin B + Flucytosine, followed by maintenance Fluconazole."
    },
    {
        "q_num": "MEN-07",
        "category": "Meningitis",
        "stem": "Which physical examination sign is positive when passive flexion of the patient's neck causes involuntary, reflexive flexion of the hips and knees due to meningeal irritation?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Kernig sign"},
            {"letter": "B", "is_correct": True, "text": "Brudzinski sign"},
            {"letter": "C", "is_correct": False, "text": "Babinski sign"},
            {"letter": "D", "is_correct": False, "text": "Lhermitte sign"},
            {"letter": "E", "is_correct": False, "text": "Chvostek sign"}
        ],
        "explanation": "Correct Answer: B. Brudzinski sign.\n\nSigns of meningeal irritation:\n• Brudzinski sign: Involuntary flexion of the hips and knees when the examiner passively flexes the patient's neck in the supine position.\n• Kernig sign: Resistance or pain in the hamstrings/lumbar spine upon passive extension of the knee when the patient's hip is flexed at 90 degrees."
    },
    {
        "q_num": "MEN-08",
        "category": "Meningitis",
        "stem": "A 20-year-old college student is diagnosed with acute meningococcal meningitis. Public health authorities are notified to identify close contacts (roommates, dorm-mates, intimate contacts). Which of the following antimicrobial regimens is recommended as first-line chemoprophylaxis for close contacts of patients with Neisseria meningitidis infection?",
        "options": [
            {"letter": "A", "is_correct": True, "text": "Rifampin (or single-dose Ciprofloxacin or Ceftriaxone)"},
            {"letter": "B", "is_correct": False, "text": "Amoxicillin for 10 days"},
            {"letter": "C", "is_correct": False, "text": "Vancomycin intravenously"},
            {"letter": "D", "is_correct": False, "text": "Doxycycline single dose"},
            {"letter": "E", "is_correct": False, "text": "Trimethoprim-sulfamethoxazole"}
        ],
        "explanation": "Correct Answer: A. Rifampin (or single-dose Ciprofloxacin or Ceftriaxone).\n\nChemoprophylaxis for close contacts of Neisseria meningitidis:\n• Indication: Household members, roommates, daycare contacts, or anyone directly exposed to oral secretions (intubation, resuscitation) within 7 days prior to onset.\n• Regimens:\n  1. Rifampin: 600 mg PO BID for 2 days (warn patient of orange discoloration of tears/urine).\n  2. Ciprofloxacin: Single 500 mg PO dose (in adults).\n  3. Ceftriaxone: Single 250 mg IM dose (preferred in pregnancy)."
    },
    {
        "q_num": "MEN-09",
        "category": "Meningitis",
        "stem": "What is the most common viral etiology of acute aseptic meningitis in children and adults, accounting for over 85% of cases with identifiable viral causes, typically occurring in late summer and autumn?",
        "options": [
            {"letter": "A", "is_correct": True, "text": "Enteroviruses (Coxsackievirus, Echovirus, Poliovirus)"},
            {"letter": "B", "is_correct": False, "text": "Herpes simplex virus type 1 (HSV-1)"},
            {"letter": "C", "is_correct": False, "text": "Varicella-zoster virus (VZV)"},
            {"letter": "D", "is_correct": False, "text": "Epstein-Barr virus (EBV)"},
            {"letter": "E", "is_correct": False, "text": "Rabies virus"}
        ],
        "explanation": "Correct Answer: A. Enteroviruses (Coxsackievirus, Echovirus, Poliovirus).\n\nEnteroviruses (positive-sense, single-stranded, non-enveloped RNA picornaviruses—primarily Coxsackievirus B and Echoviruses) are responsible for >85-90% of all cases of viral (aseptic) meningitis. Transmission is fecal-oral, with peak incidence in summer and fall. CSF analysis shows a lymphocytic pleocytosis, normal glucose, and negative bacterial cultures."
    },
    {
        "q_num": "MEN-10",
        "category": "Meningitis",
        "stem": "A 32-year-old man presents with acute-onset high fever, temporal lobe seizures, olfactory hallucinations, and bizarre behavioral changes. Brain MRI demonstrates asymmetric hyperintensity on T2/FLAIR localized to the inferior and medial temporal lobes. What is the causative pathogen, and what is the urgent antiviral therapy?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Enterovirus; Pleconaril"},
            {"letter": "B", "is_correct": True, "text": "Herpes simplex virus type 1 (HSV-1); Intravenous acyclovir"},
            {"letter": "C", "is_correct": False, "text": "Cytomegalovirus; Ganciclovir"},
            {"letter": "D", "is_correct": False, "text": "JC virus; Highly active antiretroviral therapy"},
            {"letter": "E", "is_correct": False, "text": "Rabies virus; Rabies immunoglobulin"}
        ],
        "explanation": "Correct Answer: B. Herpes simplex virus type 1 (HSV-1); Intravenous acyclovir.\n\nHerpes Simplex Encephalitis (HSE):\n• Etiology: HSV-1 (>90% of cases in adults, entering the brain via retrograde olfactory or trigeminal nerve transport).\n• Hallmark features: Hemorrhagic necrotizing encephalitis localized to the temporal and inferior frontal lobes, presenting with fever, focal temporal seizures, aphasia, and olfactory hallucinations.\n• Diagnostics: CSF HSV PCR is the test of choice.\n• Treatment: Immediate empiric IV Acyclovir (inhibits viral DNA polymerase following phosphorylation by viral thymidine kinase); delaying acyclovir dramatically increases mortality."
    },
    {
        "q_num": "MEN-11",
        "category": "Meningitis",
        "stem": "Which virulence factor possessed by Streptococcus pneumoniae is a capsule composed of polysaccharides that inhibits phagocytosis by preventing complement factor C3b opsonization, serving as the basis for the PPSV23 and PCV20 vaccines?",
        "options": [
            {"letter": "A", "is_correct": True, "text": "Polysaccharide capsule"},
            {"letter": "B", "is_correct": False, "text": "Pneumolysin"},
            {"letter": "C", "is_correct": False, "text": "IgA protease"},
            {"letter": "D", "is_correct": False, "text": "Lipoteichoic acid"},
            {"letter": "E", "is_correct": False, "text": "Hyaluronidase"}
        ],
        "explanation": "Correct Answer: A. Polysaccharide capsule.\n\nStreptococcus pneumoniae possesses several virulence factors:\n• Polysaccharide capsule: The most important virulence factor (>100 serotypes); physically shields the cell wall from opsonization by C3b, preventing neutrophil phagocytosis. Asplenic patients (sickle cell disease, splenectomy) lack splenic macrophage clearance of encapsulated bacteria and are at high risk of fatal pneumococcal sepsis/meningitis.\n• IgA protease: Cleaves secretory IgA, facilitating mucosal colonization.\n• Pneumolysin: Cytotoxin that forms pores in host membranes."
    },
    {
        "q_num": "MEN-12",
        "category": "Meningitis",
        "stem": "Prior to performing a lumbar puncture on an adult with suspected bacterial meningitis, which of the following clinical criteria warrants an immediate non-contrast head CT to rule out intracranial mass effect and prevent brain herniation?",
        "options": [
            {"letter": "A", "is_correct": True, "text": "Focal neurological deficit, altered consciousness, new-onset seizure, papilledema, or immunocompromised state"},
            {"letter": "B", "is_correct": False, "text": "Fever > 38.5°C alone"},
            {"letter": "C", "is_correct": False, "text": "Presence of nuchal rigidity alone"},
            {"letter": "D", "is_correct": False, "text": "Photophobia and headache"},
            {"letter": "E", "is_correct": False, "text": "Elevated peripheral white blood cell count"}
        ],
        "explanation": "Correct Answer: A. Focal neurological deficit, altered consciousness, new-onset seizure, papilledema, or immunocompromised state.\n\nIndications for head CT before LP in suspected meningitis ('FAILS'):\n• F: Focal neurological deficit (e.g., hemiparesis, cranial nerve palsy)\n• A: Altered mental status / consciousness (GCS < 15)\n• I: Immunocompromised state (HIV, immunosuppressants, transplant)\n• L: Lesion suspected / Papilledema (signs of elevated ICP)\n• S: Seizure within past week.\nIn patients meeting these criteria, blood cultures and empiric antibiotics + dexamethasone must be administered IMMEDIATELY before taking the patient to the CT scanner."
    },
    {
        "q_num": "MEN-13",
        "category": "Meningitis",
        "stem": "A 4-year-old child presents with tuberculous meningitis. Tuberculous meningitis characteristically causes a dense, gelatinous, inflammatory exudate that preferentially encases which anatomical region of the brain, leading to multiple cranial nerve palsies (CN III, IV, VI, VII) and communicating hydrocephalus?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Convexity of the parietal lobes"},
            {"letter": "B", "is_correct": True, "text": "Basal cisterns and base of the brain"},
            {"letter": "C", "is_correct": False, "text": "Spinal cord conus medullaris"},
            {"letter": "D", "is_correct": False, "text": "Occipital pole"},
            {"letter": "E", "is_correct": False, "text": "Corpus callosum"}
        ],
        "explanation": "Correct Answer: B. Basal cisterns and base of the brain.\n\nTuberculous (TB) meningitis (caused by Mycobacterium tuberculosis) typically begins with the rupture of a subependymal Rich focus into the subarachnoid space. It characteristically forms a thick, gelatinous, granulomatous exudate that preferentially accumulates in the Basal Cisterns (interpeduncular, chiasmatic, and prepontine cisterns). This results in:\n1. Entrapment and paralysis of cranial nerves coursing through the skull base (CN III, VI, VII).\n2. Endarteritis obliterans of Circle of Willis vessels (causing stroke).\n3. Obstructed arachnoid villi causing communicating hydrocephalus."
    },
    {
        "q_num": "MEN-14",
        "category": "Meningitis",
        "stem": "Which of the following encapsulated Gram-negative coccobacilli was historically a leading cause of bacterial meningitis, epiglottitis, and septic arthritis in children between 6 months and 2 years of age, but has seen its incidence drop by >99% following the introduction of a conjugate vaccine containing its polyribosylribitol phosphate (PRP) capsular antigen?",
        "options": [
            {"letter": "A", "is_correct": True, "text": "Haemophilus influenzae type b (Hib)"},
            {"letter": "B", "is_correct": False, "text": "Bordetella pertussis"},
            {"letter": "C", "is_correct": False, "text": "Klebsiella pneumoniae"},
            {"letter": "D", "is_correct": False, "text": "Pseudomonas aeruginosa"},
            {"letter": "E", "is_correct": False, "text": "Acinetobacter baumannii"}
        ],
        "explanation": "Correct Answer: A. Haemophilus influenzae type b (Hib).\n\nHaemophilus influenzae type b (Hib):\n• Microbiology: Small, pleomorphic Gram-negative coccobacillus requiring Factor X (hemin) and Factor V (NAD) to grow on chocolate agar.\n• Capsule: Composed of Polyribosylribitol Phosphate (PRP).\n• History: Prior to the Hib conjugate vaccine (PRP conjugated to diphtheria toxoid or tetanus toxoid to elicit T-cell dependent B-cell memory), it was the leading cause of pediatric meningitis. Sensorineural deafness was the most common long-term sequela."
    },
    {
        "q_num": "MEN-15",
        "category": "Meningitis",
        "stem": "A 16-year-old girl in the intensive care unit with fulminant meningococcal meningitis develops refractory hypotension, widespread purpura fulminans, disseminated intravascular coagulation (DIC), and acute primary adrenal insufficiency. Autopsy reveals massive bilateral adrenal hemorrhage and cortical necrosis. What is the eponymous name of this syndrome?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Sheehan syndrome"},
            {"letter": "B", "is_correct": True, "text": "Waterhouse-Friderichsen syndrome"},
            {"letter": "C", "is_correct": False, "text": "Nelson syndrome"},
            {"letter": "D", "is_correct": False, "text": "Schmidt syndrome"},
            {"letter": "E", "is_correct": False, "text": "Kallmann syndrome"}
        ],
        "explanation": "Correct Answer: B. Waterhouse-Friderichsen syndrome.\n\nWaterhouse-Friderichsen syndrome is a catastrophic complication of severe meningococcemia (and rarely S. pneumoniae or Pseudomonas):\n• Pathophysiology: Massive endotoxemia (lipooligosaccharide / LOS) causes widespread endothelial damage, severe DIC, and microvascular thrombosis.\n• Pathology: Bilateral adrenal hemorrhage with acute hemorrhagic infarction and destruction of the adrenal cortices.\n• Clinical features: Profound refractory septic shock, severe hypoglycemia, hyperkalemia, hyponatremia, and death within hours."
    },
    {
        "q_num": "MEN-16",
        "category": "Meningitis",
        "stem": "Which of the following free-living amoebae is acquired by sniffing warm, contaminated freshwater lakes through the nose, penetrates the cribriform plate along olfactory nerves, and causes rapidly fatal primary amoebic meningoencephalitis (PAM) within 3–7 days in healthy children and young adults?",
        "options": [
            {"letter": "A", "is_correct": True, "text": "Naegleria fowleri"},
            {"letter": "B", "is_correct": False, "text": "Acanthamoeba castellanii"},
            {"letter": "C", "is_correct": False, "text": "Balamuthia mandrillaris"},
            {"letter": "D", "is_correct": False, "text": "Entamoeba histolytica"},
            {"letter": "E", "is_correct": False, "text": "Toxoplasma gondii"}
        ],
        "explanation": "Correct Answer: A. Naegleria fowleri.\n\nNaegleria fowleri (the 'brain-eating amoeba'):\n• Transmission: Thermophilic free-living amoeba found in warm freshwater (lakes, rivers, unchlorinated pools, neti pots). Trophozoites enter the nasal cavity during swimming or diving.\n• Invasion: Penetrates the nasal neuroepithelium, migrates through the cribriform plate along olfactory nerve fibers into the olfactory bulb and frontal lobes.\n• Clinical course: Fulminant, purulent, hemorrhagic necrotizing meningoencephalitis (Primary Amoebic Meningoencephalitis / PAM); mortality >97%."
    },
    {
        "q_num": "MEN-17",
        "category": "Meningitis",
        "stem": "A 15-year-old boy presents with fever, stiff neck, and bilateral tender swelling of the parotid glands (parotitis). Lumbar puncture shows lymphocytic pleocytosis with normal glucose, consistent with aseptic meningitis. Which single-stranded, negative-sense RNA paramyxovirus with surface hemagglutinin and neuraminidase is responsible for this presentation?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Measles virus"},
            {"letter": "B", "is_correct": True, "text": "Mumps virus"},
            {"letter": "C", "is_correct": False, "text": "Respiratory syncytial virus"},
            {"letter": "D", "is_correct": False, "text": "Parainfluenza virus type 1"},
            {"letter": "E", "is_correct": False, "text": "Rubella virus"}
        ],
        "explanation": "Correct Answer: B. Mumps virus.\n\nMumps virus (Paramyxovirus family: enveloped, negative-sense, single-stranded RNA):\n• Manifestations: Parotitis (bilateral painful salivary gland swelling), orchitis (testicular inflammation that can cause subfertility in postpubertal males), and aseptic meningitis (~10-30% of patients).\n• Prevention: Live-attenuated MMR vaccine (Measles, Mumps, Rubella)."
    },
    {
        "q_num": "MEN-18",
        "category": "Meningitis",
        "stem": "In the empiric treatment of acute bacterial meningitis in an immunocompetent adult aged 18 to 50, standard guidelines recommend the combination of Vancomycin and Ceftriaxone. Why is Vancomycin included in this empiric regimen?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "To provide broad coverage against Gram-negative bacilli"},
            {"letter": "B", "is_correct": True, "text": "To cover penicillin- and cephalosporin-resistant strains of Streptococcus pneumoniae"},
            {"letter": "C", "is_correct": False, "text": "To treat fungal organisms in the subarachnoid space"},
            {"letter": "D", "is_correct": False, "text": "To cover Listeria monocytogenes"},
            {"letter": "E", "is_correct": False, "text": "To prevent secondary viral superinfections"}
        ],
        "explanation": "Correct Answer: B. To cover penicillin- and cephalosporin-resistant strains of Streptococcus pneumoniae.\n\nEmpiric antimicrobial rationale in adult bacterial meningitis:\n• Ceftriaxone (or cefotaxime): Excellent CSF penetration; covers Neisseria meningitidis, Haemophilus influenzae, and susceptible Streptococcus pneumoniae.\n• Vancomycin: Added routinely to empiric therapy to guarantee coverage against Cephalosporin-resistant strains of Streptococcus pneumoniae (mediated by altered penicillin-binding proteins, PBPs). (Vancomycin is stopped only if susceptibility testing confirms cephalosporin sensitivity)."
    },
    {
        "q_num": "MEN-19",
        "category": "Meningitis",
        "stem": "A 26-year-old woman presents with recurrent episodes of mild, self-limiting lymphocytic meningitis (Mollaret meningitis) over the past 3 years. Between episodes, she is completely asymptomatic. PCR testing of her CSF during acute episodes is most likely to be positive for which viral pathogen?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Herpes simplex virus type 1 (HSV-1)"},
            {"letter": "B", "is_correct": True, "text": "Herpes simplex virus type 2 (HSV-2)"},
            {"letter": "C", "is_correct": False, "text": "Cytomegalovirus (CMV)"},
            {"letter": "D", "is_correct": False, "text": "Epstein-Barr virus (EBV)"},
            {"letter": "E", "is_correct": False, "text": "Human herpesvirus 6 (HHV-6)"}
        ],
        "explanation": "Correct Answer: B. Herpes simplex virus type 2 (HSV-2).\n\nMollaret meningitis is a syndrome of benign, recurrent, self-limiting aseptic meningitis:\n• Etiology: Vast majority of cases are caused by reactivation of Herpes Simplex Virus type 2 (HSV-2) from sacral sensory ganglia.\n• Distinct clinical contrast: While HSV-1 causes severe, focal temporal necrotizing encephalitis in adults, HSV-2 characteristically causes diffuse, non-focal aseptic meningitis and recurrent Mollaret meningitis."
    },
    {
        "q_num": "MEN-20",
        "category": "Meningitis",
        "stem": "An adult patient with confirmed bacterial meningitis undergoes physical examination. Which of the following cranial nerves is most frequently affected in acute bacterial meningitis, leading to permanent sensorineural hearing loss as the most common long-term neurological sequela?",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Cranial nerve II (Optic)"},
            {"letter": "B", "is_correct": False, "text": "Cranial nerve V (Trigeminal)"},
            {"letter": "C", "is_correct": False, "text": "Cranial nerve VII (Facial)"},
            {"letter": "D", "is_correct": True, "text": "Cranial nerve VIII (Vestibulocochlear)"},
            {"letter": "E", "is_correct": False, "text": "Cranial nerve XII (Hypoglossal)"}
        ],
        "explanation": "Correct Answer: D. Cranial nerve VIII (Vestibulocochlear).\n\nSensorineural hearing loss occurs in up to 10-30% of survivors of acute bacterial meningitis (especially pneumococcal meningitis):\n• Pathophysiology: Suppurative inflammation spreads from the subarachnoid space through the cochlear aqueduct into the inner ear (suppurative labyrinthitis), damaging the delicate sensory hair cells of the organ of Corti and causing direct inflammatory neuritis of the vestibulocochlear nerve (CN VIII).\n• Early administration of dexamethasone significantly reduces this complication."
    }
]

if __name__ == '__main__':
    print(f'Part 4 loaded successfully with {len(part4_questions)} questions.')
