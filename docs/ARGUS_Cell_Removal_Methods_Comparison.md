# ARGUS — Comparison of Methods for Removing Unwanted Cells and Debris

**Date:** 2026-10-21
**Status:** working document for joint decision; addresses the engineering review on pre-committing to a removal mechanism
**Relation:** FR-5 (TRD v0.9b), pre-tests V4/V5 (03.11), companion Protocol (Phase 2)

---

## 1. Function decomposition

The function FR-5 «remove unwanted cells and their debris without harming observed cells» splits into two levels:

| Level | What it does | When it is needed |
|-------|--------------|-------------------|
| **Level 1 — detachment** | Detach the unwanted cell from the substrate, remove it from observation | After class assignment (in the first experiment: cells with intermediate-age centrioles, to keep pure OLD and NEW lineages side by side) |
| **Level 2 — export** | Remove the detached cell and necrosis products from the culture without harming neighbours | As long as the cell/debris does not disturb observation or poison the medium |

Level-1 and level-2 methods are chosen **independently** and **after** V4 (survival, accuracy) and V5 (necrosis) data.

---

## 2. Comparison criteria

| Criterion | Why it matters |
|-----------|----------------|
| Addressability | Can one act on a single cell rather than the whole field |
| Accuracy | Geometric hit accuracy (target ≤ 2 µm) |
| Risk to observed cells | Damage/stress to neighbours, phototoxicity |
| Debris removal | Does the method remove the debris itself or only the cell |
| Feasibility in a 12×12 mm chamber | Fits the footprint, does not obstruct observation |
| Sterility | Risk of contamination on insertion/removal of elements |
| Technology maturity | Proven in similar tasks |
| Cost/complexity | Budget and engineering effort |

---

## 3. Options (each for level 1 and/or level 2)

### 3.1 Fluid circulation / laminar flow
- **Description:** controlled medium flow washes detached cells and debris into a collection zone.
- **Level:** 2 (export). Not sufficient for level 1 (does not detach an attached cell).
- **Pros:** cheap, simple, proven, effective at debris removal, no moving parts in culture.
- **Cons:** flow may displace observed cells (needs V1 — attachment); not addressable; medium consumption; risk of washing away clonal lineages.
- **Maturity:** high (standard in flow chambers).
- **Decision point (V5):** is flow compatible with retaining observed cells.

### 3.2 Laser ablation (405 nm) + wash
- **Description:** laser + galvo scanner selectively kills/detaches the unwanted cell; debris is washed out (3.1) or removed otherwise.
- **Level:** 1 (detachment/ablation) + participation in 2.
- **Pros:** addressable, accurate (≤ 2 µm), non-contact, automatable.
- **Cons:** phototoxicity at 405 nm (conflict with FR-7 — dose control per V3/V4); ablation products remain (needs level 2); risk to neighbours if under-aimed.
- **Maturity:** high (laser microdissection).
- **Decision point (V4):** survival of the observed cell under adjacent ablation.

### 3.3 Micromanipulators (2: hold + detach)
- **Description:** needles/probes inside the enclosure; the first holds the unwanted cell, the second tears it off the substrate; the cell is then carried to the exit port.
- **Level:** 1 and partly 2 (can physically carry the detached cell to the exit port).
- **Pros:** addressable; can physically export the cell (reduces level-2 tasks); sterile via sealed septum ports.
- **Cons:** moving parts in the enclosure (contamination, wear); complex automation; slow; requires coordinate calibration (V8); risk of touching neighbours.
- **Maturity:** medium-high (micromanipulation is standard, but not inside a sealed enclosure for months).
- **Decision point (V4/V8).**

### 3.4 Optical tweezers
- **Description:** focused laser beam captures and moves a detached cell/particle.
- **Level:** 2 (export of a detached cell/debris).
- **Pros:** non-contact, addressable, accurate.
- **Cons:** requires high-NA optics (conflicts with compact layout and darkness); beam power — phototoxicity; limited force (only detached/small objects); costlier.
- **Maturity:** medium.
- **Decision point (V3 optics + V4/V5).**

