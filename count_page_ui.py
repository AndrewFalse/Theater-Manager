# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'count_page.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(333, 252)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(110, 140, 113, 32))
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(42, 40, 261, 21))
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(40, 100, 261, 21))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 20, 60, 16))
        font = QFont()
        font.setFamilies([u"Right Grotesk"])
        font.setPointSize(18)
        self.label.setFont(font)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 80, 60, 16))
        self.label_2.setFont(font)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 180, 271, 51))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(60, 120, 221, 16))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(60, 60, 221, 16))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0441\u0447\u0438\u0442\u0430\u0442\u044c", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u043d\u0430\u0447\u0430\u043b\u043e", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u043a\u043e\u043d\u0435\u0446", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0444\u043e\u0440\u043c\u0430\u0442 \u0434\u0430\u0442\u044b (\u0433\u043e\u0434-\u043c\u0435\u0441\u044f\u0446-\u0447\u0438\u0441\u043b\u043e)", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0444\u043e\u0440\u043c\u0430\u0442 \u0434\u0430\u0442\u044b (\u0433\u043e\u0434-\u043c\u0435\u0441\u044f\u0446-\u0447\u0438\u0441\u043b\u043e)", None))
    # retranslateUi

