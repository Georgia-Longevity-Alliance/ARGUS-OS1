# STATE — ARGUS-OS1

**Date:** 2026-07-23
**Status:** 🔵 OS1 = V6 — OpenFlexure + Jetson Orin NX + Dry 40×/0.75 (~$3-5K). Local edge-AI. Alex building.

## OS Stages
- **V0:** ~$930 — bare OpenFlexure mechanics, no AI
- **OS1 = V6:** ~$3-5K — local AI (Jetson Orin NX, CellPose + tracking + lineage)
- **OS2 = V7:** ~$126K — 60×/1.2 WI + sCMOS + microfluidic
- **OS3 = V8:** +$141K — light-sheet + fs-laser + tweezers

## 23 Jul: Motor release — breakthrough from WilliamW
- Sangaboard firmware **already contains** motor release command
- No need for TMC2209 + MOSFET — just expose via REST API
- Result: CO₂ incubator heat problem solved in software
- Task: expose motor_release() in API → PR to OpenFlexure
