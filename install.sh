#!/usr/bin/env bash

echo "Installing requirements..."
pip3 install -r requirements.txt || {
    echo "[ERROR] Failure while installing requirements."
    exit 1
}
echo "Success"

echo "Looking for rc file at \"${HOME}/.humblecriticrc\""
if ! [[ -f "${HOME}/.humblecriticrc" ]]; then
    echo "[WARNING] rc file is missing!"
    printf "# Configuration file for humblecritic\n# URL: github.com/witekbobrowski/humblecritic\n" > "${HOME}/.humblecriticrc"
    echo "rc file was created at \"${HOME}/.humblecriticrc\""
else
    echo "Success"
fi

echo "Testing package..."
python3 setup.py -q test || {
    echo "[ERROR] Failure while testing package."
    exit 1
}
echo "Success"

echo "Cleaning package..."
python3 setup.py clean || {
    echo "[ERROR] Failure while cleaning package."
    exit 1
}
echo "Success"

echo "Installing package..."
python3 setup.py -q install || {
    echo "[ERROR] Failure while installing package."
    exit 1
}
echo "Success"
