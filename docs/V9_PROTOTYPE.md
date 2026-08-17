# V9 Prototype — Robot Hands Through Glove Ports + Shared Local LLM Brain

**Date:** 2026-08-17
**Status:** Design. Upgrade of V7/V8.
**Author:** Jaba Tqemaladze

---

## 1. Scope

V9 converts ARGUS from a manually operated instrument into a self-servicing laboratory:

1. **V9-HANDS** — robotic manipulators inserted into the glove ports of the enclosure *in place of human hands*. They provide continuous long-term servicing: sample exchange, medium replenishment, objective cleaning, sterilization, and maintenance of the micro-robots inside.
2. **V9-BRAIN** — an external LLM running on local hardware, on the same host that controls the micromanipulators (FOSH) and micro-robots inside the enclosure. A single point of intelligence for planning, diagnostics, and fault tolerance.

V9 is an autonomy layer applicable to all OS stages (OS1/OS2/OS3); see section 2.1 for the per-stage variants. It is not a new platform.

## 2. Rationale

### 2.1 Applicability to OS1 / OS2 / OS3

V9 is an autonomy layer that applies to every OS stage. The full configuration was specified for OS3 (V8); OS1 and OS2 get lighter variants. The scope is set by two factors: whether the enclosure has glove ports (robot hands) and the local compute budget (LLM brain).

| Stage | Base hardware | Enclosure | Robot hands | LLM brain | Transfer box | Variant |
|-------|---------------|-----------|-------------|-----------|--------------|---------|
| **OS1 (V6)** | OpenFlexure + Jetson Orin NX + dry 40x | incubator HEPA H13; glove-box optional (~$12.5K) | 1 arm (optional; only if glove-box) | Jetson Orin NX runs small models (Llama 3.2 3-8B, Phi-3.5); full LLM on external host | optional (only if glove-box) | **V9-Lite** |
| **OS2 (V7)** | 60x/1.2 WI + sCMOS + microfluidic + Jetson AGX | glove-box HEPA H13 (included) | 2 arms | Jetson AGX 64GB + external Mac/GPU host (or single host) | V7-TRANSFER | **V9-Standard** |
| **OS3 (V8)** | + light-sheet + fs-laser + tweezers + FOSH + Mac M4 Pro | glove-box HEPA H13 + UV-C (included) | 2 arms | Mac Studio M3 Ultra 192GB, Mixtral/Llama/Qwen 70B | V8/V9-TRANSFER + VHP | **V9-Full** |

**V9-Lite (OS1) notes:**

- Without a glove-box, the OS1 robot arm is not applicable; the LLM brain and autonomy (anomaly detection, experiment scheduling, escalation) still are.
- With a glove-box: one arm is sufficient (sample exchange, objective cleaning, medium replenishment every 6 h for U2OS/HeLa pilot runs).
- The Jetson Orin NX (8-16 GB) runs a small local model (Llama 3.2 3B/8B, Phi-3.5) for real-time tasks; the planning brain runs on the lab host or the shared AIS server. Cost: ~$5-7K (1 arm + end-effectors + transfer box), host shared with the lab.

**V9-Standard (OS2) notes:**

- Full two-arm configuration as in section 3; the AGX 64GB accelerates Vision; the brain runs on the same host as the arms (single host principle, section 4.4).
- V7-TRANSFER (basic, UV-C + HEPA) per STERILIZATION_TRANSFER.md, section 2.1.

**V9-Full (OS3) notes:**

- Two arms + VHP decontamination + ultrasonic bath; full sterilization set; the exact specification in STERILIZATION_TRANSFER.md, sections 2.2-2.3 and 9.

All three variants share: the same arm/end-effector hardware, the same Tool Bridge + Safety Layer + Flight Recorder stack, and the same escalation rule.

| V7/V8 limitation | V9 solution |
|------------------|-------------|
| Operator required every 2-24 h (hands in gloves) | Robot hands through the same glove ports |
| Downtime at night, weekends, multi-week runs | 24/7 servicing with no operator in the loop |
| Operator is a contamination vector through gloves | Sealed sleeve, UV-C compatible |
| Micro-robots inside need operator support | Hands service the micro-robots themselves (charging, tool changes) |
| Brain (LLM) and actuators on separate machines | One host = one brain, zero network latency |

