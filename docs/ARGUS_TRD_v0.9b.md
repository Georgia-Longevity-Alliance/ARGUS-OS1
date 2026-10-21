# ARGUS — Technical Requirements Document (TRD) v0.9b

**Version:** 0.9b (restructured after requirements-first engineering review, 2026-10-21)
**Date:** 2026-10-21
**Status:** ⏳ framework; finalization to v1.0 on 06.11.2026, pending biological pre-test data (V1–V6)
**Client / biological requirements:** Jaba Tqemaladze (Georgia Longevity Alliance)
**Engineering lead (mechanics / electronics / software):** TBD (open collaboration)

> **What changed versus v0.9 (response to the main review objection).**
> 1. **Functional requirements (FR) are separated from technical solutions (TS).** FR — only *what* the system must do, with a measurable output and acceptance criterion (experiment-designer domain). TS — *how* to implement, as **options with trade-offs**, not mandates (engineer domain).
> 2. **Microbots removed from mandatory scope** — demoted to one removal option among several (see companion document *Cell Removal Methods Comparison*).
> 3. **New functional requirements added** (experiment-designer domain): operation in darkness with minimal phototoxicity; situational awareness inside the enclosure (internal cameras, 3D map); sterile material entry/exit over years of operation; degrees of freedom for future experiments (extension slots); minimal perturbation of tracked cells and 3D polarity registration.
> 4. **Primary experiment goal clarified:** establish the fundamental fact — whether immortalized fibroblasts have a Hayflick limit — by observing the dynamics of division rate of the oldest-centriole lineage versus a neighbouring newest-centriole lineage, over months, without opening the enclosure (see companion *Protocol*).

---

## 1. Purpose and scope

**What ARGUS is.** An autonomous robotic platform for long-term (6–12 months) live observation of dividing immortalized human fibroblasts (BJ-hTERT; cross-validation MRC5-hTERT), fluorescence identification and tracking of centrioles, measurement of the **division-rate dynamics** of lineages carrying the oldest (OLD) versus newest (NEW) centriole, and addressable removal of unwanted cells.

**Primary scientific goal (fundamental fact).** Establish whether immortalized human fibroblasts (BJ-hTERT, MRC5-hTERT) **have a Hayflick limit — yes or no**. This is the anchor: without this established fact, all subsequent tasks (cancer cells, stem-cell niches) are more complex and their results more controversial. Cancer cells are a later goal, only if time permits.

**Instrumental task of ARGUS (how the fact is established).** Observe how the division rate of a cell carrying the **oldest** centriole changes while a cell carrying the **newest** centriole sits beside it, over a long period (months), without opening the enclosure. Expected signal of limit onset: progressive slowing of the OLD lineage relative to the NEW one. Context — the Hayflick limit: somatic cells ≈ 50 divisions, stem cells ≈ 200, immortalized fibroblasts ≈ 800–1000, cancer cells — several thousand. Precisely counting the number of divisions is the task of research staff, not of ARGUS.

**Scope of this document.**
- Here: functional and non-functional requirements, technical options, minimally sufficient baseline plus extension slots, acceptance criteria, responsibility split, pre-test input data.
- NOT here: step-by-step engineering solutions, drawings, specific component models — the engineer's domain per this TRD.
- **Principle (adopted from the requirements-first review):** the final construction rests on experimentally established requirements; any parameter marked «⚠️ pre-test» is finalized from Section 6 data and is not fixed before that.

---

## 2. Functional requirements (FR) — what ARGUS must do

Experiment-designer domain. No row prescribes an implementation. Status column: ✅ specified / ⚠️ pre-test (value from V1–V6) / 🆕 new.

