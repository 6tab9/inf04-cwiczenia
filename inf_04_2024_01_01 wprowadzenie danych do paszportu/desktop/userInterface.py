# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QRadioButton, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1051, 708)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 10, 1031, 631))
        self.MainLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.MainLayout.setObjectName(u"MainLayout")
        self.MainLayout.setContentsMargins(0, 0, 0, 0)
        self.LeftLayout = QVBoxLayout()
        self.LeftLayout.setObjectName(u"LeftLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.numerInput = QLineEdit(self.horizontalLayoutWidget)
        self.numerInput.setObjectName(u"numerInput")

        self.horizontalLayout_2.addWidget(self.numerInput)


        self.LeftLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.imieInput = QLineEdit(self.horizontalLayoutWidget)
        self.imieInput.setObjectName(u"imieInput")

        self.horizontalLayout_3.addWidget(self.imieInput)


        self.LeftLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.nazwiskoInput = QLineEdit(self.horizontalLayoutWidget)
        self.nazwiskoInput.setObjectName(u"nazwiskoInput")
        self.nazwiskoInput.setMaxLength(6666)

        self.horizontalLayout_4.addWidget(self.nazwiskoInput)


        self.LeftLayout.addLayout(self.horizontalLayout_4)

        self.koloroczu = QGroupBox(self.horizontalLayoutWidget)
        self.koloroczu.setObjectName(u"koloroczu")
        self.verticalLayoutWidget_3 = QWidget(self.koloroczu)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(10, 20, 891, 121))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.niebieskieOczy = QRadioButton(self.verticalLayoutWidget_3)
        self.niebieskieOczy.setObjectName(u"niebieskieOczy")
        self.niebieskieOczy.setChecked(True)

        self.verticalLayout.addWidget(self.niebieskieOczy)

        self.zieloneOczy = QRadioButton(self.verticalLayoutWidget_3)
        self.zieloneOczy.setObjectName(u"zieloneOczy")

        self.verticalLayout.addWidget(self.zieloneOczy)

        self.piwneOczy = QRadioButton(self.verticalLayoutWidget_3)
        self.piwneOczy.setObjectName(u"piwneOczy")

        self.verticalLayout.addWidget(self.piwneOczy)


        self.LeftLayout.addWidget(self.koloroczu)


        self.MainLayout.addLayout(self.LeftLayout)

        self.RightLayout = QVBoxLayout()
        self.RightLayout.setObjectName(u"RightLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.portret = QLabel(self.horizontalLayoutWidget)
        self.portret.setObjectName(u"portret")

        self.horizontalLayout.addWidget(self.portret)

        self.linie = QLabel(self.horizontalLayoutWidget)
        self.linie.setObjectName(u"linie")
        self.linie.setFixedHeight(180)

        self.horizontalLayout.addWidget(self.linie)


        self.RightLayout.addLayout(self.horizontalLayout)

        self.WykonajButton = QPushButton(self.horizontalLayoutWidget)
        self.WykonajButton.setObjectName(u"WykonajButton")

        self.RightLayout.addWidget(self.WykonajButton)


        self.MainLayout.addLayout(self.RightLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1051, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Wprowadzanie danych do paszportu. Wykona\u0142: Szymon Orczyk", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Numer", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Imi\u0119", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Nazwisko", None))
        self.koloroczu.setTitle(QCoreApplication.translate("MainWindow", u"Kolor Oczu", None))
        self.niebieskieOczy.setText(QCoreApplication.translate("MainWindow", u"Niebieskie", None))
        self.zieloneOczy.setText(QCoreApplication.translate("MainWindow", u"Zielone", None))
        self.piwneOczy.setText(QCoreApplication.translate("MainWindow", u"Piwne", None))
        self.portret.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.linie.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.WykonajButton.setText(QCoreApplication.translate("MainWindow", u"Ok", None))
    # retranslateUi