Long-term protocols that require 24/7:

- OS2: RPE1 across 5 generations — 4-5 days per run, multiple runs
- OS3: hTERT-NPCs, 100 pairs, 4 weeks
- Overnight sample queues (100 embryos, OS1) — hands swap cassettes without an operator

## 3. V9-HANDS — Design

### 3.1 Primary constraint

Insert an arm through a glove port (Ø200-300 mm, typical) while preserving enclosure integrity, sterility, and UV-C compatibility. All electronics and actuators remain **outside** the enclosure.

### 3.2 Selected approach: cable-driven arm through a sleeve

```
OUTSIDE (unclean zone)           ENCLOSURE (clean zone)
+----------------------------+   +---------------------------+
| NEMA 17 x 5-6 (actuators)  |   |                           |
| TMC2209 drivers            |   | forearm (rod)             |
| Encoders                   |---| wrist + gripper           |
| Controller (Pico/ESP32)    |   | wrist camera              |
+----------------------------+   | exchangeable end-effectors|
      glove port flange          +---------------------------+
      (silicone sleeve, sealed)
```

- **External actuators** — no motor heat inside the enclosure, no UV-C damage to electronics, service without breaking containment.
- **Cables (Bowden/steel, 0.8-1.2 mm)** run through the sealed sleeve; all electronics stay outside.
- **Sleeve**: reinforced silicone/EPDM, mounted on the standard glove port flange (glove replaced by sleeve).
- **Inside**: forearm rod (anodized aluminum/PEEK) + wrist with a two-finger parallel gripper.

### 3.3 Specification

| Parameter | Value |
|-----------|-------|
| Arms | 2 (left/right, mirrored) |
| Degrees of freedom | 5-6 DOF per arm (3 shoulder + 2-3 wrist) |
| Actuation | NEMA 17, TMC2209 (same stack as microscope/FOSH) |
| Force | 0.5-5 N (sufficient for plates, slides, capillaries, cassettes) |
| Repeatability | ±0.5 mm positioning; ±0.05 mm at the gripper |
| Speed | 50-200 mm/s |
| Sensors | Motor encoders; FSR force sensing in the wrist; wrist camera (vision-guided) |
| Materials | Internal parts: aluminum, PEEK, PTFE — autoclave-safe, UV-C resistant |
| Seal | Silicone sleeve 0.5 mm, flange per ISO 10648-2, bubble test |

### 3.4 Exchangeable end-effectors

| End-effector | Task |
|--------------|------|
| Gripper (2 fingers, rubber pads) | Samples, cassettes, slides, capillaries |
| Pipette tool | Medium replenishment (DMEM/agarose), waste removal |
| Wipe tool | 60x/1.2 WI objective cleaning (immersion, lens) |
| UV tool | Local sterilization around the sample |
| Capillary holder | Install/replace microinjection capillaries |
| Rake/scraper | Cell-pair separation (OS3) |

### 3.5 Alternatives considered and rejected

| Option | Cost | Verdict |
|--------|:---:|---------|
| Direct drive through a large sealed flange | $8-15K/arm | Expensive, complex, heats enclosure |
| Magnetic coupling through the wall | — | Force <1 N, insufficient |
| Commercial glovebox arms (MBraun/Lamil isolator arms) | $30-80K | Expensive, closed ecosystem |
| **Cable-driven arm through a sleeve** | **~$1.2K/arm** | Open, low-cost, sterile |

### 3.6 Transfer box — consumables and spare parts entry

**Principle:** glove ports are never opened — they are occupied by V9-HANDS. All consumables (medium, capillaries, plates, end-effectors) and spare parts are sterilized **outside** the enclosure and enter through a dedicated **pass-through / airlock chamber**.

