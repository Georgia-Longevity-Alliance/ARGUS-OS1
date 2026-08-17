# Sterilization and Transfer Box — V7 / V8 / V9

**Date:** 2026-08-17
**Status:** Design.
**Author:** Jaba Tqemaladze

---

## 1. Summary

| Version | Enclosure | Transfer box | External sterilization equipment | Sterilization budget |
|:---:|------|------|------|:---:|
| V6 (OS1) | incubator HEPA H13; glove-box optional (~$12.5K) | V6-TRANSFER (optional; only if glove-box) | shared autoclave + UV-C (lab-level) | ~$1-2K (optional) |
| V7 (OS2) | glove-box, HEPA H13, Binder incubator | V7-TRANSFER (basic: UV-C + HEPA purge) | bench-top autoclave + UV-C chamber | ~$5-7K |
| V8 (OS3) | glove-box, HEPA H13, UV-C 254 nm (existing, $500) | V8-TRANSFER (UV-C + HEPA + optional VHP cycle) | autoclave + VHP generator (enclosure decontamination) + ultrasonic bath | ~$8-12K |
| V9 | + robot hands (V9-HANDS) | V9-TRANSFER (full: 2 doors, interlock, UV-C, HEPA, tray) | autoclave + VHP + UV-C + ultrasonic (full set) | ~$10-14K (shared) |

All versions use **one shared sterilization equipment set** (autoclave + VHP + UV-C) located in the lab next to the enclosures. The difference is in the transfer boxes and protocols. V9 applies to every OS stage (V9-Lite for OS1, V9-Standard for OS2, V9-Full for OS3; see V9_PROTOTYPE.md, section 2.1).

## 2. Transfer Box by Version

### 2.1 V7-TRANSFER (OS2) — basic

**Purpose:** V7 runs microfluidics (embryo loading), medium, plates. Gloves are used for loading, but consumables (cassettes, tubing, plates, medium) must enter sterile without loss of containment.

| Item | Specification |
|------|---------------|
| Body | PMMA 6 mm, ~35 x 35 x 40 cm |
| Doors | 2 sealed, mechanical interlock (never both open) |
| UV-C | 254 nm, 5-15 min timer |
| Ventilation | HEPA + valve, purge before opening inner door |
| Tray | Sliding aluminum |
| Control | ESP32, door + UV-cycle sensors; OK/UV indicator |
| Door operation | MANUAL (operator in gloves) — V7 has no robot hands |
| Budget | ~$600 (DIY) / ~$2-3K (commercial pass-through, Coy/MBraun style) |

**V7 protocol:** external sterilization → load into the box → outer door closed → UV-C 5-15 min + purge → operator in gloves opens the inner door → retrieves the load.

### 2.2 V8-TRANSFER (OS3) — with VHP option

**Purpose:** V8 runs laser ablation, injections, micromanipulation. Stricter sterilization is required (VHP for enclosure decontamination between batches) plus a spare entry route.

| Item | Specification |
|------|---------------|
| Body | PMMA 8 mm / stainless steel, ~40 x 40 x 45 cm |
| Doors | 2 sealed, interlock + DP sensor |
| UV-C | 254 nm, timer; optional double dose (2 cycles) |
| VHP port | Fitting for the VHP generator (full-enclosure decontamination) |
| Ventilation | HEPA H13 + valve; purge with residual H2O2 monitor |
| Tray | Sliding, removable (autoclavable) |
| Control | ESP32 + sensors; interlock with glove sensors (as in OS3 PARAMETERS) |
| Budget | ~$900 (DIY) |

### 2.3 V9-TRANSFER — full (see V9_PROTOTYPE.md, section 3.6)

The robot hand opens the inner door and retrieves the load. Glove ports are occupied by V9-HANDS. +$800.

## 3. Sterilization Equipment Selection

### 3.1 Autoclave (steam 121 C, 20 min) — glass, metal, PEEK, capillaries, plates

| Option | Model | Volume | USD | Verdict |
|--------|-------|:---:|:---:|---------|
| Bench-top (recommended) | Tuttnauer 2540EKA | 23 L | ~4-5K | Standard for small labs; service and parts available |
| Larger bench-top | Systec VX-65 | 65 L | ~9-12K | If load volume is high (V8 + V9 combined) |
| Budget | Boxun / Chinese bench-top | 18-50 L | 1.5-3K | Works, but weaker temperature control |
| **DIY** | Pressure cooker (Presto 23 qt / Instant Pot) + PID Arduino + thermocouple + relief valve | 12-22 L | ~250-400 | Feasible (established DIY, section 5.1) |

