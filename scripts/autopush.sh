#!/bin/bash
# ARGUS-OS1 auto-push script
# Usage: bash scripts/autopush.sh [commit message]

set -e
cd ~/Desktop/Marketing/ARGUS-OS1

MSG="${1:-auto: $(date '+%Y-%m-%d %H:%M')}"

git add -A
if git diff --cached --quiet; then
    echo "Nothing to commit."
    exit 0
fi
git commit -m "$MSG"
git push origin main
echo "✅ Pushed to Georgia-Longevity-Alliance/ARGUS-OS1"
