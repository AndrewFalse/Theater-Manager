from PySide6 import QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from PySide6.QtWidgets import QWidget, QVBoxLayout
import show_info_page_ui
from pages.count_page import CountPage


class ShowInfoPage(QtWidgets.QMainWindow, show_info_page_ui.Ui_MainWindow):
    def __init__(self, my_cursor):
        self.my_cursor = my_cursor
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.open_count_page)

    def open_count_page(self):
        self.count_page = CountPage()
        self.count_page.show()
