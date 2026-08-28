# The Model Hardware Standard (MHS) by Anthropic: analysis and relevance for ARGUS

**Date:** 2026-08-28
**Status:** Analysis / opportunity mapping
**Relevance:** V9-BRAIN (Tool Bridge), DAIS (DAISocket), AIS LLM Bridge, V9-HANDS, OS1 Vision
**Sources:** anthropic.com (primary, 27 Aug 2026), modelhardwarestandard.com, explainx.ai, CNBC, Ars Technica, TechStartups, 3DNews

---

## 1. What the announcement is about

On 27 August 2026 Anthropic opened a research preview of the **Model Hardware Standard (MHS)** — a shared specification that lets AI agents operate physical laboratory and manufacturing equipment safely. MHS grew out of a collaboration between Anthropic (Alek Kemeny, Beneficial Deployments) and the **HHMI Janelia Research Campus** (postdoc Arco Bast).

Key points:

- **The problem it solves.** Wiring laboratory instruments together normally takes weeks to months of bespoke integration work by specialists, because devices do not talk to one another. MHS cuts that to hours or minutes.
- **The abstraction.** A standardized driver layer over any device with a programmable interface, built on two primitives: `read` (for example, "get temperature") and `write` (for example, "set temperature"), plus a standard discovery format so devices and agents can find each other across a network.
- **Physical and safety context.** Facts that are not obvious from code alone — the weight of a robot arm, safe operating ranges of a laser, what a device measures versus what can be adjusted — are written in natural language into driver "tags", either by the user or by an agent interviewing the operator. From these tags MHS generates a reference file giving the agent everything it needs to operate the device.
- **Three control mechanisms.** MCP, the command line, and code files (APIs). They work together: the agent orchestrates at a high level, and for long-running or fast operations it chains driver commands into deterministic scripts.
- **The exploration-to-compile pattern.** Claude behaves like a scientist — it adjusts a laser, looks at the result through a camera, repeats, and once it understands the sequence it packages the procedure into a code file that runs as a single command.
- **Pilot results.** Genentech (autonomous BCA protein assay), University of Washington Baker/Pinglay labs (remote monitoring, agent-supervised qPCR, collision-free plate handoffs), Carnegie Mellon (serial-dilution dose-response several times faster), **QuEra (laser stabilization on a quantum computer improved from 58% to 99.3%)**, and Janelia (an imaging experiment compressed from weeks to a day).
- **Vendor ecosystem (10+).** AWS, Automata, Danaher, Doosan, MBF Bioscience, QIAGEN, Tecan, Universal Robots, Hugging Face (LeRobot), and Raspberry Pi.
- **Status.** Research preview by application (modelhardwarestandard.com); the standard will be open-sourced later, after Anthropic develops a physical-safety roadmap (Anthropic also flags concerns about misuse for biological weapons).

Honest limitations worth noting:

- LLM physical and spatial reasoning is still weaker than human expertise. For example, at Genentech Claude initially treated an error caused by bubbles in a liquid as a software bug rather than a physical problem, so expert oversight and human-in-the-loop checkpoints are still required.
- MHS works only with devices that have a programmable interface.
- The safety mechanisms are still being developed.

## 2. Similar work and the broader landscape

| Project / standard | What it is | Relevance to ARGUS |
|--------------------|------------|--------------------|
| **Coscientist** (CMU, Nature 2023, s41586-023-06792-0) | GPT-4 designs, plans, and runs chemical experiments autonomously; Planner + Code Execution + Multi-Hardware | V9-BRAIN already follows this pattern |
| **OpentronsAI / Opentrons OT-2** | LLM generates liquid-handling protocols from natural language; deck simulation and verification in chat | Useful if ARGUS adds an autosampler |
| **SiLA 2** (sila-standard.com) | Mature open standard for instrument interoperability in labs | Possible transport layer alongside MCP |
| **Autoprotocol / ANLTRN** | JSON experiment-description language and results-data model; separates design from execution | Portable protocols across OS1/OS2/OS3 |
| **LADS OPC UA** | Industrial communication standard rooted in factory automation | Alternative for industrializing V9-HANDS |
| **FutureHouse AI Scientist** | Philanthropic effort toward a semi-autonomous AI scientist | Similar design-build-test-learn direction |
| **MCP (Model Context Protocol)** | Already used in ARGUS as an MCP-style Tool Bridge | Direct bridge: MHS is MCP applied to physical hardware |
| **Anthropic Claude Science** | AI model to help scientists with diseases and drug discovery | Market context |
| **OpenAI Codex + robot arm** (UFactory xArm) | Example of an LLM driving a robot arm | Confirms the exploration-to-compile pattern |
| **AI-driven QC for liquid handling** (Springer 10489-025-06334-3) | Computer-vision quality control for liquid handlers | Vision as ground truth, matching our YOLO+CellPose |

