from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget
from PyQt5.uic.properties import QtCore


class RulesWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        uic.loadUi('config_file/Rules.ui', self)
        self.errorCheckBox.setStyleSheet("color: red;")
        self.setWindowTitle("Game rules")
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowCloseButtonHint)

    def show_rules(self):
        self.show()
        self.startGameBtn.clicked.connect(
            lambda: self.close() if self.readRules.isChecked()
            else self.errorCheckBox.setText("Подтвердите, что вы ознакомились с правилами."))

