import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from ui_everyday import Ui_MainWindow


class TaskSystem(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


def except_hook(clc, exception, traceback):
    sys.__excepthook__(clc, exception, traceback)


if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    wnd = TaskSystem()
    wnd.show()
    sys.exit(app.exec())

