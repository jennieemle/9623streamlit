import streamlit as st
view = [100, 150, 30]
st.write('## customer view')
st.write('## raw')
view
st.write('## bar chart')
st.bar_chart(view)
import pandas as pd
sview = pd.Series(view)
sview

import sys
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        #self.setGeometry(800, 400, 300, 150)

        btn1 = QPushButton('click', self)
        btn1.move(0, 0)
        btn1.clicked.connect(self.btn1_clicked)

        btn2 = QPushButton('clear', self)
        btn2.move(100, 0)
        btn2.clicked.connect(self.btn2_clicked)

        textLabel = QLabel('message: ', self)
        textLabel.move(20, 30)

        self.label = QLabel('', self)
        self.label.move(80, 30)
        self.label.resize(150, 30)

    def btn1_clicked(self):
        self.label.setText("버튼이 클릭되었습니다.")

    def btn2_clicked(self):
        self.label.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()
