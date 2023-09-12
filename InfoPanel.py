from PyQt6.QtWidgets import QVBoxLayout, QWidget

'''
under development
'''


class InfoPanel(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.vertical_layout = None
        self.setup_variables()
        self.setup_layout()

    def setup_variables(self):
        """Initialize all class-level variables."""
        self.vertical_layout = QVBoxLayout()
        # Add any other variables you might need, e.g., buttons, labels, etc.

    def setup_layout(self):
        """Set up the layout for this panel."""
        # Add widgets to layout if you have any
        # Example: self.vertical_layout.addWidget(self.some_button)
        self.setLayout(self.vertical_layout)
