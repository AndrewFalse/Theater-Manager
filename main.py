import sys
import login_page
import main_page
from PySide6 import QtWidgets


class LoginPage(QtWidgets.QMainWindow, main_page.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = LoginPage()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
