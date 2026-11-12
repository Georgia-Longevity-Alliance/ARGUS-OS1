# ARGUS — Engineering Note: Inverted Optics Everywhere, Dry Objectives over Aqueous Medium, Dual-Camera Head and In-Enclosure Cameras

**Version:** 1.0
**Date:** 2026-11-12
**Author:** Jaba Tqemaladze, MD — Georgia Longevity Alliance
**Decision recorded here:**
1. **All ARGUS stages are inverted.** OS1–OS3 upright variants are withdrawn; the inverted geometry is the platform, not an option.
2. **No immersion.** The specimen is in aqueous medium; the objective works **dry** against a 0.17 mm coverslip. Water/oil immersion is out of scope, permanently.
3. **Binocular viewing is realised with two cameras** on a split head (no eyepieces).
4. **In-enclosure cameras**: general-view cameras plus NIR night-vision cameras, gated by NFR-13.

**Related:** `docs/ARGUS_EngineeringNote_TwoZoneContainment_2026-11-12.md`, `docs/ARGUS_EngineeringNote_DarkState_2026-11-12.md`, `hardware/chamber/CHAMBER_SPEC.md`, `docs/ARGUS_TRD_v0.9b.md`.

> **Status: preliminary draft prepared by PI** (the AI assistant working with J.T.) on 2026-11-12. This is **not** approved engineering documentation. Every dimension, material, part number and control loop must be reviewed, corrected and signed off by the ARGUS engineer before any purchase, machining or firmware commitment.

---

## 1. Why inverted, and what "water, not immersion" means

The specimen sits in a closed chamber with a 170 µm glass bottom. The objective looks up from below, dry, through air and then through the coverslip into the aqueous medium. This is the standard configuration of every inverted cell-culture microscope, and it carries three consequences that are worth stating explicitly, because two of them are constraints and one is a trap.

| Consequence | Value |
|---|---|
| Working distance needed | ≥ 0.13 mm (the objective never touches liquid; the coverslip is the only interface) |
| Immersion artefacts | none: no oil film, no water evaporation, no immersion dispenser, no cleaning between objectives — this is why the configuration is right for months |
| Coverslip specification | No. 1.5H, 0.17 ± 0.005 mm, flatness λ/4 per 10 mm, low autofluorescence. Thickness tolerance matters: a 0.21 mm coverslip on a 0.95 NA objective costs measurable spherical aberration |
| Maximum dry NA | ≈ 0.95 (aplanatic dry, with correction collar 0.11–0.23 mm) |
| **The trap** | With no immersion, the best lateral PSF is **0.33 µm** at 520 nm — not 0.25 µm. See §2 |

The objective must have a **correction collar**, because the chamber's coverslip-plus-medium stack and small thickness variations otherwise leave residual spherical aberration at NA > 0.8.

---

## 2. Resolution: what "no immersion" costs, and the honest way to get it back

