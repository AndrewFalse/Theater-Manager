import configparser

import mysql
from mysql import connector
from PySide6 import QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from PySide6.QtWidgets import QWidget, QVBoxLayout
import tickets_info_page_ui


class TicketInfoPage(QtWidgets.QMainWindow, tickets_info_page_ui.Ui_MainWindow):
    def __init__(self, my_cursor):
        config = configparser.ConfigParser()
        config.read('config.ini')

        host = config['database']['host']
        user = config['database']['user']
        password = config['database']['password']
        database = config['database']['database']
        self.mydb = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.my_cursor = self.mydb.cursor()
        super().__init__()
        self.setupUi(self)

        layout5 = QVBoxLayout(self.widget)
        layout5.setContentsMargins(20, 20, 20, 20)
        layout5.addWidget(self.create_revenue_per_performance_chart())

        layout6 = QVBoxLayout(self.widget_2)
        layout6.setContentsMargins(20, 20, 20, 20)
        layout6.addWidget(self.create_total_tickets_per_genre_chart())

    def get_sql_query(self, query):
        self.my_cursor.callproc(query)
        result = []
        for result_set in self.my_cursor.stored_results():
            for row in result_set:
                result.append(row)
        return result

    def create_revenue_per_performance_chart(self):
        data = self.get_sql_query('get_revenue_per_performance')
        titles = [title for title, _ in data]
        revenues = [revenue for _, revenue in data]

        fig, ax = plt.subplots(figsize=(6, 4))
        ax.bar(titles, revenues)
        ax.set_xlabel('Спектакль')
        ax.set_ylabel('Выручка')
        ax.set_title('Выручка по спектаклям')
        ax.set_xticklabels(titles, fontsize=5, rotation=90)
        plt.tight_layout()

        canvas = FigureCanvas(fig)
        return canvas

    def create_total_tickets_per_genre_chart(self):
        data = self.get_sql_query('calculate_total_tickets_per_genre')
        genres = [genre for genre, _ in data]
        counts = [count for _, count in data]

        fig, ax = plt.subplots(figsize=(6, 4))
        ax.bar(genres, counts)
        ax.set_xlabel('Жанр')
        ax.set_ylabel('Кол-во билетов')
        ax.set_title('Общее количество билетов по жанрам')
        ax.set_xticklabels(genres, fontsize=5, rotation=90)
        plt.tight_layout()

        canvas = FigureCanvas(fig)
        return canvas


