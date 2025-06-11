# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerNnfQbM.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFormLayout,
    QGroupBox, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(656, 426)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 301, 241))
        self.widget = QWidget(self.groupBox)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(11, 27, 281, 171))
        self.formLayout = QFormLayout(self.widget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setVerticalSpacing(30)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label)

        self.nameEdit = QLineEdit(self.widget)
        self.nameEdit.setObjectName(u"nameEdit")
        self.nameEdit.setStyleSheet(u"")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.nameEdit)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.snameEdit = QLineEdit(self.widget)
        self.snameEdit.setObjectName(u"snameEdit")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.snameEdit)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.jobComboBox = QComboBox(self.widget)
        self.jobComboBox.setObjectName(u"jobComboBox")
        self.jobComboBox.addItems(["Kierownik","Starszy programista","Młodszy programista","Tester"])

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.jobComboBox)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(340, 10, 301, 241))
        self.widget1 = QWidget(self.groupBox_2)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(20, 20, 261, 144))
        self.formLayout_2 = QFormLayout(self.widget1)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setHorizontalSpacing(6)
        self.formLayout_2.setVerticalSpacing(20)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.widget1)
        self.label_4.setObjectName(u"label_4")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_4)

        self.passwordLengthEdit = QLineEdit(self.widget1)
        self.passwordLengthEdit.setObjectName(u"passwordLengthEdit")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.passwordLengthEdit)

        self.letterCheckBox = QCheckBox(self.widget1)
        self.letterCheckBox.setObjectName(u"letterCheckBox")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.SpanningRole, self.letterCheckBox)

        self.numberCheckBox = QCheckBox(self.widget1)
        self.numberCheckBox.setObjectName(u"numberCheckBox")

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.SpanningRole, self.numberCheckBox)

        self.specialCharacterCheckBox = QCheckBox(self.widget1)
        self.specialCharacterCheckBox.setObjectName(u"specialCharacterCheckBox")

        self.formLayout_2.setWidget(3, QFormLayout.ItemRole.SpanningRole, self.specialCharacterCheckBox)

        self.generatePasswordButton = QPushButton(self.groupBox_2)
        self.generatePasswordButton.setObjectName(u"generatePasswordButton")
        self.generatePasswordButton.setGeometry(QRect(70, 190, 161, 24))
        self.finishButton = QPushButton(self.centralwidget)
        self.finishButton.setObjectName(u"finishButton")
        self.finishButton.setGeometry(QRect(200, 330, 271, 24))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 656, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        MainWindow.setStyleSheet("""
        QMainWindow{
            background:#B0C4DE;
        }
        QPushButton{
            background:#4682B4;
        }
        """)
        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Dane pracownika", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Imi\u0119", None))
#if QT_CONFIG(statustip)
        self.nameEdit.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Nazwisko", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Stanowisko", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Generowanie has\u0142a", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Ile znak\u00f3w?", None))
        self.letterCheckBox.setText(QCoreApplication.translate("MainWindow", u"Ma\u0142e i Wielkie Litery", None))
        self.numberCheckBox.setText(QCoreApplication.translate("MainWindow", u"Cyfry", None))
        self.specialCharacterCheckBox.setText(QCoreApplication.translate("MainWindow", u"Znaki specjalne", None))
        self.generatePasswordButton.setText(QCoreApplication.translate("MainWindow", u"Generuj has\u0142o", None))
        self.finishButton.setText(QCoreApplication.translate("MainWindow", u"Zatwierd\u017a", None))
    # retranslateUi

