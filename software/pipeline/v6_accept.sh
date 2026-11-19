#!/usr/bin/env bash
# ARGUS-OS1 V6 — приёмка одной командой.
#
#   ./v6_accept.sh --demo                 # самопроверка всей цепочки без железа
#   ./v6_accept.sh --discover             # найти сервер микроскопа в локальной сети
#   ./v6_accept.sh --url http://scope.local:5000 --scan ~/scan_x
#   ./v6_accept.sh --url ... --scan ... --rom-frames ~/traverse --step-um 5
#
# Что делает: (1) при необходимости измеряет ROM по кадрам траверса;
# (2) прогоняет QC скана, сэмплинг-гейт, сшивку; (3) собирает отчёт A1–A7
# в hardware/acceptance_<дата>.md. Exit 0 — только если все проверки PASS.

set -uo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$HERE/../.." && pwd)"
PY="${PYTHON:-python3}"

URL=""
SCAN=""
ROM_FRAMES=""
ROM_IN=""
STEP_UM=""
MPP_UM="0.0388"        # 40x/0.75 dry + Pi HQ, 1.55 um pitch -> 39 nm/px
BINNING="1"
AXIS="x"
OVERLAP="0.35"
DEMO=""
DISCOVER=""
OUT=""

say()  { printf '%s\n' "$*"; }
head2() { printf '\n=== %s ===\n' "$*"; }
die()  { printf 'ОШИБКА: %s\n' "$*" >&2; exit 2; }

while [ $# -gt 0 ]; do
  case "$1" in
    --url)        URL="$2"; shift 2 ;;
    --scan)       SCAN="$2"; shift 2 ;;
    --rom-frames) ROM_FRAMES="$2"; shift 2 ;;
    --step-um)    STEP_UM="$2"; shift 2 ;;
    --mpp-um)     MPP_UM="$2"; shift 2 ;;
    --binning)    BINNING="$2"; shift 2 ;;
    --axis)       AXIS="$2"; shift 2 ;;
    --overlap)    OVERLAP="$2"; shift 2 ;;
    --rom-mm)     ROM_IN="$2"; shift 2 ;;
    --out)        OUT="$2"; shift 2 ;;
    --demo)       DEMO=1; shift ;;
    --discover)   DISCOVER=1; shift ;;
    -h|--help)    sed -n '2,14p' "$0"; exit 0 ;;
    *)            die "неизвестный аргумент: $1" ;;
  esac
done

# ---------------------------------------------------------------- зависимости
head2 "проверка окружения"
$PY - <<'EOF' || exit 2
import importlib, sys
need = {"numpy": "numpy", "cv2": "opencv-python", "scipy": "scipy", "skimage": "scikit-image"}
missing = []
for mod, pkg in need.items():
    try:
        importlib.import_module(mod)
    except Exception:
        missing.append(pkg)
if missing:
    print("ОШИБКА: не хватает пакетов:", ", ".join(missing))
    print("Установить: python3 -m pip install " + " ".join(missing))
    sys.exit(2)
print("пакеты на месте; python", sys.version.split()[0])
EOF

# ---------------------------------------------------------------- поиск сервера
if [ -n "$DISCOVER" ] && [ -z "$URL" ]; then
  head2 "поиск сервера микроскопа в локальной сети"
  URL="$($PY - <<'EOF'
import json, socket, urllib.request, concurrent.futures as cf

def up(url, timeout=1.2):
    try:
        with urllib.request.urlopen(url, timeout=timeout) as r:
            body = r.read(20_000).decode("utf-8", "replace")
            return r.status, body
    except Exception:
        return 0, ""

names = ["microscope.local", "raspberrypi.local", "ofm.local", "openflexure.local"]
cands = []
for n in names:
    try:
        ip = socket.gethostbyname(n)
        cands += [f"http://{n}:5000", f"http://{ip}:5000", f"http://{n}"]
    except Exception:
        pass

routes = []
try:
    import subprocess
    out = subprocess.run(["ip", "-4", "addr", "show", "scope", "global"], capture_output=True, text=True).stdout
    for line in out.splitlines():
        line = line.strip()
        if line.startswith("inet "):
            routes.append(line.split()[1].rsplit(".", 1)[0])
except Exception:
    pass

def port_open(host, port, t=0.25):
    s = socket.socket(); s.settimeout(t)
    try:
        return s.connect_ex((host, port)) == 0
    finally:
        s.close()

hosts = []
for pref in routes:
    with cf.ThreadPoolExecutor(256) as ex:
        for ip, ok in zip([f"{pref}.{i}" for i in range(1, 255)],
                          ex.map(lambda i: port_open(f"{pref}.{i}", 5000), range(1, 255))):
            if ok:
                hosts.append(ip)
cands = [f"http://{h}:5000" for h in hosts] + cands

for url in cands:
    for path in ("/api/v2/", "/api/v3/", "/api/v2/instrument/settings", "/"):
        code, body = up(url.rstrip("/") + path)
        if code and 200 <= code < 400:
            print(url)
            raise SystemExit(0)
print("")
EOF
)"
  if [ -n "$URL" ]; then say "найден: $URL"; else say "сервер не найден (порт 5000 закрыт на всех хостах) — A1/A2 останутся UNKNOWN"; fi
fi

