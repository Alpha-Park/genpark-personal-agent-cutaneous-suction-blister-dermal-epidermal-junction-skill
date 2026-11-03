---
name: genpark-personal-agent-cutaneous-suction-blister-dermal-epidermal-junction-skill
version: 1.0.0
description: Calculates Suction Blister Formation Time (SBFT in minutes) and Dermo-Epidermal Junction Adherence Index (DEJ-AI) to evaluate basement membrane zone structural integrity.
authors:
  - GenPark Ecosystem
tags:
  - personal-agent
  - dermatology
  - suction-blister
  - sbft
  - dej
  - basement-membrane
  - zero-dependency
---

# Cutaneous Suction Blister DEJ Adhesion Skill

## Mathematical Formulation

Dermo-Epidermal Junction Adherence Index (DEJ-AI):

$$\text{DEJ-AI} = \min\left(100.0, \, \left(\frac{\text{SBFT (min)}}{60.0}\right) \times 100\right)$$

Blister formation velocity index:

$$V_{\text{blister}} = \frac{60.0}{\text{SBFT (min)}} \quad (\text{units/hour})$$

Temperature-normalized formation time ($39^\circ\text{C}$ reference):

$$\text{SBFT}_{39^\circ\text{C}} = \text{SBFT} \times (1.0 + (T_{\text{skin}} - 39.0) \times 0.05)$$

## Clinical Interpretation
- **Normal DEJ Adhesion**: $\text{SBFT} \in [45, 90]\text{ min}$ (robust lamina densa anchoring fibrils)
- **Subclinical DEJ Weakness**: $\text{SBFT} \in [30, 45]\text{ min}$ (early photoaging or chronological skin thinning)
- **Marked DEJ Fragility**: $\text{SBFT} < 30\text{ min}$ (severe basement membrane separation, epidermolysis bullosa vulnerability, or steroid-induced skin atrophy)
