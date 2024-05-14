import configparser

import mysql
from mysql import connector
from PySide6 import QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from PySide6.QtWidgets import QWidget, QVBoxLayout
import show_info_page_ui
from pages.count_page import CountPage


class ShowInfoPage(QtWidgets.QMainWindow, show_info_page_ui.Ui_MainWindow):
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
        self.pushButton.clicked.connect(self.open_count_page)

        layout5 = QVBoxLayout(self.widget_3)
        layout5.setContentsMargins(20, 20, 20, 20)
        layout5.addWidget(self.create_free_seats_chart())

        layout6 = QVBoxLayout(self.widget)
        layout6.setContentsMargins(20, 20, 20, 20)
        layout6.addWidget(self.create_performance_info_chart())

        layout7 = QVBoxLayout(self.widget_2)
        layout7.setContentsMargins(20, 20, 20, 20)
        layout7.addWidget(self.create_most_prolific_author_chart())

        layout8 = QVBoxLayout(self.widget_4)
        layout8.setContentsMargins(20, 20, 20, 20)
        layout8.addWidget(self.create_author_performance_count_chart())

    def create_free_seats_chart(self):
        data = self.get_sql_query('free_seats')
        dates = [date for date, _ in data]
        counts = [count for _, count in data]

        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(dates, counts, marker='o')
        ax.set_xlabel('Дата')
        ax.set_ylabel('Кол-во свободных мест')
        ax.set_title('Свободные места на спектаклях')
        ax.set_xticklabels(dates, fontsize=5, rotation=90)
        plt.tight_layout()

        canvas = FigureCanvas(fig)
        return canvas

    def create_performance_info_chart(self):
        data = self.get_sql_query('get_performance_info')
        genres = [genre for genre, _ in data]
        counts = [count for _, count in data]

        fig, ax = plt.subplots(figsize=(6, 4))
        ax.bar(genres, counts)
        ax.set_xlabel('Жанр')
        ax.set_ylabel('Кол-во спектаклей')
        ax.set_title('Информация о спектаклях по жанрам')
        ax.set_xticklabels(genres, fontsize=5, rotation=90)
        plt.tight_layout()

        canvas = FigureCanvas(fig)
        return canvas

    def create_most_prolific_author_chart(self):
        data = self.get_sql_query('most_prolific_author')
        authors = [author for author, _ in data]
        counts = [count for _, count in data]

        fig, ax = plt.subplots(figsize=(6, 4))
        ax.bar(authors, counts)
        ax.set_xlabel('Автор')
        ax.set_ylabel('Кол-во спектаклей')
        ax.set_title('Самые продуктивные авторы')
        ax.set_xticklabels(authors, fontsize=5, rotation=90)
        plt.tight_layout()

        canvas = FigureCanvas(fig)
        return canvas

    def create_author_performance_count_chart(self):
        data = self.get_sql_query('get_author_performance_count')
        authors = [author for author, _ in data]
        counts = [count for _, count in data]

        fig, ax = plt.subplots(figsize=(6, 4))
        ax.bar(authors, counts)
        ax.set_xlabel('Автор')
        ax.set_ylabel('Кол-во спектаклей')
        ax.set_title('Количество спектаклей по авторам')
        ax.set_xticklabels(authors, fontsize=5, rotation=90)
        plt.tight_layout()

        canvas = FigureCanvas(fig)
        return canvas

    def open_count_page(self):
        self.count_page = CountPage()
        self.count_page.show()

    def get_sql_query(self, query):
        self.my_cursor.callproc(query)
        result = []
        for result_set in self.my_cursor.stored_results():
            for row in result_set:
                result.append(row)
        return result
