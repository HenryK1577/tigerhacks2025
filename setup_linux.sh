#!/bin/bash
echo "This is a setup script for Linux systems. Please make sure you are running this on a Linux machine or Linux subsystem like WSL. If you do not have them download them."
echo "Are you sure you want to continue? (Y/n)"
read answer
if [ "$answer" != "y" ] && [ "$answer" != "" ]; then
    echo "Exiting setup."
    exit 1
fi

sudo apt update
sudo apt upgrade
sudo apt install pip

python3 --version
if [ $? -ne 0 ]; then
    pip install python3
fi
python3 -m venv .venv
pip install -r requirements.txt

clear

echo "---------------"
echo "Setup complete!"
echo "---------------"

