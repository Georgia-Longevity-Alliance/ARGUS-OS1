# ARGUS-OS1 Software

Control software for the autonomous 24/7 cell lineage tracking microscope.

## Platform Versions (software)

| Version | Brain | Capabilities | Status |
|:-------:|-------|-------------|:------:|
| **v1.0** | RasPi 5 + Jetson Orin NX 16GB + Hailo-8L (13 TOPS) | CellPose 2.0, RL deconvolution, Bayesian tracking, climate logging, night vision (IR LED + Camera NoIR) | 🎯 First grant |
| **v2.0** | v1.0 + Mac M4 Pro | + AI agent (local LLM — ablation decisions), + multi-camera night vision stitching, + laser control, + glove-box climate PID, + UV-C sterilisation control | Future grant |

## Architecture (v1.0)

```
┌─────────────────────────────────────┐
│  microscope/ (OpenFlexure Connect)   │
│  - Stage control (XYZ)              │
│  - Autofocus (contrast-based,       │
│    Knapper 2022 method)             │
│  - Multi-point time-lapse           │
│  - LED 488 nm trigger               │
└─────────────────────────────────────┘
           │
┌─────────────────────────────────────┐
│  tracking/                          │
│  - CellPose 2.0 segmentation        │
│  - Bayesian lineage tracker         │
│  - Centrin1-GFP spot detection      │
│  - Mitosis detection (H2B-GFP)      │
└─────────────────────────────────────┘
           │
┌─────────────────────────────────────┐
│  climate/                           │
│  - CO₂, O₂, T, RH logging          │
│  - PID controller (RasPi Pico W)    │
│  - Telegram alerts                  │
└─────────────────────────────────────┘
           │
┌─────────────────────────────────────┐
│  nightvision/  (standard in v1.0)   │
│  - IR LED 850 nm control            │
│  - RasPi Camera NoIR capture        │
│  - Motion detection                 │
│  - Snapshot on demand / periodic    │
│  - Zero phototoxicity monitoring    │
└─────────────────────────────────────┘
```

## Architecture (v2.0 additions)

```
┌─────────────────────────────────────┐
│  agent/                             │
│  - Local LLM (Mixtral 8×7B /       │
│    Llama 3.3 70B)                   │
│  - Decision: ablate / observe /     │
│    flag for human                   │
│  - Self-learning (LoRA + RAG)       │
│  - Natural language experiment log  │
└─────────────────────────────────────┘
           │
┌─────────────────────────────────────┐
│  nightvision/  (upgraded for v2.0)  │
│  - Multi-camera IR array (2× NoIR) │
│  - Stereo depth for glove-box       │
│  - 24/7 recording with timelapse    │
│  - Full-box surveillance            │
└─────────────────────────────────────┘
           │
┌─────────────────────────────────────┐
│  laser/                             │
│  - Femtosecond pulse control        │
│  - Targeting (click cell → ablate)  │
│  - Interlock safety monitor         │
│  - Post-ablation verification       │
│  - Death confirmation (H2B-GFP      │
│    nuclear integrity + morphology)  │
└─────────────────────────────────────┘
           │
┌─────────────────────────────────────┐
│  biosafety/  (v2.0)                 │
│  - UV-C sterilisation cycle         │
│  - HEPA H13 filter status monitor   │
│  - Glove integrity check            │
│  - Airlock cycle control            │
└─────────────────────────────────────┘
```

## Requirements

| Component | v1.0 | v2.0 |
|-----------|------|------|
| Python | 3.11+ | 3.11+ |
| OpenFlexure Connect | ✅ | ✅ |
| CellPose | 2.0+ | 2.0+ |
| PyTorch | 2.0+ (Jetson) | 2.0+ (M4 + Jetson) |
| OpenCV | 4.8+ (night vision) | 4.8+ (multi-camera) |
| Brain | RasPi 5 + Jetson Orin NX | + Mac M4 Pro |
| Storage | 1 TB SSD | 4 TB SSD (night vision recording) |

## License

All software: **GPLv3**
