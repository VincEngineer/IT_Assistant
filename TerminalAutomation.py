import subprocess
import time

"""
It will automate the Terminator terminal by opening the terminator and then, 
it will run an xdotool comand to automate user keystroke.
"""


class TerminalAutomation:

    @staticmethod
    def open_terminator_and_execute_command(command):
        try:
            subprocess.Popen(["terminator", "-m", "-e", f"bash -c '{command}; bash'"])
            time.sleep(2)
            return True
        except Exception as e:
            print(f"An error occurred while opening terminator: {e}")
            return False

    @staticmethod
    def execute_xdotool_command(commands):
        try:
            subprocess.Popen(commands)
            return True
        except Exception as e:
            print(f"An error occurred while executing xdotool command: {e}")
            return False
