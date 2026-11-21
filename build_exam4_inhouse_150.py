import re
import json
import os

source_path = '/Users/markyoussef_1/Downloads/IMC535_E4_Practice_Questions.md'
output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'exam4_inhouse_150_questions.json')

with open(source_path, 'r', encoding='utf-8') as f:
    text = f.read()

part_titles = [
    'Part 1: Mental Status Exam',
    'Part 2: Schizophrenia Spectrum',
    'Part 3: Psychosis Workup & Early Intervention',
    'Part 4: Antipsychotic Medications',
    'Part 5: Substance Use Disorders'
]

parts_raw = [p for p in re.split(r'\n(?=# Part \d+:)', text) if p.strip().startswith('# Part ')]

# Option leveling overrides for questions where correct answer was an obvious giveaway
# (Key: (part_num, local_q_num) -> dict of leveled option texts)
LEVELING_OVERRIDES = {
    # Part 1: Mental Status Exam
    (1, 2): {
        'A': 'The MSE is a comprehensive neuropsychological cognitive assessment',
        'B': 'The MoCA primarily assesses mood state, affect, and thought content',
        'C': 'The MSE broadly assesses signs of mental illness; cognition is only one section and not a thorough test',
        'D': 'They are clinically interchangeable screening tools for psychiatric pathology'
    },
    (1, 4): {
        'A': 'The patient\'s internal emotional state, as stated by the patient',
        'B': 'A fixed, false belief firmly held despite contrary evidence',
        'C': 'The clinical decision a patient demonstrates in real-life scenarios',
        'D': 'The external, observable manifestation of the patient\'s emotional state'
    },
    (1, 13): {
        'A': 'Flight of ideas (rapid topic jumps with loose but discernable links)',
        'B': 'Circumstantiality (over-detailed speech that eventually reaches the goal)',
        'C': 'Echolalia (senseless repetition of words spoken by another person)',
        'D': 'Loosening of associations (fluent speech with no connecting conceptual thread)'
    },

    # Part 2: Schizophrenia Spectrum
    (2, 2): {
        'A': 'Avolition, alogia, anhedonia, or blunted emotional expression',
        'B': 'Auditory, command, or persecutory perceptual hallucinations',
        'C': 'Disorganized, tangential, or derailed cognitive speech patterns',
        'D': 'Delusions of reference, control, or persecutory paranoia'
    },
    (2, 5): {
        'A': 'Persecutory and somatic delusions',
        'B': 'Auditory and commanding hallucinations',
        'C': 'Negative and cognitive symptom domains',
        'D': 'Disorganized and circumstantial speech'
    },
    (2, 6): {
        'A': 'A disorganized motor syndrome with markedly decreased environmental reactivity or excessive purposeless motor activity',
        'B': 'A delayed hyperkinetic syndrome with involuntary choreiform movements of the face and extremities following D2 blockade',
        'C': 'A encapsulated delusional disorder characterized by fixed non-bizarre beliefs with preserved functional independence',
        'D': 'An affective mood syndrome marked by rapid cycling between euphoric grandiosity and severe unipolar depression'
    },
    (2, 8): {
        'A': 'Females have earlier onset in early adolescence; males develop symptoms in mid-adulthood',
        'B': 'Males typically develop onset in late teens to early 20s; females in mid-20s to early 30s',
        'C': 'Both biological sexes exhibit identical peak incidence after the fourth decade of life',
        'D': 'Both biological sexes develop primary manifestations during early childhood development'
    },
    (2, 23): {
        'A': 'Presence of at least 1 Criterion A symptom for at least 1 week with acute behavioral decline',
        'B': 'Presence of at least 2 psychotic symptoms for 2 weeks occurring exclusively during mood episodes',
        'C': 'Presence of a single encapsulated delusion for 1 month with intact social and occupational functioning',
        'D': 'Presence of ≥2 Criterion A symptoms for ≥1 month, ≥6 months total disturbance, and functional decline'
    },
    (2, 24): {
        'A': 'Presence of ≥1 delusion for ≥1 month, without prominent hallucinations, and functioning relatively preserved',
        'B': 'Presence of pervasive delusions accompanied by prominent negative symptoms and severe cognitive functional decline',
        'C': 'Presence of mood-congruent delusions occurring exclusively during acute euphoric manic or depressive episodes',
        'D': 'Presence of polymorphic psychotic symptoms with sudden acute onset and complete resolution in under 1 month'
    },
    (2, 25): {
        'A': 'Presence of prominent catatonic stupor, waxy flexibility, or posturing during acute illness',
        'B': 'Presence of ≥2 weeks of delusions or hallucinations in the absence of a major mood episode',
        'C': 'Onset of initial psychotic symptoms occurring predominantly after the fourth decade of life',
        'D': 'Presence of pervasive primary negative symptoms including avolition, alogia, and asociality'
    },
    (2, 26): {
        'A': 'Schizoaffective disorder, bipolar type',
        'B': 'Schizophrenia with secondary mood symptoms',
        'C': 'Bipolar I disorder with psychotic features',
        'D': 'Brief psychotic disorder with affective features'
    },
    (2, 28): {
        'A': 'Dopamine D2 and D3 receptor partial agonist',
        'B': 'Dual muscarinic M1/M4 receptor agonist agent',
        'C': 'Potent selective serotonin 5-HT2A receptor antagonist',
        'D': 'Presynaptic vesicular monoamine transporter 2 inhibitor'
    },
    (2, 29): {
        'A': 'Reducing high expressed emotion such as familial criticism, hostility, and over-involvement',
        'B': 'Increasing direct parental criticism and structured confrontation to motivate social engagement',
        'C': 'Limiting family contact entirely by transferring long-term care to residential institutions',
        'D': 'Eliminating maintenance pharmacotherapy in favor of exclusive home-based behavioral reinforcement'
    },

    # Part 3: Psychosis Differential Diagnosis & Workup
    (3, 1): {
        'A': 'Perceptual hallucinations and encapsulated somatic delusions exclusively',
        'B': 'Hallucinations, delusions, disorganized speech/behavior, and negative symptoms',
        'C': 'Expansive mood elevation, pressured speech, and grandiose delusions exclusively',
        'D': 'Severe somatic anxiety, autonomic arousal, and acute panic-related derealization'
    },
    (3, 2): {
        'A': 'Schizophrenia meeting full DSM-5 criteria with secondary negative symptoms',
        'B': 'Schizophreniform disorder with good prognostic features and acute onset',
        'C': 'Brief psychotic disorder with marked stressors and transient impairment',
        'D': 'Subthreshold perceptual experience not meeting criteria for a psychotic disorder'
    },
    (3, 3): {
        'A': 'Hypnagogic hallucinations, representing a benign physiologic sleep-wake transition phenomenon',
        'B': 'Hypnopompic hallucinations, representing an early prodromal manifestation of schizophrenia',
        'C': 'True psychotic command auditory hallucinations warranting immediate second-generation antipsychotic therapy',
        'D': 'Dissociative perceptual flashbacks secondary to acute psychological post-traumatic stress'
    },
    (3, 4): {
        'A': 'Immediately initiate high-potency oral second-generation antipsychotics',
        'B': 'Admit to an acute inpatient psychiatric unit under involuntary commitment',
        'C': 'Recognize that spiritual communion may be culturally or developmentally normative',
        'D': 'Order emergent brain MRI with and without contrast and lumbar puncture'
    },
    (3, 6): {
        'A': 'Selective serotonin reuptake inhibitors, beta-blockers, and calcium channel antagonists',
        'B': 'Second-generation atypical antipsychotics, mood stabilizers, and low-dose benzodiazepines',
        'C': 'Broad-spectrum penicillins, oral hypoglycemic agents, and proton pump inhibitors',
        'D': 'Systemic corticosteroids, dopamine agonists, anticholinergics, and stimulant medications'
    },
    (3, 8): {
        'A': 'Onset before puberty strongly indicates an underlying sporadic monogenic mitochondrial disorder',
        'B': 'Onset in the third decade of life requires mandatory serial lumbar punctures and heavy metal screening',
        'C': 'Onset after age 40 significantly raises clinical suspicion for secondary medical or neurologic etiologies',
        'D': 'Onset in late adolescence is pathognomonic for paraneoplastic anti-NMDA receptor encephalitis'
    },
    (3, 9): {
        'A': 'Auditory command hallucinations running commentary',
        'B': 'Third-person auditory voices conversing with each other',
        'C': 'Echo de la pensée (audible thought echo phenomena)',
        'D': 'Visual, olfactory, gustatory, or tactile hallucinations'
    },
    (3, 10): {
        'A': 'Early-onset behavioral variant frontotemporal lobar degeneration',
        'B': 'Anti-N-methyl-D-aspartate (anti-NMDA) receptor autoimmune encephalitis',
        'C': 'Acute uncal herniation secondary to rupture of an anterior communicating aneurysm',
        'D': 'Sporadic Creutzfeldt-Jakob disease with rapidly progressive spongiform encephalopathy'
    },
    (3, 11): {
        'A': 'Serum and cerebrospinal fluid autoimmune encephalopathy antibody panels',
        'B': 'Serum ceruloplasmin levels and 24-hour quantitative urinary copper excretion',
        'C': 'Serum rapid plasma reagin (RPR) titer and treponemal fluorescent antibody testing',
        'D': 'Serial quantitative urine heavy metal screens for lead, arsenic, and mercury'
    },
    (3, 12): {
        'A': 'Insidious progressive cognitive decline evolving silently over multiple consecutive years',
        'B': 'Static focal sensorimotor neurologic deficits with intact attentional concentration',
        'C': 'Acute onset evolving over hours to days with fluctuating course and sleep-wake disturbance',
        'D': 'Episodic behavioral disinhibition occurring exclusively during daytime waking hours'
    },
    (3, 13): {
        'A': 'Intact attentional focus with preserved serial subtraction and spelling capabilities',
        'B': 'Impaired attention and concentration with a waxing and waning level of consciousness',
        'C': 'Hyper-focused concentration accompanied by accelerated, logical linear thought processing',
        'D': 'Isolated executive dysfunction with fully preserved situational awareness and orientation'
    },
    (3, 17): {
        'A': 'Serum lead, arsenic, cadmium, and quantitative urinary porphyria profile',
        'B': 'CBC, CMP, TSH/free T4, urine drug screen, B12/folate, RPR, and HIV testing',
        'C': 'Positron emission tomography (PET) scan and full-genome exome sequencing',
        'D': 'Polysomnography sleep study, serial EEG telemetry, and cerebral angiography'
    },
    (3, 18): {
        'A': 'Serum ceruloplasmin and 24-hour urinary copper excretion testing',
        'B': 'Serum and cerebrospinal fluid paraneoplastic antineuronal antibody panels',
        'C': 'Serum copper, zinc, magnesium, and red blood cell thiamine pyrophosphate',
        'D': 'Serum thyroid-stimulating hormone, free T4, and anti-thyroid peroxidase antibodies'
    },
    (3, 20): {
        'A': 'Serum rapid plasma reagin and cerebrospinal fluid VDRL antibody testing',
        'B': 'Serum anti-nuclear antibodies (ANA) and anti-double-stranded DNA titers',
        'C': 'Serum ceruloplasmin concentration and 24-hour quantitative urinary copper',
        'D': 'Serum and urine porphobilinogen and delta-aminolevulinic acid levels'
    },
    (3, 24): {
        'A': 'Serum anti-voltage-gated potassium channel complex and contactin-associated protein',
        'B': 'Serial non-contrast head CT and 24-hour ambulatory blood pressure monitoring',
        'C': '24-hour urinary free cortisol or late-night salivary cortisol and pituitary/adrenal MRI',
        'D': 'Fasting blood glucose, hemoglobin A1c, and oral glucose tolerance challenge test'
    },
    (3, 25): {
        'A': 'Patient displays chronic auditory hallucinations without any new focal findings',
        'B': 'Presence of fever, nuchal rigidity, or clinical concern for autoimmune encephalitis',
        'C': 'Patient presents with classic adolescent onset of gradual social withdrawal and alogia',
        'D': 'Patient reports transient paranoia following recreational cannabis consumption'
    },
    (3, 27): {
        'A': 'Weekly attenuated positive symptoms in past month, beginning or worsening in past year',
        'B': 'Continuous unremitting auditory hallucinations lasting greater than 6 consecutive months',
        'C': 'Isolated family history of bipolar disorder without any subjective cognitive or perceptual changes',
        'D': 'Acute polymorphic delirium accompanied by prominent fluctuating level of consciousness'
    },
    (3, 28): {
        'A': 'Diagnosis of panic disorder with secondary situational agoraphobic avoidance',
        'B': 'Family history of unipolar depression with preserved full-time employment status',
        'C': 'First-degree relative with psychosis plus ≥30% drop in Global Assessment of Functioning',
        'D': 'Presence of prominent substance use disorder without any baseline genetic psychiatric risk'
    },
    (3, 29): {
        'A': 'Immediate high-dose first-generation neuroleptic pharmacotherapy and long-term institutionalization',
        'B': 'Cognitive behavioral therapy, family-focused education, supported schooling, and clinical monitoring',
        'C': 'Elective electroconvulsive therapy (ECT) and mandatory permanent academic withdrawal',
        'D': 'Exclusive observation without clinical monitoring until frank psychotic decompensation occurs'
    },
    (3, 30): {
        'A': 'The duration of prodromal social isolation prior to the development of subthreshold symptoms',
        'B': 'The total lifetime duration of continuous antipsychotic pharmacotherapy maintenance',
        'C': 'The time interval between the initial psychiatric clinic intake and definitive psychological testing',
        'D': 'The time interval from onset of frank psychotic symptoms to initiation of adequate treatment'
    },

    # Part 4: Antipsychotic Medications
    (4, 1): {
        'A': 'Postsynaptic dopamine D2 receptor antagonism across central dopaminergic pathways',
        'B': 'Selective serotonin 5-HT1A receptor agonism within the dorsal raphe nuclei',
        'C': 'Gamma-aminobutyric acid type A (GABA-A) positive allosteric receptor modulation',
        'D': 'Pre-synaptic vesicular monoamine transporter 2 (VMAT2) selective inhibition'
    },
    (4, 3): {
        'A': '5-HT2A blockade diminishes acetylcholine synthesis in the striatal cholinergic interneurons',
        'B': '5-HT2A blockade disinhibits dopamine release in the nigrostriatal pathway, reducing EPS risk',
        'C': '5-HT2A blockade directly upregulates D2 receptor density within the tuberoinfundibular tract',
        'D': '5-HT2A blockade prevents peripheral conversion of levodopa to circulating dopamine'
    },
    (4, 4): {
        'A': 'Equipotent D2 antagonism with identical metabolic, sedation, and EPS risk profiles',
        'B': 'Weaker central D2 antagonism, minimal risk of EPS, but marked metabolic weight gain',
        'C': 'Selective muscarinic M1 receptor agonism without any significant dopaminergic affinity',
        'D': 'Potent central D2 antagonism, higher EPS and NMS risk, and lower metabolic/sedative effects'
    },
    (4, 6): {
        'A': 'Alpha-1 adrenergic blockade causing dry mucous membranes and reflex hypertension',
        'B': 'Histamine H1 receptor blockade causing profound weight loss and central insomnia',
        'C': 'Muscarinic M1 receptor blockade causing dry mouth, constipation, urinary retention, and blurred vision',
        'D': 'Dopamine D2 receptor blockade causing excessive salivation, diarrhea, and miosis'
    },
    (4, 7): {
        'A': 'Producing marked rapid improvement in both executive processing and affective blunting',
        'B': 'Failing to improve or potentially worsening negative symptoms via mesocortical D2 blockade',
        'C': 'Inducing permanent resolution of cognitive deficits through mesolimbic D2 receptor upregulation',
        'D': 'Selectively enhancing prefrontal dopamine tone without altering subcortical transmission'
    },
    (4, 15): {
        'A': 'Acute nigrostriatal dopamine D2 receptor hypoactivity following drug discontinuation',
        'B': 'Striatal cholinergic depletion resulting from excessive muscarinic M1 receptor stimulation',
        'C': 'Dopamine D2 receptor upregulation and supersensitivity following prolonged chronic receptor blockade',
        'D': 'Autoimmune degradation of peripheral acetylcholine receptors at the neuromuscular junction'
    },
    (4, 16): {
        'A': 'Immediate dose escalation of the offending high-potency first-generation antipsychotic',
        'B': 'Oral anticholinergic agents such as benztropine or diphenhydramine (which worsen TD)',
        'C': 'Dopamine receptor agonists such as pramipexole, ropinirole, or bromocriptine',
        'D': 'Vesicular monoamine transporter 2 (VMAT2) inhibitors such as valbenazine or deutetrabenazine'
    },
    (4, 17): {
        'A': 'D2 receptor stimulation within the pituitary stalk triggers excessive prolactin gene transcription',
        'B': 'D2 receptor antagonism within the tuberoinfundibular tract removes tonic dopamine inhibition of prolactin',
        'C': 'Alpha-1 receptor antagonism within the hypothalamic nuclei stimulates growth hormone release',
        'D': 'Histamine H1 receptor blockade in the anterior pituitary directly releases stored gonadotropins'
    },
    (4, 18): {
        'A': 'Galactorrhea, secondary amenorrhea, and diminished sexual libido',
        'B': 'Acute hirsutism, central adiposity, and purple abdominal striae',
        'C': 'Severe polyuria, polydipsia, and fluctuating hypernatremia',
        'D': 'Hot flashes, severe menorrhagia, and accelerated osteoporosis'
    },
    (4, 19): {
        'A': 'Accelerated male-pattern baldness and testicular hypertrophy',
        'B': 'Severe priapism, polycythemia, and peripheral vasodilation',
        'C': 'Gynecomastia, erectile dysfunction, and decreased sexual libido',
        'D': 'Excessive muscular hypertrophy, acne vulgaris, and vocal deepening'
    },
    (4, 20): {
        'A': 'Hypothermia, flaccid paralysis, pinpoint pupils, and respiratory depression',
        'B': 'Severe choreoathetosis, hyperreflexia, ocular clonus, and profuse diarrhea',
        'C': 'Intermittent resting tremor, normal temperature, and selective facial grimacing',
        'D': 'Hyperthermia, altered mental status, lead-pipe rigidity, and autonomic instability'
    },
    (4, 21): {
        'A': 'Markedly decreased serum creatine kinase, leukopenia, and acute hypoglycemia',
        'B': 'Markedly elevated creatine kinase, leukocytosis, elevated transaminases, and hyperkalemia',
        'C': 'Profound thrombocytopenia, isolated hypercalcemia, and acute hypophosphatemia',
        'D': 'Normal serum biomarkers with isolated respiratory alkalosis on arterial blood gas'
    },
    (4, 23): {
        'A': 'Intravenous flumazenil infusion accompanied by high-dose oral benztropine',
        'B': 'Aggressive therapeutic hypothermia without discontinuing the offending antipsychotic',
        'C': 'Immediate drug cessation, supportive cooling, and dantrolene or bromocriptine therapy',
        'D': 'High-dose intravenous naloxone combined with central beta-adrenergic blockade'
    },
    (4, 26): {
        'A': 'Ziprasidone and aripiprazole convey the highest risk; olanzapine conveys the lowest',
        'B': 'Olanzapine and clozapine convey the highest risk; ziprasidone and aripiprazole convey lower risk',
        'C': 'All second-generation atypical antipsychotics exhibit completely identical metabolic liability',
        'D': 'First-generation high-potency antipsychotics produce substantially greater weight gain than atypicals'
    },
    (4, 28): {
        'A': 'First-line monotherapy for acute adolescent-onset mild schizophreniform disorder',
        'B': 'Maintenance therapy for stable delusional disorder with preserved social functioning',
        'C': 'Adjunctive therapy for uncomplicated major depressive disorder without psychotic features',
        'D': 'Treatment-resistant schizophrenia, where it also significantly reduces suicidal behavior'
    },
    (4, 29): {
        'A': 'Acute renal tubular necrosis requiring weekly urinalysis and creatinine monitoring',
        'B': 'Life-threatening agranulocytosis requiring mandatory absolute neutrophil count (ANC) monitoring',
        'C': 'Fulminant hepatic necrosis requiring serial liver biopsies every two months',
        'D': 'Severe pulmonary interstitial fibrosis requiring baseline and quarterly spirometry'
    },

    # Part 5: Substance Use Disorders
    (5, 1): {
        'A': 'Late age of initial drug experimentation and absence of childhood stressors',
        'B': 'High socioeconomic status and selective access to prescription medications',
        'C': 'Presence of strong familial cohesion and absence of parental substance use',
        'D': 'Young age at first substance use and positive family history of substance dependence'
    },
    (5, 2): {
        'A': 'A chronic medical illness driven by neurochemical, anatomical, and behavioral alterations',
        'B': 'A primary volitional defect reflecting lack of willpower and moral weakness',
        'C': 'A benign lifestyle choice that invariably remits spontaneously without clinical intervention',
        'D': 'An acute transient stress response triggered solely by external environmental adversity'
    },
    (5, 3): {
        'A': 'Nigrostriatal dopaminergic tract (substantia nigra pars compacta to dorsal striatum)',
        'B': 'Tuberoinfundibular dopaminergic tract (arcuate nucleus to hypophyseal portal system)',
        'C': 'Mesocorticolimbic dopaminergic tract (ventral tegmental area to nucleus accumbens and prefrontal cortex)',
        'D': 'Hypothalamic-pituitary-adrenal axis (paraventricular nucleus to anterior pituitary gland)'
    },
    (5, 5): {
        'A': 'Acutely enhances GABAergic inhibition and blocks NMDA; chronically upregulates NMDA receptors',
        'B': 'Acutely inhibits GABAergic tone; chronically downregulates voltage-gated sodium channels',
        'C': 'Acutely stimulates presynaptic dopamine release; chronically depletes vesicular acetylcholine',
        'D': 'Acutely activates mu-opioid receptors; chronically blocks central beta-adrenergic signaling'
    },
    (5, 6): {
        'A': 'Severe pinpoint pupils, shallow respirations, and diminished bowel motility',
        'B': 'Marked bilateral pupillary dilation, acute hyperthermia, and ocular clonus',
        'C': 'Unilateral ptosis, facial anhidrosis, and ipsilateral pupillary constriction',
        'D': 'Normal or sluggish pupils with horizontal gaze nystagmus, ataxia, and slurred speech'
    },
    (5, 7): {
        'A': 'Symptoms begin within 30 minutes; delirium tremens invariably occurs at 6 hours post-cessation',
        'B': 'Withdrawal manifestations occur exclusively between 7 and 14 days following alcohol cessation',
        'C': 'Tremors begin at 6–12 h; seizures at 12–48 h; delirium tremens typically develops at 48–96 h',
        'D': 'Hallucinations precede tremulousness and resolve completely within the first 2 hours'
    },
    (5, 8): {
        'A': 'Immediate physical restraint and observation without administering sedative medications',
        'B': 'Symptom-triggered benzodiazepine administration (e.g., lorazepam or diazepam) guided by CIWA scoring',
        'C': 'High-potency dopamine antagonists such as haloperidol monotherapy to suppress agitation',
        'D': 'Continuous intravenous infusion of flumazenil to prevent secondary receptor down-regulation'
    },
    (5, 9): {
        'A': 'To prevent acute precipitation of Wernicke encephalopathy (administer before or with dextrose)',
        'B': 'To accelerate hepatic clearance of circulating ethanol through alcohol dehydrogenase induction',
        'C': 'To correct refractory hyperkalemia and prevent cardiac dysrhythmias during intoxication',
        'D': 'To reverse acute respiratory depression secondary to sedative-hypnotic co-ingestion'
    },
    (5, 10): {
        'A': 'Mild early-morning finger tremulousness with fully preserved cognitive orientation',
        'B': 'Isolated auditory hallucinations occurring within 6 hours of cessation with normal vital signs',
        'C': 'Single generalized tonic-clonic seizure occurring 24 hours post-cessation without confusion',
        'D': 'Severe delirium, visual hallucinations, marked agitation, and extreme autonomic instability at 48–96 hours'
    },
    (5, 11): {
        'A': 'Outpatient reassurance and scheduled follow-up in primary care within two weeks',
        'B': 'Low-dose oral hydroxyzine monotherapy in a quiet, unmonitored residential setting',
        'C': 'ICU admission, high-dose intravenous benzodiazepine titration, fluid resuscitation, and thiamine repletion',
        'D': 'Emergent hemodialysis combined with competitive opioid receptor antagonist administration'
    },
    (5, 12): {
        'A': 'Irreversibly inhibiting aldehyde dehydrogenase to produce severe aversive facial flushing',
        'B': 'Competitively blocking central mu-opioid receptors to attenuate dopamine-mediated reward and cravings',
        'C': 'Selectively activating prefrontal GABA-B receptors to substitute for alcohol-induced sedation',
        'D': 'Inhibiting monoamine oxidase enzymes to elevate mood and combat depressive symptoms'
    },
    (5, 14): {
        'A': 'Full agonist at central postsynaptic mu and kappa opioid receptor complexes',
        'B': 'Non-competitive antagonist at N-methyl-D-aspartate (NMDA) glutamate receptors',
        'C': 'Direct agonist at serotonergic 5-HT2A receptors responsible for psychedelic experiences',
        'D': 'Partial agonist at cannabinoid CB1 and CB2 receptors, modulating presynaptic neurotransmitter release'
    },
    (5, 15): {
        'A': 'Bilateral pinpoint miosis, hypothermia, bradycardia, and diminished gastrointestinal motility',
        'B': 'Significant anorexia, severe pupillary dilation, horizontal nystagmus, and acute hyperreflexia',
        'C': 'Bilateral conjunctival injection, dry oral mucosa, tachycardia, and increased appetite',
        'D': 'Marked sinus bradycardia, excessive lacrimation, rhinorrhea, and severe abdominal cramping'
    },
    (5, 16): {
        'A': 'Edibles exert instantaneous clinical onset within minutes and dissipate within 1 hour',
        'B': 'Edibles exhibit delayed onset (30 min–3 h) and last up to ~12 h; inhaled onset is rapid (15–30 min) and lasts ~4 h',
        'C': 'Both oral ingestion and smoking exhibit completely identical pharmacokinetic profiles',
        'D': 'Inhaled cannabis requires extensive first-pass hepatic metabolism and outlasts oral ingestion'
    },
    (5, 17): {
        'A': 'Irritability, anxiety, insomnia, and decreased appetite; non-life-threatening without FDA-approved drugs',
        'B': 'Generalized tonic-clonic seizures, severe hyperpyrexia, and delirium tremens requiring ICU care',
        'C': 'Life-threatening autonomic storm, acute hypertensive crisis, and malignant cardiac dysrhythmias',
        'D': 'Severe pupillary constriction, respiratory depression, and profound obtundation'
    },
    (5, 20): {
        'A': 'Rigid four-point physical restraint in a brightly illuminated room without pharmacotherapy',
        'B': 'Low-stimulus calming environment, verbal reassurance, and judicious benzodiazepines or haloperidol',
        'C': 'Immediate high-dose intravenous naloxone boluses followed by continuous infusion',
        'D': 'Intravenous flumazenil administration to reverse competitive receptor antagonism'
    },
    (5, 21): {
        'A': 'Miosis, CNS sedation, shallow respiratory depression, and decreased bowel motility via mu-opioid receptors',
        'B': 'Severe pupillary dilation, marked motor agitation, tachypnea, and hyperactive bowel sounds',
        'C': 'Generalized epileptic seizures, hyperthermia, ocular clonus, and severe diaphoresis',
        'D': 'Severe sinus tachycardia, acute hypertension, paranoia, and tactile formication'
    },
    (5, 22): {
        'A': 'Pinpoint pupillary constriction, deep CNS sedation, and severe hypothermia',
        'B': 'Generalized status epilepticus, severe delirium tremens, and acute hemodynamic collapse',
        'C': 'Lacrimation, rhinorrhea, piloerection, yawning, mydriasis, and hyperactive bowel sounds with diarrhea',
        'D': 'Progressive respiratory depression, pulmonary edema, and acute anoxic encephalopathy'
    },
    (5, 23): {
        'A': 'Intravenous flumazenil titration combined with high-dose loop diuretics',
        'B': 'Intravenous beta-adrenergic antagonist administration to control tachycardia',
        'C': 'Conservative observation without airway intervention in a dark room',
        'D': 'Airway/breathing ventilatory support and immediate administration of the opioid antagonist naloxone'
    },
    (5, 24): {
        'A': 'Both agents are competitive receptor antagonists requiring intensive inpatient detoxification',
        'B': 'Methadone is a full agonist dispensed via clinics; buprenorphine is a partial agonist with ceiling effect; both safe in pregnancy',
        'C': 'Buprenorphine is a full mu agonist carrying higher respiratory risk; methadone is a pure antagonist',
        'D': 'Methadone is strictly contraindicated in pregnant patients; buprenorphine cannot be used for maintenance'
    },
    (5, 25): {
        'A': 'Only after the patient has completed full opioid withdrawal and is confirmed 7–14 days opioid-free',
        'B': 'During the acute height of active withdrawal to accelerate symptom resolution',
        'C': 'Immediately following acute overdose resuscitation without any required washout period',
        'D': 'Concurrently with full mu-opioid agonist maintenance regimens such as high-dose methadone'
    },
    (5, 26): {
        'A': 'Both drug classes directly open voltage-gated sodium channels in cortical pyramidal neurons',
        'B': 'Benzodiazepines increase chloride channel open duration; barbiturates increase opening frequency',
        'C': 'Benzodiazepines increase GABA-A opening frequency; barbiturates increase channel open duration',
        'D': 'Both drug classes act as non-competitive antagonists at central NMDA glutamate receptors'
    },
    (5, 27): {
        'A': 'A benign and self-limiting withdrawal state that requires no active medical supervision',
        'B': 'A mild, transient syndrome characterized by vivid dreams and brief daytime somnolence',
        'C': 'A condition marked by profound central nervous system sedation and respiratory slowing',
        'D': 'A life-threatening withdrawal state (seizures, delirium); requires gradual taper, never abrupt cessation'
    },
    (5, 28): {
        'A': 'Cocaine selectively triggers monoamine vesicular release; amphetamine blocks reuptake transporters',
        'B': 'Cocaine blocks DAT/NET/SERT and Na⁺ channels; amphetamine stimulates monoamine release; MDMA releases 5-HT',
        'C': 'All central stimulants function primarily as direct mu-opioid receptor agonists in the brainstem',
        'D': 'Cocaine acts primarily as an uncompetitive antagonist at glutamate NMDA receptor complexes'
    },
    (5, 29): {
        'A': 'Avoid beta-blockers due to unopposed alpha-1 vasoconstriction; administer benzodiazepines',
        'B': 'Avoid benzodiazepines due to respiratory arrest; administer non-selective beta-blockers',
        'C': 'Avoid intravenous crystalloid fluids and administer high-dose calcium gluconate',
        'D': 'Immediately administer intravenous naloxone and flumazenil as competitive antidotes'
    },
    (5, 30): {
        'A': 'Stimulant withdrawal frequently triggers status epilepticus and life-threatening delirium tremens',
        'B': 'Withdrawal is acutely life-threatening requiring ICU admission; acute intoxication is medically benign',
        'C': 'Withdrawal produces severe dysphoria/suicidality, hypersomnia, and hyperphagia; intoxication can cause paranoid psychosis',
        'D': 'Withdrawal responds rapidly to FDA-approved specific agonist-replacement pharmacotherapy'
    }
}

