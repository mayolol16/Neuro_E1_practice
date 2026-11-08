import json
from test_gen_structure import check_q

u4_questions = [
    {
        "id": "exam3_g_h_u4_q1",
        "category": "Unit 04: Infections",
        "subcategory": "Bacterial Meningitis",
        "question_type": "clinical_vignette",
        "stem": "A 56-year-old man presents with high fever, severe headache, confusion, and marked nuchal rigidity. Lumbar puncture demonstrates an opening pressure of 260 mm H2O, WBC count of 2,400/uL with 92% neutrophils, protein of 280 mg/dL, and glucose of 18 mg/dL. In addition to intravenous vancomycin and ceftriaxone, ampicillin is added to his empiric regimen. What specific microbiological coverage justifies the addition of ampicillin in this age cohort?",
        "options": [
            {"label": "A", "text": "Listeria monocytogenes exhibiting inherent resistance to third-generation cephalosporins", "is_correct": True},
            {"label": "B", "text": "Pseudomonas aeruginosa requiring double coverage with extended-spectrum penicillins", "is_correct": False},
            {"label": "C", "text": "Beta-lactamase producing strains of Neisseria meningitidis endemic to adults", "is_correct": False},
            {"label": "D", "text": "Atypical Mycoplasma hominis invading the blood-brain barrier via tight junctions", "is_correct": False},
            {"label": "E", "text": "Methicillin-susceptible Staphylococcus aureus seeding from paranasal sinuses", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "Adults older than 50 years and immunocompromised patients are at increased risk for meningitis caused by Listeria monocytogenes, a facultative intracellular Gram-positive bacillus acquired through unpasteurized dairy or processed meats. Listeria is inherently resistant to all cephalosporins due to low-affinity penicillin-binding proteins (PBPs), mandating the addition of ampicillin to empiric vancomycin and ceftriaxone.",
        "high_yield_takeaway": "Empiric meningitis therapy in adults >50 or immunocompromised requires ampicillin to cover Listeria monocytogenes, which is inherently resistant to cephalosporins."
    },
    {
        "id": "exam3_g_h_u4_q2",
        "category": "Unit 04: Infections",
        "subcategory": "Bacterial Meningitis",
        "question_type": "clinical_vignette",
        "stem": "A 46-year-old woman is diagnosed with acute pneumococcal meningitis confirmed by cerebrospinal fluid Gram stain showing Gram-positive lancet-shaped diplococci. The emergency physician administers intravenous dexamethasone fifteen minutes prior to the first dose of bactericidal antibiotics. What clinical outcome is specifically targeted by this timed administration of glucocorticoid therapy?",
        "options": [
            {"label": "A", "text": "Reduction in sensorineural hearing loss and neurological disability from cytokine release", "is_correct": True},
            {"label": "B", "text": "Direct inhibition of bacterial autolysin enzymes responsible for cell wall turnover", "is_correct": False},
            {"label": "C", "text": "Enhancement of vancomycin penetration through the intact blood-brain barrier", "is_correct": False},
            {"label": "D", "text": "Prevention of secondary systemic vasodilation and early septic cardiovascular collapse", "is_correct": False},
            {"label": "E", "text": "Acceleration of cerebrospinal fluid reabsorption across the arachnoid villi", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "Antibiotic-induced lysis of Streptococcus pneumoniae releases cell-wall fragments (peptidoglycan and teichoic acid) that stimulate intense subarachnoid cytokine production (TNF-alpha, IL-1), worsening cerebral edema, intracranial pressure, and cochlear damage. Administering dexamethasone before or with the first antibiotic dose blunts this hyperinflammatory cascade, significantly decreasing sensorineural hearing loss and mortality.",
        "high_yield_takeaway": "Dexamethasone administered before or with the first antibiotic dose in pneumococcal meningitis reduces inflammatory hearing loss and mortality."
    },
    {
        "id": "exam3_g_h_u4_q3",
        "category": "Unit 04: Infections",
        "subcategory": "Bacterial Meningitis",
        "question_type": "clinical_vignette",
        "stem": "A 19-year-old college freshman with culture-confirmed Neisseria meningitidis bacteremia abruptly deteriorates over three hours, developing widespread purpura fulminans, refractory shock, profound metabolic acidosis, and bilateral flank pain. Autopsy reveals extensive bilateral adrenal hemorrhage with cortical necrosis (Waterhouse-Friderichsen syndrome). What physiological failure directly caused his circulatory collapse?",
        "options": [
            {"label": "A", "text": "Acute primary adrenal insufficiency with severe cortisol and aldosterone depletion", "is_correct": True},
            {"label": "B", "text": "Massive release of myocardial depressant factors from pulmonary alveoli", "is_correct": False},
            {"label": "C", "text": "Rupture of internal carotid mycotic aneurysms into the subarachnoid space", "is_correct": False},
            {"label": "D", "text": "Loss of medullary sympathetic outflow from cerebellar tonsillar herniation", "is_correct": False},
            {"label": "E", "text": "Complete heart block from septic embolization into the cardiac bundle of His", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "Waterhouse-Friderichsen syndrome is a devastating complication of severe meningococcemia characterized by endotoxin-driven disseminated intravascular coagulation (DIC), purpuric rash, and bilateral adrenal gland hemorrhage. Adrenal destruction results in acute primary adrenal insufficiency with profound loss of cortisol and aldosterone, causing vasopressor-refractory hypovolemic and distributive shock.",
        "high_yield_takeaway": "Waterhouse-Friderichsen syndrome in meningococcemia causes bilateral adrenal cortical hemorrhage, acute adrenal crisis, and refractory shock."
    },
    {
        "id": "exam3_g_h_u4_q4",
        "category": "Unit 04: Infections",
        "subcategory": "Bacterial Meningitis Prophylaxis",
        "question_type": "clinical_vignette",
        "stem": "A respiratory therapist performs emergent endotracheal intubation on a patient with fulminant Neisseria meningitidis meningitis during which she is directly exposed to respiratory droplets without eye or face protection. What chemoprophylactic regimen and corresponding mechanism of action are indicated to eradicate nasopharyngeal carriage in this exposed healthcare worker?",
        "options": [
            {"label": "A", "text": "Rifampin via inhibition of bacterial DNA-dependent RNA polymerase transcription", "is_correct": True},
            {"label": "B", "text": "Amoxicillin via inhibition of transpeptidase-mediated peptidoglycan crosslinking", "is_correct": False},
            {"label": "C", "text": "Azithromycin via reversible binding to the 50S bacterial ribosomal subunit", "is_correct": False},
            {"label": "D", "text": "Trimethoprim-sulfamethoxazole via sequential block of folate enzymatic synthesis", "is_correct": False},
            {"label": "E", "text": "Doxycycline via binding to the 30S ribosomal subunit preventing tRNA docking", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "Close contacts of patients with invasive meningococcal disease (including healthcare workers with direct respiratory droplet exposure) require chemoprophylaxis to eradicate nasopharyngeal colonization. First-line prophylaxis is oral rifampin (which inhibits bacterial DNA-dependent RNA polymerase) for 2 days. Single-dose ciprofloxacin or ceftriaxone IM are alternative regimens.",
        "high_yield_takeaway": "Meningococcal close-contact chemoprophylaxis is achieved with rifampin (DNA-dependent RNA polymerase inhibitor), ciprofloxacin, or ceftriaxone."
    },
    {
        "id": "exam3_g_h_u4_q5",
        "category": "Unit 04: Infections",
        "subcategory": "Viral Encephalitis",
        "question_type": "clinical_vignette",
        "stem": "A 34-year-old man presents with acute confusion, bizarre behavior, fever, and olfactory hallucinations. Brain MRI shows asymmetric hyperintensity and petechial hemorrhage localized to the left anteromedial temporal and inferior frontal lobes. CSF shows lymphocytic pleocytosis with 450 RBCs/uL. He is immediately started on intravenous acyclovir. What viral enzyme is obligatorily required for the initial rate-limiting monophosphorylation of this therapeutic agent?",
        "options": [
            {"label": "A", "text": "Herpesvirus thymidine kinase activating the acyclovir nucleoside analog", "is_correct": True},
            {"label": "B", "text": "Host cell cellular kinase converting acyclovir directly into its active form", "is_correct": False},
            {"label": "C", "text": "Viral RNA-dependent RNA polymerase incorporating fraudulent purine bases", "is_correct": False},
            {"label": "D", "text": "Host mitochondrial ribonucleotide reductase generating deoxyribonucleotides", "is_correct": False},
            {"label": "E", "text": "Herpesvirus topoisomerase II unwinding double-stranded viral DNA strands", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "Herpes simplex virus type 1 (HSV-1) encephalitis causes hemorrhagic necrotizing encephalitis localized to the temporal and inferior frontal lobes. Treatment is immediate IV acyclovir. Acyclovir is a guanosine analogue that requires initial monophosphorylation by viral-encoded thymidine kinase. Host cellular kinases then convert it to acyclovir triphosphate, which selectively inhibits viral DNA polymerase and acts as a DNA chain terminator.",
        "high_yield_takeaway": "HSV-1 temporal encephalitis is treated with acyclovir, which requires viral thymidine kinase for initial monophosphorylation before host kinases produce active triphosphate."
    },
    {
        "id": "exam3_g_h_u4_q6",
        "category": "Unit 04: Infections",
        "subcategory": "Varicella-Zoster Virus",
        "question_type": "clinical_vignette",
        "stem": "A 64-year-old man presents with severe lancinating pain deep within his right ear canal, followed three days later by a vesicular rash on the right external auditory concha, complete right-sided facial weakness including the forehead, and vertigo with horizontal nystagmus (Ramsay Hunt syndrome). Reactivation of latent varicella-zoster virus within which sensory ganglion accounts for this clinical syndrome?",
        "options": [
            {"label": "A", "text": "Geniculate ganglion of the facial nerve within the petrous temporal bone", "is_correct": True},
            {"label": "B", "text": "Trigeminal semilunar ganglion located in the floor of the middle cranial fossa", "is_correct": False},
            {"label": "C", "text": "Spiral ganglion located within the modiolus of the bony cochlear canal", "is_correct": False},
            {"label": "D", "text": "Superior jugular ganglion of the glossopharyngeal nerve at the foramen", "is_correct": False},
            {"label": "E", "text": "Ciliary parasympathetic ganglion situated in the posterior orbital apex", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "Ramsay Hunt syndrome (herpes zoster oticus) is caused by reactivation of latent varicella-zoster virus (VZV) in the geniculate ganglion of cranial nerve VII. The viral spread causes painful vesicular eruption in the external auditory canal and concha (sensory branch of CN VII), peripheral facial nerve palsy (including forehead), and vestibulocochlear symptoms (vertigo, tinnitus, sensorineural hearing loss) due to proximity of CN VIII.",
        "high_yield_takeaway": "Ramsay Hunt syndrome is caused by VZV reactivation in the geniculate ganglion of CN VII, causing ear vesicles, facial palsy, and vestibulocochlear symptoms."
    },
    {
        "id": "exam3_g_h_u4_q7",
        "category": "Unit 04: Infections",
        "subcategory": "Rhabdovirus & Axonal Transport",
        "question_type": "clinical_vignette",
        "stem": "An 8-year-old boy bitten on the hand by a bat in an unexplored cave six weeks earlier develops fever, severe agitation, autonomic instability, and violent pharyngeal muscle spasms triggered by attempts to swallow water (hydrophobia). What motor transport protein mediated the retrograde axonal transit of this bullet-shaped virus to the spinal cord, and what pathognomonic histology is seen at autopsy?",
        "options": [
            {"label": "A", "text": "Dynein motor proteins; eosinophilic intracytoplasmic Negri inclusion bodies", "is_correct": True},
            {"label": "B", "text": "Kinesin motor proteins; basophilic intranuclear Cowdry A inclusion bodies", "is_correct": False},
            {"label": "C", "text": "Myosin V molecular motors; widespread microglial nodules with neuronophagia", "is_correct": False},
            {"label": "D", "text": "Actin filament treadmilling; diffuse amyloid plaque deposition in cortex", "is_correct": False},
            {"label": "E", "text": "Tubulin dimer elongation; perivascular lymphocytic cuffing without inclusions", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "Rabies virus (bullet-shaped Rhabdovirus) binds nicotinic acetylcholine receptors at the neuromuscular junction and travels by retrograde axoplasmic transport mediated by dynein motor proteins to the central nervous system. Histopathologically, it is characterized by pathognomonic eosinophilic intracytoplasmic Negri bodies in hippocampal pyramidal neurons and cerebellar Purkinje cells.",
        "high_yield_takeaway": "Rabies travels via retrograde dynein transport to the CNS, producing hydrophobia, agitation, and pathognomonic intracytoplasmic Negri bodies in Purkinje and hippocampal cells."
    },
    {
        "id": "exam3_g_h_u4_q8",
        "category": "Unit 04: Infections",
        "subcategory": "Arboviruses",
        "question_type": "clinical_vignette",
        "stem": "A 68-year-old retired farmer living in the Midwest presents in August with high fever, mental confusion, prominent postural tremor, and sudden asymmetric flaccid paralysis of his right lower extremity. Deep tendon reflexes in the right patellar and Achilles tendons are completely absent without sensory deficits. CSF analysis reveals lymphocytic pleocytosis and West Nile virus IgM antibodies. What neuropathological lesion is responsible for this acute asymmetric flaccid weakness?",
        "options": [
            {"label": "A", "text": "Direct cytolytic viral destruction of spinal cord anterior horn alpha motor neurons", "is_correct": True},
            {"label": "B", "text": "Autoimmune demyelination of the lateral corticospinal tract in cervical cord", "is_correct": False},
            {"label": "C", "text": "Immune complex deposition within the anterior spinal artery vascular lumen", "is_correct": False},
            {"label": "D", "text": "Autoantibody blockade of voltage-gated calcium channels at motor terminals", "is_correct": False},
            {"label": "E", "text": "Bilateral demyelination of peripheral motor nerve roots at the cauda equina", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "West Nile virus (a mosquito-borne Flavivirus) can cause a poliomyelitis-like acute flaccid paralysis syndrome. The virus has a specific tropism for spinal anterior horn alpha motor neurons, causing direct cytolytic necrosis. This manifests as acute, asymmetric, flaccid weakness with hyporeflexia/areflexia and fasciculations without sensory loss (pure lower motor neuron pattern).",
        "high_yield_takeaway": "West Nile virus can cause acute asymmetric flaccid paralysis by directly destroying anterior horn motor neurons (poliomyelitis-like syndrome)."
    },
    {
        "id": "exam3_g_h_u4_q9",
        "category": "Unit 04: Infections",
        "subcategory": "Opportunistic Viral Demyelination",
        "question_type": "clinical_vignette",
        "stem": "A 39-year-old woman with relapsing-remitting multiple sclerosis who has been receiving natalizumab for three years develops progressive apathy, cognitive slowing, right homonymous hemianopia, and gait ataxia. Brain MRI demonstrates asymmetric, non-enhancing, scalloped white matter hyperintensities involving subcortical U-fibers without mass effect. Cerebrospinal fluid PCR confirms JC virus reactivation. Which specific glial cell type undergoes lytic infection and destruction by this polyomavirus?",
        "options": [
            {"label": "A", "text": "Myelinating oligodendrocytes exhibiting enlarged glassy basophilic nuclei", "is_correct": True},
            {"label": "B", "text": "Protoplasmic astrocytes forming extensive fibrillary glial scars", "is_correct": False},
            {"label": "C", "text": "Resident parenchymal microglia acting as central antigen-presenting cells", "is_correct": False},
            {"label": "D", "text": "Ciliated ependymal cells lining the walls of the cerebral aqueduct", "is_correct": False},
            {"label": "E", "text": "Endothelial cells forming the continuous tight junctions of brain capillaries", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "Progressive Multifocal Leukoencephalopathy (PML) is caused by reactivation of the JC polyomavirus in immunocompromised individuals or those on immunosuppressive monoclonals (e.g., natalizumab, efalizumab). JC virus selectively infects and lyses oligodendrocytes, leading to widespread multifocal demyelination. On histology, oligodendrocytes show enlarged nuclei packed with glassy basophilic viral inclusion bodies.",
        "high_yield_takeaway": "PML results from JC virus reactivation in immunosuppressed patients (or on natalizumab), selectively destroying oligodendrocytes to cause multifocal demyelination."
    },
    {
        "id": "exam3_g_h_u4_q10",
        "category": "Unit 04: Infections",
        "subcategory": "Cytomegalovirus",
        "question_type": "clinical_vignette",
        "stem": "A 32-year-old HIV-infected man with a CD4 count of 22/uL presents with delirium, confusion, lower extremity weakness, and urinary incontinence. Brain MRI shows thin periventricular subependymal enhancement lining the lateral and fourth ventricles. Histopathological examination of ventricular subependymal tissue demonstrates cytomegaly with prominent intranuclear basophilic inclusions surrounded by a clear halo ('owl-eye' appearance). What is the first-line therapeutic agent and its primary mechanism of action?",
        "options": [
            {"label": "A", "text": "Ganciclovir via inhibition of cytomegalovirus DNA polymerase chain elongation", "is_correct": True},
            {"label": "B", "text": "Foscarnet via selective antagonism of viral pyrophosphate binding domains", "is_correct": False},
            {"label": "C", "text": "Cidofovir via direct phosphorylation-independent incorporation into viral RNA", "is_correct": False},
            {"label": "D", "text": "Acyclovir via selective activation by cytomegaloviral thymidine kinase", "is_correct": False},
            {"label": "E", "text": "Ribavirin via competitive inhibition of inosine monophosphate dehydrogenase", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "Cytomegalovirus (CMV) encephalitis / ventriculoependymitis occurs in advanced AIDS (CD4 < 50/uL), presenting with periventricular rim enhancement, confusion, and radiculopathy. Histology characteristically shows cytomegalic cells with prominent intranuclear basophilic inclusion bodies with halos ('owl-eye'). First-line therapy is intravenous ganciclovir, which is phosphorylated by viral UL97 kinase and inhibits viral DNA polymerase.",
        "high_yield_takeaway": "CMV ventriculoencephalitis in advanced AIDS (CD4 < 50) presents with periventricular enhancement, 'owl-eye' inclusions, and is treated with ganciclovir."
    },
    {
        "id": "exam3_g_h_u4_q11",
        "category": "Unit 04: Infections",
        "subcategory": "Cryptococcal Meningitis",
        "question_type": "clinical_vignette",
        "stem": "A 41-year-old HIV-infected man with a CD4 count of 38/uL presents with a progressive, throbbing headache, low-grade fever, and photophobia over two weeks. Lumbar puncture demonstrates an elevated opening pressure of 340 mm H2O. CSF India ink preparation shows narrow-based budding encapsulated yeasts, and cryptococcal latex agglutination is strongly positive. In addition to serial lumbar punctures to control elevated intracranial pressure, which antimicrobial induction regimen is indicated?",
        "options": [
            {"label": "A", "text": "Liposomal amphotericin B combined with oral flucytosine for two weeks", "is_correct": True},
            {"label": "B", "text": "High-dose oral fluconazole monotherapy administered for ten weeks", "is_correct": False},
            {"label": "C", "text": "Intravenous voriconazole combined with caspofungin echinocandin therapy", "is_correct": False},
            {"label": "D", "text": "Intravenous trimethoprim-sulfamethoxazole with adjunctive corticosteroids", "is_correct": False},
            {"label": "E", "text": "Oral itraconazole maintenance therapy coupled with immediate antiretrovirals", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "Cryptococcal meningitis (Cryptococcus neoformans) is an opportunistic fungal infection in advanced AIDS (CD4 < 100/uL). The standard induction regimen is liposomal amphotericin B plus flucytosine for at least 2 weeks, followed by fluconazole consolidation. Managing elevated intracranial pressure (opening pressure >200-250 mm H2O) with therapeutic serial lumbar punctures is critical to prevent visual loss and herniation.",
        "high_yield_takeaway": "Cryptococcal meningitis in AIDS requires induction with amphotericin B plus flucytosine, along with serial lumbar punctures to relieve elevated intracranial pressure."
    },
    {
        "id": "exam3_g_h_u4_q12",
        "category": "Unit 04: Infections",
        "subcategory": "Antifungal Pharmacology",
        "question_type": "clinical_vignette",
        "stem": "In the induction management of cryptococcal meningoencephalitis, flucytosine is co-administered alongside amphotericin B to synergistically enhance fungal eradication. What is the precise molecular enzymatic pathway through which flucytosine exerts its selective cytotoxic action against fungal cells?",
        "options": [
            {"label": "A", "text": "Conversion to 5-fluorouracil by fungal cytosine deaminase, inhibiting thymidylate synthase", "is_correct": True},
            {"label": "B", "text": "Binding to membrane ergosterol to generate transmembrane ion-permeable channels", "is_correct": False},
            {"label": "C", "text": "Inhibition of fungal 14-alpha-demethylase preventing conversion of lanosterol", "is_correct": False},
            {"label": "D", "text": "Blockade of 1,3-beta-D-glucan synthase disrupting the structural fungal cell wall", "is_correct": False},
            {"label": "E", "text": "Disruption of mitotic spindle microtubules arresting fungal cells in metaphase", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "Flucytosine (5-fluorocytosine) enters fungal cells via cytosine permease and is converted into 5-fluorouracil (5-FU) by fungal cytosine deaminase (an enzyme absent in human cells). 5-FU is converted to 5-dUMP, which competitively inhibits thymidylate synthase, halting fungal DNA synthesis. Amphotericin B increases fungal cell membrane permeability, facilitating flucytosine entry.",
        "high_yield_takeaway": "Flucytosine is converted by fungal cytosine deaminase to 5-FU, inhibiting thymidylate synthase and blocking fungal DNA synthesis."
    },
    {
        "id": "exam3_g_h_u4_q13",
        "category": "Unit 04: Infections",
        "subcategory": "CNS Opportunistic Infections",
        "question_type": "clinical_vignette",
        "stem": "A 30-year-old HIV-infected man with a CD4 count of 45/uL presents with headaches and left-sided hemiparesis. Contrast brain MRI reveals multiple ring-enhancing lesions with surrounding edema located predominantly at the basal ganglia and corticomedullary junction. Serum IgG antibodies to Toxoplasma gondii are positive. What is the standard initial clinical management strategy?",
        "options": [
            {"label": "A", "text": "Empiric pyrimethamine, sulfadiazine, and leucovorin with repeat imaging in 14 days", "is_correct": True},
            {"label": "B", "text": "Emergent stereotactic brain biopsy prior to initiating any antimicrobial therapy", "is_correct": False},
            {"label": "C", "text": "Whole-brain radiation therapy combined with high-dose intravenous methotrexate", "is_correct": False},
            {"label": "D", "text": "Intravenous ganciclovir monotherapy directed against cytomegalovirus encephalitis", "is_correct": False},
            {"label": "E", "text": "Surgical craniotomy and evacuation of all ring-enhancing purulent abscesses", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "In an HIV patient with CD4 < 100/uL presenting with multiple ring-enhancing lesions and positive Toxoplasma IgG, the presumptive diagnosis is cerebral toxoplasmosis. The standard approach is an empiric trial of pyrimethamine + sulfadiazine + leucovorin (folinic acid to prevent bone marrow suppression). Clinical and radiologic response is expected within 10-14 days. If lesions enlarge or fail to respond, stereotactic biopsy is indicated to evaluate for primary CNS lymphoma.",
        "high_yield_takeaway": "Multiple ring-enhancing lesions in AIDS with CD4 < 100 warrant empiric pyrimethamine + sulfadiazine + leucovorin; biopsy is reserved for non-responders."
    },
    {
        "id": "exam3_g_h_u4_q14",
        "category": "Unit 04: Infections",
        "subcategory": "Parasitic CNS Infections",
        "question_type": "clinical_vignette",
        "stem": "A 28-year-old agricultural worker from rural Latin America presents with new-onset generalized seizures. Brain MRI shows multiple small cystic parenchymal lesions, including viable cysts with an eccentric mural nodule (representing an invaginated scolex) and multiple calcified granulomas. Through which transmission route did this patient acquire this neuroparasitic infection?",
        "options": [
            {"label": "A", "text": "Fecal-oral ingestion of Taenia solium eggs shed in the stool of a human tapeworm carrier", "is_correct": True},
            {"label": "B", "text": "Ingestion of undercooked pork contaminated with encysted larval Taenia solium cysticerci", "is_correct": False},
            {"label": "C", "text": "Direct percutaneous penetration by cercarial larvae swimming in freshwater irrigation", "is_correct": False},
            {"label": "D", "text": "Inhalation of infective embryonated ova carried in contaminated barnyard dust", "is_correct": False},
            {"label": "E", "text": "Bite of an infected reduviid bug defecating near the primary skin puncture wound", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "Neurocysticercosis is caused by ingestion of Taenia solium eggs via fecal-oral contamination from a human carrier of the adult intestinal tapeworm. Once ingested, oncospheres hatch, penetrate intestinal mucosa, and hematogenously spread to the brain (forming cystic lesions with a scolex). In contrast, eating undercooked pork containing larval cysticerci causes intestinal tapeworm infection (taeniasis), NOT cysticercosis.",
        "high_yield_takeaway": "Neurocysticercosis is caused by fecal-oral ingestion of Taenia solium eggs from human stool (eating contaminated undercooked pork causes adult intestinal taeniasis)."
    },
    {
        "id": "exam3_g_h_u4_q15",
        "category": "Unit 04: Infections",
        "subcategory": "Free-Living Amoebae",
        "question_type": "clinical_vignette",
        "stem": "A 12-year-old boy presents with hyperacute fever, bifrontal headache, vomiting, and photophobia four days after diving into a warm freshwater lake in Texas during mid-July. Lumbar puncture demonstrates a marked neutrophilic pleocytosis, severe hypoglycorrhachia, and motile amoebic trophozoites on a fresh wet mount. By which anatomical route did this free-living amoeba gain access to the subarachnoid space?",
        "options": [
            {"label": "A", "text": "Cribriform plate perforations alongside the olfactory nerve fila", "is_correct": True},
            {"label": "B", "text": "Hematogenous seeding across the blood-cerebrospinal fluid barrier", "is_correct": False},
            {"label": "C", "text": "Retrograde ascension through the internal auditory canal along CN VIII", "is_correct": False},
            {"label": "D", "text": "Direct erosion through the tympanic membrane and mastoid air cells", "is_correct": False},
            {"label": "E", "text": "Invasion of the ophthalmic venous plexus via the superior orbital fissure", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "Primary Amoebic Meningoencephalitis (PAM) is caused by Naegleria fowleri, a thermophilic free-living amoeba found in warm freshwater lakes. Trophozoites enter through nasal mucosa, penetrate the olfactory neuroepithelium, and traverse the cribriform plate via the olfactory nerve (CN I) channels to enter the anterior cranial fossa, causing rapidly fatal necrotizing meningoencephalitis.",
        "high_yield_takeaway": "Naegleria fowleri penetrates the nasal olfactory mucosa and traverses the cribriform plate to cause fatal primary amoebic meningoencephalitis."
    },
    {
        "id": "exam3_g_h_u4_q16",
        "category": "Unit 04: Infections",
        "subcategory": "Immune Reconstitution",
        "question_type": "clinical_vignette",
        "stem": "A 35-year-old HIV-infected man with a baseline CD4 count of 18/uL completes two weeks of induction therapy for cryptococcal meningitis, achieving sterile CSF cultures. Combination antiretroviral therapy (ART) is initiated. Three weeks later, his CD4 count rebounds to 190/uL, but he develops high fever, worsening headache, and intense new leptomeningeal enhancement on MRI, while repeat CSF cultures remain sterile. What is the immunological mechanism of this clinical deterioration?",
        "options": [
            {"label": "A", "text": "Hyperinflammatory immune reaction against residual dead fungal antigens", "is_correct": True},
            {"label": "B", "text": "Rapid emergence of flucytosine-resistant cryptococcal mutant strains", "is_correct": False},
            {"label": "C", "text": "Direct neurotoxicity and chemical arachnoiditis induced by non-nucleosides", "is_correct": False},
            {"label": "D", "text": "Development of acute cytomegalovirus ependymitis following viral reactivation", "is_correct": False},
            {"label": "E", "text": "Secondary primary central nervous system lymphoma transformation", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "This patient has Immune Reconstitution Inflammatory Syndrome (IRIS). After starting ART in patients with profound immunodeficiency, rapid restoration of CD4+ T-cell counts and functional pathogen-specific cellular immunity triggers a paradoxical, hyperinflammatory cytokine storm against persistent non-viable antigen remnants of prior opportunistic infections (e.g., Cryptococcus, Mycobacteria). Treatment involves corticosteroids while continuing antimicrobial and antiretroviral therapy.",
        "high_yield_takeaway": "IRIS occurs after ART initiation as recovering CD4+ T cells trigger a paradoxical hyperinflammatory reaction against residual dead microbial antigens."
    },
    {
        "id": "exam3_g_h_u4_q17",
        "category": "Unit 04: Infections",
        "subcategory": "Brain Abscess Pathogenesis",
        "question_type": "clinical_vignette",
        "stem": "A 44-year-old man with uncorrected tetralogy of Fallot presents with high fever, dull headache, and new-onset focal motor seizures. Brain MRI demonstrates a single well-circumscribed ring-enhancing lesion in the left frontal lobe with marked surrounding vasogenic edema. Stereotactic aspiration yields purulent fluid growing Streptococcus viridans and peptostreptococci. Why did his congenital cardiac defect predispose him to this localized intracranial pyogenic infection?",
        "options": [
            {"label": "A", "text": "Right-to-left cardiac shunt bypassing pulmonary alveolar capillary filtration", "is_correct": True},
            {"label": "B", "text": "Chronic systemic venous hypertension causing retrograde venous microinfarcts", "is_correct": False},
            {"label": "C", "text": "Decreased renal clearance of circulating bacterial cell-wall peptidoglycans", "is_correct": False},
            {"label": "D", "text": "Chronic hypoxemia selectively impairing polymorphonuclear phagocytosis", "is_correct": False},
            {"label": "E", "text": "Direct communication between cardiac chambers and the azygos venous drainage", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "Normally, bacteria that enter the venous circulation (e.g., from dental procedures or oral mucosa) are filtered and phagocytosed by pulmonary alveolar macrophages and capillaries. In patients with cyanotic congenital heart disease and right-to-left shunts (such as tetralogy of Fallot or Eisenmenger syndrome), venous blood bypasses the pulmonary filter, allowing transient bacteremia to seed the cerebral circulation, predisposing to brain abscesses.",
        "high_yield_takeaway": "Right-to-left cardiac shunts bypass pulmonary capillary filtration, allowing transient bacteremia to seed the brain and form abscesses."
    },
    {
        "id": "exam3_g_h_u4_q18",
        "category": "Unit 04: Infections",
        "subcategory": "Neurosyphilis",
        "question_type": "clinical_vignette",
        "stem": "A 52-year-old man with untreated syphilis presents with shooting lancinating pains in his lower limbs, sensory ataxia, and a positive Romberg test. On pupillary examination, both pupils are small and irregular; they fail to constrict when exposed to bright flashlight beams but constrict promptly when focusing on a near object (Argyll Robertson pupils). Where is the neuropathological lesion localized that causes this light-near pupillary dissociation?",
        "options": [
            {"label": "A", "text": "Pretectal nuclei of the dorsal midbrain interrupting the afferent light reflex", "is_correct": True},
            {"label": "B", "text": "Edinger-Westphal nuclei within the ventral tegmentum of the upper midbrain", "is_correct": False},
            {"label": "C", "text": "Ciliary ganglion within the posterior intraorbital fat adjacent to the optic nerve", "is_correct": False},
            {"label": "D", "text": "Parasympathetic fibers traversing the superficial perimeter of cranial nerve III", "is_correct": False},
            {"label": "E", "text": "Bilateral superior cervical sympathetic ganglia within the deep carotid sheath", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "Argyll Robertson pupils ('prostitute's pupils' — accommodate but do not react) are a classic hallmark of tabes dorsalis (tertiary neurosyphilis). The lesion localizes to the pretectal area of the dorsal midbrain, which relays light-reflex afferent signals from the optic tract to the bilateral Edinger-Westphal nuclei. Accommodation fibers enter more ventrally and are spared, preserving pupillary constriction to near targets.",
        "high_yield_takeaway": "Argyll Robertson pupils in tabes dorsalis result from damage to the midbrain pretectal area, sparing ventral accommodation pathways (light-near dissociation)."
    },
    {
        "id": "exam3_g_h_u4_q19",
        "category": "Unit 04: Infections",
        "subcategory": "Neuropathic Pain",
        "question_type": "clinical_vignette",
        "stem": "A 71-year-old man had a blistering dermatomal rash across his right T5 dermatome six months ago that resolved completely. However, he continues to suffer from excruciating burning, electric sensations in that area, where even the light touch of a shirt produces intense pain (mechanical allodynia). What underlying neurobiological alteration in sensory pathways sustains this chronic postherpetic neuralgia?",
        "options": [
            {"label": "A", "text": "Central dorsal horn hyperexcitability and loss of GABAergic inhibitory interneurons", "is_correct": True},
            {"label": "B", "text": "Persistent lytic replication of active varicella virions inside Schwann cells", "is_correct": False},
            {"label": "C", "text": "Progressive demyelination of ascending spinothalamic tracts in cervical cord", "is_correct": False},
            {"label": "D", "text": "Autoimmune antibody blockade of postsynaptic alpha-motor endplate receptors", "is_correct": False},
            {"label": "E", "text": "Hypertrophy of cutaneous Pacinian corpuscles within the superficial dermis", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "Postherpetic neuralgia (PHN) is neuropathic pain persisting >3 months after herpes zoster resolution. VZV ganglionic necrosis causes both peripheral nerve damage and spinal dorsal horn reorganization: damaged sensory fibers exhibit spontaneous ectopic discharges, and death of GABAergic inhibitory interneurons in the substantia gelatinosa produces central sensitization and allodynia.",
        "high_yield_takeaway": "Postherpetic neuralgia is maintained by central sensitization and loss of inhibitory dorsal horn interneurons following VZV-induced ganglionitis."
    },
    {
        "id": "exam3_g_h_u4_q20",
        "category": "Unit 04: Infections",
        "subcategory": "Neonatal Antimicrobial Safety",
        "question_type": "clinical_vignette",
        "stem": "A 5-day-old neonate born at 39 weeks develops fever, lethargy, poor feeding, and a bulging fontanelle. Cerebrospinal fluid analysis confirms acute bacterial meningitis. The physician orders ampicillin and cefotaxime rather than ceftriaxone. What dangerous neonatal pharmacological adverse effect specifically mandates the avoidance of ceftriaxone in this age group?",
        "options": [
            {"label": "A", "text": "Displacement of bilirubin from albumin leading to kernicterus brainstem injury", "is_correct": True},
            {"label": "B", "text": "Premature closure of the ductus arteriosus causing acute pulmonary hypertension", "is_correct": False},
            {"label": "C", "text": "Irreversible inhibition of renal tubular growth leading to nephrocalcinosis", "is_correct": False},
            {"label": "D", "text": "Severe chondrotoxicity producing permanent epiphyseal growth plate arrest", "is_correct": False},
            {"label": "E", "text": "Complete bone marrow aplasia via mitochondrial ribosome subunit blockade", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "Ceftriaxone is contraindicated in neonates (<28 days old) because it strongly binds to albumin and displaces unconjugated bilirubin, markedly increasing free bilirubin levels and the risk of bilirubin encephalopathy (kernicterus). Additionally, ceftriaxone precipitates with intravenous calcium-containing solutions (e.g., parenteral nutrition) in neonatal lungs and kidneys. Cefotaxime has low protein binding and does not cause biliary sludging or kernicterus.",
        "high_yield_takeaway": "Ceftriaxone is contraindicated in neonates because it displaces bilirubin from albumin, causing kernicterus, and can precipitate with calcium."
    }
]

if __name__ == "__main__":
    for q in u4_questions:
        check_q(q)
    print("gen_g_h_u4.py: All 20 questions passed validation!")
