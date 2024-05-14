import configparser
from aifc import Error
from datetime import datetime

import mysql
from mysql import connector
from PySide6 import QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QMessageBox
import count_page_ui


def check_date_format(date_str):
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False


class CountPage(QtWidgets.QMainWindow, count_page_ui.Ui_MainWindow):
    def __init__(self):

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
        self.pushButton.clicked.connect(self.get_query)

    def get_query(self):
        self.show_performance_count(self.lineEdit.text(), self.lineEdit_2.text())

    def call_procedure(self, start_date, end_date):
        self.my_cursor.callproc("get_performance_count_by_time", [start_date, end_date])
        for result in self.my_cursor.stored_results():
            for row in result.fetchall():
                return row[0]

    def show_performance_count(self, start_date, end_date):
        if (check_date_format(start_date) and check_date_format(end_date)) is False:
            QMessageBox.critical(self, "Проверка ввода", "Неверно формат даты")
        else:
            count = self.call_procedure(start_date, end_date)
            label = QLabel(f"Спектаклей проведено: {count}")

            layout = QVBoxLayout(self.widget)
            layout.setContentsMargins(20, 20, 20, 20)
            layout.addWidget(label)