### 3.2 VHP generator (H2O2 vapor) — enclosure decontamination, non-autoclavable items

| Option | Model | USD | Verdict |
|--------|-------|:---:|---------|
| Professional | Bioquell Clarus C | 15-25K new / 5-10K used | Industry standard |
| Professional | Steris VHP 1000 | 15-30K | Large, for rooms |
| Chinese | VHP machines for clean rooms | 3-6K | Functional; weak documentation |
| **DIY** | Ultrasonic humidifier + 30-35% H2O2 + fan + residual H2O2 monitor (Dräger tube) | ~300-500 | Hazardous but feasible (section 5.2). **Residual monitor + purge mandatory** |

> **VHP is required for V8 and V9** (ablation/injection/transplantation = contamination risk). For V7, autoclave + UV-C + EtOH is sufficient.

### 3.3 UV-C equipment (254 nm) — plastic, outer surfaces, transfer boxes

| Option | Item | USD |
|--------|------|:---:|
| UV-C lamps 254 nm (Philips TUV / USHIO G15T8) | for the box and enclosure (V8 already has one) | 50-200 |
| UV-C chamber (small tools) | external sterilization of small items | 100-500 |
| UV-C tunnel (conveyor) | plate flow | 500-1500 |
| **DIY** | lamp + relay + timer + interlock | ~100 |

### 3.4 Dry-heat sterilizer (180 C, 60 min) — glass, metal (optional)

Memmert/Binder (~2-4K) or Chinese (~1-1.5K). Needed if steam is undesired for optics/metal. Optional for V9.

### 3.5 Ultrasonic bath — pre-cleaning (capillaries, end-effectors, spare parts)

| Model | USD |
|-------|:---:|
| Elma S30/S60 | 300-500 |
| Chinese 2-6 L | 50-150 |
| **DIY** | piezo transducer + ~40 kHz generator | ~80 |

Mandatory for V8 (microinjector capillaries after ablation) and V9 (end-effectors between tasks).

## 4. Matrix — What to Sterilize With What

| Load | V7 | V8 | V9 |
|------|:---:|:---:|:---:|
| Glass/metal/capillaries | Autoclave | Autoclave + ultrasonic | Autoclave + ultrasonic |
| PEEK/PTFE/end-effectors | Autoclave | Autoclave + ultrasonic | Autoclave + ultrasonic |
| Plastic/plates/cassettes | UV-C + EtOH | UV-C + EtOH | UV-C + EtOH (double packaging) |
| Medium (sealed vials) | UV-C surface | UV-C surface | UV-C surface |
| Microfluidic chips | UV-C + EtOH flush | VHP + flush | VHP + flush |
| Non-autoclavable | EtOH 70% / VHP option | VHP | VHP |
| Optics (objective) | not sterilized (inside enclosure) | as V7 | as V7 |
| Full enclosure (between batches) | EtOH + UV-C | **VHP cycle** | VHP cycle |
| V9 hand spare parts | — | — | autoclave/UV-C by material + transfer box |

## 5. DIY Designs (if commercial units are unavailable or expensive)

### 5.1 DIY autoclave (pressure cooker autoclave) — $250-400

```
Instant Pot / Presto 23 qt
+-- PID (Arduino/RPi Pico) + K thermocouple (steam zone, NOT in water)
+-- SSR relay (25 A) on the heater
+-- Stock relief valve — target 15 psi (121 C)
+-- Steam outlet fitting (sterile exhaust)
+-- Log: temperature/pressure/time to Flight Recorder
```
- Cycle: steam purge 5 min -> 121 C / 20 min -> slow cool-down
- Validation: biological indicators (*Geobacillus stearothermophilus*, e.g. Spordex steam) once per week
- Hazard: overheating/overpressure — **PID + safety valve only, never unattended**

### 5.2 DIY VHP — $300-500 (for V8/V9, with care)

```
Ultrasonic humidifier(s) + medical-grade 30-35% H2O2
+-- Injection into the enclosure via the transfer box VHP port
+-- Recirculation fan inside the enclosure
+-- Cycle: 30-60 min VHP -> 60-120 min HEPA purge (residual <1 ppm)
+-- Monitor: Dräger H2O2 tubes (residual) or electrochemical sensor
+-- Interlock: enclosure not opened until residual <1 ppm
```
- H2O2 30-35% is an oxidizer: gloves/eye protection, written SOP
- Compatibility: H2O2 degrades silicone/EPDM more slowly than O3; UV-C lamps survive; check seals
- Validation: chemical indicators (H2O2) in the box + TSA contact plates once per week

