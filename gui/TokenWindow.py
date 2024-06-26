import os

from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QLineEdit, QMainWindow, QVBoxLayout, QPushButton

from gui.GameSessionWindow import GameSessionWindow

class TokenWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.game_window = GameSessionWindow()
        self.init_ui()

    def init_ui(self):
        uic.loadUi('config_file/TokenWindow.ui', self)
        self.tokenError.setStyleSheet("color: red;")
        self.setWindowTitle("Enter token")

    def show_token_dialog(self):
        self.show()
        self.okButton.clicked.connect(lambda: self.check_entry_token())
        self.backButton.clicked.connect(lambda: self.back_to_menu())

    # Проверяю есть ли такой токен в списке игр, если да - начинаю игру по токену.
    def check_entry_token(self):
        token = self.inputLabel.text()
        print(token)
        for filename in os.listdir("game_sessions"):
            if token == filename[:len(filename) - 5]:  # т.к знаю что все файлы json - просто обрежу срезом .json
                self.tokenError.clear()
                self.inputLabel.clear()
                print("Success!")
                self.close()
                self.game_window = GameSessionWindow()
                self.game_window.start_new_game(f"game_sessions/{filename}")
                break
            else:
                self.tokenError.setText("Токен не найден! Повторите попытку.")

    def back_to_menu(self):
        self.inputLabel.clear()
        self.tokenError.clear()
        self.close()