```
OUTSIDE                  TRANSFER BOX (UV-C)          ENCLOSURE
+---------------------+   +-----------------------+   +------------------------+
| autoclave/UV-C/VHP  |-->| outer door            |-->| inner door             |
| sterilization       |   | UV-C 254 nm           |   | (opened only by hand)  |
| double packaging    |   | vent valve            |   | door/pressure sensors  |
+---------------------+   | UV-C sensor           |   | tray for the hands     |
                          +-----------------------+   +------------------------+
```

**Transfer box specification (V9-TRANSFER):**

| Item | Specification |
|------|---------------|
| Body | Transparent polycarbonate/PMMA 6-8 mm, ~40 x 40 x 45 cm (fits a cassette, plate, end-effectors) |
| Doors | 2 sealed (outer + inner), hardware interlock (never both open) |
| In-chamber sterilization | UV-C 254 nm, timer (5-15 min by load type); optional VHP (H2O2 vapor) |
| Ventilation | HEPA filter + valve: purge before opening the inner door |
| Sensors | Door states (interlock), UV-C cycle complete, pressure differential |
| Tray | Sliding aluminum tray — the hand takes the load directly from it |
| Interlock | Inner door opens only when UV-C = 0 and DP is nominal; only by robot hand, never manually |

**Standard entry protocol:**

1. **Outside the enclosure:** consumable/spare part — double packaging (two layers) — sterilization by type:
   - Autoclave 121 C / 20 min (capillaries, metal, PEEK, plates)
   - UV-C 254 nm 15-30 min (plastic, medium in sealed vials — outer surface only)
   - Chemical: 70% EtOH / VHP (non-autoclavable)
2. **Into the transfer box:** outer door — load onto the tray — outer door closed — UV-C cycle (5-15 min) + HEPA purge.
3. **Into the enclosure:** the V9 hand opens the inner door (gripper) — takes the load from the tray — delivers it to the microscope/workstation — closes the door.
4. **Reverse flow (waste):** the hand places waste on the tray — inner door closed — outer door opens outward (no UV cycle; outward flow is safe).

**Why this closes the V9 loop:**

- Robot arm repair/replacement: the arm module is detachable at the flange and is removed from the outside; replacements enter through the transfer box — the enclosure is never opened.
- 24/7 consumables: the operator tops up the transfer box once per day (sterilization outside) — the hands inside run continuously.
- Fallback: if the transfer box fails, loads enter manually through a free glove port (V8 mode, rare).

> External sterilization procedures and equipment (autoclave/VHP/UV-C/ultrasonic) for V7/V8/V9 are specified in `docs/STERILIZATION_TRANSFER.md`. The same equipment set serves V7 and V8.

## 4. V9-BRAIN — Shared Local LLM

### 4.1 Principle

One host = brain + controller of all enclosure hardware. The same computer that runs the LLM also controls:

- the V9-HANDS arms,
- the FOSH v2.0 micromanipulator (OS3),
- the micro-robots inside the enclosure,
- the microscope (Jetson AGX as compute accelerator over 10GbE/PCIe; host as orchestrator).

### 4.2 Host options

| Option | Configuration | VRAM/RAM | Cost |
|--------|---------------|:---:|:---:|
| A (baseline) | Mac M4 Pro 64GB (already in OS3) + ollama/vLLM | 64GB unified | 0 (available) |
| B (recommended) | Mac Studio M3 Ultra 192GB | 192GB unified | ~$5-6K |
| C (server) | EPYC/Threadripper + 2x RTX 4090 | 96GB VRAM | ~$6-8K |

LLM: **Mixtral 8x7B -> Llama 3.3 70B / Qwen2.5-72B**, local, no cloud. Same class already specified for OS3 (Mac M4 Pro, Mixtral/Llama).

### 4.3 Brain architecture (Coscientist/SDL pattern)

