from PySide6 import QtWidgets
import personal_db_page_ui


class PersonalDBPage(QtWidgets.QMainWindow, personal_db_page_ui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