The landscape confirms that ARGUS already sits at the leading edge of this trend: it has a Tool Bridge (MCP-style), a Safety Layer (Body Law), a local LLM brain, a Flight Recorder, and vision. MHS is an ecosystem-level standard that ARGUS should align with so that it does not reinvent its own driver layer and can interoperate with the wider ecosystem (LeRobot, Tecan, OpenFlexure, Raspberry Pi) once MHS is released.

## 3. Mapping MHS to ARGUS (V9 / DAIS)

| ARGUS component | MHS counterpart | Action |
|-----------------|-----------------|--------|
| **Tool Bridge** (V9 4.3, MCP-style) | MHS driver (read/write + discovery) | Realize the Tool Bridge to the MHS specification for compatibility with agents and vendors |
| **Safety Layer / Body Law** (force <=5 N, speed <=200 mm/s, no-touch zones) | Natural-language safety tags + reference file | Move our safety limits into MHS driver tags (interview pattern) |
| **Flight Recorder** (AIS: pose, force, time, frame) | Streaming of device state to the agent | Keep our event store; MHS reads it as the source of state |
| **V9-BRAIN** (Planner + LLM) | MCP/CLI/code orchestration by the agent | Our local brain is the harness; MHS is the transport |
| **Vision** (YOLO+CellPose on AGX) | Camera driver / ground truth | The camera is both a sensor and ground truth for verifying actions |
| **V9-HANDS** (cable-driven arms) | Robotic-arm driver (write: move/gripper; read: pose/force) | Write an MHS "arm" driver over our controller |
| **Pipette / dispenser** | Liquid-handler driver | A dedicated driver if we add an autosampler |
| **FOSH manipulator** | Positioning driver | Read/write position |

Strategic position: MHS is not yet open source (application only). For ARGUS this means:

1. **Apply for the research preview** (modelhardwarestandard.com), presenting autonomous live-cell microscopy as a use case. An application was submitted on 29 August 2026.
2. **Model our Tool Bridge on the MHS form** while we wait — read/write primitives, discovery, natural-language safety tags — so that once MHS is released we only swap the transport.
3. ARGUS-OS1, as the first instance of AIS/DAIS, is a good testbed for MHS: open, low-cost, with a live use case.

## 4. Reference code for ARGUS (MHS-shaped solutions)

### 4.1 A minimal MHS-style driver abstraction (Python, edge)

A universal read/write plus safety wrapper so that any instrument (microscope, arm, pump, FOSH) is exposed as an MHS-compatible device. Runs on the Jetson Orin NX / AGX.

```python
# argus_mhs/driver.py -- MHS-style driver base for ARGUS devices
from __future__ import annotations
import time, threading
from dataclasses import dataclass, field
from typing import Any, Dict, List

@dataclass
class Tag:
    """Natural-language physical/safety context (MHS tags).
    Replaces a paper manual: weight, limits, what is measurable vs adjustable.
    MHS derives a reference file from these."""
    description: str
    weight_kg: float
    read: List[str]
    write: List[str]
    safety_limits: Dict[str, Any]
    units: Dict[str, str] = field(default_factory=dict)

class MHSDriver:
    """Base class. Two primitives: read / write plus discoverability."""
    def __init__(self, device_id: str, tag: Tag, logger=None):
        self.id = device_id
        self.tag = tag
        self._state = {}
        self._lock = threading.Lock()
        self.flight = []                    # Flight Recorder (AIS)
        self._log = logger or (lambda m: print(f"[{self.id}] {m}"))

    def read(self, qty: str) -> Any:
        if qty not in self.tag.read:
            raise KeyError(f"{self.id}: '{qty}' not readable (allowed={self.tag.read})")
        with self._lock:
            val = self._read_impl(qty)
        self._record("read", qty, val)
        return val

    def write(self, qty: str, value: Any) -> Any:
        if qty not in self.tag.write:
            raise KeyError(f"{self.id}: '{qty}' not writable")
        self._enforce_safety(qty, value)     # Safety Layer
        self._checkpoint(qty, value)         # human-in-the-loop hook
        with self._lock:
            out = self._write_impl(qty, value)
        self._record("write", qty, {"cmd": value, "res": out})
        return out

    def _read_impl(self, qty):  raise NotImplementedError
    def _write_impl(self, qty, value): return None

    def _enforce_safety(self, qty, value):
        lim = self.tag.safety_limits.get(qty)
        if lim:
            mn, mx = lim.get("min"), lim.get("max")
            if (mn is not None and value < mn) or (mx is not None and value > mx):
                raise PermissionError(f"{self.id}: {qty}={value} violates {lim}")

    def _checkpoint(self, qty, value):
        """Human-in-the-loop gate for irreversible operations (MHS lesson)."""
        if self.tag.safety_limits.get(qty, {}).get("confirm"):
            ok = input(f"CONFIRM {self.id}: {qty}={value}? [y/N] ")
            if ok.strip().lower() not in ("y", "yes"):
                raise RuntimeError(f"aborted by operator: {qty}={value}")

    def _record(self, kind, qty, payload):
        self.flight.append({"t": time.time(), "dev": self.id,
                            "kind": kind, "qty": qty, "payload": payload})
        self._log(f"{kind} {qty} -> {payload}")

    def discover(self) -> dict:
        return {"id": self.id, **self.tag.__dict__, "online": True,
                "transport": ["mcp", "cli", "code"]}

    def reference_file(self) -> str:
        import json
        return json.dumps(self.discover(), indent=2, default=str)
```

