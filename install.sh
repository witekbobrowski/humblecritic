#!/usr/bin/env bash

script="$0"
basename="$(dirname $script)"

error=0
output_device="/dev/tty"

# Help
display_help() {
    echo "instal.sh installs humblecritic python script and its dependencies listed in requirements.txt."
    echo
    echo "humblecritic is a script that scrapes humblebundle.com bundle page for items, so it can later be reviewed. Script will call the appropriate API (ex. www.goodreads.com), try to find an item in database and if it suceeds, ask for rating for that item. At the end the avarage rating for bundle will be displayed."
    echo
    echo "Source available at: https://github.com/witekbobrowski/humblecritic"
    echo
    echo "Usage: ./instal.sh [--help] [-h]"
    echo
    echo "Options:"
    echo "	-h | --help 	Show help"
    echo "	-q | --quiet 	Run quietly - hide all output"
    echo "	-v | --verbose 	Output all logs to stdout. (default on)"
    exit $error
}

# End program early with error
error() {
    if [[ $1 != "" ]]; then
        echo -e "[!] Unknown option: \`$1\`"
        echo
        display_help
    fi
}

# Checking for options
while [[ $# -gt 0 ]]; do
    error=1
    case "$1" in
        -h|--help) display_help ;;
        -q|--quiet) output_device="/dev/null"; shift ;;
        -v|--verbose) output_device="/dev/tty"; shift ;;
        -*) error $1 ;;
        *) shift ;;
    esac
done

# Installing Requirements
requirements_path=$basename"/requirements.txt"
echo "Installing requirements from $requirements_path..." &> $output_device
pip3 install -r $requirements_path  &> $output_device || {
    echo "[ERROR] Failure while installing requirements. Package was not installed!" &> $output_device
    exit 1
}
echo "Success" &> $output_device

# Looking for rc file
echo "Looking for rc file at \"${HOME}/.humblecriticrc\"" &> $output_device
if ! [[ -f "${HOME}/.humblecriticrc" ]]; then
    echo "[WARNING] rc file is missing!" &> $output_device
    printf "# Configuration file for humblecritic\n# URL: github.com/witekbobrowski/humblecritic\n" > "${HOME}/.humblecriticrc" &> $output_device
    echo "rc file was created at \"${HOME}/.humblecriticrc\"" &> $output_device
else
    echo "Success" &> $output_device
fi

setup_path=$basename"/setup.py"
# Testing package
echo "Testing package..." &> $output_device
python3 $setup_path -q test &> $output_device || {
    echo "[ERROR] Failure while testing package. Package was not installed!" &> $output_device
    exit 1
}
echo "Success" &> $output_device

# Cleaning package
echo "Cleaning package..." &> $output_device
python3 $setup_path clean &> $output_device || {
    echo "[ERROR] Failure while cleaning package. Package was not installed!" &> $output_device
    exit 1
}
echo "Success" &> $output_device

# Installing package
echo "Installing package..." &> $output_device
python3 $setup_path install --user &> $output_device || {
    echo "[ERROR] Failure while installing package. Package was not installed!" &> $output_device
    exit 1
}

# Create symbolic link
echo "Creating Symbolic link to humblecritic in /usr/local/bin/ ..." &> $output_device
USER_BASE=$(python3 -c "from site import USER_BASE; print(USER_BASE)")
ln -s $USER_BASE "/bin/humblecritic" "/usr/local/bin/humblecritic" &> $output_device
echo "Success" &> $output_device
