# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_design.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QLabel,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(497, 222)
        Form.setStyleSheet(u"")
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(160, 160, 171, 31))
        font = QFont()
        font.setFamilies([u"Right Grotesk"])
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"QPushButton:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1,   stop:0 #e5e1d8, stop:1 #e5e1d8);\n"
"}\n"
"QPushButton {\n"
"     background-color:  #E7EAEF; border: 1px solid black;\n"
"     border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(170, 170, 127)\n"
"}")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 0, 331, 61))
        font1 = QFont()
        font1.setFamilies([u"Right Grotesk"])
        font1.setPointSize(36)
        self.label.setFont(font1)
        self.label.setFrameShadow(QFrame.Plain)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(80, 60, 331, 80))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setFamilies([u"Right Grotesk"])
        font2.setPointSize(18)
        self.label_2.setFont(font2)
        self.label_2.setFrameShadow(QFrame.Plain)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setWordWrap(False)

        self.verticalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        font3 = QFont()
        font3.setFamilies([u"Right Grotesk"])
        font3.setPointSize(14)
        self.label_3.setFont(font3)
        self.label_3.setFrameShadow(QFrame.Plain)
        self.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_3.setWordWrap(False)

        self.verticalLayout.addWidget(self.label_3)

        self.comboBox = QComboBox(self.widget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        font4 = QFont()
        font4.setFamilies([u"Right Grotesk Small"])
        self.comboBox.setFont(font4)
        self.comboBox.setMaxVisibleItems(4)
        self.comboBox.setFrame(True)
        self.comboBox.setModelColumn(0)

        self.verticalLayout.addWidget(self.comboBox)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u0410\u0432\u0442\u043e\u0440\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u0412\u043e\u0439\u0442\u0438", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0423\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0442\u0435\u0430\u0442\u0440\u043e\u043c", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u0410\u0432\u0442\u043e\u0440\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u0420\u043e\u043b\u044c \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"\u0414\u0438\u0440\u0435\u043a\u0442\u043e\u0440", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Form", u"\u0420\u0435\u0436\u0438\u0441\u0441\u0435\u0440-\u043f\u043e\u0441\u0442\u0430\u043d\u043e\u0432\u0449\u0438\u043a", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Form", u"\u041a\u0430\u0441\u0441\u0438\u0440", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Form", u"\u0410\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0430\u0442\u043e\u0440 \u0431\u0430\u0437 \u0434\u0430\u043d\u043d\u044b\u0445", None))

    # retranslateUi

