"""
The GuiConnector.py Connects the Graphical Interface with the Logic of the code.
Example:
    GuiConnector is what is in the middle of the GUi and the backend or the logic of the Software.
    in short word, from here we mainly craft function to be passed as a signal slot to the buttons
"""
from RunFile import ScriptExecution
from WebDataFetcher import HTBMachineStatus
from TerminalAutomation import TerminalAutomation
from colorama import Fore
import subprocess
from CommandDialog import CommandInputDialog
import threading
from PyQt6.QtCore import pyqtSlot

'''
This class is for the Tool panel, and it is for managing 
the VPN toggle button that is located in the ToolingPanel.py
'''


class VPNManager:
    def __init__(self):
        # Setup Commands to be executed:
        self.openvpn_command = 'openvpn /home/kali/Downloads/lab_Jonias.ovpn'
        self.kill_command = 'pkill -f openvpn'

    def execute_openvpn(self):
        try:
            connector = ScriptExecution(self.openvpn_command)
            connector.run_script()
        except Exception as e:
            print(f"An error occurred while executing OpenVPN: {e}")

    def close_resource_openvpn(self):
        try:
            subprocess.Popen(self.kill_command, shell=True)
            print(f"Command executed: {self.kill_command}")
        except Exception as e:
            print(f"An error occurred while closing OpenVPN: {e}")

    def toggle_vpn(self, is_enabled):
        if is_enabled:
            self.execute_openvpn()
        else:
            self.close_resource_openvpn()


'''
This Function is  for the Tool Panel and will 
Execute terminator + an SSH session if Pwnbox is executed in hack the box
'''


@pyqtSlot()
def ssh_and_terminator():
    # -----------SETTING UP VARIABLES-----------:
    # credentials:
    email_address = ""
    user_password = ""
    # instances:
    terminal_automation_instance = TerminalAutomation()
    htb_status_instance = HTBMachineStatus(email_address, user_password)
    # commands:
    ssh_command = " "
    xdotool_command = " "

    # -----------STARTING THE EXECUTION---------:

    # HTB STATUS:
    if htb_status_instance.login():
        print(Fore.GREEN + "[+] HTB Login successful.")
        print(Fore.RESET)
        # Fetching Machine status:
        htb_status_instance.fetch_machine_status()
        # Using Machine Status into ssh_command:
        ssh_command = f"sshpass -p {htb_status_instance.vnc_password} ssh -o StrictHostKeyChecking=no {htb_status_instance.user_name}@{htb_status_instance.hostname}"

    else:
        print(Fore.RED + "[-] HTB Login failed. Please check your Credentials in 'GuiConnector.py'")
        print(Fore.RESET)

    # SSH COMMAND:
    print("[!] Attempting to open SSH.")
    if terminal_automation_instance.open_terminator_and_execute_command(ssh_command):
        print(Fore.GREEN + f"SSH Executed: {ssh_command}")
        print(Fore.RESET)
    else:
        print(Fore.RED + "[-] Failed to open SSH. Make sure you Spawned the Pwnbox in Hack the box first")
        print(Fore.RESET)

    # XDOTOOL COMMAND:
    xdotool_command = ["xdotool", "key", "ctrl+shift+o"]
    if terminal_automation_instance.execute_xdotool_command(xdotool_command):
        print(Fore.GREEN + "[+] xdotool executed.")
        print(Fore.RESET)
    else:
        print(Fore.RED + "Failed to execute xdotool.")
        print(Fore.RESET)


'''
This function is for the Main Panel and will 
Execute Button 1 or Button 2, depend of what argument is passed to button_identifier
'''


@pyqtSlot(str)
def open_terminal_and_run_command(button_identifier):
    try:
        command = CommandInputDialog.read_command_from_config(button_identifier)
        # "X-terminal-emulator" will be used to grab the terminal you have by default,
        # if is not working, set terminator by defauls or change this command.
        subprocess.Popen(["x-terminal-emulator", "--command", f"bash -c '{command}; exec bash'"], shell=False)
    except Exception as e:
        print(f"An error occurred: {e}")

        def wrapper():
            open_terminal_and_run_command(button_identifier)

        # Create a thread that runs the function
        thread = threading.Thread(target=wrapper)

        thread.start()
