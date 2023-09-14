#!/bin/bash

# Function to print text in green
print_green() {
    printf "\e[32m$1\e[0m\n"
}

# Function to print text in red
print_red() {
    printf "\e[31m$1\e[0m\n"
}

# Check if the script is running as root
if [ "$EUID" -ne 0 ]; then
    print_red "Please run as root"
    exit 1
else
    print_green "Running as root"
fi

# Update package list and install dependencies
apt-get update -y
apt-get install -y '^libxcb.*-dev' libx11-xcb-dev libglu1-mesa-dev libxrender-dev libxi-dev
apt-get install -y dbus-x11 terminator sshpass python3-pip git

# Get the current username (not effective username because of sudo)
CURRENT_USER=$(who am i | awk '{print $1}')

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

# Switch to the regular user for pip installation
sudo -u ${CURRENT_USER} pip install --upgrade pip
sudo -u ${CURRENT_USER} pip install colorama PyQt6 configparser requests

# Check for Desktop Entry
if [ -e "/usr/share/applications/IT_Assistant.desktop" ]; then
    print_green "Desktop Entry exists."
else
    print_red "Desktop Entry does not exist."
    exit 1
fi

# Check for Desktop directory
if [ -d "/home/${CURRENT_USER}/Desktop/" ]; then
    print_green "Desktop directory exists."
    if [ -w "/home/${CURRENT_USER}/Desktop/" ]; then
        print_green "Desktop directory is writable."
    else
        print_red "Desktop directory is not writable."
        exit 1
    fi
else
    print_red "Desktop directory does not exist."
    exit 1
fi
'''
# Create the symlink
ln -s "/usr/share/applications/IT_Assistant.desktop" "/home/${CURRENT_USER}/Desktop/IT_Assistant.desktop"

if [ $? -eq 0 ]; then
    print_green "Symlink created successfully."
else
    print_red "Failed to create symlink."
    exit 1
fi
'''