### 5.3 DIY UV-C transfer box — $100-200 (basic, V7)

254 nm lamp + relay + ESP32 + door sensors + timer. (V9 has the full version with HEPA and tray.)

### 5.4 DIY ultrasonic bath — ~$80

40 kHz piezo transducer + NE555/ESP32 generator + stainless steel tank.

## 6. SOP-A: External Sterilization (Spare Parts and Consumables) by Material

> General rule: **double packaging** — the outer layer is removed INSIDE the transfer box (after UV-C); the inner layer is sterile and removed inside the enclosure. Every package is labeled: sterilization date, method, sterility shelf life (24-72 h). Loads in the box are NOT stacked (UV-C must reach all surfaces).

### 6.1 Glass and metal (tools, forceps, plates, holders)

| Step | Action | Parameters | Control |
|:---:|--------|-----------|---------|
| 1 | Ultrasonic cleaning | bath, DI water + 1% detergent, 10-15 min | visual: no residue |
| 2 | Rinse | distilled water, 3x | — |
| 3 | Drying | 60-80 C, 15-30 min | dry |
| 4 | Packaging | autoclavable kraft pouches / double layer, indicator tape | tape changes color at 121 C |
| 5 | Autoclave | **121 C / 20 min / 15 psi** + drying 15-30 min | biological indicator (*G. stearothermophilus*) once/week |
| 6 | Storage | sealed pouches, <=72 h | date on pouch |

### 6.2 PEEK / PTFE / silicone (hand end-effectors, gaskets, seals)

| Step | Action | Parameters |
|:---:|--------|-----------|
| 1 | Ultrasonic cleaning | 10 min (as 6.1) |
| 2 | Autoclave | 121 C / 20 min (PEEK and PTFE survive). **Silicone — autoclave, NOT UV-C** (UV-C degrades silicone/EPDM) |
| 3 | Packaging | double, labeled |

### 6.3 Plastic (plates, cassettes, tips, vials)

| Type | Method | Parameters |
|------|-------|-----------|
| Autoclavable (PP, polycarbonate) | Autoclave | 121 C / 20 min |
| Non-autoclavable | UV-C + EtOH | 70% EtOH wipe -> UV-C 254 nm 15-30 min (all sides) |
| Both | Packaging | double, labeled |

### 6.4 Medium and reagents (DMEM, agarose, buffers, oil)

| Step | Action | Parameters |
|:---:|--------|-----------|
| 1 | Aliquots | sterile dispensing (if prepared in-house) -> 0.22 um filtration |
| 2 | Outer surface | UV-C 254 nm 15 min (sealed vial) + 70% EtOH wipe |
| 3 | Packaging | double pouch, labeled (medium expiry date) |
| 4 | Note | medium is NOT autoclaved (thermolabile) |

### 6.5 Microfluidic chips (V7/V8)

| Step | Action | Parameters |
|:---:|--------|-----------|
| 1 | Flush | 70% EtOH through channels -> sterile water |
| 2 | UV-C | 254 nm 30 min (all sides) |
| 3 | (V8) VHP option | VHP cycle in the transfer box at entry |

### 6.6 Non-autoclavable / heat-sensitive

| Method | Parameters |
|--------|-----------|
| VHP (in transfer box, V8/V9) | 30-60 min + HEPA purge to <1 ppm H2O2 |
| Chemical | 70% EtOH or 6% H2O2 wipe, 5-10 min contact |
| Glutaraldehyde 2% (complex items) | 30 min soak + rinse with sterile water |

### 6.7 V9 hand spare parts (arm module, gripper, end-effectors)

| Part | Method | Note |
|------|--------|------|
| Metal/PEEK (rod, gripper, frame) | ultrasonic + autoclave 121 C/20 min | as 6.1 |
| Wrist camera, FSR, controllers | **do NOT autoclave** — 70% EtOH wipe + UV-C 30 min + double packaging | electronics: surface sterilization only |
| Cables/sleeve | autoclave (silicone) / replace | UV-C degrades silicone |

### 6.8 Sterile stock (running parallel to the experiment)

