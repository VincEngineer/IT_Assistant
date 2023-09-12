from PyQt6.QtWidgets import QPushButton, QVBoxLayout, QWidget, QHBoxLayout, QDialog
from CommandDialog import CommandInputDialog
from GuiConnector import open_terminal_and_run_command
from PyQt6.QtCore import pyqtSlot
dark_theme_button = "QPushButton { background-color: black; color: white; }" \
                    "QPushButton:hover { background-color: grey; color: black; }"


class MainPanel(QWidget):
    """The Button Panel containing various buttons for user actions."""

    def __init__(self, parent=None):
        """Initialize the Button Panel."""
        super().__init__(parent)
        self.small_button2 = None
        self.small_button1 = None
        self.layout = None
        self.layout_top = None
        self.layout_bottom = None
        self.button1 = None
        self.button2 = None
        self.setup_variables()
        self.setup_layout_settings()
        self.setup_layout()

    def setup_variables(self):
        """Setup all class-level variables."""
        # Layouts
        self.layout = QVBoxLayout()
        self.layout_top = QHBoxLayout()
        self.layout_bottom = QHBoxLayout()
        # Buttons
        self.button1 = QPushButton("Button 1", self)
        self.button2 = QPushButton('Button 2')
        self.button2.setCheckable(True)
        # Small buttons for command setup
        self.small_button1 = QPushButton("Config", self)
        self.small_button2 = QPushButton("Config", self)

    def setup_layout_settings(self):
        """Setup settings for layout components."""
        # Connecting buttons to functions

        # Click button execution
        self.button1.clicked.connect(lambda: open_terminal_and_run_command("button1_command"))
        self.button2.clicked.connect(lambda: open_terminal_and_run_command("button2_command"))

        # Small buttons (config)
        self.small_button1.clicked.connect(self.config_button)
        self.small_button2.clicked.connect(self.config_button)

        # Styling buttons
        self.button1.setStyleSheet(dark_theme_button)
        self.button2.setStyleSheet(dark_theme_button)

        # Adding buttons to layout
        self.layout_top.addWidget(self.button1)
        self.layout_top.addWidget(self.small_button1)
        self.layout_top.addWidget(self.button2)
        self.layout_top.addWidget(self.small_button2)

    def setup_layout(self):
        """Finalize layout by adding components."""
        # Adding sub-layouts to main layout
        self.layout.addLayout(self.layout_top)
        self.layout.addLayout(self.layout_bottom)

        # Set layout for this QWidget
        self.setLayout(self.layout)
    '''
    config_button used to pop up the dialog box, basically all that is in the 'CommandDialog.py' file.
    '''
    @pyqtSlot()
    def config_button(self):
        clicked_button = self.sender()
        if clicked_button == self.small_button1:
            button_identifier = "button1_command"
        elif clicked_button == self.small_button2:
            button_identifier = "button2_command"
        else:
            button_identifier = "unknown_button"

        self.dialog = CommandInputDialog(button_identifier, self)  # Pass the identifier
        result = self.dialog.exec()

        if result == QDialog.DialogCode.Accepted:
            command = self.dialog.command_input.text()
            # File path would be saved within the dialog itself
            print(f"Entered command: {command}")
            # Save these details for use with the main button's function