### 4.2 Arm driver (V9-HANDS): position and gripper with Body Law

```python
# argus_mhs/devices/arm.py
import time
from argus_mhs.driver import MHSDriver, Tag

ARM_TAG = Tag(
    description="Cable-driven 6-DOF arm through a glove-port sleeve",
    weight_kg=2.5,
    read=["pose", "force", "speed", "current", "gripper"],
    write=["move", "gripper", "speed_limit", "force_limit"],
    safety_limits={
        "force": {"max": 5.0},              # Body Law: F <= 5 N
        "speed": {"max": 200.0},            # Body Law: v <= 200 mm/s
        "move":  {"min": [-200,-200,-200], "max": [200,200,200], "confirm": True},
    },
    units={"pose": "mm", "force": "N", "speed": "mm/s"},
)

class ArmDriver(MHSDriver):
    def __init__(self, bus, arm="L", node_id=0x11):
        super().__init__(f"argus/arm/{arm}", ARM_TAG)
        self.bus, self.node_id = bus, node_id
        self._pose = [0, 0, 0]

    def _read_impl(self, qty):
        if qty == "pose":  return self._pose
        if qty == "force": return self.bus.read_reg(self.node_id, 0x30) / 1000.0
        if qty == "speed": return self.bus.read_reg(self.node_id, 0x32)
        return 0

    def _write_impl(self, qty, value):
        if qty == "gripper":
            self.bus.write_reg(self.node_id, 0x40, 1 if value else 0)
            return "ok"
        if qty == "move":
            self._move_to(value)
            return self._pose
        return None

    def _move_to(self, target):
        vmax = self.tag.safety_limits["speed"]["max"]
        for k in range(1, 10):
            step = [self._pose[i] + (target[i]-self._pose[i])*k/10 for i in range(3)]
            dt = 0.05
            for i in range(3):              # clamp per-tick velocity
                d = abs(step[i]-self._pose[i])
                if d/dt > vmax:
                    sgn = 1 if step[i] > self._pose[i] else -1
                    step[i] = self._pose[i] + sgn*vmax*dt
            self.bus.move_to(self.node_id, step)
            self._pose = step
            time.sleep(dt)
```

### 4.3 Microscope driver (OpenFlexure), with the Motor Release API

```python
# argus_mhs/devices/microscope.py
from argus_mhs.driver import MHSDriver, Tag

SCOPE_TAG = Tag(
    description="OpenFlexure microscope (ARGUS-OS1), 40x/0.75 dry",
    weight_kg=4.0,
    read=["stage_xyz", "focus", "temperature", "snr"],
    write=["move_stage", "set_focus", "capture", "led"],
    safety_limits={"move_stage": {"min":[0,0,0],"max":[30,30,15]},
                   "set_focus": {"min":0,"max":20}, "led": {"min":0,"max":100}},
    units={"stage_xyz":"mm", "focus":"mm", "temperature":"C"},
)

class ScopeDriver(MHSDriver):
    def __init__(self, hw, vision=None):
        super().__init__("argus/scope", SCOPE_TAG)
        self.hw, self.vision = hw, vision

    def _read_impl(self, qty):
        if qty == "stage_xyz":   return self.hw.position()
        if qty == "focus":       return self.hw.focus_position()
        if qty == "temperature": return self.hw.temp()
        if qty == "snr":
            return self.vision.report_snr() if self.vision else self.hw.report_snr()
        return None

    def _write_impl(self, qty, value):
        if qty == "move_stage": self.hw.move_abs(value); return self.hw.position()
        if qty == "set_focus":  self.hw.focus_abs(value); return self.hw.focus_position()
        if qty == "capture":    return self.hw.capture(value)
        if qty == "led":        self.hw.set_led(value); return "ok"
        return None
```