| Stock | Quantity | Re-sterilization |
|-------|:---:|------|
| Microinjector capillaries | 10x per protocol | autoclave, pouches <=72 h |
| Hand end-effectors (gripper, pipette, wipe) | 2 sets | 6.2 / 6.7 |
| Plates/cassettes | 3x per sample shift | 6.3 |
| Medium | 2x daily need | fresh dispensing, per medium expiry |

## 7. SOP-IN: Entry Through the Transfer Box (Step by Step)

> Goal: bring a load in without compromising enclosure sterility. Key: **outer door -> UV-C cycle -> only then inner door**.

| Step | Who | Action | Control/condition |
|:---:|-----|--------|-------------------|
| 1 | Operator (outside) | Check box status: no cycle running, both doors closed, green indicator | door sensors |
| 2 | Operator | Remove OUTER packaging layer (inner layer stays) | label on pouch |
| 3 | Operator | Place load on tray, single layer (not stacked) | UV-C must reach all sides |
| 4 | Operator | Close outer door (sealed) | closure sensor + DP |
| 5 | Transfer box (auto) | **UV-C 254 nm 10-15 min** (timer by load type) | timer; V8: optional VHP 30-60 min |
| 6 | Transfer box (auto) | **HEPA purge 2-5 min** (V8/V9: to <1 ppm H2O2 if VHP was used) | residual H2O2 sensor |
| 7 | Transfer box | Indicator "CYCLE COMPLETE" (green) | interlock: inner door locked while UV-C != 0 |
| 8 | Inside enclosure | **V7/V8:** operator in gloves opens inner door, retrieves load, removes inner packaging layer inside, closes door. **V9:** robot hand (gripper) opens door, retrieves load, delivers to station, closes door | V9: vision check of grip |
| 9 | Operator | inner packaging layer discarded inside as waste (next removal) | — |
| 10 | Transfer box | HEPA purge 2-5 min (ready for next cycle) | — |
| 11 | System | **Log to Flight Recorder:** load, time, sterilization method, cycle number, actor (human/hand) | journal |

**SOP-IN limits:**

- Max load: <=90% of tray (UV-C shadow near walls)
- One load per cycle (except identical sterile items, per protocol)
- Do not bring in: open medium vials (sealed only), wet items (dry before UV-C), V9 electronics except per 6.7

## 8. SOP-OUT: Removal of Waste Materials (Step by Step)

> Goal: remove waste without contaminating the enclosure or the operator. Bio-waste — sealed INSIDE the enclosure + autoclaved OUTSIDE before disposal.

| Step | Who | Action | Control/condition |
|:---:|-----|--------|-------------------|
| 1 | Inside enclosure | Collect waste in a **sealed bag/container** (double bag for bio-waste) | bag sealed |
| 2 | Inside enclosure | **Sharps** (capillaries, needles) in a rigid sharps container | separate container |
| 3 | Inside enclosure | **Liquid bio-waste** (medium, supernatant) in a sealed vial with disinfectant (10% hypochlorite, 30 min) | inactivated before removal |
| 4 | Inside enclosure | Place bags/containers on the transfer tray (single layer) | do not overload |
| 5 | Inside enclosure | Close inner door (sealed) | closure sensor |
| 6 | Operator | Outer surface of the bag (visible through the box) — optional short UV-C 2-5 min (V8/V9) | only if outer decontamination needed |
| 7 | Operator | Open outer door outward — **no full UV cycle** (outward flow is safe) | — |
| 8 | Operator | Retrieve bags, close outer door | — |
| 9 | Operator | **Bio-waste -> autoclave 121 C / 20 min -> disposal.** Sharps -> rigid container -> regulated disposal. Non-bio (packaging, dry) -> regular waste | biological indicator (*G. stearothermophilus*) in every waste autoclave cycle |
| 10 | Transfer box | HEPA purge 2-5 min | — |
| 11 | System | **Log to Flight Recorder:** waste, time, inactivation (yes/no), destination (autoclave/disposal) | journal |

**Special cases:**

- **Broken V9 spare part (arm module/end-effector):** first EtOH wipe of outer surfaces inside the enclosure -> sealed bag -> removal -> repair/disassembly outside (all electronics: 70% EtOH + UV-C before re-entry, see 6.7)
- **Spill/leak inside the enclosure:** do NOT remove via the transfer box. First in-enclosure decontamination: absorbent -> disinfectant (10% hypochlorite) -> UV-C cycle -> then remove as bio-waste
- **Emergency stop (pressure, UV-C, hand):** waste stays inside until normalization; the transfer box is used only for repair tools
- **DP control:** after every removal, check enclosure pressure; if it drops, pause protocols until stabilized

