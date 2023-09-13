#!/bin/bash
# install.sh

# Update package list and install dependencies
sudo apt-get update -y
sudo apt-get install -y '^libxcb.*-dev' libx11-xcb-dev libglu1-mesa-dev libxrender-dev libxi-dev
sudo apt-get install -y dbus-x11
sudo apt-get install -y terminator
sudo apt-get install -y sshpass
sudo apt-get install -y python3-pip git

# Get the current username
CURRENT_USER=$(whoami)

# Get the current directory
CURRENT_DIR=$(pwd)

# Make the script executable
chmod +x Main.py

# Create the .desktop file
echo "[Desktop Entry]
Version=1.0
Name=IT Assistant
Comment=Your IT Assistant
Exec=/usr/bin/python3 ${CURRENT_DIR}/Main.py
Icon=${CURRENT_DIR}/Kali_Linux_Red.ico
Terminal=false
Type=Application
Categories=Utility;" | sudo tee "/usr/share/applications/IT_Assistant.desktop"

# Update desktop database
sudo update-desktop-database

# Python dependencies
pip install --user --upgrade pip
pip install --user colorama
pip install --user PyQt6
pip install --user configparser
pip install --user requests




# Check for Desktop Entry
if [ -e "/usr/share/applications/IT_Assistant.desktop" ]; then
    echo "Desktop Entry exists."
else
    echo "Desktop Entry does not exist."
    exit 1
fi

# Check for Desktop directory
if [ -d "/home/${CURRENT_USER}/Desktop/" ]; then
    echo "Desktop directory exists."
    if [ -w "/home/${CURRENT_USER}/Desktop/" ]; then
        echo "Desktop directory is writable."
    else
        echo "Desktop directory is not writable."
        exit 1
    fi
else
    echo "Desktop directory does not exist."
    exit 1
fi

# Create the symlink
ln -s "/usr/share/applications/IT_Assistant.desktop" "/home/${CURRENT_USER}/Desktop/IT_Assistant.desktop"



