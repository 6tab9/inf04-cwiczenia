import sys
from userInterface import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow,QApplication
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.setWindowTitle("Wprowadzenie danych do paszportu. Wykonał: ja")
        # self.setGeometry(600,400,600,400)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__=="__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setStyleSheet("""
    QMainWindow{
        background:#5F9EA0
    """)
    window.show()
    sys.exit(app.exec())