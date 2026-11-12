# ARGUS — Engineering Note: Dark State and Objective-Side Photon Leakage Control

**Version:** 1.0
**Date:** 2026-11-12
**Author:** Jaba Tqemaladze, MD — Georgia Longevity Alliance
**Trigger:** ARGUS requirement FR-7 ("operation in complete darkness with minimal phototoxicity") cannot be met by switching LED drivers off. The imaging path is optically reversible: light admitted anywhere on the objective or camera side reaches the specimen.
**Applies to:** OS1, OS2, OS3 (upright builds) and OS4 (inverted build on the Zeiss IM35 optical core). All numbers below refer to the inverted geometry with a fixed specimen vessel and an objective that moves in XYZ.
**Status:** design note + acceptance procedure. Closes the FR-7 implementation gap; adds **NFR-13**.

> **Status: preliminary draft prepared by PI** (the AI assistant working with J.T.) on 2026-11-12. This is **not** approved engineering documentation. Every dimension, material, part number and control loop must be reviewed, corrected and signed off by the ARGUS engineer before any purchase, machining or firmware commitment.

---

## 1. Purpose and scope

This note defines how ARGUS keeps the specimen in a **verified dark state whenever it is not being imaged**, and how that state is measured rather than assumed.

In scope: every light path that can deliver photons to the specimen plane from the far side of the objective, plus light piping through vessel walls, medium, micropipettes and tubing.

Out of scope: deliberate exposure during acquisition (that is the light budget of FR-7/V3), and the geometry of the culture chamber itself (see the containment note).

---

## 2. Why "LEDs off" is not dark — the arithmetic

The optical train is reciprocal. A photon entering the camera port, the binocular tube, or the open air gap under the coverslip leaves at the specimen plane with the same collection efficiency as an emitted photon travelling the other way.

Illuminance conversion: 1 lux at 555 nm = 1.464 mW/m². Room light at 300 lux is therefore 0.44 W/m² = 44 µW/cm². An objective concentrates an extended source by approximately NA²:

| Objective | Concentration | Irradiance at specimen | Dose over 24 h |
|---|---|---|---|
| 40×/0.95 dry (NA 0.95) | ×0.90 | ≈ 40 µW/cm² | **≈ 3.5 J/cm²/day** |
| 40×/1.25 silicone (NA 1.25) | ×1.56 | ≈ 68 µW/cm² | **≈ 5.9 J/cm²/day** |
| 60×/1.2 water (NA 1.2) | ×1.44 | ≈ 63 µW/cm² | **≈ 5.5 J/cm²/day** |

For comparison, a deliberate acquisition regime of 1 W/cm² for 100 ms, 24 frames/day, is 2.4 J/cm²/day.

**Conclusion.** Uncontrolled room light through the objective is not a nuisance — it is an experiment in phototoxicity running in parallel, of the same order of magnitude as the intended exposure, for months. Because room light is broadband, the fraction in the 400–500 nm band carries the highest per-joule risk (Icha et al., *BioEssays* 2017, PMID 28749075), so the blue band must be measured separately.

---

## 3. The five leakage channels

| # | Channel | Mechanism | Typical magnitude |
|---|---|---|---|
| L1 | Open air gap under the coverslip | Inverted objective leaves an annular gap of 0.13–0.3 mm between the front lens and the 170 µm coverslip, open to the room on all sides | dominant |
| L2 | Reverse path through the camera | C-mount/M42 thread gaps, camera body vents or fan, uncapped binocular tube (a direct light pipe into the specimen) | dominant if uncapped |
| L3 | Vessel walls and medium | Transparent plastic/glass walls and the medium column act as a light guide, delivering room light into the field of view | moderate |
| L4 | Micropipettes and tubing | A glass capillary is an optical fibre; PTFE/FEP perfusion tubing is a light guide; light enters at the free end and exits in the medium | moderate |
| L5 | Active sources inside the enclosure | NIR illumination for the internal awareness cameras (FR-8), NIR autofocus beam, indicator LEDs on devices inside the enclosure | continuous |

The failure mode is not bulk attenuation but a **single direct line of sight**. A black anodised box with one open thread is optically equivalent to no box at all.

---

## 4. Design principle: one or two optical apertures, everything else opaque

