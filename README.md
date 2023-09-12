# IT_Assistant
This sofware is used to run Scripts with 1 click in linux. and will be added to the systemctl, so you only need to enable it and start it.


NOTE:To configure the Tooling panel, you can do it in GuiConnector.py, add your hack the box account and it will retrieve your information from HTB and will logged you in the spawned pwnbox. (you should have the pwnbox spawned already)

It has 3 features:

1. The Main Panel contains 2 programmable buttons, so you just need to config every button by searching for the file/script you want to execute or simply adding the command in the config button. then you can execute your command every time you press the first o the second button.

2. in the tooling panel, we have 1 Terminator (HTB); this is for hack the box, before executing this tool, you need to add your Hack the box credentials in one of the .py files (GuiConnector.py).

3. Also, the second button that is located in the Tooling panel, is called 'Start OpenVPN(HTB)', and this is to start Hack the box VPN, you only need to provide the path in the (GuiConnector.py) of where you stored your ovpn file and every time you press that button, it will toggle the VPN to start.
