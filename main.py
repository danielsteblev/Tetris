import sys

from PyQt5.QtWidgets import QApplication

from gui.MainMenu import GameWindow
from gui.SettingsWindow import SettingsWindow
from gui.TokenWindow import TokenWindow


def main():
    try:
        app = QApplication(sys.argv)
        main_window = GameWindow()
        main_window.show()
        sys.exit(app.exec_())
    except Exception as e:
        print(f"Ошибка: {e}")
        sys.exit(-1)




if __name__ == '__main__':
    import sys

    main()