# ---------------------------------------------------------------- демо-режим
WORK=""
if [ -n "$DEMO" ]; then
  head2 "демо: генерация фантома (мозаика + траверс)"
  WORK="$(mktemp -d /tmp/argus_demo.XXXXXX)"
  $PY "$HERE/phantom.py" "$WORK/mosaic" --size 1080 --tile 400 --overlap 0.35 || die "phantom"
  $PY - "$WORK" <<'EOF' || die "traverse"
import sys, os, cv2, numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath("__file__")))
from phantom import make_ground_truth
work = sys.argv[1]
os.makedirs(os.path.join(work, "traverse"), exist_ok=True)
gt = make_ground_truth(8200, seed=11)
rng = np.random.default_rng(3)
step, tile, n = 120, 400, 40
for i in range(n):
    patch = gt[2000:2000 + tile, i * step:i * step + tile].copy()
    gain = np.linspace(0.9, 1.1, tile, dtype=np.float32)[None, :, None]
    out = np.clip(patch * gain + rng.normal(0, 0.006, patch.shape), 0, 1)
    cv2.imwrite(os.path.join(work, "traverse", f"frame_{i:03d}.png"), (out * 255).astype(np.uint8))
print(f"траверс: {n} кадров, шаг 120 px = {120*0.0388:.2f} µm")
EOF
  head2 "демо: запись scan_data.json (как его пишет сервер микроскопа)"
  $PY - "$WORK/mosaic" <<'EOF' || die "scan_data"
import sys, os
sys.path.insert(0, os.getcwd())
from tiles import load_tiles, register, save_scan_data_like
d = sys.argv[1]
tiles = load_tiles(d)
register(tiles)
save_scan_data_like(os.path.join(d, "scan_data.json"), tiles, mpp_um=0.0388, overlap=0.35)
print(f"scan_data.json: {len(tiles)} полей, {tiles[0].w}x{tiles[0].h} px, capture_mode=full")
EOF
  SCAN="$WORK/mosaic"
  ROM_FRAMES="$WORK/traverse"
  STEP_UM="4.66"
fi

[ -n "$ROM_IN" ] && ROM_MM="$ROM_IN"

if [ -z "$SCAN" ] && [ -z "$URL" ]; then
  if [ -n "$DISCOVER" ]; then
    die "сервер в локальной сети не найден: укажи --url http://<IP>:5000 вручную (адрес виден в OpenFlexure Connect) либо запусти --demo для самопроверки"
  fi
  die "нужен --url и/или --scan (или --demo / --discover). См. --help"
fi

# ---------------------------------------------------------------- ROM
ROM_MM=""
if [ -n "$ROM_FRAMES" ] && [ -d "$ROM_FRAMES" ]; then
  head2 "A5: измерение ROM по кадрам траверса"
  ROM_JSON="$($PY "$HERE/measure_rom.py" "$ROM_FRAMES" --mpp-um "$MPP_UM" --axis "$AXIS" ${STEP_UM:+--step-um "$STEP_UM"} | tee /dev/stderr)"
  ROM_MM="$(printf '%s\n' "$ROM_JSON" | awk -F': *' '/measured_travel_mm/{print $2}')"
  RATIO="$(printf '%s\n' "$ROM_JSON" | awk -F': *' '/measured\/commanded/{print $2}')"
  say "ROM = ${ROM_MM} мм${RATIO:+ (измерено/скомандовано = ${RATIO})}"
  if [ -n "$DEMO" ]; then
    say "демо: траверс короткий по построению (проверяется точность шага, не полный ход) → A5 не оценивается"
    ROM_MM=""
  elif awk -v r="$ROM_MM" 'BEGIN{exit !(r < 1.0)}'; then
    say "ВНИМАНИЕ: измеренный ход < 1 мм — похоже на короткий траверс; A5 не оценивается"
    ROM_MM=""
  fi
fi

# ---------------------------------------------------------------- скан: QC + сшивка
if [ -n "$SCAN" ] && [ -d "$SCAN" ]; then
  head2 "A3/A4: QC скана"
  $PY "$HERE/qc.py" scan "$SCAN" --seconds-per-field 3 || say "→ QC вернул FAIL (см. выше)"

  head2 "A7: сшивка (fusion) + швы"
  TIFF="$(dirname "${SCAN%/}")/stitched_$(date +%Y%m%d).tif"
  $PY "$HERE/blend.py" "$SCAN" --out "$TIFF" --overlap "$OVERLAP" 2>/dev/null \
    && say "сшивка: $TIFF" || say "сшивка не выполнена (см. qc.py scan)"
fi

# ---------------------------------------------------------------- отчёт A1–A7
head2 "отчёт приёмки A1–A7"
OUT="${OUT:-$ROOT/hardware/acceptance_$(date +%F).md}"
mkdir -p "$(dirname "$OUT")"
ARGS=()
[ -n "$URL" ]  && ARGS+=(--url "$URL")
[ -n "$SCAN" ] && ARGS+=(--scan "$SCAN")
[ -n "$ROM_MM" ] && ARGS+=(--rom-mm "$ROM_MM")
ARGS+=(--mpp-um "$MPP_UM" --binning "$BINNING" --overlap "$OVERLAP" --out "$OUT")
$PY "$HERE/acceptance.py" "${ARGS[@]}"
RC=$?

say ""
say "отчёт: $OUT"
[ -n "$WORK" ] && say "демо-данные: $WORK"
exit $RC
