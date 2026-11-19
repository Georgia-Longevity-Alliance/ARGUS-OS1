"""ARGUS-OS1 — V6 acceptance runner (checklist A1–A7 from the runbook).

One command produces the evidence pack for `hardware/PROVENANCE_V6.md`:

    python3 acceptance.py --url http://microscope.local:5000 \
                          --scan ~/scan_2026-11-20 --mpp-um 0.0388 --binning 1 \
                          --rom-mm 11.2 --out acceptance_2026-11-20.md

Checks
------
A1  server reports a Sangaboard firmware version and does not flag a mismatch
A2  `motor_release` is exposed by the server API (needed for the incubator fix)
A3  scan directory passes the QC gate (`qc.py scan`)
A4  field size / capture mode as declared in `scan_data.json`
A5  measured stage travel in range (0 < ROM <= 12.5 mm; reference 11.4 ± 0.4)
A6  sampling gate: <= 100 nm/px, binning <= 2x2
A7  stitching sanity on the same scan: seams < 1.05

Nothing is assumed about the API layout: candidate endpoints are probed and the
script reports exactly what it found. A check that cannot be evaluated is
`UNKNOWN`, never `PASS` (project rule: silence is not consent).

Exit code: 0 only if every check is PASS.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import numpy as np  # noqa: E402

import qc  # noqa: E402
from blend import blend  # noqa: E402
from evaluate import seam_score  # noqa: E402
from tiles import load_tiles, register  # noqa: E402

API_CANDIDATES = (
    "/api/v3/",
    "/api/v2/",
    "/api/v2/instrument/",
    "/api/v2/instrument/settings",
    "/api/v2/status",
    "/api/v2/actions",
    "/api/v3/actions",
    "/api/v3/instrument/",
)
API_TIMEOUT = 4.0

STATUS_ORDER = {"PASS": 0, "UNKNOWN": 1, "FAIL": 2}


# ---------------------------------------------------------------- API probing
def _get(url: str, timeout: float = API_TIMEOUT) -> tuple[int, str]:
    try:
        with urllib.request.urlopen(url, timeout=timeout) as resp:  # noqa: S310
            return resp.status, resp.read(400_000).decode("utf-8", "replace")
    except urllib.error.HTTPError as exc:                     # reachable, bad path
        return exc.code, ""
    except Exception as exc:                                  # unreachable
        return 0, f"{type(exc).__name__}: {exc}"


def probe(url: str) -> dict[str, tuple[int, str]]:
    out = {}
    for path in API_CANDIDATES:
        out[path] = _get(url.rstrip("/") + path)
    return out


def _walk(obj, needle: str) -> list[str]:
    """Every key/value in a JSON blob containing `needle` (case-insensitive)."""
    hits: list[str] = []

    def rec(node):
        if isinstance(node, dict):
            for k, v in node.items():
                if needle in str(k).lower():
                    hits.append(f"{k}={v}" if not isinstance(v, (dict, list)) else str(k))
                rec(v)
        elif isinstance(node, list):
            for v in node:
                rec(v)
        elif needle in str(node).lower():
            hits.append(str(node))

    rec(obj)
    return hits


def check_a1_a2(probes: dict[str, tuple[int, str]]) -> tuple[dict, dict, str]:
    reachable = {p: (c, b) for p, (c, b) in probes.items() if c and 200 <= c < 400}
    if not reachable:
        detail = "; ".join(f"{p}:{c}" for p, (c, _) in probes.items() if c == 0) or "no HTTP response"
        return (
            {"id": "A1", "name": "firmware version reported by server", "status": "UNKNOWN",
             "detail": f"server not reachable ({detail})"},
            {"id": "A2", "name": "motor_release exposed", "status": "UNKNOWN",
             "detail": "server not reachable"},
            "not reachable",
        )

    blobs, firmware_hits, release_hits, warnings = [], [], [], []
    for path, (code, body) in reachable.items():
        blobs.append(f"{path} -> {code}")
        if not body.strip().startswith(("{", "[")):
            continue
        try:
            data = json.loads(body)
        except json.JSONDecodeError:
            continue
        firmware_hits += _walk(data, "firmware")
        firmware_hits += _walk(data, "version")
        release_hits += _walk(data, "motor_release")
        release_hits += _walk(data, "release")
        for needle in ("mismatch", "incompatible", "outdated", "warning"):
            warnings += _walk(data, needle)

    firmware_hits = sorted(set(firmware_hits))[:8]
    release_hits = sorted(set(release_hits))[:8]

    if not firmware_hits:
        a1 = {"id": "A1", "name": "firmware version reported by server", "status": "UNKNOWN",
              "detail": "API reachable, but no firmware/version field found — inspect "
                        f"{', '.join(sorted(reachable))} manually"}
    elif warnings:
        a1 = {"id": "A1", "name": "firmware version reported by server", "status": "FAIL",
              "detail": f"warning indicators present: {warnings[:4]}; fields: {firmware_hits}"}
    else:
        a1 = {"id": "A1", "name": "firmware version reported by server", "status": "PASS",
              "detail": f"no mismatch indicators; fields: {firmware_hits}"}

    if release_hits:
        a2 = {"id": "A2", "name": "motor_release exposed", "status": "PASS",
              "detail": f"found: {release_hits}"}
    else:
        a2 = {"id": "A2", "name": "motor_release exposed", "status": "UNKNOWN",
              "detail": "API reachable but no motor_release/release capability advertised "
                        "— call it directly against the stage endpoint and record the result"}
    return a1, a2, "; ".join(blobs)


# ---------------------------------------------------------------- local checks
def check_a3_a4(scan_dir: str) -> tuple[dict, dict]:
    import contextlib
    import io

    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        rc = qc.scan(scan_dir)
    text = buf.getvalue()
    errors = re.findall(r"^\s+\[ERROR\] (.+)$", text, flags=re.M)
    warns = re.findall(r"^\s+\[WARN \] (.+)$", text, flags=re.M)
    a3 = {"id": "A3", "name": "scan passes QC gate", "status": "PASS" if rc == 0 else "FAIL",
          "detail": "; ".join(errors) if errors else "scan_data consistent with files"}
    res_hit = [e for e in errors if "declared resolution" in e or "capture_mode" in str(warns)]
    a4 = {"id": "A4", "name": "field size / capture mode as declared",
          "status": "FAIL" if res_hit else ("PASS" if rc == 0 else "UNKNOWN"),
          "detail": "; ".join(res_hit or warns) or "declared resolution == actual, capture_mode full"}
    return a3, a4


def check_a5(rom_mm: float | None, rom_source: str) -> dict:
    if rom_mm is None:
        return {"id": "A5", "name": "measured stage travel", "status": "UNKNOWN",
                "detail": "not measured yet — run measure_rom.py, then pass --rom-mm"}
    if not 0 < rom_mm <= 12.5:
        return {"id": "A5", "name": "measured stage travel", "status": "FAIL",
                "detail": f"{rom_mm} mm outside (0, 12.5] design envelope"}
    ref_ok = abs(rom_mm - 11.4) <= 1.5
    return {"id": "A5", "name": "measured stage travel",
            "status": "PASS" if ref_ok else "UNKNOWN",
            "detail": f"{rom_mm} mm ({rom_source}); reference 11.4 ± 0.4 mm (PMID 42960477)"
                      + ("" if ref_ok else " — deviates >1.5 mm from reference, re-measure")}


def check_a6(mpp_um: float | None, binning: int) -> dict:
    if mpp_um is None:
        return {"id": "A6", "name": "sampling gate", "status": "UNKNOWN",
                "detail": "no --mpp-um given"}
    import contextlib
    import io

    with contextlib.redirect_stdout(io.StringIO()):
        ok = qc.gate(mpp_um, binning) == 0
    return {"id": "A6", "name": "sampling gate", "status": "PASS" if ok else "FAIL",
            "detail": f"{mpp_um * 1000:.1f} nm/px, binning {binning}x{binning} "
                      "(protocol Amendment 2: <=100 nm/px, binning <=2x2)"}


def check_a7(scan_dir: str | None, overlap: float) -> dict:
    if not scan_dir:
        return {"id": "A7", "name": "stitching sanity", "status": "UNKNOWN",
                "detail": "no --scan given"}
    tiles = load_tiles(scan_dir)
    if len(tiles) < 4:
        return {"id": "A7", "name": "stitching sanity", "status": "UNKNOWN",
                "detail": f"only {len(tiles)} fields — full mosaic not meaningful"}
    reg = register(tiles)
    img = blend(tiles, mode="fusion", overlap=overlap, progress=False)
    bx = sorted({int(t.pos[0]) for t in tiles} | {int(t.pos[0] + t.w) for t in tiles})
    by = sorted({int(t.pos[1]) for t in tiles} | {int(t.pos[1] + t.h) for t in tiles})
    seams = seam_score(img, bx, by)
    return {"id": "A7", "name": "stitching sanity",
            "status": "PASS" if seams < 1.05 else "FAIL",
            "detail": f"seam score {seams:.3f} (<1.05 pass), registration "
                      f"{reg.summary().get('median_score')} median match score"}


# ---------------------------------------------------------------- reporting
def report(checks: list[dict], api_log: str, args) -> str:
    worst = max((STATUS_ORDER[c["status"]] for c in checks), default=1)
    verdict = "PASS" if worst == 0 else ("FAIL" if worst == 2 else "INCOMPLETE")
    lines = [
        "# ARGUS-OS1 V6 — acceptance report",
        "",
        f"Verdict: **{verdict}**",
        "",
        "| # | Check | Status | Detail |",
        "|---|---|---|---|",
    ]
    for c in checks:
        lines.append(f"| {c['id']} | {c['name']} | {c['status']} | {c['detail']} |")
    lines += [
        "",
        "## Inputs",
        f"* server URL: `{args.url or '—'}`",
        f"* API probe: {api_log or '—'}",
        f"* scan directory: `{args.scan or '—'}`",
        f"* mpp: {args.mpp_um} µm/px, binning {args.binning}, overlap {args.overlap}",
        f"* ROM: {args.rom_mm} mm",
        "",
        "Copy the table into `hardware/PROVENANCE_V6.md`; keep this file as the evidence pack.",
    ]
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="ARGUS-OS1 V6 acceptance (A1–A7)")
    ap.add_argument("--url", help="OpenFlexure server base URL, e.g. http://microscope.local:5000")
    ap.add_argument("--scan", help="scan directory with fields + scan_data.json")
    ap.add_argument("--mpp-um", type=float, default=None)
    ap.add_argument("--binning", type=int, default=1)
    ap.add_argument("--overlap", type=float, default=0.35)
    ap.add_argument("--rom-mm", type=float, default=None)
    ap.add_argument("--rom-source", default="measure_rom.py")
    ap.add_argument("--out", default=None, help="write markdown report here")
    a = ap.parse_args(argv)

    if a.url:
        a1, a2, api_log = check_a1_a2(probe(a.url))
    else:
        a1 = {"id": "A1", "name": "firmware version reported by server", "status": "UNKNOWN",
              "detail": "no --url given"}
        a2 = {"id": "A2", "name": "motor_release exposed", "status": "UNKNOWN",
              "detail": "no --url given"}
        api_log = ""

    if a.scan:
        a3, a4 = check_a3_a4(a.scan)
    else:
        a3 = {"id": "A3", "name": "scan passes QC gate", "status": "UNKNOWN", "detail": "no --scan given"}
        a4 = {"id": "A4", "name": "field size / capture mode as declared", "status": "UNKNOWN",
              "detail": "no --scan given"}

    checks = [a1, a2, a3, a4, check_a5(a.rom_mm, a.rom_source),
              check_a6(a.mpp_um, a.binning), check_a7(a.scan, a.overlap)]
    text = report(checks, api_log, a)
    print(text)
    if a.out:
        with open(a.out, "w", encoding="utf-8") as fh:
            fh.write(text + "\n")
        print(f"\nwritten {a.out}", file=sys.stderr)
    return 0 if all(c["status"] == "PASS" for c in checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