| Element | Rule |
|---|---|
| Vessel | Exactly **one** permanent optical aperture — the 170 µm glass bottom. Walls, lid and ports opaque (black POM/PEEK, matte black). A second aperture (top window for transmitted-light brightfield) is permitted only with its own shutter and is opaque by default |
| Objective | Sits inside a **light-tight dark cell**: opaque shroud from the fixed vessel holder to the moving carriage, closed by an opaque bellows, with a light-trap labyrinth at the moving edge |
| Epi path | **Normally-closed mechanical shutter** (spring-closed solenoid) + independent driver enable line + TTL. Park position carries a blocking flag/ND. Three independent means, because a TTL-off LED driver is a single point of failure |
| Camera | In its own light-tight mini-box; flock-lined M42→C-mount adapter with O-ring; **binocular/eyepiece tube capped** with a matte black insert |
| Transmitted light | LED panel above the vessel with its own shutter; off and shuttered by default |
| Pipettes / tubing | Capillary shank shrouded or blackened except the last 2–3 mm; perfusion lines opaque (black FEP/PEEK) |
| Internal awareness cameras | NIR illumination baffled away from the vessel, 940 nm, power-limited and gated; must not raise specimen-plane irradiance above NFR-13 |
| Autofocus | No continuous NIR beam. Gate the focus beam to focus checks only, ≤1–10 µW at the specimen, 850 nm (not 980 nm — water absorption peak, heating), or use image-based autofocus on acquisition frames only |

```
     [ white LED ]  ← shutter + enable line, normally closed
          ▼        (top aperture: open only during label-free acquisition)
   ╔══════════════════════════════════════════╗
   ║  VESSEL — opaque walls/lid/ports          ║
   ║  medium · cells · pipette tips            ║
   ╚═══════════════════╤══════════════════════╝
                       │  aperture #1 = 170 µm glass bottom
        ┌──────────────┴──────────────┐
        │  DARK CELL (light-tight)    │  black anodised shell + flock
        │  objective + 2 Fi reflector │  opaque bellows on the XYZ carriage
        │  epi LED engine + shutter   │  light guide into the reflector
        └──────────────┬──────────────┘
                       ▼  flock-lined M42 adapter, O-ring
                 [ camera in light-tight mini-box ]
```

**Why the bellows is mandatory.** The objective must translate in XYZ while the vessel stays fixed (fixed-specimen geometry). A sliding seal is not light-tight; an opaque bellows is. For silicone immersion the requirement is stricter still, because the immersion film couples sideways light into the objective cone.

---

## 5. Requirements (new NFR-13)

| ID | Requirement | Value | Verification |
|---|---|---|---|
| NFR-13.1 | No direct line of sight from the room to the specimen through any path other than a shuttered aperture | 0 such paths | Visual + leak-map test (D1) |
| NFR-13.2 | Attenuation of every non-imaging path | **OD ≥ 4** (≥10⁴) | Leak-map with known external illuminance (D1/D2) |
| NFR-13.3 | Leakage irradiance at the specimen plane, 400–700 nm | **≤ 0.5 µW/cm²** (≤0.043 J/cm²/day, ≤1 % of imaging dose) | Photodiode, 24 h log (D4) |
| NFR-13.4 | Same, 400–500 nm band | **≤ 0.1 µW/cm²** | Photodiode + blue filter (D4) |
| NFR-13.5 | Default state | Shutters normally closed; darkness on power loss, watchdog trip or process crash | Power-cut test (D3) |
| NFR-13.6 | Continuous monitoring | Photodiode at the specimen plane, 10 s logging of µW/cm² and cumulative J/cm²; alarm above threshold | Log audit (D4/D5) |
| NFR-13.7 | Anomaly traceability | Any shutter open outside an active exposure is an anomaly event in the Flight Recorder | Event injection test |

**FR-7 restated (measurable).** Light reaches the specimen only while an exposure is active. At all other times the dark state is *verified* by NFR-13.3/13.4, and the cumulative dose is logged continuously. "Image on demand" becomes an auditable property, not an intention.

**FR-8 addition.** NIR illumination for internal cameras and any NIR source inside the enclosure must not raise the specimen-plane irradiance above NFR-13.3/13.4 at any duty cycle.

---

## 6. Acceptance procedure — "dark test" (V8e)

**Rig.** Replica vessel: a light-tight chamber with a calibrated photodiode (BPW34, transimpedance amplifier) mounted under a 170 µm coverslip at the specimen plane, same objective, same nosepiece, same carriage position.

