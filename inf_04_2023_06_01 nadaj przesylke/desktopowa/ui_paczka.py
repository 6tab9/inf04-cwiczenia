# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'paczkaIjWkPe.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QGridLayout, QGroupBox,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QRadioButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(657, 406)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.imgLabel = QLabel(self.centralwidget)
        self.imgLabel.setObjectName(u"imgLabel")
        self.imgLabel.setGeometry(QRect(20, 230, 49, 16))
        self.cenaOutput = QLabel(self.centralwidget)
        self.cenaOutput.setObjectName(u"cenaOutput")
        self.cenaOutput.setGeometry(QRect(148, 230, 101, 20))
        self.cenaOutput.setStyleSheet(u"font-weight:bold;\n"
"font-size:15px;")
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(310, 20, 321, 231))
        self.gridLayout = QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.ulicaInput = QLineEdit(self.groupBox_2)
        self.ulicaInput.setObjectName(u"ulicaInput")

        self.verticalLayout_2.addWidget(self.ulicaInput)

        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)

        self.pocztaInput = QLineEdit(self.groupBox_2)
        self.pocztaInput.setObjectName(u"pocztaInput")

        self.verticalLayout_2.addWidget(self.pocztaInput)

        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_2.addWidget(self.label_4)

        self.miastoInput = QLineEdit(self.groupBox_2)
        self.miastoInput.setObjectName(u"miastoInput")

        self.verticalLayout_2.addWidget(self.miastoInput)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.finishButton = QPushButton(self.centralwidget)
        self.finishButton.setObjectName(u"finishButton")
        self.finishButton.setGeometry(QRect(20, 320, 611, 24))
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 20, 221, 171))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.layoutWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.postRadio = QRadioButton(self.groupBox)
        self.postRadio.setObjectName(u"postRadio")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.postRadio)

        self.letterRadio = QRadioButton(self.groupBox)
        self.letterRadio.setObjectName(u"letterRadio")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.letterRadio)

        self.packageRadio = QRadioButton(self.groupBox)
        self.packageRadio.setObjectName(u"packageRadio")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.packageRadio)


        self.verticalLayout.addWidget(self.groupBox)

        self.cenaCheckButton = QPushButton(self.layoutWidget)
        self.cenaCheckButton.setObjectName(u"cenaCheckButton")

        self.verticalLayout.addWidget(self.cenaCheckButton)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 657, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.imgLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.cenaOutput.setText(QCoreApplication.translate("MainWindow", u"Cena:", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Dane adresowe", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Ulica z numerem", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Kod pocztowy", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Miasto", None))
        self.finishButton.setText(QCoreApplication.translate("MainWindow", u"Zatwierd\u017a", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Rodzaj przesy\u0142ki", None))
        self.postRadio.setText(QCoreApplication.translate("MainWindow", u"Poczt\u00f3wka", None))
        self.letterRadio.setText(QCoreApplication.translate("MainWindow", u"List", None))
        self.packageRadio.setText(QCoreApplication.translate("MainWindow", u"Paczka", None))
        self.cenaCheckButton.setText(QCoreApplication.translate("MainWindow", u"Sprawd\u017a cen\u0119", None))
    # retranslateUi

