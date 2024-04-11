# Классы фигур
class Figure:
    shape = []

    def width(self):
        return len(self.shape[0])

    def height(self):
        return len(self.shape)


class ShapeSquare(Figure):
    shape = [[1, 1],
             [1, 1]]


class ShapeLine(Figure):
    shape = [[1, 1, 1, 1]]


class ShapeG(Figure):
    shape = [[0, 0, 1],
             [1, 1, 1]]


class ShapeReverseG(Figure):
    shape = [[1, 0, 0],
             [1, 1, 1]]


class ShapeT(Figure):
    shape = [[0, 1, 0],
             [1, 1, 1]]


class ShapeZ(Figure):
    shape = [[1, 1, 0],
             [0, 1, 1]]


class ShapeReverseZ(Figure):
    shape = [[0, 1, 1],
             [1, 1, 0]]