```
V9-BRAIN (local host)
+-- LLM (ollama/vLLM, Mixtral/Llama/Qwen)       <- "brain"
+-- Planner (agent: servicing tasks, 24/7 schedule)
+-- Tool Bridge (MCP-like: microscope, hands, FOSH, pumps, incubator, robots)
+-- Vision (YOLO + CellPose on Jetson AGX: cell/mitosis/artifact detection)
+-- Flight Recorder (AIS) - log of every action (pose, force, time)
+-- Safety Layer (Body Law: force <=5 N, speed <=200 mm/s, no-touch zones during laser)
+-- Watchdog (device heartbeats, auto-restart, alerts)
```

The LLM never touches tools directly — only through the **Tool Bridge with validation** (ChemCrow pattern: domain-validated external tools against hallucination). Every action passes the Safety Layer before execution.

### 4.4 Why the LLM shares the host with the actuators

1. **Zero latency** brain-to-hand (critical for vision-guided pick-and-place)
2. **Single point of failure** — simpler watchdog, easier debugging
3. **No network dependency** (preprint data never leaves the enclosure)
4. **Cost** — no second server; the AIS dedicated server ($18K/10 yr) stays for the global network, not real-time control
5. **Coscientist pattern** — Planner + Code Execution + Multi-Hardware on one machine

## 5. 24/7 Operating Cycle (hand tasks)

| # | Task | Trigger | Hand |
|---|------|---------|------|
| 1 | Sample exchange (embryo/cassette) | "mitosis complete" from Vision | pick-and-place |
| 2 | Medium replenishment (DMEM/agarose) | every 6 h | pipette tool |
| 3 | Objective cleaning | SNR drop >10% | wipe + immersion |
| 4 | Microinjector capillary replacement | after N injections | capillary holder |
| 5 | Zone UV-C sterilization | between samples | UV tool |
| 6 | Cell-pair separation (OS3) | per experiment plan | rake/scraper |
| 7 | Micro-robot servicing | charging/tools/calibration | gripper |
| 8 | Stage jam recovery | motor release API + hand | gripper-release |
| 9 | Consumable pickup from transfer box | UV-C cycle complete (sensor) | open inner door + pick |
| 10 | Waste removal via transfer box | tray full / protocol end | place + close door |
| 11 | End-effector/spare part replacement | wear/failure/new protocol | via transfer box |

**Escalation rule:** a task goes to the LLM brain first; if confidence <0.7, the task is queued for a human (Telegram/dashboard) while the rest continues.

## 6. AIS Integration

| AIS component | V9 instantiation |
|---------------|------------------|
| Passport | +15 capabilities (pick-and-place, pipette, wipe, UV, capillary, rake, charge, calibrate, transfer-in, transfer-out, door-interlock...) |
| Body Law | force <=5 N, speed <=200 mm/s, no-touch zones around the objective during fs-laser |
| Flight Recorder | every action: pose (x,y,z,theta), force, timestamp, camera frame |
| LLM Bridge | error diagnosis for the hands -> solution -> safe restart |
| Trace Network | "how to clean the 60x/1.2 WI objective", "how to replace a capillary" — procedures in the shared registry |
| Knowledge Field | servicing procedures -> Noepedia claims with verification |

## 7. Budget

### 7.1 V9-Full (OS3) — reference configuration, itemized

| Item | USD | Basis |
|------|----:|-------|
| 2x cable-driven arms | 2,500 | 12x NEMA 17 (~$18 ea), 12x TMC2209 (~$5 ea), encoders, 2x glove-port flanges (~$150 ea, machined), 2x reinforced silicone sleeves (~$100 ea), shafts/pulleys/cables, printed parts |
| End-effectors (6) + tool changer | 1,000 | gripper, pipette (syringe pump), wipe, UV, capillary holder, rake + quick-change mechanism |
| Sensors | 600 | 4x FSR, 2x wrist cameras, door/UV/DP sensors for the transfer box |
| Controllers + CAN bus | 400 | 4x RP2040/ESP32, CAN transceivers |
| PSU + infrastructure | 300 | 24 V supplies, cabling, connectors |
| V9-TRANSFER box | 1,000 | PMMA body, 2 doors + hardware interlock, UV-C 254 nm, HEPA purge, sensors, tray |
| LLM host: Mac Studio M3 Ultra 192GB | 6,400 | ~$6,000 (192 GB unified) + 4 TB NVMe (~$400) for week-long imaging data |
| Software: LLM agent, Tool Bridge, Safety Layer | 3,000 | agent development + integration effort |
| Spare parts | 800 | motors, drivers, end-effectors, sleeves |
| Engineering / assembly / calibration | 3,500 | commissioning, vision calibration, integration |
| Contingency 15% | 2,925 | |
| **V9-Full total (base)** | **~22,400** | |
| + Sterilization set (shared V7/V8/V9) | 12,200 | autoclave 5K + VHP 4K + UV-C 0.3K + ultrasonic 0.3K + transfer boxes 2.3K + indicators 0.3K (STERILIZATION_TRANSFER.md, section 10) |
| **V9-Full total (incl. sterilization)** | **~34,600** | |

