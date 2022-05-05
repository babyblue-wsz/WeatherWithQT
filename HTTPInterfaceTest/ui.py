from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QPlainTextEdit, QMessageBox
from PyQt5.QtCore import QFile
class Stats():
    def __init__(self):
        self.ui = uic.loadUi("ui.ui")

app = QApplication([])
stats = Stats()
stats.ui.show()
app.exec_()