import os

from PyQt5 import uic
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QColor, QPainter, QPen, QIcon
from PyQt5.QtWidgets import QLabel, QMainWindow, QDesktopWidget
from PyQt5.uic.properties import QtGui

from gui.GameSessionWindow import GameSessionWindow
from gui.RulesWindow import RulesWindow
from gui.SettingsWindow import SettingsWindow
from gui.TokenWindow import TokenWindow


class GameWindow(QMainWindow):
    CANVAS_SIZE = 720
    CANVAS_WIDTH = 745
    CANVAS_HEIGHT = 980
    FIXED_SIZE = 200
    BACKGROUND_COLOR = QColor('#FFFFFF')
    CELL_BORDER_WIDTH = 3
    LINE_COLOR = QColor(0, 0, 0)

    def __init__(self):
        super().__init__()

        self.token_window = TokenWindow()
        self.rules_window = RulesWindow()
        self.game_window = GameSessionWindow()



        self.init_ui()

    def init_ui(self):
        uic.loadUi('config_file/Menu.ui', self)
        self.setWindowTitle('Tetris')
        self.setWindowIcon(QIcon('images/icon.png'))

        self.newGameButton.clicked.connect(self.new_game_btn)

        # При выборе игры через токен хочу получить окно ввода токена
        self.enterTokenButton.clicked.connect(self.token_game_btn)

        self.center_window()

    def new_game_btn(self):
        self.close()
        self.game_window.start_new_game("config_file/settings.json")

    #  Показываю окно с вводом токена
    def token_game_btn(self):
        self.token_window.show_token_dialog()
        self.close()

    def play_game(self):
        print("Игра началась")

    def center_window(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
