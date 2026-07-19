#!/bin/bash
# ARGUS-LP_OS auto-push watcher
# Monitors project directory and auto-commits+pushed after 60s of no changes
# Run as systemd user service or: nohup bash scripts/watchdog.sh &

WATCH_DIR="$HOME/Desktop/Marketing/ARGUS-LP_OS"
DEBOUNCE=60
LAST_CHANGE=0

inotifywait -m -r -e modify,create,delete,move --exclude '.git/' "$WATCH_DIR" 2>/dev/null | while read -r path event file; do
    LAST_CHANGE=$(date +%s)
    (
        sleep "$DEBOUNCE"
        NOW=$(date +%s)
        if [ $((NOW - LAST_CHANGE)) -ge $DEBOUNCE ]; then
            cd "$WATCH_DIR" || exit
            if ! git diff --quiet --exit-code || [ -n "$(git ls-files --others --exclude-standard)" ]; then
                git add -A
                git commit -m "auto: $(date '+%Y-%m-%d %H:%M')" --allow-empty-message
                git push origin main 2>&1 | tail -1
            fi
        fi
    ) &
done
