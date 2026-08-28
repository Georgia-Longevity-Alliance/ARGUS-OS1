"""Tamper-evident audit log for the ARGUS Flight Recorder (AIS).

Chains every entry with a SHA-256 hash of the previous entry -> any edit is
detectable. Provides `export()` as JSON (evidence for ERC / MHS safety-evals)
and `verify()` to check chain integrity.
"""
from __future__ import annotations

import hashlib
import json
import time
from typing import Any, Dict, List, Optional


class AuditLog:
    def __init__(self, name: str = "argus"):
        self.name = name
        self.entries: List[Dict[str, Any]] = []
        self._prev = "GENESIS"

    def append(self, event: str, device: str, qty: str = "",
               payload: Any = None) -> Dict[str, Any]:
        rec = {
            "ts": time.time(),
            "seq": len(self.entries),
            "event": event,          # read / write / escalate / error
            "device": device,
            "qty": qty,
            "payload": payload,
            "prev_hash": self._prev,
        }
        rec["hash"] = self._hash(rec)
        self.entries.append(rec)
        self._prev = rec["hash"]
        return rec

    # ---- sha256 chain ----
    @staticmethod
    def _hash(rec: Dict[str, Any]) -> str:
        body = json.dumps({k: rec[k] for k in
                           ("ts", "seq", "event", "device", "qty", "payload",
                            "prev_hash")},
                          sort_keys=True, default=str).encode()
        return hashlib.sha256(body).hexdigest()

    # ---- export / verify ----
    def export(self, path: str) -> None:
        with open(path, "w") as f:
            json.dump({"name": self.name, "root_hash": self._prev,
                       "entries": self.entries}, f, indent=2, default=str)

    @classmethod
    def from_file(cls, path: str) -> "AuditLog":
        with open(path) as f:
            data = json.load(f)
        log = cls(data["name"])
        log.entries = data["entries"]
        log._prev = data["root_hash"]
        return log

    def verify(self) -> bool:
        prev = "GENESIS"
        for rec in self.entries:
            if rec["prev_hash"] != prev:
                return False
            body = json.dumps({k: rec[k] for k in
                               ("ts", "seq", "event", "device", "qty", "payload",
                                "prev_hash")},
                              sort_keys=True, default=str).encode()
            if hashlib.sha256(body).hexdigest() != rec["hash"]:
                return False
            prev = rec["hash"]
        return prev == self._prev


# ---- global collector so MHSDriver can log without coupling ----
_default_log: Optional[AuditLog] = None


def get_default_log() -> AuditLog:
    global _default_log
    if _default_log is None:
        _default_log = AuditLog()
    return _default_log


def collect_drivers(drivers, dest: AuditLog) -> int:
    """Flush each MHSDriver's flight list into an AuditLog (returns count)."""
    n = 0
    for d in drivers:
        for rec in d.flight:
            dest.append(rec["kind"], d.id, rec["qty"], rec["payload"])
            n += 1
        d.flight.clear()
    return n