| ID | Function | Measurable output | Criterion (draft) | Status |
|----|----------|-------------------|-------------------|--------|
| FR-1 | Long-term live observation 24/7 without opening the sealed enclosure | Continuous recording; failures/day | ≥ 30 days without recording failure; then months | ✅ specified |
| FR-2 | Real-time mitosis detection | Fraction of divisions auto-detected vs manual annotation | ≥ 90 % | ⚠️ pre-test (imaging rate, resolution) |
| FR-3 | Centriole tracking: identify mother (Cep164+) and daughter (Cep164−); age from pedigree | Tracking completeness; signal SNR | Completeness ≥ 80 %; SNR ≥ 3× above background | ⚠️ pre-test (critical: V3) |
| FR-4 | **Division-rate dynamics: OLD vs NEW, side by side, many generations**; the culture is maintained as exactly **2 studied single cells** (oldest and newest centriole) | Interdivision time per lineage; time trend (stable / diverging) | Statistically detectable trend (pilot → power) | ⚠️ pre-test |
| FR-5 | **Continuous removal of all mitotic progeny except the 2 studied cells (OLD/NEW)** and export of their debris, without harming observed cells | Removals/day; survival of observed cell; hit accuracy | Accuracy ≤ 2 µm; survival per V4/V5; reliability of the continuous regime | ⚠️ pre-test; **method = TS (not assigned)** |
| FR-6 | Culture maintenance (media change, reagents) without loss of containment | Proliferation vs control | Not worse than control over 7 days | ⚠️ pre-test (V6) |
| FR-7 | 🆕 **Operation in complete darkness with minimal phototoxicity** (cells live in the enclosure for years) | Light dose per cell: number of excitations and dose per 24 h | Minimum that meets SNR (V3); «image only when needed» mode | ✅ specified (range — ⚠️ V3) |
| FR-8 | 🆕 **Situational awareness inside the enclosure**: 3D picture of activity and coordinates for safe manipulation in darkness | Coordinate accuracy of objects; map resolution | Accuracy sufficient for manipulation (V8-metrology) | ✅ specified (numbers — ⚠️) |
| FR-9 | 🆕 **Sterile material entry and sterile waste exit over years of operation** without opening the enclosure | Success of sterile cycles; growth on control media | 0 contamination per entry/exit cycle | ✅ specified |
| FR-10 | 🆕 **Degrees of freedom for future experiments**: minimally sufficient baseline + extension slots (cancer cells, stem-cell niches, cardiac protocols) | Number of swappable modules attachable without baseline rework | ≥ list in §3.2; attachable without opening mechanics | ✅ specified |
| FR-11 | Full digital event log + remote monitoring (alerts, dashboard) | Fraction of events logged; alert delivery | 100 % events; alerts delivered | ✅ specified |
| FR-12 | 🆕 **Minimal perturbation of tracked-cell position**: OLD/NEW identity is assigned by location; no chemical treatment of tracked cells | Position shift of a tracked cell per day/week; identity losses caused by displacement | Minimum compatible with imaging; 0 identity losses from perturbation | ✅ specified (numbers — ⚠️ V1) |
| FR-13 | 🆕 **3D cell-polarity registration** (top/bottom in addition to left/right) — for future centriole-transplantation experiments | Registered cell orientation (incl. top-bottom axis); preserved through manipulations | Orientation registered and preserved per tracked lineage | ✅ specified |

---

## 3. Minimally sufficient baseline and extension slots

Principle: **minimally sufficient for the first experiment** (immortalized fibroblasts; OLD/NEW division-rate dynamics), **yet not «crippled»** — the baseline provides standard slots so that everything needed for later experiments can be added without redesign.

### 3.1 Baseline (first experiment)
1. Sealed enclosure: 37 ± 0.3 °C; 5 ± 0.5 % CO₂; 2 ± 0.3 % O₂; RH ≥ 90 % in the culture volume.
2. Fluorescence imaging: 488/561 nm excitation (Centrin1-GFP / Cep164-RFP), objective + camera (selection — by V3/V10, not fixed).
3. Long-term 24/7 timelapse, months of recording.
4. Mitosis detection + lineage tracking (on-device AI).
5. Centriole-age assignment by pedigree (Cep164 + lineage).
6. OLD/NEW division-rate dynamics computation.
7. Cell-removal function via a **swappable port** (method — TS, see companion comparison).
8. Internal cameras (day/night vision) + IR illumination + 3D map of the enclosure (FR-7/FR-8) + 3D polarity registration (FR-13).
9. Sterile entry/exit transfer ports (FR-9; hardware concept — see `docs/STERILIZATION_TRANSFER.md`, `docs/V9_PROTOTYPE.md`).
10. Logging, monitoring, alerts (FR-11).
11. Power: UPS + LiFePO₄, ≥ 14 h.

