#!/bin/bash
IS_IGNORE_VENV="$1"
if [ -z "$IS_IGNORE_VENV" ]; then
  echo "======================================================================"
  echo "Connecting to Virtual Environment......."
  echo "======================================================================"

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
fi


echo "Calling Development Library Clone and Pull Script"
echo "-------------------------------------------------------------------------------"
python tools/dev-clone-and-pull.py

echo "Installing Development Dependencies"
echo "-------------------------------------------------------------------------------"
pip install -r dev-requirements.txt


if [ -z "$IS_IGNORE_VENV" ]; then
  deactivate
fi