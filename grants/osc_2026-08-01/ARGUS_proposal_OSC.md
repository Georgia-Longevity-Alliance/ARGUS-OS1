# ARGUS-OS1 — Open-Source AI Microscope for Centriole Lineage Tracking

**Open Science Cup / Open Source Collective**
**PI:** Jaba Tqemaladze, MD — Georgia Longevity Alliance (reg. №404506520)
**GitHub:** https://github.com/Georgia-Longevity-Alliance/ARGUS-OS1
**Deadline:** August 1, 2026
**Budget:** $17,000

---

## Abstract

ARGUS-OS1 is an open-source, AI-first microscope for hands-free longitudinal imaging of C. elegans embryogenesis. All inference runs locally on an NVIDIA Jetson AGX Orin (275 TOPS)—no cloud, no data leaving the lab. The core question: **does a cell's division history predict when its centrioles disappear, beyond what cell fate already tells us?** All hardware, firmware, and software released under Apache 2.0.

---

## 1. Problem

A single C. elegans embryo takes over three hours of continuous manual microscopy. A skilled operator tracks 10–20 cells at a time. ARGUS tracks all of them—centriole intensity, division orientation, apoptosis markers—without a human at the eyepiece.

Commercial motorized microscopes with incubation run $15–50K and were never designed for AI. We are building something different: open, affordable, and local-AI from the ground up.

---

## 2. Scientific Background

Centriole elimination in C. elegans follows cell fate. Kalbfuss & Gönczy (2023, PMID 37256957) showed that ~88% of somatic cells lose their centrioles during embryogenesis, with retention restricted to specific lineages.

What has never been measured is **timing**. Two cells of the same type, in the same embryo, may lose their centrioles at different points. Does division history explain any of that variation? No one has measured this—because no one has had a tool that can track every cell continuously for hours.

---

## 3. Approach

### Hardware (OS1 = V6)
- OpenFlexure motorized microscope (open-source, 3D-printable)
- 40×/0.75 Plan Fluor objective
- sCMOS camera (ZWO ASI183MM Pro)
- NVIDIA Jetson AGX Orin (275 TOPS, on-device AI)
- CO₂ incubator with active humidity control

### AI Pipeline
- **OCW** (Bassett et al. 2026) — C. elegans embryo nuclear segmentation + tracking
- **Custom centriole detector** — SAS-4::GFP spot detection
- **Cell lineage reconstruction** — from division events
- **Pedigree Score** — mixed-effects logistic regression + Bayesian hierarchical model (JMbayes2)
- All inference on-device, no cloud dependency

### Validation
- 100 embryos, 4D imaging (xyz + time)
- Triple transgenic strain: Centrin1-GFP + SAS-4::mCherry + histone::BFP
- Heidenhain iron haematoxylin for label-free centriole detection

---

## 4. Milestones (15 months)

| Phase | Duration | Deliverable |
|-------|----------|------------|
| **Pilot** | Months 1–3 | Stochasticity validation, phototoxicity ceiling, marker cross-validation |
| **Build** | Months 2–4 | ARGUS V6 assembly, motor release API, triple transgenic strain |
| **Main** | Months 4–10 | 100 embryos, pedigree + fate recording |
| **Analysis** | Months 10–12 | Mixed-effects regression + Bayesian hierarchical model |
| **Release** | Months 12–15 | Open data, Zenodo archive, publication |

---

## 5. Budget ($17,000)

| Item | Amount |
|------|--------|
| Jetson AGX Orin (64GB) | $2,000 |
| OpenFlexure Microscope Kit v7 | $1,500 |
| 40×/0.75 Plan Fluor Objective | $3,500 |
| sCMOS Camera (ZWO ASI183MM Pro) | $1,200 |
| Optical components (filters, dichroics) | $1,800 |
| Motorized stage + Sangaboard v3 | $600 |
| C. elegans strains + reagents | $1,500 |
| CO₂ incubator + dehumidifier | $2,500 |
| Compute (cloud — JMbayes2) | $400 |
| Consumables (12 months) | $800 |
| Contingency (10%) | $1,200 |
| **TOTAL** | **$17,000** |

---

## 6. Open Science Commitment

- **Apache 2.0** — all code, firmware, and hardware designs
- **Zenodo** — data and analysis scripts archived with DOI
- **OSF** — protocols and documentation
- **GitHub** — 200+ commits (14–28 Jul 2026), public repository
- **No proprietary components** — entirely open-source toolchain

---

## 7. Team

| Name | Role |
|------|------|
| **Jaba Tqemaladze, MD** | PI — experimental design, data analysis |
| **Ilya Zheleznov** | Lead developer — Jetson deployment, OCW pipeline |
| **Giorgi Tsomaia** | Hardware — OpenFlexure assembly, optics |
| **David Meyer, PhD** (Uni Köln) | C. elegans consultant |

---

## 8. Why Open Source Collective

ARGUS-OS1 is built on open-source principles from day one:
- Hardware: OpenFlexure (CERN OHL v1.2)
- Firmware: Sangaboard (MIT)
- AI: OCW + custom detectors (Apache 2.0)
- Data: public Zenodo archive

OSC fiscal hosting aligns perfectly with our model: transparent budgeting, community governance, and public accountability. Funds go directly to equipment and reagents—no institutional overhead, no closed-source licenses.
