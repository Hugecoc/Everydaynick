import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget

from ui_vuw import Ui_mainWindow


class TaskSystem(QMainWindow, Ui_mainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


def except_hooks(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    wnd = TaskSystem()
    wnd.show()
    sys.exit(app.exec())
