# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'show_info_page.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(779, 643)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 30, 361, 251))
        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(400, 30, 361, 251))
        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(400, 310, 361, 261))
        self.widget_4 = QWidget(self.centralwidget)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(20, 310, 361, 261))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(20, 590, 741, 32))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(110, 10, 191, 16))
        font = QFont()
        font.setFamilies([u"Right Grotesk"])
        font.setPointSize(18)
        self.label.setFont(font)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(500, 10, 191, 16))
        self.label_2.setFont(font)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(110, 290, 191, 16))
        self.label_3.setFont(font)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(490, 290, 201, 16))
        self.label_4.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0441\u0447\u0438\u0442\u0430\u0442\u044c \u043a\u043e\u043b\u0438\u0447\u0435\u0442\u0441\u0432\u043e \u043f\u0440\u043e\u0432\u0435\u0434\u0435\u043d\u043d\u044b\u0445 \u0441\u043f\u0435\u043a\u0442\u0430\u043a\u043b\u0435\u0439 \u043f\u043e \u0434\u0430\u0442\u0430\u043c", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0435\u043c\u044b\u0435 \u0430\u043a\u0442\u0435\u0440\u044b", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0441\u0442\u0430\u0432\u0448\u0438\u0435\u0441\u044f \u043c\u0435\u0441\u0442\u0430", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u043d\u0438\u0435 \u0436\u0430\u043d\u0440\u043e\u0432", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0430\u043c\u044b\u0439 \u043f\u043e\u043f\u0443\u043b\u044f\u0440\u043d\u044b\u0439 \u0430\u0432\u0442\u043e\u0440", None))
    # retranslateUi