**Waste streams (summary):**

| Waste | Packaging | Inactivation | Disposal |
|-------|-----------|--------------|----------|
| Capillaries/sharps | sharps container | — | rigid container |
| Medium/supernatant | sealed vial | 10% hypochlorite 30 min | autoclave -> drain |
| Plates/tips (bio) | double bag | — | autoclave -> municipal waste |
| Packaging/dry (non-bio) | bag | — | municipal waste |
| Electronics (repair) | double bag | EtOH wipe | repair outside |

## 9. Version-Specific SOPs — Full Protocols V7 / V8 / V9

> Each version = FULL cycle: external sterilization -> entry via transfer box -> work -> waste removal. Common steps (6-8) apply; here the version-specific details and sequence.

### 9.1 V7 (OS2) — operator in gloves, basic transfer box

**Profile:** microfluidics (embryo loading), medium, plates. Transfer box V7-TRANSFER. Doors opened by OPERATOR IN GLOVES. No VHP, no ultrasonic bath (optional).

**External sterilization set (V7):** autoclave (glass/metal/PEEK), UV-C 254 nm (plastic, vials), 70% EtOH (non-autoclavable). Microfluidic chips — EtOH flush + UV-C (6.5).

**Entry (SOP-IN-V7):**

| Step | Action |
|:---:|--------|
| 1 | Operator: box status (doors closed, green indicator) |
| 2 | Remove outer packaging, load on tray, single layer |
| 3 | Outer door closed -> **UV-C 10-15 min** -> HEPA purge 2-5 min |
| 4 | Indicator "CYCLE COMPLETE" (inner door unlocked) |
| 5 | Operator in gloves: open inner door -> retrieve load -> remove inner packaging inside enclosure -> close door |
| 6 | Box purge; **log to Flight Recorder** |

**Removal (SOP-OUT-V7):**

| Step | Action |
|:---:|--------|
| 1 | Operator in gloves: waste -> sealed bag (bio — double), sharps -> sharps container, liquid -> vial + 10% hypochlorite |
| 2 | Bags on tray -> inner door closed |
| 3 | Operator: outer door (no UV cycle) -> retrieve bags |
| 4 | Bio-waste -> **autoclave 121 C / 20 min** -> disposal; sharps -> rigid container |
| 5 | HEPA purge; **log to Flight Recorder** |

**Frequency (OS2 24/7 protocol):** sample exchange every ~2-3 h (chips), medium once/day, waste removal once per shift (8 h).

### 9.2 V8 (OS3) — operator in gloves + VHP decontamination, ultrasonic bath

**Profile:** laser ablation, microinjector, FOSH micromanipulator, hTERT-NPCs. Transfer box V8-TRANSFER (+VHP port). Doors — OPERATOR IN GLOVES (interlock with glove sensors).

**External sterilization set (V8):** autoclave + **ultrasonic bath** (capillaries after ablation, FOSH end-effectors), VHP cycle (enclosure decontamination between batches), UV-C, EtOH. Capillaries — ultrasonic 10 min -> autoclave (6.1).

**Entry (SOP-IN-V8):**

| Step | Action |
|:---:|--------|
| 1 | Operator: box status; confirm enclosure NOT in VHP cycle |
| 2 | Load (capillaries, FOSH end-effectors, NPC dishes, medium) — remove outer layer, on tray |
| 3 | Outer door closed -> **UV-C 10-15 min** -> HEPA purge to <1 ppm |
| 4 | (Optional, once per batch) **VHP enclosure cycle 30-60 min** via box VHP port -> purge to <1 ppm (Dräger tube) |
| 5 | Operator in gloves: inner door (unlocked ONLY when UV-C = 0 and <1 ppm H2O2) -> retrieve -> close |
| 6 | **Log to Flight Recorder** (including VHP cycle if run) |

**Removal (SOP-OUT-V8):**

| Step | Action |
|:---:|--------|
| 1 | Operator in gloves: **capillaries after ablation -> sharps container** (sharp, contaminated); medium/supernatant -> vial + hypochlorite 30 min; plates -> double bag |
| 2 | On tray -> inner door closed |
| 3 | Operator: outer door -> retrieve |
| 4 | **Autoclave ALL bio-waste** 121 C / 20 min (NPCs = human cells, stricter); sharps -> disposal |
| 5 | **After each ablation batch:** VHP decontamination of the enclosure before the next batch |
| 6 | Purge; **log** |

