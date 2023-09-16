- Install::

apt-get install git
git clone https://github.com/VincEngineer/IT_Assistant.git
cd IT_Assistant && chmod +x install.sh
./install.sh


- Software Details:

# IT_Assistant
This software is used to run Scripts with one click in Linux.


NOTE: To configure the Tooling panel, you can do it in GuiConnector.py, add your hack the box account, and it will retrieve your information from HTB and will log you in the spawned pwnbox. (you should have the pwnbox spawned already)

It has three features:

1. The Main Panel contains two programmable buttons, so you need to configure every button by searching for the file/script you want to execute or simply adding the command in the config button. Then, you can execute your command whenever you press the first or the second button.

2. in the tooling panel, we have 1 Terminator (HTB); this is for Hack the Box. Before executing this tool, you must add your Hack the Box credentials in one of the .py files (GuiConnector.py).

3. Also, the second button that is located in the Tooling panel, is called 'Start OpenVPN(HTB),' and this is to start Hack the box VPN; you only need to provide the path in the (GuiConnector.py) of where you stored your ovpn file and every time you press that button, it will toggle the VPN to start.
