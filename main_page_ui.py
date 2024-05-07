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
        MainWindow.resize(808, 654)
        MainWindow.setStyleSheet(u"background-color: white;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
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

        self.gridLayout_2.addWidget(self.icon_widget, 0, 0, 1, 1)

        self.label_widget = QWidget(self.centralwidget)
        self.label_widget.setObjectName(u"label_widget")
        self.label_widget.setMinimumSize(QSize(170, 0))
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
        font1.setFamilies([u"Right Grotesk"])
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


        self.gridLayout_2.addWidget(self.label_widget, 0, 1, 1, 1)

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
        self.personal_page.setStyleSheet(u"QPushButton{\n"
"	height: 30px;\n"
"	border :2px solid;\n"
"	border-color: rgb(120, 0, 0);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: #F5FAFE;\n"
"	border :2px solid;\n"
"	border-color: rgb(102, 102, 102);\n"
"	color: #1F95EF;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QComboBox {\n"
"    border: 2px solid;\n"
"	border-color: rgb(120, 0, 0);\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"	font: 57 13pt \"Right Grotesk Small\";\n"
"}\n"
"\n"
"QTableView {\n"
"    border: 1px solid;\n"
"	border-color: rgb(120, 0, 0);\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"	font: 57 13pt \"Right Grotesk Small\";\n"
"}")
        self.gridLayout = QGridLayout(self.personal_page)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.comboBox = QComboBox(self.personal_page)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(115, 30))
        font2 = QFont()
        font2.setFamilies([u"Right Grotesk Small"])
        font2.setPointSize(13)
        font2.setBold(False)
        font2.setItalic(False)
        self.comboBox.setFont(font2)

        self.horizontalLayout_4.addWidget(self.comboBox)

        self.horizontalSpacer_4 = QSpacerItem(78, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.add_prs_btn = QPushButton(self.personal_page)
        self.add_prs_btn.setObjectName(u"add_prs_btn")
        self.add_prs_btn.setMinimumSize(QSize(60, 30))
        self.add_prs_btn.setMaximumSize(QSize(40, 16777215))
        self.add_prs_btn.setStyleSheet(u"")
        icon7 = QIcon()
        icon7.addFile(u":/icons/free-icon-font-user-3917559.png", QSize(), QIcon.Normal, QIcon.Off)
        self.add_prs_btn.setIcon(icon7)

        self.horizontalLayout_4.addWidget(self.add_prs_btn)

        self.prs_qr_btn = QPushButton(self.personal_page)
        self.prs_qr_btn.setObjectName(u"prs_qr_btn")
        self.prs_qr_btn.setMinimumSize(QSize(60, 30))
        self.prs_qr_btn.setStyleSheet(u"")
        icon8 = QIcon()
        icon8.addFile(u":/icons/free-icon-font-document-3914193.png", QSize(), QIcon.Normal, QIcon.Off)
        self.prs_qr_btn.setIcon(icon8)

        self.horizontalLayout_4.addWidget(self.prs_qr_btn)

        self.prs_set_btn = QPushButton(self.personal_page)
        self.prs_set_btn.setObjectName(u"prs_set_btn")
        self.prs_set_btn.setMinimumSize(QSize(60, 30))
        self.prs_set_btn.setStyleSheet(u"")
        icon9 = QIcon()
        icon9.addFile(u":/icons/setting.png", QSize(), QIcon.Normal, QIcon.Off)
        self.prs_set_btn.setIcon(icon9)

        self.horizontalLayout_4.addWidget(self.prs_set_btn)


        self.verticalLayout_7.addLayout(self.horizontalLayout_4)

        self.tableView = QTableView(self.personal_page)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setFont(font2)
        self.tableView.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableView.setTabKeyNavigation(False)
        self.tableView.setProperty("showDropIndicator", False)
        self.tableView.setShowGrid(False)
        self.tableView.setCornerButtonEnabled(False)
        self.tableView.horizontalHeader().setDefaultSectionSize(80)
        self.tableView.verticalHeader().setVisible(False)
        self.tableView.verticalHeader().setHighlightSections(False)

        self.verticalLayout_7.addWidget(self.tableView)


        self.gridLayout.addLayout(self.verticalLayout_7, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.personal_page)
        self.schedule_page = QWidget()
        self.schedule_page.setObjectName(u"schedule_page")
        self.schedule_page.setStyleSheet(u"QPushButton{\n"
"	height: 30px;\n"
"	border :2px solid;\n"
"	border-color: rgb(120, 0, 0);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: #F5FAFE;\n"
"	border :2px solid;\n"
"	border-color: rgb(102, 102, 102);\n"
"	color: #1F95EF;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QComboBox {\n"
"    border: 2px solid;\n"
"	border-color: rgb(120, 0, 0);\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"	font: 57 13pt \"Right Grotesk Small\";\n"
"}\n"
"\n"
"QTableView {\n"
"    border: 1px solid;\n"
"	border-color: rgb(120, 0, 0);\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"	font: 57 13pt \"Right Grotesk Small\";\n"
"}")
        self.gridLayout_3 = QGridLayout(self.schedule_page)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_6 = QSpacerItem(298, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_6)

        self.add_sch_btn = QPushButton(self.schedule_page)
        self.add_sch_btn.setObjectName(u"add_sch_btn")
        self.add_sch_btn.setMinimumSize(QSize(60, 30))
        icon10 = QIcon()
        icon10.addFile(u":/icons/free-icon-font-clock-3917267.png", QSize(), QIcon.Normal, QIcon.Off)
        self.add_sch_btn.setIcon(icon10)

        self.horizontalLayout_6.addWidget(self.add_sch_btn)

        self.sch_qr_btn = QPushButton(self.schedule_page)
        self.sch_qr_btn.setObjectName(u"sch_qr_btn")
        self.sch_qr_btn.setMinimumSize(QSize(60, 30))
        self.sch_qr_btn.setIcon(icon8)

        self.horizontalLayout_6.addWidget(self.sch_qr_btn)

        self.sch_set_btn = QPushButton(self.schedule_page)
        self.sch_set_btn.setObjectName(u"sch_set_btn")
        self.sch_set_btn.setMinimumSize(QSize(60, 30))
        self.sch_set_btn.setIcon(icon9)

        self.horizontalLayout_6.addWidget(self.sch_set_btn)


        self.verticalLayout_8.addLayout(self.horizontalLayout_6)

        self.sch_table = QTableView(self.schedule_page)
        self.sch_table.setObjectName(u"sch_table")

        self.verticalLayout_8.addWidget(self.sch_table)


        self.gridLayout_3.addLayout(self.verticalLayout_8, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.schedule_page)
        self.items_page = QWidget()
        self.items_page.setObjectName(u"items_page")
        self.items_page.setStyleSheet(u"QPushButton{\n"
"	height: 30px;\n"
"	border :2px solid;\n"
"	border-color: rgb(120, 0, 0);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: #F5FAFE;\n"
"	border :2px solid;\n"
"	border-color: rgb(102, 102, 102);\n"
"	color: #1F95EF;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QComboBox {\n"
"    border: 2px solid;\n"
"	border-color: rgb(120, 0, 0);\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"	font: 57 13pt \"Right Grotesk Small\";\n"
"}\n"
"\n"
"QTableView {\n"
"    border: 1px solid;\n"
"	border-color: rgb(120, 0, 0);\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"	font: 57 13pt \"Right Grotesk Small\";\n"
"}")
        self.gridLayout_4 = QGridLayout(self.items_page)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_8 = QSpacerItem(298, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_8)

        self.add_item_btn = QPushButton(self.items_page)
        self.add_item_btn.setObjectName(u"add_item_btn")
        self.add_item_btn.setMinimumSize(QSize(60, 30))
        icon11 = QIcon()
        icon11.addFile(u":/icons/free-icon-font-piggy-bank-7653246.png", QSize(), QIcon.Normal, QIcon.Off)
        self.add_item_btn.setIcon(icon11)

        self.horizontalLayout_5.addWidget(self.add_item_btn)

        self.item_qr_btn = QPushButton(self.items_page)
        self.item_qr_btn.setObjectName(u"item_qr_btn")
        self.item_qr_btn.setMinimumSize(QSize(60, 30))
        self.item_qr_btn.setIcon(icon8)

        self.horizontalLayout_5.addWidget(self.item_qr_btn)

        self.item_set_btn = QPushButton(self.items_page)
        self.item_set_btn.setObjectName(u"item_set_btn")
        self.item_set_btn.setMinimumSize(QSize(60, 30))
        self.item_set_btn.setIcon(icon9)

        self.horizontalLayout_5.addWidget(self.item_set_btn)


        self.verticalLayout_9.addLayout(self.horizontalLayout_5)

        self.item_table = QTableView(self.items_page)
        self.item_table.setObjectName(u"item_table")

        self.verticalLayout_9.addWidget(self.item_table)


        self.gridLayout_4.addLayout(self.verticalLayout_9, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.items_page)
        self.cash_page = QWidget()
        self.cash_page.setObjectName(u"cash_page")
        self.cash_page.setStyleSheet(u"QPushButton{\n"
"	height: 30px;\n"
"	border :2px solid;\n"
"	border-color: rgb(120, 0, 0);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: #F5FAFE;\n"
"	border :2px solid;\n"
"	border-color: rgb(102, 102, 102);\n"
"	color: #1F95EF;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QComboBox {\n"
"    border: 2px solid;\n"
"	border-color: rgb(120, 0, 0);\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"	font: 57 13pt \"Right Grotesk Small\";\n"
"}\n"
"\n"
"QTableView {\n"
"    border: 1px solid;\n"
"	border-color: rgb(120, 0, 0);\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"	font: 57 13pt \"Right Grotesk Small\";\n"
"}")
        self.gridLayout_5 = QGridLayout(self.cash_page)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_7 = QSpacerItem(298, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_7)

        self.add_tck_btn = QPushButton(self.cash_page)
        self.add_tck_btn.setObjectName(u"add_tck_btn")
        self.add_tck_btn.setMinimumSize(QSize(60, 30))
        icon12 = QIcon()
        icon12.addFile(u":/icons/free-icon-font-ticket-3916614.png", QSize(), QIcon.Normal, QIcon.Off)
        self.add_tck_btn.setIcon(icon12)

        self.horizontalLayout_7.addWidget(self.add_tck_btn)

        self.tck_qr_btn = QPushButton(self.cash_page)
        self.tck_qr_btn.setObjectName(u"tck_qr_btn")
        self.tck_qr_btn.setMinimumSize(QSize(60, 30))
        self.tck_qr_btn.setIcon(icon8)

        self.horizontalLayout_7.addWidget(self.tck_qr_btn)

        self.tck_set_btn = QPushButton(self.cash_page)
        self.tck_set_btn.setObjectName(u"tck_set_btn")
        self.tck_set_btn.setMinimumSize(QSize(60, 30))
        self.tck_set_btn.setIcon(icon9)

        self.horizontalLayout_7.addWidget(self.tck_set_btn)


        self.verticalLayout_10.addLayout(self.horizontalLayout_7)

        self.tck_table = QTableView(self.cash_page)
        self.tck_table.setObjectName(u"tck_table")

        self.verticalLayout_10.addWidget(self.tck_table)


        self.gridLayout_5.addLayout(self.verticalLayout_10, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.cash_page)
        self.shows_page = QWidget()
        self.shows_page.setObjectName(u"shows_page")
        self.shows_page.setStyleSheet(u"QPushButton{\n"
"	height: 30px;\n"
"	border :2px solid;\n"
"	border-color: rgb(120, 0, 0);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: #F5FAFE;\n"
"	border :2px solid;\n"
"	border-color: rgb(102, 102, 102);\n"
"	color: #1F95EF;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QComboBox {\n"
"    border: 2px solid;\n"
"	border-color: rgb(120, 0, 0);\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"	font: 57 13pt \"Right Grotesk Small\";\n"
"}\n"
"\n"
"QTableView {\n"
"    border: 1px solid;\n"
"	border-color: rgb(120, 0, 0);\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"	font: 57 13pt \"Right Grotesk Small\";\n"
"}")
        self.gridLayout_6 = QGridLayout(self.shows_page)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.show_cmbox = QComboBox(self.shows_page)
        self.show_cmbox.addItem("")
        self.show_cmbox.addItem("")
        self.show_cmbox.setObjectName(u"show_cmbox")
        self.show_cmbox.setMinimumSize(QSize(115, 30))

        self.horizontalLayout_8.addWidget(self.show_cmbox)

        self.horizontalSpacer_5 = QSpacerItem(58, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_5)

        self.add_role_btn = QPushButton(self.shows_page)
        self.add_role_btn.setObjectName(u"add_role_btn")
        self.add_role_btn.setMinimumSize(QSize(60, 30))
        self.add_role_btn.setIcon(icon7)

        self.horizontalLayout_8.addWidget(self.add_role_btn)

        self.show_qr_btn = QPushButton(self.shows_page)
        self.show_qr_btn.setObjectName(u"show_qr_btn")
        self.show_qr_btn.setMinimumSize(QSize(60, 30))
        self.show_qr_btn.setIcon(icon8)

        self.horizontalLayout_8.addWidget(self.show_qr_btn)

        self.show_set_btn = QPushButton(self.shows_page)
        self.show_set_btn.setObjectName(u"show_set_btn")
        self.show_set_btn.setMinimumSize(QSize(60, 30))
        self.show_set_btn.setIcon(icon9)

        self.horizontalLayout_8.addWidget(self.show_set_btn)


        self.verticalLayout_11.addLayout(self.horizontalLayout_8)

        self.show_table = QTableView(self.shows_page)
        self.show_table.setObjectName(u"show_table")

        self.verticalLayout_11.addWidget(self.show_table)


        self.gridLayout_6.addLayout(self.verticalLayout_11, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.shows_page)

        self.verticalLayout_6.addWidget(self.stackedWidget)


        self.verticalLayout_5.addWidget(self.widget)


        self.gridLayout_2.addWidget(self.main_widget, 0, 2, 1, 1)

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

        self.stackedWidget.setCurrentIndex(0)


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

        self.add_prs_btn.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.prs_qr_btn.setText("")
        self.prs_set_btn.setText("")
        self.add_sch_btn.setText("")
        self.sch_qr_btn.setText("")
        self.sch_set_btn.setText("")
        self.add_item_btn.setText("")
        self.item_qr_btn.setText("")
        self.item_set_btn.setText("")
        self.add_tck_btn.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.tck_qr_btn.setText("")
        self.tck_set_btn.setText("")
        self.show_cmbox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u041f\u043e \u0440\u043e\u043b\u044f\u043c", None))
        self.show_cmbox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u041f\u043e \u0441\u043f\u0435\u043a\u0442\u0430\u043a\u043b\u044f\u043c", None))

        self.add_role_btn.setText("")
        self.show_qr_btn.setText("")
        self.show_set_btn.setText("")
    # retranslateUi

