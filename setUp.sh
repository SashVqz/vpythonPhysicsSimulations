#!/bin/bash

# This script sets up a virtual environment for the project
# chmod +x setup.sh
# ./setup.sh

VENV_DIR="testEnv"
python -m venv $VENV_DIR
source $VENV_DIR/bin/activate

pip install -r requirements.txt

echo "Virtual environment ready"

