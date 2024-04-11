from PyQt5 import uic
from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtGui import QColor, QPixmap, QPainter, QPen
from PyQt5.QtWidgets import QMainWindow, QLabel, QDesktopWidget, QMessageBox

from game_logic.Game import Game
from game_logic.Logic import Logic
from gui.RulesWindow import RulesWindow


class GameSessionWindow(QMainWindow):
    CANVAS_SIZE = 720
    CANVAS_WIDTH = 721
    CANVAS_HEIGHT = 980
    FIXED_SIZE = 200
    CELL_BORDER_WIDTH = 3
    LINE_COLOR = QColor(0, 0, 0)
    BACKGROUND_COLOR = QColor(255, 255, 255)

    def __init__(self):
        super().__init__()
        self.figure = None
        self.rules_window = RulesWindow()

        self.game = None
        self.is_rules_shown = False

        self.init_ui()

    def init_ui(self):
        uic.loadUi('config_file/GameSessionWindow.ui', self)
        self.figure1.installEventFilter(self)

        canvas = QPixmap(721, 721)
        canvas.fill(Qt.gray)

        figure1 = QPixmap(200, 200)
        figure2 = QPixmap(200, 200)
        figure3 = QPixmap(200, 200)

        self.canvas.setPixmap(canvas)

        self.figure1.setPixmap(figure1)
        self.figure2.setPixmap(figure2)
        self.figure3.setPixmap(figure3)

        self.saveButton.clicked.connect(lambda: self.game.save_game())

        self.center_window()

    def start_new_game(self, config_file):
        print("Initializing new game...")
        self.game = Game(config_file)
        self.setWindowTitle(f"Game/{self.game.token}")
        # Тут по логике должен рисовать поле
        self.draw_cells()

        self.show()

        # если правила ещё не показывал - показываю
        if not self._is_rules_shown or not self.rules_window.readRules.isChecked():
            self.rules_window.show_rules()
            self._is_rules_shown = True

    def draw_cells(self):
        painter = QPainter(self.canvas.pixmap())
        painter.setPen(QPen(QColor(0, 0, 0), self.CELL_BORDER_WIDTH))

        painter_fig_1 = QPainter(self.figure1.pixmap())
        painter_fig_2 = QPainter(self.figure2.pixmap())
        painter_fig_3 = QPainter(self.figure3.pixmap())

        painter_fig_1.setPen(QPen(QColor(0, 0, 0), self.CELL_BORDER_WIDTH))
        painter.setBrush(QColor(0, 0, 0))

        painter_fig_2.setPen(QPen(QColor(0, 0, 0), self.CELL_BORDER_WIDTH))
        painter.setBrush(QColor(0, 0, 0))

        painter_fig_3.setPen(QPen(QColor(0, 0, 0), self.CELL_BORDER_WIDTH))
        painter.setBrush(QColor(0, 0, 0))

        cell_size = int(self.CANVAS_WIDTH / self.game.width)

        for i in range(5):
            for j in range(5):
                painter_fig_1.drawRect(i * 40, j * 40, 40, 40)
                painter_fig_2.drawRect(i * 40, j * 40, 40, 40)
                painter_fig_3.drawRect(i * 40, j * 40, 40, 40)

                painter_fig_1.setBrush(QColor(255, 255, 255))
                painter_fig_2.setBrush(QColor(255, 255, 255))
                painter_fig_3.setBrush(QColor(255, 255, 255))

                painter_fig_1.drawRect(i * 40 + 1, j * 40 + 1, 40, 40)
                painter_fig_2.drawRect(i * 40 + 1, j * 40 + 1, 40, 40)
                painter_fig_3.drawRect(i * 40 + 1, j * 40 + 1, 40, 40)

        cur_fugures = Logic.generate_cur_figures(self.game)

        painter_fig_1.end()
        painter_fig_2.end()
        painter_fig_3.end()

        # Черчу сетку
        for i in range(self.game.width):
            for j in range(self.game.height):
                cur_color = QColor(255, 255, 255)

                if self.game.board[i][j] == 1:
                    cur_color.setNamedColor("#f3ca20")

                self.draw_square(painter, QColor(0, 0, 0), i * cell_size, j * cell_size, cell_size)
                self.draw_square(painter, cur_color, i * cell_size + 1, j * cell_size + 1, cell_size)

        painter.end()
        self.update()

    def center_window(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Подтверждение выхода', 'Вы уверены, что хотите выйти? ВНИМАНИЕ! Не забудьте сохранить игру!',
                                     QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    @staticmethod
    def draw_square(painter, color, x, y, size):
        painter.setBrush(color)
        painter.drawRect(x, y, size, size)

    @property
    def is_rules_shown(self):
        return self._is_rules_shown

    @is_rules_shown.setter
    def is_rules_shown(self, value):
        self._is_rules_shown = value

    @property
    def is_game_saved(self):
        return self._is_game_saved

    @staticmethod
    def is_game_saved_true(self, value):
        self._is_game_saved = value
