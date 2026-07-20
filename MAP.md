# MAP — ARGUS-OS1

```
ARGUS-OS1/
├── README.md               # Homepage (platform versions table)
├── CONCEPT.md              # Concept (v49 — hypothesis + 23 refs)
├── PARAMETERS.md           # Budget, technical specs, timeline
├── TODO.md                 # Tasks
├── STATE.md                # Current status
├── MEMORY.md               # Decision history
├── _pi.md                  # Rules for pi
├── CONTRIBUTING.md         # How to contribute
├── CODE_OF_CONDUCT.md      # Code of conduct
├── SECURITY.md             # Security
├── LICENSE                 # MIT + GPLv3 + CC-BY-SA
├── .gitignore
│
├── docs/                   # Documentation
│   ├── DEEP_AUDIT_2026-07-18.md
│   ├── ARGUS_ACTION_PLAN_2026-07-18.md
│   ├── PEER_REVIEW_STRICT_2026-07-18.md
│   ├── REVIEW_VERIFICATION_2026-07-18.md
│   ├── REVIEW2_VERIFICATION_2026-07-18.md
│   ├── REVIEW3_VERIFICATION_2026-07-18.md
│   ├── REVIEW4_VERIFICATION_2026-07-18.md
│   ├── VALIDATION_PLAN.md
│   ├── PILOT_CENTRIN1_SNR_PLAN.md
│   ├── OUTREACH.md
│   ├── Alex_update.md
│   └── logo.png
│
├── hardware/               # 3D models, schematics
│   └── README.md           # v1.0 + v2.0 hardware specs
│
├── software/               # Control + AI + night vision
│   └── README.md           # v1.0 + v2.0 software specs
│
├── firmware/               # Firmware
│   └── README.md
│
├── letters/                # Outreach correspondence
│   ├── letter-bowman-2026-07-18.md
│   ├── letter-bowman-openflexure-2026-07-18.md
│   ├── openflexure-forum-post-2026-07-18.md
│   └── centrin1-gfp-request-post-2026-07-18.md
│
├── grants/                 # Grant applications (planned)
│
└── refs/                   # Scientific references (planned)

Planned subdirectories (created during build):
  hardware/openflexure/      — OpenFlexure v6.1.5 modifications
  hardware/enclosure/        — Glove-box design (FreeCAD) — v2.0
  hardware/optics/           — Optical path diagram, filter cube
  hardware/electronics/      — Schematics (KiCad), BOM
  hardware/lasers/           — Laser safety & integration — v2.0
  software/microscope/       — OpenFlexure Connect + ARGUS extensions
  software/tracking/         — CellPose + Bayesian lineage tracker
  software/climate/          — PID climate controller
  software/nightvision/      — IR LED control + Camera NoIR (standard v1.0, upgraded v2.0)
  software/agent/            — AI agent (local LLM) — v2.0
  software/laser/            — Femtosecond laser control — v2.0
  software/biosafety/        — UV-C, HEPA monitor, glove check — v2.0
  firmware/climate-controller/  — RasPi Pico W
  docs/build-guide/          — Build guide
  docs/protocols/            — Lab protocols
  docs/images/               — Build photos
  grants/NLNet/              — NLNet NGI0 Commons Fund
  grants/EIC/                — EIC Pathfinder WP2
```

## Platform Versions

| Version | Hardware | Software | Experiment | Laser |
|:-------:|----------|----------|------------|:-----:|
| **v1.0** | OpenFlexure v6.1.5, 60×/1.2 NA WI, LED 488, Camera HQ, night vision (1× NoIR), HEPA H13 incubator | RasPi 5 + Jetson Orin NX, CellPose 2.0, climate logging, night vision | Phase 1 — RPE1 observation | ❌ |
| **v1.5** | Same as v1.0 | Same as v1.0 | Phase 2 — Odf2 KO causality | ❌ |
| **v2.0** | v1.0 + glove-box (HEPA H13, UV-C), fs laser 800 nm, sCMOS, night vision (2× NoIR), internal storage | v1.0 + Mac M4 Pro, AI agent, multi-camera NV, laser control, biosafety | Phase 3 — NPC progenitor map + ablation | ✅ |

## Links
- **Scientific basis:** `~/Desktop/LC/MCARA/CEDAR/` (centriolar hypothesis)
- **Old version:** `~/Desktop/LC/MCARA/ARGUS-OS1/` (archive)
- **EIC Pathfinder:** `~/Desktop/Marketing/MCARA_EIC_Pathfinder/wp2_argus/`
- **OpenFlexure upstream:** `https://github.com/openflexure/openflexure-microscope`
- **GitHub:** `https://github.com/Georgia-Longevity-Alliance/ARGUS-OS1`
