#!/bin/bash

GIT_PATH="$(which git)"
export git_path="$GIT_PATH"
WINDOWS_VENV="venv/Scripts/activate"
LINUX_VENV="venv/bin/activate"
VENV=""
if [ -f "$WINDOWS_VENV" ]; then
  VENV="$WINDOWS_VENV"
elif [ -f "$LINUX_VENV" ]; then
  VENV="$LINUX_VENV"
fi

if [ -z "$VENV" ]; then
    echo "======================================================================"
    echo "Sorry The Virtual Environment not found"
    echo "======================================================================"
    exit 1
fi

source "$VENV"
python tools/dev-clone-and-pull.py
pip install -r dev-requirements.txt
deactivate