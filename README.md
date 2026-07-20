# ARGUS-OS1 — centrosome maturation state as a division history marker

An open-source robotic microscope that tracks centrosome maturation state across divisions — asking whether the daughter cell that inherits the mature mother centrosome follows a different trajectory than its sister.

Built on [OpenFlexure](https://openflexure.org/) v6.1.5 inside a standard CO₂ incubator. 60×/1.2 NA water immersion. ASA filament. 24/7 autonomous imaging. **Primary system: RPE1-hTERT.**

## Platform Versions

| Version | Project | Hardware | Experiment | Laser | Budget |
|:-------:|---------|----------|------------|:-----:|:------:|
| **v1.0** | [ARGUS-OS1](./) | OF v6.1.5, 60×/1.2 NA WI, LED 488, glove-box (HEPA H13), night vision | RPE1 observation | ❌ | **$24,053** |
| **v2.0** | [ARGUS-OS2](../ARGUS-OS2/) | Same as v1.0 + Odf2 domain deletion reagents (Tateishi 2013) | Causality (Odf2 KO + FL/Δ188-806/Δ1-59/ΔC rescue) | ❌ | +$6,000 |
| **v3.0** | [ARGUS-OS3](../ARGUS-OS3/) | v1.0 + micromanipulator, fs laser, sCMOS, UV-C, Mac M4 Pro | NPC ablation + injection | ✅ | **$40,600** |

> **First grant = v1.0** ($24,053). Observation only. Own glove-box. No laser. No micromanipulator. v2.0 and v3.0 are separate projects with their own core files.

## What it costs (v1.0)

**$24,053** (max with fallbacks). Own glove-box from day one — no commercial incubator needed.

## What's inside

| Component | Details | Cost |
|-----------|---------|:----:|
| **Scope** | OpenFlexure v6.1.5 (ASA, NEMA 17 ×3, drivers, belts, bearings, fasteners) | $600 |
| **Glove-box** | Acrylic/polycarbonate enclosure 50×50×60 cm, arm-length neoprene gloves, airlock 20×20×20 cm | $3,300 |
| **Climate** | HEPA H13 + active circulation + CO₂/O₂/T/RH sensors + PID controller + heater | $2,500 |
| **Objective** | 60×/1.2 NA WI (Olympus/Nikon, tested used) | $3,500 |
| **Camera** | RasPi Camera HQ 12.3 MP (IMX477). Fallback: ZWO ASI183MM Pro cooled | $150 |
| **Fluorescence** | LED 488 nm + excitation/emission/dichroic filter cube (Thorlabs) | $900 |
| **Brain** | Jetson Orin NX 16GB + carrier board. CellPose, deconvolution, tracking | $700 |
| **AI accelerator** | RasPi 5 (4GB) + Hailo-8L (13 TOPS). Real-time CellPose inference | $180 |
| **Incubator** | New CO₂ incubator (Benchmark MyTemp / Binder CB 60) | $7,500 |
| **O₂ control** | N₂ cylinder + regulator + LuminOx sensor + solenoid valve | $500 |
| **Sister isolation** | CYTOO 2-cell micropatterned islands (fibronectin, PEG borders) ×20 | $1,500 |
| **Night vision** | IR LED 850 nm + RasPi Camera NoIR. 24/7 monitoring, zero phototoxicity | $50 |
| **Micromanipulator** | 3-axis (FOSH-adapted), stepper motors, glass capillary 1-2 µm, microinjector (optional) | $1,200 |

## AI Hardware — Jetson Orin NX. Local. 24/7.

| Component | Job |
|-----------|-----|
| **Jetson Orin NX 16GB** | CellPose 2.0, RL deconvolution, Bayesian tracking |
| **RasPi 5 (8GB)** | Microscope control, climate logging, night vision |
| **Hailo-8L (13 TOPS)** | Real-time CellPose inference |

**All models FREE. All models LOCAL. No API keys. No subscriptions.**

## Fluorescence — two probes, two tasks

| Probe | When | Task |
|-------|------|------|
| **Centrin1-GFP** | Live, every frame | TRACKING — centriole POSITIONS through mitosis |
| **Cenexin antibody** | Endpoint (72h, fixed) | CLASSIFICATION — mature mother centrosome (Cenexin-bright) |

## How it works

1. RPE1-hTERT Centrin1-GFP + H2B-GFP divide inside the incubator
2. Every 10 minutes: autofocus, acquire 2 channels (GFP + H2B)
3. Live tracking: Centrin1-GFP follows centriole POSITIONS through mitosis
4. Sisters tracked on CYTOO 2-cell islands for 72h (or separated via micromanipulator)
5. Optional: microinjection of apoptosis factors, dyes, siRNA
6. Endpoint: fix, Cenexin antibody → classify mature mother centrosome
7. McNemar test + glmer: does maturation state correlate with cilium fate?

## Full Budget — v1.0

| Line item | $ |
|-----------|--:|
| OpenFlexure v6.1.5 (ASA filament, NEMA 17 motors ×3, drivers, belts, bearings, fasteners) | 600 |
| RasPi 5 (8GB) + 1TB NVMe SSD + enclosure | 250 |
| Camera HQ (IMX477) + C-mount RMS adapter | 150 |
| Objective 60×/1.2 NA WI (Olympus/Nikon, tested used) | 3,500 |
| LED 488 nm (Thorlabs) + excitation filter + emission filter + dichroic beamsplitter | 900 |
| IR LED 850 nm + RasPi Camera NoIR (night vision) | 50 |
| Glove-box enclosure (acrylic/polycarbonate, 50×50×60 cm, custom fabrication) | 2,500 |
| Glove ports + arm-length neoprene gloves (2 pairs) + airlock (20×20×20 cm) | 800 |
| HEPA H13 filter unit + active circulation fan | 1,000 |
| Climate control (CO₂ sensor + O₂ sensor + T/RH sensor + PID controller + heater) | 1,200 |
| CO₂ cylinder (5 lb) + regulator (refillable, 6 month supply) | 300 |
| O₂ control (N₂ cylinder + regulator + LuminOx sensor + solenoid valve) | 500 |
| Jetson Orin NX 16GB module + carrier board (Seeed/Connect Tech) | 700 |
| RasPi 5 (4GB) + Hailo-8L AI accelerator | 180 |
| Centrin1-GFP RPE1-hTERT (lentiviral transduction, commercial service) | 1,500 |
| Odf2/Cenexin antibody (100 µg, Abcam/Santa Cruz) | 350 |
| RPE1-hTERT (ATCC CRL-4000) + ReNcell NPCs (Lonza, 1 vial) | 1,800 |
| Culture media, FBS, supplements, antibiotics (DMEM/F12, B-27, EGF, FGF-2) | 500 |
| CYTOO 2-cell micropatterned coverslips ×20 | 1,500 |
| Tetraspeck fluorescent beads (ThermoFisher, calibration set) | 250 |
| IF antibodies (acetylated tubulin + Alexa Fluor secondary + DAPI + blocking buffer) | 400 |
| Transfection reagents (Lipofectamine, polybrene, puromycin) | 250 |
| Consumables (Petri dishes, pipette tips, tubes, PFA, Triton X-100, immersion water) | 600 |
| Cables, connectors, power supplies, misc hardware | 200 |
| Shipping, customs, import duties (Georgia) | 500 |
| **Subtotal v1.0** | **19,880** |
| **+15% contingency** | **2,982** |
| **SNR fallback (ZWO ASI183MM Pro cooled sCMOS, net)** | **1,018** |
| **TOTAL v1.0 (max)** | **$24,053** |

## Micromanipulator Module (optional, +$1,208)

| Line item | $ |
|-----------|--:|
| 3-axis micromanipulator (FOSH v2.0 adapted: STL print + NEMA 11 steppers ×3 + drivers) | 400 |
| Pneumatic microinjector (adjustable pressure + vacuum hold) | 500 |
| Glass capillaries (borosilicate, 1.0 mm OD, box of 100) | 60 |
| Mounting bracket (3D-printed, OF v6.1.5 compatible) | 40 |
| Tubing, connectors, syringe, mineral oil | 50 |
| +15% contingency | 158 |
| **TOTAL v1.0+ (with micromanipulator)** | **$25,261** |

> Capillary puller: assume university core facility. If purchase: +$3,000.

## What this IS

- **An INSTRUMENT** — open-source robotic microscope for centrosome-aware lineage tracking
- **A METHOD** — maturation state (Cenexin ratio _M_) as a continuous predictor of cell fate
- **A PLATFORM** — extensible: micromanipulation, microinjection, laser ablation, night vision

## What this IS NOT

- **NOT** a causal experiment (Odf2 domain deletions = [v2.0](../ARGUS-OS2/))
- **NOT** a mechanistic study (PCM1/Notch = v3.0+)
- **NOT** a laser ablation platform in v1.0
- **NOT** a "barcode" — maturation state is dynamic, graded, evolved

## License

- Code: **GPLv3**
- Hardware (STL, CAD, schematics): **CC-BY-SA 4.0**
- Image analysis pipeline: **MIT**
- Data: **CC0**

## Who's behind this

Built by [Jaba Tqemaladze](https://github.com/djabbat) at the Georgia Longevity Alliance.

Questions? jaba@longevity.ge
