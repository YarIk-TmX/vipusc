from PyQt5.QtWidgets import QPushButton, QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit
from random import *

app4 =QApplication([])
win4 = QWidget()


win4.setWindowTitle('игра угадай число')

v1 = QLabel('Твой ответ:')
lab_ans = QLabel('')
otvet = QLineEdit()
otvet_btn = QPushButton('Ответить')

main_win2 = QHBoxLayout()
winn = QVBoxLayout()


winn.addWidget(v1)
winn.addWidget(lab_ans)
winn.addLayout(main_win2)
win4.setLayout(winn)
main_win2.addWidget(otvet)
main_win2.addWidget(otvet_btn)




chislo = randint(1, 100)


def check():
    if int(otvet.text()) < chislo:
        pendos = 'Число больше'
    elif int(otvet.text()) > chislo:
        pendos = 'Число меньше'
    elif int(otvet.text()) == chislo:
        pendos = 'Верно'
    otvet.clear()
    lab_ans.setText(str(pendos))




otvet_btn.clicked.connect(check)


