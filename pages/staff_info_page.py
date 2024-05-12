from PySide6 import QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from PySide6.QtWidgets import QWidget, QVBoxLayout
import staff_info_page_ui


class StaffInfoPage(QtWidgets.QMainWindow, staff_info_page_ui.Ui_MainWindow):
    def __init__(self, my_cursor):
        self.my_cursor = my_cursor
        super().__init__()
        self.setupUi(self)
        layout = QVBoxLayout(self.widget)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.addWidget(self.create_chart())



    def get_actor_title_count(self):
        self.my_cursor.callproc('get_actor_title_count')
        result = []
        for result_set in self.my_cursor.stored_results():
            for row in result_set:
                result.append(row)
        return result

    def create_chart(self):
        data = self.get_actor_title_count()
        titles = [title for title, _ in data]
        counts = [count for _, count in data]

        fig, ax = plt.subplots(figsize=(3, 2))
        ax.bar(titles, counts)
        ax.set_ylabel('Count')
        ax.tick_params(axis='x', rotation=90)
        ax.set_xticklabels(titles, fontsize=4, rotation=90)
        plt.tight_layout()

        canvas = FigureCanvas(fig)

        return canvas
