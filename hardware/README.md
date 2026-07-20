# ARGUS-OS1 — Hardware

This directory contains STL files, FreeCAD models, and electronics schematics for the ARGUS-OS1 robotic microscope platform.

## Platform Versions (hardware)

| Version | Base | Objective | Laser | Enclosure | Status |
|:-------:|------|-----------|:-----:|-----------|:------:|
| **v1.0** | OpenFlexure v6.1.5 | 60×/1.2 NA WI | ❌ | Standard CO₂ incubator (HEPA H13) | 🎯 First grant |
| **v2.0** | OpenFlexure v6.1.5 + mods | 60×/1.2 NA WI | ✅ NIR 800 nm fs | Glove-box (37°C, 5% CO₂, 2% O₂, HEPA H13, UV-C) | Future grant |

> **v1.0 = first grant.** No laser. No ablation. No micromanipulators. Sister isolation via CYTOO micropatterned islands. LED 488 nm for fluorescence excitation only.
>
> **v2.0 = future.** Adds femtosecond laser for ablation, glove-box enclosure with night vision, internal storage, and cooled sCMOS. Requires separate grant (EIC Pathfinder WP2).

## ARGUS v1.0 Hardware

Based on [OpenFlexure Microscope](https://openflexure.org/) v6.1.5 with:
- **Water immersion objective** — 60×/1.2 NA, capillary-fed
- **Fluorescence** — LED 488 nm excitation + emission filters (Centrin1-GFP, H2B-GFP)
- **Camera** — RasPi Camera HQ (12.3 MP IMX477). Fallback: ZWO ASI183MM Pro cooled sCMOS (+$1,800)
- **Brain** — Jetson Orin NX 16GB (CellPose, deconvolution, tracking) + RasPi 5 (microscope control)
- **Sister isolation** — CYTOO 2-cell micropatterned islands (fibronectin, PEG borders). NO micropipette.
- **Climate** — Standard CO₂ incubator (Binder CB 60 / Thermo HeraCell), 37°C, 5% CO₂, HEPA H13
- **O₂ control** — 5% via N₂ purge + LuminOx sensor
- **Night vision (standard)** — IR LED (850 nm) + RasPi Camera NoIR inside incubator for 24/7 monitoring without phototoxicity. IR does not excite GFP, zero photodamage. Allows checking cell morphology, confluency, and microscope alignment between fluorescence acquisitions without opening the incubator door.

## ARGUS v2.0 (planned)

Adds to v1.0:

### Glove-box enclosure
- **Dimensions (internal):** ~50 × 50 × 60 cm (W × D × H) — enough for OpenFlexure (~20×20×25 cm) + both hands manipulating freely
- **Material:** acrylic or polycarbonate panels, sealed with silicone gaskets
- **Gloves:** arm-length neoprene/rubber, mounted in front panel. Reach every corner of the box.
- **Access port:** small airlock (20×20×20 cm) for introducing items without breaking atmosphere
- **Climate:** 37°C, 5% CO₂, 2% O₂, HEPA H13 filtration, active circulation — same biosafety level as v1.0 incubator
- **Sterilisation:** internal UV-C lamp (254 nm, timer-controlled, interlocked — shuts off when gloves are in use). Pre-run sterilisation cycle before experiment start.

### Internal storage
 Shelves and drawers mounted on side and back walls:
- **Upper shelf:** CYTOO coverslips, Petri dishes (35 mm, 60 mm), pipette tips (P10, P200, P1000)
- **Middle shelf:** small reagents — PBS (50 mL), trypsin (10 mL), fixation solution (4% PFA, 15 mL), immersion water
- **Lower drawer:** spare objectives, lens wipes, forceps, parafilm
- **Wall rack:** pipettes (P10, P200, P1000), marker pen, lab tape
- Everything accessible with gloved hands without opening the box. Reduces door openings from ~3/day to ~1/week.

### Night vision (standard in v2.0)
- **IR LED array** (850 nm, 4× emitters, adjustable power) — illuminates the entire box interior
- **2× RasPi Camera NoIR** — positioned for:
  - Camera A: microscope stage area (check objective, sample, focus drift)
  - Camera B: storage/workspace area (check reagent levels, locate tools)
- **Why IR:** completely invisible to cells. Zero phototoxicity. Does not excite GFP, Centrin1-GFP, H2B-GFP, or any fluorescent probe. 850 nm is safely outside all fluorophore excitation spectra used in the experiment.
- **Not a substitute for phototoxicity protection** — LED 488 nm exposure is already minimised (≤200 ms, ≤5% power, 10 min intervals). Night vision is ADDITIONAL monitoring, not a replacement for the dark cycle. Cells still get 9 min 59.8 s of darkness between acquisitions.
- **Use case:** check that everything is running at 3 AM without opening the box, without turning on visible light, without disturbing the experiment.

### Laser & optics
- **Femtosecond laser** — NIR 800 nm, whole-cell ablation
- **Cooled sCMOS** — ZWO ASI183MM Pro (standard, not fallback)
- **Laser safety** — interlock system (laser shuts off if box is opened), laser safety officer, IRB protocol

## Build prerequisites

- 3D printer (PLA+/PETG/ASA compatible, ≥200×200 mm bed)
- OpenFlexure v6.1.5 STL files: https://build.openflexure.org/
- RMS-thread optics
- RasPi 5 + Camera HQ (or sCMOS)

## Directory

| Folder | Contents |
|--------|----------|
| `openflexure/` | Modifications to OpenFlexure STL files |
| `enclosure/` | Glove-box design (FreeCAD) — v2.0 |
| `optics/` | Optical path diagram, filter cube design |
| `electronics/` | KiCad schematics, wiring, BOM |
| `lasers/` | Laser safety & integration — v2.0 |

## License

All hardware files: **CC-BY-SA 4.0**
