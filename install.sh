#!/usr/bin/env bash

echo "Installing requirements..."
pip3 install -r requirements.txt || {
    echo "[ERROR] Failure while installing requirements."
    exit 1
}
echo "Success"

echo "Looking for rc file..."
if ! [[ -f "~/.humblecriticrc" ]]; then
    echo "[WARNING] rc file is missing!"
else
    echo "Success"
fi

echo "Testing package..."
python3 setup.py test || {
    echo "[ERROR] Failure while testing package."
    exit 1
}
echo "Success"

echo "Installing package..."
python3 setup.py install || {
    echo "[ERROR] Failure while installing package."
    exit 1
}
echo "Success"
