# ARGUS — Engineering Note: Two-Zone Containment and Fixed-Specimen (Objective-Scanning) Geometry

**Version:** 1.0
**Date:** 2026-11-12
**Author:** Jaba Tqemaladze, MD — Georgia Longevity Alliance
**Trigger:** Long-term (months) culture in a sealed enclosure cannot be reconciled with a heavy, humid, 37 °C box wrapped around a whole microscope: condensation, mould, thermal drift, camera access and manipulator access all fail at once. At the same time the specimen vessel must not be moved, because cell identity is assigned by position.
**Applies to:** OS1–OS3 (upright) and OS4 (inverted, Zeiss IM35 optical core). The inverted case is worked out in detail because it is the binding one.

> **Status: preliminary draft prepared by PI** (the AI assistant working with J.T.) on 2026-11-12. This is **not** approved engineering documentation. Every dimension, material, part number and control loop must be reviewed, corrected and signed off by the ARGUS engineer before any purchase, machining or firmware commitment.
**Companion:** `docs/ARGUS_EngineeringNote_DarkState_2026-11-12.md` (NFR-13), `docs/ARGUS_TRD_v0.9b.md` §3, §5, §12.

---

## 1. Decision

Two changes of principle, both of which remove whole classes of requirements:

1. **The humid, warm, sterile volume is the vessel — not the enclosure.** ARGUS runs a **closed perfusion chamber** (170 µm glass bottom, opaque walls, lid with a small optical window and septum ports). The enclosure around the microscope becomes a **dry** thermal and dust shield.
2. **The specimen is fixed; only the objective moves (XYZ).** The vessel is held rigidly for the whole run. Focus is driven by the objective carriage, which on the IM35 already exists: the coarse/fine focus moves the nosepiece carriage, while the stage is fixed.

Consequence that carries the rest of the design: **the 170 µm coverslip is the only permanent optical boundary between the wet and the dry side.** No window in a box wall is needed, no camera window heating, no desiccated sensor chamber beyond a small dry box around the camera.

---

## 2. Why this is the right decomposition

| Requirement | Box-around-the-microscope | Two-zone (closed vessel + dry enclosure) |
|---|---|---|
| NFR-3 environment (37 °C, 5 % CO₂, RH ≥ 90 %) | entire enclosure volume: slow response, litres of gas per hour, heavy condensation load | vessel only, ≈0.5–1 mL: minutes to equilibrate, gas demand negligible; CO₂ can be dropped entirely (see §5) |
| NFR-8 condensation on optics | dew point 35 °C at 37 °C/90 % RH — every surface colder condenses; camera, sensor, objective at risk | cold optics live in dry air; the only water-facing surface is the coverslip, whose underside is in the dry zone |
| NFR-7 optical drift | thermal bridges through the box wall, stage and vessel both drift | one metrology loop: vessel ↔ objective carriage |
| FR-12 no perturbation of tracked cells | moving stage, moving vessel, sloshing medium | nothing moves but the objective |
| Camera serviceability / replacement | camera inside, sealed, humid | camera outside on the M42 port, in a dry mini-box; swap never touches the specimen |
| Sterility (FR-9) | must be maintained for a 100-litre volume | maintained by one small closed chamber with two Luer ports and two septum ports |
| BSL-2 secondary containment | box does double duty, compromised by both roles | vessel = primary containment; dry enclosure = secondary |

---

## 3. Geometry

```
        [ white LED panel, diffuse ]  ← outside the vessel, shuttered (NFR-13)
                    ▼
   ┌──────────────────────────────────────────┐
   │ CLOSED VESSEL     37.0 ± 0.3 °C          │   opaque walls (black POM/PEEK)
   │  170 µm glass bottom  ·  medium 1–2 mm   │   lid: 10–12 mm optical window
   │  2 septum ports @45° for micromanipulators│  + 2 Luer (perfusion in/out)
   └───────────────────┬──────────────────────┘
                       │  APERTURE = coverslip (only permanent optical path)
        ┌──────────────┴───────────────┐
        │ XYZ OBJECTIVE CARRIAGE        │   X/Y: stepper, closed loop, ±6–8 mm,
        │  objective + 2 Fi reflector   │        step ≤100 nm (NFR-1)
        │  (epi light via light guide)  │   Z: piezo, 100 µm travel
        └──────────────┬───────────────┘
                       ▼  fixed tube optics of the IM35, M42×0.75 port
                [ camera in dry mini-box ]      ← fixed, outside, replaceable

   DRY ENCLOSURE (optional): dry air, desiccant, 24–30 °C, opaque (NFR-13)
```

