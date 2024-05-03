import sys
from PySide6 import QtWidgets
from sidebar import SideBar
from login_page import LoginPage


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = LoginPage()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
