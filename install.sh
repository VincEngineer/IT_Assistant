#!/bin/bash
# install.sh

# Update package list and install dependencies
sudo apt-get update -y
sudo apt-get install -y '^libxcb.*-dev' libx11-xcb-dev libglu1-mesa-dev libxrender-dev libxi-dev
sudo apt-get install -y dbus-x11
sudo apt-get install -y terminator
sudo apt-get install -y sshpass
sudo apt-get install -y python3-pip git
# Python dependencies
pip install --upgrade pip
pip install colorama
pip install PyQt6
pip install configparser
pip install requests

# Navigate into the directory and install
cd IT_Assistant

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
Categories=Utility;" > "/usr/share/applications/IT_Assistant.desktop"

# Update desktop database
update-desktop-database

# Optional: Create a symlink on the Desktop
ln -s "/usr/share/applications/IT_Assistant.desktop" "/home/${CURRENT_USER}/Desktop/IT_Assistant.desktop"