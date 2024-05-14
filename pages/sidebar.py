import configparser

import mysql.connector
from PySide6 import QtWidgets
from PySide6.QtGui import QStandardItem, QStandardItemModel

from main_page_ui import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow

from pages.personal_db_page import PersonalDBPage
from pages.staff_info_page import StaffInfoPage
from sql_queries import get_actors, get_musicians, get_producers, get_staffs, get_shows, get_schedule, get_items, \
    get_tickets


class SideBar(QMainWindow, Ui_MainWindow):
    def __init__(self, user):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Управление театром")

        self.icon_widget.setHidden(True)

        self.button1.clicked.connect(self.set_personal_page)
        self.btn1.clicked.connect(self.set_personal_page)
        self.button2.clicked.connect(self.set_shows_page)
        self.btn2.clicked.connect(self.set_shows_page)
        self.button3.clicked.connect(self.set_schedule_page)
        self.btn3.clicked.connect(self.set_schedule_page)
        self.button4.clicked.connect(self.set_items_page)
        self.btn4.clicked.connect(self.set_items_page)
        self.button5.clicked.connect(self.set_cash_page)
        self.btn5.clicked.connect(self.set_cash_page)
        self.button6.clicked.connect(self.logout)
        self.btn6.clicked.connect(self.logout)
        self.comboBox.currentTextChanged.connect(self.change_datatable)
        self.prs_qr_btn.clicked.connect(self.show_staff_info)

        if user == 'Режиссер-постановщик':
            self.button1.hide()
            self.btn1.hide()
            self.button5.hide()
            self.btn5.hide()

        if user == 'Кассир':
            self.button1.hide()
            self.btn1.hide()
            self.button2.hide()
            self.btn2.hide()
            self.button3.hide()
            self.btn3.hide()
            self.button4.hide()
            self.btn4.hide()

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

        self.change_datatable()
        self.set_personal_page()

    def set_personal_page(self):
        self.stackedWidget.setCurrentIndex(0)
        self.change_datatable()
        self.add_prs_btn.clicked.connect(self.show_prs_page)

    def set_schedule_page(self):
        self.stackedWidget.setCurrentIndex(1)
        self.set_schedule_table()

    def set_items_page(self):
        self.stackedWidget.setCurrentIndex(2)
        self.set_item_table()

    def set_cash_page(self):
        self.stackedWidget.setCurrentIndex(3)
        self.set_tickets_table()

    def set_shows_page(self):
        self.stackedWidget.setCurrentIndex(4)
        self.set_performance_table()

    def set_performance_table(self):
        model = QStandardItemModel()

        query = get_shows
        header = ['ID', 'Название', 'Автор', 'Жанр']

        self.my_cursor.execute(query)
        result = self.my_cursor.fetchall()
        model.setHorizontalHeaderLabels(header)
        for row_number, row_data in enumerate(result):
            for column_number, data in enumerate(row_data):
                item = QStandardItem(str(data))
                model.setItem(row_number, column_number, item)
        self.show_table.setModel(model)
        self.show_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)

    def set_tickets_table(self):
        model = QStandardItemModel()

        query = get_tickets
        header = ['Спектакль', 'Цена', 'Место']

        self.my_cursor.execute(query)
        result = self.my_cursor.fetchall()
        model.setHorizontalHeaderLabels(header)
        for row_number, row_data in enumerate(result):
            for column_number, data in enumerate(row_data):
                item = QStandardItem(str(data))
                model.setItem(row_number, column_number, item)
        self.tck_table.setModel(model)
        self.tck_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)

    def set_item_table(self):
        model = QStandardItemModel()

        query = get_items
        header = ['Название', 'Спектакль']

        self.my_cursor.execute(query)
        result = self.my_cursor.fetchall()
        model.setHorizontalHeaderLabels(header)
        for row_number, row_data in enumerate(result):
            for column_number, data in enumerate(row_data):
                item = QStandardItem(str(data))
                model.setItem(row_number, column_number, item)
        self.item_table.setModel(model)
        self.item_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)

    def set_schedule_table(self):
        model = QStandardItemModel()

        query = get_schedule
        header = ['ID', 'Название', 'Дата', 'Автор', 'Жанр', 'Продюсер', 'Кол-во мест']

        self.my_cursor.execute(query)
        result = self.my_cursor.fetchall()
        model.setHorizontalHeaderLabels(header)
        for row_number, row_data in enumerate(result):
            for column_number, data in enumerate(row_data):
                item = QStandardItem(str(data))
                model.setItem(row_number, column_number, item)
        self.sch_table.setModel(model)
        self.sch_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)

    def change_datatable(self):
        model = QStandardItemModel()
        selected_item = self.comboBox.currentText()
        header = []

        if selected_item == "Актеры":
            query = get_actors
            header = ['ID', 'Имя', 'Звание', 'Статус', 'Пол', 'Возраст', 'Тип голоса', 'Рост', 'Директор',
                      'Начал работать', 'Зарплата']
        elif selected_item == "Музыканты":
            header = ['ID', 'Имя', 'Роль', 'Статус', 'Инструмент', 'Директор', 'Начал работать', 'Возраст', 'Зарплата']
            query = get_musicians
        elif selected_item == "Продюсеры":
            header = ['ID', 'Имя', 'Статус', 'Стаж', 'Должность', 'Директор', 'Начал работать', 'Возраст', 'Зарплата']
            query = get_producers
        else:
            header = ['ID', 'Имя', 'Статус', 'Должность', 'Директор', 'Начал работать', 'Возраст', 'Зарплата']
            query = get_staffs

        self.my_cursor.execute(query)
        result = self.my_cursor.fetchall()
        model.setHorizontalHeaderLabels(header)
        for row_number, row_data in enumerate(result):
            for column_number, data in enumerate(row_data):
                item = QStandardItem(str(data))
                model.setItem(row_number, column_number, item)
        self.tableView.setModel(model)
        self.tableView.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)

    def show_prs_page(self):
        self.prs_page = PersonalDBPage()
        self.prs_page.show()

    def logout(self):
        from main import LoginPage
        self.login_page = LoginPage()
        self.login_page.show()
        self.close()

    def show_staff_info(self):
        self.staff_info_page = StaffInfoPage(self.my_cursor)
        self.staff_info_page.show()