Notes:

- The sterilization set is shared across V7/V8/V9; V9-Full requires the VHP generator (ablation/injection workflows), which is already counted there.
- If the OS3 Mac M4 Pro (64 GB, already in the OS3 budget) is retained as the host, the LLM host line drops to ~$400 (NVMe only): base ~$15.5K, incl. sterilization ~$27.7K.
- Reference: commercial glovebox arms alone cost $30-80K. V9-Full (incl. sterilization) is ~$35K and open.

### 7.2 Per-stage budget

| Variant | Stage | Added to stage | USD (base) | USD (incl. sterilization share) |
|---------|:---:|----------------|----:|----:|
| V9-Lite | OS1 | 1 arm + end-effectors + transfer box; LLM on Jetson Orin NX + shared lab host (no new host) | ~5-7K | ~7-9K |
| V9-Standard | OS2 | 2 arms + transfer box; LLM on AGX + shared host | ~11-13K | ~15-17K |
| V9-Full | OS3 | 2 arms + VHP/ultrasonic-ready transfer box + dedicated LLM host | ~22.4K | ~34.6K |

Hardware (arms, end-effectors, controllers) is identical across variants; the delta is the number of arms, the transfer box option, and the LLM host. The sterilization set is one shared purchase per lab (V9-Full is the only variant that mandates VHP).

## 8. Roadmap

Deployment order is per OS stage; V9.0-V9.2 are capability levels that apply to each stage.

| Version | Content | Acceptance criterion | Stage |
|---------|---------|----------------------|-------|
| V9.0 | 1 arm + gripper, teleoperation (remote operator, as in surgery) | slide pickup with ±0.5 mm accuracy | OS1 first (cheapest, fastest proof) |
| V9.1 | 2 arms + vision-guided, semi-autonomous (LLM plans, human approves critical steps) | sample-exchange cycle without touching the enclosure | OS2 |
| V9.2 | Full 24/7 autonomy (LLM brain + Body Law + watchdog) | 72 h without human intervention, zero incidents | OS3 (full set: +VHP/ultrasonic) |

## 9. Risks and Mitigations

| Risk | Mitigation |
|------|------------|
| Sleeve leak | Bubble test, double sleeve, enclosure pressure sensor |
| UV-C degradation of silicone | UV-C-resistant sleeve (EPDM), replacement every 6 months |
| Accuracy over sleeve length | Motor encoders + vision calibration (wrist camera) |
| LLM hallucination | Tool Bridge validation (ChemCrow pattern), Safety Layer, double-check of critical actions |
| Arm jammed/broken inside | Arm removable in ~2 min; operator in gloves (standard V8 mode) |
| Both transfer doors open (loss of containment) | Hardware interlock (both never open), not software |
| UV-C cycle incomplete, inner door opens | Interlock: inner door opens only when UV-C = 0 and DP nominal (sensors) |
| Under-sterilized load enters | Double packaging + in-chamber UV-C + HEPA purge; every entry logged (Flight Recorder) |
| Collision between FOSH manipulator and hands | No-go zone map in config; collisions checked in simulation before execution |

---

*Engineering document. For grants, see CONCEPT.md. V9 = autonomy layer over V7 (OS2) / V8 (OS3).*
