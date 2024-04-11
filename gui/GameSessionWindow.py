from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QPixmap, QPainter, QPen
from PyQt5.QtWidgets import QMainWindow, QLabel, QDesktopWidget

from game_logic.Game import Game
from gui.RulesWindow import RulesWindow


class GameSessionWindow(QMainWindow):
    CANVAS_SIZE = 720
    CANVAS_WIDTH = 745
    CANVAS_HEIGHT = 980
    FIXED_SIZE = 200
    CELL_BORDER_WIDTH = 3
    LINE_COLOR = QColor(0, 0, 0)
    BACKGROUND_COLOR = QColor(255, 255, 255)

    def __init__(self):
        super().__init__()
        self.rules_window = RulesWindow()

        self.game = None
        self.is_rules_shown = False

        self.points = QLabel(self)
        self.label = QLabel(self)

        self.init_ui()

    def init_ui(self):
        uic.loadUi('config_file/GameSessionWindow.ui', self)

        canvas = QPixmap(721, 721)
        canvas.fill(Qt.gray)

        self.canvas.setPixmap(canvas)
        self.center_window()

    def start_new_game(self):
        print("Initializing new game...")
        self.game = Game("config_file/settings.json")
        self.setWindowTitle(f"Game/{self.game.token}")
        self.show()

        # если правила ещё не показывал - показываю
        if not self.is_rules_shown or not self.rules_window.readRules.isChecked():
            self.rules_window.show_rules()
            self.is_rules_shown = True

    def draw_cells(self):
        painter = QPainter(self)
        painter.setPen(QPen(QColor(0, 0, 0), self.CELL_BORDER_WIDTH))
        painter.setBrush(QColor(0, 0, 0))
        painter.drawRect(0, 0, 500, 500)

    def center_window(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
