#!/usr/bin/env bash
set -e

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
OUT_DIR="$ROOT_DIR/out"
VENV_DIR="$ROOT_DIR/.venv"

echo ""
echo "[cleanup]-[LOG]: Cleaning up build artifacts and temporary files..."

# remove out dir
if [ -d "$OUT_DIR" ]; then
    echo "[cleanup]-[LOG]: Removing '$OUT_DIR'..."
    rm -rf "$OUT_DIR"
fi

# remove venv
if [ -d "$VENV_DIR" ]; then
    echo "[cleanup]-[LOG]: Removing '.venv'..."
    rm -rf "$VENV_DIR"
fi

# remove bytecode
echo "[cleanup]-[LOG]: Removing '__pycache__' directories..."
find "$ROOT_DIR" -type d -name "__pycache__" -exec rm -rf {} +

# remove pyinstaller build files
echo "[cleanup]-[LOG]: Removing pyinstaller build folders..."
find "$ROOT_DIR" -type d -name "build" -exec rm -rf {} +

echo "[cleanup]-[LOG]: Cleanup complete!"
echo ""
