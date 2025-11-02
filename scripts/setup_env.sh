#!/usr/bin/env bash
set -e

echo ""
echo "[setup_env]-[LOG]: Setting up environment..."

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
VENV_DIR="$ROOT_DIR/.venv"

# installed needed packages
if command -v apt >/dev/null 2>&1; then
    echo "[setup_env]-[LOG]: Installing system packages (python3-dev, python3-venv, build-essential)..."
    sudo apt update
    sudo apt install -y python3-dev python3-venv python3-pip build-essential
fi

# create venv if doesnt exist
if [ ! -d "$VENV_DIR" ]; then
    echo "[setup_env]-[LOG]: Creating virtual environment..."
    python3 -m venv "$VENV_DIR"
fi

# activate venv
source "$VENV_DIR/bin/activate"

# upgrade pip inside venv
echo "[setup_env]-[LOG]: Upgrading pip..."
pip install --upgrade pip

# install dependencies unless 'requirements.txt' not found
if [ -f "$ROOT_DIR/requirements.txt" ]; then
    echo "[setup_env]-[LOG]: Installing dependencies from requirements.txt..."
    pip install -r "$ROOT_DIR/requirements.txt"
else
    echo "[setup_env]-[WARN]: requirements.txt not found; skipping dependency install."
fi

# install pyinstaller if not already installed
if ! pip show pyinstaller > /dev/null 2>&1; then
    echo "[setup_env]-[LOG]: Installing PyInstaller..."
    pip install pyinstaller
else
    echo "[setup_env]-[LOG]: PyInstaller already installed."
fi

echo "[setup_env]-[LOG]: Setup complete! You can now run:"
echo "    python main.py   # or"
echo "    ./scripts/build.sh   # to build the executable"
echo ""