### 3.2 Extension slots (future experiments)
| Slot | Purpose | Interface |
|------|---------|-----------|
| Additional excitation channel 640 nm and others | Other fluorophores/markers (cancer, stem) | Standard light port, no mechanical rework |
| Objective upgrade 40× dry → 60× water (V2) | Higher NA/resolution | Standard holder/rail |
| Additional manipulators / in-enclosure transporter | Moving vessels and tools by 3D map | Standard sealed ports + control bus |
| Removal module (magnetic beads / microbots / circulation) | Removal method chosen after V4/V5 | Swappable removal port (baseline item 7) |
| Culture format change (chamber between two thin glasses, plate, dish) | Different protocols | Standard 12×12 mm sample stage + adapters |
| Controlled fluid delivery/withdrawal | Future assays (reagent addition, sampling) | Fluid port via entry transfer port |
| External equipment docking (sorting, etc.) | Extended protocols | Exit transfer port |

---

## 4. Technical solutions / options (TS) — engineer domain

**Options, not mandates.** No TS is fixed before Section 6 data (V1–V6) and the engineer's decision. Earlier technical specifications (2026-07) and TRD v0.9 are sources of options, not requirements.

| FR | Implementation options | Key trade-off | Status |
|----|------------------------|---------------|--------|
| FR-1/FR-3 | Inverted microscope; compact optical module above the sample; hybrid | Layout, access to the chamber from both sides, thermal regime | Open until V1–V3 |
| FR-3 | Objective 40×/0.95 dry (V1) → 60×/1.2 water (V2); camera RasPi HQ → sCMOS | SNR vs phototoxicity (FR-7) — the central trade-off | Open until V3/V10 |
| FR-5 | Laser 405 nm + galvo scanner; 2 micromanipulators; fluid circulation; optical tweezers; magnetic microbeads; microbots | See companion *Cell Removal Methods Comparison*; joint decision after V4/V5 | Open |
| FR-7/FR-8 | Internal day/night cameras; IR illumination; stereo/SLAM 3D reconstruction | 3D-map accuracy vs cost/placement | Open (V8) |
| FR-9 | Sterile transfer boxes (entry and exit) with UV cycle; sealed septum ports | Cycle speed vs sterility assurance | Open (reference `docs/STERILIZATION_TRANSFER.md`) |
| FR-10 | Open mechanics (OpenFlexure v7 or other); standard bus/interfaces for slots | Maturity vs flexibility | Open |
| FR-11 | Local LLM agent + edge AI (e.g., Hailo-8L); dashboard/Telegram | Security/autonomy | Open |

---

## 5. Non-functional requirements (NFR)

| ID | Requirement | Value | Status |
|----|-------------|-------|--------|
| NFR-1 | Positioning accuracy | Stage step < 100 nm | ✅ specified |
| NFR-2 | Addressable-action accuracy (removal) | ≤ 2 µm from target | ⚠️ V4/V5 |
| NFR-3 | Environment stability | 37 ± 0.3 °C; 5 ± 0.5 % CO₂; 2 ± 0.3 % O₂; RH ≥ 90 % | ✅ specified |
| NFR-4 | Autonomy | ≥ 30 days without opening the enclosure | ✅ specified (extends to months) |
| NFR-5 | Power resilience | ≥ 14 h (UPS + LiFePO₄) | ✅ specified |
| NFR-6 | Biosafety | BSL-1; BSL-2 under transduction — confirm with local committee | ✅ |
| NFR-7 | Optical drift | Thermostable enclosure, vibration isolation; drift within focus tolerance | ⚠️ V8 |
| NFR-8 | Condensation | No condensate on optics/camera window over ≥ 14 days (37 °C, RH ≥ 90 %); dry compartment RH < 50 % | ⚠️ stage 4 |
| NFR-9 | Licensing | Software GPLv3; hardware CERN-OHL-S v2; documentation CC-BY-SA 4.0 | ✅ |
| NFR-10 | Budget | V1 PoC ≈ $2,355 … V6 Full ≈ $10,455 | ✅ indicative |
| NFR-11 | Culture-volume humidity | RH ≥ 90 % at 37 °C — do NOT reduce (local dehumidification only, §12) | ✅ |
| NFR-12 | 🆕 Minimal light load | Dose and number of excitations per cell per 24 h minimized while meeting SNR; «image on demand» mode | ⚠️ V3 |

