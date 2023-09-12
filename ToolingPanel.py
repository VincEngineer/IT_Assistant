from PyQt6.QtWidgets import QPushButton, QVBoxLayout, QWidget
from GuiConnector import ssh_and_terminator, VPNManager
from PyQt6.QtCore import pyqtSlot
dark_theme_button = "QPushButton { background-color: black; color: white; }" \
                    "QPushButton:hover { background-color: grey; color: black; }"


class ToolingPanel(QWidget):
    """Configuration Panel containing various buttons for configuration."""

    def __init__(self, parent=None):
        """Initialize the Configuration Panel."""
        super().__init__(parent)
        self.vpn_manager = None
        self.HTB_VPN = None
        self.HTB_Terminator = None
        self.layout = None
        self.configButton2 = None
        self.configButton1 = None
        self.setup_variables()
        self.setup_layout_settings()
        self.setup_layout()

    def setup_variables(self):
        """Setup all class-level variables."""
        self.layout = QVBoxLayout()
        self.HTB_Terminator = QPushButton("Terminator (HTB)", self)
        self.HTB_VPN = QPushButton("Start OpenVPN (HTB)", self)
        self.vpn_manager = VPNManager()

    def setup_layout_settings(self):
        """Setup settings to make it work layout components."""
        # Connecting buttons to functions
        self.HTB_Terminator.clicked.connect(ssh_and_terminator)
        self.HTB_VPN.clicked.connect(self.toggle_button_vpn)
        self.HTB_VPN.setCheckable(True)
        # Styling buttons
        self.HTB_Terminator.setStyleSheet(dark_theme_button)
        self.HTB_VPN.setStyleSheet(dark_theme_button)

        # Adding buttons to layout
        self.layout.addWidget(self.HTB_Terminator)
        self.layout.addWidget(self.HTB_VPN)

    def setup_layout(self):
        """Finalize layout by adding components."""
        self.setLayout(self.layout)

    @pyqtSlot(bool)
    def toggle_button_vpn(self, checked):
        """Start or stop VPN based on the button state."""
        self.vpn_manager.toggle_vpn(checked)
        if checked:
            self.HTB_VPN.setText('Stop OpenVPN (HTB)')
        else:
            self.HTB_VPN.setText('Start OpenVPN (HTB)')