### 4.4 The exploration-to-compile pattern (MHS) applied to ARGUS

```python
# argus_mhs/explore_compile.py
def explore_and_compile(driver, goal, callback, max_steps=20):
    """Tune a device iteratively, observe the result, compile a script."""
    chain = []
    for _ in range(max_steps):
        action = callback.pick_next_action(goal, chain)
        result = driver.write(action["qty"], action["value"])
        obs = callback.observe(result)          # camera / vision snapshot
        chain.append({"qty": action["qty"], "value": action["value"], "obs": obs})
        if callback.is_done(obs):
            return compile_script(chain)
    raise TimeoutError("not converged")

def compile_script(chain):
    lines = ["def run(driver):"]
    for i, c in enumerate(chain):
        lines.append(f"    r{i} = driver.write({c['qty']!r}, {c['value']!r})")
    lines.append("    return locals()")
    src = "\n".join(lines)
    open("compiled_procedure.py", "w").write(src)
    return src
```

A natural use is closed-loop autofocus on the 60x/1.2 WI objective: the agent moves focus, reads SNR from Vision, repeats, and once it converges it compiles `focus_60x.py`, which then runs as one command (the same approach QuEra used with its laser).

### 4.5 An MCP server over the drivers

```python
# argus_mhs/mcp_server.py
from mcp.server.fastmcp import FastMCP
_devices = {}
def register(driver): _devices[driver.id] = driver

mcp = FastMCP("ARGUS")

@mcp.tool()
def list_devices() -> str:
    import json; return json.dumps([d.discover() for d in _devices.values()], indent=2)

@mcp.tool()
def read(device: str, qty: str) -> str:
    import json; return json.dumps(_devices[device].read(qty))

@mcp.tool()
def write(device: str, qty: str, value) -> str:
    import json; return json.dumps(_devices[device].write(qty, value))

if __name__ == "__main__":
    mcp.run()
```

### 4.6 Building driver tags through an interview

```python
# argus_mhs/interview.py
QUESTIONS = [
    ("What does the device measure?", "read"),
    ("What can be adjusted?", "write"),
    ("What are the safe limits (min/max)?", "safety_limits"),
    ("What units?", "units"),
]
def interview(fn=input):
    d = {}
    for q, key in QUESTIONS:
        raw = fn(q).strip()
        d[key] = json.loads(raw) if key in ("read","write","safety_limits","units") else raw
    return Tag(**d)
```

## 5. Recommended actions for ARGUS

1. **Apply for the MHS research preview** (modelhardwarestandard.com) with autonomous live-cell microscopy as the use case. Done: application submitted on 29 August 2026.
2. **Align the Tool Bridge with the MHS form** now — read/write primitives, discovery, natural-language safety tags — so that once MHS is released we only swap the transport. A working implementation is in `software/argus_mhs/`.
3. **Move Safety Layer / Body Law into MHS tags.** Our limits (force <=5 N, speed <=200 mm/s, no-touch zones) are already expressed as `safety_limits` in the reference drivers.
4. **Keep human-in-the-loop checkpoints** on irreversible operations (the Genentech lesson: the model can misattribute a physical failure to a software bug) and keep the escalation rule (confidence below 0.7 goes to a human).
5. **Watch the ecosystem:** Hugging Face is integrating MHS into LeRobot (open arms), Raspberry Pi ships a camera driver, and Tecan covers liquid handling. ARGUS-OS3 already uses open arms, so aligning with LeRobot would strengthen FOSH and V9-HANDS.
6. **Add a liquid-handler driver** to the OS2 portfolio (V7 microfluidics) — an autosampler with read/write plus vision quality control.
7. **Document the exploration-to-compile pattern** in CONCEPT/METHODOLOGY as a strong argument for grants (EIC Pathfinder, 28 October, WP2).

## 6. Sources

- Primary: https://www.anthropic.com/news/model-hardware-standard-research-preview (27 Aug 2026)
- Application: https://www.modelhardwarestandard.com/
- Technical breakdown (MCP analogy, vendors, limits): https://explainx.ai/blog/anthropic-model-hardware-standard-mhs-research-preview-august-2026
- Coscientist (Nature 2023): https://www.nature.com/articles/s41586-023-06792-0
- OpentronsAI: https://opentrons.com/ai ; SiLA 2: https://sila-standard.com ; FutureHouse: https://www.futurehouse.org/
- Related ARGUS docs: `docs/V9_PROTOTYPE.md`, `docs/STERILIZATION_TRANSFER.md`, `../DAIS/README.md`

---

*Engineering document. MHS is not yet open source, so external texts should say "aligned with the MHS pattern" rather than "integrated with MHS".*
