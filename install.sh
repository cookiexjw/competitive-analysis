#!/usr/bin/env bash

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SRC_DIR="$SCRIPT_DIR/competitive-analysis"
DEST_DIR="${HOME}/.codex/skills/competitive-analysis"

if [[ ! -d "$SRC_DIR" ]]; then
  echo "Error: skill directory not found: $SRC_DIR" >&2
  exit 1
fi

mkdir -p "$DEST_DIR"
rm -rf "$DEST_DIR"/*
cp -R "$SRC_DIR"/. "$DEST_DIR"/

echo "Installed competitive-analysis skill to:"
echo "  $DEST_DIR"
echo
echo "You can now ask Codex:"
echo "  做竞品分析"
echo "or:"
echo "  帮我做一版竞品调研"