| Step | Action | Output |
|---|---|---|
| D1 | External illuminance 300–500 lux; all ARGUS sources off; shutter closed. Single 60 s frame at maximum gain and no gain offset | **Leak map**: bright regions locate the offending seam (typical: camera flange, bellows edge, septum port gland) |
| D2 | Reciprocity check: place a calibrated LED at the camera port, then at the binocular port; measure at the specimen plane | Transmission of each reverse path; confirms that a single external-source test covers both directions |
| D3 | Cut power to the shutter driver and to the LED drivers | Shutter closes; leakage unchanged from D1; camera exposure not required |
| D4 | 24 h photodiode log, with and without the blue bandpass filter | µW/cm² (total and blue), J/cm²/day; compare with NFR-13.3/13.4 |
| D5 | 14-day combined test at 37 °C, RH ≥ 90 % in the closed vessel, dry zone with desiccant | No condensate artefacts (NFR-8) and leakage stable over 14 days (NFR-13) |
| D6 | Repeat D4 with NIR awareness illumination and autofocus active | Confirms NFR-13.7 / FR-8 addendum |

**Pass criterion.** NFR-13.1…13.7 all met; leak map free of hot spots; 14-day log without a single excursion.

---

## 7. Bill of materials (indicative, 2026)

| Item | Purpose | Cost, USD |
|---|---|---|
| Opaque bellows, 60–100 mm ID, black rubberised fabric | light-tight XYZ carriage | 40–150 |
| Matt black flock sheet (Acktar / ProStar / Edmund class) | shroud lining, thread sealing | 40–80 |
| 2× normally-closed solenoid shutter + controller | epi path, transmitted path | 150–250 |
| BPW34 photodiode + TIA + ADS1115 + ESP32 logger | continuous dose monitor | 30–50 |
| Black POM/PEEK sheet for vessel walls and lid | removes light piping (L3) | 20–40 |
| Black heat-shrink for capillary shanks | removes pipette light guide (L4) | 5–10 |
| Opaque FEP/PEEK tubing | perfusion lines | 20–40 |
| Black anodised mini-box for camera | reverse path (L2) | 40–80 |
| Matte black paint / flocked caps for open ports | binocular, optovar, spare ports | 10–20 |
| **Total** | | **≈ 350–720** |

---

## 8. Limitations, stated honestly

1. Zero photons is impossible during acquisition; NFR-13 constrains *all other time* and makes the total dose auditable.
2. The NA² concentration model is an order-of-magnitude estimate; the leaked irradiance must be measured (D1/D4), not computed.
3. Opaque vessel walls reduce unaided visual inspection through the wall; the internal awareness cameras (FR-8) compensate, but their own NIR illumination becomes a leakage source and must be gated (L5).
4. Silicone immersion improves resolution over months but couples sideways light into the objective cone; the bellows is then not optional.
5. A photodiode at the specimen plane occupies the field; it is a test rig, not a permanent component. For long-term operation the monitor sits beside the field at a calibrated position, and the calibration is repeated at each service.
6. This note does not remove the need for the light-budget measurement V3; it only guarantees that the *unintended* part of the dose is bounded and logged.

---

## 9. References

1. Icha J, Weber M, Waters JC, Norden C. Phototoxicity in live fluorescence microscopy, and how to avoid it. *BioEssays* 2017. PMID 28749075 — dose framework used here.
2. Chiou PY, Ohta AT, Wu MC. *Nature* 2005;436:370 — OET light-dose constraint inherited by OS4 (projector path is a sixth, deliberate leakage source during manipulation).
3. ARGUS TRD v0.9b §5 (NFR), §12 (humidity/condensation), §7 (verification plan) — updated by this note.
4. Zeiss IM 35 / ICM 405 operating manual (RU translation in the project archive) — nosepiece-carriage focusing, M42×0.75 photo port, 2 Fi reflector housing under the nosepiece.

---

*Companion documents: ARGUS_EngineeringNote_TwoZoneContainment_2026-11-12.md (closed-vessel containment, fixed specimen, objective XYZ), ARGUS_EngineeringNote_IM35_EpiLED_2026-10-22.md, ARGUS_EngineeringNote_TubeLens_60x_2026-10-22.md, ARGUS_Optics_Selection_Criteria_2026-10-22.md, docs/internal/ARGUS_DarkState_brief_AZIZA_2026-11-12_RU.md (work order, private).*