| Objective (dry) | NA | Lateral PSF @520 nm | Axial FWHM | Sampling with a 3.45 µm pixel | Object field (1" sensor) |
|---|---|---|---|---|---|
| 4×/0.13 | 0.13 | 2.4 µm | 18 µm | 0.86 µm | 3.3 × 2.2 mm |
| 10×/0.30 | 0.30 | 1.06 µm | 3.4 µm | 0.35 µm | 1.3 × 0.9 mm |
| 20×/0.75 | 0.75 | 0.42 µm | 1.1 µm | 0.17 µm | 0.66 × 0.44 mm |
| **40×/0.95 (corr.)** | **0.95** | **0.33 µm** | **0.7 µm** | **0.086 µm** | **0.33 × 0.22 mm** |
| 40×/0.95 + SIM (2×) | — | **0.17 µm** | 1.4 µm | — | 0.33 × 0.22 mm |

Two centrioles of one pair sit roughly 0.3–0.5 µm apart. At 0.33 µm PSF they are **not** optically separated; the readout then rests on marker SNR and sub-pixel centroiding (V3), not on optical resolution. This is a scientific consequence of the no-immersion decision and must not be papered over.

**The route back to <0.3 µm without immersion is structured illumination**, and ARGUS already owns the hardware for it: the OET projection module (DMD, Mightex Polygon1000 class) can generate the three-angle/three-phase fringe patterns. Linear SIM yields 2× lateral improvement → ≈0.17 µm, i.e. the resolution that was wanted from a 60×/1.2 water objective, obtained dry and without touching the specimen. The cost is a z-sectioning scheme with 9 frames per plane and a modest dose — which lands directly in the light-budget question (FR-7/V3), so SIM is an **extension slot**, not a baseline item.

---

## 3. "Binocular" with two cameras — what is and is not possible

A compound microscope's binocular head splits **one** objective image into two eyepieces. Both eyes receive **identical** images: there is no parallax, and stereopsis is essentially zero; depth perception comes from accommodation and from focusing, not from disparity. Therefore:

| Requested | Reality | Implementation |
|---|---|---|
| Two simultaneous views, two operators or two displays | achievable exactly | 50/50 splitter to two identical camera ports |
| Two colour channels simultaneously (488 / 561) | better than a 50/50 split | dichroic splitter (e.g. 560 LP) + two cameras, no filter wheel, no temporal offset |
| Full light to one camera when needed | achievable | motorised **flip mirror** ahead of the splitter: 100 % to port A, or split A/B |
| True stereo depth | **not** achievable through one objective | see §3.2 |

### 3.1 Dual-camera head (baseline)

```
   IM35 tube optics (finite 160 mm, fixed)  →  M42×0.75 photo port
                                                   │
                                   ┌───────────────┴───────────────┐
                                   │  motorised flip mirror        │
                                   │   (100 % A  |  split A+B)     │
                                   └───────┬───────────────┬───────┘
                                   100 %   │               │  dichroic 560 LP
                                           ▼               ▼
                                    [ camera A ]     [ camera B ]
                                    science path     second channel / second view
```

- **Camera A** bolts directly to the M42 port: the science channel (highest SNR, tightest parfocal tolerance).
- **Camera B** sits behind the splitter. For the "second eye" use, a **1:1 relay** (2f–2f, matched doublets or two 50 mm C-mount lenses) keeps magnification identical to port A; for the "second channel" use, drop the relay and put the emission filter in front of B.
- Parfocality: shim each port once (C-mount 17.526 mm baseline), verify with a USAF target; the objective is the only moving element, so the ports never need re-shimming during a campaign.
- Photon budget: a 50/50 split halves the signal on each camera; a dichroic split sends ≈90 % of each band to its own camera. Default to the dichroic; use 50/50 only for the two-operator view.
- Registration: if both cameras view the same field (not two channels), keep one as master and confirm alignment by cross-correlation on a fixed fiducial (part of V8h).

### 3.2 Why a real stereo pair is the wrong tool here (numbers)

A stereo pair needs two viewpoints. Through one coverslip the baseline is limited by the oblique angle an objective tolerates: at a 5° half-angle and 15 mm working distance the baseline is 2 × 15 × tan 5° ≈ **2.6 mm**. With 20× sampling (0.35 µm/pixel) the depth resolution is

Δz ≈ s · z / b = 0.35 µm × 15 mm / 2.6 mm ≈ **2.9 µm** per pixel of disparity.

For cells that are 10–20 µm thick and a focal plane that must hold to ≈0.5 µm, that is useless. **Depth comes from a Z-stack plus autofocus** (0.1–0.3 µm steps, the piezo Z that is already in the BOM), not from stereo. A genuine stereo view remains available cheaply as a separate low-magnification module (two 4×/0.13 objectives, 20 mm baseline, WD 30 mm, ≈4 µm depth resolution) if a "3D feel" for the workspace is ever wanted for the operators — it is an accessory, not a replacement for the science path.

---

## 4. Cameras inside the enclosure

Two families, both mounted on the enclosure frame and **outside** the dark cell:

| Camera | Purpose | Spec | Placement |
|---|---|---|---|
| General view ×2 (visible, wide) | workspace awareness, manipulator and tubing positions, 3D map (FR-8) | 1/1.8" colour CMOS, 16 mm lens → ≈100 mm field at 300 mm; global shutter preferred | two corners of the enclosure, ~45° to the stage, 250–350 mm from the chamber |
| Night vision ×2 (NIR) | operation with all visible light off (FR-7) | 1/1.8" mono, IR-cut filter removed, 850/940 nm illuminator, ≤0.001 lux, 30 fps | same corners, interleaved with the visible cameras, aimed at the workspace not at the chamber aperture |

**Dark-state interaction (NFR-13).** Night-vision operation is safe *by construction* in the two-zone design: the chamber walls are opaque and the only optical path is the bottom coverslip, which is enclosed in the dark cell. Three residual leaks must still be closed:

1. The septum membranes and O-rings must be **black** silicone; translucent silicone pipes NIR into the medium.
2. The lid window needs an **opaque flap** (not just a shutter): a 1 mm black flap closed by default, opened only for transmitted-light acquisition.
3. The night illuminators must be baffled so that no direct path exists to the coverslip plane; verify with the photodiode of NFR-13.2 (step D6 of the dark test) rather than by reasoning.

Sync: all cameras share the acquisition host clock; night frames are timestamped against the science frames so that a manipulation can be reconstructed against the lineage log (Flight Recorder).

---

## 5. Requirement deltas

| ID | Requirement |
|---|---|
| FR-14 (new) | **Dual-view head**: two camera ports, switchable 100 %/split; simultaneous dual-channel acquisition without a filter wheel; per-port parfocality ≤ ±2 µm |
| FR-15 (new) | **In-enclosure awareness**: ≥2 visible cameras + ≥2 NIR night cameras; workspace coverage ≥ 90 % of the manipulation volume; NIR contribution to the specimen plane within NFR-13 |
| NFR-13 addendum | Night-vision illumination, septum membranes and the lid window are part of the leakage budget; opaque seal materials are mandatory |
| Geometry (all stages) | inverted; dry objectives with correction collar; No. 1.5H coverslip; no immersion anywhere |
| Extension slot | SIM via the OET DMD → 0.17 µm lateral, dry |
| V8h (new) | dual-port parfocality, magnification match, channel registration |
| V8i (new) | awareness camera coverage, NIR leakage (D6), timestamp alignment |

---

## 6. Bill of materials (indicative, 2026)

| Item | USD |
|---|---|
| Motorised flip mirror + 50/50 cube + dichroic 560 LP (M42-compatible) | 900–1,800 |
| Second science-class camera (identical to A, for shim simplicity) | 1,100–6,000 |
| 1:1 relay pair for port B (two matched 50 mm C-mount lenses + mounts) | 300–700 |
| Correction-collar dry objectives: 10×/0.30, 20×/0.75, 40×/0.95 | 2,000–6,000 (used market lowers this) |
| No. 1.5H high-precision coverslips (pack of 100) | 60–120 |
| General-view cameras ×2 with 16 mm lenses | 300–600 |
| NIR night cameras ×2 (IR-cut removed) + 850/940 nm illuminators + baffles | 400–800 |
| Black silicone septa / O-rings / opaque flap | 60–120 |
| **Total** | **≈ 5,200–16,100** |

---

## 7. Limitations

1. No immersion caps the PSF at 0.33 µm; SIM is required to go below, and SIM multiplies the light dose — the trade-off belongs to V3.
2. Two cameras on a splitter do not double information unless they receive different bands; the "second eye" is a convenience, not a measurement.
3. Night-vision cameras see the workspace, not the specimen; the specimen stays dark by design, which is the point.
4. The IM35 head is finite-conjugate; the second port needs a relay, which costs a little resolution. Keep port A direct.
5. Correction collars must be reset after any coverslip lot change; log the setting in the Flight Recorder per campaign.

---

*Companion notes: TwoZoneContainment (geometry, containment), DarkState (NFR-13), CHAMBER_SPEC (the vessel).*
