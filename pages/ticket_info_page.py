from PySide6 import QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from PySide6.QtWidgets import QWidget, QVBoxLayout
import tickets_info_page_ui


class TicketInfoPage(QtWidgets.QMainWindow, tickets_info_page_ui.Ui_MainWindow):
    def __init__(self, my_cursor):
        self.my_cursor = my_cursor
        super().__init__()
        self.setupUi(self)

