# focused_zen_part4.py
# 80 Board-Style USMLE Step 1 Questions directly aligned with
# "Copy of Long NeuroPsych Exam 1 Study Guide.docx"
# Topics 13-16 (20 Questions each, IDs FZ_Q241 to FZ_Q320)

focused_questions_part4 = [
    # =========================================================================
    # TOPIC 13: Cannabis Management (FZ_Q241 - FZ_Q260)
    # =========================================================================
    {
        "id": "FZ_Q241",
        "question_number": 241,
        "category": "Cannabis Management",
        "stem": "Endocannabinoids such as anandamide (N-arachidonoylethanolamine) and 2-arachidonoylglycerol (2-AG) serve as retrograde synaptic messengers in the central nervous system. How are these endogenous ligands synthesized and released at central synapses?",
        "options": [
            {"text": "Synthesized on demand from membrane phospholipid precursors in the postsynaptic neuron upon depolarization, then diffuse retrogradely to act on presynaptic CB1 receptors", "is_correct": True},
            {"text": "Stored in dense-core vesicles in the presynaptic terminal and exocytosed in response to voltage-gated calcium influx", "is_correct": False},
            {"text": "Produced constitutively in astrocytic end-feet and transported across the blood-brain barrier via glucose transporter 1 (GLUT-1)", "is_correct": False},
            {"text": "Synthesized in the rough endoplasmic reticulum as prepropeptides and cleaved in the Golgi apparatus before anterograde axonal transport", "is_correct": False},
            {"text": "Released continuously by oligodendrocytes into the node of Ranvier to maintain axonal conduction velocity", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Synthesized on demand from membrane phospholipid precursors in the postsynaptic neuron upon depolarization, then diffuse retrogradely to act on presynaptic CB1 receptors.\n\nEndocannabinoids (anandamide and 2-AG) are unconventional neurotransmitters because they are lipid molecules synthesized 'on demand' rather than stored in synaptic vesicles:\n1. Postsynaptic depolarization causes intracellular calcium influx (or Gq-coupled receptor activation), activating phospholipase D (for anandamide) or phospholipase C / diacylglycerol lipase (for 2-AG).\n2. These lipophilic mediators traverse the postsynaptic membrane into the synaptic cleft and travel retrogradely to bind presynaptic cannabinoid type 1 (CB1) receptors.\n3. Activation of presynaptic CB1 receptors inhibits presynaptic neurotransmitter release (depolarization-induced suppression of inhibition [DSI] if GABA is blocked, or depolarization-induced suppression of excitation [DSE] if glutamate is blocked).\n\n• Option B is incorrect: Endocannabinoids are not stored in vesicles; their hydrophobic nature prevents vesicular compartmentalization."
    },
    {
        "id": "FZ_Q242",
        "question_number": 242,
        "category": "Cannabis Management",
        "stem": "Cannabinoid type 1 (CB1) receptors are among the most abundant G-protein coupled receptors in the human brain. What is the downstream signal transduction mechanism activated upon agonist binding to the CB1 receptor?",
        "options": [
            {"text": "Coupling to Gi/o proteins, leading to inhibition of adenylyl cyclase, closure of voltage-gated N- and P/Q-type calcium channels, and opening of inward-rectifying potassium channels", "is_correct": True},
            {"text": "Coupling to Gs proteins, leading to adenylyl cyclase activation, elevated cyclic AMP, and protein kinase A phosphorylation", "is_correct": False},
            {"text": "Coupling to Gq proteins, activating phospholipase C to generate inositol trisphosphate (IP3) and diacylglycerol (DAG)", "is_correct": False},
            {"text": "Intrinsic tyrosine kinase autophosphorylation activating the MAP kinase cascade", "is_correct": False},
            {"text": "Direct opening of ligand-gated chloride channels causing fast postsynaptic hyperpolarization", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Coupling to Gi/o proteins, leading to inhibition of adenylyl cyclase, closure of voltage-gated N- and P/Q-type calcium channels, and opening of inward-rectifying potassium channels.\n\nCB1 receptors are presynaptic Gi/o-protein coupled receptors. Their downstream cascade includes:\n• Inhibition of adenylyl cyclase -> decreases intracellular cyclic AMP (cAMP) and reduces PKA activity.\n• Inhibition of presynaptic voltage-gated N-type and P/Q-type calcium channels -> reduces presynaptic calcium influx required for SNARE-mediated vesicle fusion.\n• Activation of G-protein-coupled inwardly rectifying potassium channels (GIRK) -> hyperpolarizes the presynaptic terminal.\nTogether, these actions potently suppress the exocytosis of classical neurotransmitters (glutamate, GABA, acetylcholine, and norepinephrine) from the presynaptic terminal."
    },
    {
        "id": "FZ_Q243",
        "question_number": 243,
        "category": "Cannabis Management",
        "stem": "A neuropharmacologist is mapping the anatomical distribution of cannabinoid receptors in the human body. Which of the following correctly pairs the cannabinoid receptor subtype with its predominant tissue distribution and primary physiological role?",
        "options": [
            {"text": "CB1: Central nervous system (basal ganglia, hippocampus, cerebellum); CB2: Immune cells (spleen, tonsils, microglia)", "is_correct": True},
            {"text": "CB1: Peripheral mast cells and eosinophils; CB2: Cerebral cortex and thalamic relay nuclei", "is_correct": False},
            {"text": "CB1: Cardiac pacemakers and atria; CB2: Renal glomeruli and proximal tubules", "is_correct": False},
            {"text": "CB1: Medullary respiratory rhythm centers; CB2: Spinal dorsal horn primary nociceptors", "is_correct": False},
            {"text": "CB1: Skeletal muscle neuromuscular junctions; CB2: Hepatic biliary canaliculi", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. CB1: Central nervous system (basal ganglia, hippocampus, cerebellum); CB2: Immune cells (spleen, tonsils, microglia).\n\nDistribution of cannabinoid receptors:\n• CB1 receptors: Predominantly expressed in the CNS, with highest densities in the basal ganglia (substantia nigra, globus pallidus), cerebellum (mediating motor coordination and balance), hippocampus (mediating short-term memory deficits), and cerebral cortex. Notably, CB1 density is remarkably sparse in the brainstem cardiorespiratory centers, explaining why cannabis overdose does not cause fatal respiratory depression.\n• CB2 receptors: Primarily localized peripherally on immune system tissues (spleen, tonsils, macrophages, B cells, T cells) and CNS microglia. CB2 activation mediates immunosuppressive and anti-inflammatory effects by modulating cytokine release without producing psychotropic effects."
    },
    {
        "id": "FZ_Q244",
        "question_number": 244,
        "category": "Cannabis Management",
        "stem": "A 28-year-old man who smokes cannabis daily presents with a 6-month history of recurrent, debilitating episodes of severe nausea, cyclical vomiting, and colicky abdominal pain. Extensive GI workups, including upper endoscopy and abdominal CT, are completely normal. During history taking, he states that the only thing that relieves his nausea is taking scalding hot showers multiple times each day. Which of the following conditions is the most likely diagnosis?",
        "options": [
            {"text": "Cannabinoid hyperemesis syndrome", "is_correct": True},
            {"text": "Cyclic vomiting syndrome secondary to migraine", "is_correct": False},
            {"text": "Gastroparesis secondary to diabetic autonomic neuropathy", "is_correct": False},
            {"text": "Acute intermittent porphyria", "is_correct": False},
            {"text": "Irritable bowel syndrome, diarrhea-predominant", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Cannabinoid hyperemesis syndrome.\n\nCannabinoid Hyperemesis Syndrome (CHS) is a clinical disorder characterized by:\n1. Chronic, heavy, daily cannabis use (usually >1 year).\n2. Cyclic, severe nausea, intractable vomiting, and colicky periumbilical abdominal pain.\n3. Pathognomonic compulsive hot bathing or showering: Patients spend hours in hot water because heat activates cutaneous transient receptor potential vanilloid 1 (TRPV1) receptors, which restores hypothalamic thermoregulation and causes splanchnic vasodilation, temporarily counteracting cannabis-induced hypothermia and GI dysmotility.\n4. Resolution of symptoms upon complete cannabis cessation.\n\n• First-line acute symptomatic relief includes haloperidol and topical capsaicin cream (TRPV1 agonist). Conventional antiemetics (ondansetron, promethazine) are notoriously ineffective."
    },
    {
        "id": "FZ_Q245",
        "question_number": 245,
        "category": "Cannabis Management",
        "stem": "A patient with cannabinoid hyperemesis syndrome presents to the emergency department in distress. What is the mechanism of action by which application of topical capsaicin cream to the periumbilical region provides rapid symptomatic relief of nausea and abdominal pain?",
        "options": [
            {"text": "Stimulates peripheral cutaneous TRPV1 receptors, mimicking the thermal sensory input of hot showers and downregulating hypothalamic and splanchnic nociceptive signaling", "is_correct": True},
            {"text": "Competitively antagonizes CB1 receptors in the chemoreceptor trigger zone", "is_correct": False},
            {"text": "Inhibits postsynaptic dopamine D2 receptors in the area postrema", "is_correct": False},
            {"text": "Blocks serotonin 5-HT3 receptors on vagal afferents in the gastrointestinal mucosa", "is_correct": False},
            {"text": "Promotes gastric emptying by agonizing motilin receptors in the duodenum", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Stimulates peripheral cutaneous TRPV1 receptors, mimicking the thermal sensory input of hot showers and downregulating hypothalamic and splanchnic nociceptive signaling.\n\nChronic high-dose THC exposure desensitizes both CB1 and TRPV1 receptors in the enteric nervous system and hypothalamus. Heat and capsaicin:\n• Both activate TRPV1 receptors (the heat- and capsaicin-sensitive ion channel), which redirects cerebral/cutaneous blood flow, corrects cannabis-mediated splanchnic hypoperfusion, and overrides aberrant visceral pain signals to the brainstem vomiting centers.\n• Capsaicin cream applied to the abdomen or back is therefore standard-of-care adjuvant pharmacotherapy in acute CHS presentations in the emergency department."
    },
    {
        "id": "FZ_Q246",
        "question_number": 246,
        "category": "Cannabis Management",
        "stem": "A 54-year-old man undergoing adjuvant chemotherapy for metastatic colon adenocarcinoma suffers from intractable chemotherapy-induced nausea and vomiting (CINV) despite trials of ondansetron and dexamethasone. He is prescribed dronabinol. What is the active pharmaceutical chemical in dronabinol?",
        "options": [
            {"text": "Synthetic delta-9-tetrahydrocannabinol (THC)", "is_correct": True},
            {"text": "Purified cannabidiol (CBD)", "is_correct": False},
            {"text": "Synthetic analog of anandamide (AEA)", "is_correct": False},
            {"text": "Selective CB2 receptor inverse agonist", "is_correct": False},
            {"text": "Inhibitor of fatty acid amide hydrolase (FAAH)", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Synthetic delta-9-tetrahydrocannabinol (THC).\n\nDronabinol (Marinol) is an orally administered synthetic delta-9-tetrahydrocannabinol (THC). Indications FDA-approved for dronabinol:\n1. Chemotherapy-induced nausea and vomiting (CINV) in patients who have failed to respond adequately to conventional antiemetics.\n2. Anorexia and weight loss (cachexia) associated with AIDS.\n\n• Cannabidiol (Option B) is Epidiolex, approved for pediatric epilepsy, not dronabinol."
    },
    {
        "id": "FZ_Q247",
        "question_number": 247,
        "category": "Cannabis Management",
        "stem": "A 4-year-old child with a refractory genetic epileptic encephalopathy characterized by multiple daily polymorphic seizures (atonic drop attacks and tonic seizures) is diagnosed with Lennox-Gastaut syndrome. Which of the following cannabis-derived compounds is FDA-approved specifically for refractory pediatric seizure disorders such as Dravet syndrome and Lennox-Gastaut syndrome?",
        "options": [
            {"text": "Cannabidiol (CBD)", "is_correct": True},
            {"text": "Delta-9-tetrahydrocannabinol (THC)", "is_correct": False},
            {"text": "Nabilone", "is_correct": False},
            {"text": "Rimonabant", "is_correct": False},
            {"text": "Dronabinol", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Cannabidiol (CBD).\n\nEpidiolex is an FDA-approved, highly purified plant-derived oral solution of Cannabidiol (CBD). It is approved for the treatment of seizures associated with:\n1. Lennox-Gastaut syndrome (LGS)\n2. Dravet syndrome (severe myoclonic epilepsy of infancy)\n3. Tuberous sclerosis complex (TSC)\nUnlike THC, CBD has negligible affinity for CB1 receptors, is non-intoxicating (does not cause euphoria), and exerts anticonvulsant activity via antagonism of GPR55, desensitization of TRPV1 channels, and modulation of intracellular calcium."
    },
    {
        "id": "FZ_Q248",
        "question_number": 248,
        "category": "Cannabis Management",
        "stem": "A 36-year-old woman with relapsing-remitting multiple sclerosis suffers from painful, spastic lower extremity spasms that are refractory to baclofen and tizanidine. In several countries, an oromucosal spray containing a 1:1 ratio of delta-9-THC and cannabidiol (nabiximols / Sativex) is approved for this condition. What is the clinical benefit of combining cannabidiol (CBD) with THC in medical cannabis formulations?",
        "options": [
            {"text": "CBD acts as a negative allosteric modulator of CB1, mitigating the intoxicating psychoactive adverse effects, tachycardia, and anxiety caused by THC while synergistically improving muscle spasticity", "is_correct": True},
            {"text": "CBD completely blocks THC absorption across mucosal membranes", "is_correct": False},
            {"text": "CBD irreversibly binds to and inactivates hepatic cytochrome P450 3A4 to eliminate all drug metabolism", "is_correct": False},
            {"text": "CBD converts delta-9-THC into delta-8-THC in the bloodstream", "is_correct": False},
            {"text": "CBD stimulates peripheral histamine release to induce sedation", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. CBD acts as a negative allosteric modulator of CB1, mitigating the intoxicating psychoactive adverse effects, tachycardia, and anxiety caused by THC while synergistically improving muscle spasticity.\n\nCBD modulates the pharmacodynamic profile of THC:\n• CBD functions as a negative allosteric modulator (NAM) at the CB1 receptor, dampening the maximum efficacy of THC at CB1. This reduces THC-induced tachycardia, panic, paranoia, and cognitive impairment.\n• Concurrently, CBD and THC act synergistically on non-CB1 targets (glycine receptors, 5-HT1A, TRPV1) to provide enhanced analgesia and reduction in spasticity (the 'entourage effect')."
    },
    {
        "id": "FZ_Q249",
        "question_number": 249,
        "category": "Cannabis Management",
        "stem": "A 21-year-old college student presents to the student health clinic 45 minutes after smoking marijuana. Physical examination reveals bilateral conjunctival injection, dry oral mucosa, heart rate of 115/min, and blood pressure of 105/65 mmHg. Which physiological mechanism explains the pathognomonic conjunctival injection and tachycardia seen in acute cannabis intoxication?",
        "options": [
            {"text": "Vasodilation of episcleral blood vessels via CB1 activation, and reflex tachycardia secondary to decreased peripheral vascular resistance combined with direct sympathetic activation", "is_correct": True},
            {"text": "Potent constriction of anterior ciliary arteries with compensatory hypertension", "is_correct": False},
            {"text": "Direct stimulation of muscarinic M3 receptors on ciliary body smooth muscle", "is_correct": False},
            {"text": "Immune complex deposition in the episcleral capillary beds", "is_correct": False},
            {"text": "Release of histamine from conjunctival mast cells via IgE cross-linking", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Vasodilation of episcleral blood vessels via CB1 activation, and reflex tachycardia secondary to decreased peripheral vascular resistance combined with direct sympathetic activation.\n\nAcute cannabis intoxication features classic cardiovascular and ocular findings:\n1. Conjunctival injection: Cannabinoids cause active vasodilation of conjunctival/episcleral vessels (and lowers intraocular pressure), producing bright red, bloodshot eyes.\n2. Tachycardia: Acute THC ingestion causes prominent sinus tachycardia (dose-dependent increase by 20-50 bpm) through sympathetic stimulation, inhibition of parasympathetic vagal tone, and reflex baroreceptor compensation for mild peripheral vasodilation/orthostatic hypotension.\n3. Xerostomia (dry mouth): Submandibular and parotid glands express CB1/CB2 receptors; cannabinoid activation inhibits salivary secretion."
    },
    {
        "id": "FZ_Q250",
        "question_number": 250,
        "category": "Cannabis Management",
        "stem": "A 24-year-old man who has been smoking cannabis multiple times daily for 3 years abruptly discontinues use when applying for a new job. Three days later, he presents complaining of severe irritability, restlessness, insomnia, vivid disturbing dreams, night sweats, nausea, and loss of appetite. He has lost 2 kg over the past week. What is the expected time course for DSM-5 Cannabis Withdrawal Syndrome?",
        "options": [
            {"text": "Symptoms onset within 24 to 72 hours, peak between days 2 and 6, and typically resolve within 1 to 2 weeks", "is_correct": True},
            {"text": "Symptoms onset within 30 minutes, peak at 4 hours, and completely resolve within 12 hours", "is_correct": False},
            {"text": "Symptoms do not appear until 4 weeks after cessation and persist indefinitely", "is_correct": False},
            {"text": "Cannabis produces only psychological craving without any physical or physiological withdrawal syndrome", "is_correct": False},
            {"text": "Withdrawal always culminates in life-threatening grand mal seizures and autonomic instability similar to delirium tremens", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Symptoms onset within 24 to 72 hours, peak between days 2 and 6, and typically resolve within 1 to 2 weeks.\n\nDSM-5 Cannabis Withdrawal Syndrome occurs in heavy, prolonged users after abrupt cessation:\n• Symptoms include: irritability, anger, aggression, anxiety, sleep difficulty (insomnia, strange/vivid dreams), decreased appetite/weight loss, depressed mood, and physical symptoms (sweats, chills, headache, abdominal pain).\n• Time course: Because THC is highly lipophilic and stored in adipose tissue, it is slowly eliminated. Withdrawal begins within 24-48 hours, peaks at day 2-6, and gradually resolves within 1-2 weeks.\n• Unlike alcohol or benzodiazepine withdrawal, cannabis withdrawal is not fatal and does not cause seizures or delirium tremens."
    },
    {
        "id": "FZ_Q251",
        "question_number": 251,
        "category": "Cannabis Management",
        "stem": "Synthetic cannabinoids (often sold illicitly under street names such as 'K2' or 'Spice') carry a significantly higher risk of severe toxicity, agitation, psychosis, tachyarrhythmias, and death compared to natural cannabis. What pharmacological property accounts for the dramatically increased toxicity of synthetic cannabinoids?",
        "options": [
            {"text": "Synthetic cannabinoids act as high-potency, full agonists at the CB1 receptor with high intrinsic activity, whereas delta-9-THC is only a partial agonist", "is_correct": True},
            {"text": "Synthetic cannabinoids selectively antagonize dopamine D2 receptors in the striatum", "is_correct": False},
            {"text": "Synthetic cannabinoids contain high concentrations of pure cannabidiol", "is_correct": False},
            {"text": "Synthetic cannabinoids are irreversibly cleared by pulmonary surfactant rather than hepatic metabolism", "is_correct": False},
            {"text": "Synthetic cannabinoids block voltage-gated chloride channels in peripheral nerves", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Synthetic cannabinoids act as high-potency, full agonists at the CB1 receptor with high intrinsic activity, whereas delta-9-THC is only a partial agonist.\n\nPharmacological difference:\n• Natural THC is a low-efficacy partial agonist at the CB1 receptor. Even at saturating doses, it achieves only partial receptor activation.\n• Illicit synthetic cannabinoids (e.g., JWH-018, AM-2201) are full agonists at CB1 with binding affinities up to 100-800 times greater than THC. They produce maximal receptor activation without any modulatory CBD. This leads to profound toxic delirium, hallucinations, extreme tachycardia, acute kidney injury, seizures, and fatal cardiac arrhythmias."
    },
    {
        "id": "FZ_Q252",
        "question_number": 252,
        "category": "Cannabis Management",
        "stem": "Why does a massive overdose of pure cannabis or delta-9-THC virtually never result in fatal respiratory depression, in stark contrast to overdoses involving opioids or barbiturates?",
        "options": [
            {"text": "CB1 receptors are virtually absent in the brainstem medullary respiratory centers (pre-Bötzinger complex)", "is_correct": True},
            {"text": "THC is rapidly hydrolyzed by serum cholinesterase within 5 seconds of entering the bloodstream", "is_correct": False},
            {"text": "Cannabinoids directly stimulate medullary phrenic motor neurons to prevent hypoventilation", "is_correct": False},
            {"text": "Cannabinoids stimulate central chemoreceptors in the carotid body to double the respiratory drive", "is_correct": False},
            {"text": "CB1 receptors are coupled exclusively to excitatory Gs proteins in the central nervous system", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. CB1 receptors are virtually absent in the brainstem medullary respiratory centers (pre-Bötzinger complex).\n\nFatal opioid and sedative overdoses occur because mu-opioid and GABA-A receptors are heavily expressed in brainstem respiratory control centers (pre-Bötzinger complex and solitary tract nucleus), blunting responsiveness to arterial carbon dioxide.\nIn contrast, CB1 receptors have an extremely low density in brainstem cardiorespiratory centers. As a result, massive doses of cannabis cause sedation and intoxication without shutting down the brainstem respiratory rhythm generator, giving THC an extraordinarily wide therapeutic index."
    },
    {
        "id": "FZ_Q253",
        "question_number": 253,
        "category": "Cannabis Management",
        "stem": "A 19-year-old woman is brought to the clinic because of worsening social withdrawal, paranoid delusions, and auditory hallucinations. A detailed family history reveals that her maternal uncle has schizophrenia. Epidemiological studies demonstrate that heavy, early-onset adolescent cannabis use is associated with a significantly increased risk of developing schizophrenia. Which polymorphism is associated with increased vulnerability to cannabis-induced psychosis in adolescents?",
        "options": [
            {"text": "Catechol-O-methyltransferase (COMT) Val158Met polymorphism", "is_correct": True},
            {"text": "Apolipoprotein E epsilon 4 (APOE4) allele", "is_correct": False},
            {"text": "Dihydropyrimidine dehydrogenase (DPYD) deficiency", "is_correct": False},
            {"text": "Factor V Leiden mutation", "is_correct": False},
            {"text": "HLA-B*5701 allele", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Catechol-O-methyltransferase (COMT) Val158Met polymorphism.\n\nGene-environment interactions in cannabis-induced psychosis:\n• Adolescents carrying the Val/Val genotype of the catechol-O-methyltransferase (COMT) gene (which metabolizes dopamine) have a significantly higher risk of developing psychotic disorders and schizophrenia if they use cannabis during adolescent neurodevelopment.\n• THC enhances mesolimbic dopamine transmission while disrupting prefrontal dopamine clearance, accelerating psychosis in genetically vulnerable individuals."
    },
    {
        "id": "FZ_Q254",
        "question_number": 254,
        "category": "Cannabis Management",
        "stem": "Which of the following enzymes is responsible for the rapid degradation and intracellular inactivation of the endocannabinoid anandamide (AEA) following its cellular reuptake?",
        "options": [
            {"text": "Fatty acid amide hydrolase (FAAH)", "is_correct": True},
            {"text": "Monoacylglycerol lipase (MAGL)", "is_correct": False},
            {"text": "Acetylcholinesterase (AChE)", "is_correct": False},
            {"text": "Catechol-O-methyltransferase (COMT)", "is_correct": False},
            {"text": "DOPA decarboxylase", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Fatty acid amide hydrolase (FAAH).\n\nEndocannabinoid degradation enzymes:\n• Anandamide (AEA) is primarily hydrolyzed into arachidonic acid and ethanolamine by Fatty Acid Amide Hydrolase (FAAH), a membrane-bound serine hydrolase located in postsynaptic intracellular membranes.\n• 2-Arachidonoylglycerol (2-AG) is primarily broken down into arachidonic acid and glycerol by Monoacylglycerol Lipase (MAGL), located presynaptically.\n• Pharmacological inhibitors of FAAH (or genetic FAAH mutations) increase endogenous anandamide levels, producing analgesia and anxiolysis without cannabis intoxication."
    },
    {
        "id": "FZ_Q255",
        "question_number": 255,
        "category": "Cannabis Management",
        "stem": "A 32-year-old patient who uses cannabis regularly undergoes a routine urine drug screening. Although his last cannabis use was 3 weeks ago, his urine immunoassay remains positive for 11-nor-9-carboxy-delta-9-THC (THC-COOH). What pharmacokinetic property of cannabinoids explains this prolonged detection window?",
        "options": [
            {"text": "High lipophilicity with extensive sequestration in adipose tissue, followed by slow, prolonged redistribution into the circulation and elimination", "is_correct": True},
            {"text": "Covalent irreversible binding to albumin in plasma preventing glomerular filtration", "is_correct": False},
            {"text": "Continuous endogenous de novo synthesis of THC by bone marrow adipocytes", "is_correct": False},
            {"text": "Enterohepatic recirculation driven by bacterial beta-glucuronidase that multiplies drug mass", "is_correct": False},
            {"text": "Storage in insoluble renal tubular calculi that slowly erode over months", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. High lipophilicity with extensive sequestration in adipose tissue, followed by slow, prolonged redistribution into the circulation and elimination.\n\nPharmacokinetics of THC:\n• THC is extraordinarily lipophilic with a large volume of distribution (~10 L/kg). Following inhalation or ingestion, it rapidly distributes into highly vascular tissues (brain, liver) and then partitions into body fat stores (adipose tissue).\n• In chronic heavy users, THC slowly leaches back out of fat deposits into the bloodstream over days to weeks, where it is metabolized by hepatic CYP2C9 and CYP3A4 to 11-hydroxy-THC (active) and carboxy-THC (inactive THC-COOH), which undergoes glucuronidation and renal excretion. As a result, urine drug tests can remain positive for up to 30 days or longer in chronic users."
    },
    {
        "id": "FZ_Q256",
        "question_number": 256,
        "category": "Cannabis Management",
        "stem": "Which of the following describes the mechanism by which cannabis consumption stimulates acute hyperphagia, colloquially known as 'the munchies'?",
        "options": [
            {"text": "Activation of CB1 receptors in the hypothalamic arcuate nucleus and olfactory bulb, enhancing appetite and odor detection while stimulating pro-opiomelanocortin (POMC) neurons to release beta-endorphin", "is_correct": True},
            {"text": "Direct inhibition of lateral hypothalamic orexin synthesis", "is_correct": False},
            {"text": "Profound suppression of circulating ghrelin levels in gastric fundic glands", "is_correct": False},
            {"text": "Upregulation of leptin receptor signaling in the ventromedial hypothalamus", "is_correct": False},
            {"text": "Direct antagonism of neuropeptide Y (NPY) receptors in the gut", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Activation of CB1 receptors in the hypothalamic arcuate nucleus and olfactory bulb, enhancing appetite and odor detection while stimulating pro-opiomelanocortin (POMC) neurons to release beta-endorphin.\n\nCannabinoids stimulate appetite through multiple convergent central mechanisms:\n1. Hypothalamus: CB1 activation in the arcuate and paraventricular nuclei paradoxically stimulates POMC neurons to release appetite-stimulating beta-endorphins and increases Neuropeptide Y (NPY) and agouti-related peptide (AgRP) signaling.\n2. Olfactory bulb: CB1 activation on cortical feedback projections enhances odor sensitivity and food aroma detection.\n3. Nucleus accumbens: Enhances dopamine release, amplifying the hedonic reward value ('palatability') of food."
    },
    {
        "id": "FZ_Q257",
        "question_number": 257,
        "category": "Cannabis Management",
        "stem": "A 10-year-old child with Dravet syndrome is treated with cannabidiol (Epidiolex) alongside clobazam for refractory seizures. At a follow-up visit, the parents report that the child has become severely somnolent, lethargic, and unsteady on his feet. Which pharmacokinetic drug interaction between cannabidiol and clobazam explains this clinical presentation?",
        "options": [
            {"text": "Cannabidiol inhibits CYP2C19, leading to markedly elevated serum concentrations of N-desmethylclobazam, the active sedating metabolite of clobazam", "is_correct": True},
            {"text": "Clobazam displaces cannabidiol from plasma proteins, increasing free active CBD by 500%", "is_correct": False},
            {"text": "Cannabidiol induces CYP3A4, accelerating the conversion of clobazam into inactive glucuronide conjugates", "is_correct": False},
            {"text": "Clobazam blocks intestinal absorption of cannabidiol via P-glycoprotein competition", "is_correct": False},
            {"text": "Cannabidiol directly antagonizes GABA-A receptors, producing paradoxical sedation", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Cannabidiol inhibits CYP2C19, leading to markedly elevated serum concentrations of N-desmethylclobazam, the active sedating metabolite of clobazam.\n\nHigh-yield drug interaction:\n• Clobazam (a 1,5-benzodiazepine) is metabolized by CYP3A4 to N-desmethylclobazam (norclobazam), an active metabolite with a long half-life that mediates significant sedation.\n• Norclobazam is further metabolized and cleared by CYP2C19.\n• Cannabidiol is a potent inhibitor of CYP2C19. When co-administered, CBD causes a 3- to 5-fold increase in plasma concentrations of active N-desmethylclobazam, resulting in profound sedation, somnolence, drooling, and ataxia. Management requires reducing the dose of clobazam."
    },
    {
        "id": "FZ_Q258",
        "question_number": 258,
        "category": "Cannabis Management",
        "stem": "An anti-obesity medication developed in the 2000s, rimonabant, was designed to suppress appetite by functioning as an inverse agonist/antagonist at the CB1 receptor. Although effective for weight loss, it was withdrawn worldwide due to serious neuropsychiatric adverse effects. Which adverse effects led to its withdrawal?",
        "options": [
            {"text": "Severe depression, anxiety, and suicidal ideation", "is_correct": True},
            {"text": "Refractory hypertension and aortic dissection", "is_correct": False},
            {"text": "Fulminant hepatic necrosis and liver failure", "is_correct": False},
            {"text": "Malignant hyperthermia and rhabdomyolysis", "is_correct": False},
            {"text": "Progressive multifocal leukoencephalopathy (PML)", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Severe depression, anxiety, and suicidal ideation.\n\nRimonabant was a potent selective CB1 inverse agonist. By blocking endogenous endocannabinoid tone in the mesolimbic reward system and amygdala:\n• It effectively reduced appetite and body weight.\n• However, blocking tonic CB1 signaling in emotional processing circuits led to severe dysphoria, major depressive episodes, unprovoked panic attacks, and completed suicides. This led to its abrupt withdrawal from the global market and demonstrated the vital role of basal endocannabinoid tone in maintaining normal mood and emotional homeostasis."
    },
    {
        "id": "FZ_Q259",
        "question_number": 259,
        "category": "Cannabis Management",
        "stem": "In the human hippocampus, cannabinoid CB1 receptors are heavily expressed on cholecystokinin (CCK)-positive GABAergic interneurons. How does exogenous delta-9-THC intake impair short-term memory encoding and working memory in humans?",
        "options": [
            {"text": "Disrupts physiological theta and gamma oscillations and suppresses long-term potentiation (LTP) in CA1 pyramidal neurons", "is_correct": True},
            {"text": "Causes immediate apoptosis of CA3 pyramidal hippocampal neurons", "is_correct": False},
            {"text": "Irreversibly degrades acetylcholinesterase in the medial septum", "is_correct": False},
            {"text": "Selectively blocks NMDA glutamate channels in the dentate gyrus directly", "is_correct": False},
            {"text": "Stimulates microglial engulfment of dendritic spines in the entorhinal cortex within minutes", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Disrupts physiological theta and gamma oscillations and suppresses long-term potentiation (LTP) in CA1 pyramidal neurons.\n\nMechanisms of cannabis-induced memory impairment:\n• High density of CB1 receptors in hippocampal CA1, CA3, and dentate gyrus. CB1 activation suppresses both GABA and glutamate release from hippocampal terminals.\n• In the absence of coordinated physiological synaptic control, hippocampal theta and gamma oscillatory rhythms (necessary for synaptic synchronization and working memory) are desynchronized.\n• Furthermore, tonic CB1 activation inhibits the induction of Long-Term Potentiation (LTP), impairing the consolidation of new short-term memories into long-term storage."
    },
    {
        "id": "FZ_Q260",
        "question_number": 260,
        "category": "Cannabis Management",
        "stem": "A 42-year-old patient with chemotherapy-associated nausea asks about the differences between smoking/inhaling cannabis versus consuming oral cannabinoid edibles. What primary pharmacokinetic difference distinguishes oral ingestion of THC from pulmonary inhalation?",
        "options": [
            {"text": "Oral THC undergoes extensive first-pass hepatic metabolism converting it into 11-hydroxy-THC, a more potent active metabolite with delayed onset and longer duration of action", "is_correct": True},
            {"text": "Inhaled THC has a bioavailability of 100% and zero distribution to adipose tissue", "is_correct": False},
            {"text": "Oral THC is completely destroyed by gastric hydrochloric acid and exhibits zero systemic absorption", "is_correct": False},
            {"text": "Inhaled THC is metabolized exclusively in the pulmonary alveoli by carbonic anhydrase", "is_correct": False},
            {"text": "Oral THC reaches peak plasma concentrations within 2 minutes of ingestion", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Oral THC undergoes extensive first-pass hepatic metabolism converting it into 11-hydroxy-THC, a more potent active metabolite with delayed onset and longer duration of action.\n\nComparison of cannabis routes:\n• Inhalation (smoking/vaping): Rapid pulmonary alveolar absorption into arterial blood, bypassing hepatic first-pass metabolism. Onset within seconds to minutes; peak blood levels in 10-30 minutes; duration 2-4 hours.\n• Oral ingestion (edibles): Slow, erratic GI absorption with heavy first-pass hepatic metabolism by CYP2C9 and CYP3A4. A major portion of delta-9-THC is converted into 11-hydroxy-delta-9-THC, a metabolite that readily crosses the blood-brain barrier and is more potent and psychoactive than delta-9-THC itself. Onset is delayed (30-90 minutes), peak is delayed (2-4 hours), and duration is significantly prolonged (6-12 hours), often leading to accidental overconsumption."
    },

    # =========================================================================
    # TOPIC 14: Pathways and Opioids (FZ_Q261 - FZ_Q280)
    # =========================================================================
    {
        "id": "FZ_Q261",
        "question_number": 261,
        "category": "Pathways and Opioids",
        "stem": "Opioid receptors (mu, delta, and kappa) are class A G-protein coupled receptors. At the cellular level within the substantia gelatinosa of the spinal dorsal horn, what dual ionic mechanisms mediate opioid-induced inhibition of neurotransmission?",
        "options": [
            {"text": "Closure of presynaptic voltage-gated calcium channels (inhibiting glutamate and substance P exocytosis) and opening of postsynaptic G-protein-coupled inward-rectifying potassium channels (hyperpolarizing projection neurons)", "is_correct": True},
            {"text": "Opening of presynaptic sodium channels and closure of postsynaptic chloride channels", "is_correct": False},
            {"text": "Direct blockade of postsynaptic AMPA receptors and stimulation of presynaptic calcium influx", "is_correct": False},
            {"text": "Closure of postsynaptic potassium channels leading to prolonged subthreshold depolarization", "is_correct": False},
            {"text": "Opening of presynaptic calcium channels to activate calcineurin phosphatase", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Closure of presynaptic voltage-gated calcium channels (inhibiting glutamate and substance P exocytosis) and opening of postsynaptic G-protein-coupled inward-rectifying potassium channels (hyperpolarizing projection neurons).\n\nOpioid receptors couple to inhibitory Gi/o proteins to block pain transmission via two simultaneous actions:\n1. Presynaptic action: In primary nociceptive afferents (A-delta and C fibers), activated G-beta/gamma subunits bind to and inhibit voltage-gated Ca2+ channels (N-type and P/Q-type). This prevents calcium entry upon action potential arrival, blocking exocytosis of Substance P, CGRP, and glutamate.\n2. Postsynaptic action: In second-order spinothalamic neurons, G-beta/gamma subunits open G-protein inwardly rectifying potassium (GIRK) channels, allowing K+ to exit the cell. This produces hyperpolarization (IPSPs), making the second-order neuron resistant to firing."
    },
    {
        "id": "FZ_Q262",
        "question_number": 262,
        "category": "Pathways and Opioids",
        "stem": "In the endogenous descending pain-modulating pathway, electrical or pharmacological stimulation of the periaqueductal gray (PAG) produces profound analgesia. How does activation of the periaqueductal gray recruit descending pathways to inhibit nociception at the spinal cord dorsal horn?",
        "options": [
            {"text": "PAG neurons project to the rostral ventromedial medulla (nucleus raphe magnus) and locus coeruleus, which send serotonergic and noradrenergic fibers to activate enkephalin-releasing inhibitory interneurons in the substantia gelatinosa", "is_correct": True},
            {"text": "PAG axons project directly to peripheral pain receptors in the dermis to degrade bradykinin", "is_correct": False},
            {"text": "PAG neurons release GABA directly into the corticospinal tract to inhibit lower motor neurons", "is_correct": False},
            {"text": "PAG stimulates the anterior pituitary to secrete adrenocorticotropic hormone (ACTH)", "is_correct": False},
            {"text": "PAG neurons activate thalamic VPL neurons to overwhelm the somatosensory cortex with tactile input", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. PAG neurons project to the rostral ventromedial medulla (nucleus raphe magnus) and locus coeruleus, which send serotonergic and noradrenergic fibers to activate enkephalin-releasing inhibitory interneurons in the substantia gelatinosa.\n\nDescending pain modulation circuit:\n1. Midbrain periaqueductal gray (PAG) expresses high levels of mu-opioid receptors. Opioid binding disinhibits PAG projection neurons (by hyperpolarizing tonic GABAergic interneurons).\n2. Excitatory projections travel from PAG down to the rostral ventromedial medulla (RVM, specifically the Nucleus Raphe Magnus) and the Locus Coeruleus (pons).\n3. Nucleus raphe magnus sends serotonergic (5-HT) fibers and locus coeruleus sends noradrenergic (NE) fibers down the dorsolateral funiculus into the spinal dorsal horn.\n4. Serotonin and norepinephrine bind to alpha-2 and 5-HT receptors on local inhibitory interneurons in the substantia gelatinosa, triggering the release of endogenous opioids (enkephalin and dynorphin), which inhibit primary nociceptive afferents."
    },
    {
        "id": "FZ_Q263",
        "question_number": 263,
        "category": "Pathways and Opioids",
        "stem": "A 58-year-old man with end-stage renal disease (ESRD) on hemodialysis suffers severe postoperative pain after femoral neck fracture repair. The intern orders high-dose intravenous morphine. Over the next 24 hours, the patient develops profound respiratory depression, altered mental status, and myoclonic jerks. Accumulation of which morphine metabolites explains this clinical presentation in renal failure?",
        "options": [
            {"text": "Morphine-6-glucuronide (potent mu-agonist causing respiratory depression) and Morphine-3-glucuronide (neurotoxic metabolite causing myoclonus and hyperalgesia)", "is_correct": True},
            {"text": "Normeperidine causing ventricular tachycardia", "is_correct": False},
            {"text": "6-Monoacetylmorphine crossing into the biliary system", "is_correct": False},
            {"text": "Diacetylmorphine stimulating histamine H1 receptors", "is_correct": False},
            {"text": "Methadone-induced N-demethylation products", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Morphine-6-glucuronide (potent mu-agonist causing respiratory depression) and Morphine-3-glucuronide (neurotoxic metabolite causing myoclonus and hyperalgesia).\n\nMorphine hepatic metabolism produces two active glucuronide conjugates cleared by the kidneys:\n1. Morphine-6-glucuronide (M6G): Highly active at mu-opioid receptors, with analgesic and respiratory depressant potency ~4 to 6 times greater than morphine itself. In renal failure, M6G accumulates, causing profound, prolonged coma and respiratory depression.\n2. Morphine-3-glucuronide (M3G): Accounts for ~50-60% of morphine metabolites. It has no mu-opioid activity but is neurotoxic; accumulation produces central nervous system hyperexcitability, allodynia, myoclonus, and seizures.\n• Morphine and codeine should be avoided in renal insufficiency; fentanyl or methadone (which lack active renally cleared metabolites) are safer alternatives."
    },
    {
        "id": "FZ_Q264",
        "question_number": 264,
        "category": "Pathways and Opioids",
        "stem": "A 48-year-old woman with a history of major depressive disorder treated with sertraline (an SSRI) undergoes an orthopedic procedure. Postoperatively, she is administered intravenous meperidine for pain and shivering. Two hours later, she develops a temperature of 39.8°C (103.6°F), severe agitation, diaphoresis, hyperreflexia, and sustained ocular clonus. What pharmacological interaction caused this life-threatening condition?",
        "options": [
            {"text": "Meperidine inhibits neuronal serotonin reuptake (SERT), interacting synergistically with sertraline to trigger Serotonin Syndrome", "is_correct": True},
            {"text": "Meperidine accelerates hepatic conversion of sertraline into toxic metabolites", "is_correct": False},
            {"text": "Sertraline competitively blocks mu-opioid receptors, causing acute opioid withdrawal", "is_correct": False},
            {"text": "Meperidine and sertraline trigger malignant hyperthermia via ryanodine receptor gene mutation", "is_correct": False},
            {"text": "Meperidine induces acute adrenal insufficiency by blocking 11-beta-hydroxylase", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Meperidine inhibits neuronal serotonin reuptake (SERT), interacting synergistically with sertraline to trigger Serotonin Syndrome.\n\nMeperidine (Demerol) has unique pharmacological properties distinguishing it from other opioids:\n• In addition to mu-opioid agonism, meperidine is a serotonin reuptake inhibitor (SRI).\n• Co-administration with SSRIs, SNRIs, or MAO inhibitors leads to excessive intrasynaptic serotonin, causing Serotonin Syndrome (Hunter criteria: neuromuscular hyperactivity [hyperreflexia, clonus], autonomic hyperactivity [hyperthermia, tachycardia, diaphoresis], and altered mental status).\n• Furthermore, meperidine's metabolite normeperidine lowers the seizure threshold. Meperidine also has atropine-like anticholinergic properties (mydriasis, tachycardia)."
    },
    {
        "id": "FZ_Q265",
        "question_number": 265,
        "category": "Pathways and Opioids",
        "stem": "A 34-year-old woman enrolled in a methadone maintenance program for severe opioid use disorder presents for an annual checkup. A routine electrocardiogram reveals a corrected QT (QTc) interval of 520 ms (normal <450 ms). What is the mechanism by which methadone causes QT prolongation and increases the risk of Torsades de Pointes?",
        "options": [
            {"text": "Blocks human ether-a-go-go-related gene (hERG) voltage-gated potassium channels (IKr) in cardiac ventricular myocytes", "is_correct": True},
            {"text": "Directly activates cardiac L-type calcium channels to prolong phase 2 plateau", "is_correct": False},
            {"text": "Inhibits cardiac Ryanodine receptors causing intracellular calcium overload", "is_correct": False},
            {"text": "Competitively antagonizes muscarinic M2 receptors on the SA node", "is_correct": False},
            {"text": "Blocks fast voltage-gated sodium channels (phase 0) without altering repolarization", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Blocks human ether-a-go-go-related gene (hERG) voltage-gated potassium channels (IKr) in cardiac ventricular myocytes.\n\nMethadone cardiac toxicity:\n• Methadone is a full mu-opioid agonist and NMDA receptor antagonist with a very long elimination half-life (15-60 hours).\n• However, it blocks the hERG-encoded rapid delayed rectifier potassium channel (IKr) in ventricular myocytes, delaying cardiac repolarization.\n• This leads to concentration-dependent QTc prolongation, predisposing patients to the polymorphic ventricular tachycardia known as Torsades de Pointes, especially at doses >100 mg/day or when combined with other QT-prolonging drugs (e.g., fluconazole, ciprofloxacin, citalopram)."
    },
    {
        "id": "FZ_Q266",
        "question_number": 266,
        "category": "Pathways and Opioids",
        "stem": "A 29-year-old man with opioid dependence actively taking 80 mg of oxycodone daily presents to an addiction clinic. The physician administers a dose of sublingual buprenorphine. Within 45 minutes, the patient becomes violently agitated, sweating, shivering, and vomiting, with severe piloerection, abdominal cramps, and dilated pupils. What pharmacological property of buprenorphine precipitated this acute withdrawal state?",
        "options": [
            {"text": "Buprenorphine has very high binding affinity for mu-opioid receptors but low intrinsic activity (partial agonist), displacing full agonists from the receptor", "is_correct": True},
            {"text": "Buprenorphine is a pure competitive antagonist at mu, delta, and kappa receptors", "is_correct": False},
            {"text": "Buprenorphine rapidly blocks GABA-A receptors in the locus coeruleus", "is_correct": False},
            {"text": "Buprenorphine is metabolized into naloxone in the oral mucosa", "is_correct": False},
            {"text": "Buprenorphine induces hepatic cytochrome P450 enzymes within 30 minutes", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Buprenorphine has very high binding affinity for mu-opioid receptors but low intrinsic activity (partial agonist), displacing full agonists from the receptor.\n\nBuprenorphine is a partial mu-opioid agonist with extraordinarily high receptor affinity:\n• When administered to a patient who has full agonists (e.g., oxycodone, heroin, methadone) occupying their mu receptors, buprenorphine's high affinity allows it to displace the full agonist from the receptor.\n• However, because buprenorphine has low intrinsic efficacy, net receptor signaling drops precipitously from 100% to ~30-40%.\n• This abrupt drop in downstream signal transduction precipitates severe Precipitated Opioid Withdrawal. To avoid this, buprenorphine induction must occur only after the patient is already in mild-to-moderate spontaneous withdrawal (Clinical Opiate Withdrawal Scale [COWS] score ≥8-12)."
    },
    {
        "id": "FZ_Q267",
        "question_number": 267,
        "category": "Pathways and Opioids",
        "stem": "Suboxone is a widely prescribed sublingual film containing a 4:1 fixed-dose combination of buprenorphine and naloxone for maintenance treatment of opioid use disorder. What is the pharmacological rationale for adding naloxone to this formulation?",
        "options": [
            {"text": "Naloxone has negligible sublingual/oral bioavailability due to extensive first-pass metabolism, but if crushed and injected intravenously, it blocks opioid receptors and precipitates immediate withdrawal to deter IV abuse", "is_correct": True},
            {"text": "Naloxone synergistically enhances the analgesic and euphoric potency of sublingual buprenorphine", "is_correct": False},
            {"text": "Naloxone prevents buprenorphine-induced QT prolongation in cardiac myocytes", "is_correct": False},
            {"text": "Naloxone increases the sublingual absorption of buprenorphine across the oral mucosa", "is_correct": False},
            {"text": "Naloxone accelerates the clearance of buprenorphine by inducing CYP3A4", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Naloxone has negligible sublingual/oral bioavailability due to extensive first-pass metabolism, but if crushed and injected intravenously, it blocks opioid receptors and precipitates immediate withdrawal to deter IV abuse.\n\nSuboxone design:\n• When taken sublingually as prescribed, buprenorphine is absorbed across the oral mucosa (~30-50% bioavailability). In contrast, naloxone has poor sublingual absorption (<10%) and undergoes >95% first-pass hepatic glucuronidation, rendering it pharmacologically inactive when taken by mouth.\n• However, if an individual attempts to dissolve the film and inject it intravenously, naloxone enters the systemic circulation directly without first-pass clearance, where it potently blocks mu-opioid receptors and precipitates immediate, severe withdrawal. This acts as an abuse-deterrent."
    },
    {
        "id": "FZ_Q268",
        "question_number": 268,
        "category": "Pathways and Opioids",
        "stem": "A 52-year-old woman with advanced ovarian cancer receives escalating doses of oral oxycodone for malignant pelvic pain. Over several months, she requires increasing doses to achieve pain relief. However, which of the following physiological effects of opioids NEVER exhibits tolerance despite chronic, high-dose therapy?",
        "options": [
            {"text": "Miosis (pupillary constriction) and Constipation", "is_correct": True},
            {"text": "Analgesia and Euphoria", "is_correct": False},
            {"text": "Sedation and Drowsiness", "is_correct": False},
            {"text": "Respiratory depression and Nausea", "is_correct": False},
            {"text": "Antitussive effect and Pruritus", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Miosis (pupillary constriction) and Constipation.\n\nHigh-yield opioid tolerance concept:\n• Patients rapidly develop tolerance to analgesia, euphoria, sedation, respiratory depression, and nausea through receptor desensitization (GRK phosphorylation and beta-arrestin recruitment) and receptor downregulation.\n• However, tolerance does NOT develop to:\n  1. Miosis (pinpoint pupils via parasympathetic Edinger-Westphal nucleus outflow).\n  2. Constipation (inhibition of peristalsis and secretomotor transmission via myenteric and submucosal plexus opioid receptors in the GI tract).\n• Therefore, chronic opioid users always require prophylactic bowel regimens (stimulant laxatives and stool softeners) to prevent obstipation."
    },
    {
        "id": "FZ_Q269",
        "question_number": 269,
        "category": "Pathways and Opioids",
        "stem": "A 64-year-old man on chronic high-dose methadone for chronic back pain suffers from severe, refractory opioid-induced constipation (OIC) that has failed treatment with senna, docusate, and polyethylene glycol. The physician prescribes methylnaltrexone. Why does methylnaltrexone relieve constipation without reversing pain relief or precipitating opioid withdrawal?",
        "options": [
            {"text": "Methylnaltrexone contains a quaternary amine group with permanent positive charge, preventing it from crossing the blood-brain barrier", "is_correct": True},
            {"text": "Methylnaltrexone selectively antagonizes kappa-opioid receptors in the colon", "is_correct": False},
            {"text": "Methylnaltrexone is degraded into glucose in the stomach and never absorbed", "is_correct": False},
            {"text": "Methylnaltrexone stimulates smooth muscle motilin receptors exclusively", "is_correct": False},
            {"text": "Methylnaltrexone activates central mu-opioid receptors while blocking peripheral muscarinic receptors", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Methylnaltrexone contains a quaternary amine group with permanent positive charge, preventing it from crossing the blood-brain barrier.\n\nMethylnaltrexone (and naloxegol) are peripheral mu-opioid receptor antagonists (PAMORAs):\n• Methylnaltrexone has a methylated quaternary ammonium group, giving it a fixed positive ionic charge and high polarity. It cannot cross the lipid bilayer of the blood-brain barrier.\n• Consequently, it blocks mu-opioid receptors on the enteric nervous system (restoring intestinal motility and fluid secretion) without entering the CNS, completely preserving central opioid analgesia without precipitating central withdrawal."
    },
    {
        "id": "FZ_Q270",
        "question_number": 270,
        "category": "Pathways and Opioids",
        "stem": "A 23-year-old man is found unresponsive in an alleyway with shallow respirations of 4/min, heart rate of 52/min, blood pressure of 90/58 mmHg, and pinpoint pupils (1 mm bilaterally). Intravenous naloxone (0.4 mg) is administered, and within 90 seconds his respirations increase to 16/min and he awakens. Given naloxone's pharmacokinetic profile, why must this patient be closely monitored in the emergency department for several hours?",
        "options": [
            {"text": "Naloxone has a short elimination half-life (~30 to 90 minutes) and may be eliminated while longer-acting opioids remain active, leading to recurrent respiratory arrest ('renarcotization')", "is_correct": True},
            {"text": "Naloxone irreversibly inhibits hepatic CYP3A4, causing delayed accumulation of endogenous epinephrine", "is_correct": False},
            {"text": "Naloxone triggers delayed anaphylactic shock in >50% of patients after 3 hours", "is_correct": False},
            {"text": "Naloxone transforms into morphine-6-glucuronide via serum transaminases", "is_correct": False},
            {"text": "Naloxone induces permanent miosis that impairs neurological pupillary checks", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Naloxone has a short elimination half-life (~30 to 90 minutes) and may be eliminated while longer-acting opioids remain active, leading to recurrent respiratory arrest ('renarcotization').\n\nNaloxone kinetics and emergency management:\n• Naloxone is a competitive opioid antagonist with a rapid onset (1-2 minutes IV) but a short half-life of only ~30-90 minutes.\n• Most abused opioids (methadone, extended-release oxycodone, or fentanyl analogs) have elimination half-lives or active depot kinetics lasting many hours or days.\n• Once naloxone levels decline, uneliminated opioid molecules will reoccupy the vacated mu receptors, precipitating a lethal recurrence of respiratory depression ('renarcotization'). Patients must be observed for at least 2 to 4 hours (longer for methadone/ER formulations) and may require a continuous naloxone infusion."
    },
    {
        "id": "FZ_Q271",
        "question_number": 271,
        "category": "Pathways and Opioids",
        "stem": "A 30-year-old pregnant woman in labor is administered intravenous butorphanol for labor analgesia. What are the receptor properties of butorphanol, and what unique psychiatric adverse effect is associated with kappa-opioid receptor agonism?",
        "options": [
            {"text": "Kappa-receptor agonist and mu-receptor partial agonist/antagonist; kappa agonism produces dysphoria, hallucinations, and sedation", "is_correct": True},
            {"text": "Pure mu-receptor full agonist; kappa antagonism produces extreme euphoria", "is_correct": False},
            {"text": "Delta-receptor agonist and NMDA blocker; kappa agonism causes hyperthermia", "is_correct": False},
            {"text": "GABA-A positive allosteric modulator and mu antagonist; kappa agonism causes insomnia", "is_correct": False},
            {"text": "Selective CB1 receptor agonist; kappa agonism causes profound appetite stimulation", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Kappa-receptor agonist and mu-receptor partial agonist/antagonist; kappa agonism produces dysphoria, hallucinations, and sedation.\n\nMixed agonist-antagonists (Butorphanol, Pentazocine, Nalbuphine):\n• Kappa-opioid receptor: Agonist. Produces spinal analgesia, sedation, and decreases postoperative shivering, but kappa activation inhibits dopamine release in the nucleus accumbens, producing dysphoria, depersonalization, psychotomimetic reactions, and vivid nightmares.\n• Mu-opioid receptor: Antagonist or weak partial agonist. Causes less respiratory depression than full agonists (has a respiratory ceiling effect) but can precipitate acute withdrawal if administered to a patient dependent on full mu agonists."
    },
    {
        "id": "FZ_Q272",
        "question_number": 272,
        "category": "Pathways and Opioids",
        "stem": "Which of the following cellular mechanisms mediates the lethal effect of acute opioid overdose leading to hypoxemic brain injury and death?",
        "options": [
            {"text": "Direct suppression of the respiratory rhythm generator in the medullary pre-Bötzinger complex and blunting of brainstem chemoreceptor sensitivity to arterial hypercapnia (PaCO2)", "is_correct": True},
            {"text": "Massive coronary artery vasospasm causing transmural myocardial infarction", "is_correct": False},
            {"text": "Irreversible bronchoconstriction due to selective leukotriene D4 release", "is_correct": False},
            {"text": "Complete paralysis of the diaphragm due to blockade of nicotinic receptors at the motor end plate", "is_correct": False},
            {"text": "Rupture of pulmonary alveoli secondary to severe hypocapnia", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Direct suppression of the respiratory rhythm generator in the medullary pre-Bötzinger complex and blunting of brainstem chemoreceptor sensitivity to arterial hypercapnia (PaCO2).\n\nMechanisms of opioid-induced respiratory depression:\n• Mu-opioid receptors are densely concentrated in the pre-Bötzinger complex (the pacemaker of respiratory rhythm in the ventrolateral medulla) and the nucleus tractus solitarius.\n• Opioid activation hyperpolarizes these pacemaker neurons, decreasing respiratory frequency and tidal volume.\n• Crucially, opioids shift the carbon dioxide response curve to the right, blunting the respiratory drive in response to elevated arterial PaCO2. Ventilation drops, severe respiratory acidosis develops, and the patient ceases breathing entirely, culminating in fatal anoxic cardiac arrest."
    },
    {
        "id": "FZ_Q273",
        "question_number": 273,
        "category": "Pathways and Opioids",
        "stem": "A patient receives an intravenous bolus of morphine for severe acute trauma. Within 2 minutes, he develops intense facial flushing, warm skin, pruritus, mild bronchospasm, and a drop in blood pressure from 125/80 to 95/60 mmHg. Which mechanism explains this reaction, and does it represent an IgE-mediated type I hypersensitivity allergy?",
        "options": [
            {"text": "Non-immunologic direct mast cell degranulation with histamine release via MRGPRX2 receptor activation; not an IgE-mediated allergic reaction", "is_correct": True},
            {"text": "Classical type I IgE-mediated anaphylaxis requiring immediate lifelong avoidance of all opioids", "is_correct": False},
            {"text": "Type III immune complex deposition in dermal and pulmonary capillary beds", "is_correct": False},
            {"text": "Direct stimulation of vascular alpha-1 adrenergic receptors causing peripheral pooling", "is_correct": False},
            {"text": "Rapid inhibition of angiotensin-converting enzyme by morphine metabolites", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Non-immunologic direct mast cell degranulation with histamine release via MRGPRX2 receptor activation; not an IgE-mediated allergic reaction.\n\nMorphine, codeine, and meperidine stimulate mast cells directly through non-IgE pathways (specifically via the Mas-related G-protein-coupled receptor X2 [MRGPRX2]):\n• This triggers direct histamine exocytosis, causing localized or generalized flushing, pruritus, urticaria, bronchospasm, and mild hypotension.\n• This is a pseudoallergy (anaphylactoid reaction), not an IgE-mediated allergy. It can be pretreated with antihistamines or managed by switching to synthetic opioids (such as fentanyl), which do not trigger mast cell degranulation."
    },
    {
        "id": "FZ_Q274",
        "question_number": 274,
        "category": "Pathways and Opioids",
        "stem": "A 45-year-old man undergoing general anesthesia for coronary artery bypass graft surgery is administered an intravenous push of high-dose fentanyl. Moments later, the anesthesiologist finds that manual bag-valve-mask ventilation has become virtually impossible due to extreme, board-like chest wall and abdominal muscle rigidity. What is this phenomenon, and what is the immediate treatment of choice?",
        "options": [
            {"text": "Fentanyl-induced wooden chest syndrome (chest wall rigidity); treated immediately with a neuromuscular blocking agent (succinylcholine or rocuronium) or naloxone", "is_correct": True},
            {"text": "Malignant hyperthermia; treated immediately with intravenous dantrolene", "is_correct": False},
            {"text": "Tension pneumothorax; treated immediately with needle thoracostomy", "is_correct": False},
            {"text": "Acute bronchospasm; treated immediately with inhaled albuterol and epinephrine", "is_correct": False},
            {"text": "Status epilepticus; treated immediately with intravenous lorazepam", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Fentanyl-induced wooden chest syndrome (chest wall rigidity); treated immediately with a neuromuscular blocking agent (succinylcholine or rocuronium) or naloxone.\n\nFentanyl wooden chest syndrome:\n• Rapid intravenous administration of high-dose lipophilic synthetic opioids (fentanyl, sufentanil, remifentanil) can trigger acute chest wall and abdominal muscle rigidity mediated by central dopaminergic and GABAergic pathways in the striatum and locus coeruleus.\n• The chest wall becomes board-like, preventing thoracic expansion and rendering bag-mask ventilation or mechanical ventilation impossible.\n• Immediate management: Neuromuscular blocking agents (e.g., succinylcholine) to paralyze skeletal muscle, or intravenous naloxone to reverse opioid action, allowing prompt endotracheal intubation and ventilation."
    },
    {
        "id": "FZ_Q275",
        "question_number": 275,
        "category": "Pathways and Opioids",
        "stem": "A 38-year-old woman is prescribed tramadol for moderate neuropathic pain after lumbar spine surgery. Which dual mechanism of action explains the analgesic efficacy of tramadol?",
        "options": [
            {"text": "Weak mu-opioid receptor agonism combined with neuronal reuptake inhibition of norepinephrine (NET) and serotonin (SERT)", "is_correct": True},
            {"text": "Potent kappa-opioid receptor agonism and selective COX-2 inhibition", "is_correct": False},
            {"text": "Direct opening of GABA-A chloride channels and blockade of substance P receptors", "is_correct": False},
            {"text": "Selective CB2 receptor agonism and inhibition of phosphodiesterase-5", "is_correct": False},
            {"text": "Irreversible inhibition of voltage-gated calcium channels without any opioid receptor binding", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Weak mu-opioid receptor agonism combined with neuronal reuptake inhibition of norepinephrine (NET) and serotonin (SERT).\n\nTramadol mechanism:\n1. Mu-opioid activity: Tramadol itself has very low affinity for mu receptors, but its hepatic CYP2D6 metabolite (O-desmethyltramadol / M1) is a significant mu-agonist with ~300x higher affinity.\n2. Monoamine reuptake inhibition: The parent compound inhibits both norepinephrine transporter (NET) and serotonin transporter (SERT) reuptake, enhancing endogenous descending inhibitory pain pathways in the spinal dorsal horn.\n• High-yield risks: Tramadol lowers the seizure threshold and carries a significant risk of Serotonin Syndrome when combined with other serotonergic medications."
    },
    {
        "id": "FZ_Q276",
        "question_number": 276,
        "category": "Pathways and Opioids",
        "stem": "A 10-year-old boy undergoes adenotonsillectomy for obstructive sleep apnea. Postoperatively, he is prescribed liquid codeine for pain control. Within 12 hours of discharge, the child becomes unarousable and is found in cardiac arrest secondary to severe respiratory depression. Genetic testing reveals that the patient is a CYP2D6 'ultra-rapid metabolizer.' What pharmacokinetic explanation accounts for this tragedy?",
        "options": [
            {"text": "Codeine is an inactive prodrug that requires CYP2D6 O-demethylation to become morphine; ultra-rapid metabolizers rapidly convert therapeutic doses of codeine into massive, lethal systemic levels of morphine", "is_correct": True},
            {"text": "CYP2D6 ultra-rapid metabolizers fail to break down codeine, causing toxic accumulation of unchanged codeine", "is_correct": False},
            {"text": "Codeine directly destroys pulmonary alveolar type II pneumocytes in patients with CYP2D6 duplications", "is_correct": False},
            {"text": "CYP2D6 converts codeine directly into cyanide in pediatric hepatocytes", "is_correct": False},
            {"text": "Codeine blocks the child's endogenous endorphin receptors irreversibly", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Codeine is an inactive prodrug that requires CYP2D6 O-demethylation to become morphine; ultra-rapid metabolizers rapidly convert therapeutic doses of codeine into massive, lethal systemic levels of morphine.\n\nCodeine pharmacogenomics:\n• Codeine has virtually no intrinsic analgesic activity (10-carbon methyl ether of morphine). It is a prodrug requiring hepatic CYP2D6 to undergo O-demethylation into active morphine (~10% of dose under normal conditions).\n• Individuals with multiple functional gene copies of CYP2D6 (ultra-rapid metabolizers, ~1-10% of Caucasians and up to 29% of Ethiopians/Middle Easterners) convert codeine into dangerously high concentrations of morphine rapidly.\n• In children following tonsillectomy, this produces fatal respiratory arrest. The FDA has issued a black box warning strictly contraindicating codeine and tramadol in children under 12."
    },
    {
        "id": "FZ_Q277",
        "question_number": 277,
        "category": "Pathways and Opioids",
        "stem": "An over-the-counter antidiarrheal medication, loperamide, is a potent mu-opioid receptor agonist. Why does loperamide relieve diarrhea without producing central analgesia, euphoria, or respiratory depression at standard therapeutic doses?",
        "options": [
            {"text": "Loperamide has poor oral bioavailability and is actively transported out of the brain back into the capillary lumen by P-glycoprotein (MDR1) efflux transporters at the blood-brain barrier", "is_correct": True},
            {"text": "Loperamide binds exclusively to kappa receptors and completely lacks mu receptor activity", "is_correct": False},
            {"text": "Loperamide is completely degraded by gastric acid into inactive amino acids", "is_correct": False},
            {"text": "Loperamide does not bind opioid receptors and works entirely as an osmotic laxative antagonist", "is_correct": False},
            {"text": "Loperamide binds to albumin so tightly that it never dissociates in systemic tissues", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Loperamide has poor oral bioavailability and is actively transported out of the brain back into the capillary lumen by P-glycoprotein (MDR1) efflux transporters at the blood-brain barrier.\n\nLoperamide pharmacology:\n• Loperamide binds to mu-opioid receptors on the myenteric plexus of the gastrointestinal tract, decreasing circular and longitudinal muscle peristalsis and prolonging transit time.\n• Although it is a potent mu-agonist, any small amount that crosses the blood-brain barrier is immediately recognized and extruded back into the bloodstream by the P-glycoprotein (MDR1 / ABCB1) efflux transporter on brain capillary endothelial cells.\n• Note: Massive supra-therapeutic doses ('poor man's methadone') or co-administration with P-glycoprotein inhibitors (e.g., quinidine) can overwhelm the transporter, leading to central opioid toxicity and lethal cardiac arrhythmias (QT prolongation and QRS widening)."
    },
    {
        "id": "FZ_Q278",
        "question_number": 278,
        "category": "Pathways and Opioids",
        "stem": "Which of the following medications is a non-opioid, centrally acting antitussive (cough suppressant) that functions as an NMDA receptor antagonist and sigma-1 receptor agonist without producing significant mu-opioid analgesia?",
        "options": [
            {"text": "Dextromethorphan", "is_correct": True},
            {"text": "Diphenoxylate", "is_correct": False},
            {"text": "Hydromorphone", "is_correct": False},
            {"text": "Naltrexone", "is_correct": False},
            {"text": "Buprenorphine", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Dextromethorphan.\n\nDextromethorphan is the D-isomer of the codeine analog levorphanol:\n• Mechanism: Antagonizes NMDA glutamate receptors and acts as a sigma-1 receptor agonist in the medullary cough center, suppressing the cough reflex.\n• Unlike the L-isomer (levorphanol), it has negligible affinity for mu or kappa opioid receptors and does not produce analgesia or physical dependence at therapeutic doses.\n• At high recreational doses ('dexing', 'robo-tripping'), it acts as a dissociative hallucinogen similar to ketamine and PCP, and inhibits serotonin reuptake (risking serotonin syndrome)."
    },
    {
        "id": "FZ_Q279",
        "question_number": 279,
        "category": "Pathways and Opioids",
        "stem": "Which physiological mechanism is primarily responsible for the development of cellular and molecular tolerance to chronic opioid therapy at the level of the mu-opioid receptor?",
        "options": [
            {"text": "G-protein coupled receptor kinase (GRK) phosphorylation of the receptor, leading to beta-arrestin binding, receptor uncoupling from G-proteins, and receptor endocytosis", "is_correct": True},
            {"text": "Autoimmune antibody formation against mu-opioid receptors", "is_correct": False},
            {"text": "Permanent covalent cross-linking of the receptor to presynaptic SNARE complexes", "is_correct": False},
            {"text": "Exhaustion of vesicular calcium stores in the postsynaptic dendrite", "is_correct": False},
            {"text": "Complete enzymatic destruction of spinal dynorphin by microglial proteases", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. G-protein coupled receptor kinase (GRK) phosphorylation of the receptor, leading to beta-arrestin binding, receptor uncoupling from G-proteins, and receptor endocytosis.\n\nMolecular mechanism of opioid tolerance:\n1. Agonist binding causes G-protein coupled receptor kinases (GRK2/GRK3) to phosphorylate serine and threonine residues on the C-terminal tail of the mu-opioid receptor.\n2. Beta-arrestin is recruited to the phosphorylated receptor, physically blocking further interaction with Gi/o heterotrimeric G-proteins (receptor desensitization).\n3. Beta-arrestin targets the receptor to clathrin-coated pits for internalization (endocytosis). Receptors are either degraded in lysosomes (downregulation) or dephosphorylated and recycled.\n4. Concurrently, chronic Gi inhibition leads to compensatory upregulation of adenylyl cyclase (cAMP superactivation), requiring larger opioid doses to achieve the same inhibitory effect."
    },
    {
        "id": "FZ_Q280",
        "question_number": 280,
        "category": "Pathways and Opioids",
        "stem": "A 32-year-old man who abruptly discontinued heroin 18 hours ago presents with severe dysphoria, diarrhea, rhinorrhea, lacrimation, piloerection ('goosebumps'), yawning, muscle spasms, and pupillary dilation. Which brainstem nucleus is the primary site of noradrenergic hyperactivity driving these autonomic manifestations of opioid withdrawal?",
        "options": [
            {"text": "Locus coeruleus", "is_correct": True},
            {"text": "Substantia nigra pars compacta", "is_correct": False},
            {"text": "Nucleus basalis of Meynert", "is_correct": False},
            {"text": "Edinger-Westphal nucleus", "is_correct": False},
            {"text": "Inferior olivary nucleus", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Locus coeruleus.\n\nPathophysiology of opioid withdrawal:\n• The locus coeruleus (located in the dorsal rostral pons) is the primary noradrenergic center in the brain.\n• Under normal conditions, chronic opioid use suppresses locus coeruleus firing via Gi-coupled mu receptors, prompting homeostatic upregulation of cAMP and PKA.\n• When opioids are abruptly removed, the disinhibited locus coeruleus fires wildly, causing massive release of norepinephrine throughout the brain and spinal cord.\n• This noradrenergic storm drives acute withdrawal symptoms: tachycardia, hypertension, diaphoresis, piloerection (origin of 'cold turkey'), mydriasis, hyperreflexia, and anxiety.\n• Clonidine (a central alpha-2 adrenergic agonist) dampens locus coeruleus outflow and is standard non-opioid treatment for withdrawal symptoms."
    },

    # =========================================================================
    # TOPIC 15: Traumatic Brain Injuries (FZ_Q281 - FZ_Q300)
    # =========================================================================
    {
        "id": "FZ_Q281",
        "question_number": 281,
        "category": "Traumatic Brain Injuries",
        "stem": "A 21-year-old baseball player is struck directly in the right temple by a fastball. He loses consciousness for 30 seconds, awakens fully alert and conversant with a Glasgow Coma Scale score of 15, and insists he is fine. Two hours later in the dugout, he develops an excruciating headache, vomits, and rapidly lapses into an unarousable coma with a blown, fixed right pupil. A non-contrast head CT will most likely demonstrate which characteristic finding?",
        "options": [
            {"text": "Biconvex (lenticular), hyperdense extra-axial collection that does not cross cranial suture lines", "is_correct": True},
            {"text": "Crescent-shaped (concave-convex), hyperdense extra-axial collection that crosses cranial suture lines", "is_correct": False},
            {"text": "Hyperdensity filling the basal cisterns, sylvian fissures, and cerebral sulci", "is_correct": False},
            {"text": "Punctate microhemorrhages at the gray-white matter junction and splenium of the corpus callosum", "is_correct": False},
            {"text": "Hypodense wedge-shaped lesion confined to the middle cerebral artery territory", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Biconvex (lenticular), hyperdense extra-axial collection that does not cross cranial suture lines.\n\nEpidural Hematoma (EDH):\n• Classic presentation: Blow to the pterion (temporal bone) -> brief loss of consciousness -> 'lucid interval' (hours of normal neurological function) -> rapid secondary neurological deterioration as arterial bleeding expands.\n• Mechanism: Laceration of the middle meningeal artery (a branch of the maxillary artery entering via foramen spinosum).\n• Radiologic hallmark: Biconvex (lenticular or 'lemon-shaped') hyperdense extra-axial hematoma. Because the outer periosteal layer of the dura mater is tightly anchored to the skull at the cranial sutures, the expanding arterial blood cannot cross suture lines, causing it to push inward against the brain parenchyma.\n• The fixed, dilated right pupil indicates ipsilateral uncal herniation with compression of CN III."
    },
    {
        "id": "FZ_Q282",
        "question_number": 282,
        "category": "Traumatic Brain Injuries",
        "stem": "An 82-year-old woman with mild cognitive impairment and chronic balance issues presents with 3 weeks of insidious, worsening morning headaches, progressive confusion, and unsteady gait. Her family recalls she had a minor fall from a chair a month ago without loss of consciousness. Non-contrast head CT reveals a crescent-shaped, hypodense extra-axial fluid collection along the left cerebral convexity that crosses cranial suture lines. What vascular structure is the source of this hemorrhage?",
        "options": [
            {"text": "Bridging cortical veins draining into the superior sagittal sinus", "is_correct": True},
            {"text": "Middle meningeal artery", "is_correct": False},
            {"text": "Ruptured saccular aneurysm of the anterior communicating artery", "is_correct": False},
            {"text": "Charcot-Bouchard microaneurysm in the lenticulostriate arteries", "is_correct": False},
            {"text": "Cavernous portion of the internal carotid artery", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Bridging cortical veins draining into the superior sagittal sinus.\n\nChronic Subdural Hematoma (SDH):\n• Mechanism: Tearing of the bridging cortical veins that traverse the subdural space from the cerebral cortex to drain into the superior sagittal sinus.\n• Predisposing factors: Cerebral cortical atrophy (seen in the elderly and chronic alcoholism) increases the distance between the brain surface and the dural sinuses, stretching the fragile bridging veins so that even minor head trauma can shear them.\n• Radiologic features: Crescent-shaped (concave-convex or 'banana-shaped') extra-axial collection. Because blood accumulates between the dura and arachnoid, it is not restricted by cranial sutures and can cross suture lines (limited only by dural reflections like the falx cerebri).\n• Chronology on CT: Acute = hyperdense (bright); Subacute = isodense; Chronic (>2-3 weeks) = hypodense (dark) due to hemoglobin degradation."
    },
    {
        "id": "FZ_Q283",
        "question_number": 283,
        "category": "Traumatic Brain Injuries",
        "stem": "A 25-year-old unrestrained driver involved in a high-speed rollover motor vehicle collision arrives comatose with a Glasgow Coma Scale of 4. Emergency non-contrast head CT shows no skull fractures, no mass lesions, and no epidural or subdural hematomas, with only tiny punctate hyperdensities at the corticomedullary junction. However, susceptibility-weighted MRI (SWI) reveals extensive, widespread blooming artifact and microhemorrhages throughout the gray-white matter junction, corpus callosum (splenium), and dorsolateral midbrain. What is the diagnosis?",
        "options": [
            {"text": "Diffuse axonal injury (DAI)", "is_correct": True},
            {"text": "Fat embolism syndrome", "is_correct": False},
            {"text": "Global cerebral ischemia secondary to cardiac arrest", "is_correct": False},
            {"text": "Acute disseminated encephalomyelitis (ADEM)", "is_correct": False},
            {"text": "Cerebral venous sinus thrombosis", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Diffuse axonal injury (DAI).\n\nDiffuse Axonal Injury (DAI):\n• Mechanism: High-velocity angular or rotational acceleration-deceleration forces that cause rapid deformation, stretching, and shearing of long axonal tracts at boundaries between tissues of differing densities (gray-white matter junction, splenium of corpus callosum, rostral brainstem).\n• Clinical picture: Severe, immediate coma without a lucid interval and without a focal surgical mass lesion on initial CT. It is the most common cause of persistent coma and vegetative state following closed head trauma.\n• Imaging: Routine non-contrast CT is frequently normal or shows only subtle petechiae. MRI (especially GRE or Susceptibility-Weighted Imaging [SWI]) is vastly superior, demonstrating widespread hypointense punctate foci with 'blooming artifact' from microscopic hemosiderin deposition.\n• Histology: Axonal retraction balls (spheroids) and positive immunohistochemical staining for beta-amyloid precursor protein (beta-APP), which accumulates due to disrupted anterograde axonal transport."
    },
    {
        "id": "FZ_Q284",
        "question_number": 284,
        "category": "Traumatic Brain Injuries",
        "stem": "A 35-year-old construction worker falls 15 feet from scaffolding, landing on his head. On examination, he has ecchymosis behind his left ear over the mastoid process ('Battle sign'), bilateral periorbital ecchymosis ('raccoon eyes'), clear, watery fluid draining from his left ear, and hemotympanum. Which type of skull fracture does this patient have?",
        "options": [
            {"text": "Basilar skull fracture involving the petrous temporal bone", "is_correct": True},
            {"text": "Depressed frontal calvarial fracture", "is_correct": False},
            {"text": "Linear sagittal suture fracture", "is_correct": False},
            {"text": "Isolated orbital blowout fracture of the maxillary sinus floor", "is_correct": False},
            {"text": "Zygomaticomaxillary complex fracture", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Basilar skull fracture involving the petrous temporal bone.\n\nBasilar Skull Fracture:\n• Fractures involving the floor of the cranial vault (most commonly the petrous portion of the temporal bone, followed by orbital plate of frontal bone and cribriform plate of ethmoid).\n• Classical signs:\n  1. Battle sign: Postauricular ecchymosis over the mastoid process (indicates temporal bone fracture).\n  2. Raccoon eyes: Periorbital ecchymosis without direct facial eye trauma (indicates anterior cranial fossa fracture).\n  3. CSF rhinorrhea or CSF otorrhea: Clear drainage due to dural laceration (confirmed by testing for beta-2 transferrin, a protein unique to CSF).\n  4. Hemotympanum: Blood behind the tympanic membrane.\n  5. Cranial nerve palsies: Particularly CN VII (facial palsy) and CN VIII (sensorineural hearing loss/vertigo), which traverse the internal acoustic meatus of the petrous temporal bone."
    },
    {
        "id": "FZ_Q285",
        "question_number": 285,
        "category": "Traumatic Brain Injuries",
        "stem": "A 19-year-old snowboarder strikes a tree, sustaining severe cranial trauma. On arrival at the trauma center, his vital signs are blood pressure 195/105 mmHg, heart rate 44/min, and irregular, slow, gasping respirations (6/min). Pupils are unequal. This clinical constellation (hypertension with widened pulse pressure, bradycardia, and irregular respirations) is known as Cushing's triad. What pathophysiological crisis does Cushing's triad signify?",
        "options": [
            {"text": "Life-threatening intracranial hypertension with imminent brainstem herniation", "is_correct": True},
            {"text": "Hypovolemic hemorrhagic shock secondary to internal bleeding", "is_correct": False},
            {"text": "Neurogenic shock secondary to complete high cervical spinal cord transection", "is_correct": False},
            {"text": "Cardiac tamponade secondary to blunt thoracic trauma", "is_correct": False},
            {"text": "Thyroid storm triggered by physical trauma", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Life-threatening intracranial hypertension with imminent brainstem herniation.\n\nCushing Triad (Cushing Reflex):\n• Physiologic response to dangerously elevated intracranial pressure (ICP) that compromises cerebral perfusion pressure (CPP = MAP - ICP):\n  1. Hypertension (with widened pulse pressure): Severe brainstem ischemia triggers a massive central sympathetic discharge, constricting peripheral arterioles to raise MAP in a desperate attempt to restore cerebral blood flow.\n  2. Bradycardia: The severe hypertension stimulates carotid sinus and aortic arch baroreceptors, triggering compensatory parasympathetic vagal output that slows the heart rate.\n  3. Irregular respirations (Cheyne-Stokes or ataxic breathing): Increased ICP causes mechanical compression and ischemia of the medullary respiratory centers.\n• Cushing's triad is a late, ominous sign of impending brainstem herniation requiring emergency neurosurgical intervention and hyperosmolar therapy."
    },
    {
        "id": "FZ_Q286",
        "question_number": 286,
        "category": "Traumatic Brain Injuries",
        "stem": "An unconscious patient with an expanding right-sided epidural hematoma exhibits an uncal herniation. The medial temporal lobe uncus herniates inferiorly past the tentorium cerebelli. Which cranial nerve and which cerebral arterial territory are typically compressed first by this herniating mass?",
        "options": [
            {"text": "Ipsilateral Oculomotor nerve (CN III) and Posterior cerebral artery (PCA)", "is_correct": True},
            {"text": "Contralateral Abducens nerve (CN VI) and Middle cerebral artery (MCA)", "is_correct": False},
            {"text": "Bilateral Optic nerves (CN II) and Anterior cerebral artery (ACA)", "is_correct": False},
            {"text": "Ipsilateral Trochlear nerve (CN IV) and Basilar artery", "is_correct": False},
            {"text": "Contralateral Trigeminal nerve (CN V) and Superior cerebellar artery (SCA)", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Ipsilateral Oculomotor nerve (CN III) and Posterior cerebral artery (PCA).\n\nUncal (Transtentorial) Herniation:\n• The uncus of the medial temporal lobe is displaced medially and inferiorly through the tentorial notch (incisura):\n  1. Compression of ipsilateral CN III: Parasympathetic pupillomotor fibers run superficially on the outer dorsomedial surface of CN III. Compression causes early loss of parasympathetic tone -> ipsilateral 'blown,' dilated, non-reactive pupil, followed later by somatic motor paralysis ('down-and-out' eye with ptosis).\n  2. Compression of ipsilateral Posterior Cerebral Artery (PCA): Causes ischemia and infarction of the ipsilateral occipital lobe -> contralateral homonymous hemianopia (with macular sparing).\n  3. Compression of ipsilateral cerebral peduncle (corticospinal tract): Produces contralateral hemiparesis."
    },
    {
        "id": "FZ_Q287",
        "question_number": 287,
        "category": "Traumatic Brain Injuries",
        "stem": "In severe uncal herniation, the expanding supratentorial mass may displace the midbrain laterally across the tentorial notch, causing the CONTRALATERAL cerebral peduncle to be compressed against the hard, free edge of the tentorium. What is this classic clinical phenomenon called, and what misleading neurological sign does it produce?",
        "options": [
            {"text": "Kernohan notch phenomenon, producing a false-localizing IPSILATERAL hemiparesis", "is_correct": True},
            {"text": "Duret hemorrhage, producing bilateral cranial nerve IV palsies", "is_correct": False},
            {"text": "Parinaud syndrome, producing loss of downward gaze", "is_correct": False},
            {"text": "Brown-Séquard syndrome, producing contralateral loss of vibration sense", "is_correct": False},
            {"text": "Wallenberg syndrome, producing contralateral facial numbness", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Kernohan notch phenomenon, producing a false-localizing IPSILATERAL hemiparesis.\n\nKernohan Notch Phenomenon:\n• Normally, a right-sided mass compressing the right cerebral peduncle causes contralateral (left-sided) hemiparesis.\n• However, if the brainstem is pushed violently to the opposite side, the left (contralateral) cerebral peduncle is forced against the sharp, rigid edge of the tentorium cerebelli (the Kernohan notch).\n• Because the left corticospinal tract decussates in the caudal medulla below, damage to the left cerebral peduncle causes weakness on the right side of the body—which is the same (ipsilateral) side as the original mass lesion!\n• This is a famous 'false-localizing' sign: the patient has an ipsilateral dilated pupil and ipsilateral hemiparesis."
    },
    {
        "id": "FZ_Q288",
        "question_number": 288,
        "category": "Traumatic Brain Injuries",
        "stem": "A neurocritical care physician is calculating the Glasgow Coma Scale (GCS) score for a patient who suffered a severe traumatic brain injury. On examination: the patient opens his eyes only in response to a painful sternal rub (2 points); utters incomprehensible moans and groans (2 points); and demonstrates decorticate abnormal flexion posturing of his upper extremities to pain (3 points). What is this patient's total Glasgow Coma Scale score?",
        "options": [
            {"text": "7", "is_correct": True},
            {"text": "3", "is_correct": False},
            {"text": "5", "is_correct": False},
            {"text": "9", "is_correct": False},
            {"text": "11", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. 7.\n\nGlasgow Coma Scale (GCS) scoring breakdown (range 3 to 15):\n• Eye Opening (E, max 4):\n  4 = Spontaneous; 3 = To verbal command; 2 = To pain; 1 = None. (Patient = 2)\n• Verbal Response (V, max 5):\n  5 = Oriented; 4 = Confused; 3 = Inappropriate words; 2 = Incomprehensible sounds (moans); 1 = None. (Patient = 2)\n• Motor Response (M, max 6):\n  6 = Obeys commands; 5 = Localizes pain; 4 = Normal flexion/withdrawal; 3 = Abnormal flexion (decorticate posturing); 2 = Extension (decerebrate posturing); 1 = None. (Patient = 3)\n• Total GCS = E (2) + V (2) + M (3) = 7.\n• A GCS score of ≤8 defines severe traumatic brain injury (coma) and is an immediate indication for endotracheal intubation ('GCS less than 8, intubate')."
    },
    {
        "id": "FZ_Q289",
        "question_number": 289,
        "category": "Traumatic Brain Injuries",
        "stem": "A comatose patient in the neurotrauma ICU exhibits abnormal posturing in response to noxious stimulation. She presents with adduction of both upper arms, flexion of the elbows, wrists, and fingers against her chest, along with extension, internal rotation, and plantarflexion of both lower extremities. What type of posturing is this, and where is the anatomical lesion located?",
        "options": [
            {"text": "Decorticate posturing; lesion above the red nucleus (cerebral hemispheres or internal capsule), with intact rubrospinal and vestibulospinal tracts", "is_correct": True},
            {"text": "Decerebrate posturing; lesion below the red nucleus involving the midbrain or upper pons", "is_correct": False},
            {"text": "Flaccid paralysis; complete transection of the lower cervical spinal cord", "is_correct": False},
            {"text": "Chorea; bilateral infarction of the caudate nuclei", "is_correct": False},
            {"text": "Hemiballismus; unilateral lesion of the subthalamic nucleus", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Decorticate posturing; lesion above the red nucleus (cerebral hemispheres or internal capsule), with intact rubrospinal and vestibulospinal tracts.\n\nComparison of posturing:\n• Decorticate posturing (Flexor posturing): Arms flexed ('like holding core/chest'), legs extended.\n  - Lesion level: Supratentorial / rostral to the red nucleus (cortex, internal capsule, thalamus).\n  - Pathophysiology: Loss of descending corticospinal inhibition, but the midbrain red nucleus remains intact. The rubrospinal tract facilitates upper extremity flexor tone, while the lateral vestibulospinal tract facilitates lower extremity extensor tone.\n• Decerebrate posturing (Extensor posturing): Arms extended, pronated, and adducted; legs extended. Lesion is caudal to the red nucleus (midbrain below superior colliculus or rostral pons). The rubrospinal tract is destroyed, leaving the vestibulospinal tract unopposed -> global extension. Decerebrate posturing carries a worse prognosis."
    },
    {
        "id": "FZ_Q290",
        "question_number": 290,
        "category": "Traumatic Brain Injuries",
        "stem": "A 28-year-old man with severe traumatic brain injury has an intracranial pressure (ICP) monitor placed. His ICP is elevated at 28 mmHg (normal <15 mmHg). His mean arterial pressure (MAP) is 88 mmHg. What is this patient's Cerebral Perfusion Pressure (CPP), and what is the target CPP range recommended by traumatic brain injury guidelines?",
        "options": [
            {"text": "CPP = 60 mmHg; target range is 60 to 70 mmHg", "is_correct": True},
            {"text": "CPP = 116 mmHg; target range is 100 to 120 mmHg", "is_correct": False},
            {"text": "CPP = 3.1 mmHg; target range is 1 to 5 mmHg", "is_correct": False},
            {"text": "CPP = 35 mmHg; target range is 30 to 40 mmHg", "is_correct": False},
            {"text": "CPP = 88 mmHg; target range is 80 to 90 mmHg", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. CPP = 60 mmHg; target range is 60 to 70 mmHg.\n\nCerebral Perfusion Pressure (CPP) equation:\n• CPP = Mean Arterial Pressure (MAP) - Intracranial Pressure (ICP)\n• Calculation: CPP = 88 mmHg - 28 mmHg = 60 mmHg.\n• Clinical management: Brain Trauma Foundation guidelines recommend maintaining CPP between 60 and 70 mmHg in adults with severe TBI.\n  - CPP <60 mmHg increases the risk of cerebral ischemia and secondary brain infarction.\n  - Aggressive elevation of CPP >70 mmHg with vasopressors is avoided because it increases the risk of acute respiratory distress syndrome (ARDS) and vasogenic cerebral edema."
    },
    {
        "id": "FZ_Q291",
        "question_number": 291,
        "category": "Traumatic Brain Injuries",
        "stem": "Which fundamental neurophysiological principle states that the cranium is a rigid, non-expansile vault containing brain parenchyma (~80%), blood (~10%), and cerebrospinal fluid (~10%), meaning that any increase in the volume of one constituent must be compensated by an equal reduction in the volume of another to prevent a dramatic rise in intracranial pressure?",
        "options": [
            {"text": "Monro-Kellie doctrine", "is_correct": True},
            {"text": "Frank-Starling law", "is_correct": False},
            {"text": "Cushing reflex", "is_correct": False},
            {"text": "Bernoulli principle", "is_correct": False},
            {"text": "Fick's law of diffusion", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Monro-Kellie doctrine.\n\nThe Monro-Kellie Doctrine (hypothesis):\n• The cranial compartment is an inelastic closed box with a fixed total volume.\n• Total intracranial volume = Volume(brain) + Volume(blood) + Volume(CSF) = Constant.\n• When a mass lesion expands (e.g., epidural hematoma):\n  1. Initial compensation: CSF is displaced into the spinal subarachnoid space and venous blood is shunted into extracranial jugular veins. ICP remains relatively normal during this compensable phase.\n  2. Decompensation: Once compensatory mechanisms are exhausted, further minor increases in mass volume cause an exponential, steep rise in ICP, leading to cerebral herniation and ischemia."
    },
    {
        "id": "FZ_Q292",
        "question_number": 292,
        "category": "Traumatic Brain Injuries",
        "stem": "In the acute medical management of critically elevated intracranial pressure (ICP >25 mmHg) with impending herniation, an intubated patient is temporarily hyperventilated to lower PaCO2. What is the physiological mechanism and recommended target PaCO2 range for therapeutic hyperventilation?",
        "options": [
            {"text": "Hypocapnia causes cerebral arteriolar vasoconstriction, reducing cerebral blood volume; target PaCO2 is 30 to 35 mmHg as a temporary bridge", "is_correct": True},
            {"text": "Hypercapnia dilates cerebral arterioles; target PaCO2 is 55 to 60 mmHg", "is_correct": False},
            {"text": "Severe alkalosis directly opens arachnoid granulations; target PaCO2 is <20 mmHg indefinitely", "is_correct": False},
            {"text": "Hypocapnia increases systemic venous return to augment cardiac output; target PaCO2 is 40 to 45 mmHg", "is_correct": False},
            {"text": "Hypocapnia precipitates microglial apoptosis to halt neuroinflammation; target PaCO2 is 15 to 20 mmHg", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Hypocapnia causes cerebral arteriolar vasoconstriction, reducing cerebral blood volume; target PaCO2 is 30 to 35 mmHg as a temporary bridge.\n\nMechanisms of therapeutic hyperventilation in high ICP:\n• Cerebral arterioles are exquisitely sensitive to arterial carbon dioxide (PaCO2):\n  - Hypercapnia (high CO2) -> cerebral vasodilation -> increases cerebral blood flow and blood volume -> spikes ICP.\n  - Hypocapnia (low CO2) -> increases perivascular pH -> cerebral vasoconstriction -> decreases cerebral blood volume -> rapidly lowers ICP.\n• Clinical rule: Hyperventilation to a target PaCO2 of 30-35 mmHg must only be used as a short-term, temporary bridge during acute herniation crises or while preparing for surgical decompression. Excessive or prolonged hyperventilation (PaCO2 <30 mmHg) causes severe vasoconstriction that leads to profound secondary cerebral ischemia and infarction."
    },
    {
        "id": "FZ_Q293",
        "question_number": 293,
        "category": "Traumatic Brain Injuries",
        "stem": "Which of the following osmotic agents is administered intravenously to treat acute intracranial hypertension by creating an osmolar gradient that draws water out of edematous brain parenchymal cells across an intact blood-brain barrier into the vascular compartment?",
        "options": [
            {"text": "Mannitol or 3% Hypertonic Saline", "is_correct": True},
            {"text": "5% Dextrose in Water (D5W)", "is_correct": False},
            {"text": "0.45% Half-Normal Saline", "is_correct": False},
            {"text": "Lactated Ringer's solution with potassium chloride", "is_correct": False},
            {"text": "Intravenous Albumin 5%", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Mannitol or 3% Hypertonic Saline.\n\nHyperosmolar therapy for elevated ICP:\n1. Mannitol: An impermeable polyol sugar alcohol administered as an IV bolus (0.25 to 1 g/kg). It elevates serum osmolality, establishing an osmotic gradient that extracts water from the cerebral parenchyma into the intravascular space, where it is excreted by the kidneys. It also expands circulating plasma volume and lowers blood viscosity, enhancing microvascular cerebral blood flow. (Must monitor serum osmolality; hold if >320 mOsm/kg).\n2. Hypertonic saline (3% or 23.4% NaCl): Acts via an identical osmotic mechanism and does not cause profound hypovolemic diuresis like mannitol.\n• Hypotonic fluids (e.g., D5W, 0.45% NS) are strictly contraindicated because free water readily crosses the blood-brain barrier, worsening cerebral edema and precipitating fatal herniation."
    },
    {
        "id": "FZ_Q294",
        "question_number": 294,
        "category": "Traumatic Brain Injuries",
        "stem": "A 40-year-old pedestrian is struck by an automobile, sustaining severe blunt trauma. Non-contrast CT of the head reveals a subfalcine (cingulate) herniation, in which the cingulate gyrus is pushed underneath the falx cerebri from right to left across the midline. Which major intracranial artery is compressed against the free edge of the falx in subfalcine herniation, and what clinical deficit results?",
        "options": [
            {"text": "Anterior cerebral artery (ACA), causing contralateral lower extremity weakness and sensory loss", "is_correct": True},
            {"text": "Middle cerebral artery (MCA), causing contralateral facial and upper extremity weakness", "is_correct": False},
            {"text": "Posterior cerebral artery (PCA), causing contralateral homonymous hemianopia", "is_correct": False},
            {"text": "Basilar artery, causing 'locked-in' syndrome", "is_correct": False},
            {"text": "Posterior inferior cerebellar artery (PICA), causing lateral medullary syndrome", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Anterior cerebral artery (ACA), causing contralateral lower extremity weakness and sensory loss.\n\nSubfalcine (Cingulate) Herniation:\n• The cingulate gyrus of one hemisphere is displaced across the midline beneath the rigid, sickle-shaped falx cerebri.\n• Complication: The ipsilateral Anterior Cerebral Artery (ACA) runs in the longitudinal fissure adjacent to the cingulate gyrus and is compressed against the falx.\n• Clinical result: Ischemia and infarction in the ACA territory (medial surface of the frontal and parietal lobes). Because the sensory and motor homunculus for the lower extremity resides in the paracentral lobule on the medial cortical surface, ACA infarction causes contralateral leg/foot weakness and sensory loss, along with abulia or frontal lobe release signs."
    },
    {
        "id": "FZ_Q295",
        "question_number": 295,
        "category": "Traumatic Brain Injuries",
        "stem": "An elderly patient with acute epidural hematoma rapidly deteriorates. Autopsy reveals linear, flame-shaped secondary hemorrhages within the midline paramedian tegmentum of the upper pons and midbrain. What are these fatal brainstem hemorrhages called, and what herniation event produces them?",
        "options": [
            {"text": "Duret hemorrhages secondary to central downward transtentorial herniation", "is_correct": True},
            {"text": "Charcot-Bouchard hemorrhages secondary to chronic essential hypertension", "is_correct": False},
            {"text": "Petechial petrosal hemorrhages secondary to basilar invagination", "is_correct": False},
            {"text": "Spicer hemorrhages secondary to superior cerebellar tonsillar herniation", "is_correct": False},
            {"text": "Kimmelstiel hemorrhages secondary to diabetic microangiopathy", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Duret hemorrhages secondary to central downward transtentorial herniation.\n\nDuret Hemorrhages:\n• Secondary small, linear hemorrhages in the midbrain and upper pons.\n• Pathogenesis: Caused by severe downward central or uncal transtentorial herniation. As the cerebral hemispheres and diencephalon are forced caudalward through the tentorial incisura, the brainstem is displaced downward while the basilar artery remains fixed at the base of the skull. This causes stretching and mechanical tearing of the delicate, penetrating paramedian branches of the basilar artery.\n• Clinical implication: Duret hemorrhages disrupt the reticular activating system and vital cardiorespiratory nuclei; they are virtually always fatal."
    },
    {
        "id": "FZ_Q296",
        "question_number": 296,
        "category": "Traumatic Brain Injuries",
        "stem": "A 22-year-old male motorcyclist fractures his right femur and pelvis in a collision. Forty-eight hours later while admitted to the orthopedic floor, he develops acute hypoxemia (PaO2 55 mmHg on room air), sudden confusion and lethargy, and a petechial rash across his axillae, anterior chest wall, and conjunctivae. Non-contrast head CT is unremarkable, but MRI shows diffuse white matter microinfarctions. What is the diagnosis?",
        "options": [
            {"text": "Fat embolism syndrome (FES)", "is_correct": True},
            {"text": "Meningococcemia", "is_correct": False},
            {"text": "Heparin-induced thrombocytopenia", "is_correct": False},
            {"text": "Thrombotic thrombocytopenic purpura", "is_correct": False},
            {"text": "Acute bacterial endocarditis", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Fat embolism syndrome (FES).\n\nFat Embolism Syndrome (FES):\n• Occurs 24 to 72 hours after fractures of marrow-rich long bones (e.g., femur, tibia, pelvis) or orthopedic joint reconstruction.\n• Classic Triad (Gurd's criteria):\n  1. Pulmonary dysfunction: Tachypnea, dyspnea, acute hypoxemia, ARDS.\n  2. Neurological abnormalities: Acute confusion, delirium, stupor, or coma (microvascular cerebral emboli).\n  3. Petechial rash: Non-palpable petechiae in a vest-like distribution (anterior neck, axillae, chest, and conjunctivae) due to microvascular occlusion of dermal capillaries by fat globules and thrombocytopenia.\n• Histopathology: Intravascular fat globules and microvascular petechial hemorrhages in cerebral white matter (visualized with Oil Red O staining)."
    },
    {
        "id": "FZ_Q297",
        "question_number": 297,
        "category": "Traumatic Brain Injuries",
        "stem": "A 30-year-old boxer is struck hard on the forehead and falls backward, striking the back of his head on the canvas. Autopsy shows brain contusions. Why are cerebral contusions following closed head trauma characteristically located on the orbital surfaces of the frontal lobes and the anterior poles of the temporal lobes, regardless of whether the initial impact occurred at the front or back of the skull?",
        "options": [
            {"text": "The inferior frontal and anterior temporal lobes collide forcefully with the irregular, sharp, bony ridges of the anterior cranial fossa and sphenoid wings", "is_correct": True},
            {"text": "Frontal and temporal lobes lack an intact pia mater", "is_correct": False},
            {"text": "Arterial perfusion to the temporal poles is absent during head movement", "is_correct": False},
            {"text": "These lobes contain 90% of the brain's microglial cells", "is_correct": False},
            {"text": "The tentorium cerebelli attaches directly to the orbital cortex", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. The inferior frontal and anterior temporal lobes collide forcefully with the irregular, sharp, bony ridges of the anterior cranial fossa and sphenoid wings.\n\nBiomechanics of Cerebral Contusions:\n• Cerebral contusions represent direct parenchymal bruising (microvascular hemorrhage and cortical necrosis):\n  - Coup contusion: Occurs at the site of impact.\n  - Contrecoup contusion: Occurs on the opposite side of the brain when it decelerates and rebounds against the opposite skull wall.\n• Predilection sites: The base of the skull is not smooth. The orbital roof has jagged bony protuberances, and the lesser wing of the sphenoid bone forms a sharp transverse shelf. As the moving brain glides inside the skull during impact, the inferior frontal lobes and anterior/inferior temporal poles grind against these bony ridges, making them the most common sites of traumatic contusion."
    },
    {
        "id": "FZ_Q298",
        "question_number": 298,
        "category": "Traumatic Brain Injuries",
        "stem": "Which herniation syndrome is characterized by downward displacement of the cerebellar tonsils through the foramen magnum, resulting in direct mechanical compression of the medulla oblongata and rapid cardiac and respiratory arrest?",
        "options": [
            {"text": "Tonsillar herniation", "is_correct": True},
            {"text": "Subfalcine herniation", "is_correct": False},
            {"text": "Uncal herniation", "is_correct": False},
            {"text": "Transcalvarial (external) herniation", "is_correct": False},
            {"text": "Upward cerebellar herniation", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Tonsillar herniation.\n\nTonsillar Herniation (coning):\n• Downward displacement of the cerebellar tonsils (located on the inferior surface of the cerebellum) through the foramen magnum into the cervical spinal canal.\n• Complication: Direct compression of the medulla oblongata, which contains the dorsal and ventral respiratory groups, the pre-Bötzinger pacemaker complex, and the vasomotor center.\n• Clinical result: Rapid medullary ischemia causing flaccid paralysis, Cheyne-Stokes/ataxic breathing, apnea, profound bradycardia, cardiac arrest, and sudden death. (This is why performing a lumbar puncture in the presence of mass effect is strictly contraindicated)."
    },
    {
        "id": "FZ_Q299",
        "question_number": 299,
        "category": "Traumatic Brain Injuries",
        "stem": "A 17-year-old football player sustains a hard tackle to the helmet. He experiences immediate confusion, retrograde amnesia for the play, and a mild headache, but does not lose consciousness. Neurological examination and non-contrast head CT are completely normal. Which clinical syndrome does this presentation represent, and what is the primary pathophysiological alteration?",
        "options": [
            {"text": "Concussion (mild traumatic brain injury); characterized by functional neurometabolic crisis (potassium efflux, glutamate excitotoxicity, and energy crisis) without macroscopic structural parenchymal damage", "is_correct": True},
            {"text": "Subacute subdural hematoma; characterized by gross disruption of the superior sagittal sinus", "is_correct": False},
            {"text": "Cerebral contusion; characterized by wedge-shaped cortical hemorrhagic necrosis", "is_correct": False},
            {"text": "Epidural hematoma; characterized by laceration of the middle meningeal artery", "is_correct": False},
            {"text": "Diffuse axonal injury; characterized by gross transection of the corpus callosum", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Concussion (mild traumatic brain injury); characterized by functional neurometabolic crisis (potassium efflux, glutamate excitotoxicity, and energy crisis) without macroscopic structural parenchymal damage.\n\nConcussion (mTBI) pathophysiology:\n• Clinical diagnosis characterized by transient neurological dysfunction (confusion, amnesia, dizziness, headache, photophobia) induced by biomechanical forces. Loss of consciousness occurs in <10% of concussions.\n• Standard structural neuroimaging (CT and routine MRI) is normal because there is no macroscopic tissue hemorrhage or necrosis.\n• Neurometabolic cascade of concussion: Biomechanical stretching of neuronal membranes triggers non-specific ionic flux -> massive efflux of potassium and influx of calcium -> uncontrolled release of excitatory glutamate -> Na+/K+ ATPase pumps work overtime to restore resting membrane potential -> cellular hypermetabolism consumes glucose stores at the exact time cerebral blood flow is reduced, producing a cellular 'energy crisis'."
    },
    {
        "id": "FZ_Q300",
        "question_number": 300,
        "category": "Traumatic Brain Injuries",
        "stem": "A retired 55-year-old professional football player with a 20-year history of repeated concussions presents with progressive memory loss, severe depression, emotional lability, and parkinsonism. Brain autopsy demonstrates cortical atrophy (especially frontal and temporal lobes), ventricular enlargement, and abnormal perivascular neurofibrillary tangles containing hyperphosphorylated tau protein localized in the depths of cerebral sulci. What neurodegenerative disease is this?",
        "options": [
            {"text": "Chronic traumatic encephalopathy (CTE)", "is_correct": True},
            {"text": "Alzheimer disease", "is_correct": False},
            {"text": "Amyotrophic lateral sclerosis (ALS)", "is_correct": False},
            {"text": "Huntington disease", "is_correct": False},
            {"text": "Creutzfeldt-Jakob disease", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Chronic traumatic encephalopathy (CTE).\n\nChronic Traumatic Encephalopathy (CTE):\n• Progressive neurodegenerative tauopathy triggered by repetitive head impacts (concussions and subconcussive blows), seen in contact sports athletes (football, boxing, hockey) and military veterans.\n• Clinical presentation: Insidious onset of mood disturbances (depression, suicidality), behavioral changes (impulsivity, aggression), cognitive decline (executive dysfunction, memory loss), and late motor features (parkinsonism, dysarthria).\n• Pathological hallmark (consensus criteria): Perivascular accumulation of hyperphosphorylated tau (p-tau) in neurofibrillary and astrocytic tangles with a distinctive predilection for the depths of cerebral sulci in the neocortex (in contrast to Alzheimer disease, which begins in the transentorhinal cortex and features widespread extracellular beta-amyloid plaques)."
    },

    # =========================================================================
    # TOPIC 16: Meningitis (FZ_Q301 - FZ_Q320)
    # =========================================================================
    {
        "id": "FZ_Q301",
        "question_number": 301,
        "category": "Meningitis",
        "stem": "A 2-week-old neonate presents with poor feeding, lethargy, hypothermia (temperature 35.8°C / 96.4°F), and a bulging anterior fontanelle. Lumbar puncture confirms bacterial meningitis. Cerebrospinal fluid cultures grow narrow-zone beta-hemolytic gram-positive cocci in pairs and chains that are bacitracin-resistant and demonstrate a positive CAMP test. Which pathogen is the most common cause of neonatal meningitis in this age group?",
        "options": [
            {"text": "Streptococcus agalactiae (Group B Streptococcus)", "is_correct": True},
            {"text": "Escherichia coli", "is_correct": False},
            {"text": "Listeria monocytogenes", "is_correct": False},
            {"text": "Streptococcus pneumoniae", "is_correct": False},
            {"text": "Neisseria meningitidis", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Streptococcus agalactiae (Group B Streptococcus).\n\nNeonatal Meningitis (<3 months / especially <1 month):\n• Top 3 pathogens:\n  1. Streptococcus agalactiae (Group B Strep / GBS): Most common cause overall (>50% of neonatal cases). Characteristics: Gram-positive cocci in chains, beta-hemolytic, bacitracin-resistant, Hippurate hydrolysis positive, produces CAMP factor (which enlarges the area of beta-hemolysis formed by S. aureus on sheep blood agar).\n  2. Escherichia coli: Second most common cause; >80% of meningitis strains possess the K1 capsular antigen, which prevents phagocytosis.\n  3. Listeria monocytogenes: Gram-positive rod with tumbling motility.\n• Maternal intrapartum screening at 36-37 weeks and prophylaxis with IV penicillin/ampicillin prevents vertical GBS transmission."
    },
    {
        "id": "FZ_Q302",
        "question_number": 302,
        "category": "Meningitis",
        "stem": "A 19-year-old college freshman living in a crowded dormitory presents with acute onset of high fever (39.5°C / 103.1°F), severe throbbing headache, photophobia, and stiff neck. Physical examination reveals non-blanching petechiae and purpuric macules on his lower extremities and trunk. CSF examination reveals bean-shaped gram-negative diplococci. Which organism is the most likely pathogen?",
        "options": [
            {"text": "Neisseria meningitidis", "is_correct": True},
            {"text": "Streptococcus pneumoniae", "is_correct": False},
            {"text": "Haemophilus influenzae type b", "is_correct": False},
            {"text": "Cryptococcus neoformans", "is_correct": False},
            {"text": "Enterovirus (Coxsackievirus B)", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Neisseria meningitidis.\n\nMeningococcal Meningitis (Neisseria meningitidis):\n• Epidemiology: Predominant pathogen in adolescents and young adults (causes >50% of cases in ages 11-20), with high rates in close-contact environments (college dormitories, military barracks).\n• Microbiology: Gram-negative, oxidase-positive, kidney bean-shaped diplococci that ferment both glucose and maltose.\n• Key clinical feature: Petechial and purpuric rash (petechiae on trunk/extremities that progress to purpura fulminans). Driven by shedding of Lipooligosaccharide (LOS) endotoxin into the bloodstream, triggering widespread endothelial injury, microvascular thrombosis, and disseminated intravascular coagulation (DIC).\n• Can progress rapidly to Waterhouse-Friderichsen syndrome."
    },
    {
        "id": "FZ_Q303",
        "question_number": 303,
        "category": "Meningitis",
        "stem": "A 68-year-old woman with a history of chronic lymphocytic leukemia presents with fever, confusion, and nuchal rigidity. Gram stain of the CSF reveals intracellular and extracellular short gram-positive rods. Cultures demonstrate narrow beta-hemolysis and characteristic 'tumbling motility' in broth at room temperature (25°C). Which pathogen is responsible?",
        "options": [
            {"text": "Listeria monocytogenes", "is_correct": True},
            {"text": "Streptococcus pneumoniae", "is_correct": False},
            {"text": "Escherichia coli", "is_correct": False},
            {"text": "Corynebacterium diphtheriae", "is_correct": False},
            {"text": "Bacillus cereus", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Listeria monocytogenes.\n\nListeria monocytogenes:\n• Epidemiology: High risk in neonates (<1 month), elderly adults (>50 years), pregnant women, and immunocompromised patients (impaired cell-mediated immunity, e.g., hematologic malignancies, transplant recipients, steroids).\n• Transmission: Ingestion of unpasteurized dairy, soft cheeses, cold cuts/deli meats. It is cold-tolerant (multiplies at 4°C).\n• Microbiology: Facultative intracellular gram-positive bacillus, non-spore forming, tumbling motility at 22-25°C (via flagella), forms 'actin rockets' (via ActA protein) to spread directly from cell to cell without entering extracellular space.\n• Clinical implication: Listeria is intrinsically resistant to third-generation cephalosporins (ceftriaxone)! Therefore, Ampicillin must be added to empiric regimens in neonates, patients >50 years, and the immunocompromised."
    },
    {
        "id": "FZ_Q304",
        "question_number": 304,
        "category": "Meningitis",
        "stem": "A 55-year-old man presents with acute bacterial meningitis following right-sided acute otitis media. Gram stain of the CSF reveals gram-positive, lancet-shaped diplococci that are alpha-hemolytic, bile-soluble, and optochin-sensitive. What is the most common bacterial pathogen causing acute meningitis in adults worldwide?",
        "options": [
            {"text": "Streptococcus pneumoniae", "is_correct": True},
            {"text": "Neisseria meningitidis", "is_correct": False},
            {"text": "Staphylococcus aureus", "is_correct": False},
            {"text": "Pseudomonas aeruginosa", "is_correct": False},
            {"text": "Klebsiella pneumoniae", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Streptococcus pneumoniae.\n\nPneumococcal Meningitis (Streptococcus pneumoniae):\n• Most common cause of bacterial meningitis in adults of all ages, accounting for ~60% of adult cases.\n• Predisposing conditions: Preceding otitis media, sinusitis, pneumonia, CSF leak secondary to skull fracture, asplenia (loss of splenic antibody opsonization), or alcoholism.\n• Microbiology: Lancet-shaped gram-positive diplococci, alpha-hemolytic (green on blood agar), optochin-sensitive (zone of inhibition), and lysed by bile salts (bile-soluble).\n• Carries the highest mortality rate among bacterial meningitis pathogens (~15-30%) and high rates of permanent sensorineural hearing loss."
    },
    {
        "id": "FZ_Q305",
        "question_number": 305,
        "category": "Meningitis",
        "stem": "An unconscious 30-year-old patient undergoes lumbar puncture for suspected meningitis. The CSF opening pressure is 320 mm H2O (normal 80-200). Laboratory analysis of the CSF reveals:\n• WBC: 2,500/mm³ with 92% polymorphonuclear neutrophils (PMNs)\n• Protein: 280 mg/dL (normal 15-45)\n• Glucose: 18 mg/dL (serum glucose is 100 mg/dL; ratio 0.18)\nWhich category of meningitis do these CSF findings diagnostic of?",
        "options": [
            {"text": "Acute bacterial meningitis", "is_correct": True},
            {"text": "Aseptic viral meningitis", "is_correct": False},
            {"text": "Fungal meningitis", "is_correct": False},
            {"text": "Guillain-Barré syndrome", "is_correct": False},
            {"text": "Multiple sclerosis", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Acute bacterial meningitis.\n\nCSF Profiles Comparison:\n1. Acute Bacterial Meningitis:\n   • Opening pressure: Markedly elevated (>200-300 mm H2O).\n   • WBC: Markedly elevated (1,000 to >10,000/mm³) with PMN predominance (>80-90%).\n   • Protein: Markedly elevated (>100-500 mg/dL) due to increased blood-brain barrier permeability.\n   • Glucose: Markedly decreased (<40 mg/dL or CSF:serum ratio <0.4; normally ~0.6) due to pathogen and leukocyte consumption and impaired hexose transport.\n2. Viral (Aseptic) Meningitis:\n   • Normal/mildly elevated opening pressure, lymphocytic pleocytosis (10-500/mm³), normal or slightly elevated protein (<100 mg/dL), and NORMAL glucose (>40 mg/dL or ratio >0.6).\n3. Fungal/TB: Elevated pressure, lymphocytic predominance, very high protein, low glucose."
    },
    {
        "id": "FZ_Q306",
        "question_number": 306,
        "category": "Meningitis",
        "stem": "A 22-year-old woman presents in mid-July with low-grade fever, mild headache, photophobia, and neck stiffness. She has no altered mental status or focal deficits. Lumbar puncture demonstrates an opening pressure of 160 mm H2O, WBC of 120/mm³ with 85% lymphocytes, protein of 65 mg/dL, and CSF glucose of 60 mg/dL (serum glucose 95 mg/dL). Which class of viruses is the most common cause of aseptic (viral) meningitis?",
        "options": [
            {"text": "Non-polio Enteroviruses (Coxsackievirus, Echovirus)", "is_correct": True},
            {"text": "Herpes simplex virus type 1 (HSV-1)", "is_correct": False},
            {"text": "Rabies virus", "is_correct": False},
            {"text": "Cytomegalovirus (CMV)", "is_correct": False},
            {"text": "Varicella-zoster virus (VZV)", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Non-polio Enteroviruses (Coxsackievirus, Echovirus).\n\nAseptic (Viral) Meningitis:\n• Enteroviruses (Picornaviridae family: Coxsackievirus A and B, Echoviruses, Parechoviruses) account for >85-90% of all viral meningitis cases where a pathogen is identified, typically peaking in summer and autumn.\n• Enteroviruses are positive-sense single-stranded RNA viruses transmitted via the fecal-oral route.\n• Clinical course is typically benign and self-limiting with complete recovery, requiring supportive care rather than antimicrobial therapy.\n• HSV-2 can cause recurrent benign lymphocytic meningitis (Mollaret meningitis), whereas HSV-1 typically causes temporal lobe encephalitis rather than pure meningitis."
    },
    {
        "id": "FZ_Q307",
        "question_number": 307,
        "category": "Meningitis",
        "stem": "During physical examination of a patient with suspected meningitis, the physician places the patient in the supine position and passively flexes the neck toward the chest. This maneuver causes the patient to immediately and involuntarily flex both hips and knees. What is the name of this physical sign of meningeal irritation?",
        "options": [
            {"text": "Brudzinski sign", "is_correct": True},
            {"text": "Kernig sign", "is_correct": False},
            {"text": "Lhermitte sign", "is_correct": False},
            {"text": "Chvostek sign", "is_correct": False},
            {"text": "Trousseau sign", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Brudzinski sign.\n\nMeningismus physical examination signs:\n1. Brudzinski sign: Involuntary flexion of the hips and knees in response to passive flexion of the patient's neck while lying supine. Stretching of the inflamed cervical meninges causes reflexive spinal flexion to relieve traction on the spinal cord and nerve roots.\n2. Kernig sign: Inability to extend the knee past 135 degrees without severe pain or resistance when the hip is flexed to 90 degrees in a supine patient.\n3. Nuchal rigidity: Inability to touch the chin to the chest due to spasm and stiffness of the extensor neck muscles.\n• Note: These signs have high specificity (>95%) but low sensitivity (<50%); their absence never rules out meningitis."
    },
    {
        "id": "FZ_Q308",
        "question_number": 308,
        "category": "Meningitis",
        "stem": "A 45-year-old man presents with suspected bacterial meningitis. Fundoscopy reveals blurring of the optic disc margins with absent venous pulsations (papilledema), and he has a right-sided pronator drift. Why is an urgent non-contrast CT scan of the head required BEFORE performing a lumbar puncture in this patient?",
        "options": [
            {"text": "To rule out an intracranial mass lesion or midline shift that could trigger fatal tentorial or tonsillar herniation upon CSF removal", "is_correct": True},
            {"text": "To confirm the bacterial species causing the infection", "is_correct": False},
            {"text": "To measure the exact CSF protein concentration non-invasively", "is_correct": False},
            {"text": "To determine whether the patient has penicillin resistance", "is_correct": False},
            {"text": "To assess for acute sphenoid sinusitis", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. To rule out an intracranial mass lesion or midline shift that could trigger fatal tentorial or tonsillar herniation upon CSF removal.\n\nIndications for Head CT prior to Lumbar Puncture:\n• When a significant intracranial mass lesion (abscess, hematoma, tumor) or severe brain edema exists, removing CSF via lumbar puncture creates a downward pressure gradient between the cranial vault and spinal canal.\n• This pressure gradient can precipitate fatal brain herniation (uncal or cerebellar tonsillar herniation through the foramen magnum).\n• IDSA Guidelines for CT before LP:\n  1. Focal neurological deficits (e.g., hemiparesis, visual field cut, cranial nerve palsy)\n  2. New-onset seizures within 1 week\n  3. Papilledema on fundoscopic examination\n  4. Severely depressed level of consciousness (GCS <10)\n  5. Immunocompromised state (HIV, chemotherapy, organ transplant)\n• CRITICAL rule: If CT is indicated, do NOT delay antibiotics! Draw blood cultures, start empiric IV antibiotics + dexamethasone immediately, and then send the patient for CT."
    },
    {
        "id": "FZ_Q309",
        "question_number": 309,
        "category": "Meningitis",
        "stem": "A 24-year-old previously healthy woman presents with fever, severe headache, photophobia, and nuchal rigidity. While awaiting lumbar puncture, the emergency physician must initiate empiric intravenous antibiotic therapy. What is the standard empiric antibiotic regimen for community-acquired bacterial meningitis in an immunocompetent adult aged 18 to 50 years?",
        "options": [
            {"text": "Vancomycin + Ceftriaxone (or Cefotaxime)", "is_correct": True},
            {"text": "Ampicillin + Gentamicin", "is_correct": False},
            {"text": "Vancomycin + Ceftriaxone + Ampicillin", "is_correct": False},
            {"text": "Ciprofloxacin monotherapy", "is_correct": False},
            {"text": "Penicillin G alone", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Vancomycin + Ceftriaxone (or Cefotaxime).\n\nEmpiric Antibiotic Regimens for Bacterial Meningitis:\n• Age 1 month to 50 years: Vancomycin + 3rd-generation cephalosporin (Ceftriaxone or Cefotaxime).\n  - Ceftriaxone provides high CSF penetration and excellent bactericidal coverage against Neisseria meningitidis and susceptible Streptococcus pneumoniae.\n  - Vancomycin is added specifically to cover penicillin- and cephalosporin-resistant strains of Streptococcus pneumoniae.\n• Age >50 years or Immunocompromised: Vancomycin + Ceftriaxone + Ampicillin (Ampicillin is required to cover Listeria monocytogenes).\n• Neonates (<1 month): Ampicillin + Cefotaxime (or Gentamicin). Ceftriaxone is avoided in neonates because it displaces bilirubin from albumin (risking kernicterus) and precipitates in bile."
    },
    {
        "id": "FZ_Q310",
        "question_number": 310,
        "category": "Meningitis",
        "stem": "Why must adjunctive intravenous dexamethasone be administered prior to or concurrently with the first dose of antibiotics in adults with suspected or confirmed Streptococcus pneumoniae meningitis?",
        "options": [
            {"text": "To suppress the massive subarachnoid inflammatory cascade triggered by antibiotic-induced bacterial cell wall lysis, significantly reducing mortality and sensorineural hearing loss", "is_correct": True},
            {"text": "To directly lyse the bacterial polysaccharide capsule", "is_correct": False},
            {"text": "To increase the permeability of the blood-brain barrier to hydrophilic antibiotics", "is_correct": False},
            {"text": "To stimulate hepatic glycogenolysis and elevate CSF glucose levels", "is_correct": False},
            {"text": "To prevent acute renal failure caused by vancomycin toxicity", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. To suppress the massive subarachnoid inflammatory cascade triggered by antibiotic-induced bacterial cell wall lysis, significantly reducing mortality and sensorineural hearing loss.\n\nRole of Dexamethasone in Meningitis:\n• When bactericidal antibiotics (beta-lactams and vancomycin) lyse bacteria, large quantities of cell wall peptidoglycan and teichoic acid fragments are released into the subarachnoid space.\n• This triggers a massive, paradoxical surge in microglial and endothelial activation, releasing pro-inflammatory cytokines (TNF-alpha, IL-1beta) that worsen cerebral edema, intracranial pressure, and neuronal damage.\n• Dexamethasone administered 15-20 minutes before or with the first dose of antibiotics blunts this inflammatory surge, proven in clinical trials to significantly reduce mortality, severe neurological sequelae, and permanent sensorineural hearing loss in pneumococcal meningitis."
    },
    {
        "id": "FZ_Q311",
        "question_number": 311,
        "category": "Meningitis",
        "stem": "During a lumbar puncture, the initial CSF collection in tube 1 appears pinkish-red. The resident suspects a 'traumatic tap' rather than a true subarachnoid hemorrhage. Which CSF finding is the most definitive evidence that the bloody CSF is due to a subarachnoid hemorrhage rather than an accidental traumatic vessel puncture?",
        "options": [
            {"text": "Presence of xanthochromia (yellow/pink pigmentation of centrifuged CSF supernatant)", "is_correct": True},
            {"text": "Equal opening pressure in the lateral decubitus position", "is_correct": False},
            {"text": "Marked clearing of RBC counts between tube 1 and tube 4", "is_correct": False},
            {"text": "Presence of crenated RBCs on light microscopy", "is_correct": False},
            {"text": "Normal CSF glucose level", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Presence of xanthochromia (yellow/pink pigmentation of centrifuged CSF supernatant).\n\nDifferentiating Traumatic Tap vs. Subarachnoid Hemorrhage (SAH):\n1. Traumatic Tap (needle lacerates an epidural venous plexus):\n   • RBC count drops significantly from Tube 1 to Tube 4 ('clearing').\n   • Centrifugation of CSF produces a clear, colorless supernatant because fresh RBCs have not had time to hemolyze in the subarachnoid space.\n2. Subarachnoid Hemorrhage:\n   • RBC count remains persistently high and uniform across tubes 1 through 4.\n   • Xanthochromia is PRESENT: Yellow, pink, or amber tint of the centrifuged supernatant due to enzymatic breakdown of lysed RBCs into oxyhemoglobin and bilirubin. Xanthochromia requires 2 to 4 hours to develop in vivo, making it the definitive hallmark of true pre-existing intracranial hemorrhage."
    },
    {
        "id": "FZ_Q312",
        "question_number": 312,
        "category": "Meningitis",
        "stem": "A 20-year-old college student is admitted to the ICU with fulminant Neisseria meningitidis meningitis and septicemia. His dorm roommate, who shares the same bedroom, presents to the student health center inquiring about post-exposure prophylaxis. Which of the following prophylactic regimens is recommended for close contacts of patients with invasive meningococcal disease?",
        "options": [
            {"text": "Rifampin (600 mg orally twice daily for 2 days) or a single dose of Ciprofloxacin (or Ceftriaxone IM)", "is_correct": True},
            {"text": "Amoxicillin orally for 14 days", "is_correct": False},
            {"text": "Vancomycin IV for 7 days", "is_correct": False},
            {"text": "Acyclovir orally for 5 days", "is_correct": False},
            {"text": "Immediate lumbar puncture followed by isolation for 21 days", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Rifampin (600 mg orally twice daily for 2 days) or a single dose of Ciprofloxacin (or Ceftriaxone IM).\n\nMeningococcal Chemoprophylaxis:\n• Indicated for close contacts within the 7 days prior to onset:\n  - Household members, roommates, childcare center contacts.\n  - Anyone directly exposed to patient's oral secretions (kissing, sharing utensils/drinks, mouth-to-mouth resuscitation, endotracheal intubation without mask).\n• Regimens:\n  1. Rifampin: 600 mg PO BID for 2 days (4 doses total). Eradicates nasopharyngeal carriage. Note: Imparts harmless orange/red discoloration to tears, saliva, and urine; soft contact lenses will be permanently stained.\n  2. Ciprofloxacin: 500 mg PO single dose (adults).\n  3. Ceftriaxone: 250 mg IM single dose (preferred choice in pregnant women)."
    },
    {
        "id": "FZ_Q313",
        "question_number": 313,
        "category": "Meningitis",
        "stem": "A 16-year-old boy with Neisseria meningitidis septicemia rapidly develops refractory hypotension, cyanosis, cold extremities, diffuse ecchymoses and purpura across his body, and profound metabolic acidosis. Autopsy reveals bilateral massive hemorrhagic necrosis of both adrenal glands. What eponym describes this catastrophic complication of fulminant meningococcemia?",
        "options": [
            {"text": "Waterhouse-Friderichsen syndrome", "is_correct": True},
            {"text": "Sheehan syndrome", "is_correct": False},
            {"text": "Nelson syndrome", "is_correct": False},
            {"text": "Conn syndrome", "is_correct": False},
            {"text": "Schmidt syndrome", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Waterhouse-Friderichsen syndrome.\n\nWaterhouse-Friderichsen Syndrome:\n• Severe, catastrophic complication of fulminant meningococcemia (Neisseria meningitidis bacteremia), though occasionally caused by S. pneumoniae or Pseudomonas.\n• Pathophysiology:\n  1. Massive endotoxemia (LOS) triggers widespread microvascular thrombosis and Disseminated Intravascular Coagulation (DIC).\n  2. Extensive purpura fulminans of the skin.\n  3. Bilateral adrenal hemorrhagic infarction (apoplexy), causing acute primary adrenal insufficiency.\n• Clinical result: Acute deficiency of cortisol and aldosterone produces profound, refractory vasodilatory septic shock, cardiovascular collapse, and death within hours."
    },
    {
        "id": "FZ_Q314",
        "question_number": 314,
        "category": "Meningitis",
        "stem": "What is the single most common long-term permanent neurological deficit seen in pediatric and adult survivors of acute bacterial meningitis?",
        "options": [
            {"text": "Sensorineural hearing loss", "is_correct": True},
            {"text": "Bitemporal hemianopsia", "is_correct": False},
            {"text": "Severe flaccid paraplegia", "is_correct": False},
            {"text": "Isolated expressive (Broca) aphasia", "is_correct": False},
            {"text": "Parkinsonism", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Sensorineural hearing loss.\n\nSensorineural Hearing Loss after Meningitis:\n• Occurs in up to 10-30% of survivors of bacterial meningitis (highest with Streptococcus pneumoniae, followed by N. meningitidis and H. influenzae).\n• Mechanism: Purulent infection and inflammatory mediators in the subarachnoid space spread directly from the subarachnoid space into the inner ear via the cochlear aqueduct (perilymphatic duct). This causes suppurative labyrinthitis, destruction of the sensory hair cells in the organ of Corti and spiral ganglion neurons, followed by fibrosis and ossification (labyrinthitis ossificans).\n• Audiometric screening is mandatory for all patients after hospital discharge."
    },
    {
        "id": "FZ_Q315",
        "question_number": 315,
        "category": "Meningitis",
        "stem": "Three weeks after successful antibiotic treatment for pneumococcal meningitis, a 4-year-old child presents with progressive morning headache, vomiting, lethargy, and papilledema. Head CT reveals symmetric enlargement of all four cerebral ventricles (lateral, third, and fourth ventricles) without any mass lesion obstructing the ventricular foramina. What is the mechanism of this hydrocephalus?",
        "options": [
            {"text": "Communicating hydrocephalus caused by inflammatory scarring, purulent exudate clogging, and fibrosis of the arachnoid granulations (villi), impairing CSF resorption", "is_correct": True},
            {"text": "Non-communicating hydrocephalus caused by congenital aqueductal stenosis", "is_correct": False},
            {"text": "Overproduction of CSF by a choroid plexus papilloma", "is_correct": False},
            {"text": "Ex-vacuo hydrocephalus caused by primary cerebral cortical atrophy", "is_correct": False},
            {"text": "Colloid cyst occlusion of the foramen of Monro", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Communicating hydrocephalus caused by inflammatory scarring, purulent exudate clogging, and fibrosis of the arachnoid granulations (villi), impairing CSF resorption.\n\nCommunicating Hydrocephalus Post-Meningitis:\n• During bacterial meningitis, purulent inflammatory exudate accumulates in the subarachnoid space and basal cisterns.\n• The thick exudate and subsequent fibroblast proliferation clog and scar the arachnoid villi (granulations) that project into the superior sagittal sinus.\n• Because arachnoid villi are the primary site of CSF absorption into the venous circulation, CSF resorption is severely impaired.\n• Because fluid can still communicate freely between the ventricles and subarachnoid space, all ventricles dilate symmetrically (communicating/non-obstructive hydrocephalus), elevating intracranial pressure."
    },
    {
        "id": "FZ_Q316",
        "question_number": 316,
        "category": "Meningitis",
        "stem": "A 3-year-old child presents with high fever, neck stiffness, and irritability. Lumbar puncture confirms bacterial meningitis. The hospital laboratory reports that the causative organism is a pleomorphic, gram-negative coccobacillus that requires both factor X (hematin) and factor V (NAD) to grow on chocolate agar. The child's parents immigrated recently and have no vaccination records. Which organism is this?",
        "options": [
            {"text": "Haemophilus influenzae type b", "is_correct": True},
            {"text": "Bordetella pertussis", "is_correct": False},
            {"text": "Moraxella catarrhalis", "is_correct": False},
            {"text": "Legionella pneumophila", "is_correct": False},
            {"text": "Francisella tularensis", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Haemophilus influenzae type b.\n\nHaemophilus influenzae type b (Hib):\n• Microbiology: Small, pleomorphic gram-negative coccobacillus. Requires two erythrocyte factors for growth: Factor X (hemin / hematin) and Factor V (NAD+). It cannot grow on sheep blood agar alone unless plated with Staphylococcus aureus (satellite phenomenon), but grows robustly on chocolate agar (heated lysed blood).\n• Virulence factor: Polyribosylribitol phosphate (PRP) capsule, which inhibits phagocytosis and complement-mediated lysis.\n• Historically a leading cause of childhood meningitis (ages 6 months to 3 years), but virtually eradicated in vaccinated populations due to the Hib conjugate vaccine (PRP conjugated to diphtheria or tetanus toxoid), given at 2, 4, 6, and 12-15 months."
    },
    {
        "id": "FZ_Q317",
        "question_number": 317,
        "category": "Meningitis",
        "stem": "Which virulence factor shared by Neisseria meningitidis, Streptococcus pneumoniae, and Haemophilus influenzae enables these pathogens to colonize the nasopharyngeal mucosa and overcome initial respiratory mucosal defense mechanisms?",
        "options": [
            {"text": "Secretory IgA1 protease", "is_correct": True},
            {"text": "Lecithinase (alpha-toxin)", "is_correct": False},
            {"text": "Coagulase", "is_correct": False},
            {"text": "Exotoxin A", "is_correct": False},
            {"text": "M protein", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Secretory IgA1 protease.\n\nIgA Protease in Meningitis Pathogens:\n• The top three causes of community-acquired bacterial meningitis (Streptococcus pneumoniae, Neisseria meningitidis, and Haemophilus influenzae) all produce an extracellular IgA1 protease.\n• Function: Cleaves the proline-rich hinge region of human secretory immunoglobulin A (sIgA) on respiratory mucosal surfaces.\n• By cleaving sIgA, these bacteria prevent antibody-mediated agglutination and mucosal clearance, allowing them to adhere to nasopharyngeal epithelial microvilli, colonize the upper airway, and eventually penetrate into the bloodstream."
    },
    {
        "id": "FZ_Q318",
        "question_number": 318,
        "category": "Meningitis",
        "stem": "An 11-year-old boy presents to his pediatrician for a routine well-child checkup prior to entering middle school. According to CDC and Advisory Committee on Immunization Practices (ACIP) guidelines, which routine vaccine is recommended at age 11 to 12 years with a booster at age 16 to protect against epidemic bacterial meningitis?",
        "options": [
            {"text": "Quadrivalent Meningococcal conjugate vaccine (MenACWY)", "is_correct": True},
            {"text": "Pneumococcal polysaccharide vaccine (PPSV23)", "is_correct": False},
            {"text": "Bacillus Calmette-Guérin (BCG) vaccine", "is_correct": False},
            {"text": "Oral poliovirus vaccine (OPV)", "is_correct": False},
            {"text": "Live attenuated varicella-zoster vaccine", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Quadrivalent Meningococcal conjugate vaccine (MenACWY).\n\nMeningococcal Vaccination Schedule:\n• Quadrivalent Meningococcal conjugate vaccine (MenACWY covers serogroups A, C, W-135, and Y):\n  - Primary dose: Recommended at age 11 to 12 years.\n  - Booster dose: Recommended at age 16 years (prior to high school graduation, college dormitories, or military service, when the risk of invasive disease peaks).\n• Serogroup B Meningococcal vaccine (MenB): Recommended as a separate series at age 16-23 (preferred 16-18) for young adults and high-risk patients (e.g., complement deficiencies, eculizumab therapy, asplenia)."
    },
    {
        "id": "FZ_Q319",
        "question_number": 319,
        "category": "Meningitis",
        "stem": "A 32-year-old HIV-positive man with a CD4+ T-cell count of 38/mm³ presents with a 2-week history of low-grade fever, progressive dull headache, and malaise. Physical examination reveals mild nuchal rigidity without papilledema. Lumbar puncture demonstrates an opening pressure of 280 mm H2O. CSF examination with an India ink preparation demonstrates round budding yeasts with prominent, wide clear halos. Which fungal pathogen is this?",
        "options": [
            {"text": "Cryptococcus neoformans", "is_correct": True},
            {"text": "Candida albicans", "is_correct": False},
            {"text": "Histoplasma capsulatum", "is_correct": False},
            {"text": "Aspergillus fumigatus", "is_correct": False},
            {"text": "Coccidioides immitis", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Cryptococcus neoformans.\n\nCryptococcal Meningitis (Cryptococcus neoformans):\n• Epidemiology: Heavily encapsulated, opportunistic environmental yeast found in pigeon droppings and soil. Major cause of subacute/chronic meningitis in immunocompromised patients (HIV CD4 <100/mm³).\n• Diagnostics:\n  1. India ink stain: Round, narrow-based budding yeast cells surrounded by a thick, transparent polysaccharide capsule that repels ink particles ('halo' sign).\n  2. Cryptococcal antigen (CrAg) lateral flow assay: >98% sensitivity and specificity, detecting the glucuronoxylomannan capsular antigen.\n  3. Mucicarmine stain: Stains the polysaccharide capsule bright red.\n• Treatment: Induction with Amphotericin B + Flucytosine, followed by long-term consolidation/maintenance with Fluconazole."
    },
    {
        "id": "FZ_Q320",
        "question_number": 320,
        "category": "Meningitis",
        "stem": "A 42-year-old man undergoes lumbar puncture for suspected meningitis. The initial tap is bloody due to vein laceration during needle insertion. The lab technician reports 3,000 RBCs/mm³ and 15 WBCs/mm³ in the CSF. In clinical practice, which standard correction ratio is applied to determine whether the elevated CSF white blood cell count is solely an artifact of peripheral blood contamination from a traumatic tap?",
        "options": [
            {"text": "Subtract 1 WBC for every 500 to 1,000 RBCs present in the CSF", "is_correct": True},
            {"text": "Subtract 10 WBCs for every 10 RBCs present in the CSF", "is_correct": False},
            {"text": "Add 5 WBCs for every 100 RBCs present in the CSF", "is_correct": False},
            {"text": "Multiply total WBC count by the hematocrit", "is_correct": False},
            {"text": "Traumatic taps can never be corrected and always require repeat tap at a higher lumbar interspace", "is_correct": False}
        ],
        "explanation": "Correct Answer: A. Subtract 1 WBC for every 500 to 1,000 RBCs present in the CSF.\n\nTraumatic Tap Correction Formula:\n• In normal peripheral blood, the ratio of white blood cells to red blood cells is approximately 1 WBC per 500 to 1,000 RBCs (e.g., normal peripheral WBC ~5,000-10,000/uL, RBC ~5 million/uL).\n• Therefore, when accidental blood enters the CSF during a traumatic tap:\n  - Estimated artifactual WBCs = Observed CSF RBCs / 500 (or 750).\n  - In this patient with 3,000 RBCs, expected artifactual WBCs = 3,000 / (500 to 1,000) = 3 to 6 WBCs.\n  - Since the observed WBC count is 15, the corrected true CSF WBC count is ~9 to 12 WBCs/mm³, indicating genuine mild CSF pleocytosis beyond blood contamination."
    }
]
