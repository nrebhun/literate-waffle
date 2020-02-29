#!/usr/bin/env zsh

# Clean up old virtualenv
if [ -d ./venv/ ]; then
    echo "Removing existing python virtual environment..."
    rm -rf ./venv/
fi

echo "Setting up fresh python virtual environment..."
python3 -m venv venv

echo "Activating clean virtual environment..."
source venv/bin/activate

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Done! Clean python virtual environment set up with dependencies installed."