### 3.5 Local enzymatic detachment (microdose trypsin/EDTA) + wash
- **Description:** local delivery of a solution that detaches the unwanted cell; then flow exports it.
- **Level:** 1 (detachment) + 2 (flow).
- **Pros:** cheap, gentle to neighbours (if dose is local and brief).
- **Cons:** not addressable as-is (needs microfluidic dosing); residual enzyme stresses the culture; concentration control in a sealed chamber is difficult.
- **Maturity:** medium (standard outside a sealed chamber).
- **Decision point (V5/V6).**

### 3.6 Magnetic microbeads + external magnet
- **Description:** functionalized magnetic beads bind/mark detached cells and debris; an external magnet draws them to a collection zone.
- **Level:** 2 (export).
- **Pros:** cheap, proven (magnetic separation), works in darkness, few moving parts.
- **Cons:** bead delivery and sterility; control of «do not bind observed cells»; beads in the medium may interfere with optics.
- **Maturity:** high (biotechnology), in a sealed chamber requires adaptation.
- **Decision point (V5).**

### 3.7 Microbots (magnetic / self-propelled) in culture
- **Description:** autonomous/controlled micro-objects in the medium capture the detached cell/debris and carry them out of the culture.
- **Level:** 2 (export).
- **Pros:** addressable in 3D enclosure space; can work in darkness from the 3D map (FR-8); scalable over large areas.
- **Cons:** **low maturity in this task** — no evidence that the mechanism is necessary, superior to alternatives, or feasible at 12×12 mm scale; materials/control/sterility unproven; risk to neighbours and optics.
- **Maturity:** low (research-grade).
- **Status:** remains **one option** for level 2, NOT a mandatory requirement. Joint decision after V4/V5, only if it shows an advantage over 3.1/3.6.

---

## 4. Summary table

| Method | Level | Addressability | Accuracy | Risk to neighbours | Debris export | In 12×12 mm chamber | Sterility | Maturity | Cost |
|--------|-------|----------------|----------|--------------------|---------------|---------------------|-----------|----------|------|
| Circulation (3.1) | 2 | no | n/a | medium (wash-off) | yes | yes | yes | high | low |
| Laser 405 + wash (3.2) | 1 (+2) | yes | ≤ 2 µm | medium (phototoxic.) | no (needs 2) | yes | yes | high | medium |
| Micromanipulators (3.3) | 1+2 | yes | high | low-medium | partial | yes | via ports | medium-high | medium |
| Optical tweezers (3.4) | 2 | yes | high | medium (phototoxic.) | yes | questionable (optics) | yes | medium | higher |
| Enzyme local (3.5) | 1+2 | low | low | low | yes (with flow) | needs dispenser | yes | medium | low |
| Magnetic beads (3.6) | 2 | medium | medium | low | yes | yes | needs adaptation | high | low |
| **Microbots (3.7)** | 2 | yes | unconfirmed | unknown | yes | **unconfirmed** | unproven | **low** | high |

---

## 5. Conclusion and proposed decision

1. **Level 1 (detachment)** — choice between laser 405 nm and micromanipulators **from V4 data** (observed-cell survival, accuracy). One working method is enough for the first stage.
2. **Level 2 (export)** — choice among circulation (3.1), magnetic beads (3.6) and microbots (3.7) **from V5 data** (debris-removal method, neighbour preservation). Start with the most mature (3.1/3.6); microbots only if they demonstrate an advantage.
3. **The ARGUS baseline** is designed so the removal method is a **swappable module** (standard removal port), not a permanently built-in part. This allows changing the method between stages and for future experiments without rework.
4. **Decision is joint**, led by the engineer, after 03.11 (V4/V5). Until then — only the port interface is prepared.

---

*Companion documents: TRD v0.9b (FR-5, §4), Protocol: Hayflick Limit in Immortalized Fibroblasts (Phase 2).*