all_questions = []
global_q_num = 1

for p_idx, part in enumerate(parts_raw):
    cat = part_titles[p_idx]
    split_ans = re.split(r'\n## Part \d+ Answer Key\s*\n', part)
    q_section = split_ans[0]
    ans_section = split_ans[1] if len(split_ans) > 1 else ''
    
    ans_dict = {}
    for line in ans_section.splitlines():
        line = line.strip()
        m = re.match(r'^(\d+)\.\s+\*\*([A-E])\*\*\.?\s*(.*)$', line)
        if m:
            ans_dict[int(m.group(1))] = (m.group(2), m.group(3).strip())
            
    q_blocks = []
    current_block = []
    for line in q_section.splitlines():
        if line.startswith('# Part '): continue
        if re.match(r'^\*{0,2}(\d+)\.\*{0,2}\s*(.*)$', line.strip()):
            if current_block: q_blocks.append(current_block)
            current_block = [line]
        elif current_block: current_block.append(line)
    if current_block: q_blocks.append(current_block)
    
    for q_lines in q_blocks:
        first_line = q_lines[0].strip()
        m_first = re.match(r'^\*{0,2}(\d+)\.\*{0,2}\s*(.*)$', first_line)
        local_num = int(m_first.group(1))
        initial_stem = m_first.group(2)
        
        stem_parts = [initial_stem] if initial_stem else []
        options = []
        
        in_options = False
        for l in q_lines[1:]:
            l_str = l.strip()
            opt_m = re.match(r'^([A-E])\.\s+(.*)$', l_str)
            if opt_m:
                in_options = True
                options.append({'letter': opt_m.group(1), 'text': opt_m.group(2).strip()})
            elif in_options and options:
                options[-1]['text'] += ' ' + l_str
            else:
                if l_str:
                    stem_parts.append(l_str)
                    
        stem = ' '.join(stem_parts).strip()
        ans_info = ans_dict.get(local_num)
        correct_letter, explanation = ans_info
        
        # Apply leveling override if present
        override_key = (p_idx + 1, local_num)
        if override_key in LEVELING_OVERRIDES:
            ov = LEVELING_OVERRIDES[override_key]
            for opt in options:
                if opt['letter'] in ov:
                    opt['text'] = ov[opt['letter']]
                    
        correct_idx = -1
        for idx, opt in enumerate(options):
            if opt['letter'] == correct_letter:
                opt['is_correct'] = True
                correct_idx = idx
            else:
                opt['is_correct'] = False
                
        all_questions.append({
            'id': f'exam4_inhouse_q{global_q_num}',
            'q_num': str(global_q_num),
            'part': p_idx + 1,
            'part_q_num': local_num,
            'stem': stem,
            'category': cat,
            'source': f'IMC 535 Exam 4 Practice ({cat})',
            'options': options,
            'correct_idx': correct_idx,
            'explanation': explanation,
            'high_yield_pearl': explanation,
            'image': None
        })
        global_q_num += 1

print(f'Successfully built {len(all_questions)} questions.')

with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(all_questions, f, indent=2, ensure_ascii=False)

print(f'Saved to {output_path}')
