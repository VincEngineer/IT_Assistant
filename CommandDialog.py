import subprocess
from PyQt6.QtWidgets import QPushButton, QVBoxLayout, QFileDialog, QLineEdit, QDialog, QLabel
from PyQt6.QtCore import pyqtSlot, QStandardPaths
import configparser
import os  # Import for getting the file extension

'''
This class is for the Main Panel and Holds the functionality of the GUI Config button, 
such Functionality is used to find the file you need to execute with Button 1 or Button 2.
'''


class CommandInputDialog(QDialog):
    def __init__(self, button_identifier, parent=None):
        super().__init__(parent)
        self.button_identifier = button_identifier
        self.layout = QVBoxLayout()

        self.command_label = QLabel("Search for the file to be executed or Enter the command manually")
        self.command_input = QLineEdit()

        self.file_button = QPushButton("Search")
        self.save_button = QPushButton("Save")

        self.file_button.clicked.connect(self.search_file)
        self.save_button.clicked.connect(self.save_command)

        self.layout.addWidget(self.command_label)
        self.layout.addWidget(self.command_input)
        self.layout.addWidget(self.file_button)
        self.layout.addWidget(self.save_button)

        self.setLayout(self.layout)

        self.populate_existing_command()

    '''
    It will populate the command that is saved in the config.ini
     file to the dialog box for the user to avoid looking into the config.ini file. 
    '''

    def populate_existing_command(self):
        config = configparser.ConfigParser()
        config.read("config.ini")
        if "File_Paths" in config.sections():
            if self.button_identifier in config["File_Paths"]:
                existing_command = config["File_Paths"][self.button_identifier]
                self.command_input.setText(existing_command)

    '''
    It will search for a file and will use the method 'suggest_command_based_on_file'
     to automatically add the given command to the dialog box 'QLineEdit()'
    '''

    @pyqtSlot()
    def search_file(self):
        file_dialog = QFileDialog(self)
        file_path, _ = file_dialog.getOpenFileName()
        if file_path:
            suggested_command = self.suggest_command_based_on_file(file_path)
            self.command_input.setText(suggested_command)

    '''
    Suggest_command_based_on_file will add a command base on the file you search with 'search_file' method.
    Example: If you select a .py file, this will suggest a python3 command like 'python3 /path/to/file/script.py'
    '''
    def suggest_command_based_on_file(self, file_path):
        file_extension = os.path.splitext(file_path)[1]
        if file_extension == '.ovpn':
            return f"openvpn {file_path}"
        elif file_extension == '.py':
            return f"python3 {file_path}"
        elif file_extension == '.sh':
            return f"bash {file_path}"
        # Add more file types and corresponding command templates here
        else:
            return file_path  # return file_path as is if extension is not recognized

    '''
    Read the command from the config.ini file 
    from each button button1_command or button2_command
    '''

    @staticmethod
    def read_command_from_config(button_identifier):
        config = configparser.ConfigParser()
        config.read("config.ini")
        if "File_Paths" in config.sections():
            if button_identifier in config["File_Paths"]:
                return config["File_Paths"][button_identifier]
        return None

    '''
    The 'save_command' and 'save_to_config_ini' will work together 
    to properly save the command from the dialog box to the config.ini file
    '''

    @pyqtSlot()
    def save_command(self):
        command_or_path = self.command_input.text()
        if command_or_path:
            self.save_to_config_ini(command_or_path)
    @staticmethod
    def get_config_file_path():
        # Get the directory where the main script is located
        script_dir = os.path.dirname(os.path.realpath(__file__))
        # Return the full path to the config.ini file within the installation directory
        print(script_dir)
        return os.path.join(script_dir, "config.ini")

    '''
    This method will create the config.ini file.
    '''
    def save_to_config_ini(self, value):
        config_file_path = self.get_config_file_path()
        config = configparser.ConfigParser()
        config.read("config.ini")
        if "File_Paths" not in config.sections():
            config.add_section("File_Paths")
        config.set("File_Paths", self.button_identifier, value)
        with open(config_file_path, "w") as config_file:
            config.write(config_file)
