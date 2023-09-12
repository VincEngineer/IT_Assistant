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

# Clone repository
# git clone https://github.com/your-username/your-repo.git

# Navigate into the directory and install
cd IT_Assistant

# Get the current username
CURRENT_USER=$(whoami)

# Get the current directory
CURRENT_DIR=$(pwd)

# Make the script executable
chmod +x Main.py

# Create a systemd service
echo "[Unit]
Description=IT_Assistant
After=network.target

[Service]
ExecStart=/usr/bin/python3 $CURRENT_DIR/Main.py
User=$CURRENT_USER
Restart=always

[Install]
WantedBy=multi-user.target" | sudo tee /etc/systemd/system/IT_Assistant.service

# Reload systemd, enable and start the service
sudo systemctl daemon-reload
sudo systemctl enable IT_Assistant.service
sudo systemctl start IT_Assistant.service
