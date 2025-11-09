#!/bin/bash

echo "This is a setup script for Linux systems. Please make sure you are running this on a Linux machine or Linux subsystem like WSL. If you do not have them download them."
echo "Are you sure you want to continue? (Y/n)"
read answer
if [ "$answer" != "y" ] && [ "$answer" != "" ]; then
    echo "Exiting setup."
    exit 1
fi

sudo apt update -y
sudo apt upgrade -y

sudo apt install nodejs -y
nvm install 22.12
sudo apt install npm -y
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash

if ! command -v python3 &> /dev/null; then
    echo "Installing Python3..."
    sudo apt install python3 -y
fi

sudo apt install python3-pip -y
sudo apt install python3-venv -y

# Setup backend
cd ..
cd flask_backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
deactivate

# Setup frontend
cd ..
cd react_frontend
npm install

cd ..

clear
echo "---------------"
echo "Setup complete!"
echo "---------------"