Numbers that matter:

- **IM35 is finite-conjugate (160 mm tube).** A transverse (X/Y) shift of the objective changes neither focus nor magnification; only the viewed field moves. This is why objective scanning is safe on this frame, and why the camera can stay bolted to the body.
- **Image-side NA at the M42 port** ≈ NA_objective / magnification ≈ 0.95 / 32 ≈ 0.027 (f/18). A 1 mm plane-parallel window anywhere near that port costs ≈ λ/10, so even if the camera needs its own sealed box with a window, resolution is unaffected. (The "window must sit in infinity space" rule applies to high-NA spaces, not to this port.)
- **Travel.** FR-4 keeps exactly two studied cells in the field, so full-area scanning is not required. X/Y travel covers (a) the post-seeding survey and (b) re-framing as fibroblasts crawl (V1). ±6–8 mm with a closed-loop stepper is enough; piezo Z provides the nm-scale focus.

---

## 4. What must and must not move

**Moves (single carriage):** objective + epi reflector housing (2 Fi). Illumination follows the field, so uniformity is preserved across the vessel.

**Does not move:** vessel, vessel holder, perfusion lines, septum seals, transmitted-light panel, tube optics, camera.

**Epi light delivery:** the LED engine stays off the carriage and feeds the reflector through a **liquid light guide or fibre bundle**. A bundle is acceptable here and only here — it is in the illumination path, where it merely scrambles light; in the imaging path it would cost resolution.

---

## 5. Medium and gas: the option that removes CO₂ and humidity control

If V6 shows that the cells tolerate it, ARGUS runs a **CO₂-independent, HEPES- or L-15-buffered medium with continuous perfusion** (0.5–2 mL/day). Then:

- no CO₂ supply, no gas mixing, no humidity control, no evaporative osmolarity drift (the chamber is closed);
- NFR-3 reduces to "specimen temperature 37.0 ± 0.3 °C";
- NFR-8 reduces to "no condensate on the coverslip underside", which is automatic because that surface faces dry air.

This is a **biological** decision, not an engineering one, and it must be closed by V6 (proliferation vs control over ≥7 days). Until V6 reports, the CO₂ variant remains the baseline and the two-zone layout is unchanged — only a gas line is added through a filtered port.

---

## 6. Thermal design (the part that decides success over months)

1. Heat the vessel **from the sides and the lid**, never from below. A heater under the coverslip bows the 170 µm glass and produces micrometre-scale focus drift; that failure mode is silent and looks like "autofocus is bad".
2. Measure temperature **in the medium**, not on the holder.
3. Keep the metrology loop short: vessel holder and objective carriage mounted on the same rigid block (aluminium; Invar insert if drift data demand it). Any thermal expansion between holder and carriage appears directly as defocus.
4. Dry side: 24–30 °C, desiccant, RH < 40 %. This keeps the objective front lens and the camera well above any dew point that could exist in that compartment.
5. Immersion: for months, **silicone oil** (40×/1.25 class) rather than water or oil — it neither evaporates nor creeps. Silicone is compatible with a parked objective; it is not compatible with large X/Y excursions, which is consistent with §3 (travel is only for survey and re-framing). A dry 40×/0.85–0.95 sits on the same nosepiece for survey work — switching objectives happens in the dry zone and does not breach the vessel.

---

## 7. Verification (extends V8)

