#!/bin/bash
# Marp slide layout checker using agent-browser.
#
# Builds HTML from Marp markdown, opens in agent-browser,
# and captures each slide as a screenshot.
#
# Usage:
#   bash skills/layout-fix/scripts/check-layout.sh <deck.md>
#   bash skills/layout-fix/scripts/check-layout.sh <deck.md> --theme <css>
#   bash skills/layout-fix/scripts/check-layout.sh --cleanup <dir>

set -euo pipefail

THEME_CANDIDATES=("MIYAKOH.css" "rector.css" "theme.css")

# --- Parse arguments ---
DECK=""
THEME=""
CLEANUP=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    --theme)  THEME="$2"; shift 2 ;;
    --cleanup) CLEANUP="$2"; shift 2 ;;
    *)        DECK="$1"; shift ;;
  esac
done

# --- Cleanup mode ---
if [[ -n "$CLEANUP" ]]; then
  if [[ -d "$CLEANUP" ]]; then
    rm -rf "$CLEANUP"
    echo "Cleaned up: $CLEANUP"
  fi
  exit 0
fi

# --- Validate deck path ---
if [[ -z "$DECK" ]]; then
  echo "Usage: bash check-layout.sh <deck.md> [--theme <css>] [--cleanup <dir>]" >&2
  exit 1
fi

DECK=$(cd "$(dirname "$DECK")" && pwd)/$(basename "$DECK")
if [[ ! -f "$DECK" ]]; then
  echo "Error: $DECK not found" >&2
  exit 1
fi

DECK_DIR=$(dirname "$DECK")

# --- Auto-detect theme ---
if [[ -z "$THEME" ]]; then
  for candidate in "${THEME_CANDIDATES[@]}"; do
    if [[ -f "$DECK_DIR/$candidate" ]]; then
      THEME="$DECK_DIR/$candidate"
      break
    fi
  done
fi

if [[ -z "$THEME" || ! -f "$THEME" ]]; then
  echo "Error: Theme CSS not found. Use --theme to specify." >&2
  exit 1
fi

# --- Build HTML via marp-cli ---
HTML_PATH="${DECK%.md}.html"
echo "Building HTML..." >&2
npx --yes @marp-team/marp-cli "$DECK" \
  --theme-set "$THEME" \
  --html \
  --allow-local-files \
  --output "$HTML_PATH" 2>&1 | cat >&2

# --- Capture screenshots via agent-browser ---
SCREENSHOT_DIR=$(mktemp -d /tmp/marp-layout-XXXXXX)
echo "Capturing slides with agent-browser..." >&2

# Open the HTML file
agent-browser open "file://$HTML_PATH" --width 1920 --height 1080 2>/dev/null

# Wait for page load
sleep 1

# Get slide count by evaluating JS in the page
TOTAL=$(agent-browser eval "document.querySelectorAll('section[id]').length" 2>/dev/null | grep -oE '[0-9]+' | head -1)

if [[ -z "$TOTAL" || "$TOTAL" -eq 0 ]]; then
  echo "Error: No slides found in HTML" >&2
  agent-browser close 2>/dev/null
  exit 1
fi

# Screenshot each slide
for i in $(seq 1 "$TOTAL"); do
  agent-browser open "file://${HTML_PATH}#${i}" 2>/dev/null
  sleep 0.3
  OUT=$(printf "%s/slide-%03d.png" "$SCREENSHOT_DIR" "$i")
  agent-browser screenshot "$OUT" 2>/dev/null
done

agent-browser close 2>/dev/null

# --- Output ---
echo "${TOTAL} slides captured" >&2
echo "SCREENSHOT_DIR=$SCREENSHOT_DIR"
for i in $(seq 1 "$TOTAL"); do
  printf "%s/slide-%03d.png\n" "$SCREENSHOT_DIR" "$i"
done
