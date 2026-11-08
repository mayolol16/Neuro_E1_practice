import json
from test_gen_structure import check_q

u3_questions = [
    {
        "id": "exam3_g_h_u3_q1",
        "category": "Unit 03: Tumors",
        "subcategory": "Adult Gliomas",
        "question_type": "clinical_vignette",
        "stem": "A 63-year-old man presents with rapid cognitive decline, personality changes, and morning headaches over four weeks. Brain MRI shows a solitary 4.5-cm rim-enhancing frontotemporal mass crossing the corpus callosum with extensive surrounding vasogenic edema. Histopathology confirms a Grade 4 astrocytoma with pseudopalisading necrosis and microvascular proliferation. Molecular testing reveals hypermethylation of the O6-methylguanine-DNA methyltransferase (MGMT) gene promoter. What is the clinical significance of this epigenetic alteration?",
        "options": [
            {"label": "A", "text": "Enhanced tumor susceptibility and improved response to temozolomide chemotherapy", "is_correct": True},
            {"label": "B", "text": "Resistance to ionizing radiation therapy requiring high-dose stereotactic surgery", "is_correct": False},
            {"label": "C", "text": "Significantly elevated risk of leptomeningeal dissemination along spinal cord", "is_correct": False},
            {"label": "D", "text": "Rapid loss of heterozygosity in the neurofibromatosis tumor suppressor gene", "is_correct": False},
            {"label": "E", "text": "Constitutive vascular endothelial growth factor overexpression and hemorrhage", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "In glioblastoma (GBM), MGMT promoter hypermethylation silences the MGMT DNA-repair enzyme, which would otherwise remove alkyl adducts created by temozolomide. Silencing MGMT prevents tumor cells from repairing alkylating chemotherapy damage, conferring significantly improved sensitivity to temozolomide and better overall survival.",
        "high_yield_takeaway": "MGMT promoter methylation silences DNA repair in glioblastoma, conferring increased sensitivity to temozolomide and improved survival."
    },
    {
        "id": "exam3_g_h_u3_q2",
        "category": "Unit 03: Tumors",
        "subcategory": "Extra-axial Neoplasms",
        "question_type": "clinical_vignette",
        "stem": "A 32-year-old woman in her 34th week of gestation develops new-onset focal motor seizures involving her left hand. Brain MRI demonstrates an extra-axial, dural-based, intensely enhancing mass along the right parasagittal frontoparietal convexity with a distinct dural tail sign. Biopsy demonstrates whorled syncytial clusters of spindle cells containing psammoma bodies. What hormonal characteristic of this tumor explains its accelerated clinical presentation during the third trimester?",
        "options": [
            {"label": "A", "text": "High expression of functional nuclear progesterone receptors driving cell growth", "is_correct": True},
            {"label": "B", "text": "Constitutive overexpression of human chorionic gonadotropin-stimulated receptors", "is_correct": False},
            {"label": "C", "text": "Suppression of epidermal growth factor receptor signaling by placental lactogen", "is_correct": False},
            {"label": "D", "text": "Selective reliance on elevated circulating prolactin for angiogenic signaling", "is_correct": False},
            {"label": "E", "text": "Inactivation of mineralocorticoid receptors by elevated free plasma aldosterone", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "Meningiomas arise from arachnoid cap cells and frequently express progesterone receptors (up to 70-80% of cases). During pregnancy (particularly the third trimester when circulating progesterone levels are highest), meningiomas can rapidly enlarge and produce new-onset neurological deficits or seizures, followed by potential postpartum regression.",
        "high_yield_takeaway": "Meningiomas are extra-axial dural-based tumors that express progesterone receptors, causing rapid growth and symptom onset during pregnancy."
    },
    {
        "id": "exam3_g_h_u3_q3",
        "category": "Unit 03: Tumors",
        "subcategory": "Adult Gliomas",
        "question_type": "clinical_vignette",
        "stem": "A 45-year-old man presents following an unprovoked generalized tonic-clonic seizure. Non-contrast head CT reveals a well-demarcated cortical mass in the right frontal lobe with coarse intrinsic calcifications. Histopathological examination shows monomorphic round cells with clear perinuclear halos ('fried-egg' appearance) embedded in a network of branching delicate capillaries ('chicken-wire' pattern). Cytogenetic analysis demonstrates complete whole-arm co-deletion of chromosomes 1p and 19q. What is the clinical implication of this chromosomal finding?",
        "options": [
            {"label": "A", "text": "Marked therapeutic sensitivity to alkylating chemotherapy and favorable prognosis", "is_correct": True},
            {"label": "B", "text": "High resistance to radiotherapy and rapid dedifferentiation to glioblastoma", "is_correct": False},
            {"label": "C", "text": "Predisposition to aggressive multicentric metastases outside the neuroaxis", "is_correct": False},
            {"label": "D", "text": "Contraindication to gross total surgical resection due to high bleeding risk", "is_correct": False},
            {"label": "E", "text": "Need for emergent bilateral optic nerve decompression to prevent blindness", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "Oligodendrogliomas are defined molecularly by IDH mutation and 1p/19q codeletion (formed by an unbalanced translocation t(1;19)(q10;p10)). The 1p/19q codeletion confers exquisite sensitivity to procarbazine-CCNU-vincristine (PCV) and temozolomide chemotherapy, and is associated with significantly longer overall survival.",
        "high_yield_takeaway": "Oligodendrogliomas have 'fried-egg' cells, 'chicken-wire' vessels, calcifications, and 1p/19q codeletion predicting chemosensitivity and prolonged survival."
    },
    {
        "id": "exam3_g_h_u3_q4",
        "category": "Unit 03: Tumors",
        "subcategory": "Nerve Sheath Tumors",
        "question_type": "clinical_vignette",
        "stem": "A 51-year-old woman presents with progressive right-sided sensorineural hearing loss, unsteadiness, mild facial asymmetry, and an absent right corneal reflex. MRI reveals a 3.5-cm well-circumscribed mass centered within the right cerebellopontine angle, expanding the internal acoustic meatus. Biopsy demonstrates alternating dense cellular zones with nuclear palisading (Verocay bodies) and hypocellular myxoid regions, staining strongly positive for S100 protein. From which embryologic precursor cells did this neoplasm originate?",
        "options": [
            {"label": "A", "text": "Neural crest cells migrating to form myelinating peripheral glia", "is_correct": True},
            {"label": "B", "text": "Neuroectoderm cells forming central myelinating oligodendrocytes", "is_correct": False},
            {"label": "C", "text": "Surface ectoderm invaginating into the primitive oral stomodeum", "is_correct": False},
            {"label": "D", "text": "Mesodermal angioblasts forming cerebellar capillary loops", "is_correct": False},
            {"label": "E", "text": "Ependymal radial glia lining the floor of the fourth ventricle", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "Schwannomas arise from Schwann cells, which are derived from neural crest cells (along with melanocytes, chromaffin cells, dorsal root ganglia, and autonomic ganglia). Schwann cells are S100 positive because S100 is an acidic calcium-binding protein characteristic of neural-crest-derived cells. Acoustic schwannomas typically arise from the vestibular division of CN VIII at the cerebellopontine angle.",
        "high_yield_takeaway": "Schwannomas originate from neural crest-derived Schwann cells, stain positive for S100, and show Antoni A (Verocay bodies) and Antoni B patterns."
    },
    {
        "id": "exam3_g_h_u3_q5",
        "category": "Unit 03: Tumors",
        "subcategory": "Pediatric Posterior Fossa",
        "question_type": "clinical_vignette",
        "stem": "An 8-year-old girl is evaluated for morning nausea, vomiting, and progressive right-sided clumsiness. Posterior fossa MRI reveals a large cystic mass with an intensely enhancing mural nodule in the right cerebellar hemisphere. Following surgical resection, histopathology demonstrates biphasic tissue composed of bipolar piloid astrocytes with hair-like processes, eosinophilic Rosenthal fibers, and granular bodies. Which molecular alteration is most commonly the primary genetic driver of this neoplasm?",
        "options": [
            {"label": "A", "text": "Tandem duplication resulting in a KIAA1549-BRAF gene fusion", "is_correct": True},
            {"label": "B", "text": "Amplification of MYC oncogene with chromosome 17q gain", "is_correct": False},
            {"label": "C", "text": "Germline loss-of-function mutation in the NF2 gene on 22q", "is_correct": False},
            {"label": "D", "text": "Somatic mutation in the GNAQ gene leading to mTOR activation", "is_correct": False},
            {"label": "E", "text": "Deletions involving the SMARCB1 (INI1) tumor suppressor gene", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "Pilocytic astrocytoma (WHO Grade 1) is the most common pediatric primary brain tumor, typically presenting in the cerebellum as a cystic mass with an enhancing mural nodule. The classic histological features are bipolar astrocytes with hair-like processes, eosinophilic corkscrew-shaped Rosenthal fibers, and granular bodies. The vast majority (>70%) harbor a KIAA1549-BRAF gene fusion that constitutively activates the MAPK/ERK pathway.",
        "high_yield_takeaway": "Pilocytic astrocytoma is a benign pediatric cerebellar tumor (cystic with mural nodule, Rosenthal fibers, GFAP+) driven by KIAA1549-BRAF gene fusion."
    },
    {
        "id": "exam3_g_h_u3_q6",
        "category": "Unit 03: Tumors",
        "subcategory": "Pediatric Posterior Fossa",
        "question_type": "clinical_vignette",
        "stem": "A 7-year-old boy presents with severe gait ataxia, papilledema, and vomiting. Neuroimaging identifies a hyperdense, avidly enhancing midline cerebellar vermian mass obstructing the fourth ventricle. Resection reveals sheets of small, round, blue cells with hyperchromatic nuclei forming Homer Wright rosettes and expressing synaptophysin. Following operative resection, what critical diagnostic staging evaluation must be performed prior to craniospinal radiotherapy?",
        "options": [
            {"label": "A", "text": "Contrast-enhanced total neuroaxis spine MRI and CSF cytologic analysis", "is_correct": True},
            {"label": "B", "text": "Whole-body 18F-fluorodeoxyglucose PET scan to evaluate bone metastases", "is_correct": False},
            {"label": "C", "text": "High-resolution computed tomography of the chest, abdomen, and pelvis", "is_correct": False},
            {"label": "D", "text": "Bone marrow aspiration and core biopsy from posterior iliac crests", "is_correct": False},
            {"label": "E", "text": "Urinary catecholamine metabolite quantification for pheochromocytoma", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "Medulloblastoma is a WHO Grade 4 primitive embryonal neuroepithelial tumor (small round blue cells, Homer Wright rosettes, synaptophysin+) originating in the cerebellar vermis. It has a high propensity to disseminate through CSF pathways across the craniospinal axis ('drop metastases' to cauda equina). Full staging requires total neuroaxis spinal MRI and lumbar CSF cytology (obtained post-operatively once mass effect is relieved).",
        "high_yield_takeaway": "Medulloblastoma (small round blue cells, Homer Wright rosettes) carries high risk for CSF seeding ('drop metastases'), requiring total neuroaxis MRI and CSF cytology."
    },
    {
        "id": "exam3_g_h_u3_q7",
        "category": "Unit 03: Tumors",
        "subcategory": "VHL & Vascular Tumors",
        "question_type": "clinical_vignette",
        "stem": "A 38-year-old man presents with progressive limb unsteadiness and persistent headaches. Routine laboratory studies show a hemoglobin of 19.8 g/dL and hematocrit of 59%. Brain MRI reveals a highly vascular cystic lesion with an enhancing mural nodule in the cerebellar hemisphere. Histology reveals lipid-rich foamy stromal cells interspersed among extensive thin-walled capillary networks. What molecular mechanism directly links his underlying genetic defect to the erythrocytosis?",
        "options": [
            {"label": "A", "text": "Impaired degradation of hypoxia-inducible factor driving erythropoietin", "is_correct": True},
            {"label": "B", "text": "Constitutive hyperactivation of fibroblast growth factor receptor kinase", "is_correct": False},
            {"label": "C", "text": "Direct somatic mutation in the erythropoietin receptor promoter region", "is_correct": False},
            {"label": "D", "text": "Defective ubiquitination of tuberin stimulating mTOR protein synthesis", "is_correct": False},
            {"label": "E", "text": "Overexpression of platelet-derived growth factor stimulating stem cells", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "This patient has a cerebellar hemangioblastoma, a hallmark of von Hippel-Lindau (VHL) disease (chromosome 3p). The VHL tumor suppressor protein forms part of an E3 ubiquitin ligase that targets hypoxia-inducible factor 1-alpha (HIF-1alpha) for proteasomal degradation under normoxic conditions. Loss of VHL causes constitutive HIF-1alpha accumulation, driving transcription of VEGF, PDGF, and erythropoietin (EPO), resulting in paraneoplastic secondary polycythemia.",
        "high_yield_takeaway": "VHL mutations prevent ubiquitin-mediated degradation of HIF-1alpha, driving VEGF and EPO transcription, leading to hemangioblastomas and secondary polycythemia."
    },
    {
        "id": "exam3_g_h_u3_q8",
        "category": "Unit 03: Tumors",
        "subcategory": "Sellar & Suprasellar Tumors",
        "question_type": "clinical_vignette",
        "stem": "A 10-year-old boy is brought to the clinic due to poor linear growth, excessive thirst, and progressive difficulty reading off the board at school. Visual field examination reveals bitemporal hemianopsia. Sagittal MRI shows a partially cystic, calcified sellar and suprasellar mass that displaces the optic chiasm upward. Aspiration yields viscous, dark brown fluid resembling 'crankcase motor oil' that contains abundant cholesterol crystals. From which embryonic precursor did this neoplasm develop?",
        "options": [
            {"label": "A", "text": "Rathke pouch diverticulum of the oral cavity surface ectoderm", "is_correct": True},
            {"label": "B", "text": "Diencephalic neuroectodermal outgrowth forming the neurohypophysis", "is_correct": False},
            {"label": "C", "text": "Mesodermal paraxial condensations surrounding the primitive chorda", "is_correct": False},
            {"label": "D", "text": "Neural crest cells migrating into the first pharyngeal arch complex", "is_correct": False},
            {"label": "E", "text": "Endodermal epithelium derived from the ventral wall of the foregut", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "Craniopharyngiomas are benign suprasellar tumors derived from remnants of Rathke pouch, an ectodermal outpocketing of the primitive stomodeum (oral cavity roof) that normally forms the anterior pituitary. They typically exhibit cystic components containing rich 'motor oil' fluid filled with glistening cholesterol crystals, peripheral rim calcifications on CT, and compression of the optic chiasm (bitemporal hemianopsia) and pituitary stalk.",
        "high_yield_takeaway": "Craniopharyngiomas derive from Rathke pouch (surface ectoderm), contain 'motor oil' fluid with cholesterol crystals, calcify, and cause bitemporal hemianopsia."
    },
    {
        "id": "exam3_g_h_u3_q9",
        "category": "Unit 03: Tumors",
        "subcategory": "Phakomatoses",
        "question_type": "clinical_vignette",
        "stem": "A 14-year-old girl is evaluated for progressive painless vision loss in her left eye. Physical examination demonstrates eight café-au-lait macules greater than 1.5 cm across her trunk, dense axillary freckling, and multiple raised dome-shaped brown iris hamartomas. Contrast-enhanced MRI reveals diffuse thickening and enhancement of the left optic nerve consistent with an optic pathway glioma. The protein normally encoded by the gene mutated in this condition acts primarily through which cellular mechanism?",
        "options": [
            {"label": "A", "text": "Accelerating the hydrolysis of active Ras-GTP to inactive Ras-GDP", "is_correct": True},
            {"label": "B", "text": "Phosphorylating p53 to initiate apoptotic arrest during DNA damage", "is_correct": False},
            {"label": "C", "text": "Scaffolding membrane actin filaments to establish contact inhibition", "is_correct": False},
            {"label": "D", "text": "Forming an E3 ubiquitin ligase targeting hypoxia-inducible factors", "is_correct": False},
            {"label": "E", "text": "Inactivating Rheb GTPase to suppress downstream mTORC1 signaling", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "This patient has Neurofibromatosis Type 1 (NF1, von Recklinghausen disease) due to an autosomal dominant mutation in NF1 on chromosome 17q11. NF1 encodes neurofibromin, a GTPase-activating protein (GAP) that hydrolyzes active Ras-GTP to inactive Ras-GDP. Loss of neurofibromin leads to constitutive Ras activation and uncontrolled cell proliferation, manifesting as café-au-lait spots, axillary freckling (Crowe sign), Lisch nodules, and optic pathway gliomas.",
        "high_yield_takeaway": "NF1 (chromosome 17) encodes neurofibromin, a Ras-GAP that inactivates Ras-GTP; loss leads to constitutive Ras hyperactivation, optic gliomas, and Lisch nodules."
    },
    {
        "id": "exam3_g_h_u3_q10",
        "category": "Unit 03: Tumors",
        "subcategory": "Phakomatoses",
        "question_type": "clinical_vignette",
        "stem": "A 27-year-old woman presents with progressive bilateral hearing loss and recurrent unsteadiness. Brain MRI demonstrates bilateral enhancing masses in the cerebellopontine angles expanding both internal acoustic meatuses, as well as multiple dural-based parietal convex masses with dural tails. Genetic testing reveals a heterozygous inactivating mutation in a tumor suppressor gene located on chromosome 22q12. What is the fundamental physiological role of the protein encoded by this gene?",
        "options": [
            {"label": "A", "text": "Linking the actin cytoskeleton to cell-surface contact-inhibition proteins", "is_correct": True},
            {"label": "B", "text": "Binding free cytoplasmic iron to prevent generation of hydroxyl radicals", "is_correct": False},
            {"label": "C", "text": "Hydrolyzing epidermal growth factor receptor extracellular domains", "is_correct": False},
            {"label": "D", "text": "Catalyzing DNA double-strand break repair via homologous recombination", "is_correct": False},
            {"label": "E", "text": "Ubiquitinating cytosolic oncoproteins to trigger proteasomal destruction", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "Neurofibromatosis Type 2 (NF2) is caused by mutations on chromosome 22q12 in the NF2 gene encoding merlin (schwannomin). Merlin is a member of the ERM (ezrin-radixin-moesin) protein family that links actin cytoskeleton to cell membrane glycoproteins (such as CD44) to mediate contact inhibition of cell growth. Deficiency of merlin causes multiple schwannomas (characteristically bilateral vestibular schwannomas), meningiomas, and ependymomas (MISME syndrome).",
        "high_yield_takeaway": "NF2 (chromosome 22q) encodes merlin, a cytoskeletal scaffolding protein mediating contact inhibition; loss causes bilateral acoustic schwannomas, meningiomas, and ependymomas."
    },
    {
        "id": "exam3_g_h_u3_q11",
        "category": "Unit 03: Tumors",
        "subcategory": "Phakomatoses",
        "question_type": "clinical_vignette",
        "stem": "A 9-year-old boy with a history of infantile spasms and cognitive impairment presents with severe refractory morning vomiting and lethargy. Physical examination demonstrates multiple hypomelanotic ash-leaf macules and facial angiofibromas. Neuroimaging reveals an avidly enhancing 2.5-cm intraventricular mass at the foramen of Monro causing acute bilateral lateral ventriculomegaly. Targeted medical therapy that directly inhibits which enzymatic complex has proven efficacy in shrinking this specific tumor?",
        "options": [
            {"label": "A", "text": "Mammalian target of rapamycin complex 1 mTORC1 serine/threonine kinase", "is_correct": True},
            {"label": "B", "text": "Epidermal growth factor receptor tyrosine kinase intracellular domain", "is_correct": False},
            {"label": "C", "text": "Anaplastic lymphoma kinase ALK catalytic fusion oncoprotein", "is_correct": False},
            {"label": "D", "text": "Cyclin-dependent kinases 4 and 6 regulating the G1-S checkpoint", "is_correct": False},
            {"label": "E", "text": "Poly ADP-ribose polymerase 1 mediating single-strand DNA base repair", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "This patient with tuberous sclerosis has developed a subependymal giant cell astrocytoma (SEGA) at the foramen of Monro, causing non-communicating hydrocephalus. Tuberous sclerosis results from mutations in TSC1 (hamartin) or TSC2 (tuberin), which normally form a complex that inhibits Rheb GTPase. Loss of this complex leads to constitutive Rheb-mediated activation of mTORC1. The mTOR inhibitors everolimus and sirolimus directly inhibit mTORC1, reducing SEGA volume and preventing hydrocephalus.",
        "high_yield_takeaway": "Tuberous sclerosis causes mTOR hyperactivation; SEGA at the foramen of Monro can be treated medically with mTOR inhibitors (everolimus/sirolimus)."
    },
    {
        "id": "exam3_g_h_u3_q12",
        "category": "Unit 03: Tumors",
        "subcategory": "Phakomatoses",
        "question_type": "clinical_vignette",
        "stem": "A newborn infant is found to have a harsh holosystolic murmur and multiple well-circumscribed echogenic masses within the ventricular myocardium on echocardiography, consistent with cardiac rhabdomyomas. Wood's lamp examination discloses several hypomelanotic macules across the torso. What is the typical clinical course of these cardiac masses, and what life-threatening renal complication is this child at risk for developing in young adulthood?",
        "options": [
            {"label": "A", "text": "Spontaneous rhabdomyoma regression; severe retroperitoneal bleed from angiomyolipoma", "is_correct": True},
            {"label": "B", "text": "Rapid malignant sarcomatous degeneration; bilateral clear cell renal carcinomas", "is_correct": False},
            {"label": "C", "text": "Progression to fatal dilated cardiomyopathy; diffuse renal medullary amyloidosis", "is_correct": False},
            {"label": "D", "text": "Metastasis to regional thoracic nodes; end-stage renal medullary cystic disease", "is_correct": False},
            {"label": "E", "text": "Calcific aortic stenosis by age five; recurrent staghorn calculus formation", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "Cardiac rhabdomyomas are benign hamartomas strongly associated with tuberous sclerosis (>50% have TSC). Remarkably, most cardiac rhabdomyomas spontaneously regress during childhood as cardiomyocytes mature. However, TSC patients are at high lifetime risk for bilateral renal angiomyolipomas (composed of blood vessels, smooth muscle, and adipose tissue), which are prone to aneurysmal rupture and massive retroperitoneal hemorrhage.",
        "high_yield_takeaway": "Cardiac rhabdomyomas in tuberous sclerosis typically undergo spontaneous regression; renal angiomyolipomas can cause catastrophic retroperitoneal bleeding."
    },
    {
        "id": "exam3_g_h_u3_q13",
        "category": "Unit 03: Tumors",
        "subcategory": "Phakomatoses",
        "question_type": "clinical_vignette",
        "stem": "A 2-year-old child presents with intractable focal seizures. Examination reveals a unilateral facial port-wine stain (nevus flammeus) strictly demarcating the ophthalmic division of the trigeminal nerve. Non-contrast head CT demonstrates prominent ipsilateral parieto-occipital cortical 'tram-track' gyriform calcifications and underlying cerebral atrophy. What genetic mechanism explains the spontaneous, non-familial occurrence of this disorder?",
        "options": [
            {"label": "A", "text": "Postzygotic somatic mosaic gain-of-function mutation in the GNAQ gene", "is_correct": True},
            {"label": "B", "text": "Maternal uniparental disomy involving chromosome 15 imprinted alleles", "is_correct": False},
            {"label": "C", "text": "Germline trinucleotide repeat expansion showing maternal anticipation", "is_correct": False},
            {"label": "D", "text": "Autosomal dominant deletion of the proximal p-arm of chromosome 3", "is_correct": False},
            {"label": "E", "text": "Mitochondrial DNA point mutation exhibiting variable tissue heteroplasmy", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "Sturge-Weber syndrome (encephalotrigeminal angiomatosis) is not inherited; it is caused by an activating postzygotic somatic mosaic mutation in the GNAQ gene (encoding G-alpha-q). Because the mutation occurs postzygotically in embryonic progenitor cells, it affects only a mosaic subset of cells forming capillary venules in the V1 trigeminal distribution, ipsilateral leptomeninges (leptomeningeal angioma leading to hypoperfusion, seizures, and 'tram-track' cortical calcification), and anterior eye (glaucoma).",
        "high_yield_takeaway": "Sturge-Weber syndrome is caused by a somatic mosaic GNAQ mutation, causing a V1 port-wine stain, leptomeningeal angiomas, seizures, and tram-track calcifications."
    },
    {
        "id": "exam3_g_h_u3_q14",
        "category": "Unit 03: Tumors",
        "subcategory": "CNS Lymphoma",
        "question_type": "clinical_vignette",
        "stem": "A 36-year-old HIV-infected man with a CD4 count of 28/uL presents with progressive confusion and right-sided hemiparesis. Brain MRI reveals a solitary 3.8-cm periventricular rim-enhancing lesion with extensive surrounding edema. CSF testing is strongly positive for Epstein-Barr virus DNA by PCR. Empiric antitoxoplasmosis therapy produces no reduction in lesion volume after two weeks. Stereotactic biopsy is performed. Which histopathologic finding is most likely to be observed?",
        "options": [
            {"label": "A", "text": "Dense angiocentric infiltrates of atypical B-lymphocytes expressing CD20", "is_correct": True},
            {"label": "B", "text": "Encapsulated yeasts with mucopolysaccharide capsules clearing on mucicarmine", "is_correct": False},
            {"label": "C", "text": "Intracellular pseudocysts containing crescents of Toxoplasma gondii bradyzoites", "is_correct": False},
            {"label": "D", "text": "Extensive demyelination with oligodendrocytes containing glassy inclusions", "is_correct": False},
            {"label": "E", "text": "Large syncytial cells with multiple eosinophilic intranuclear inclusions", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "Primary central nervous system lymphoma (PCNSL) is an aggressive diffuse large B-cell lymphoma (DLBCL, CD20+) strongly linked to Epstein-Barr virus (EBV) in severely immunocompromised patients (HIV CD4 < 50/uL). PCNSL characteristically presents as a solitary periventricular ring-enhancing mass (unlike toxoplasmosis, which is typically multiple and responds to pyrimethamine/sulfadiazine). Detection of EBV DNA in CSF has high specificity for PCNSL.",
        "high_yield_takeaway": "In HIV patients with CD4 < 50, a solitary periventricular ring-enhancing lesion with CSF EBV DNA is primary CNS lymphoma (CD20+ DLBCL)."
    },
    {
        "id": "exam3_g_h_u3_q15",
        "category": "Unit 03: Tumors",
        "subcategory": "Pediatric Ventricular Tumors",
        "question_type": "clinical_vignette",
        "stem": "A 5-year-old boy presents with progressive morning headaches, vomiting, and secondary torticollis. Brain MRI reveals an expansile mass arising from the floor of the fourth ventricle that extends out into the cerebellomedullary cistern through the foramina of Luschka. Biopsy demonstrates tumor cells arrayed in perivascular pseudorosettes with intracytoplasmic blepharoplasts (basal ciliary bodies). What is the primary route of metastatic dissemination characteristic of this neoplasm?",
        "options": [
            {"label": "A", "text": "Cerebrospinal fluid seeding along the craniospinal leptomeningeal subarachnoid space", "is_correct": True},
            {"label": "B", "text": "Hematogenous spread via the retroperitoneal Batson vertebral venous plexus", "is_correct": False},
            {"label": "C", "text": "Lymphatic drainage into the deep superior internal jugular cervical lymph nodes", "is_correct": False},
            {"label": "D", "text": "Transdural invasion across the tentorium into the posterior sagittal sinus", "is_correct": False},
            {"label": "E", "text": "Direct retrobulbar extension along the perineural sheaths of the optic nerve", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "Ependymomas arise from ependymal cells lining the ventricular system, most commonly the fourth ventricle in children. Histology features perivascular pseudorosettes (tumor cells arranged around blood vessels with fibrillary cuffs) and blepharoplasts. Because of their intraventricular location, they frequently disseminate throughout the subarachnoid space via CSF seeding along the spinal cord.",
        "high_yield_takeaway": "Ependymomas arise in the 4th ventricle in children, show perivascular pseudorosettes and blepharoplasts, and disseminate via CSF pathways."
    },
    {
        "id": "exam3_g_h_u3_q16",
        "category": "Unit 03: Tumors",
        "subcategory": "Sellar Pathology",
        "question_type": "clinical_vignette",
        "stem": "A 31-year-old woman is evaluated for secondary amenorrhea and spontaneous bilateral galactorrhea. Contrast MRI of the sella reveals an 8-mm non-calcified microadenoma within the adenohypophysis, and her serum prolactin is 240 ng/mL (normal <25 ng/mL). She is started on cabergoline therapy. What is the molecular mechanism of action by which this medication causes rapid reduction in prolactin secretion and tumor volume?",
        "options": [
            {"label": "A", "text": "Stimulation of pituitary dopamine D2 receptors coupled to inhibitory G-protein Gi", "is_correct": True},
            {"label": "B", "text": "Competitive antagonism at nuclear estrogen and progesterone receptor complexes", "is_correct": False},
            {"label": "C", "text": "Direct blockade of voltage-gated L-type calcium channels on anterior lactotrophs", "is_correct": False},
            {"label": "D", "text": "Inhibition of somatostatin receptor subtype 2 on hypothalamic releasing cells", "is_correct": False},
            {"label": "E", "text": "Antagonism of prolactin releasing hormone receptors within the hypophyseal portal", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "Prolactinomas are benign lactotroph adenomas of the anterior pituitary. Dopamine (prolactin-inhibiting factor) released by the hypothalamus normally inhibits prolactin synthesis and secretion via dopamine D2 receptors coupled to Gi proteins (adenylyl cyclase inhibition). Cabergoline and bromocriptine are potent dopamine D2 receptor agonists that mimic this tonic inhibition, suppressing prolactin secretion and inducing shrinkage of lactotroph tumors.",
        "high_yield_takeaway": "Dopamine D2 receptor agonists (cabergoline, bromocriptine) inhibit prolactin secretion and reduce tumor size in prolactinomas via Gi signaling."
    },
    {
        "id": "exam3_g_h_u3_q17",
        "category": "Unit 03: Tumors",
        "subcategory": "VHL & Surveillance",
        "question_type": "clinical_vignette",
        "stem": "A 29-year-old man successfully undergoes resection of a cerebellar hemangioblastoma. His family pedigree reveals that his father died of bilateral kidney cancer at age 42, and his paternal aunt was treated for a retinal angioma. Genetic testing confirms a pathogenic germline deletion in the VHL tumor suppressor gene. In addition to periodic brain and spinal cord MRI, what annual surveillance modality is critical to detect the most frequent cause of cancer mortality in this syndrome?",
        "options": [
            {"label": "A", "text": "Abdominal MRI or contrast-enhanced ultrasound to screen for renal cell carcinoma", "is_correct": True},
            {"label": "B", "text": "High-resolution chest computed tomography to evaluate for pulmonary hamartomas", "is_correct": False},
            {"label": "C", "text": "Annual colonoscopy beginning at age thirty to resect adenomatous polyps", "is_correct": False},
            {"label": "D", "text": "Serum calcitonin and thyroid ultrasound screening for medullary thyroid cancer", "is_correct": False},
            {"label": "E", "text": "Endoscopic ultrasound to evaluate for diffuse gastric adenocarcinoma", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "Von Hippel-Lindau (VHL) disease is an autosomal dominant condition (deletion on chromosome 3p) that predisposes to cerebellar and retinal hemangioblastomas, clear cell renal cell carcinoma (RCC), pheochromocytomas, and pancreatic neuroendocrine tumors. Renal cell carcinoma is bilateral/multifocal and represents the leading cause of mortality in VHL patients. Annual abdominal imaging (MRI or ultrasound) is recommended starting in early adulthood.",
        "high_yield_takeaway": "VHL syndrome (chromosome 3p) requires regular abdominal surveillance for clear cell renal cell carcinoma (the leading cause of death) and pheochromocytoma."
    },
    {
        "id": "exam3_g_h_u3_q18",
        "category": "Unit 03: Tumors",
        "subcategory": "Adult Gliomas",
        "question_type": "clinical_vignette",
        "stem": "A 65-year-old man presents with progressive left hemiparesis and morning headaches over three weeks. Brain MRI shows a 5-cm irregularly rim-enhancing right frontal mass with extensive central necrosis and significant surrounding vasogenic edema. Biopsy shows dense GFAP immunoreactivity, microvascular proliferation forming glomeruloid vascular tufts, and hypercellular zones of tumor cells pseudopalisading around geographic areas of ischemic necrosis. What is the cell of origin of this malignancy?",
        "options": [
            {"label": "A", "text": "Astrocyte undergoing dedifferentiation driven by oncogenic driver mutations", "is_correct": True},
            {"label": "B", "text": "Oligodendrocyte with secondary loss of chromosome 1p and 19q arms", "is_correct": False},
            {"label": "C", "text": "Arachnoid cap cell invading through the frontal meningeal dura mater", "is_correct": False},
            {"label": "D", "text": "Microglial cell derived from primitive yolk sac myeloid progenitors", "is_correct": False},
            {"label": "E", "text": "Pericyte proliferating within capillary basal lamina of the neocortex", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "Glioblastoma (Grade 4 astrocytoma) arises from astrocytes (or neural stem cell progenitors acquiring astrocytic differentiation), as demonstrated by intense immunohistochemical staining for glial fibrillary acidic protein (GFAP). The diagnostic hallmarks are pseudopalisading necrosis and microvascular (endothelial) proliferation.",
        "high_yield_takeaway": "Glioblastoma originates from astrocytes, stains positive for GFAP, and is characterized by pseudopalisading necrosis and glomeruloid microvascular proliferation."
    },
    {
        "id": "exam3_g_h_u3_q19",
        "category": "Unit 03: Tumors",
        "subcategory": "Nerve Sheath Tumors",
        "question_type": "clinical_vignette",
        "stem": "A 44-year-old man presents with a slow-growing, painful mass in his left posterior thigh along the trajectory of the sciatic nerve. During surgical excision, the surgeon notes that the mass is well-circumscribed, encapsulated, and lies eccentric to the main nerve trunk, allowing complete enucleation without sacrificing functional nerve fascicles. Histopathology reveals alternating Antoni A and B areas with intense S100 positivity. What surgical and pathological feature fundamentally distinguishes this tumor from a localized neurofibroma?",
        "options": [
            {"label": "A", "text": "True fibrous encapsulation and eccentric displacement of intact nerve fascicles", "is_correct": True},
            {"label": "B", "text": "Absence of S100 immunoreactivity within neoplastic supporting stromal cells", "is_correct": False},
            {"label": "C", "text": "Diffuse infiltrative entrapment of nerve fibers necessitating complete transection", "is_correct": False},
            {"label": "D", "text": "Origin from central oligodendrocytes rather than peripheral neural crest cells", "is_correct": False},
            {"label": "E", "text": "High malignant transformation rate exceeding fifty percent during adulthood", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "Schwannomas are true encapsulated tumors that grow eccentrically from a single nerve fascicle, pushing the remaining nerve fibers aside without infiltrating them; thus, they can usually be resected while sparing the nerve trunk. In contrast, neurofibromas lack a capsule, infiltrate and entangle multiple nerve fascicles directly (making nerve-sparing resection impossible), and have a higher risk of malignant transformation (especially in plexiform neurofibromas in NF1).",
        "high_yield_takeaway": "Schwannomas are encapsulated and grow eccentrically from a nerve without fascicular infiltration, allowing nerve-sparing surgical enucleation."
    },
    {
        "id": "exam3_g_h_u3_q20",
        "category": "Unit 03: Tumors",
        "subcategory": "Pineal Region Tumors",
        "question_type": "clinical_vignette",
        "stem": "A 14-year-old boy presents with progressive morning headaches, vomiting, upward gaze paralysis, convergence-retraction nystagmus on attempted upward gaze, and bilateral pupillary light-near dissociation (pupils constrict to accommodation but do not react to direct light). Brain MRI reveals a 2.5-cm mass in the pineal gland compressing the dorsal midbrain. What specific anatomical structure compression produces this constellation of neuro-ophthalmic findings (Parinaud syndrome)?",
        "options": [
            {"label": "A", "text": "Midbrain tectum including superior colliculi and pretectal nuclei", "is_correct": True},
            {"label": "B", "text": "Ventral tegmentum including oculomotor nerve roots in the interpeduncular fossa", "is_correct": False},
            {"label": "C", "text": "Abducens nucleus within the facial colliculus of the dorsal pontine floor", "is_correct": False},
            {"label": "D", "text": "Lateral geniculate body within the posterior inferior thalamic complex", "is_correct": False},
            {"label": "E", "text": "Medial longitudinal fasciculus traversing the paramedian midbrain core", "is_correct": False}
        ],
        "correct_idx": 0,
        "explanation": "Parinaud syndrome (dorsal midbrain syndrome) is caused by compression of the midbrain tectum (specifically the pretectal area and superior colliculi), most commonly by a pineal region tumor (germinoma or pineocytoma/pineoblastoma) or obstructive hydrocephalus. Features include upward gaze palsy (compression of vertical gaze center in rostral interstitial nucleus of MLF/pretectal area), convergence-retraction nystagmus, light-near dissociation, and bilateral eyelid retraction (Collier sign).",
        "high_yield_takeaway": "Parinaud syndrome results from pineal mass compression of the dorsal midbrain tectum (pretectal area and superior colliculi), causing upward gaze palsy and light-near dissociation."
    }
]

if __name__ == "__main__":
    for q in u3_questions:
        check_q(q)
    print("gen_g_h_u3.py: All 20 questions passed validation!")
