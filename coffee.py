import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, \
    QTableWidgetItem
import sqlite3

from coffiadd import dopvin


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('bd.ui', self)
        self.con = sqlite3.connect("coffe(1).db")
        self.pushButton.clicked.connect(self.update_result)
        self.pushButton_3.clicked.connect(self.newcof)
        self.modified = {}
        self.titles = None

    def update_result(self):
        cur = self.con.cursor()
        print(0)

        result = cur.execute("Select * from coffe WHERE id=?",
                             (self.spinBox.text(),)).fetchall()
        print(result)

        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setColumnCount(len(result[0]))
        self.titles = [description[0] for description in cur.description]
        self.tableWidget.setHorizontalHeaderLabels(self.titles)
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
        self.modified = {}

    def newcof(self):
        ex2 = dopvin()
        ex2.show()
        


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
