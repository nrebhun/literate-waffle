#!/usr/bin/env zsh

# Check for virtual environment
if [ ! -d ./venv/ ]; then
    echo "Virtual environment not found. Run the setup script before this one."
    exit 1
fi

# ACtivate virtual environment
source venv/bin/activate

python nasa_iotd.py

