#!/usr/bin/env bash
# Собирает самодостаточный пакет для приёмки V6 на месте (без git, без интернета).
#   ./make_handoff_bundle.sh            -> dist/argus-os1-acceptance-<дата>.tar.gz
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DATE="$(date +%F)"
NAME="argus-os1-acceptance-$DATE"
DIST="$ROOT/dist"; STAGE="$DIST/$NAME"
rm -rf "$STAGE"; mkdir -p "$STAGE/pipeline" "$STAGE/firmware/vendor/sangaboard-v1.0.4" "$STAGE/docs" "$STAGE/tests" "$STAGE/hardware"

cp "$ROOT"/software/pipeline/*.py "$STAGE/pipeline/"
cp "$ROOT"/software/pipeline/*.sh "$STAGE/pipeline/"
cp "$ROOT"/software/pipeline/README.md "$ROOT"/software/pipeline/RUN_ME.md "$STAGE/pipeline/"
cp "$ROOT"/software/tests/test_pipeline.py "$STAGE/tests/"
cp "$ROOT"/firmware/vendor/sangaboard-v1.0.4/* "$STAGE/firmware/vendor/sangaboard-v1.0.4/" 2>/dev/null || true
cp "$ROOT"/docs/ARGUS_OS1_Scan_Acceptance_Runbook_2026-11-18.md "$STAGE/docs/" 2>/dev/null || true
cp "$ROOT"/docs/ARGUS_Forum_Intel_OFM_2026-11-18.md "$STAGE/docs/" 2>/dev/null || true
cp "$ROOT"/hardware/PROVENANCE_V6.md "$STAGE/hardware/" 2>/dev/null || true
chmod +x "$STAGE"/pipeline/*.sh

( cd "$STAGE" && find . -type f ! -name SHA256SUMS -exec sha256sum {} + | sort -k2 > SHA256SUMS )
tar -czf "$DIST/$NAME.tar.gz" -C "$DIST" "$NAME"
sha256sum "$DIST/$NAME.tar.gz" | tee "$DIST/$NAME.tar.gz.sha256"
du -h "$DIST/$NAME.tar.gz"
echo "готово: $DIST/$NAME.tar.gz"