**Frequency (OS3, 4 weeks):** capillaries once/day (after batch), medium once/day, VHP cycle once/week (between batches), waste once per shift.

### 9.3 V9 — robot hands, full transfer box

**Profile:** V9-HANDS arms through glove ports, LLM brain V9-BRAIN. Transfer box V9-TRANSFER. Inner door opened by **ROBOT HAND** (gripper). Operator outside — only the outer door and the autoclave.

**External sterilization set (V9):** full set (autoclave + VHP + UV-C + ultrasonic) + **hand spare-part specifics (6.7):** metal/PEEK — autoclave; electronics (wrist camera, FSR) — 70% EtOH + UV-C 30 min + double packaging; silicone/sleeve — autoclave (NOT UV-C).

**Entry (SOP-IN-V9):**

| Step | Actor | Action |
|:---:|-------|--------|
| 1 | Operator | Box status; remove outer packaging; load on tray, single layer |
| 2 | Operator | Outer door closed -> **UV-C 10-15 min** (VHP option for non-autoclavable) -> HEPA purge to <1 ppm |
| 3 | Transfer box | Indicator "CYCLE COMPLETE"; inner door unlocked |
| 4 | **Robot hand** | Opens inner door (gripper) -> vision check of grip -> retrieves load from tray -> delivers to station/microscope -> closes door |
| 5 | LLM brain | Checklist verification (correct load, door closed) -> **log to Flight Recorder** (pose, force, time) |

**Removal (SOP-OUT-V9):**

| Step | Actor | Action |
|:---:|-------|--------|
| 1 | Robot hand | Collect waste: bio -> double sealed bag; sharps -> sharps container; liquid -> vial + hypochlorite |
| 2 | Robot hand | Place on tray -> close inner door |
| 3 | Operator | Outer door -> retrieve bags |
| 4 | Operator | **Bio-waste -> autoclave 121 C / 20 min**; sharps -> container; spare parts/electronics -> repair outside (EtOH + UV-C before re-entry, 6.7) |
| 5 | LLM brain | Log; if DP drops — pause protocols until stabilized |

**Frequency (24/7, weeks):** sample exchange automatic (on "mitosis complete"), medium every 6 h, capillaries once/day, VHP enclosure once/week, waste once per shift (8 h). Operator: only transfer-box top-up once/day + autoclave.

## 10. Budget Summary

| Equipment | V7 | V8 | V9 | Shared set (1 per lab) |
|-----------|:---:|:---:|:---:|:---:|
| Bench-top autoclave (Tuttnauer 2540EKA) | yes 5K | yes (shared) | yes (shared) | **5,000** |
| VHP generator (Chinese) or DIY | — | yes 4K | yes (shared) | **4,000** |
| UV-C chamber + lamps | yes 300 | yes (exists $500) | yes (in box) | **300** |
| Ultrasonic bath | — | yes 300 | yes (shared) | **300** |
| Dry-heat (optional) | — | — | optional 1.5K | — |
| Transfer box | DIY 600 | DIY 900 | 800 (in V9) | **2,300** |
| Indicators/consumables (Spordex, plates, Dräger tubes) | 200 | 300 | 300 | **300** |
| **TOTAL (sterilization, shared set)** | | | | **~12,200** |

V7 + transfer box: ~$600 | V8 + transfer box + VHP: ~$5.2K | V9: transfer box already in the V9 budget ($800); sterilization — shared set.

## 11. Decisions

1. **One shared sterilization set** (autoclave + VHP + UV-C + ultrasonic) in the lab, next to the enclosures. Each version adds only its own transfer box.
2. **V7** — autoclave + UV-C + EtOH is sufficient (microfluidics, medium).
3. **V8** — adds **VHP enclosure decontamination** (ablation/injection = high risk) and an ultrasonic bath (capillaries).
4. **V9** — full set + robot hands; transfer box with hardware interlock.
5. **DIY** — autoclave (pressure cooker + PID) and UV-C transfer box are recommended as workable; VHP — only with a residual monitor + SOP (with care).
6. **Weekly validation:** biological indicators (autoclave), TSA contact plates (VHP/enclosure), chemical indicators (UV-C).

---

*Engineering document. Related: docs/V9_PROTOTYPE.md (V9-TRANSFER), ARGUS-OS3/PARAMETERS.md (UV-C sterilization $500).*
