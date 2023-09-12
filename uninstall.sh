#!/bin/bash

# Confirm the user wants to uninstall
read -p "Are you sure you want to uninstall [Your Software]? [y/n]: " confirm
if [ "$confirm" != "y" ]; then
  echo "Uninstallation canceled."
  exit 1
fi

# Remove the .desktop file
sudo rm /usr/share/applications/IT_Assistant.desktop

# Uninstall Python dependencies
pip uninstall colorama PyQt6 configparser requests -y

# Uninstall other dependencies
sudo apt-get remove --purge '^libxcb.*-dev' libx11-xcb-dev libglu1-mesa-dev libxrender-dev libxi-dev dbus-x11 terminator sshpass python3-pip git -y
sudo apt-get autoremove -y
sudo apt-get autoclean

echo -e "\033[0;32mThe uninstallation is complete. Please remove the software directory manually.\033[0m"

