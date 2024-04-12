from random import choice

from PyQt5 import uic
from PyQt5.QtCore import Qt, QEvent, QMimeData
from PyQt5.QtGui import QColor, QPixmap, QPainter, QPen, QIcon, QDrag, QCursor
from PyQt5.QtWidgets import QMainWindow, QLabel, QDesktopWidget, QMessageBox
from PyQt5.uic.properties import QtCore

from game_logic import Figure
from game_logic.GameTetris import GameTetris
from game_logic.Logic import Logic
from gui.RulesWindow import RulesWindow


class GameSessionWindow(QMainWindow):
    CANVAS_SIZE = 722
    CANVAS_WIDTH = 723
    CANVAS_HEIGHT = 982
    CANVAS_FIGURE_SIZE = 200
    FIXED_SIZE = 200
    CELL_BORDER_WIDTH = 1
    CUR_FIGURES_CELL = 60
    LINE_COLOR = QColor(0, 0, 0)
    BACKGROUND_COLOR = QColor(255, 255, 255)
    CLOSE_CANVAS_RECT = Figure.CloseCanvasRect

    def __init__(self):
        super().__init__()

        self.cell_size = None
        self.figure = None

        self.rules_window = RulesWindow()

        self.cur_color = None

        self.game = None
        self.is_rules_shown = False

        self.init_ui()
        self.setMouseTracking(True)

    def init_ui(self):
        uic.loadUi('config_file/GameSessionWindow.ui', self)
        self.setWindowIcon(QIcon('images/icon.png'))
        self.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.saveButton.setStyleSheet("border: 1px solid black;")
        self.menuButton.setStyleSheet("border: 1px solid black;")



        canvas = QPixmap(721, 721)
        canvas.fill(Qt.gray)

        canvas_figure1 = QPixmap(200, 200)
        canvas_figure1.fill(QColor(255, 255, 255))

        canvas_figure2 = QPixmap(200, 200)
        canvas_figure2.fill(QColor(255, 255, 255))

        canvas_figure3 = QPixmap(200, 200)
        canvas_figure3.fill(QColor(255, 255, 255))

        self.canvas.setPixmap(canvas)

        self.figure1.setPixmap(canvas_figure1)

        self.figure2.setPixmap(canvas_figure2)

        self.figure3.setPixmap(canvas_figure3)

        self.saveButton.clicked.connect(lambda: self.game.save_game())

        self.center_window()

    def start_new_game(self, config_file):
        print("Initializing new game...")
        self.game = GameTetris(config_file)
        self.setWindowTitle(f"Game/{self.game.token}")
        self.score.setText(f"{self.game.score}")

        # Тут по логике должен рисовать поле
        self.draw_cells()
        # генерирую и рисую фигуры в лейбл
        self.draw_cur_figures()

        self.show()

        # если правила ещё не показывал - показываю
        if not self._is_rules_shown or not self.rules_window.readRules.isChecked():
            self.rules_window.show_rules()
            self._is_rules_shown = True

    def draw_cells(self):
        painter = QPainter(self.canvas.pixmap())
        painter.setPen(QPen(QColor(0, 0, 0), self.CELL_BORDER_WIDTH))

        self.cell_size = min(int(self.CANVAS_WIDTH / self.game.width), int(self.CANVAS_HEIGHT / self.game.height))

        # Черчу сетку
        for i in range(self.game.width):
            for j in range(self.game.height):
                cur_color = QColor(255, 255, 255)

                if self.game.board[i][j] == 1:
                    cur_color = self.game.cur_figures[0].color

                self.draw_square(painter, QColor(0, 0, 0), i * self.cell_size, j * self.cell_size, self.cell_size)
                self.draw_square(painter, cur_color, i * self.cell_size, j * self.cell_size, self.cell_size)

                Logic.check_lines(game=self.game)  # проверка полных линий
                self.score.setText(f"{self.game.score}")

        painter.end()
        self.update()

    def draw_cur_figures(self):
        # генерирую 3 фигуры
        cur_figures = Logic.generate_cur_figures(self.game)
        self.game.cur_figures = cur_figures

        # устанавливаю настройки для отслеживания перемещений и т.д
        self.label_set_mouse_settings(self.figure1, self.figure2, self.figure3)


        # черчу 3 фигуры
        self.draw_figure_in_label(self.figure1, self.game.cur_figures[0])
        self.draw_figure_in_label(self.figure2, self.game.cur_figures[1])
        self.draw_figure_in_label(self.figure3, self.game.cur_figures[2])

    #  метод для отрисовки фигуры в лейбле
    def draw_figure_in_label(self, label, figure):
        painter = QPainter(label.pixmap())
        painter.setPen(QPen(QColor(0, 0, 0), self.CELL_BORDER_WIDTH))

        # перед рисованием всегда под ним рисую фон
        self.draw_square(painter, QColor(255, 255, 255), -1, -1, label.width() + 1)
        print(label.x(), label.y(), label.width())

        for j in range(len(figure.shape)):
            for k in range(len(figure.shape[j])):
                if figure.shape[j][k] == 1:
                    self.draw_square(painter, figure.color,
                                     j * self.CUR_FIGURES_CELL, k * self.CUR_FIGURES_CELL, self.CUR_FIGURES_CELL)

        painter.end()

    def center_window(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Подтверждение выхода',
                                     'Вы уверены, что хотите выйти? ВНИМАНИЕ! Не забудьте сохранить игру!',
                                     QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def label_set_mouse_settings(self, *args):
        for label in args:
            label.setMouseTracking(True)
            label.setCursor(QCursor(Qt.OpenHandCursor))
            label.mouseMoveEvent = self.mouseMoveEvent
            label.mouseReleaseEvent = self.mouseReleaseEvent

    # def mouse_move(self, event, label):  # перемещение мыши
    #     mouse_pos = event.pos()
    #     if event.buttons() == Qt.LeftButton:
    #         label.move(label.pos() + event.pos())
    #         print(mouse_pos)

    def mouseMoveEvent(self, event):  # перемещение мыши
        mouse_pos = event.pos()
        if event.buttons() == Qt.LeftButton:
            self.figure1.move(self.figure1.pos() + event.pos())
            print(mouse_pos)

    # def mouse_release(self, event, label):  # отпускаю мышь
    #     print("Мышь отпущена!")
    #
    #     start_x = label.pos().x()
    #     start_y = label.pos().y()
    #     print(start_x, start_y)
    #
    #     x, y = label.pos().x(), label.pos().y()
    #     print(x, y)
    #
    #     #  если в пределах игрового поля
    #     if self.canvas.x() < x < self.canvas.x() + self.canvas.width() \
    #             and self.canvas.y() < y < self.canvas.y() + self.canvas.height():
    #
    #         cell_row = y // self.cell_size
    #         cell_col = x // self.cell_size
    #
    #         cur_f = self.game.cur_figures[label[-1]]
    #
    #         self.add_figure_to_board(cell_x=cell_col, cell_y=cell_row, figure=cur_f)
    #
    #         self.clear_label(label, start_x, start_y)
    #
    #         self.draw_cells()
    #
    #     else:
    #         print("Фигура вне игрового поля!")
    #         label.move(start_x, start_y)
    #
    #     self.update()

    def mouseReleaseEvent(self, event):  # отпускаю мышь
        print("Мышь отпущена!")

        x, y = self.figure1.pos().x(), self.figure1.pos().y()
        print(x, y)

        #  если в пределах игрового поля
        if self.canvas.x() < x < self.canvas.x() + self.canvas.width() \
                and self.canvas.y() < y < self.canvas.y() + self.canvas.height():

            cell_row = y // self.cell_size
            cell_col = x // self.cell_size

            cur_f = self.game.cur_figures[0]

            can_drag = self.can_drag_fugire(cur_f, cell_col, cell_row)

            # self.figure2.clear()
            # self.figure3.clear()
            if can_drag:
                self.add_figure_to_board(cell_x=cell_col, cell_y=cell_row, figure=cur_f)
                self.draw_cells()
                self.clear_label(self.figure1, 800, 130)
                self.draw_cur_figures()

            else:
                print("Фигура попадает на другую фигуру!")
                self.figure1.move(800, 130)

        else:
            print("Фигура вне игрового поля!")
            self.figure1.move(800, 130)

        self.update()

    def can_drag_fugire(self, figure, cell_x, cell_y):
        for i in range(len(figure.shape)):
            for j in range(len(figure.shape[0])):
                if figure.shape[i][j] == self.game.board[i + cell_x][j + cell_y] == 1:
                    return False

        return True



    def clear_label(self, label, start_x, start_y):
        label.setCursor(QCursor(Qt.ArrowCursor))
        label.mouseMoveEvent = None
        label.setMouseTracking(False)
        label.mouseReleaseEvent = None
        label.move(start_x, start_y)

    def add_figure_to_board(self, cell_x, cell_y, figure):
        for i in range(min(len(figure.shape), self.game.width - cell_x)):
            for j in range(min(len(figure.shape[0]), self.game.height - cell_y)):
                if figure.shape[i][j] == 1:
                    self.game.board[i + cell_x][j + cell_y] = figure.shape[i][j]

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
