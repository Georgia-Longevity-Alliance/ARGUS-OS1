# VALIDATION PLAN — ARGUS-OS1

**Date:** 2026-07-16  
**Purpose:** Prove that each version of ARGUS-OS1 does what it claims.

---

## V1 — "Catch a Division" ($4,280)

### Objective
Prove the platform can maintain live cells and capture at least one complete cell division with lineage tracking over 48 hours.

### Validation Criteria (all must pass)

| # | Test | Method | Pass Threshold |
|---|------|--------|:--------------:|
| V1.1 | **Climate stability** | Log T, CO₂, O₂, RH at 1 Hz for 48h | ±0.5°C, ±0.5% CO₂, ±0.5% O₂, >90% RH — 99% of time |
| V1.2 | **Cell viability** | Trypan blue exclusion at t=0, 24h, 48h | >90% viability at 48h |
| V1.3 | **Division capture** | Manual review of time-lapse | ≥1 complete mitosis (prophase → cytokinesis) in frame |
| V1.4 | **Autofocus stability** | Measure focus score (Brenner gradient) over 48h | <10% degradation; no frames lost to focus failure |
| V1.5 | **Lineage tracking** | Compare automated tree vs. manual annotation | >90% correct parent-daughter assignments |
| V1.6 | **Data integrity** | SHA256 checksum of all frames | 0 corrupted frames |
| V1.7 | **Recovery from power loss** | Pull plug, restore after 10 min | System recalibrates, resumes acquisition within 5 min |

### Control Experiment
- Parallel culture in standard incubator (37°C, 5% CO₂, 20% O₂). Compare viability and division rate at 48h.

---

## V2 — "Cell Ablation Based on Centriole Identity" ($12,390)

### Objective
Prove targeted 405 nm whole-cell ablation kills the correct cell (Cell-Old or Cell-New) without affecting its sister, and that between-arms comparison reveals centriole-dependent effects.

### Validation Criteria

| # | Test | Method | Pass Threshold |
|---|------|--------|:--------------:|
| V2.1 | **Ablation specificity** | Ablate 50 Cell-Old + 50 Cell-New; count sister deaths at 1h | ≤2 sister deaths per 100 ablations |
| V2.2 | **Dose-response curve** | Vary power (10-100 mW) and duration (1-10 s), measure death at 1h | R² > 0.9 for logistic fit |
| V2.3 | **Sham equivalence** | Laser at intercellular space vs. untouched control; measure proliferation at 48h | p>0.1 (no difference) |
| V2.4 | **Arm discrimination** | Arm A (kill Cell-Old) vs. Arm B (kill Cell-New); compare surviving sister division probability at 24h | Measurable difference (p<0.05) OR effect size estimate with confidence interval |
| V2.5 | **Laser safety** | Interlock test: open door during pulse | Laser shuts off within 50 ms |
| V2.6 | **Photo-bleaching** | Measure GFP signal in non-targeted cells after 48h routine imaging | <20% signal loss |

### Control Experiment
- **Sham ablation:** Laser at intercellular space → both cells survive → verify proliferation = untouched.
- **Between-arms comparison:** If H₀ is true (no centriole effect), Arm A and Arm B sister fates should be identical. Any difference → centriole identity matters.

---

## V3 — "Edge AI" ($12,670)

### Objective
Prove on-device inference matches cloud/desktop performance for segmentation and tracking.

### Validation Criteria

| # | Test | Method | Pass Threshold |
|---|------|--------|:--------------:|
| V3.1 | **Segmentation accuracy** | CellPose 2.0 on Hailo-8L vs. GPU baseline (same model) | IoU > 0.90 vs. baseline |
| V3.2 | **Inference latency** | Measure end-to-end segmentation time per frame | <500 ms per 2048×2048 tile |
| V3.3 | **Power envelope** | Measure total system power draw | <15W sustained (RasPi 5 + Hailo) |

---

## V4-V6 — "AI Agent" ($14,970-$15,890)

### Objective
Prove LLM-based post-hoc analysis adds value without compromising system reliability.

### Validation Criteria

| # | Test | Method | Pass Threshold |
|---|------|--------|:--------------:|
| V4.1 | **Protocol deviation detection** | Introduce 5 known anomalies (e.g., bubble, focus jump, cell clumping), check if agent flags them | 5/5 detected |
| V4.2 | **False positive rate** | Run agent on 48h of clean data | <1 false alert per 24h |
| V4.3 | **Experiment summarisation** | Agent generates summary from 48h run. Compare to human-written summary | ≥3/5 key events correctly identified |
| V4.4 | **No interference** | Verify agent never blocks or delays acquisition loop | 0 delayed acquisitions |
| V4.5 | **Self-improvement (V5)** | Fine-tune on 5 experiments, test on 6th | ≥5% improvement in anomaly detection F1 |

---

## Centriolar Hypothesis Validation (Cross-Version)

### Objective
Prove ARGUS-OS1 can test the centriolar asymmetry hypothesis.

| # | Test | Method | Pass Threshold |
|---|------|--------|:--------------:|
| C1 | **Centriole age discrimination** | Dual-colour (Centrobin-GFP / Cenexin-mCherry) — can the system distinguish mother from daughter centriole in a dividing cell? | >95% accuracy vs. manual annotation (n=50 divisions) |
| C2 | **Inheritance tracking** | Track which daughter inherits mother centriole across ≥3 divisions | Correct assignment in ≥90% of divisions |
| C3 | **Ablation validation** | Ablate daughter cell that inherited mother centriole vs. daughter that did not. Compare sister cell fate at 24h | Measurable difference in division probability (p < 0.05, n≥20 pairs) |
| C4 | **Threshold detection** | Monitor Cenexin-mCherry intensity over lineage. Does signal decay correlate with fate change? | Spearman ρ > 0.5 between Cenexin intensity trend and time-to-senescence |

---

## Documentation Deliverables

Each validation test must produce:
1. Raw data (images, logs) — CC0, public
2. Analysis script (Jupyter notebook) — MIT, public
3. Summary figure — CC-BY-SA, public

---

> **Reference:** `CONCEPT.md` §5 for experimental protocol.  
> **Reference:** `docs/peer_review_2026-07-16.md` for weaknesses this plan addresses.
