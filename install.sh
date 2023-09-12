#!/bin/bash
# install.sh
# Check if the script is being run as root
if [ "$(id -u)" != "0" ]; then
    echo -e "\e[33mPlease run this script as root.\e[0m"
    exit 1
fi
# Update package list and install dependencies
sudo apt-get update
sudo apt-get install '^libxcb.*-dev' libx11-xcb-dev libglu1-mesa-dev libxrender-dev libxi-dev
sudo apt-get install dbus-x11
sudo apt-get install terminator
sudo apt-get install sshpass
sudo apt-get install -y python3-pip git
sudo apt-get install dbus-x11
sudo apt-get install terminator
sudo apt-get install sshpass
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

# Get the full path of the current directory
script_dir=$(pwd)


# Make the script executable
chmod +x Main.py

# Install as a systemd service
echo "[Unit]
Description=IT_Assistant
After=network.target

[Service]
ExecStart=/usr/bin/python3 $script_dir/Main.py
Restart=always

[Install]
WantedBy=multi-user.target" | sudo tee /etc/systemd/system/IT_Assistant.service

# Reload systemd, enable and start the service
sudo systemctl daemon-reload
sudo systemctl enable IT_Assistant.service
sudo systemctl start IT_Assistant.service
