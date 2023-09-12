from PyQt6.QtWidgets import QMainWindow, QDockWidget, QListWidget, QListWidgetItem, QStackedWidget
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction
from InfoPanel import InfoPanel
from MainPanel import MainPanel
from ToolingPanel import ToolingPanel

dark_theme_button = "QPushButton { background-color: black; color: white; }" \
                    "QPushButton:hover { background-color: grey; color: black; }"


# Main application window class
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.stacked_widget = None
        self.button_panel = None
        self.config_panel = None
        self.info_panel = None
        self.sidebar = None
        self.sidebar_list = None

        self.toggle_action = None
        self.setup_variables()
        self.setup_layout_settings()
        self.setup_layout()

    def setup_variables(self):
        self.stacked_widget = QStackedWidget()
        self.button_panel = MainPanel(self)
        self.config_panel = ToolingPanel(self)
        self.info_panel = InfoPanel(self)
        self.sidebar = QDockWidget(self)
        self.sidebar_list = QListWidget()
        menu_bar = self.menuBar()
        self.toggle_action = QAction('Menu', self)
        menu_bar.addAction(self.toggle_action)

    def setup_layout_settings(self):
        self.toggle_action.triggered.connect(self.toggle_sidebar)
        self.sidebar_list.addItem(QListWidgetItem("Main"))
        self.sidebar_list.addItem(QListWidgetItem("Tools"))
        self.sidebar_list.addItem(QListWidgetItem("Info"))
        self.sidebar_list.itemClicked.connect(self.change_page)
        self.stacked_widget.addWidget(self.button_panel)
        self.stacked_widget.addWidget(self.config_panel)
        self.stacked_widget.addWidget(self.info_panel)

    def setup_layout(self):
        self.setWindowTitle("Scripting")
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint)
        self.setCentralWidget(self.stacked_widget)
        self.sidebar.setAllowedAreas(Qt.DockWidgetArea.AllDockWidgetAreas)
        self.sidebar.setWidget(self.sidebar_list)
        self.sidebar.setFixedWidth(120)
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.sidebar)

    def toggle_sidebar(self):
        if self.sidebar.isVisible():
            self.sidebar.hide()
        else:
            self.sidebar.show()

    def change_page(self, item):
        if item.text() == "Main":
            self.stacked_widget.setCurrentWidget(self.button_panel)
        elif item.text() == "Tools":
            self.stacked_widget.setCurrentWidget(self.config_panel)
        elif item.text() == "Info":
            self.stacked_widget.setCurrentWidget(self.info_panel)
