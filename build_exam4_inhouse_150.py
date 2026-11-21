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

LEVELING_OVERRIDES = {
    # =========================================================================
    # PART 1: MENTAL STATUS EXAM
    # =========================================================================
    (1, 2): {
        'A': 'MSE is a dedicated cognitive battery; MMSE and MoCA assess affective and emotional psychopathology',
        'B': 'MoCA primarily evaluates mood and thought content; MSE evaluates focal motor and cerebellar reflexes',
        'C': 'MSE broadly assesses signs of mental illness; cognition is only one brief screening section tested',
        'D': 'MSE is identical to cognitive screening tools; both instruments assess the exact same mental domains'
    },
    (1, 3): {
        'A': 'The patient\'s predominant internal feeling state, as stated by the patient',
        'B': 'The external, dynamic emotional expression observed objectively by the clinician',
        'C': 'The patient\'s cognitive awareness and intellectual understanding of their illness',
        'D': 'The structural flow, goal-directedness, and organization of the patient\'s thoughts'
    },
    (1, 4): {
        'A': 'The internal emotional feeling state, as described verbally by the patient',
        'B': 'A fixed, false belief firmly held despite contrary reality and evidence',
        'C': 'The real-world decision a patient demonstrates in complex social dilemmas',
        'D': 'The external, observable manifestation of the patient\'s emotional state'
    },
    (1, 5): {
        'A': 'Blunted emotional affect',
        'B': 'Mood-affect incongruence',
        'C': 'Rapid pressured speech',
        'D': 'Tangential thought form'
    },
    (1, 6): {
        'A': 'Labile emotional affect',
        'B': 'Restricted affective range',
        'C': 'Flat or blunted affect',
        'D': 'Exaggerated dramatic affect'
    },
    (1, 7): {
        'A': 'Labile emotional affect',
        'B': 'Fixed emotional affect',
        'C': 'Flat emotional affect',
        'D': 'Congruent emotional affect'
    },
    (1, 8): {
        'A': 'Full-range emotional affect',
        'B': 'Mobile-range emotional affect',
        'C': 'Congruent emotional affect',
        'D': 'Non-reactive emotional affect'
    },
    (1, 9): {
        'A': 'Hyperverbal spontaneous speech',
        'B': 'Pressured un-interruptible speech',
        'C': 'Prosodic monotone emotional speech',
        'D': 'Impoverished telegraphic speech'
    },
    (1, 10): {
        'A': 'Circumstantial thought form',
        'B': 'Tangential thought form',
        'C': 'Flight of ideas thought form',
        'D': 'Word salad thought form'
    },
    (1, 11): {
        'A': 'Circumstantial thought form',
        'B': 'Flight of ideas thought form',
        'C': 'Tangential thought form',
        'D': 'Loose associations thought form'
    },
    (1, 12): {
        'A': 'Loosening of associations',
        'B': 'Flight of rapid ideas',
        'C': 'Clanging associations',
        'D': 'Acute thought blocking'
    },
    (1, 13): {
        'A': 'Flight of ideas (rapid topic jumps with loose but discernable links)',
        'B': 'Circumstantiality (over-detailed speech that eventually reaches the goal)',
        'C': 'Echolalia (senseless repetition of words spoken by another person)',
        'D': 'Loosening of associations (fluent speech with no connecting conceptual thread)'
    },
    (1, 14): {
        'A': 'Word salad (schizophasia)',
        'B': 'Neologisms (coined words)',
        'C': 'Tangentiality (loss of goal)',
        'D': 'Perseveration (repetitive words)'
    },
    (1, 16): {
        'A': 'Echolalia vocalization',
        'B': 'Clanging associations',
        'C': 'Verbal perseveration',
        'D': 'Neologistic invention'
    },
    (1, 17): {
        'A': 'Clanging and echolalic vocalizations',
        'B': 'Perseveration and neologistic speech',
        'C': 'Echolalia and clanging associations',
        'D': 'Neologisms and acute thought blocking'
    },
    (1, 18): {
        'A': 'Acute delirium',
        'B': 'Schizophrenia',
        'C': 'Major depression',
        'D': 'Delusional state'
    },
    (1, 19): {
        'A': 'Abstract reasoning',
        'B': 'Executive judgment',
        'C': 'Sustained attention',
        'D': 'Episodic memory'
    },
    (1, 20): {
        'A': 'A sensory perceptual experience occurring in the absence of any real external stimulus',
        'B': 'A fixed, false belief not culturally shared and unshakeable despite contrary evidence',
        'C': 'An intrusive, unwanted ego-dystonic thought that the patient recognizes as irrational',
        'D': 'An overvalued cognitive preoccupation held with strong emotion without frank psychosis'
    },
    (1, 21): {
        'A': 'A veteran believes the moon is an extraterrestrial satellite monitoring citizens',
        'B': 'A businessman believes federal intelligence agencies have wiretapped his office phone',
        'C': 'A woman believes her apartment neighbors are deliberately contaminating her food supply',
        'D': 'An executive believes corporate competitors are actively conspiring to terminate him'
    },
    (1, 22): {
        'A': 'Persecutory delusion',
        'B': 'Delusion of reference',
        'C': 'Grandiose delusion',
        'D': 'Erotomanic delusion'
    },
    (1, 23): {
        'A': 'Cotard delusion',
        'B': 'Capgras delusion',
        'C': 'Fregoli delusion',
        'D': 'Erotomanic state'
    },
    (1, 24): {
        'A': 'Persecutory delusion',
        'B': 'Delusion of reference',
        'C': 'Somatic delusion',
        'D': 'Erotomanic delusion'
    },
    (1, 25): {
        'A': 'Delusion of reference',
        'B': 'Somatic delusion',
        'C': 'Persecutory delusion',
        'D': 'Grandiose delusion'
    },
    (1, 26): {
        'A': 'Psychosis is a specific categorical DSM-5 diagnosis with defined illness course',
        'B': 'Psychosis is a broad clinical symptom syndrome with diverse underlying etiologies',
        'C': 'Psychosis is exclusively caused by primary idiopathic psychiatric brain disorders',
        'D': 'Psychosis is defined purely by presence of active auditory hallucination phenomena'
    },
    (1, 27): {
        'A': 'Erotomanic delusion (fixed belief)',
        'B': 'Command hallucination (perception)',
        'C': 'Persecutory idea (cultural belief)',
        'D': 'Intrusive obsession (ego-dystonic)'
    },
    (1, 28): {
        'A': 'Perceptual sensory illusion',
        'B': 'Fixed persecutory delusion',
        'C': 'True sensory hallucination',
        'D': 'Derealization phenomenon'
    },
    (1, 29): {
        'A': 'Depersonalization experience',
        'B': 'Derealization phenomenon',
        'C': 'Visual illusion misperception',
        'D': 'Somatosensory dissociation'
    },

    # =========================================================================
    # PART 2: SCHIZOPHRENIA SPECTRUM
    # =========================================================================
    (2, 1): {
        'A': 'Negative symptom domain',
        'B': 'Cognitive symptom domain',
        'C': 'Positive symptom domain',
        'D': 'Affective symptom domain'
    },
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
    (2, 7): {
        'A': 'Resting pill-rolling tremor',
        'B': 'Acute oculogyric crisis',
        'C': 'Choreiform tongue protrusion',
        'D': 'Waxy flexibility and mutism'
    },
    (2, 8): {
        'A': 'Females typically develop onset in early adolescence, while males present in mid-adulthood',
        'B': 'Males typically develop onset in late teens to early 20s, while females present in mid-20s',
        'C': 'Both biological sexes exhibit identical peak incidence after the fourth decade of adult life',
        'D': 'Both biological sexes develop primary clinical manifestations during early childhood years'
    },
    (2, 9): {
        'A': 'Approximately 0.1%',
        'B': 'Approximately 10.0%',
        'C': 'Approximately 1.0%',
        'D': 'Approximately 5.0%'
    },
    (2, 10): {
        'A': 'Approximately 40% to 50%',
        'B': 'Approximately 95% to 100%',
        'C': 'Approximately 5% to 10%',
        'D': 'Approximately 75% to 80%'
    },
    (2, 11): {
        'A': 'Equal to baseline (1× relative risk)',
        'B': 'Moderately elevated (2× relative risk)',
        'C': 'Substantially elevated (5× relative risk)',
        'D': 'Markedly elevated (10× relative risk)'
    },
    (2, 13): {
        'A': 'Advanced paternal age at time of conception',
        'B': 'Advanced maternal age at time of conception',
        'C': 'Very young maternal age during adolescence',
        'D': 'Maternal strictly vegetarian dietary intake'
    },
    (2, 14): {
        'A': 'Maternal prenatal influenza viral infection',
        'B': 'Advanced paternal chronological age at birth',
        'C': 'Perinatal obstetric complications and hypoxia',
        'D': 'Aberrant post-zygotic epigenetic methylation'
    },
    (2, 15): {
        'A': 'Chronic excessive caffeine consumption',
        'B': 'Early adolescent nicotine vaping habits',
        'C': 'Binge alcohol drinking during weekends',
        'D': 'Frequent high-potency cannabis smoking'
    },
    (2, 16): {
        'A': 'Severe maternal in utero famine exposure',
        'B': 'Higher completed educational attainment',
        'C': 'Birth and upbringing in an urban residence',
        'D': 'International migration and minority status'
    },
    (2, 17): {
        'A': '22q11.2 microdeletion syndrome',
        'B': 'Trisomy 21 Down chromosomal syndrome',
        'C': '45,X monosomy Turner dysgenesis syndrome',
        'D': 'FMR1 gene Fragile X mental syndrome'
    },
    (2, 18): {
        'A': 'Mesolimbic and mesocortical tracts',
        'B': 'Mesolimbic and nigrostriatal tracts',
        'C': 'Nigrostriatal and tuberoinfundibular',
        'D': 'Mesocortical and tuberoinfundibular'
    },
    (2, 19): {
        'A': 'Mesolimbic dopaminergic pathway',
        'B': 'Mesocortical dopaminergic pathway',
        'C': 'Nigrostriatal dopaminergic pathway',
        'D': 'Tuberoinfundibular dopamine pathway'
    },
    (2, 20): {
        'A': 'Nigrostriatal dopaminergic pathway',
        'B': 'Mesolimbic dopaminergic pathway',
        'C': 'Tuberoinfundibular dopamine pathway',
        'D': 'Mesocortical dopaminergic pathway'
    },
    (2, 21): {
        'A': 'Schizophreniform disorder',
        'B': 'Brief psychotic disorder',
        'C': 'Primary delusional disorder',
        'D': 'Schizoaffective disorder'
    },
    (2, 22): {
        'A': 'Less than 1 day in total duration',
        'B': '1 day to less than 1 full month',
        'C': '1 month to less than 6 full months',
        'D': 'Greater than 6 continuous months'
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
    (2, 27): {
        'A': 'Brief psychotic disorder',
        'B': 'Undifferentiated schizophrenia',
        'C': 'Primary delusional disorder',
        'D': 'Schizophreniform disorder'
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
    (2, 30): {
        'A': 'Selective serotonin reuptake inhibitors, primarily targeting affective symptoms',
        'B': 'Lithium carbonate monotherapy, primarily targeting neurovegetative sleep symptoms',
        'C': 'Dopamine-blocking antipsychotics, primarily targeting positive psychotic symptoms',
        'D': 'High-potency benzodiazepines, primarily targeting chronic negative social symptoms'
    },

    # =========================================================================
    # PART 3: PSYCHOSIS WORKUP & EARLY INTERVENTION
    # =========================================================================
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
    (3, 5): {
        'A': 'Major depressive disorder with psychotic features',
        'B': 'Bipolar I disorder with manic psychotic features',
        'C': 'Severe obsessive-compulsive disorder with poor insight',
        'D': 'Chronic post-traumatic stress disorder with dissociation'
    },
    (3, 6): {
        'A': 'Selective serotonin reuptake inhibitors, beta-blockers, and calcium channel antagonists',
        'B': 'Second-generation atypical antipsychotics, mood stabilizers, and low-dose benzodiazepines',
        'C': 'Broad-spectrum penicillins, oral hypoglycemic agents, and proton pump inhibitors',
        'D': 'Systemic corticosteroids, dopamine agonists, anticholinergics, and stimulant medications'
    },
    (3, 7): {
        'A': 'Acute delirium confusional state',
        'B': 'Schizoaffective psychotic disorder',
        'C': 'Borderline personality pathology',
        'D': 'Brief situational psychotic episode'
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
        'C': 'Echo de la pensée with audible thought echo phenomena',
        'D': 'Visual, olfactory, gustatory, or tactile hallucinations'
    },
    (3, 10): {
        'A': 'Early-onset behavioral variant frontotemporal lobar brain degeneration',
        'B': 'Autoimmune encephalitis mediated by anti-N-methyl-D-aspartate receptors',
        'C': 'Acute uncal herniation secondary to rupture of an anterior cerebral aneurysm',
        'D': 'Sporadic Creutzfeldt-Jakob disease with rapidly progressive spongiform change'
    },
    (3, 11): {
        'A': 'Serum and cerebrospinal fluid autoimmune encephalopathy antibody panels',
        'B': 'Serum ceruloplasmin levels and 24-hour quantitative urinary copper excretion',
        'C': 'Serum rapid plasma reagin titer and treponemal fluorescent antibody testing',
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
    (3, 15): {
        'A': 'Fleeting, fragmented, and poorly organized',
        'B': 'Fixed, complex, and highly systematized',
        'C': 'Stable, bizarre, and chronic in duration',
        'D': 'Entirely absent across all presentations'
    },
    (3, 16): {
        'A': 'Normal alpha rhythm',
        'B': '3-Hz spike-and-wave',
        'C': 'Generalized slowing',
        'D': 'Periodic sharp waves'
    },
    (3, 17): {
        'A': 'Serum lead, arsenic, cadmium, and quantitative urinary porphyria profile',
        'B': 'CBC, CMP, TSH/free T4, urine drug screen, B12/folate, RPR, and HIV testing',
        'C': 'Positron emission tomography scan and full-genome exome sequencing profile',
        'D': 'Polysomnography sleep study, serial EEG telemetry, and cerebral angiography'
    },
    (3, 18): {
        'A': 'Serum ceruloplasmin and 24-hour urinary copper excretion testing',
        'B': 'Serum and cerebrospinal fluid paraneoplastic antineuronal antibody panels',
        'C': 'Serum copper, zinc, magnesium, and red blood cell thiamine pyrophosphate',
        'D': 'Serum thyroid-stimulating hormone, free T4, and anti-thyroid peroxidase antibodies'
    },
    (3, 19): {
        'A': 'Rapid plasma reagin and FTA-ABS testing',
        'B': 'Blood lead and heavy metal screening',
        'C': 'Epstein-Barr viral capsid antibody titers',
        'D': 'Hemoglobin A1c and fasting blood glucose'
    },
    (3, 20): {
        'A': 'Serum rapid plasma reagin and cerebrospinal fluid VDRL antibody testing',
        'B': 'Serum antinuclear antibodies and anti-double-stranded DNA titers',
        'C': 'Serum ceruloplasmin concentration and 24-hour quantitative urinary copper',
        'D': 'Serum and urine porphobilinogen and delta-aminolevulinic acid levels'
    },
    (3, 21): {
        'A': 'Korsakoff confabulatory psychosis',
        'B': 'Wernicke acute encephalopathy state',
        'C': 'Marchiafava-Bignami demyelination',
        'D': 'Delirium tremens withdrawal state'
    },
    (3, 22): {
        'A': 'Beriberi (thiamine / vitamin B1)',
        'B': 'Scurvy (ascorbate / vitamin C)',
        'C': 'Rickets (calciferol / vitamin D)',
        'D': 'Pellagra (niacin / vitamin B3)'
    },
    (3, 23): {
        'A': 'Pyridoxine deficiency (vitamin B6)',
        'B': 'Thiamine deficiency (vitamin B1)',
        'C': 'Niacin deficiency (vitamin B3)',
        'D': 'Cobalamin deficiency (vitamin B12)'
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
    (3, 26): {
        'A': 'Form, Flow, Frequency, Fullness, and Finality',
        'B': 'Feeling, Fixation, Fluency, Fatigue, and Fear',
        'C': 'Focus, Fulfillment, Flashbacks, Fragility, Fate',
        'D': 'Frequency, Fixity, Fluctuation, Function, Fear'
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
        'C': 'Elective electroconvulsive therapy and mandatory permanent academic withdrawal',
        'D': 'Exclusive observation without clinical monitoring until frank psychotic decompensation occurs'
    },
    (3, 30): {
        'A': 'The duration of prodromal social isolation prior to the development of subthreshold symptoms',
        'B': 'The total lifetime duration of continuous antipsychotic pharmacotherapy maintenance',
        'C': 'The time interval between the initial psychiatric clinic intake and definitive psychological testing',
        'D': 'The time interval from onset of frank psychotic symptoms to initiation of adequate treatment'
    },

    # =========================================================================
    # PART 4: ANTIPSYCHOTIC MEDICATIONS
    # =========================================================================
    (4, 1): {
        'A': 'Postsynaptic dopamine D2 receptor antagonism across central dopaminergic pathways',
        'B': 'Selective serotonin 5-HT1A receptor agonism within the dorsal raphe nuclei',
        'C': 'Gamma-aminobutyric acid type A positive allosteric receptor modulation',
        'D': 'Pre-synaptic vesicular monoamine transporter 2 selective inhibition'
    },
    (4, 2): {
        'A': 'Selective antagonism of serotonin 5-HT2A receptors',
        'B': 'Partial agonism at dopamine D2 and D3 receptors',
        'C': 'Dual antagonism at dopamine D2 and 5-HT2A receptors',
        'D': 'Negative allosteric modulation of GABA-A receptors'
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
    (4, 5): {
        'A': 'Histamine H1, alpha-1 adrenergic, and muscarinic M1',
        'B': 'Hormone receptors, alpha-2 adrenergic, and mu-opioid',
        'C': 'Hydroxytryptamine, acetylcholine, and mesolimbic D2',
        'D': 'Histamine H2, acetylcholinesterase, and mu-opioid'
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
    (4, 8): {
        'A': 'Subjective motor akathisia',
        'B': 'Acute spasmodic dystonia',
        'C': 'Delayed choreic dyskinesia',
        'D': 'Bradykinetic pseudoparkinsonism'
    },
    (4, 9): {
        'A': 'Oral benztropine or trihexyphenidyl',
        'B': 'Oral non-selective propranolol',
        'C': 'Oral valbenazine or deutetrabenazine',
        'D': 'Intravenous dantrolene infusion'
    },
    (4, 10): {
        'A': 'Subjective inner motor restlessness (akathisia)',
        'B': 'Resting tremor and cogwheeling (pseudoparkinsonism)',
        'C': 'Acute painful muscle spasm (acute dystonia)',
        'D': 'Involuntary choreiform movements (tardive dyskinesia)'
    },
    (4, 11): {
        'A': 'Oral propranolol administration',
        'B': 'Intravenous benztropine injection',
        'C': 'Oral valbenazine pharmacotherapy',
        'D': 'Intravenous dantrolene infusion'
    },
    (4, 12): {
        'A': 'Delayed tardive dyskinesia',
        'B': 'Acute euphoric bipolar mania',
        'C': 'Drug-induced pseudoparkinsonism',
        'D': 'Neuroleptic-induced akathisia'
    },
    (4, 13): {
        'A': 'Oral propranolol or a low-dose benzodiazepine',
        'B': 'High-dose oral benztropine or trihexyphenidyl',
        'C': 'Intravenous dantrolene or oral bromocriptine',
        'D': 'Immediate dose escalation of the antipsychotic'
    },
    (4, 14): {
        'A': 'Acute muscular dystonia',
        'B': 'Tardive dyskinesia syndrome',
        'C': 'Parkinsonian cogwheel tremor',
        'D': 'Severe akathisia restlessness'
    },
    (4, 15): {
        'A': 'Acute nigrostriatal dopamine D2 receptor hypoactivity following drug discontinuation',
        'B': 'Striatal cholinergic depletion resulting from excessive muscarinic M1 receptor stimulation',
        'C': 'Dopamine D2 receptor upregulation and supersensitivity following prolonged chronic receptor blockade',
        'D': 'Autoimmune degradation of peripheral acetylcholine receptors at the neuromuscular junction'
    },
    (4, 16): {
        'A': 'Immediate dose escalation of the offending high-potency first-generation antipsychotic',
        'B': 'Oral anticholinergic agents such as benztropine or diphenhydramine therapy',
        'C': 'Dopamine receptor agonists such as pramipexole, ropinirole, or bromocriptine',
        'D': 'Vesicular monoamine transporter 2 inhibitors such as valbenazine or deutetrabenazine'
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
    (4, 22): {
        'A': 'Stop the antipsychotic immediately',
        'B': 'Escalate the antipsychotic dosage',
        'C': 'Administer high-dose propranolol',
        'D': 'Initiate prophylactic haloperidol'
    },
    (4, 23): {
        'A': 'Intravenous flumazenil infusion accompanied by high-dose oral benztropine',
        'B': 'Aggressive therapeutic hypothermia without discontinuing the offending antipsychotic',
        'C': 'Immediate drug cessation, supportive cooling, and dantrolene or bromocriptine therapy',
        'D': 'High-dose intravenous naloxone combined with central beta-adrenergic blockade'
    },
    (4, 26): {
        'A': 'Ziprasidone and aripiprazole convey the highest risk, while olanzapine conveys the lowest risk',
        'B': 'Olanzapine and clozapine convey the highest risk, while ziprasidone and aripiprazole convey lower risk',
        'C': 'Risperidone and paliperidone convey the highest risk, while clozapine and olanzapine convey lower risk',
        'D': 'High-potency typical antipsychotics convey greater risk, while atypical agents convey zero metabolic risk'
    },
    (4, 28): {
        'A': 'First-line monotherapy for acute adolescent-onset mild schizophreniform disorder',
        'B': 'Maintenance therapy for stable delusional disorder with preserved social functioning',
        'C': 'Adjunctive therapy for uncomplicated major depressive disorder without psychotic features',
        'D': 'Treatment-resistant schizophrenia, where it also significantly reduces suicidal behavior'
    },
    (4, 29): {
        'A': 'Acute renal tubular necrosis requiring routine serum creatinine monitoring',
        'B': 'Life-threatening agranulocytosis requiring regular absolute neutrophil count monitoring',
        'C': 'Fulminant hepatic failure requiring serial liver biopsy surveillance',
        'D': 'Interstitial pulmonary fibrosis requiring routine baseline spirometry'
    },

    # =========================================================================
    # PART 5: SUBSTANCE USE DISORDERS
    # =========================================================================
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
    (5, 4): {
        'A': 'Precontemplation stage of change',
        'B': 'Contemplation stage of change',
        'C': 'Preparation stage of change',
        'D': 'Maintenance stage of change'
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
        'A': 'Symptoms begin at 30 minutes, tremors peak at 6 hours, and delirium tremens resolves by 24 hours',
        'B': 'Symptoms begin at 24 hours, seizures occur at 4 days, and delirium tremens develops after 2 weeks',
        'C': 'Tremors begin at 6 to 12 hours, seizures occur at 12 to 48 hours, and delirium tremens peaks at 48 to 96 hours',
        'D': 'Hallucinations begin at 1 hour, confusion resolves at 6 hours, and autonomic instability is absent'
    },
    (5, 8): {
        'A': 'Immediate physical restraint and observation without administering sedative pharmacotherapy',
        'B': 'Symptom-triggered benzodiazepine administration such as lorazepam guided by CIWA protocol',
        'C': 'High-potency dopamine antagonists such as haloperidol monotherapy to suppress motor agitation',
        'D': 'Continuous intravenous flumazenil infusion to prevent secondary GABA-A down-regulation'
    },
    (5, 9): {
        'A': 'To prevent precipitating acute Wernicke encephalopathy by administering prior to intravenous dextrose',
        'B': 'To accelerate hepatic clearance of circulating ethanol through metabolic enzyme induction pathways',
        'C': 'To correct refractory intracellular hyperkalemia and prevent life-threatening ventricular dysrhythmias',
        'D': 'To reverse acute respiratory depression secondary to concomitant sedative-hypnotic co-ingestion'
    },
    (5, 10): {
        'A': 'Mild early-morning finger tremulousness with fully preserved cognitive orientation',
        'B': 'Isolated auditory hallucinations occurring within 6 hours of cessation with normal vital signs',
        'C': 'Single generalized tonic-clonic seizure occurring 24 hours post-cessation without confusion',
        'D': 'Severe delirium, visual hallucinations, marked agitation, and extreme autonomic instability at 48–96 hours'
    },
    (5, 11): {
        'A': 'Outpatient reassurance with primary care clinic follow-up within two weeks',
        'B': 'Low-dose oral hydroxyzine monotherapy in an unmonitored residential setting',
        'C': 'Intensive care unit admission, aggressive IV benzodiazepines, and thiamine',
        'D': 'Emergent hemodialysis combined with competitive opioid receptor antagonists'
    },
    (5, 12): {
        'A': 'Irreversibly inhibiting aldehyde dehydrogenase to produce severe aversive facial flushing',
        'B': 'Competitively blocking central mu-opioid receptors to attenuate dopamine-mediated reward and cravings',
        'C': 'Selectively activating prefrontal GABA-B receptors to substitute for alcohol-induced sedation',
        'D': 'Inhibiting monoamine oxidase enzymes to elevate mood and combat depressive symptoms'
    },
    (5, 13): {
        'A': 'Acamprosate modulates NMDA/GABA tone, while disulfiram inhibits aldehyde dehydrogenase',
        'B': 'Acamprosate stimulates dopamine release, while disulfiram enhances alcohol dehydrogenase',
        'C': 'Acamprosate blocks central mu receptors, while disulfiram stimulates GABA-A receptors',
        'D': 'Acamprosate inhibits monoamine oxidase, while disulfiram blocks cardiac sodium channels'
    },
    (5, 14): {
        'A': 'Full agonist at central postsynaptic mu and kappa opioid receptor complexes',
        'B': 'Non-competitive antagonist at glutamate N-methyl-D-aspartate receptors',
        'C': 'Direct agonist at serotonergic 5-HT2A receptors causing psychedelic experiences',
        'D': 'Partial agonist at cannabinoid CB1 and CB2 receptors modulating neurotransmission'
    },
    (5, 15): {
        'A': 'Bilateral pinpoint miosis, hypothermia, bradycardia, and diminished gastrointestinal motility',
        'B': 'Significant anorexia, severe pupillary dilation, horizontal nystagmus, and acute hyperreflexia',
        'C': 'Bilateral conjunctival injection, dry oral mucosa, tachycardia, and increased appetite',
        'D': 'Marked sinus bradycardia, excessive lacrimation, rhinorrhea, and severe abdominal cramping'
    },
    (5, 16): {
        'A': 'Edibles exert onset in minutes and dissipate in 1 hour, while inhaled lasts up to 12 hours',
        'B': 'Edibles exhibit delayed onset of 30 min to 3 h, while inhaled onset is rapid in 15 to 30 min',
        'C': 'Edibles and inhaled cannabis exhibit completely identical clinical pharmacokinetic profiles',
        'D': 'Inhaled cannabis undergoes extensive first-pass metabolism, while edibles bypass liver clearance'
    },
    (5, 17): {
        'A': 'Irritability, anxiety, insomnia, and anorexia, which are non-life-threatening without approved drugs',
        'B': 'Generalized tonic-clonic seizures, hyperthermia, and delirium tremens requiring intensive ICU care',
        'C': 'Life-threatening autonomic storm, acute hypertensive crisis, and malignant cardiac dysrhythmias',
        'D': 'Severe pinpoint pupillary miosis, respiratory depression, and profound unarousable coma state'
    },
    (5, 18): {
        'A': 'PCP acts as a serotonin receptor agonist; LSD acts as an NMDA receptor antagonist',
        'B': 'PCP acts as a selective mu-opioid agonist; LSD acts as a kappa-opioid receptor agonist',
        'C': 'PCP acts as an allosteric GABA-A agonist; LSD acts as a central GABA-B receptor agonist',
        'D': 'PCP acts as an NMDA receptor antagonist; LSD acts as a serotonin 5-HT2A receptor agonist'
    },
    (5, 19): {
        'A': 'Lysergic acid diethylamide ingestion',
        'B': 'Tetrahydrocannabinol concentration',
        'C': 'Phencyclidine intoxication exposure',
        'D': 'Prescription opioid analgesic agents'
    },
    (5, 20): {
        'A': 'Rigid four-point physical restraint in a brightly illuminated room without pharmacotherapy',
        'B': 'Low-stimulus calming environment, verbal reassurance, and judicious benzodiazepines or haloperidol',
        'C': 'Immediate high-dose intravenous naloxone boluses followed by continuous infusion',
        'D': 'Intravenous flumazenil administration to reverse competitive receptor antagonism'
    },
    (5, 21): {
        'A': 'Miosis, CNS depression, respiratory depression, and decreased bowel motility',
        'B': 'Mydriasis, marked motor agitation, tachypnea, and hyperactive bowel sounds',
        'C': 'Generalized seizures, hyperthermia, ocular clonus, and profuse diaphoresis',
        'D': 'Sinus tachycardia, acute hypertension, paranoia, and formication sensations'
    },
    (5, 22): {
        'A': 'Pinpoint pupillary miosis, CNS depression, and severe hypothermia',
        'B': 'Generalized status epilepticus, delirium tremens, and hemodynamic collapse',
        'C': 'Lacrimation, rhinorrhea, piloerection, yawning, mydriasis, and diarrhea',
        'D': 'Progressive respiratory depression, pulmonary edema, and anoxic brain injury'
    },
    (5, 23): {
        'A': 'Intravenous flumazenil titration combined with loop diuretics',
        'B': 'Intravenous beta-adrenergic antagonist administration for tachycardia',
        'C': 'Conservative observation in a darkened room without intervention',
        'D': 'Airway and ventilatory support with immediate intravenous naloxone'
    },
    (5, 24): {
        'A': 'Both are competitive antagonists requiring inpatient detoxification prior to therapy',
        'B': 'Methadone is a full agonist, while buprenorphine is a partial agonist and both safe in pregnancy',
        'C': 'Buprenorphine is a full agonist with high overdose risk, while methadone is a pure antagonist',
        'D': 'Methadone is contraindicated in pregnancy, while buprenorphine is restricted to inpatient use'
    },
    (5, 25): {
        'A': 'Only after the patient has completed full opioid withdrawal and is confirmed 7–14 days opioid-free',
        'B': 'During the acute height of active withdrawal to accelerate symptom resolution',
        'C': 'Immediately following acute overdose resuscitation without any required washout period',
        'D': 'Concurrently with full mu-opioid agonist maintenance regimens such as high-dose methadone'
    },
    (5, 26): {
        'A': 'Both drug classes directly open voltage-gated sodium channels in cerebral cortical neurons',
        'B': 'Benzodiazepines increase chloride channel open duration, while barbiturates increase opening frequency',
        'C': 'Benzodiazepines increase GABA-A opening frequency, while barbiturates increase channel open duration',
        'D': 'Both drug classes function as non-competitive antagonists at central NMDA glutamate receptors'
    },
    (5, 27): {
        'A': 'A benign and self-limiting withdrawal state that requires no active medical supervision',
        'B': 'A mild, transient syndrome characterized by vivid dreams and brief daytime somnolence',
        'C': 'A condition marked by profound central nervous system sedation and respiratory slowing',
        'D': 'A life-threatening state marked by seizures and delirium, requiring gradual taper and never abrupt cessation'
    },
    (5, 28): {
        'A': 'Cocaine selectively triggers monoamine vesicular release, while amphetamine blocks reuptake transporters',
        'B': 'Cocaine blocks monoamine reuptake and sodium channels, while amphetamine and MDMA release monoamines',
        'C': 'All central stimulants function primarily as direct mu-opioid receptor agonists in the brainstem',
        'D': 'Cocaine acts primarily as an uncompetitive antagonist at glutamate NMDA receptor complexes'
    },
    (5, 29): {
        'A': 'Avoid beta-blockers due to unopposed alpha-1 vasoconstriction; administer benzodiazepines',
        'B': 'Avoid benzodiazepines due to respiratory depression; administer non-selective beta-blockers',
        'C': 'Avoid intravenous crystalloid fluids; administer high-dose calcium channel antagonists',
        'D': 'Avoid all pharmacologic interventions; observe the patient under low lighting conditions'
    },
    (5, 30): {
        'A': 'Stimulant withdrawal frequently triggers status epilepticus and life-threatening delirium tremens',
        'B': 'Withdrawal is acutely life-threatening requiring ICU care, while intoxication is medically benign',
        'C': 'Withdrawal causes dysphoria, hypersomnia, and hyperphagia, while intoxication can cause psychosis',
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
