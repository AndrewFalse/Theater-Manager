# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_page.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QComboBox, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLayout,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTableView, QVBoxLayout, QWidget)
import resources

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(810, 655)
        MainWindow.setStyleSheet(u"background-color: white;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_5 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.icon_widget = QWidget(self.centralwidget)
        self.icon_widget.setObjectName(u"icon_widget")
        self.icon_widget.setMaximumSize(QSize(70, 16777215))
        self.icon_widget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(128, 0, 2);\n"
"}\n"
"\n"
"QPushButton{\n"
"	height: 30px;\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	background-color: #F5FAFE;\n"
"	color: #1F95EF;\n"
"	font-weight: bold;\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.icon_widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.icon_widget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(40, 40))
        self.label.setStyleSheet(u"")
        self.label.setPixmap(QPixmap(u":/icons/free-icon-font-smile.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(-1, 15, -1, -1)
        self.btn1 = QPushButton(self.icon_widget)
        self.btn1.setObjectName(u"btn1")
        icon = QIcon()
        icon.addFile(u":/icons/free-icon-font-user.png", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/icons/free-icon-font-user-3917559.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn1.setIcon(icon)
        self.btn1.setCheckable(True)
        self.btn1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.btn1)

        self.btn2 = QPushButton(self.icon_widget)
        self.btn2.setObjectName(u"btn2")
        icon1 = QIcon()
        icon1.addFile(u":/icons/free-icon-font-megaphone-2.png", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/icons/free-icon-font-megaphone-3914404.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn2.setIcon(icon1)
        self.btn2.setCheckable(True)
        self.btn2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.btn2)

        self.btn3 = QPushButton(self.icon_widget)
        self.btn3.setObjectName(u"btn3")
        icon2 = QIcon()
        icon2.addFile(u":/icons/free-icon-font-calendar.png", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u":/icons/free-icon-font-calendar-3917244.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn3.setIcon(icon2)
        self.btn3.setCheckable(True)
        self.btn3.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.btn3)

        self.btn4 = QPushButton(self.icon_widget)
        self.btn4.setObjectName(u"btn4")
        icon3 = QIcon()
        icon3.addFile(u":/icons/free-icon-font-film.png", QSize(), QIcon.Normal, QIcon.Off)
        icon3.addFile(u":/icons/free-icon-font-film-3914173.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn4.setIcon(icon3)
        self.btn4.setCheckable(True)
        self.btn4.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.btn4)

        self.btn5 = QPushButton(self.icon_widget)
        self.btn5.setObjectName(u"btn5")
        icon4 = QIcon()
        icon4.addFile(u":/icons/free-icon-font-ticket.png", QSize(), QIcon.Normal, QIcon.Off)
        icon4.addFile(u":/icons/free-icon-font-ticket-3916614.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn5.setIcon(icon4)
        self.btn5.setCheckable(True)
        self.btn5.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.btn5)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 241, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.btn6 = QPushButton(self.icon_widget)
        self.btn6.setObjectName(u"btn6")
        icon5 = QIcon()
        icon5.addFile(u":/icons/free-icon-font-exit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn6.setIcon(icon5)

        self.verticalLayout_3.addWidget(self.btn6)

        self.btn6.raise_()

        self.horizontalLayout_5.addWidget(self.icon_widget)

        self.label_widget = QWidget(self.centralwidget)
        self.label_widget.setObjectName(u"label_widget")
        self.label_widget.setMaximumSize(QSize(180, 16777215))
        self.label_widget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(128, 0, 2);\n"
"}\n"
"\n"
"QPushButton{\n"
"	color: white;\n"
"	height: 30px;\n"
"	border: none;\n"
"	padding-left: 10px;\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	background-color: #F5FAFE;\n"
"	color: #1F95EF;\n"
"	font-weight: bold;\n"
"}\n"
"")
        self.verticalLayout_4 = QVBoxLayout(self.label_widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.label_2 = QLabel(self.label_widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(40, 40))
        self.label_2.setPixmap(QPixmap(u":/icons/free-icon-font-smile.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.label_widget)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setFamilies([u"Right Grotesk"])
        font.setPointSize(24)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.label_3)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(15, 15, -1, -1)
        self.button1 = QPushButton(self.label_widget)
        self.button1.setObjectName(u"button1")
        font1 = QFont()
        font1.setFamilies([u"Right Grotesk Small"])
        self.button1.setFont(font1)
        self.button1.setIcon(icon)
        self.button1.setCheckable(True)
        self.button1.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.button1)

        self.button2 = QPushButton(self.label_widget)
        self.button2.setObjectName(u"button2")
        self.button2.setFont(font1)
        self.button2.setIcon(icon1)
        self.button2.setCheckable(True)
        self.button2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.button2)

        self.button3 = QPushButton(self.label_widget)
        self.button3.setObjectName(u"button3")
        self.button3.setFont(font1)
        self.button3.setIcon(icon2)
        self.button3.setCheckable(True)
        self.button3.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.button3)

        self.button4 = QPushButton(self.label_widget)
        self.button4.setObjectName(u"button4")
        self.button4.setFont(font1)
        self.button4.setIcon(icon3)
        self.button4.setCheckable(True)
        self.button4.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.button4)

        self.button5 = QPushButton(self.label_widget)
        self.button5.setObjectName(u"button5")
        self.button5.setFont(font1)
        self.button5.setIcon(icon4)
        self.button5.setCheckable(True)
        self.button5.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.button5)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 241, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.button6 = QPushButton(self.label_widget)
        self.button6.setObjectName(u"button6")
        self.button6.setIcon(icon5)

        self.verticalLayout_4.addWidget(self.button6)


        self.horizontalLayout_5.addWidget(self.label_widget)

        self.main_widget = QWidget(self.centralwidget)
        self.main_widget.setObjectName(u"main_widget")
        self.main_widget.setMinimumSize(QSize(400, 400))
        self.verticalLayout_5 = QVBoxLayout(self.main_widget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.widget = QWidget(self.main_widget)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_6 = QVBoxLayout(self.widget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.menu = QPushButton(self.widget)
        self.menu.setObjectName(u"menu")
        self.menu.setStyleSheet(u"border:none;")
        icon6 = QIcon()
        icon6.addFile(u":/icons/free-icon-font-menu-burger-3917215.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu.setIcon(icon6)
        self.menu.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.menu)

        self.horizontalSpacer = QSpacerItem(408, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.verticalLayout_6.addLayout(self.horizontalLayout_3)

        self.stackedWidget = QStackedWidget(self.widget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setEnabled(True)
        self.stackedWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.personal_page = QWidget()
        self.personal_page.setObjectName(u"personal_page")
        self.gridLayout = QGridLayout(self.personal_page)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.comboBox = QComboBox(self.personal_page)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(0, 20))

        self.verticalLayout_7.addWidget(self.comboBox)

        self.tableView = QTableView(self.personal_page)
        self.tableView.setObjectName(u"tableView")
        font2 = QFont()
        font2.setFamilies([u"Right Grotesk Small"])
        font2.setPointSize(10)
        self.tableView.setFont(font2)
        self.tableView.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableView.setTabKeyNavigation(False)
        self.tableView.setProperty("showDropIndicator", False)
        self.tableView.setShowGrid(False)
        self.tableView.setCornerButtonEnabled(False)
        self.tableView.verticalHeader().setVisible(False)
        self.tableView.verticalHeader().setHighlightSections(False)

        self.verticalLayout_7.addWidget(self.tableView)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton = QPushButton(self.personal_page)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(100, 32))
        font3 = QFont()
        font3.setFamilies([u"Right Grotesk"])
        self.pushButton.setFont(font3)
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"background-color: white;\n"
"border-style: solid;\n"
"border-color: rgb(120, 0, 0);\n"
"border-width: 2px;\n"
"border-radius:10px;\n"
"}")

        self.horizontalLayout_4.addWidget(self.pushButton)

        self.pushButton_4 = QPushButton(self.personal_page)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(100, 32))
        self.pushButton_4.setFont(font3)
        self.pushButton_4.setStyleSheet(u"QPushButton{\n"
"background-color: white;\n"
"border-style: solid;\n"
"border-color: rgb(120, 0, 0);\n"
"border-width: 2px;\n"
"border-radius:10px;\n"
"}")

        self.horizontalLayout_4.addWidget(self.pushButton_4)


        self.verticalLayout_7.addLayout(self.horizontalLayout_4)


        self.gridLayout.addLayout(self.verticalLayout_7, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.personal_page)
        self.schedule_page = QWidget()
        self.schedule_page.setObjectName(u"schedule_page")
        self.stackedWidget.addWidget(self.schedule_page)
        self.items_page = QWidget()
        self.items_page.setObjectName(u"items_page")
        self.stackedWidget.addWidget(self.items_page)
        self.cash_page = QWidget()
        self.cash_page.setObjectName(u"cash_page")
        self.stackedWidget.addWidget(self.cash_page)
        self.shows_page = QWidget()
        self.shows_page.setObjectName(u"shows_page")
        self.stackedWidget.addWidget(self.shows_page)

        self.verticalLayout_6.addWidget(self.stackedWidget)


        self.verticalLayout_5.addWidget(self.widget)


        self.horizontalLayout_5.addWidget(self.main_widget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.menu.toggled.connect(self.icon_widget.setHidden)
        self.menu.toggled.connect(self.label_widget.setVisible)
        self.btn5.toggled.connect(self.button5.setChecked)
        self.btn4.toggled.connect(self.button4.setChecked)
        self.btn3.toggled.connect(self.button3.setChecked)
        self.btn2.toggled.connect(self.button2.setChecked)
        self.btn1.toggled.connect(self.button1.setChecked)
        self.button1.toggled.connect(self.btn1.setChecked)
        self.button2.toggled.connect(self.btn2.setChecked)
        self.button3.toggled.connect(self.btn3.setChecked)
        self.button4.toggled.connect(self.btn4.setChecked)
        self.button5.toggled.connect(self.btn5.setChecked)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.btn1.setText("")
        self.btn2.setText("")
        self.btn3.setText("")
        self.btn4.setText("")
        self.btn5.setText("")
        self.btn6.setText("")
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u043d\u044e", None))
        self.button1.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0441\u043e\u043d\u0430\u043b", None))
        self.button2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0435\u043a\u0442\u0430\u043a\u043b\u0438", None))
        self.button3.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.button4.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u043f\u0435\u0440\u0442\u0443\u0430\u0440", None))
        self.button5.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0441\u0441\u0430", None))
        self.button6.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0439\u0442\u0438", None))
        self.menu.setText("")
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0410\u043a\u0442\u0435\u0440\u044b", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u041c\u0443\u0437\u044b\u043a\u0430\u043d\u0442\u044b", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0434\u044e\u0441\u0435\u0440\u044b", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0447\u0438\u0435 \u0440\u0430\u0431\u043e\u0442\u043d\u0438\u043a\u0438 \u0442\u0435\u0430\u0442\u0440\u0430", None))

        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0411\u0414", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u043e", None))
    # retranslateUi

