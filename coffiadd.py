import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, \
    QTableWidgetItem
import sqlite3


class dopvin(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)

    def dop(self):
        cur = self.con.cursor()
        ob = self.lineEdit.text()
        so = self.lineEdit_2.text()
        vk = self.lineEdit_3.text()
        obe = self.lineEdit_4.text()
        zn = self.lineEdit_5.text()
        cur.execute(
            f"INSERT INTO films(обжарка, сорт, вкус, объём, цена) VALUES('{ob}'"
            f",'{so}', '{vk}', '{int(obe)}',"
            f" '{int(zn)}')")
        self.con.commit()


app = QApplication(sys.argv)
ex = dopvin()
ex.show()
sys.exit(app.exec_())
