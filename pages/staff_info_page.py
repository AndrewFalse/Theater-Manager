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

        layout2 = QVBoxLayout(self.widget2)
        layout2.setContentsMargins(20, 20, 20, 20)
        layout2.addWidget(self.create_ring_chart())

        layout3 = QVBoxLayout(self.widget3)
        layout3.setContentsMargins(20, 20, 20, 20)
        layout3.addWidget(self.create_tour_pie())

        layout4 = QVBoxLayout(self.widget4)
        layout4.setContentsMargins(20, 20, 20, 20)
        layout4.addWidget(self.create_age_chart())

    def get_sql_query(self, query):
        self.my_cursor.callproc(query)
        result = []
        for result_set in self.my_cursor.stored_results():
            for row in result_set:
                result.append(row)
        return result

    def create_chart(self):
        data = self.get_sql_query('get_actor_title_count')
        titles = [title for title, _ in data]
        counts = [count for _, count in data]

        fig, ax = plt.subplots(figsize=(3, 2))
        ax.bar(titles, counts)
        ax.tick_params(axis='x', rotation=90)
        ax.set_xticklabels(titles, fontsize=5, rotation=90)
        plt.tight_layout()

        canvas = FigureCanvas(fig)

        return canvas

    def create_tour_pie(self):
        data = self.get_sql_query('get_total_tour_info')
        titles = [title for title, _ in data]
        counts = [count for _, count in data]

        fig, ax = plt.subplots(figsize=(6, 4))
        labels = ['В туре', 'В театре']
        sizes = [counts[0], counts[1]]
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
        ax.axis('equal')

        canvas = FigureCanvas(fig)
        return canvas

    def create_age_chart(self):
        data = self.get_sql_query('count_ages')
        ages = [row[0] for row in data]
        counts = [row[1] for row in data]

        fig, ax = plt.subplots()
        ax.bar(ages, counts)
        ax.set_xlabel('Age')
        ax.set_ylabel('Count')
        ax.set_title('Distribution of Ages')

        canvas = FigureCanvas(fig)
        return canvas

    def create_ring_chart(self):
        data = self.get_sql_query('count_experience_years')
        titles = [title for title, _ in data]
        counts = [count for _, count in data]

        fig, ax = plt.subplots(figsize=(6, 6))
        wedges, texts, autotexts = ax.pie(counts, labels=titles, autopct='%1.1f%%', startangle=90,
                                          wedgeprops=dict(width=0.4, edgecolor='w'))

        plt.setp(autotexts, size=8, weight="bold")
        ax.axis('equal')

        # Добавляем белый круг в центр для создания эффекта donut chart
        centre_circle = plt.Circle((0, 0), 0.2, color='white', linewidth=0)
        ax.add_artist(centre_circle)

        plt.tight_layout()

        canvas = FigureCanvas(fig)

        return canvas
