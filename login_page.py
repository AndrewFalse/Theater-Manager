from PySide6 import QtWidgets
import login_page_ui


class LoginPage(QtWidgets.QMainWindow, login_page_ui.Ui_Form):
    def __init__(self):
        super().__init__()
        self.main_page = None
        self.setupUi(self)
        self.pushButton.clicked.connect(self.open_main_page)

    def open_main_page(self):
        self.close()
        from main import SideBar
        self.main_page = SideBar(self.comboBox.currentText())
        self.main_page.show()