---

## 6. Input data from biological pre-tests (bio-group commitments)

**The bio-group fills by 03.11.2026 with measurable numbers (not qualitative statements).**

| # | Question | Measurable output | Closes | Deadline |
|---|----------|-------------------|--------|----------|
| V1 | How reliably does a fibroblast attach and how far does it move over 24–72 h | % attached at 2/6/24 h; displacement µm/h; coating | Chamber material, stage speed, autofocus (FR-1/FR-3) | 03.11 |
| V2 | Behaviour during division | Mitosis scenario (rounding/shift/attachment) | Tracking algorithm, imaging rate (FR-2/FR-4) | 03.11 |
| V3 | Real distinguishability of the centriole marker | SNR vs background; minimum exposure | Camera/objective/filters + light load (FR-3/FR-7) | 03.11 |
| V4 | Removal of a cell without harm to the observed one | % survival; hit accuracy | Removal protocol and method (FR-5) | 03.11 |
| V5 | Debris/necrosis removal | Method; preservation of neighbours | Level-2 removal choice (FR-5, companion comparison) | 03.11 |
| V6 | Effect of the device environment on proliferation | Proliferation in chamber vs control | Chamber design, lighting mode (FR-6) | 03.11 |

**Output:** table «marker → wavelength → expected intensity → recommended filters/camera → fitness criterion» + update of Sections 2–5 to v1.0 (06.11).

---

## 7. Engineering verifications with a defined purpose (not «exercises»)

Each verification has a purpose, an expected measurable result, a stated necessity and an agreed scope. Scope is confirmed or amended by the engineer before starting.

| # | Verification | Purpose | Expected measurable output | Necessity | Deadline |
|---|--------------|---------|---------------------------|-----------|----------|
| V8a | XY-stage metrology | Close U-E1 | Repeatability (µm), step, hysteresis | Numbers for NFR-1 and acceptance | from 28.10, in parallel |
| V8b | Focus drift | Close U-E2 | Z drift over 24–72 h | Numbers for NFR-7 | in parallel |
| V8c | Addressable-action accuracy on inert objects | Close U-E3/U-E4 | Accuracy ≤ 2 µm; coordination of 2 manipulators | Numbers for NFR-2 | in parallel |
| V8d | Internal cameras: 3D enclosure map | Partially close FR-8 | Object-coordinate accuracy; behaviour in darkness | Safe manipulation in darkness (FR-7) | after test-stand assembly |

**Important (per review):** V8 removes **engineering** risk (repeatability, drift, accuracy) by its own objective criteria and does NOT confirm biological fitness of the construction. Fitness is established only by V10/V11 on culture.

---

## 8. Acceptance criteria and verification methods

| Function | Success criterion | Verification method | Data status |
|----------|-------------------|---------------------|-------------|
| FR-1 | Recording ≥ 30 days without failure; then months | Recording stress test | ✅ |
| FR-2 | ≥ 90 % divisions detected | Cross-check with manual annotation | ⚠️ |
| FR-3 | SNR ≥ 3×; Completeness ≥ 80 % | Marker calibration on sample; spotiflow metrics | ⚠️ critical |
| FR-4 | OLD/NEW trend statistically detectable | Pilot → power analysis | ⚠️ |
| FR-5 | Accuracy ≤ 2 µm; survival ≥ specified | Inert (V8c) + culture | ⚠️ |
| FR-7 | Light load within NFR-12 while meeting SNR | Dose measurements at V3 | ⚠️ |
| FR-8 | 3D-map accuracy sufficient for manipulation | Test-stand validation | ⚠️ |
| FR-9 | 0 contamination per cycle | Control media at each cycle | ✅ specified |
| FR-10 | Slots attach without baseline rework | Per-slot check | ✅ specified |
| FR-11 | 100 % events; alerts delivered | Test-event injection | ✅ |
| NFR-8 | No condensate over ≥ 14 days; dry compartment RH < 50 % | Frame review (PSF), photo documentation | ⚠️ stage 4 |

**Acceptance rule:** any item marked «⚠️» is not admitted into the final specification until the bio-group/verification provides the value. Intermediate versions (V1 PoC) are accepted by criteria independent of biological data (mechanics, electronics, software, calibration on inert objects).

---

## 9. Responsibility split

