# argus_mhs — Tool Bridge ↔ MHS alignment

**Status:** scaffold (2026-08-29) · **Purpose:** align ARGUS Tool Bridge with
Anthropic's **Model Hardware Standard (MHS)** — a shared spec for AI agents to
safely operate physical devices. MHS was previewed Aug 27 2026 (application
submitted by ARGUS Aug 29).

## Why
MHS uses read/write drivers + discoverability + natural-language safety tags
and three transports (MCP / CLI / code). ARGUS V9 already has a Tool Bridge
(MCP-style) + Safety Layer (Body Law) + Flight Recorder. This package formalizes
the driver abstraction so that:
- any MHS-aware agent can operate ARGUS;
- ARGUS interoperates with the MHS ecosystem (LeRobot/Hugging Face, Raspberry Pi,
  Tecan) once MHS is open-sourced (only transport swap needed).

## Layout
```
argus_mhs/
  __init__.py
  driver.py            # MHSDriver base: read/write + discover + Safety Layer
  explore_compile.py   # exploration -> compile pattern
  mcp_server.py        # optional MCP transport (pip install mcp)
  devices/
    arm.py             # V9-HANDS cable-driven arm (Body Law limits)
    microscope.py      # OpenFlexure stage/focus (Motor Release API)
    # TODO: pipette.py (liquid handling, medium replenishment)
    # TODO: transfer_box.py (door interlock, UV-C sensors)
```

## How to use
```python
from argus_mhs.devices.arm import ArmDriver
from argus_mhs.mcp_server import register, run_mcp

register(ArmDriver(bus=my_can_bus, arm="L", node_id=0x11))
register(ScopeDriver(hw=openflexure_hw))

# CLI-style:
arm.read("pose")
arm.write("move", [10, 0, 5])     # passes Safety Layer; human confirms (move)
# MCP transport (optional):
run_mcp("ARGUS")
```

## Alignment checklist (per MHS)
- [x] read / write primitives (MHSDriver)
- [x] discoverability (discover() / reference_file())
- [x] natural-language safety tags (Tag) + Body Law
- [x] human-in-the-loop on irreversible ops (checkpoint)
- [x] exploration -> compile (explore_compile.py)
- [ ] transport: MCP server (present, optional) — wire real devices
- [ ] devices: pipette, transfer-box, FOSH, Vision-as-source
- [ ] when MHS open-sources: swap transport to official spec

Reference: `docs/MHS_MODEL_HARDWARE_STANDARD_ANALYSIS.md`
