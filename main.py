import sys

from PyQt5.QtCore import QMimeData, Qt
from PyQt5.QtGui import QDrag
from PyQt5.QtWidgets import QApplication, QLabel, QWidget

class DraggableLabel(QLabel):
    def __init__(self, parent):
        super().__init__(parent)

        self.setMouseTracking(True)
        self.setStyleSheet("background-color: #f0f0f0; padding: 10px;")

    def mousePressEvent(self, event):
        if event.button() == 1:
            self.dragStartPosition = event.pos()

    def mouseMoveEvent(self, event):
        if not hasattr(self, 'dragStartPosition'):
            return

        if (event.pos() - self.dragStartPosition).manhattanLength() < QApplication.startDragDistance():
            return

        drag = QDrag(self)
        mimeData = QMimeData()
        drag.setMimeData(mimeData)

        drag.exec_(Qt.MoveAction)

class Example(QWidget):
    def __init__(self):
        super().__init__()

        label = DraggableLabel(self)
        label.setText("Drag me")
        label.move(50, 50)

        self.setGeometry(300, 300, 400, 200)
        self.setWindowTitle('Drag and Drop Example')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())