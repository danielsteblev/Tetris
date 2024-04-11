from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QMainWindow


class SettingsWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setGeometry(20, 60, 400, 200)
        self.setWindowTitle('Settings')
        layout = QGridLayout(self)

