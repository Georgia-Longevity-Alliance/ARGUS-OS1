# ARGUS-OS1 Software

**Status:** 🟡 Planned — awaiting V6 hardware assembly.

## Stack
| Component | Technology | Purpose |
|-----------|------------|---------|
| Microscope Control | OpenFlexure Connect + ARGUS extensions | Stage, focus, laser |
| AI Tracking | CellPose 2.0 + custom Bayesian lineage tracker | Centriole detection |
| Edge AI | Jetson Orin NX (TensorRT FP16/INT8) | Real-time inference |
| Climate Control | PID controller (RasPi Pico W) | Temperature ±0.1°C |
| Night Vision | IR LED + Camera NoIR | Overnight monitoring |
| Data Pipeline | Zenodo + BioImage Archive | Open data |

## Planned Subdirectories
- `microscope/` — OpenFlexure Connect + ARGUS extensions
- `tracking/` — CellPose + Bayesian lineage tracker
- `climate/` — PID climate controller
- `nightvision/` — IR LED + Camera NoIR
- `agent/` — AI agent (local LLM, Jetson)
- `laser/` — Femtosecond laser control (V7+)
- `biosafety/` — UV-C, HEPA, glove check (V7+)

## AIS Integration
Software communicates with AIS Central Node via REST API:
- Passport registration
- Flight Recorder event streaming
- LLM anomaly diagnosis requests
- Knowledge Graph submission
