import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QHBoxLayout, QMessageBox, QRadioButton
from PyQt5.QtCore import Qt
app = QApplication([])
my_win = QWidget()

def show_win():
    u_win = QMessageBox()
    u_win.setText('Correct!\nYou win a gyro scooter')
    u_win.setWindowTitle('YESSS')
    u_win.exec_()
def show_lose():
    u_wrong = QMessageBox()
    u_wrong.setText('Wrong!\nYou win a company poster💀')
    u_wrong.setWindowTitle('Really man...')
    u_wrong.exec_()

my_win.setWindowTitle('Competition from Crazy People')
question = QLabel('What year did the channel recieve the "gold play button" from youtube?')
btn_ans1 = QRadioButton('2005')
btn_ans2 = QRadioButton('2010')
btn_ans3 = QRadioButton('2015')
btn_ans4 = QRadioButton('2020')
layout_main = QVBoxLayout()
layout_main.addWidget(question, alignment = Qt.AlignCenter)
layout_main.addWidget(btn_ans1, alignment = Qt.AlignCenter)
layout_main.addWidget(btn_ans2, alignment = Qt.AlignCenter)
layout_main.addWidget(btn_ans3, alignment = Qt.AlignCenter)
layout_main.addWidget(btn_ans4, alignment = Qt.AlignCenter)


btn_ans1.clicked.connect(show_lose)
btn_ans2.clicked.connect(show_lose)
btn_ans3.clicked.connect(show_win)
btn_ans4.clicked.connect(show_lose)

my_win.setLayout(layout_main)
my_win.show()
app.exec_()