| Party | Domain | Excludes |
|-------|--------|----------|
| **Bio-group (J. Tqemaladze)** | Biological hypothesis, pre-tests (§6), measurable requirements, success criteria, culture validation | Engineering decisions, component selection |
| **Engineer** | Concept, alternative technical solutions, mechanics, electronics, software, calibration on inert objects, assembly | Biological conditions and predictions; final construction only per TRD data |
| **Joint** | TRD v1.0, final optics selection, removal method, acceptance, grant application | — |

---

## 10. Work order (stages)

| Stage | What | Responsible | Deadline |
|-------|------|-------------|----------|
| 0 | Biological pre-experiments (V1–V6) | Bio-group | 27.10 — 03.11.2026 |
| P | In parallel: metrology (V8), concept, software modules, calibration on inert objects (agreed scope) | Engineer | from 28.10, not blocked |
| 1 | TRD v1.0 (finalize Sections 2–5 from stage-0 data) | Joint | 06.11.2026 |
| 2 | Optics/camera/filters and removal-method selection per TRD v1.0 | Engineer (per TRD) | after 06.11 |
| 3 | Mechanics construction, electronics, software integration | Engineer | per plan |
| 4 | Culture validation against Section 8 criteria | Joint | when ready |

---

## 11. Risks and open questions

1. **Marker SNR below threshold** (V3) → more sensitive camera / longer exposure / alternative marker. Open until V3.
2. **SNR ↔ phototoxicity conflict (FR-7):** more light = better tracking but higher risk over months. The central trade-off of stage 1; resolved by V3 (minimum exposure) + «image on demand» mode.
3. **Cell drift beyond tracking capability** (V1/V2) → autonomy limits. Open.
4. **Survival at removal below threshold** (V4) → revise criterion/method. Open.
5. **3D-map accuracy of internal cameras** insufficient for manipulation in darkness → constrains FR-8. Verified by V8d.
6. **Transfer-port sterility** (FR-9) — control media each cycle; risk revealed at validation.
7. **Condensation on sCMOS** at RH ≥ 90 % — hermetically sealed, desiccated sensor chamber mandatory (NFR-8, §12).
8. **BSL-2 under transduction** — confirm with local committee.
9. Grant application: functions as «goals + validation plan + success criteria».

---

## 12. Humidity management in the enclosure (condensation)

**Problem.** The culture volume requires RH ≥ 90 % at 37 °C (otherwise media evaporation and osmolarity drift). Humid air over months of operation causes frost/condensate on the cooled sCMOS sensor (down to −20 °C), on cold spots (Peltier, heatsinks), on the objective body, and mould.

**Principle.** Dehumidification is LOCAL ONLY (at sensor/optics/electronics). Dehumidifying the culture volume is prohibited (violates osmolarity control, FR-6). Dew point at 37 °C / RH 90 % ≈ 35 °C — any surface colder will condense.

**Protection scheme:**
1. **Hermetically sealed, desiccated sCMOS sensor chamber — mandatory** (verify against the model datasheet).
2. **Camera-window heating** (≈ 2–5 W, ~38 °C — above dew point).
3. **Dry instrument compartment** (sealed partition between humid culture volume and dry instrument volume; 3Å molecular-sieve cartridge, target RH < 40–50 %).
4. **Local purge with dry filtered air (HEPA H14)** into the dry compartment; NOT N₂ (interferes with O₂ control).
5. **Thermal decoupling and objective heating** (components in the humid volume held ~37 °C).
6. **Monitoring and alerts** (T/RH sensor in the dry compartment; alert at RH > 50 %).

**Acceptance criterion (NFR-8):** ≥ 14 days at 37 °C / RH ≥ 90 % — no condensate/frost on the camera window and optics (frames: no artefacts, no PSF degradation), dry compartment RH < 50 %.

**Open decision for the engineer (before stage 3):** combine items 2–4 within budget and layout. Item 1 is mandatory in any variant.

---

*Version 0.9b → 1.0 after Section 6 is filled by the bio-group. Companion documents: Cell Removal Methods Comparison; Protocol: Hayflick Limit in Immortalized Fibroblasts. Hardware concepts for the transfer box and autonomy layer: docs/STERILIZATION_TRANSFER.md, docs/V9_PROTOTYPE.md.*
