"""MHS-style driver base for ARGUS devices.

Two primitives (read / write) + discoverability + natural-language safety
tags + Safety Layer (Body Law) + Flight Recorder, mirroring Anthropic's
Model Hardware Standard. Model-agnostic: any agent harness can drive it via
MCP, CLI, or code files.
"""
from __future__ import annotations

import time
import threading
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class Tag:
    """Natural-language physical/safety context (MHS 'tags').

    Replaces paper manuals: weight, safe limits, what is measurable vs
    adjustable. MHS uses these to auto-generate a reference file.
    """
    description: str
    weight_kg: float
    read: List[str]          # measurable quantities
    write: List[str]         # adjustable quantities
    safety_limits: Dict[str, Any]
    units: Dict[str, str] = field(default_factory=dict)


class MHSDriver:
    """Base driver. Two primitives: read / write + discoverability."""

    def __init__(self, device_id: str, tag: Tag, logger=None):
        self.id = device_id
        self.tag = tag
        self._state: Dict[str, Any] = {}
        self._lock = threading.Lock()
        self.flight: List[Dict[str, Any]] = []     # Flight Recorder (AIS)
        self._log = logger or (lambda msg: print(f"[{self.id}] {msg}"))

    # ---- primitives ----
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
        self._enforce_safety(qty, value)            # Safety Layer / Body Law
        self._checkpoint(qty, value)                # human-in-the-loop hook
        with self._lock:
            out = self._write_impl(qty, value)
        self._record("write", qty, {"cmd": value, "res": out})
        return out

    # ---- subclass hooks ----
    def _read_impl(self, qty): raise NotImplementedError
    def _write_impl(self, qty, value): return None

    def _enforce_safety(self, qty, value):
        lim = self.tag.safety_limits.get(qty)
        if lim:
            mn, mx = lim.get("min"), lim.get("max")
            if (mn is not None and value < mn) or (mx is not None and value > mx):
                raise PermissionError(f"{self.id}: {qty}={value} violates {lim}")

    def _checkpoint(self, qty, value):
        """Human-in-the-loop gate for irreversible ops (MHS lesson)."""
        if self.tag.safety_limits.get(qty, {}).get("confirm"):
            ok = input(f"CONFIRM {self.id}: {qty}={value}? [y/N] ")
            if ok.strip().lower() not in ("y", "yes"):
                raise RuntimeError(f"aborted by operator: {qty}={value}")

    def _record(self, kind, qty, payload):
        self.flight.append({"t": time.time(), "dev": self.id,
                            "kind": kind, "qty": qty, "payload": payload})
        self._log(f"{kind} {qty} -> {payload}")

    # ---- discoverability ----
    def discover(self) -> dict:
        return {
            "id": self.id, **self.tag.__dict__,
            "online": True,
            "transport": ["mcp", "cli", "code"],
        }

    def reference_file(self) -> str:
        import json as _json
        return _json.dumps(self.discover(), indent=2, default=str)
