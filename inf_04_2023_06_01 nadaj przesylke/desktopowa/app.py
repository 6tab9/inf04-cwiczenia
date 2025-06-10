import re
import sys

from PySide6.QtWidgets import *
from ui_paczka import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Nadaj Przesyłkę, PESEL:")
        self.ui.postRadio.setChecked(True)
        self.ustawCene()
        self.ui.cenaCheckButton.clicked.connect(self.ustawCene)
        self.ui.finishButton.clicked.connect(self.checkData)
    def checkData(self):
        if re.match("^[0-9]{5}$",self.ui.pocztaInput.text()):
            msg = QMessageBox()
            msg.setText("Dane przesyłki zostały wprowadzone")
            msg.exec()
        elif len(self.ui.pocztaInput.text()) != 5:
            msg = QMessageBox()
            msg.setText("Nieprawidłowa ilość cyfr w kodzie pocztowym")
            msg.exec()
        else:
            msg = QMessageBox()
            msg.setText("Kod pocztowy powinien składać się z samych cyfr")
            msg.exec()

    def ustawCene(self):
        self.ui.cenaOutput.setText(f"Cena: {self.ogarnijCene()}zł")
    def ogarnijCene(self):
        if self.ui.postRadio.isChecked():
            return "1"
        elif self.ui.letterRadio.isChecked():
            return "1,5"
        elif self.ui.packageRadio.isChecked():
            return "10"


if __name__=="__main__":
    app = QApplication()
    window = MainWindow()
    window.show()

    sys.exit(app.exec())