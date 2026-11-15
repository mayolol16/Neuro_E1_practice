# Part 2: Questions 49 to 93 (Opportunistic Infections: 15 Qs, Blood Supply: 15 Qs, Cerebrovascular: 15 Qs)

def get_part2_questions():
    qs = []

    # =========================================================================
    # UNIT 4: OPPORTUNISTIC INFECTIONS (15 Questions: Q49 - Q63, 10%)
    # =========================================================================

    # Q49
    qs.append({
        "id": "exam3_in_house_like_g_q49",
        "q_num": "49",
        "stem": "A 44-year-old man presents with acute fever, confusion, and unusual behavior. Family members report he complained of smelling burnt rubber prior to experiencing a focal motor seizure. Lumbar puncture demonstrates a lymphocytic pleocytosis with elevated red blood cells and normal glucose. MRI demonstrates asymmetric hyperintensity with petechial hemorrhages in the left inferior temporal and orbitofrontal cortex. Which of the following is the most appropriate initial therapy for this patient?",
        "category": "Opportunistic Infection",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Intravenous liposomal amphotericin B therapy"},
            {"letter": "B", "is_correct": True, "text": "Intravenous high-dose acyclovir antiviral therapy"},
            {"letter": "C", "is_correct": False, "text": "Intravenous broad-spectrum vancomycin therapy"},
            {"letter": "D", "is_correct": False, "text": "Intravenous broad-spectrum ganciclovir therapy"},
            {"letter": "E", "is_correct": False, "text": "Intravenous pyrimethamine-sulfadiazine therapy"}
        ],
        "correct_idx": 1,
        "explanation": "This patient presents with classic herpes simplex virus type 1 (HSV-1) encephalitis, characterized by acute fever, temporal lobe seizures with olfactory auras (uncinate fits due to uncus involvement), behavioral changes, and hemorrhagic temporal necrosis. CSF typically shows lymphocytic pleocytosis with elevated erythrocytes due to hemorrhagic necrosis. Immediate empiric intravenous acyclovir is critical to prevent permanent neurological morbidity and mortality.",
        "high_yield_pearl": "High-Yield Clinical Pearl: HSV-1 encephalitis targets the temporal and orbitofrontal lobes, causing hemorrhagic necrosis, olfactory auras, and bizarre behavior. Treat immediately with IV acyclovir.",
        "image": None
    })

    # Q50
    qs.append({
        "id": "exam3_in_house_like_g_q50",
        "q_num": "50",
        "stem": "A 52-year-old man recovering from herpes simplex virus encephalitis exhibits focal neurocognitive deficits. Visual field examination reveals a right superior homonymous quadrantanopia (\"pie in the sky\" defect). Neuropathologic necrosis in which of the following temporal lobe structures accounts for this specific visual field deficit?",
        "category": "Opportunistic Infection",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Cuneus cortex inferior to the calcarine fissure"},
            {"letter": "B", "is_correct": True, "text": "Meyer loop traveling through anterior temporal lobe"},
            {"letter": "C", "is_correct": False, "text": "Dorsal optic radiation passing through parietal lobe"},
            {"letter": "D", "is_correct": False, "text": "Lingual gyrus superior to the calcarine fissure"},
            {"letter": "E", "is_correct": False, "text": "Lateral geniculate nucleus of the posterolateral thalamus"}
        ],
        "correct_idx": 1,
        "explanation": "Meyer loop consists of lower retinal fibers carrying information from the superior contralateral visual field. These fibers sweep anteriorly and ventrally through the temporal lobe around the inferior horn of the lateral ventricle before traveling to the lingual gyrus. Damage to the left temporal lobe (as in HSV-1 encephalitis or anterior temporal lobectomy) damages Meyer loop, resulting in a contralateral right superior homonymous quadrantanopia.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Meyer loop sweeps through the temporal lobe carrying superior visual field information to the lingual gyrus; temporal damage causes a contralateral superior quadrantanopia.",
        "image": None
    })

    # Q51
    qs.append({
        "id": "exam3_in_house_like_g_q51",
        "q_num": "51",
        "stem": "A 38-year-old man with advanced HIV infection (CD4+ T-cell count of 65/uL) presents with fever, headache, and right hemiparesis. Brain MRI reveals multiple ring-enhancing lesions in the basal ganglia and corticomedullary junction with surrounding vasogenic edema. Biopsy shows intracellular encysted bradyzoites and free tachyzoites. Which of the following is the first-line pharmacotherapeutic regimen for this condition?",
        "category": "Opportunistic Infection",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Liposomal amphotericin B plus intravenous flucytosine"},
            {"letter": "B", "is_correct": True, "text": "Pyrimethamine plus sulfadiazine plus folinic acid"},
            {"letter": "C", "is_correct": False, "text": "High-dose intravenous ganciclovir plus foscarnet"},
            {"letter": "D", "is_correct": False, "text": "High-dose intravenous acyclovir plus valacyclovir"},
            {"letter": "E", "is_correct": False, "text": "Trimethoprim-sulfamethoxazole monotherapy alone"}
        ],
        "correct_idx": 1,
        "explanation": "Toxoplasma gondii is an intracellular protozoan that causes central nervous system opportunistic infection in immunocompromised patients (typically CD4 < 100/uL). It presents with focal neurological deficits, headache, and multiple ring-enhancing lesions preferentially involving the basal ganglia. First-line acute treatment is pyrimethamine, sulfadiazine, and leucovorin (folinic acid, added to prevent bone marrow suppression).",
        "high_yield_pearl": "High-Yield Clinical Pearl: Toxoplasmosis in HIV presents with multiple ring-enhancing basal ganglia lesions; treat acutely with pyrimethamine, sulfadiazine, and leucovorin.",
        "image": None
    })

    # Q52
    qs.append({
        "id": "exam3_in_house_like_g_q52",
        "q_num": "52",
        "stem": "A 41-year-old man with AIDS (CD4+ count of 35/uL) presents with lethargy, headache, and progressive confusion. Brain MRI demonstrates a single 3.5-cm periventricular mass lesion with prominent ring enhancement and surrounding edema. Toxoplasma serology is negative, and empiric anti-toxoplasma therapy fails to produce improvement. Cerebrospinal fluid PCR is positive for Epstein-Barr virus DNA. Which of the following neoplasms is most likely present?",
        "category": "Opportunistic Infection",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Metastatic systemic clear cell renal carcinoma"},
            {"letter": "B", "is_correct": True, "text": "Primary central nervous system large B-cell lymphoma"},
            {"letter": "C", "is_correct": False, "text": "High-grade invasive oligodendroglioma neoplasm"},
            {"letter": "D", "is_correct": False, "text": "Glioblastoma multiforme World Health Grade IV"},
            {"letter": "E", "is_correct": False, "text": "Multifocal intracranial capillary hemangioblastoma"}
        ],
        "correct_idx": 1,
        "explanation": "Primary central nervous system lymphoma (PCNSL) is a high-grade diffuse large B-cell neoplasm strongly associated with Epstein-Barr virus (EBV) in immunocompromised patients with AIDS (CD4 < 50/uL). Neuroimaging typically demonstrates a solitary, large periventricular ring- or solid-enhancing lesion with mass effect. The detection of EBV DNA in CSF via PCR has high diagnostic sensitivity and specificity, distinguishing PCNSL from toxoplasmosis.",
        "high_yield_pearl": "High-Yield Clinical Pearl: In AIDS patients, a solitary periventricular ring-enhancing lesion with positive CSF EBV PCR is classic for primary CNS lymphoma (diffuse large B-cell).",
        "image": None
    })

    # Q53
    qs.append({
        "id": "exam3_in_house_like_g_q53",
        "q_num": "53",
        "stem": "A 36-year-old man with untreated HIV infection (CD4+ count 48/uL) presents with a 2-week history of worsening indolent headache, low-grade fever, and malaise. Physical examination shows mild photophobia but no significant nuchal rigidity. Lumbar puncture reveals an elevated opening pressure of 320 mm H2O. India ink preparation demonstrates round budding yeast cells surrounded by wide, clear unstained gelatinous halos. Which of the following is the most appropriate initial induction therapy?",
        "category": "Opportunistic Infection",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Intravenous high-dose acyclovir and dexamethasone"},
            {"letter": "B", "is_correct": True, "text": "Liposomal amphotericin B plus intravenous flucytosine"},
            {"letter": "C", "is_correct": False, "text": "Oral fluconazole monotherapy at maximal maintenance dose"},
            {"letter": "D", "is_correct": False, "text": "Intravenous caspofungin plus oral voriconazole therapy"},
            {"letter": "E", "is_correct": False, "text": "Intravenous ceftriaxone plus intravenous vancomycin"}
        ],
        "correct_idx": 1,
        "explanation": "Cryptococcus neoformans is an opportunistic fungus with a thick polysaccharide capsule that causes subacute meningitis in immunocompromised hosts. The capsule creates a clear halo on India ink staining and stains bright red with mucicarmine. Patients characteristically present with markedly elevated intracranial opening pressure. First-line induction therapy consists of liposomal amphotericin B plus flucytosine for at least 2 weeks, followed by consolidation with oral fluconazole.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Cryptococcal meningitis presents with indolent headache and elevated opening pressure; diagnose via cryptococcal antigen or India ink; treat with amphotericin B and flucytosine.",
        "image": None
    })

    # Q54
    qs.append({
        "id": "exam3_in_house_like_g_q54",
        "q_num": "54",
        "stem": "A 49-year-old woman with relapsing-remitting multiple sclerosis who has been receiving natalizumab therapy for 3 years develops subacute cognitive decline, right-sided hemiparesis, and aphasia. Brain MRI demonstrates multiple asymmetric, non-enhancing T2/FLAIR hyperintensities in the subcortical white matter without mass effect or surrounding vasogenic edema. PCR testing of cerebrospinal fluid confirms the presence of JC virus DNA. Which of the following cells is the primary target of viral infection in this disorder?",
        "category": "Opportunistic Infection",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Perivascular microglia in cerebral deep gray matter"},
            {"letter": "B", "is_correct": True, "text": "Myelin-producing oligodendrocytes in white matter tracts"},
            {"letter": "C", "is_correct": False, "text": "Protoplasmic astrocytes forming the blood-brain barrier"},
            {"letter": "D", "is_correct": False, "text": "Ciliated ependymal cells lining the cerebral ventricles"},
            {"letter": "E", "is_correct": False, "text": "Pyramidal neurons in the deeper layers of motor cortex"}
        ],
        "correct_idx": 1,
        "explanation": "Progressive multifocal leukoencephalopathy (PML) is caused by reactivation of the JC polyomavirus in immunocompromised individuals or patients receiving monoclonal antibodies that inhibit leukocyte trafficking (such as natalizumab). JC virus selectively infects and destroys oligodendrocytes in the central nervous system, leading to patchy multifocal white matter demyelination that typically does NOT cause mass effect or prominent contrast enhancement.",
        "high_yield_pearl": "High-Yield Clinical Pearl: PML is caused by JC virus lytic destruction of oligodendrocytes in immunosuppressed patients (or natalizumab therapy), resulting in non-enhancing white matter plaques without mass effect.",
        "image": None
    })

    # Q55
    qs.append({
        "id": "exam3_in_house_like_g_q55",
        "q_num": "55",
        "stem": "A 33-year-old man with end-stage AIDS (CD4+ count of 18/uL) presents with confusion, delirium, and bilateral lower extremity paraparesis. Brain MRI demonstrates diffuse subependymal enhancement along the margins of the lateral ventricles. Microscopic examination of brain tissue demonstrates markedly enlarged cytomegalic cells containing dense, basophilic intranuclear inclusion bodies surrounded by a distinct clear halo (\"owl-eye\" inclusions). Which of the following is the most appropriate acute pharmacotherapy?",
        "category": "Opportunistic Infection",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Intravenous liposomal amphotericin B therapy"},
            {"letter": "B", "is_correct": True, "text": "Intravenous ganciclovir plus intravenous foscarnet"},
            {"letter": "C", "is_correct": False, "text": "Intravenous acyclovir plus oral valacyclovir therapy"},
            {"letter": "D", "is_correct": False, "text": "Intravenous pyrimethamine plus oral sulfadiazine"},
            {"letter": "E", "is_correct": False, "text": "Oral fluconazole plus intravenous voriconazole"}
        ],
        "correct_idx": 1,
        "explanation": "Cytomegalovirus (CMV) causes severe necrotizing ventriculitis and encephalitis in patients with profound immunosuppression (CD4 < 50/uL). Contrast-enhanced MRI characteristically demonstrates thin, linear periventricular subependymal enhancement. Histology demonstrates classic cytomegaly with prominent basophilic intranuclear \"owl-eye\" inclusions. First-line therapy for CMV encephalitis/ventriculitis is intravenous ganciclovir combined with foscarnet.",
        "high_yield_pearl": "High-Yield Clinical Pearl: CMV ventriculitis in AIDS (CD4 < 50) causes subependymal ventricular enhancement and \"owl-eye\" intranuclear inclusions; treat with IV ganciclovir/foscarnet.",
        "image": None
    })

    # Q56
    qs.append({
        "id": "exam3_in_house_like_g_q56",
        "q_num": "56",
        "stem": "A 58-year-old man presents with progressive difficulty walking, sharp \"lightning-like\" shooting pains in his legs, and urinary incontinence. Neurologic examination shows loss of vibration sense and proprioception in both lower extremities, absent knee and ankle deep tendon reflexes, and marked sensory ataxia with a positive Romberg sign. Bilateral pupils constrict briskly when viewing a near target but fail to constrict in response to bright light. Which of the following tests is most definitive for confirming this diagnosis?",
        "category": "Opportunistic Infection",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Serum detection of 14-3-3 protein by Western blotting"},
            {"letter": "B", "is_correct": True, "text": "Cerebrospinal fluid Venereal Disease Research Laboratory test"},
            {"letter": "C", "is_correct": False, "text": "Serum acetylcholine receptor binding autoantibody assay"},
            {"letter": "D", "is_correct": False, "text": "Cerebrospinal fluid oligoclonal band protein electrophoresis"},
            {"letter": "E", "is_correct": False, "text": "Serum anti-aquaporin-4 IgG autoantibody titer evaluation"}
        ],
        "correct_idx": 1,
        "explanation": "This patient presents with tabes dorsalis, a late neurosyphilitic complication caused by Treponema pallidum spirochetal destruction of the dorsal columns and dorsal roots of the spinal cord. Hallmark features include impaired proprioception/vibration, sensory ataxia (positive Romberg), lancinating lower extremity pains, areflexia, and Argyll Robertson pupils (light-near dissociation: constrict to accommodation but not light). Positive CSF VDRL confirms active neurosyphilis, treated with IV penicillin G.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Tabes dorsalis involves dorsal column/root degeneration, sensory ataxia, lancinating pains, and Argyll Robertson pupils; confirm with positive CSF VDRL and treat with IV penicillin G.",
        "image": None
    })

    # Q57
    qs.append({
        "id": "exam3_in_house_like_g_q57",
        "q_num": "57",
        "stem": "A 34-year-old man presents with a severe unremitting left-sided headache, low-grade fever, and lethargy following a 3-week bout of untreated maxillary sinusitis. Contrast-enhanced brain CT demonstrates a single 3-cm ring-enhancing lesion in the left frontal lobe with central non-enhancement, a well-defined hyperdense rim, and prominent surrounding hypodensity. Which of the following pathologic processes forms the central core of this lesion?",
        "category": "Opportunistic Infection",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Caseous granulomatous necrosis with Langhans giant cells"},
            {"letter": "B", "is_correct": True, "text": "Liquefactive necrosis with abundant apoptotic neutrophils"},
            {"letter": "C", "is_correct": False, "text": "Coagulative ischemic necrosis with preserved tissue ghosts"},
            {"letter": "D", "is_correct": False, "text": "Fibrinoid necrotic degeneration of small penetrating arteries"},
            {"letter": "E", "is_correct": False, "text": "Enzymatic fat necrosis with saponification calcium deposits"}
        ],
        "correct_idx": 1,
        "explanation": "Brain abscesses typically arise via contiguous spread (from sinusitis, otitis media, or mastoiditis) or hematogenous dissemination. Histopathologically, a mature brain abscess consists of a central zone of liquefactive necrosis containing dead neutrophils and cellular debris (pus), surrounded by a vascularized collagenous capsule synthesized by fibroblasts, and an outer zone of intense reactive astrogliosis and vasogenic edema. Contrast enhancement corresponds to the vascular fibrous capsule.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Brain abscesses feature central liquefactive necrosis surrounded by a vascularized fibrous capsule that enhances on contrast imaging; contiguous sinusitis is a common etiology.",
        "image": None
    })

    # Q58
    qs.append({
        "id": "exam3_in_house_like_g_q58",
        "q_num": "58",
        "stem": "A 74-year-old woman with chronic lymphocytic leukemia presents with fever, confusion, and cranial nerve palsies. CSF examination reveals a neutrophilic pleocytosis with elevated protein and low glucose. Gram stain demonstrates short Gram-positive rods with narrow zones of beta-hemolysis on sheep blood agar. Culture of the organism at room temperature reveals distinctive end-over-end tumbling motility. Which of the following antimicrobial agents must be included in the empiric treatment of this patient?",
        "category": "Opportunistic Infection",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Intravenous liposomal amphotericin B therapy"},
            {"letter": "B", "is_correct": True, "text": "Intravenous ampicillin antimicrobial therapy"},
            {"letter": "C", "is_correct": False, "text": "Intravenous ceftriaxone antimicrobial therapy"},
            {"letter": "D", "is_correct": False, "text": "Intravenous high-dose acyclovir antiviral therapy"},
            {"letter": "E", "is_correct": False, "text": "Intravenous metronidazole antimicrobial therapy"}
        ],
        "correct_idx": 1,
        "explanation": "Listeria monocytogenes is a facultative intracellular Gram-positive bacillus that causes meningitis and rhombencephalitis in neonates, elderly patients (>50 years), and immunocompromised individuals. It exhibits characteristic tumbling motility at room temperature (25°C) and can grow at cold temperatures (4°C). Because Listeria is inherently resistant to cephalosporins (including ceftriaxone), ampicillin must be added to the empiric meningitis regimen in patients >50 years or immunocompromised.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Listeria monocytogenes is a tumbling Gram-positive rod causing meningitis in neonates and elderly/immunocompromised patients; cephalosporins are ineffective, so ampicillin is required.",
        "image": None
    })

    # Q59
    qs.append({
        "id": "exam3_in_house_like_g_q59",
        "q_num": "59",
        "stem": "A 24-year-old wildlife researcher is admitted with severe agitation, agitation upon hearing running water, and uncontrollable pharyngeal spasms whenever liquids are offered. Family reports he sustained a minor animal bite to his right forearm while exploring a bat cave 2 months ago. He rapidly deteriorates into coma and dies. Postmortem histopathologic examination of the cerebellum and hippocampus is most likely to demonstrate which of the following findings?",
        "category": "Opportunistic Infection",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Intranuclear basophilic viral inclusions surrounded by halo"},
            {"letter": "B", "is_correct": True, "text": "Eosinophilic cytoplasmic inclusions within Purkinje cells"},
            {"letter": "C", "is_correct": False, "text": "Extracellular silver-staining amyloid-beta senile plaques"},
            {"letter": "D", "is_correct": False, "text": "Intracytoplasmic inclusions composed of alpha-synuclein"},
            {"letter": "E", "is_correct": False, "text": "Spongiform vacuolation within cortical gray matter neuropil"}
        ],
        "correct_idx": 1,
        "explanation": "Rabies virus (a bullet-shaped Rhabdovirus) is transmitted through the saliva of infected mammals (bats, raccoons, skunks). It binds to nicotinic acetylcholine receptors and travels retrograde via peripheral nerves to the central nervous system. Clinical rabies presents with painful pharyngeal spasms provoked by the sight or sound of water (hydrophobia), autonomic instability, and fatal encephalitis. Pathognomonic Negri bodies are round, eosinophilic intracytoplasmic inclusions found in Purkinje cells of the cerebellum and pyramidal neurons of the hippocampus.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Rabies presents with hydrophobia and agitation following bat/animal exposure; postmortem pathology reveals pathognomonic eosinophilic cytoplasmic Negri bodies in Purkinje cells and hippocampal neurons.",
        "image": None
    })

    # Q60
    qs.append({
        "id": "exam3_in_house_like_g_q60",
        "q_num": "60",
        "stem": "A 68-year-old man from Colorado presents in August with high fever, headache, tremors, and sudden acute asymmetric flaccid weakness in his left leg. Examination reveals 0/5 strength in the left lower extremity with complete loss of the left patellar and Achilles reflexes, but sensation is entirely intact throughout. Lumbar puncture demonstrates a lymphocytic pleocytosis. Which of the following vectors is primarily responsible for transmitting the causative agent of this patient's illness?",
        "category": "Opportunistic Infection",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Ixodes scapularis tick bite vector"},
            {"letter": "B", "is_correct": True, "text": "Culex mosquito bite insect vector"},
            {"letter": "C", "is_correct": False, "text": "Phlebotomine sandfly bite insect vector"},
            {"letter": "D", "is_correct": False, "text": "Glossina tsetse fly bite insect vector"},
            {"letter": "E", "is_correct": False, "text": "Triatomine kissing bug insect vector"}
        ],
        "correct_idx": 1,
        "explanation": "West Nile virus is an arbovirus (Flaviviridae) transmitted by Culex mosquitoes, with birds serving as the natural reservoir. Infection classically peaks in late summer. While most infections are asymptomatic, neuroinvasive disease causes meningitis, encephalitis, and a poliomyelitis-like acute flaccid paralysis caused by destruction of anterior horn cells in the spinal cord. Presentation features asymmetric weakness, hyporeflexia, and preserved sensation.",
        "high_yield_pearl": "High-Yield Clinical Pearl: West Nile virus is transmitted by Culex mosquitoes and can cause neuroinvasive polio-like acute flaccid paralysis due to anterior horn cell destruction with preserved sensation.",
        "image": None
    })

    # Q61
    qs.append({
        "id": "exam3_in_house_like_g_q61",
        "q_num": "61",
        "stem": "A previously healthy 13-year-old boy presents with severe bifrontal headache, high fever, vomiting, and confusion 4 days after swimming and diving in a warm freshwater lake. Physical examination reveals severe meningismus and complete anosmia. Lumbar puncture yields cloudy cerebrospinal fluid with marked neutrophilic pleocytosis, elevated protein, and low glucose. Wet-mount examination of CSF reveals motile ameboid trophozoites. Through which of the following anatomical structures did this pathogen gain access to the central nervous system?",
        "category": "Opportunistic Infection",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Superior orbital fissure along the ophthalmic division"},
            {"letter": "B", "is_correct": True, "text": "Cribriform plate along the olfactory nerve unmyelinated axons"},
            {"letter": "C", "is_correct": False, "text": "Internal acoustic meatus along the vestibulocochlear nerve"},
            {"letter": "D", "is_correct": False, "text": "Jugular foramen along the glossopharyngeal nerve fibers"},
            {"letter": "E", "is_correct": False, "text": "Foramen spinosum along the middle meningeal artery branches"}
        ],
        "correct_idx": 1,
        "explanation": "Naegleria fowleri is a free-living amebic protozoan found in warm freshwater lakes. It causes primary amebic meningoencephalitis (PAM). The amebae enter through the nasal cavity during swimming or diving, penetrate the nasal mucosa, and travel across the cribriform plate along unmyelinated olfactory nerve fibers into the anterior cranial fossa. This causes fulminant, rapidly fatal purulent and hemorrhagic necrotizing meningoencephalitis.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Naegleria fowleri penetrates the cribriform plate via olfactory nerves after warm freshwater swimming, causing rapidly fatal primary amebic meningoencephalitis.",
        "image": None
    })

    # Q62
    qs.append({
        "id": "exam3_in_house_like_g_q62",
        "q_num": "62",
        "stem": "A 22-year-old college student presents with high fever, petechial skin rash, and neck stiffness. Lumbar puncture is performed, and cerebrospinal fluid analysis demonstrates an opening pressure of 280 mm H2O (normal 100-200), white blood cell count of 4,200/uL with 92% neutrophils, glucose of 18 mg/dL (concurrent blood glucose 110 mg/dL), and protein of 240 mg/dL (normal 15-45). Which of the following sets of CSF findings is most characteristic of viral aseptic meningitis?",
        "category": "Opportunistic Infection",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Marked neutrophilic pleocytosis with severe hypoglycorrhachia"},
            {"letter": "B", "is_correct": True, "text": "Lymphocytic pleocytosis with normal glucose and mild protein rise"},
            {"letter": "C", "is_correct": False, "text": "Marked eosinophilic pleocytosis with profound hyperproteinorrachia"},
            {"letter": "D", "is_correct": False, "text": "Lymphocytic pleocytosis with severe hypoglycorrhachia and high protein"},
            {"letter": "E", "is_correct": False, "text": "Normal leukocyte count with markedly elevated protein and glucose"}
        ],
        "correct_idx": 1,
        "explanation": "Bacterial meningitis (as shown in the stem's vignette) is characterized by markedly elevated opening pressure, prominent neutrophilic pleocytosis (>1000/uL), low glucose (<40 mg/dL or CSF:serum ratio <0.4), and markedly elevated protein. In contrast, viral (aseptic) meningitis characteristically displays normal to slightly elevated opening pressure, lymphocytic predominance (typically <500/uL), completely normal glucose, and normal or only mildly elevated protein.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Viral meningitis presents with lymphocytic pleocytosis, normal glucose, and normal/mild protein elevation. Bacterial meningitis shows high neutrophils, low glucose, and high protein.",
        "image": None
    })

    # Q63
    qs.append({
        "id": "exam3_in_house_like_g_q63",
        "q_num": "63",
        "stem": "A 29-year-old immigrant from rural Guatemala presents with a new-onset generalized tonic-clonic seizure. Physical examination is unremarkable. Brain MRI reveals several small, cystic parenchymal lesions containing a visible eccentrically located mural nodule (invaginated scolex with hooklets) and mild surrounding edema. Which of the following was the specific route of transmission for this patient's underlying condition?",
        "category": "Opportunistic Infection",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Ingestion of undercooked pork containing larval cysticerci"},
            {"letter": "B", "is_correct": True, "text": "Ingestion of food contaminated with Taenia solium human feces eggs"},
            {"letter": "C", "is_correct": False, "text": "Direct skin penetration by cercariae during freshwater swimming"},
            {"letter": "D", "is_correct": False, "text": "Inhalation of fungal spores from pigeon droppings soil residue"},
            {"letter": "E", "is_correct": False, "text": "Ingestion of undercooked freshwater fish encysted larvae"}
        ],
        "correct_idx": 1,
        "explanation": "Neurocysticercosis is caused by the larval stage of Taenia solium (pork tapeworm). Humans contract neurocysticercosis by ingesting food or water contaminated with T. solium EGGS shed in human feces (fecal-oral route). Ingesting undercooked pork containing CYSTS causes intestinal tapeworm infection (taeniasis), NOT cysticercosis. Neuroimaging classically reveals cysts with a visible scolex (\"hole-with-dot\" sign). It is the leading cause of acquired epilepsy in developing countries.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Ingestion of T. solium eggs from human feces causes neurocysticercosis (cysts with scolex, adult-onset seizures). Ingestion of undercooked pork with cysts causes intestinal taeniasis.",
        "image": None
    })

    # =========================================================================
    # UNIT 6: STROKE - BLOOD SUPPLY OF THE CNS (15 Questions: Q64 - Q78, 10%)
    # =========================================================================

    # Q64
    qs.append({
        "id": "exam3_in_house_like_g_q64",
        "q_num": "64",
        "stem": "A 71-year-old man presents with sudden acute weakness and sensory loss in his right lower extremity. Neurological examination reveals 1/5 strength in the right leg, with hyperreflexia and an extensor plantar response. Strength in his right upper extremity and face is 5/5. He also displays urinary incontinence and pronounced abulia with lack of initiative. Occlusion of which of the following cerebral arterial vessels is responsible for this clinical presentation?",
        "category": "Stroke (Blood Supply, Cerebrovascular, Brainstem)",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Main trunk of the left middle cerebral artery"},
            {"letter": "B", "is_correct": True, "text": "Left anterior cerebral artery vascular branch"},
            {"letter": "C", "is_correct": False, "text": "Left posterior cerebral artery cortical branch"},
            {"letter": "D", "is_correct": False, "text": "Left anterior choroidal artery deep branches"},
            {"letter": "E", "is_correct": False, "text": "Left lenticulostriate penetrating branches"}
        ],
        "correct_idx": 1,
        "explanation": "The anterior cerebral artery (ACA) supplies the medial surface of the frontal and parietal lobes, including the paracentral lobule (which contains the motor and sensory representations for the contralateral lower extremity and foot). ACA infarction classically results in contralateral leg weakness and sensory loss that is significantly greater than arm or facial involvement, accompanied by urinary incontinence (damage to the frontal micturition center) and abulia/psychomotor slowing.",
        "high_yield_pearl": "High-Yield Clinical Pearl: ACA infarction produces contralateral lower extremity weakness and sensory loss (paracentral lobule), urinary incontinence (micturition center), and abulia.",
        "image": None
    })

    # Q65
    qs.append({
        "id": "exam3_in_house_like_g_q65",
        "q_num": "65",
        "stem": "A 64-year-old right-handed woman presents with sudden onset weakness of her right face and right upper extremity, while right leg strength is largely preserved. When asked about her symptoms, she speaks with great effort, using short, halting telegraphic sentences without grammatical connectors, but she correctly follows complex auditory commands. She cannot repeat the phrase \"no ifs, ands, or buts.\" Occlusion of which of the following arterial vessels best accounts for these findings?",
        "category": "Stroke (Blood Supply, Cerebrovascular, Brainstem)",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Inferior division of the left middle cerebral artery"},
            {"letter": "B", "is_correct": True, "text": "Superior division of the left middle cerebral artery"},
            {"letter": "C", "is_correct": False, "text": "Cortical branches of the left anterior cerebral artery"},
            {"letter": "D", "is_correct": False, "text": "Cortical branches of the left posterior cerebral artery"},
            {"letter": "E", "is_correct": False, "text": "Penetrating lenticulostriate branches of the left MCA"}
        ],
        "correct_idx": 1,
        "explanation": "The superior division of the middle cerebral artery (MCA) supplies the lateral frontal lobe, encompassing the primary motor cortex for the face and upper extremity (precentral gyrus) and Broca expressive language area in the inferior frontal gyrus of the dominant hemisphere. Occlusion results in contralateral faciobrachial hemiparesis and Broca aphasia (non-fluent, effortful speech, impaired repetition, with preserved auditory comprehension).",
        "high_yield_pearl": "High-Yield Clinical Pearl: MCA superior division strokes cause Broca aphasia (non-fluent, repetition impaired, comprehension intact) and contralateral face and arm weakness sparing the leg.",
        "image": None
    })

    # Q66
    qs.append({
        "id": "exam3_in_house_like_g_q66",
        "q_num": "66",
        "stem": "A 67-year-old right-handed man presents with acute difficulty communicating. On examination, his speech is fluent, effortless, and rapid, but it is entirely devoid of meaning, filled with paraphasic errors and neologisms (\"word salad\"). He is unable to follow verbal commands or repeat words spoken to him. Motor strength and tactile sensation are 5/5 bilaterally. Visual field testing reveals a right superior homonymous quadrantanopia. Occlusion of which of the following arterial divisions is the cause?",
        "category": "Stroke (Blood Supply, Cerebrovascular, Brainstem)",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Superior division of the left middle cerebral artery"},
            {"letter": "B", "is_correct": True, "text": "Inferior division of the left middle cerebral artery"},
            {"letter": "C", "is_correct": False, "text": "Main trunk of the left anterior cerebral artery"},
            {"letter": "D", "is_correct": False, "text": "Deep penetrating lenticulostriate arterial vessels"},
            {"letter": "E", "is_correct": False, "text": "Posterior inferior cerebellar artery vascular trunk"}
        ],
        "correct_idx": 1,
        "explanation": "The inferior division of the left (dominant) middle cerebral artery supplies the lateral superior temporal gyrus (Wernicke area) and the adjacent inferior parietal lobule. It also supplies Meyer loop traversing the temporal lobe. Occlusion causes Wernicke aphasia (fluent, paraphasic speech with severely impaired comprehension and repetition) and a contralateral superior homonymous quadrantanopia (\"pie in the sky\"), typically without motor hemiparesis.",
        "high_yield_pearl": "High-Yield Clinical Pearl: MCA inferior division strokes cause Wernicke aphasia (fluent, impaired comprehension, impaired repetition) and a contralateral upper quadrantanopia without motor weakness.",
        "image": None
    })

    # Q67
    qs.append({
        "id": "exam3_in_house_like_g_q67",
        "q_num": "67",
        "stem": "A 62-year-old man with poorly controlled hypertension experiences sudden dense weakness of his left face, left arm, and left leg. Physical examination confirms 1/5 strength equally across the left upper extremity, lower extremity, and lower face, with hyperreflexia and left Babinski sign. Speech, comprehension, tactile sensation, and visual fields are completely normal, with no evidence of neglect or aphasia. Occlusion of which of the following arterial vessels is the underlying cause?",
        "category": "Stroke (Blood Supply, Cerebrovascular, Brainstem)",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Cortical branches of the right anterior cerebral artery"},
            {"letter": "B", "is_correct": True, "text": "Lenticulostriate branches of the right middle cerebral artery"},
            {"letter": "C", "is_correct": False, "text": "Cortical branches of the right posterior cerebral artery"},
            {"letter": "D", "is_correct": False, "text": "Inferior division of the right middle cerebral artery"},
            {"letter": "E", "is_correct": False, "text": "Penetrating branches of the right anterior choroidal"}
        ],
        "correct_idx": 1,
        "explanation": "The lenticulostriate arteries are small, deep penetrating branches of the middle cerebral artery (M1 trunk) that supply the basal ganglia and the posterior limb of the internal capsule. A lacunar infarct in the posterior limb of the internal capsule produces pure motor hemiparesis, causing dense, proportional weakness of the contralateral face, arm, and leg without \"cortical\" signs (no aphasia, neglect, visual field cuts, or sensory loss).",
        "high_yield_pearl": "High-Yield Clinical Pearl: Lenticulostriate artery occlusion damages the posterior limb of the internal capsule, causing a pure motor lacunar stroke (proportional face, arm, leg weakness without cortical deficits).",
        "image": None
    })

    # Q68
    qs.append({
        "id": "exam3_in_house_like_g_q68",
        "q_num": "68",
        "stem": "A 59-year-old woman wakes up with visual difficulty. Formal perimetric visual field testing reveals a right homonymous hemianopia with complete macular sparing. Pupillary light reflexes are normal in both eyes. Occlusion of the left posterior cerebral artery is confirmed on neuroimaging. Which of the following vascular collateral supplies explains the preservation of central macular vision in this patient?",
        "category": "Stroke (Blood Supply, Cerebrovascular, Brainstem)",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Anterior cerebral artery collateral anastomotic supply"},
            {"letter": "B", "is_correct": True, "text": "Middle cerebral artery collateral branches to occipital pole"},
            {"letter": "C", "is_correct": False, "text": "Anterior choroidal artery branches to lateral geniculate"},
            {"letter": "D", "is_correct": False, "text": "Superior cerebellar artery collateral cortical supply"},
            {"letter": "E", "is_correct": False, "text": "Ophthalmic artery retrograde branches through orbits"}
        ],
        "correct_idx": 1,
        "explanation": "The primary visual cortex (calcarine cortex) in the occipital lobe is supplied by the posterior cerebral artery (PCA). Occlusion of the PCA results in a contralateral homonymous hemianopia. However, central macular vision is represented at the occipital pole, which has a dual blood supply receiving collateral anastomotic branches from terminal branches of the middle cerebral artery (MCA). This dual supply results in classic \"macular sparing.\"",
        "high_yield_pearl": "High-Yield Clinical Pearl: PCA occlusion causes contralateral homonymous hemianopia with macular sparing; the occipital pole (macular representation) is spared by collateral branches from the MCA.",
        "image": None
    })

    # Q69
    qs.append({
        "id": "exam3_in_house_like_g_q69",
        "q_num": "69",
        "stem": "A 55-year-old man presents with sudden left-sided weakness and sensory loss. Neurologic examination demonstrates a left spastic hemiplegia, left hemianesthesia to all modalities, and a left homonymous hemianopia. Language, speech comprehension, and spatial attention are intact. MRI confirms an acute infarct involving the posterior limb of the internal capsule, the optic tract, and the lateral geniculate body. Occlusion of which of the following arterial vessels produces this classic clinical triad?",
        "category": "Stroke (Blood Supply, Cerebrovascular, Brainstem)",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Posterior inferior cerebellar artery arterial trunk"},
            {"letter": "B", "is_correct": True, "text": "Anterior choroidal artery branch of internal carotid"},
            {"letter": "C", "is_correct": False, "text": "Superior division of the right middle cerebral artery"},
            {"letter": "D", "is_correct": False, "text": "Cortical branch of the right anterior cerebral artery"},
            {"letter": "E", "is_correct": False, "text": "Paramedian penetrating branch of the basilar artery"}
        ],
        "correct_idx": 1,
        "explanation": "The anterior choroidal artery arises directly from the internal carotid artery and supplies the posterior limb of the internal capsule, the optic tract, lateral geniculate nucleus, uncus, and hippocampus. Occlusion produces the classic anterior choroidal syndrome triad: contralateral hemiparesis (posterior limb internal capsule), contralateral hemisensory loss (thalamocortical radiations), and contralateral homonymous hemianopia (optic tract/lateral geniculate body).",
        "high_yield_pearl": "High-Yield Clinical Pearl: Anterior choroidal artery occlusion produces a triad of contralateral hemiplegia, hemisensory loss, and homonymous hemianopia (posterior limb of internal capsule and lateral geniculate nucleus).",
        "image": None
    })

    # Q70
    qs.append({
        "id": "exam3_in_house_like_g_q70",
        "q_num": "70",
        "stem": "A 69-year-old man presents with an acute episode of sudden, painless loss of vision in his right eye that lasted for 8 minutes before resolving completely. He describes the episode as a \"black shade or curtain pulling down over the eye.\" Funduscopic examination shows mild retinal arteriolar narrowing without hemorrhage. A right carotid bruit is audible on neck auscultation. Which of the following arterial vessels was transiently occluded during this ischemic episode?",
        "category": "Stroke (Blood Supply, Cerebrovascular, Brainstem)",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Posterior communicating artery branch of carotid"},
            {"letter": "B", "is_correct": True, "text": "Ophthalmic artery branch of internal carotid artery"},
            {"letter": "C", "is_correct": False, "text": "Anterior cerebral artery A1 precommunicating segment"},
            {"letter": "D", "is_correct": False, "text": "Middle cerebral artery M1 sphenoidal main segment"},
            {"letter": "E", "is_correct": False, "text": "Anterior choroidal artery branch of internal carotid"}
        ],
        "correct_idx": 1,
        "explanation": "This patient presents with amaurosis fugax (transient monocular vision loss), classic for transient ischemia in the distribution of the ophthalmic artery (the first intracranial branch of the internal carotid artery) or its branch, the central retinal artery. It is most commonly caused by microemboli originating from an atheromatous plaque at the ipsilateral internal carotid artery bifurcation (often manifesting as a carotid bruit).",
        "high_yield_pearl": "High-Yield Clinical Pearl: Amaurosis fugax is transient, painless monocular vision loss (\"curtain coming down\") caused by embolic occlusion of the ophthalmic artery, usually from ipsilateral carotid stenosis.",
        "image": None
    })

    # Q71
    qs.append({
        "id": "exam3_in_house_like_g_q71",
        "q_num": "71",
        "stem": "A 66-year-old man undergoes emergency coronary artery bypass grafting complicated by prolonged systemic hypotension with mean arterial pressures remaining below 45 mm Hg for 40 minutes. Following extubation, neurologic examination demonstrates severe bilateral weakness of the shoulder abductors and hip flexors, while distal hand grasp, fine finger movements, and foot movements are completely preserved (\"man-in-a-barrel\" syndrome). Which of the following vascular regions is most susceptible to this type of ischemic injury?",
        "category": "Stroke (Blood Supply, Cerebrovascular, Brainstem)",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Deep territories supplied by lenticulostriate vessels"},
            {"letter": "B", "is_correct": True, "text": "Watershed borderzones between major cerebral arteries"},
            {"letter": "C", "is_correct": False, "text": "Brainstem territories supplied by paramedian basilar"},
            {"letter": "D", "is_correct": False, "text": "Medial occipital territories supplied by the calcarine"},
            {"letter": "E", "is_correct": False, "text": "Cerebellar cortex supplied by posterior inferior vessels"}
        ],
        "correct_idx": 1,
        "explanation": "Watershed (borderzone) infarcts occur at the terminal junctional boundaries between major arterial territories (e.g., between ACA and MCA, or MCA and PCA). These distal vascular beds are exquisitely sensitive to profound systemic hypotension and hypoperfusion. Infarction of the ACA-MCA borderzone damages cortical motor representations for proximal limb girdles (shoulders and hips), resulting in the classic \"man-in-a-barrel\" presentation.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Severe systemic hypotension causes watershed (borderzone) infarcts between ACA-MCA, producing proximal limb girdle weakness with preserved distal strength (\"man-in-a-barrel\").",
        "image": None
    })

    # Q72
    qs.append({
        "id": "exam3_in_house_like_g_q72",
        "q_num": "72",
        "stem": "A 26-year-old woman presents with severe headache, fever, chemosis, marked periorbital edema, and proptosis of the right eye 5 days after squeezing a painful furuncle in the \"danger triangle\" of her midface. Neuro-ophthalmologic examination demonstrates right-sided ptosis, fixed dilated right pupil, complete ophthalmoplegia of the right eye, and numbness over the right forehead and cheek. Infection in which of the following venous structures accounts for these findings?",
        "category": "Stroke (Blood Supply, Cerebrovascular, Brainstem)",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Superior sagittal dural venous sinus channels"},
            {"letter": "B", "is_correct": True, "text": "Cavernous dural venous sinus vascular complex"},
            {"letter": "C", "is_correct": False, "text": "Transverse dural venous sinus lateral channels"},
            {"letter": "D", "is_correct": False, "text": "Sigmoid dural venous sinus jugular channels"},
            {"letter": "E", "is_correct": False, "text": "Straight dural venous sinus tentorial channels"}
        ],
        "correct_idx": 1,
        "explanation": "The cavernous sinus receives venous drainage from the face and orbits via the valveless ophthalmic and facial veins. Infections in the facial \"danger triangle\" can spread into the cavernous sinus, causing septic cavernous sinus thrombosis. Structures passing through the cavernous sinus include CN III, IV, VI, V1, V2, and the internal carotid artery with its sympathetic plexus. CN VI runs freely adjacent to the internal carotid inside the sinus lumen and is typically affected first.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Cavernous sinus thrombosis presents with chemosis, proptosis, and palsies of CN III, IV, V1, V2, and VI; CN VI runs directly in the sinus lumen next to the internal carotid.",
        "image": None
    })

    # Q73
    qs.append({
        "id": "exam3_in_house_like_g_q73",
        "q_num": "73",
        "stem": "A 58-year-old man undergoes surgical repair of a descending thoracic aortic aneurysm. Postoperatively, he exhibits complete flaccid paralysis of both lower extremities and complete loss of pain and temperature sensation below the level of T10. Vibration sense, joint position sense, and light touch perception in both lower extremities remain completely intact. Occlusion of which of the following spinal vessels is responsible for this selective pattern of spinal deficit?",
        "category": "Stroke (Blood Supply, Cerebrovascular, Brainstem)",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Paired posterior spinal arteries supplying cord"},
            {"letter": "B", "is_correct": True, "text": "Anterior spinal artery supplying anterior cord"},
            {"letter": "C", "is_correct": False, "text": "Posterolateral spinal arterial anastomotic plexus"},
            {"letter": "D", "is_correct": False, "text": "Posterior inferior cerebellar artery spinal branch"},
            {"letter": "E", "is_correct": False, "text": "Anterior inferior cerebellar artery spinal branch"}
        ],
        "correct_idx": 1,
        "explanation": "The anterior spinal artery supplies the anterior two-thirds of the spinal cord, which includes the anterior horn motor neurons, the lateral corticospinal tracts, and the spinothalamic tracts (pain and temperature). The paired posterior spinal arteries supply the posterior one-third (dorsal columns: vibration and proprioception). Anterior spinal artery occlusion (often during thoracic aortic surgery) causes anterior cord syndrome: bilateral paralysis and loss of pain/temp below the lesion, with dorsal column sparing.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Anterior spinal artery occlusion causes anterior cord syndrome (bilateral paraplegia, loss of pain/temp below level) with selective preservation of dorsal column proprioception/vibration.",
        "image": None
    })

    # Q74
    qs.append({
        "id": "exam3_in_house_like_g_q74",
        "q_num": "74",
        "stem": "During repair of an extensive thoracoabdominal aortic aneurysm, cross-clamping of the lower thoracic aorta places the spinal cord at risk for ischemic infarction. The surgeon must take special care to preserve the great anterior radiculomedullary artery (artery of Adamkiewicz), which provides the critical supplemental blood supply to the lower thoracic and lumbosacral cord. At which of the following vertebral levels does this artery most commonly originate?",
        "category": "Stroke (Blood Supply, Cerebrovascular, Brainstem)",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Upper cervical levels C1 through C4 on the right"},
            {"letter": "B", "is_correct": True, "text": "Lower thoracic levels T9 through T12 on the left"},
            {"letter": "C", "is_correct": False, "text": "Mid-cervical levels C5 through C8 on the left"},
            {"letter": "D", "is_correct": False, "text": "Upper thoracic levels T1 through T4 on the right"},
            {"letter": "E", "is_correct": False, "text": "Mid-lumbar levels L3 through L5 on the left"}
        ],
        "correct_idx": 1,
        "explanation": "The artery of Adamkiewicz (arteria radicularis magna) is the major anterior radicular artery supplying the lower two-thirds of the spinal cord (lumbosacral enlargement). It most commonly arises on the left side from an intercostal branch between the T9 and T12 vertebral levels. Iatrogenic occlusion or sacrifice during thoracoabdominal aortic repair can lead to catastrophic lower cord infarction and paraplegia.",
        "high_yield_pearl": "High-Yield Clinical Pearl: The artery of Adamkiewicz arises between T9 and T12 (usually left) and supplies the anterior spinal cord; injury during aortic surgery causes lower cord ischemia and paraplegia.",
        "image": None
    })

    # Q75
    qs.append({
        "id": "exam3_in_house_like_g_q75",
        "q_num": "75",
        "stem": "A 54-year-old woman presents with sudden onset of a severe right-sided retro-orbital headache and double vision. Neuro-ophthalmologic examination reveals ptosis of the right upper eyelid, a fixed dilated right pupil that does not react to light, and an abducted and depressed resting position of the right eye (\"down and out\"). Brain CT angiography confirms an unruptured saccular aneurysm compressing the oculomotor nerve. At which of the following arterial branch points is this aneurysm located?",
        "category": "Stroke (Blood Supply, Cerebrovascular, Brainstem)",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Anterior cerebral and anterior communicating junction"},
            {"letter": "B", "is_correct": True, "text": "Internal carotid and posterior communicating junction"},
            {"letter": "C", "is_correct": False, "text": "Basilar artery bifurcation and posterior cerebral"},
            {"letter": "D", "is_correct": False, "text": "Middle cerebral artery main bifurcation bifurcation"},
            {"letter": "E", "is_correct": False, "text": "Vertebral artery and posterior inferior cerebellar"}
        ],
        "correct_idx": 1,
        "explanation": "Aneurysms of the posterior communicating artery (PCommA), typically at its junction with the internal carotid artery, compress the adjacent oculomotor nerve (CN III). Because pupilloconstrictor parasympathetic fibers run superficially along the outer dorsomedial aspect of CN III, extrinsic compressive aneurysms cause early pupil dilation (mydriasis) and loss of pupillary light reflexes, accompanied by somatic CN III motor palsy (ptosis, \"down and out\" eye). In contrast, diabetic microvascular ischemia damages deep central fibers, sparing the superficial pupil.",
        "high_yield_pearl": "High-Yield Clinical Pearl: PCommA aneurysms compress CN III, causing pupillary dilation (superficial parasympathetics) and ptosis with \"down and out\" eye. Microvascular diabetic CN III ischemia spares the pupil.",
        "image": None
    })

    # Q76
    qs.append({
        "id": "exam3_in_house_like_g_q76",
        "q_num": "76",
        "stem": "A 63-year-old man presents with acute vertigo, severe limb ataxia in his right arm and leg, and nausea. Neurological examination reveals right-sided dysmetria on finger-to-nose testing, intention tremor, and an ipsilateral Horner syndrome (miosis and ptosis). Sensory examination demonstrates loss of pain and temperature on the left side of his body and extremities. Occlusion of which of the following arterial vessels best accounts for this cerebellar and brainstem syndrome?",
        "category": "Stroke (Blood Supply, Cerebrovascular, Brainstem)",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Anterior inferior cerebellar artery vascular trunk"},
            {"letter": "B", "is_correct": True, "text": "Superior cerebellar artery branch of basilar artery"},
            {"letter": "C", "is_correct": False, "text": "Posterior inferior cerebellar artery medullary branch"},
            {"letter": "D", "is_correct": False, "text": "Paramedian penetrating branch of the basilar artery"},
            {"letter": "E", "is_correct": False, "text": "Anterior spinal artery paramedian vascular branches"}
        ],
        "correct_idx": 1,
        "explanation": "The superior cerebellar artery (SCA) branches from the distal basilar artery just proximal to the posterior cerebral artery. It supplies the superior half of the cerebellum, the superior cerebellar peduncle, and the lateral rostral pontine/midbrain tegmentum. SCA infarction causes severe ipsilateral cerebellar limb ataxia (superior cerebellar peduncle and cerebellar cortex), nausea, ipsilateral Horner syndrome, and contralateral loss of pain and temperature on the body (spinothalamic tract).",
        "high_yield_pearl": "High-Yield Clinical Pearl: Superior cerebellar artery (SCA) infarct causes ipsilateral limb ataxia (superior cerebellar peduncle), ipsilateral Horner syndrome, and contralateral body pain/temp loss.",
        "image": None
    })

    # Q77
    qs.append({
        "id": "exam3_in_house_like_g_q77",
        "q_num": "77",
        "stem": "A 58-year-old woman presents with language difficulty following a stroke. Testing demonstrates fluent spontaneous speech with normal cadence, intact auditory comprehension (she correctly executes complex multi-step commands), but she exhibits a profound inability to repeat phrases spoken by the examiner. When asked to repeat \"the dog chased the brown rabbit,\" she produces multiple phonemic paraphasias and cannot reproduce the phrase. A lesion in which of the following neural pathways causes this condition?",
        "category": "Stroke (Blood Supply, Cerebrovascular, Brainstem)",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Inferior longitudinal fasciculus white matter tract"},
            {"letter": "B", "is_correct": True, "text": "Arcuate fasciculus connecting temporal and frontal lobes"},
            {"letter": "C", "is_correct": False, "text": "Uncinate fasciculus connecting limbic and frontal cortex"},
            {"letter": "D", "is_correct": False, "text": "Corpus callosum anterior commissural white matter"},
            {"letter": "E", "is_correct": False, "text": "Medial longitudinal fasciculus brainstem pathway"}
        ],
        "correct_idx": 1,
        "explanation": "Conduction aphasia is characterized by fluent speech, intact auditory comprehension, but severely impaired repetition with prominent phonemic paraphasias (word substitutions). It is caused by damage to the arcuate fasciculus (or superior longitudinal fasciculus), the subcortical white matter association tract that connects Wernicke area in the superior temporal gyrus with Broca area in the inferior frontal gyrus.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Conduction aphasia features fluent speech and intact comprehension, but severely impaired repetition; it is caused by damage to the arcuate fasciculus.",
        "image": None
    })

    # Q78
    qs.append({
        "id": "exam3_in_house_like_g_q78",
        "q_num": "78",
        "stem": "A 28-year-old postpartum woman on oral contraceptives presents with progressive unremitting diffuse headache, vomiting, and visual blurring. Funduscopic examination reveals bilateral papilledema. Neurological exam reveals bilateral lower extremity hyperreflexia and extensor plantar responses. Magnetic resonance venography confirms thrombosis of the superior sagittal sinus. Into which of the following dural venous sinuses does blood directly drain immediately after the confluence of sinuses?",
        "category": "Stroke (Blood Supply, Cerebrovascular, Brainstem)",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Superior petrosal dural venous sinus channels"},
            {"letter": "B", "is_correct": True, "text": "Transverse dural venous sinuses bilaterally"},
            {"letter": "C", "is_correct": False, "text": "Cavernous dural venous sinus vascular channels"},
            {"letter": "D", "is_correct": False, "text": "Inferior sagittal dural venous sinus pathway"},
            {"letter": "E", "is_correct": False, "text": "Internal jugular vein venous bulb terminus"}
        ],
        "correct_idx": 1,
        "explanation": "Cerebral venous drainage flows from cortical veins into the superior sagittal sinus and straight sinus, which unite at the confluence of sinuses (torcular Herophili) at the internal occipital protuberance. From the confluence, venous blood flows laterally into the paired transverse sinuses, continues into the S-shaped sigmoid sinuses, and exits the jugular foramen into the internal jugular veins.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Dural venous flow pathway: Superior sagittal sinus -> Confluence of sinuses -> Transverse sinuses -> Sigmoid sinuses -> Internal jugular vein.",
        "image": None
    })

    # =========================================================================
    # UNIT 7: STROKE - CEREBROVASCULAR DISEASE & ISCHEMIA (15 Qs: Q79 - Q93, 10%)
    # =========================================================================

    # Q79
    qs.append({
        "id": "exam3_in_house_like_g_q79",
        "q_num": "79",
        "stem": "A 68-year-old man presents with acute left-sided hemiplegia 2 hours after symptom onset. Perfusion-diffusion mismatch imaging on brain MRI demonstrates a small area of restricted diffusion (non-viable necrotic core) surrounded by a substantial, larger volume of hypoperfused cerebral tissue. Which of the following terms specifically designates this salvageable, hypoperfused tissue zone?",
        "category": "Stroke (Blood Supply, Cerebrovascular, Brainstem)",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Liquefactive core zone of irreversible destruction"},
            {"letter": "B", "is_correct": True, "text": "Ischemic penumbra zone of viable tissue at risk"},
            {"letter": "C", "is_correct": False, "text": "Gliotic border zone of chronic astrocytic scarring"},
            {"letter": "D", "is_correct": False, "text": "Microglial nodule zone of neuronal phagocytosis"},
            {"letter": "E", "is_correct": False, "text": "Fibrinoid necrotic zone of vascular destruction"}
        ],
        "correct_idx": 1,
        "explanation": "In acute ischemic stroke, the ischemic penumbra refers to the rim of hypoperfused, electrically silent, but structurally viable brain tissue surrounding the central irreversible necrotic ischemic core. Cells in the penumbra are kept marginally viable by collateral circulation. The primary clinical objective of acute reperfusion therapy (intravenous thrombolysis and endovascular mechanical thrombectomy) is to salvage the penumbra before irreversible infarction occurs.",
        "high_yield_pearl": "High-Yield Clinical Pearl: The ischemic penumbra is hypoperfused, metabolically compromised but salvageable brain tissue; timely reperfusion rescues the penumbra from progressing to infarction.",
        "image": None
    })

    # Q80
    qs.append({
        "id": "exam3_in_house_like_g_q80",
        "q_num": "80",
        "stem": "During an acute ischemic stroke, severe interruption of cerebral blood flow leads to rapid neuronal ATP depletion and failure of the Na+/K+-ATPase pump. This induces persistent cellular membrane depolarization and unregulated exocytosis of an excitatory neurotransmitter, triggering massive intracellular influx of calcium ions and activation of autolytic enzymes. Which of the following neurotransmitters is the primary mediator of this excitotoxic cascade?",
        "category": "Stroke (Blood Supply, Cerebrovascular, Brainstem)",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Gamma-aminobutyric acid inhibitory transmitter"},
            {"letter": "B", "is_correct": True, "text": "Glutamate excitatory neurotransmitter ligand"},
            {"letter": "C", "is_correct": False, "text": "Acetylcholine cholinergic neurotransmitter ligand"},
            {"letter": "D", "is_correct": False, "text": "Dopamine catecholaminergic neurotransmitter"},
            {"letter": "E", "is_correct": False, "text": "Serotonin indolaminergic neurotransmitter ligand"}
        ],
        "correct_idx": 1,
        "explanation": "Ischemic excitotoxicity is triggered by cellular energy failure (ATP depletion) and subsequent dysfunction of Na+/K+-ATPase pumps. Depolarized presynaptic terminals release massive amounts of glutamate into the synaptic cleft. Glutamate overstimulates postsynaptic NMDA and AMPA receptors, driving excessive intracellular calcium (Ca2+) influx. High intracellular calcium activates calcium-dependent proteases (calpains), phospholipases, and endonucleases, leading to apoptotic and necrotic neuronal death.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Ischemia causes ATP depletion, Na+/K+ pump failure, unregulated glutamate release, and massive Ca2+ influx via NMDA receptors, driving enzymatic cellular digestion.",
        "image": None
    })

    # Q81
    qs.append({
        "id": "exam3_in_house_like_g_q81",
        "q_num": "81",
        "stem": "A 64-year-old man presents to the emergency department 2 hours after the acute onset of right-sided weakness and expressive aphasia. Non-contrast head CT demonstrates no evidence of intracranial hemorrhage or acute infarction. Vital signs show blood pressure of 210/125 mm Hg, pulse 82/min, and respirations 16/min. The medical team considers intravenous recombinant tissue plasminogen activator (rtPA). Which of the following is an absolute contraindication to rtPA administration unless immediately corrected?",
        "category": "Stroke (Blood Supply, Cerebrovascular, Brainstem)",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Serum blood glucose level of 165 mg/dL on admission"},
            {"letter": "B", "is_correct": True, "text": "Sustained blood pressure exceeding 185/110 mm Hg"},
            {"letter": "C", "is_correct": False, "text": "Patient age exceeding 60 years at time of presentation"},
            {"letter": "D", "is_correct": False, "text": "History of well-controlled non-insulin diabetes"},
            {"letter": "E", "is_correct": False, "text": "Presence of mild non-disabling facial asymmetry"}
        ],
        "correct_idx": 1,
        "explanation": "Intravenous rtPA (alteplase/tenecteplase) is approved within 4.5 hours of last known normal for acute ischemic stroke. Severe uncontrolled hypertension with blood pressure >185 mm Hg systolic or >110 mm Hg diastolic is a major contraindication because it drastically increases the risk of fatal symptomatic intracerebral hemorrhage. Blood pressure must be aggressively lowered below 185/110 mm Hg (e.g., with IV labetalol or nicardipine) before rtPA can be safely administered.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Strict contraindications to IV rtPA include BP >185/110 mm Hg, active internal bleeding, recent head trauma/surgery within 3 months, prior intracranial hemorrhage, or INR >1.7.",
        "image": None
    })

    # Q82
    qs.append({
        "id": "exam3_in_house_like_g_q82",
        "q_num": "82",
        "stem": "A 70-year-old woman presents 5 hours after the onset of acute right hemiplegia, right hemisensory loss, global aphasia, and left-sided eye deviation. CT angiography reveals an acute occlusive thrombus in the proximal M1 segment of the left middle cerebral artery. Perfusion imaging confirms a small ischemic core with a large salvageable penumbra. Which of the following acute therapeutic interventions is indicated for this patient?",
        "category": "Stroke (Blood Supply, Cerebrovascular, Brainstem)",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "High-dose intravenous heparin infusion protocol"},
            {"letter": "B", "is_correct": True, "text": "Catheter-based endovascular mechanical thrombectomy"},
            {"letter": "C", "is_correct": False, "text": "Immediate therapeutic whole-body hypothermia cooling"},
            {"letter": "D", "is_correct": False, "text": "Intravenous recombinant tissue plasminogen activator"},
            {"letter": "E", "is_correct": False, "text": "Emergency surgical craniotomy with aneurysm clipping"}
        ],
        "correct_idx": 1,
        "explanation": "Endovascular mechanical thrombectomy is indicated for acute ischemic stroke caused by large vessel occlusion (LVO) of the internal carotid artery or proximal middle cerebral artery (M1 segment). Thrombectomy is proven effective up to 24 hours from last known normal in selected patients with imaging-confirmed mismatch between core infarct volume and clinical deficit/penumbra. Because this patient is beyond the 4.5-hour rtPA window, mechanical thrombectomy is the treatment of choice.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Endovascular mechanical thrombectomy is indicated for acute large vessel occlusion (proximal MCA or ICA) up to 24 hours in patients with salvageable penumbra on perfusion imaging.",
        "image": None
    })

    # Q83
    qs.append({
        "id": "exam3_in_house_like_g_q83",
        "q_num": "83",
        "stem": "A 67-year-old man presents with acute right-sided hemiparesis 6 hours after symptom onset, making him ineligible for intravenous thrombolysis. Admission blood pressure is 198/104 mm Hg. The neurology resident advises allowing \"permissive hypertension\" up to 220/120 mm Hg rather than acutely normalizing the patient's blood pressure. Which of the following is the primary physiologic rationale for this therapeutic strategy?",
        "category": "Stroke (Blood Supply, Cerebrovascular, Brainstem)",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Promote immediate lysis of the occlusive fibrin thrombus"},
            {"letter": "B", "is_correct": True, "text": "Maintain collateral perfusion to the ischemic penumbra"},
            {"letter": "C", "is_correct": False, "text": "Suppress central sympathetic outflow from the hypothalamus"},
            {"letter": "D", "is_correct": False, "text": "Prevent acute vasogenic edema around the necrotic core"},
            {"letter": "E", "is_correct": False, "text": "Facilitate rapid renal clearance of lactic acid metabolites"}
        ],
        "correct_idx": 1,
        "explanation": "In acute ischemic stroke without thrombolytic therapy, cerebral autoregulation is impaired in the ischemic zone. Blood flow into the ischemic penumbra becomes passively dependent on systemic mean arterial pressure through leptomeningeal collateral channels. Rapidly lowering blood pressure can critically reduce collateral perfusion pressure and convert salvageable penumbral tissue into completed infarction. Therefore, permissive hypertension up to 220/120 mm Hg is maintained unless organ damage occurs.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Permissive hypertension (up to 220/120 mm Hg in non-thrombolyzed stroke) maintains collateral blood flow to the ischemic penumbra in the setting of lost autoregulation.",
        "image": None
    })

    # Q84
    qs.append({
        "id": "exam3_in_house_like_g_q84",
        "q_num": "84",
        "stem": "A 68-year-old man with a 20-year history of poorly controlled hypertension presents with acute left-sided hemiplegia. Physical examination shows 1/5 strength in the left arm and leg and a left lower facial droop. Sensation, visual fields, and language are intact. Non-contrast CT demonstrates a 1-cm fluid-density cavity in the posterior limb of the right internal capsule. Which of the following vascular pathologies is the primary etiology of this lesion?",
        "category": "Stroke (Blood Supply, Cerebrovascular, Brainstem)",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Atherosclerotic plaque ulceration in the carotid bulb"},
            {"letter": "B", "is_correct": True, "text": "Lipohyalinosis and microatheroma of penetrating arteries"},
            {"letter": "C", "is_correct": False, "text": "Cardioembolic occlusion of the main middle cerebral trunk"},
            {"letter": "D", "is_correct": False, "text": "Arterial dissection with intramural hematoma expansion"},
            {"letter": "E", "is_correct": False, "text": "Leptomeningeal arteriovenous malformation with thrombosis"}
        ],
        "correct_idx": 1,
        "explanation": "Lacunar infarcts are small (<15 mm), non-cortical infarcts caused by occlusion of single small penetrating arterioles (lenticulostriate, thalamoperforating, or paramedian basilar branches). Chronic hypertension and diabetes induce lipohyalinosis (vessel wall thickening, endothelial leakage of plasma proteins, and luminal narrowing) and microatheroma formation in these long, narrow vessels, leading to microinfarction and resulting in cavitary lacunes.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Lacunar strokes result from lipohyalinosis and microatheromas in small penetrating arteries (e.g., lenticulostriates) secondary to chronic hypertension and diabetes.",
        "image": None
    })

    # Q85
    qs.append({
        "id": "exam3_in_house_like_g_q85",
        "q_num": "85",
        "stem": "A 65-year-old woman with chronic hypertension presents with sudden onset of numbness and tingling over her right face, right arm, and right leg. Physical examination confirms loss of light touch, pinprick, and vibration sensation over the entire right side of her body. Muscle strength, deep tendon reflexes, cranial nerve motor functions, and cerebellar coordination are completely intact. An acute lacunar stroke is suspected. In which of the following structures is this lesion localized?",
        "category": "Stroke (Blood Supply, Cerebrovascular, Brainstem)",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Anterior limb of the left internal capsule structure"},
            {"letter": "B", "is_correct": True, "text": "Ventral posterolateral and posteromedial thalamic nuclei"},
            {"letter": "C", "is_correct": False, "text": "Genu of the left internal capsule white matter tract"},
            {"letter": "D", "is_correct": False, "text": "Basis pontis along the descending corticospinal fibers"},
            {"letter": "E", "is_correct": False, "text": "Caudate nucleus head along the lateral ventricular wall"}
        ],
        "correct_idx": 1,
        "explanation": "A pure sensory stroke is a classic lacunar syndrome resulting from infarction of the sensory relay nuclei of the thalamus (ventral posterolateral [VPL] nucleus for body sensory input from the medial lemniscus and spinothalamic tract, and ventral posteromedial [VPM] nucleus for facial sensation from the trigeminothalamic tract). It is caused by lipohyalinotic occlusion of thalamoperforating branches of the posterior cerebral artery.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Pure sensory stroke is a lacunar syndrome caused by infarction of the thalamic VPL/VPM nuclei via occlusion of thalamoperforating branches of the PCA.",
        "image": None
    })

    # Q86
    qs.append({
        "id": "exam3_in_house_like_g_q86",
        "q_num": "86",
        "stem": "A 61-year-old man presents with right leg and arm weakness accompanied by prominent incoordination in the same extremities. Physical examination reveals mild right hemiparesis (strength 4/5), but prominent right-sided dysmetria on finger-to-nose and heel-to-shin testing that is out of proportion to the weakness. Speech and sensation are completely normal. Which of the following lacunar stroke syndromes does this patient exhibit?",
        "category": "Stroke (Blood Supply, Cerebrovascular, Brainstem)",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Pure motor hemiparesis syndrome of internal capsule"},
            {"letter": "B", "is_correct": True, "text": "Ataxic hemiparesis syndrome of capsule or basis pontis"},
            {"letter": "C", "is_correct": False, "text": "Dysarthria-clumsy hand lacunar stroke syndrome of pons"},
            {"letter": "D", "is_correct": False, "text": "Pure sensory stroke syndrome of posterolateral thalamus"},
            {"letter": "E", "is_correct": False, "text": "Sensorimotor lacunar syndrome of thalamus and capsule"}
        ],
        "correct_idx": 1,
        "explanation": "Ataxic hemiparesis is one of the classic lacunar stroke syndromes, characterized by ipsilateral motor weakness and cerebellar ataxia out of proportion to the motor deficit. The most common anatomical localization is either the posterior limb/anterior limb/genu of the internal capsule or the basis pontis (affecting both descending corticospinal motor fibers and adjacent pontocerebellar tracts).",
        "high_yield_pearl": "High-Yield Clinical Pearl: Ataxic hemiparesis is a lacunar syndrome (internal capsule or basis pontis) featuring combination of mild hemiparesis and prominent ipsilateral limb ataxia.",
        "image": None
    })

    # Q87
    qs.append({
        "id": "exam3_in_house_like_g_q87",
        "q_num": "87",
        "stem": "A 48-year-old woman presents to the emergency department complaining of an excruciating, explosive headache that began suddenly while exercising. She describes it as \"the worst headache of my entire life.\" Physical examination shows marked nuchal rigidity without focal motor weakness. A non-contrast head CT performed 4 hours after symptom onset demonstrates hyperattenuating blood in the basal cisterns and sulcal spaces. What is the most common underlying cause of this condition?",
        "category": "Stroke (Blood Supply, Cerebrovascular, Brainstem)",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Rupture of Charcot-Bouchard penetrating microaneurysms"},
            {"letter": "B", "is_correct": True, "text": "Rupture of a saccular berry aneurysm in Circle of Willis"},
            {"letter": "C", "is_correct": False, "text": "Tearing of parasagittal cortical bridging venous vessels"},
            {"letter": "D", "is_correct": False, "text": "Rupture of the middle meningeal artery after head trauma"},
            {"letter": "E", "is_correct": False, "text": "Cerebral amyloid angiopathy of cortical lobar vessels"}
        ],
        "correct_idx": 1,
        "explanation": "Nontraumatic subarachnoid hemorrhage (SAH) is most commonly (85% of cases) caused by rupture of a saccular (berry) aneurysm located at arterial bifurcations in the Circle of Willis (most commonly the anterior communicating artery). Patients classically present with an abrupt, excruciating \"thunderclap\" headache (\"worst headache of life\"), vomiting, meningismus, and loss of consciousness.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Subarachnoid hemorrhage classically presents with sudden \"thunderclap\" headache and meningismus; 85% are caused by rupture of a saccular berry aneurysm in the Circle of Willis.",
        "image": None
    })

    # Q88
    qs.append({
        "id": "exam3_in_house_like_g_q88",
        "q_num": "88",
        "stem": "A 52-year-old woman is admitted to the neuro-intensive care unit following endovascular coiling of a ruptured anterior communicating artery aneurysm. On hospital day 7, she develops new-onset confusion and mild left hemiparesis. Repeat head CT shows no re-bleeding or hydrocephalus. Transcranial Doppler demonstrates marked elevation of middle cerebral artery blood flow velocities consistent with arterial vasospasm. Which of the following medications is routinely administered to prevent this complication?",
        "category": "Stroke (Blood Supply, Cerebrovascular, Brainstem)",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Intravenous high-dose sodium nitroprusside vasodilator"},
            {"letter": "B", "is_correct": True, "text": "Oral nimodipine dihydropyridine calcium channel blocker"},
            {"letter": "C", "is_correct": False, "text": "Intravenous broad-spectrum methylprednisolone steroid"},
            {"letter": "D", "is_correct": False, "text": "Intravenous recombinant tissue plasminogen activator"},
            {"letter": "E", "is_correct": False, "text": "Oral aspirin plus clopidogrel antiplatelet therapy"}
        ],
        "correct_idx": 1,
        "explanation": "Cerebral vasospasm and delayed cerebral ischemia typically occur 4 to 14 days after aneurysmal subarachnoid hemorrhage, triggered by the breakdown products of blood (especially oxyhemoglobin) in the subarachnoid space. Oral nimodipine (a lipophilic dihydropyridine calcium channel blocker) is initiated in all patients with aneurysmal SAH to prevent vasospasm and improve neurological outcomes.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Cerebral vasospasm occurs 4-14 days post-SAH due to blood breakdown products; oral nimodipine is administered to prevent vasospasm and delayed cerebral ischemia.",
        "image": None
    })

    # Q89
    qs.append({
        "id": "exam3_in_house_like_g_q89",
        "q_num": "89",
        "stem": "A 63-year-old man with longstanding untreated hypertension collapses at home. On arrival to the ED, he is stuporous with a blood pressure of 230/130 mm Hg. Examination reveals dense left hemiplegia, left hemisensory loss, and conjugate eye deviation to the right. Non-contrast head CT demonstrates a 4.5-cm acute hyperdense intraparenchymal hematoma in the right putamen with mass effect and midline shift. Rupture of which of the following microvascular structures is the primary cause of this hemorrhage?",
        "category": "Stroke (Blood Supply, Cerebrovascular, Brainstem)",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Congenital saccular aneurysms at the anterior communicating"},
            {"letter": "B", "is_correct": True, "text": "Charcot-Bouchard microaneurysms in lenticulostriate vessels"},
            {"letter": "C", "is_correct": False, "text": "Subcortical amyloid-beta deposits in leptomeningeal walls"},
            {"letter": "D", "is_correct": False, "text": "Arteriovenous malformations in superficial cortical veins"},
            {"letter": "E", "is_correct": False, "text": "Fusiform atherosclerotic ectasias in the basilar artery"}
        ],
        "correct_idx": 1,
        "explanation": "Hypertensive intracerebral hemorrhage (ICH) is the most common cause of non-traumatic parenchymal brain hemorrhage. Chronic severe hypertension damages small penetrating arteries (lenticulostriate branches of MCA), causing lipohyalinosis and formation of Charcot-Bouchard microaneurysms. The most common site of hypertensive ICH is the putamen (basal ganglia, ~50%), followed by the thalamus, pons, and cerebellum.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Hypertensive intracerebral hemorrhage is caused by rupture of Charcot-Bouchard microaneurysms; the putamen (lenticulostriate vessels) is the most frequent location.",
        "image": None
    })

    # Q90
    qs.append({
        "id": "exam3_in_house_like_g_q90",
        "q_num": "90",
        "stem": "A 79-year-old woman with mild Alzheimer disease presents with sudden right-sided weakness and confusion. Brain CT demonstrates a subcortical lobar hemorrhage in the left parietal lobe. Review of her records shows that she experienced a right frontal lobar hemorrhage 18 months ago. She has no history of hypertension. Histopathologic examination of cerebral cortical vessels reveals vessel wall thickening with Congo red staining that displays apple-green birefringence under polarized light. What is the diagnosis?",
        "category": "Stroke (Blood Supply, Cerebrovascular, Brainstem)",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Hypertensive arteriolosclerosis with Charcot-Bouchard"},
            {"letter": "B", "is_correct": True, "text": "Cerebral amyloid angiopathy with recurrent lobar bleed"},
            {"letter": "C", "is_correct": False, "text": "Granulomatous angiitis of the central nervous system"},
            {"letter": "D", "is_correct": False, "text": "Cavernous malformation with intraparenchymal bleed"},
            {"letter": "E", "is_correct": False, "text": "Fibromuscular dysplasia with recurrent ischemic stroke"}
        ],
        "correct_idx": 1,
        "explanation": "Cerebral amyloid angiopathy (CAA) is the most common cause of recurrent, spontaneous lobar (superficial cortical/subcortical) intracerebral hemorrhage in elderly, non-hypertensive patients. It is caused by deposition of beta-amyloid peptide in the media and adventitia of small-to-medium-sized cortical and leptomeningeal arteries, making them fragile and prone to rupture. Apple-green birefringence under polarized light after Congo red staining is diagnostic.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Cerebral amyloid angiopathy causes recurrent lobar intracerebral hemorrhages in elderly non-hypertensive patients; Congo red stain shows apple-green birefringence.",
        "image": None
    })

    # Q91
    qs.append({
        "id": "exam3_in_house_like_g_q91",
        "q_num": "91",
        "stem": "A 32-year-old man presents with acute right-sided neck pain and headache 1 day after a vigorous chiropractic cervical manipulation. Physical examination demonstrates mild ptosis of the right upper eyelid and pupillary miosis in the right eye, but facial sweating is completely normal. Four hours later, he develops transient weakness and numbness of the left arm. Magnetic resonance angiography confirms an intramural hematoma with a \"string sign.\" Which of the following conditions is present?",
        "category": "Stroke (Blood Supply, Cerebrovascular, Brainstem)",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Subclavian steal syndrome secondary to proximal occlusion"},
            {"letter": "B", "is_correct": True, "text": "Internal carotid artery dissection with partial Horner"},
            {"letter": "C", "is_correct": False, "text": "Vertebral artery aneurysm compression of the brainstem"},
            {"letter": "D", "is_correct": False, "text": "Giant cell arteritis involving the external carotid branches"},
            {"letter": "E", "is_correct": False, "text": "Takayasu arteritis involving the aortic arch branches"}
        ],
        "correct_idx": 1,
        "explanation": "Internal carotid artery (ICA) dissection is a leading cause of stroke in young patients, often triggered by minor neck trauma or cervical manipulation. A tear in the arterial intima allows blood under pressure to enter the vessel wall, creating a false lumen/intramural hematoma that narrows the true lumen (\"string sign\"). Compression of ascending sympathetic fibers traveling along the ICA causes an ipsilateral partial Horner syndrome (ptosis and miosis, without anhidrosis because sudomotor fibers travel with the external carotid). Thrombus formation can embolize distally, causing cerebral TIA or stroke.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Internal carotid dissection (trauma/manipulation) causes unilateral neck pain, partial Horner syndrome (ptosis/miosis without anhidrosis), and contralateral TIA/stroke.",
        "image": None
    })

    # Q92
    qs.append({
        "id": "exam3_in_house_like_g_q92",
        "q_num": "92",
        "stem": "A 73-year-old woman with a history of chronic non-valvular atrial fibrillation who is not taking anticoagulation presents with acute right-sided hemiparesis and expressive aphasia. Brain MRI reveals multiple wedge-shaped cortical hyperintensities involving both the left middle cerebral and right posterior cerebral artery territories. Which of the following mechanisms is the primary cause of these multifocal territorial cerebral infarctions?",
        "category": "Stroke (Blood Supply, Cerebrovascular, Brainstem)",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Severe diffuse intracranial small vessel lipohyalinosis"},
            {"letter": "B", "is_correct": True, "text": "Cardioembolic occlusion from left atrial appendage thrombi"},
            {"letter": "C", "is_correct": False, "text": "Hemodynamic watershed hypoperfusion during sleep apnea"},
            {"letter": "D", "is_correct": False, "text": "In situ large vessel atherothrombosis of both arteries"},
            {"letter": "E", "is_correct": False, "text": "Cerebral venous sinus thrombosis with venous congestion"}
        ],
        "correct_idx": 1,
        "explanation": "Cardioembolic stroke accounts for ~20-30% of all ischemic strokes, most commonly arising from thrombi forming in the left atrial appendage in patients with atrial fibrillation. Emboli typically produce sudden, maximal neurological deficits at onset and lodge in distal cortical branches, causing wedge-shaped cortical infarcts. The involvement of multiple distinct vascular territories (left MCA and right PCA) is a hallmark of a proximal embolic source.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Cardioembolic strokes (atrial fibrillation) present with sudden maximal deficit and multiple wedge-shaped cortical infarcts across different vascular territories; treat with oral anticoagulation.",
        "image": None
    })

    # Q93
    qs.append({
        "id": "exam3_in_house_like_g_q93",
        "q_num": "93",
        "stem": "An 18-year-old male is struck in the temporal region by a baseball. He initially loses consciousness for 1 minute, but quickly recovers and appears fully alert and conversant for 2 hours (\"lucid interval\"). He then rapidly develops severe headache, vomiting, progressive somnolence, and a dilated unreactive ipsilateral pupil. Non-contrast head CT demonstrates a biconvex (lens-shaped) hyperdense collection that does not cross cranial suture lines. Rupture of which of the following vessels is responsible?",
        "category": "Stroke (Blood Supply, Cerebrovascular, Brainstem)",
        "source": "in_house_like_G (150 Questions)",
        "options": [
            {"letter": "A", "is_correct": False, "text": "Parasagittal bridging veins draining into superior sinus"},
            {"letter": "B", "is_correct": True, "text": "Middle meningeal artery branch of the maxillary artery"},
            {"letter": "C", "is_correct": False, "text": "Superficial temporal artery branch of external carotid"},
            {"letter": "D", "is_correct": False, "text": "Anterior inferior cerebellar artery cerebellar branch"},
            {"letter": "E", "is_correct": False, "text": "Ophthalmic artery branch supplying the orbital cavity"}
        ],
        "correct_idx": 1,
        "explanation": "Epidural hematoma is classically caused by skull fracture at the pterion (where the frontal, parietal, temporal, and sphenoid bones articulate), which lacerates the underlying middle meningeal artery (a branch of the maxillary artery). Arterial bleeding rapidly strips the dura from the calvarium, creating a biconvex (lenticular) hyperdense collection on CT that is limited by suture lines where the dura is firmly adherent. A classic \"lucid interval\" precedes rapid neurological collapse and uncal herniation.",
        "high_yield_pearl": "High-Yield Clinical Pearl: Epidural hematoma is caused by middle meningeal artery rupture at the pterion; features a lucid interval and biconvex (lens-shaped) collection limited by suture lines.",
        "image": None
    })

    return qs

if __name__ == '__main__':
    qs = get_part2_questions()
    print(f"Generated {len(qs)} questions for Part 2 (Q49 - Q93).")
