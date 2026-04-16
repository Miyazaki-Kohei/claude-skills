#!/bin/bash
# Clean up screenshot directory and optionally HTML files.
#
# Usage:
#   bash skills/layout-fix/scripts/cleanup.sh <screenshot-dir>

set -euo pipefail

if [[ $# -eq 0 ]]; then
  echo "Usage: bash cleanup.sh <screenshot-dir>" >&2
  exit 1
fi

DIR="$1"
if [[ -d "$DIR" ]]; then
  rm -rf "$DIR"
  echo "Cleaned up: $DIR"
else
  echo "Directory not found: $DIR" >&2
fi
