#!/bin/bash

echo "[clean.sh]:  Starting clean..."

rm -rf ./modules/__pycache__
echo "[clean.sh]: Removed './modules/__pycache__'"

rm -rf ./modules/utils/__pycache__
echo "[clean.sh]: Removed './modules/utils/__pycache__'"

echo "[clean.sh]: Finished clean!"
