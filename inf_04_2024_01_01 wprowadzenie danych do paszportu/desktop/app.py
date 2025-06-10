import sys

from PIL.ImageQt import QPixmap

from userInterface import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.setWindowTitle("Wprowadzenie danych do paszportu. Wykonał: ja")
        # self.setGeometry(600,400,600,400)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.portret.setPixmap(QPixmap(f"../img/000-zdjecie.jpg"))
        self.ui.linie.setPixmap(QPixmap(f"../img/000-odcisk.jpg"))
        self.ui.numerInput.editingFinished.connect(self.setImage)
        self.ui.WykonajButton.clicked.connect(self.showCredentials)
    def setImage(self):
        self.ui.portret.setPixmap(QPixmap(f"../img/{self.ui.numerInput.text()}-zdjecie.jpg"))
        self.ui.linie.setPixmap(QPixmap(f"../img/{self.ui.numerInput.text()}-odcisk.jpg"))
    def showCredentials(self):
        msg = QMessageBox()
        msg.setText(f"{self.ui.imieInput.text()} {self.ui.nazwiskoInput.text()} kolor oczu {self.getKolorOczu()}")
        if self.ui.imieInput.text()=="" or self.ui.nazwiskoInput.text()=="":
            msg.setText("Wprowadź dane")
        msg.exec()
    def getKolorOczu(self):
        for radio in self.ui.verticalLayoutWidget_3.children()[1:]:
            if radio.isChecked():
                return radio.objectName()[:-4]


if __name__=="__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setStyleSheet("""
    QWidget{
        background-color:#5F9EA0;
    }
    QPushButton, QLineEdit{
        background-color:#F0FFFF;
        color:black;
    }
    """)
    window.show()
    sys.exit(app.exec())