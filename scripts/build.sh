#!/usr/bin/env bash
set -e

APP_NAME="Mosaic"
ENTRY_POINT="main.py"
ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
OUT_DIR="$ROOT_DIR/out"
VENV_DIR="$ROOT_DIR/.venv"

echo ""
echo "[build]-[LOG]: Building $APP_NAME..."

# activate virtual environment (i hate venv)
if [ -d "$VENV_DIR" ]; then
    source "$VENV_DIR/bin/activate"
else
    echo "[build]-[ERR]: Virtual environment not found. Run './scripts/setup_env.sh' first."
    exit 1
fi

# ensure pyinstaller is installed
if ! pip show pyinstaller > /dev/null 2>&1; then
    echo "[build]-[LOG]: Installing pyinstaller..."
    pip install pyinstaller
fi

# get output dir ready
rm -rf "$OUT_DIR"
mkdir -p "$OUT_DIR"

# build
WORK_DIR="$(mktemp -d)"  # tmp work directory for pyinstaller

if pyinstaller \
    --onefile \
    --name "$APP_NAME" \
    --distpath "$OUT_DIR" \
    --workpath "$WORK_DIR" \
    --specpath "$OUT_DIR" \
    "$ROOT_DIR/$ENTRY_POINT"; then

    echo "[build]-[LOG]: Build complete! Run with: './out/$APP_NAME'"
    echo ""
else
    echo "[build]-[ERR]: Build failed."
    echo ""
    exit 1
fi

# clean
rm -rf "$WORK_DIR"
