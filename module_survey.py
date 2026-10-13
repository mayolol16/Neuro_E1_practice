import os
from pptx import Presentation
import fitz

folder = "/Users/markyoussef_1/Downloads/NeuroE1ShEET"

# 1. Lectures
lectures_meta = [
    {
        "module": "1. CNS Anatomy",
        "file": "CNS Anatomy 2026.pdf",
        "los": [
            "1. Describe the divisions of the central nervous system",
            "2. Describe the lobes of the brain and the location of major gyri and sulci",
            "3. Describe the functions of each of the lobes",
            "4. Describe the internal organization of the brain including the location of gray and white matter",
            "5. Describe the components of the brainstem",
            "6. Describe the meningeal coverings of the brain & the spaces they create"
        ]
    },
    {
        "module": "2. CNS Development",
        "file": "CNS Development- student.pptx",
        "los": [
            "1. Describe the process of neurulation and the significance of ectoderm and neural crest",
            "2. Describe the primary and secondary embryological compartments of the CNS and adult derivatives",
            "3. Describe how the alar and basal plates position sensory and motor nuclei in spinal cord and brainstem",
            "4. Explain neuronal proliferation, migration in cerebral hemispheres and associated developmental disorders",
            "5. Explain Chiari Malformation I and II and association with syringomyelia and meningomyelocele",
            "6. Explain postnatal CNS maturation: brain weight, critical periods, myelination, synaptogenesis, dendritic growth"
        ]
    },
    {
        "module": "3. Neurotransmission & Action Potentials",
        "file": "Neurotransmission- student.pptx",
        "los": [
            "1. Describe the steps involved in synaptic transmission",
            "2. Explain how reuptake transporters are involved in transmitter recycling and energy metabolism",
            "3. Explain how NMDA receptors work and their role in excitotoxicity",
            "4. Explain how the GABA-A receptor suppresses neuronal activity",
            "5. Describe the characteristics of monoamine neurotransmitters (NE, DA, 5-HT)"
        ]
    },
    {
        "module": "4. Ventricular System & CSF",
        "file": "IMC 535 - Ventricles student.pptx",
        "los": [
            "1. Describe the different parts of the ventricular system",
            "2. Identify the ventricular system on gross specimens and imaging",
            "3. Explain the flow of cerebral spinal fluid",
            "4. Explain the different types of hydrocephalus and treatments"
        ]
    },
    {
        "module": "5. Neuromuscular Junction Disorders",
        "file": "Neuromuscular Junction Disorders.pptx",
        "los": [
            "1. Describe the events occurring at the neuromuscular junction that lead to successful transmission",
            "2. Describe presentation, pathophysiology, diagnostic testing, and treatment for MG, LEMS, and botulism",
            "3. Identify the symptoms and signs of MG, LEMS, & botulism"
        ]
    },
    {
        "module": "6. Somatosensory DCML (Tactile & Spinal Cord)",
        "file": "Somatosensory pathway- DCML student.pptx",
        "los": [
            "1. Describe the general characteristics of sensory pathways",
            "2. Describe the general characteristics of tactile sensory receptors",
            "3. Discuss how axon diameter relates to transmission of tactile information",
            "4. Describe the pathway that transmits tactile sensory information (cell bodies, axons, cortical areas)",
            "5. Explain somatotopic orientation of tactile information at spinal cord and cortex",
            "6. Describe how the stretch reflex is related to this pathway and its clinical significance",
            "7. Describe how the cortical homunculus can change",
            "8. Describe the effect of lesions involving the pathway and in related cortical areas",
            "9. Explain the concept of agnosia and give examples"
        ]
    },
    {
        "module": "7. Somatosensory ALS (Pain & Nociception)",
        "file": "Somatosensory pathway- ALS student.pptx",
        "los": [
            "1. Explain the difference between nociception and pain",
            "2. Discuss how axon diameter relates to transmission of tactile and pain information",
            "3. Describe pathways transmitting pain, cell bodies/axons, and cortical areas involved",
            "4. Describe the withdrawal reflex",
            "5. Compare position of tactile and pain pathways in spinal cord, brainstem, and hemisphere",
            "6. Describe effects of lesions at different locations along each pathway"
        ]
    },
    {
        "module": "8. Trigeminal Somatosensory Pathway",
        "file": "Somatosensory pathway- Trigeminal student.pptx",
        "los": [
            "1. Describe pathways transmitting tactile and pain/temp from face to cortex (cell bodies and axons)",
            "2. Describe the jaw-jerk reflex and corneal reflex",
            "3. Describe effects of lesions at different locations along facial pathways",
            "4. Explain the pathophysiological mechanisms involved in pain",
            "5. Explain sensitization and its relationship to allodynia and hyperalgesia"
        ]
    },
    {
        "module": "9. Headache Disorders",
        "file": "SMBS MS2 lecture 10-9-26.pptx",
        "los": [
            "1. Explain proposed pathophysiologic mechanisms for migraine",
            "2. Identify diagnostic criteria for major primary headache disorders and where to find them",
            "3. Understand therapeutic approach to primary headache disorders (acute and preventive)"
        ]
    }
]

print("Module Summary of Lectures:")
total_los = sum(len(m["los"]) for m in lectures_meta)
for m in lectures_meta:
    print(f"  {m['module']}: {len(m['los'])} LOs ({m['file']})")
print(f"Total Lecture Learning Objectives: {total_los}")
