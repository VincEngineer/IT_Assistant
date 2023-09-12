import os
import subprocess
import threading

'''
So far only using this to run the VPN. but we can also run .sh and .py files
'''


class ScriptExecution:
    def __init__(self, command):
        self.command = command.split()
        self.process = None
        self.extensions_that_require_terminal = ['.sh', '.py']

    """Adds an extension to the list of extensions that require a terminal."""

    def add_terminal_extension(self, extension):
        if extension not in self.extensions_that_require_terminal:
            self.extensions_that_require_terminal.append(extension)

    def run_script(self):

        def target_function():
            try:
                file_path = self.command[-1]  # Assuming the file path is the last argument
                file_extension = os.path.splitext(file_path)[1]
                file_name = os.path.basename(file_path)
                print("File Name ", file_name)
                if file_extension in self.extensions_that_require_terminal:
                    self.process = subprocess.Popen(
                        ["x-terminal-emulator", "-e"] + ["bash", "-c", f"{self.command[0]}; exec bash"])
                else:
                    self.process = subprocess.Popen(self.command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

                print(f"{file_name} opened.")
            except Exception as e:
                print(f"An error occurred while opening {file_name}: {e}")

        thread = threading.Thread(target=target_function)
        thread.start()


# Uncomment the below block for testing
'''
if __name__ == "__main__":
    command = 'openvpn /home/kali/Downloads/lab_Jonias.ovpn'
    # Open resources:    
    connector = ScriptExecution(command)
    connector.open_resource()
'''
