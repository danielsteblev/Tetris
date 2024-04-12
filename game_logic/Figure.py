# Классы фигур
from PyQt5.QtGui import QColor


class Figure:
    shape = []
    color = None

    def width(self):
        return len(self.shape[0])

    def height(self):
        return len(self.shape)


class ShapeSquare(Figure):
    shape = [[1, 1],
             [1, 1]]

    color = QColor(40, 222, 210)


class ShapeLine(Figure):
    shape = [[1, 1, 1]]

    color = QColor(183, 64, 201)


class ShapeG(Figure):
    shape = [[0, 0, 1],
             [1, 1, 1]]

    color = QColor(235, 179, 96)


class ShapeReverseG(Figure):
    shape = [[1, 0, 0],
             [1, 1, 1]]

    color = QColor(134, 166, 247)


class ShapeT(Figure):
    shape = [[0, 1, 0],
             [1, 1, 1]]

    color = QColor(124, 247, 181)


class ShapeZ(Figure):
    shape = [[1, 1, 0],
             [0, 1, 1]]

    color = QColor(250, 218, 221)


class Rect(Figure):
    shape = [[0, 1, 1, 0]]

    color = QColor(159, 226, 191)


class ReverseT(Figure):
    shape = [[0, 1],
             [1, 1],
             [0, 1]]

    color = QColor(127, 199, 255)


class Block(Figure):
    shape = [[0, 1, 0]]

    color = QColor(255, 140, 105)


class ShapeReverseZ(Figure):
    shape = [[0, 1, 1],
             [1, 1, 0]]

    color = QColor(240, 161, 199)


class CloseCanvasRect(Figure):
    shape = [[1, 1, 1, 1],
             [1, 1, 1, 1],
             [1, 1, 1, 1],
             [1, 1, 1, 1]]

    color = QColor(240, 240, 240)
