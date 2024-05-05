import configparser
from main_page_ui import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow
import mysql.connector
from personal_table_model import TableModel


class SideBar(QMainWindow, Ui_MainWindow):
    def __init__(self, user):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Управление театром")

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
        self.my_cursor.execute("""
                SELECT a.name AS employee_name, 'Актер', d.name AS director_name
                FROM actors a
                JOIN directors d ON a.director_id = d.id
                UNION
                SELECT m.name, 'Музыкант', d.name
                FROM musicians m
                JOIN directors d ON m.director_id = d.id
                UNION
                SELECT s.name, 'Работник', d.name
                FROM staffs s
                JOIN directors d ON s.director_id = d.id
                UNION
                SELECT p.name, 'Продюсер', d.name
                FROM producers p
                JOIN directors d ON p.director_id = d.id;
            """)
        actors = self.my_cursor.fetchall()

        header = ["Имя", "Должность", "Директор"]
        model = TableModel(actors, header)
        self.tableView.setModel(model)

        self.initiate_widgets(user)

    def set_personal_page(self):
        self.stackedWidget.setCurrentIndex(0)

    def set_schedule_page(self):
        self.stackedWidget.setCurrentIndex(1)

    def set_items_page(self):
        self.stackedWidget.setCurrentIndex(2)

    def set_cash_page(self):
        self.stackedWidget.setCurrentIndex(3)

    def set_shows_page(self):
        self.stackedWidget.setCurrentIndex(4)

    def logout(self):
        from main import LoginPage
        self.login_page = LoginPage()
        self.login_page.show()
        self.close()

    def initiate_widgets(self, user):
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
