---
# AGENTS.md

## Project Overview

This project is a neuroeconomics presentation based on:

**Zhang et al. (2025), “Inter-brain neural dynamics in biological and artificial intelligence systems,” Nature.**  
DOI: `10.1038/s41586-025-09196-4`

Main paper file:

- `Primary.pdf`

Supporting file:

- `Supplementary.pdf`

The presentation should explain the paper clearly, but not merely summarize biology. It must connect the paper to neuroeconomics, especially:

- social interaction
- strategic decision-making
- trust
- cooperation
- competition
- AI agents
- coupled decision systems
- multi-agent interaction

---

## Main Presentation Goal

Produce classroom presentation material that answers:

1. What is the research question?
2. What is the experimental design?
3. What are the main results?
4. What is the authors’ interpretation?
5. Am I convinced by the interpretation?
6. How would I redesign or extend the experiment?
7. What new experiment or application can be proposed?
8. How does this paper connect to neuroeconomics?

Tone should be suitable for an undergraduate classroom presentation: academic, clear, and understandable.

---

## One-Sentence Thesis

Social interaction is not only processed inside one individual brain; interacting individuals may form a coupled neural system with shared neural dynamics. This paper argues that such shared dynamics appear in both biological brains and artificial agents.

---

## Core Paper Summary

The paper studies whether interacting individuals show **shared neural dynamics**.

It has two main systems:

### Biological System

Two freely interacting mice were recorded simultaneously in the **dmPFC**, dorsomedial prefrontal cortex, using **in vivo microendoscopic calcium imaging**.

The paper compares:

- GABAergic neurons
- glutamatergic neurons

Key biological claim:

> GABAergic neurons contribute more strongly to inter-brain shared neural dynamics during social interaction than glutamatergic neurons.

### Artificial Intelligence System

The paper also studies interacting AI agents in a multi-agent reinforcement learning setting.

Key AI claim:

> Shared neural dynamics can also emerge in artificial agents when they learn social interaction.

---

## Main Research Questions

When preparing material, focus on these questions:

1. Do interacting brains show inter-brain neural correlation?
2. Which cell types contribute most to shared neural dynamics?
3. Can neural activity be decomposed into shared and unique neural subspaces?
4. Is shared neural activity merely caused by coordinated behavior?
5. Do AI agents show similar shared neural dynamics?
6. Can shared neural dynamics be understood as a general feature of interacting intelligent systems?

---

## Key Methods to Explain

Explain these methods in plain language when they appear:

- Pearson correlation
- cross-correlation
- phase-randomized control
- cross-pair control
- ROC analysis
- SVM classifier
- PLSC: Partial Least Squares Correlation
- PCA
- PLSR: Partial Least Squares Regression
- CCA: Canonical Correlation Analysis

Important explanation rule:

> Do not only name the method. Explain what the method is trying to test and why it matters for the paper’s interpretation.

---

## Main Results to Track

### Result 1: Inter-brain correlation exists during interaction

Two interacting mice show correlated dmPFC neural activity during social interaction.

This correlation is reduced or absent in:

- separation session
- cross-pair control
- phase-randomized control

Interpretation:

> Inter-brain correlation depends on real-time social interaction.

---

### Result 2: GABAergic neurons are more socially coupled

GABAergic neurons show stronger inter-brain correlation than glutamatergic neurons.

They also show stronger representation of social behavior.

Interpretation:

> GABAergic neurons may play a special role in coordinating or tracking social interaction states.

---

### Result 3: Social-responsive GABAergic neurons are especially important

Removing social-responsive GABAergic neurons computationally reduces inter-brain correlation.

Interpretation:

> Not all GABAergic neurons matter equally; social-responsive ones are especially important.

---

### Result 4: Neural activity separates into shared and unique subspaces

Using PLSC, the authors define:

- shared neural subspace
- unique neural subspace

Interpretation:

> Social interaction is represented in a high-dimensional shared neural structure, not just simple average synchrony.

---

### Result 5: Shared neural dynamics are not only coordinated behavior

The paper distinguishes:

- coordinated behavioral subspace
- uncoordinated behavioral subspace

Example:

- one mouse attacks
- the other escapes or defends

Interpretation:

> Shared neural dynamics are not just two animals doing the same action. They may reflect an interactive state between two individuals.

---

### Result 6: AI agents also show shared neural dynamics

Socially trained AI agents show shared neural dimensions.

Perturbing shared neural components reduces social actions.

Interpretation:

> Shared neural dynamics may be a general property of interacting intelligent systems, not only biological brains.

---

## Neuroeconomics Connection

Always connect the paper back to neuroeconomics.

Important framing:

> Economic and social decisions often happen between interacting agents, not inside isolated individuals.

Useful connections:

- strategic interaction
- best response
- trust game
- cooperation
- competition
- reciprocity
- social learning
- multi-agent decision-making
- coupled neural systems
- human-AI interaction

Possible analogy:

> In game theory, one agent’s best response depends on another agent’s action. In this paper, one brain’s activity may also be dynamically coupled with another brain during interaction.

---

## Critical Evaluation

Do not overstate the paper.

### Convincing Points

The paper is convincing because it uses:

