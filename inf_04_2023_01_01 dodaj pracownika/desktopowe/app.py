import random
import sys

from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox
from ui import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.password = ""
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.generatePasswordButton.clicked.connect(self.displayPassword)
        self.ui.finishButton.clicked.connect(self.displayPracownikData)

    def generatePassword(self):
        passNumbers,passLetters,passSpecialCharacters = "0123456789","abcdefghijklmnoprstuvwxyz","!@#$%^&*()"
        passLength = int(self.ui.passwordLengthEdit.text())
        if self.ui.numberCheckBox.isChecked():
            self.password+=passNumbers[random.randint(0,len(passNumbers)-1)]
            passLength-=1
        if self.ui.letterCheckBox.isChecked():
            self.password+=passLetters[random.randint(0,len(passLetters)-1)]
            passLength-=1
        if self.ui.specialCharacterCheckBox.isChecked():
            self.password+=passSpecialCharacters[random.randint(0,len(passSpecialCharacters)-1)]
            passLength-=1
        for i in range(passLength):
            self.password+=passLetters[random.randint(0,len(passLetters)-1)]
        return self.password
    def displayPassword(self):
        msg = QMessageBox()
        msg.setText(self.generatePassword())
        msg.exec()
    def displayPracownikData(self):
        msg = QMessageBox()
        msg.setText(f"Dane pracownika: {self.ui.nameEdit.text()} {self.ui.snameEdit.text()} {self.ui.jobComboBox.currentText()} Hasło: {self.password}")
        msg.exec()


if __name__=="__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec())