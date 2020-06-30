import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

from_class = uic.loadUiType("mywindow.ui")[0]


class MyWindow(QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.btn_clicked)

    def btn_clicked(self):
        print("버튼클릭")



app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()