| ID | Test | Output | Closes |
|---|---|---|---|
| V8a | X/Y metrology of the objective carriage | repeatability, step, hysteresis, backlash | NFR-1 |
| V8b | Z drift over 72 h, side heating vs bottom heating | µm/h and correlation with temperature | NFR-7 |
| V8e | Dark state / leakage (`DarkState` note) | leak map, µW/cm², J/cm²/day | FR-7, NFR-13 |
| **V8f** | **Closed-vessel stability**: 14 days at 37 °C, perfusion running, no CO₂ (option) | focus drift, condensate on coverslip underside, osmolarity proxy (volume loss), contamination | NFR-3, NFR-8, FR-6, FR-9 |
| **V8g** | **Objective-scanning invariance**: magnification and parfocality vs X/Y position over the full travel | % magnification change, µm focus change | NFR-1, FR-12 |
| V6 | Medium/buffering: CO₂-free perfusion vs control, 7 days | proliferation ratio | §5 decision |

---

## 8. Requirement deltas

| Item | Change |
|---|---|
| TRD §3.1 item 1 | enclosure requirement restated: **closed vessel** carries environment; enclosure is dry |
| NFR-3 | add variant "CO₂-free closed chamber + perfusion" (validation V6); temperature unchanged at 37.0 ± 0.3 °C at the specimen |
| NFR-8 | restated: no condensate on the coverslip underside or on dry-zone optics for ≥14 days; sensor-chamber desiccation remains, camera-window heating becomes optional |
| NFR-7 | drift budget now belongs to a single loop (holder ↔ objective carriage); steady-state autofocus still required |
| FR-12 | strengthened: nothing but the objective moves |
| New | V8f, V8g verification rows (§7 above) |

---

## 9. Bill of materials (indicative, 2026)

| Item | Purpose | USD |
|---|---|---|
| Closed chamber: black POM body, 170 µm glass bottom, lid with 10–12 mm window, 2 septum + 2 Luer ports | containment, single optical boundary | 250–500 (machined) |
| X/Y closed-loop carriage for the objective (stepper, ±8 mm, ≤100 nm step) | fixed-specimen scanning | 400–1,200 |
| Piezo Z (objective) | nm focus | 1,500–3,000 (deferrable: stepper first) |
| Side/top heating + PID + thermistor in medium | 37.0 ± 0.3 °C without bowing the coverslip | 150–300 |
| Perfusion: 2 syringe pumps or a peristaltic + black FEP lines | media change, osmolarity | 300–900 |
| Silicone-immersion objective 40×/1.25 (optional, OS4 slot A6) | high NA over months | 3,000–5,000 (used market) |
| **Total, minimum viable** | | **≈ 1,100–2,900** |

---

## 10. Open items and limitations

1. **Cell migration vs a fixed vessel.** Fibroblasts crawl (V1). The field must follow them, therefore X/Y on the objective is not optional — it is the mechanism that reconciles "vessel untouched" with "cells move".
2. **Silicone immersion and X/Y travel** are mutually limiting; the survey/re-frame split in §3 handles it, but it must be verified (V8g) rather than assumed.
3. **Immersion over months** is the least proven element of the whole design. If it fails, resolution falls back to dry 0.95 NA (≈0.33 µm PSF) and the centriole readout relies on marker SNR and sub-pixel centroiding — a question for V3, not for the engineer.
4. **Closed chamber with perfusion** creates its own risks: bubble trapping at the septum, medium ageing, waste accumulation. V8f/V6 cover them.
5. This note does not select the removal method (FR-5) or the manipulator model; it only fixes the geometry those devices must live with.

---

## 11. References

1. Zeiss IM 35 / ICM 405 operating manual (RU translation, project archive) — nosepiece-carriage focusing, fixed stage, M42×0.75 photo port, 2 Fi reflector housing under the nosepiece, finite 160 mm tube.
2. Collins JT et al. OpenFlexure Microscope. *Biomed Opt Express* 2020;11:2447 — open frame baseline for the upright variants.
3. ARGUS TRD v0.9c §3, §5, §7, §12; PARAMETERS.md (dark state block).

---

*The chamber itself (dimensions, materials, bonding, sterilization, BOM) is specified in `ARGUS-OS4/hardware/chamber/CHAMBER_SPEC.md` with drawing `drawings/ARGUS_chamber_revA.pdf` (A3, 1:1).*

*Companion: `docs/ARGUS_EngineeringNote_DarkState_2026-11-12.md`. Work order for the engineer (private, Russian): `docs/internal/ARGUS_DarkState_brief_AZIZA_2026-11-12_RU.md`.*