- interaction vs separation comparison
- phase-randomized control
- cross-pair control
- cell-type comparison
- high-dimensional subspace analysis
- AI-agent perturbation

### Limitations

Mention these limitations clearly:

1. Mouse results are mostly correlational.
2. The paper does not directly manipulate shared neural subspace in mice.
3. AI agents are useful models, but not equivalent to biological brains.
4. Social behaviors in the mouse experiment are partly aggression-heavy.
5. dmPFC is only one part of the social brain network.
6. Shared neural subspace may partly reflect attention, arousal, or movement state.

Do not claim causality in the mouse experiment unless directly supported by the paper.

---

## Proposed New Experiment

Preferred proposal:

### Shared Neural Dynamics in a Repeated Trust Game

Research question:

> Do human pairs with higher trust and cooperation show stronger shared neural dynamics?

Design:

- human-human condition
- human-AI condition
- human-random-bot condition
- repeated trust game
- EEG or fNIRS hyperscanning

Variables:

- amount sent
- amount returned
- cooperation rate
- betrayal events
- reaction time
- self-reported trust
- inter-brain synchrony
- shared neural subspace

Prediction:

1. Human-human trust pairs show stronger shared neural dynamics.
2. Higher cooperation predicts larger shared neural subspace.
3. Betrayal may reduce or reorganize shared neural dynamics.
4. Shared neural dynamics may predict future cooperation.

Why this is neuroeconomics:

> It connects neural coupling to trust, reciprocity, strategic uncertainty, and interactive decision-making.

---

## Suggested Presentation Structure

Use this structure unless the user asks otherwise:

1. Title and one-sentence thesis
2. Why this paper matters for neuroeconomics
3. Research question
4. Experimental design
5. Neural recording and behavior tracking
6. Main result 1: inter-brain correlation
7. Main result 2: GABAergic neurons
8. Main result 3: shared vs unique neural subspace
9. Main result 4: not just coordinated behavior
10. AI-agent extension
11. Interpretation
12. Critical evaluation
13. New experiment proposal
14. Discussion questions
15. Final takeaway

---

## Required References

Before working on this project, use:

- `Primary.pdf` as the main source.
- `Supplementary.pdf` for methods, controls, and technical details.
- `docs/required_references.md` for external repositories and background tools.

Do not rely only on memory.

When a task involves paper claims, check `Primary.pdf` first.

When a task involves methods or supplementary controls, check `Supplementary.pdf`.

When a task involves implementation details, check the relevant external repository in `docs/required_references.md`.

---

## External Repositories and Tools

These are important references listed in `docs/required_references.md`.

### Paper-Specific Analysis Codebase

URL:

`https://github.com/hongw-lab/code_for_2024_zhang-phi`

Use for:

- analysis code
- reproduction workflow
- paper-specific implementation
- figure/table generation
- PLSC / CCA / behavioral analysis details

### MARL Chaser-Explorer Environment

URL:

`https://github.com/hongw-lab/marl_environment_chase`

Use for:

- multi-agent reinforcement learning environment
- Chaser-Explorer task
- agent interaction logic
- reward structure
- AI-agent social behavior

### Behavior Annotator

URL:

`https://github.com/hongw-lab/behavior_annotator`

Use for:

- behavior labels
- annotation workflow
- social vs non-social behavior categories

### Miniscope

URL:

`https://github.com/Aharoni-lab/Miniscope-v4/wiki/Lens-Configurations`

Use for:

- in vivo microendoscopic calcium imaging
- lens configuration
- neural recording setup

### SLEAP

URL:

`https://github.com/talmolab/sleap`

Use for:

- multi-animal pose tracking
- behavior features
- posture tracking

### CNMF-E

URL:

`https://github.com/zhoupc/cnmf_e`

Use for:

- calcium imaging signal extraction
- background noise removal
- neuronal trace extraction

### Background Literature

Kingsbury & Hong (2020), Trends in Neurosciences  
DOI:

`https://doi.org/10.1016/j.tins.2020.06.004`

Use for:

- multi-brain framework
- social interaction as coupled system

Kingsbury et al. (2019), Cell  
DOI:

`https://doi.org/10.1016/j.cell.2019.05.044`

Use for:

- prior inter-brain synchrony in mice
- dmPFC cross-brain neural correlation

---

## Do Not Do

Do not:

1. Invent results not in the paper.
2. Modify `Primary.pdf` or `Supplementary.pdf`.
3. Treat GitHub repositories as optional when implementation details matter.
4. Overstate biological causality.
5. Overstate equivalence between mice and AI agents.
6. Produce a generic biology-only summary.
7. Ignore the neuroeconomics connection.
8. Ignore `docs/required_references.md`.

---

## Desired Output Style

Use Traditional Chinese by default.

Keep important English terms, such as:

- shared neural dynamics
- inter-brain correlation
- shared neural subspace
- unique neural subspace
- PLSC
- CCA
- MARL
- GABAergic neurons
- glutamatergic neurons

Explain technical terms in plain language.

Use clear headings and tables when useful.

Separate:

- paper facts
- interpretation
- critique
- proposed extension

Final materials should be suitable for undergraduate classroom presentation.