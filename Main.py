from PyQt6.QtWidgets import QApplication
from MainWindow import MainWindow

# Application Entry Point
if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.setGeometry(2450, 400, 650, 450)
    window.show()
    app.exec()
