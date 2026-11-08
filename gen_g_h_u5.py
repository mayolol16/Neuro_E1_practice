import json
from test_gen_structure import check_q

u5_questions = [
    {
        "id": "exam3_g_h_u5_q1",
        "category": "Unit 05: Epilepsy",
        "subcategory": "Seizure Semiology",
        "question_type": "clinical_vignette",
        "stem": "A 47-year-old man with a low-grade oligodendroglioma develops stereotyped episodes beginning with rhythmic clonic jerking of his right thumb that progressively marches over sixty seconds to involve his right fingers, wrist, forearm, arm, and right lower face without impairment of awareness. Where does this seizure activity originate and what neuroanatomical principle dictates its order of progression?",
        "options": [
            {"label": "A", "text": "Precentral gyrus propagating sequentially along the somatic motor homunculus", "is_correct": True},
            {"label": "B", "text": "Postcentral gyrus spreading via intracortical associative thalamic fibers", "is_correct": False},
            {"label": "C", "text": "Supplementary motor area discharging across the anterior corpus callosum", "is_correct": False},
            {"label": "D", "text": "Dentate cerebellar nucleus propagating through the superior peduncle", "is_correct": False},
            {"label": "E", "text": "Subthalamic nucleus sending disinhibited signals to the globus pallidus", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "This patient exhibits a classic Jacksonian march, a form of focal aware motor seizure originating in the primary motor cortex (precentral gyrus, Brodmann area 4). Epileptiform discharges travel contiguously across neighboring neuronal populations along the motor homunculus, sequentially recruiting adjacent anatomical representations (thumb to fingers to wrist to arm to face).",
        "high_yield_takeaway": "Jacksonian march is a focal aware seizure originating in the precentral gyrus that spreads contiguously along the cortical motor homunculus."
    },
    {
        "id": "exam3_g_h_u5_q2",
        "category": "Unit 05: Epilepsy",
        "subcategory": "Status Epilepticus",
        "question_type": "clinical_vignette",
        "stem": "A 24-year-old woman is brought to the emergency department in continuous generalized convulsive status epilepticus lasting twelve minutes. Two successive intravenous doses of lorazepam temporarily halt her motor convulsions, but continuous generalized rhythmic jerking resumes eight minutes later. What is the most appropriate next step in the established pharmacotherapeutic algorithm?",
        "options": [
            {"label": "A", "text": "Administer an intravenous loading infusion of fosphenytoin or levetiracetam", "is_correct": True},
            {"label": "B", "text": "Administer repeated doses of intravenous diazepam every fifteen minutes", "is_correct": False},
            {"label": "C", "text": "Initiate emergent therapeutic hypothermia to suppress cerebral metabolism", "is_correct": False},
            {"label": "D", "text": "Perform emergent endotracheal intubation with oral carbamazepine loading", "is_correct": False},
            {"label": "E", "text": "Inject intramuscular flumazenil to reverse allosteric receptor saturation", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "In established status epilepticus, first-line therapy is an intravenous benzodiazepine (lorazepam 0.1 mg/kg or diazepam). If seizures continue or recur beyond 5-10 minutes, second-line therapy is an urgent non-sedating intravenous antiseizure medication, specifically fosphenytoin (20 mg PE/kg), levetiracetam (60 mg/kg), or valproate (40 mg/kg). Benzodiazepines should not be endlessly repeated because GABA-A receptors undergo rapid internalization during prolonged seizures.",
        "high_yield_takeaway": "Status epilepticus failing initial benzodiazepines requires emergent second-line loading with IV fosphenytoin, levetiracetam, or valproate."
    },
    {
        "id": "exam3_g_h_u5_q3",
        "category": "Unit 05: Epilepsy",
        "subcategory": "Pharmacokinetics",
        "question_type": "clinical_vignette",
        "stem": "A 32-year-old man with focal epilepsy takes 300 mg daily of phenytoin with a steady-state serum concentration of 9 mcg/mL (therapeutic range 10-20 mcg/mL). Due to persistent seizures, his dosage is increased by 33% to 400 mg daily. Two weeks later, he presents with severe ataxia, coarse horizontal nystagmus, and confusion, with a serum level of 36 mcg/mL. What pharmacokinetic principle explains this disproportionate level increase?",
        "options": [
            {"label": "A", "text": "Transition from first-order to zero-order saturation elimination kinetics", "is_correct": True},
            {"label": "B", "text": "Marked down-regulation of renal tubular organic anion secretory pumps", "is_correct": False},
            {"label": "C", "text": "Auto-inhibition of gastrointestinal enterocyte P-glycoprotein transport", "is_correct": False},
            {"label": "D", "text": "Progressive displacement from serum albumin by endogenous fatty acids", "is_correct": False},
            {"label": "E", "text": "Allosteric conformational activation of hepatic cytochrome P450 oxidases", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "Phenytoin displays Michaelis-Menten non-linear pharmacokinetics. At low concentrations, elimination is first-order (rate proportional to concentration). Near therapeutic levels (10-20 mcg/mL), hepatic microsomal clearance enzymes (CYP2C9 and CYP2C19) become fully saturated, shifting elimination to zero-order kinetics (fixed amount cleared per unit time). Small incremental dosage increases then cause massive, toxic jumps in serum concentration.",
        "high_yield_takeaway": "Phenytoin follows zero-order (saturation) kinetics near therapeutic range, meaning small dose increases can trigger massive jumps in serum level and toxicity."
    },
    {
        "id": "exam3_g_h_u5_q4",
        "category": "Unit 05: Epilepsy",
        "subcategory": "Antiseizure Pharmacology",
        "question_type": "clinical_vignette",
        "stem": "A 29-year-old man started on carbamazepine for focal epilepsy achieves complete seizure cessation with a therapeutic serum level of 8 mcg/mL at two weeks. By week six, despite strict medication adherence confirmed by pill counts, his focal seizures recur and his trough level drops to 3.5 mcg/mL. What pharmacological mechanism accounts for this reduction in circulating drug concentration?",
        "options": [
            {"label": "A", "text": "Auto-induction of hepatic CYP3A4 accelerating its own metabolic clearance", "is_correct": True},
            {"label": "B", "text": "Saturation of intestinal carrier-mediated mucosal absorption receptors", "is_correct": False},
            {"label": "C", "text": "Gradual induction of renal tubular clearance via proton-coupled antiport", "is_correct": False},
            {"label": "D", "text": "Competitive displacement by endogenously synthesized steroid hormones", "is_correct": False},
            {"label": "E", "text": "Tachyphylaxis from desensitization of central voltage-gated sodium channels", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "Carbamazepine is a potent inducer of hepatic cytochrome P450 enzymes, particularly CYP3A4, and crucially undergoes auto-induction (it induces the very enzymes responsible for its own metabolism). Auto-induction typically begins within 3-5 days and is complete by 3-5 weeks, shortening its elimination half-life from ~30 hours down to ~12-15 hours, necessitating dose adjustments.",
        "high_yield_takeaway": "Carbamazepine induces its own hepatic metabolism (CYP3A4 auto-induction), causing serum levels to fall after 2-4 weeks and requiring upward titration."
    },
    {
        "id": "exam3_g_h_u5_q5",
        "category": "Unit 05: Epilepsy",
        "subcategory": "Drug-Drug Interactions",
        "question_type": "clinical_vignette",
        "stem": "A 21-year-old woman with epilepsy well-controlled on valproate has lamotrigine added to her regimen. Two weeks later, she develops high fever, oral mucosal ulcerations, conjunctival injection, and a rapidly spreading erythematous macular rash with full-thickness epidermal sloughing (Stevens-Johnson syndrome). Why did the combination of these two agents dramatically increase her susceptibility to this life-threatening drug reaction?",
        "options": [
            {"label": "A", "text": "Valproate inhibits lamotrigine glucuronidation markedly prolonging half-life", "is_correct": True},
            {"label": "B", "text": "Lamotrigine displaces valproate from albumin triggering acute hepatotoxicity", "is_correct": False},
            {"label": "C", "text": "Both medications competitively block renal tubular clearance of metabolites", "is_correct": False},
            {"label": "D", "text": "Valproate induces skin keratinocyte major histocompatibility class II antigens", "is_correct": False},
            {"label": "E", "text": "Lamotrigine accelerates valproate mitochondrial beta-oxidation breakdown", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "Valproate is a potent inhibitor of hepatic UDP-glucuronosyltransferase (specifically UGT1A4 and UGT2B7), the primary clearance pathway for lamotrigine. Co-administration more than doubles lamotrigine's elimination half-life and dramatically increases circulating levels. If lamotrigine is not started at less than half the normal starting dose and titrated very slowly, patients face a severe risk of Stevens-Johnson syndrome (SJS) and toxic epidermal necrolysis (TEN).",
        "high_yield_takeaway": "Valproate inhibits lamotrigine glucuronidation, more than doubling lamotrigine levels and dramatically increasing the risk of Stevens-Johnson syndrome."
    },
    {
        "id": "exam3_g_h_u5_q6",
        "category": "Unit 05: Epilepsy",
        "subcategory": "Adverse Drug Reactions",
        "question_type": "clinical_vignette",
        "stem": "A 16-year-old girl with juvenile myoclonic epilepsy managed with valproic acid presents with progressive stupor, vomiting, and flapping asterixis. Serum transaminases (AST and ALT), total bilirubin, and synthetic coagulation parameters are completely normal, but her serum ammonia level is markedly elevated at 195 umol/L. What enzyme in the urea cycle does valproic acid metabolite indirectly inhibit to cause this non-cirrhotic hyperammonemia?",
        "options": [
            {"label": "A", "text": "Carbamoyl phosphate synthetase I via depletion of N-acetylglutamate cofactor", "is_correct": True},
            {"label": "B", "text": "Ornithine transcarbamylase via direct active-site competitive antagonism", "is_correct": False},
            {"label": "C", "text": "Argininosuccinate synthetase via consumption of cytosolic ATP stores", "is_correct": False},
            {"label": "D", "text": "Arginase via chelation of critical manganese catalytic cofactors", "is_correct": False},
            {"label": "E", "text": "Glutamine synthetase via irreversible covalent alkylation of lysine residues", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "Valproate-induced hyperammonemic encephalopathy can occur with normal liver function tests. Valproate metabolites (e.g., valproyl-CoA) deplete mitochondrial acetyl-CoA and carnitine, which decreases synthesis of N-acetylglutamate (NAG). Because NAG is the obligate allosteric activator of carbamoyl phosphate synthetase I (CPS-I), CPS-I activity is suppressed, halting urea cycle clearance of ammonia. Treatment includes L-carnitine.",
        "high_yield_takeaway": "Valproate can cause non-cirrhotic hyperammonemic encephalopathy by depleting N-acetylglutamate, inhibiting carbamoyl phosphate synthetase I in the urea cycle."
    },
    {
        "id": "exam3_g_h_u5_q7",
        "category": "Unit 05: Epilepsy",
        "subcategory": "Absence Seizures",
        "question_type": "clinical_vignette",
        "stem": "A 7-year-old girl has multiple daily episodes of blank staring lasting six seconds, accompanied by subtle rhythmic eye blinking, with immediate resumption of normal conversation and no postictal confusion. EEG shows generalized 3-Hz spike-and-wave discharges reliably provoked by hyperventilation. What is the precise molecular target of the first-line pharmacotherapeutic agent indicated for this condition?",
        "options": [
            {"label": "A", "text": "Low-threshold T-type voltage-gated calcium channels in thalamic relay neurons", "is_correct": True},
            {"label": "B", "text": "Presynaptic high-voltage-activated N-type calcium channels in the cortex", "is_correct": False},
            {"label": "C", "text": "Postsynaptic GABA-A receptor chloride channels in the reticular nucleus", "is_correct": False},
            {"label": "D", "text": "Fast-inactivating voltage-gated sodium channels in hippocampal CA1 neurons", "is_correct": False},
            {"label": "E", "text": "Synaptic vesicle glycoprotein SV2A preventing vesicular glutamate release", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "This child has classic absence (petit mal) seizures characterized by brief staring spells without postictal confusion and 3-Hz spike-and-wave EEG pattern. The first-line drug is ethosuximide. Ethosuximide specifically blocks low-threshold T-type voltage-gated calcium channels in thalamic relay neurons, disrupting the rhythmic thalamocortical oscillatory burst-firing that drives absence seizures.",
        "high_yield_takeaway": "Ethosuximide is first-line for absence seizures and works by blocking low-threshold T-type calcium channels in thalamic relay neurons."
    },
    {
        "id": "exam3_g_h_u5_q8",
        "category": "Unit 05: Epilepsy",
        "subcategory": "Antiseizure Pharmacology",
        "question_type": "clinical_vignette",
        "stem": "A 35-year-old woman taking topiramate for focal epilepsy presents with acute severe right flank pain radiating to her groin and gross hematuria. Non-contrast CT confirms a calcium phosphate nephrolithiasis. Serum chemistry shows a normal anion gap metabolic acidosis with a serum bicarbonate of 17 mEq/L. What enzymatic inhibition explains both her systemic acidosis and her predisposition to kidney stone formation?",
        "options": [
            {"label": "A", "text": "Carbonic anhydrase inhibition reducing renal proximal tubular bicarbonate reabsorption", "is_correct": True},
            {"label": "B", "text": "Xanthine oxidase inhibition promoting accumulation of insoluble purine crystals", "is_correct": False},
            {"label": "C", "text": "HMG-CoA reductase inhibition decreasing renal synthesis of protective prostaglandins", "is_correct": False},
            {"label": "D", "text": "Succinate dehydrogenase inhibition disrupting the mitochondrial Krebs cycle", "is_correct": False},
            {"label": "E", "text": "Renal 1-alpha-hydroxylase inhibition producing severe hypocalcemia and tetany", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "Topiramate is a sulfamate-substituted monosaccharide that weakly inhibits carbonic anhydrase (isozymes II and IV) in renal proximal tubule cells. This causes impaired bicarbonate reabsorption, leading to alkaline urine, systemic non-anion gap metabolic acidosis, and decreased urinary citrate excretion (hypocitraturia). Low citrate combined with alkaline urine precipitates calcium phosphate kidney stones.",
        "high_yield_takeaway": "Topiramate inhibits carbonic anhydrase, causing metabolic acidosis, hypocitraturia, and calcium phosphate kidney stones (nephrolithiasis)."
    },
    {
        "id": "exam3_g_h_u5_q9",
        "category": "Unit 05: Epilepsy",
        "subcategory": "Pediatric Epilepsy",
        "question_type": "clinical_vignette",
        "stem": "A 6-month-old infant with tuberous sclerosis develops clusters of myoclonic flexor spasms (salaam spasms) on awakening, with an EEG demonstrating hypsarrhythmia (West syndrome). The pediatric neurologist prescribes vigabatrin. What irreversible, dose-cumulative sensory toxicity mandates serial baseline and ongoing ophthalmologic visual field evaluations in this infant?",
        "options": [
            {"label": "A", "text": "Permanent bilateral concentric visual field constriction from retinal toxicity", "is_correct": True},
            {"label": "B", "text": "Accelerated posterior subcapsular cataract formation in bilateral lenses", "is_correct": False},
            {"label": "C", "text": "Rapid fibrovascular proliferation leading to tractional retinal detachment", "is_correct": False},
            {"label": "D", "text": "Ischemic optic neuropathy resulting from choroidal microvascular occlusion", "is_correct": False},
            {"label": "E", "text": "Acute closed-angle glaucoma secondary to anterior pupillary block", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "Vigabatrin is an irreversible inhibitor of GABA transaminase (the enzyme that degrades GABA), increasing brain GABA concentrations; it is the drug of choice for infantile spasms associated with tuberous sclerosis. However, vigabatrin carries a black-box warning for permanent, irreversible concentric peripheral visual field constriction in 30-40% of patients due to retinal amacrine and ganglion cell toxicity.",
        "high_yield_takeaway": "Vigabatrin (GABA transaminase inhibitor) is first-line for infantile spasms in tuberous sclerosis but can cause irreversible peripheral visual field constriction."
    },
    {
        "id": "exam3_g_h_u5_q10",
        "category": "Unit 05: Epilepsy",
        "subcategory": "Antiseizure Pharmacology",
        "question_type": "clinical_vignette",
        "stem": "A 30-year-old man with refractory focal epilepsy receives an antiseizure medication that does not alter voltage-gated sodium channels or GABA receptor kinetics. Instead, it selectively binds to a specific integral transmembrane glycoprotein residing on presynaptic synaptic vesicles, inhibiting calcium-dependent neurotransmitter exocytosis. What is the molecular pharmacological target of this drug?",
        "options": [
            {"label": "A", "text": "Synaptic vesicle protein 2A targeted by levetiracetam", "is_correct": True},
            {"label": "B", "text": "Alpha-2-delta auxiliary calcium channel subunit targeted by gabapentin", "is_correct": False},
            {"label": "C", "text": "GABA transporter 1 reuptake pump targeted by tiagabine", "is_correct": False},
            {"label": "D", "text": "AMPA-type ionotropic glutamate receptor targeted by perampanel", "is_correct": False},
            {"label": "E", "text": "Neuronal potassium channel subfamily KCNQ2/3 targeted by ezogabine", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "Levetiracetam (Keppra) has a unique mechanism of action: it binds stereoselectively to synaptic vesicle protein 2A (SV2A) on presynaptic vesicles. This modulates synaptic vesicle fusion and reduces the calcium-dependent release of excitatory neurotransmitters (such as glutamate) during high-frequency epileptiform trains.",
        "high_yield_takeaway": "Levetiracetam binds presynaptic vesicle protein SV2A, inhibiting glutamate exocytosis."
    },
    {
        "id": "exam3_g_h_u5_q11",
        "category": "Unit 05: Epilepsy",
        "subcategory": "Temporal Lobe Epilepsy",
        "question_type": "clinical_vignette",
        "stem": "A 28-year-old woman presents with stereotyped episodes beginning with a rising epigastric sensation ('butterflies in stomach') and intense déjà vu, followed by motionless blank staring, lip smacking, right-hand picking automatisms, and ninety seconds of unresponsiveness with postictal amnesia. Coronal T2-weighted MRI shows right hippocampal atrophy and hyperintensity. What is the classic histopathologic finding in this resected hippocampal tissue?",
        "options": [
            {"label": "A", "text": "Marked pyramidal neuronal loss with dense fibrillary astrogliosis in CA1 and CA4", "is_correct": True},
            {"label": "B", "text": "Extensive neurofibrillary tangles composed of hyperphosphorylated tau proteins", "is_correct": False},
            {"label": "C", "text": "Intracellular Lewy bodies containing aggregated alpha-synuclein polymers", "is_correct": False},
            {"label": "D", "text": "Perivascular lymphohistiocytic cuffing with viral Cowdry A inclusion bodies", "is_correct": False},
            {"label": "E", "text": "Widespread cortical microvacuolation and spongiform neuronal degeneration", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "This patient has mesial temporal lobe epilepsy (MTLE), the most common refractory focal epilepsy syndrome in adults, characterized by epigastric auras, autonomic/psychic sensations, automatisms, and impaired awareness. The underlying etiology is hippocampal sclerosis (mesial temporal sclerosis), histologically characterized by selective neuronal loss and dense astrogliosis in the Sommer sector (CA1), end-folium (CA4), and dentate gyrus, with relative sparing of CA2.",
        "high_yield_takeaway": "Mesial temporal lobe epilepsy is caused by hippocampal sclerosis, characterized by neuronal loss and astrogliosis in hippocampal CA1/CA4 subfields."
    },
    {
        "id": "exam3_g_h_u5_q12",
        "category": "Unit 05: Epilepsy",
        "subcategory": "Adverse Drug Reactions",
        "question_type": "clinical_vignette",
        "stem": "A 58-year-old man started on carbamazepine for trigeminal neuralgia three weeks ago presents with progressive lethargy, headache, and mild nausea. Serum electrolytes reveal a sodium of 122 mEq/L, serum osmolality of 252 mOsm/kg, and urine sodium of 46 mEq/L with urine osmolality of 520 mOsm/kg. He is euvolemic on examination. What mechanism accounts for this electrolyte abnormality?",
        "options": [
            {"label": "A", "text": "Syndrome of inappropriate antidiuresis via enhanced renal collecting duct V2 response", "is_correct": True},
            {"label": "B", "text": "Aldosterone receptor antagonism producing isolated mineralocorticoid resistance", "is_correct": False},
            {"label": "C", "text": "Osmotic natriuresis secondary to competitive proximal tubule sodium cotransport", "is_correct": False},
            {"label": "D", "text": "Drug-induced interstitial nephritis impairing medullary countercurrent gradients", "is_correct": False},
            {"label": "E", "text": "Direct stimulation of central thirst osmoreceptors causing psychogenic polydipsia", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "Carbamazepine (and its derivative oxcarbazepine) is a well-known cause of the syndrome of inappropriate antidiuretic hormone secretion (SIADH). Carbamazepine both increases hypothalamic release of vasopressin (ADH) and enhances the sensitivity of renal medullary collecting duct V2 receptors to circulating ADH, leading to excessive water reabsorption, concentrated urine (urine Osm >100), and euvolemic hypoosmolar hyponatremia.",
        "high_yield_takeaway": "Carbamazepine can cause SIADH (euvolemic hyponatremia) by increasing ADH release and enhancing renal collecting duct V2 sensitivity."
    },
    {
        "id": "exam3_g_h_u5_q13",
        "category": "Unit 05: Epilepsy",
        "subcategory": "Teratogenicity",
        "question_type": "clinical_vignette",
        "stem": "A 23-year-old woman with generalized epilepsy managed with valproate conceives unexpectedly. High-resolution anatomical fetal ultrasound at eighteen weeks reveals a lumbar neural tube defect (myelomeningocele) and mild ventriculomegaly, with markedly elevated maternal serum alpha-fetoprotein. What cellular biochemical mechanism underlies valproate-induced neural tube defects during early embryogenesis?",
        "options": [
            {"label": "A", "text": "Inhibition of histone deacetylases and antagonism of folate-dependent one-carbon metabolism", "is_correct": True},
            {"label": "B", "text": "Selective blockage of neural crest cell migration via cadherin downregulation", "is_correct": False},
            {"label": "C", "text": "Direct mutagenesis causing trinucleotide expansion in homeobox developmental genes", "is_correct": False},
            {"label": "D", "text": "Destruction of fetal thyroid follicles resulting in profound intrauterine cretinism", "is_correct": False},
            {"label": "E", "text": "Arrest of embryonic cardiac looping via endocardial cushion apoptosis", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "Valproate is the most teratogenic antiseizure medication, conferring a 1-2% risk of neural tube defects (spina bifida aperta / myelomeningocele). Valproate interferes with folate-mediated one-carbon metabolism, downregulates folate receptors, and acts as a potent inhibitor of histone deacetylases (HDACs), inducing chromatin remodeling and aberrant gene expression during neural tube closure (days 24-28 of embryonic development).",
        "high_yield_takeaway": "Valproate is a potent teratogen that causes neural tube defects by inhibiting histone deacetylases (HDACs) and antagonizing folate metabolism."
    },
    {
        "id": "exam3_g_h_u5_q14",
        "category": "Unit 05: Epilepsy",
        "subcategory": "Refractory Status Epilepticus",
        "question_type": "clinical_vignette",
        "stem": "A 45-year-old man in convulsive status epilepticus remains in persistent electrographic and clinical seizure activity at thirty-five minutes despite full weight-based intravenous lorazepam, fosphenytoin, and levetiracetam infusions. He is intubated and started on a continuous propofol infusion with continuous bedside electroencephalography. What specific electroencephalographic pattern is the primary therapeutic target when titrating general anesthetics in refractory status epilepticus?",
        "options": [
            {"label": "A", "text": "Burst suppression pattern with periods of generalized flatline inactivity", "is_correct": True},
            {"label": "B", "text": "Continuous generalized high-voltage polymorphic delta background slowing", "is_correct": False},
            {"label": "C", "text": "Symmetrical frontally predominant sleep spindles and vertex K-complexes", "is_correct": False},
            {"label": "D", "text": "Periodic lateralized epileptiform discharges occurring once every two seconds", "is_correct": False},
            {"label": "E", "text": "Continuous low-voltage fast beta activity exceeding twenty-five hertz", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "Refractory status epilepticus (persisting despite benzodiazepine and second-line ASM) requires continuous intravenous anesthetic infusions (propofol, midazolam, or pentobarbital). Anesthetics are titrated to continuous electroencephalographic (cEEG) cessation of all electrographic seizure activity or to a burst-suppression pattern (brief bursts of brain electrical activity separated by 5-15 seconds of flatline isoelectric silence) maintained for 24-48 hours.",
        "high_yield_takeaway": "In refractory status epilepticus, continuous IV anesthetics are titrated on EEG to achieve a burst suppression pattern or complete electrographic seizure cessation."
    },
    {
        "id": "exam3_g_h_u5_q15",
        "category": "Unit 05: Epilepsy",
        "subcategory": "Postictal Phenomena",
        "question_type": "clinical_vignette",
        "stem": "A 62-year-old man experiences a two-minute focal motor seizure involving clonic contractions of his left face and left upper extremity. Immediately following seizure cessation, he has a flaccid left hemiplegia and left facial droop with normal consciousness. Non-contrast head CT and CT angiography show no acute intracranial hemorrhage or large vessel occlusion. Over the subsequent four hours, his motor strength recovers completely to 5/5. What is the physiological mechanism of this transient postictal paresis (Todd paralysis)?",
        "options": [
            {"label": "A", "text": "Transient motor cortex neuronal metabolic exhaustion and active synaptic hyperpolarization", "is_correct": True},
            {"label": "B", "text": "Spontaneous thromboembolic occlusion followed by rapid endogenous tissue tPA lysis", "is_correct": False},
            {"label": "C", "text": "Transient compression of the corticospinal tract by acute focal vasogenic edema", "is_correct": False},
            {"label": "D", "text": "Acute depletion of acetylcholine stores at the skeletal neuromuscular junction", "is_correct": False},
            {"label": "E", "text": "Reversible demyelinating conduction block along the descending internal capsule", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "Todd paralysis (Todd paresis) is a transient focal neurological deficit (most commonly motor weakness) following a seizure, typically lasting minutes to a few hours (rarely up to 24-48 hours). The pathophysiology involves prolonged postictal neuronal depression, energy/metabolite (ATP, glucose) exhaustion in overactivated epileptogenic motor networks, and intense, active GABAergic synaptic hyperpolarization.",
        "high_yield_takeaway": "Todd paralysis is transient postictal focal paresis caused by localized neuronal metabolic exhaustion and synaptic hyperpolarization following a seizure."
    },
    {
        "id": "exam3_g_h_u5_q16",
        "category": "Unit 05: Epilepsy",
        "subcategory": "Seizure Classification",
        "question_type": "clinical_vignette",
        "stem": "A 9-year-old child is evaluated for classroom staring spells. During an observed episode, she suddenly stops speaking for seven seconds with rapid eye blinking, then immediately resumes reading her textbook at the exact sentence where she left off, completely unaware that any time elapsed. Which clinical feature definitively distinguishes this absence seizure from a focal impaired-awareness seizure of temporal lobe origin?",
        "options": [
            {"label": "A", "text": "Instantaneous recovery to baseline cognitive function without a postictal confusional period", "is_correct": True},
            {"label": "B", "text": "Presence of subtle bilateral facial automatisms during the period of unresponsiveness", "is_correct": False},
            {"label": "C", "text": "Occurrence of brief retrograde amnesia encompassing events prior to the seizure", "is_correct": False},
            {"label": "D", "text": "Complete absence of any motor movements during the entire episode duration", "is_correct": False},
            {"label": "E", "text": "Preceding visceral epigastric rising sensation lasting thirty seconds", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "The critical distinguishing feature between typical absence seizures and focal impaired-awareness (complex partial) seizures is the duration and postictal state. Typical absence seizures last brief seconds (<10-15 s) and resolve instantly with immediate, seamless return to baseline activity and zero postictal confusion. In contrast, focal impaired-awareness seizures last longer (1-2 minutes), often feature complex automatisms, and characteristically leave the patient with minutes of postictal confusion.",
        "high_yield_takeaway": "Absence seizures last seconds and end instantaneously without postictal confusion; focal impaired-awareness seizures last minutes and have prominent postictal confusion."
    },
    {
        "id": "exam3_g_h_u5_q17",
        "category": "Unit 05: Epilepsy",
        "subcategory": "Adverse Drug Reactions",
        "question_type": "clinical_vignette",
        "stem": "A 24-year-old man who has been taking phenytoin for two years presents with progressive, firm, fibrous overgrowth of his gums that now covers nearly half the crowns of his anterior teeth. Biopsy of the gingival tissue shows extensive collagen deposition and hyperplastic stroma without malignant atypia. Which growth factor overexpressed in response to phenytoin mediates this gingival fibrous hyperplasia?",
        "options": [
            {"label": "A", "text": "Platelet-derived growth factor stimulating gingival fibroblast proliferation", "is_correct": True},
            {"label": "B", "text": "Vascular endothelial growth factor inducing mucosal capillary cavernomas", "is_correct": False},
            {"label": "C", "text": "Epidermal growth factor driving squamous epithelial keratinization", "is_correct": False},
            {"label": "D", "text": "Insulin-like growth factor 1 causing generalized mucosal acromegaloid hypertrophy", "is_correct": False},
            {"label": "E", "text": "Tumor necrosis factor alpha activating stromal matrix metalloproteinases", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "Phenytoin causes gingival hyperplasia in up to 50% of chronic users. Phenytoin and its metabolites stimulate the expression of platelet-derived growth factor (PDGF) and transforming growth factor-beta (TGF-beta) in gingival fibroblasts, which drives excessive synthesis of collagen and proteoglycans. Good oral hygiene reduces severity, and regression typically occurs after drug discontinuation.",
        "high_yield_takeaway": "Phenytoin-induced gingival hyperplasia is mediated by increased platelet-derived growth factor (PDGF) stimulating fibroblast collagen synthesis."
    },
    {
        "id": "exam3_g_h_u5_q18",
        "category": "Unit 05: Epilepsy",
        "subcategory": "Juvenile Myoclonic Epilepsy",
        "question_type": "clinical_vignette",
        "stem": "A 17-year-old high school student presents after suffering a first generalized tonic-clonic seizure following overnight studying. On direct questioning, he admits that for the past year he has had brief, shock-like morning jerks in both arms that occasionally cause him to drop breakfast items or his toothbrush. EEG shows generalized 4- to 6-Hz polyspike-and-wave discharges. Which antiseizure medication represents the drug of choice for this condition, and which class must be avoided due to the risk of paradoxically aggravating these myoclonic seizures?",
        "options": [
            {"label": "A", "text": "Valproate is first-line; sodium-channel blockers like carbamazepine must be avoided", "is_correct": True},
            {"label": "B", "text": "Carbamazepine is first-line; broad-spectrum agents like valproate must be avoided", "is_correct": False},
            {"label": "C", "text": "Ethosuximide is first-line; benzodiazepines like clonazepam must be avoided", "is_correct": False},
            {"label": "D", "text": "Phenytoin is first-line; calcium-channel modulators like gabapentin must be avoided", "is_correct": False},
            {"label": "E", "text": "Phenobarbital is first-line; synaptic vesicle ligands like levetiracetam must be avoided", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "Juvenile Myoclonic Epilepsy (JME, Janz syndrome) presents in adolescence with morning myoclonic jerks (often dropping objects after waking), generalized tonic-clonic seizures, and occasional absence seizures, with 4-6 Hz polyspike-and-wave EEG. The drug of choice is broad-spectrum valproate (or levetiracetam/lamotrigine in women of childbearing potential). Narrow-spectrum sodium channel blockers (carbamazepine, phenytoin) and GABA analogs (gabapentin, vigabatrin) can paradoxically worsen myoclonic seizures.",
        "high_yield_takeaway": "JME (morning arm jerks + GTC) is treated with valproate; narrow-spectrum sodium channel blockers (carbamazepine, phenytoin) can worsen myoclonic seizures."
    },
    {
        "id": "exam3_g_h_u5_q19",
        "category": "Unit 05: Epilepsy",
        "subcategory": "Antiseizure Pharmacology",
        "question_type": "clinical_vignette",
        "stem": "A 54-year-old man with focal epilepsy on adjunctive lacosamide undergoes a routine electrocardiogram that demonstrates a PR interval prolongation of 240 milliseconds without QRS widening. What unique electrophysiological mechanism of action distinguishes lacosamide from traditional sodium channel blockers such as phenytoin and carbamazepine?",
        "options": [
            {"label": "A", "text": "Selective enhancement of the slow inactivation state of voltage-gated sodium channels", "is_correct": True},
            {"label": "B", "text": "Competitive blockade of fast inactivation gates on voltage-gated sodium channels", "is_correct": False},
            {"label": "C", "text": "Permanent irreversible alkylation of pore-forming alpha subunits in Purkinje cells", "is_correct": False},
            {"label": "D", "text": "Selective opening of inward rectifying potassium channels in cardiac myocytes", "is_correct": False},
            {"label": "E", "text": "Direct inhibition of sarcoplasmic reticulum calcium ATPase in the sinoatrial node", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "Traditional sodium channel blockers (phenytoin, carbamazepine, lamotrigine) bind to and stabilize the fast-inactivated state of voltage-gated sodium channels. In contrast, lacosamide selectively enhances slow inactivation of voltage-gated sodium channels, terminating sustained repetitive burst firing without affecting physiological rapid action potentials. Lacosamide can prolong the PR interval, necessitating caution in patients with cardiac conduction disease.",
        "high_yield_takeaway": "Lacosamide selectively enhances the slow inactivation of voltage-gated sodium channels and can cause PR interval prolongation."
    },
    {
        "id": "exam3_g_h_u5_q20",
        "category": "Unit 05: Epilepsy",
        "subcategory": "Psychogenic Non-Epileptic Seizures",
        "question_type": "clinical_vignette",
        "stem": "A 26-year-old woman is admitted to the continuous video-EEG monitoring unit for evaluation of daily drug-resistant seizures. During an observed episode, she exhibits asynchronous, out-of-phase thrashing of all four limbs, forceful pelvic thrusting, side-to-side head shaking, and tightly closed eyes that actively resist manual opening by the examiner. Concurrent continuous electroencephalography shows a normal posterior dominant alpha rhythm with muscle artifact and no epileptiform discharges. Which physical examination sign during an episode is most specific for psychogenic non-epileptic seizures?",
        "options": [
            {"label": "A", "text": "Active resistance to forced passive eye opening with forceful eyelid closure", "is_correct": True},
            {"label": "B", "text": "Presence of bilateral plantar extensor responses immediately after the event", "is_correct": False},
            {"label": "C", "text": "Transient elevation of serum prolactin measured twenty minutes post-ictus", "is_correct": False},
            {"label": "D", "text": "Lateral tongue biting along the border of the anterior two-thirds of the tongue", "is_correct": False},
            {"label": "E", "text": "Development of postictal stertorous snoring breathing with metabolic lactic acidosis", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "Psychogenic Non-Epileptic Seizures (PNES) are functional neurological disorders mimicking epilepsy. Key semiological signs include out-of-phase limb movements, pelvic thrusting, head shaking ('no-no' motions), preserved consciousness during bilateral movements, absence of postictal confusion, and crucially, forced eyelid closure with active resistance to examiner opening (epileptic seizures typically feature open eyes). Normal EEG during an active event confirms the non-epileptic nature.",
        "high_yield_takeaway": "PNES is characterized by active resistance to eye opening, pelvic thrusting, out-of-phase movements, and normal concurrent EEG without postictal prolactin surge."
    }
]

if __name__ == "__main__":
    for q in u5_questions:
        check_q(q)
    print("gen_g_h_u5.py: All 20 questions passed validation!")
