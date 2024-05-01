import sys
import login_page
from PyQt6 import QtWidgets


class LoginPage(QtWidgets.QMainWindow, login_page.Ui_Form):
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
