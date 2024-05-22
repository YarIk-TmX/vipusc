from PyQt5.QtWidgets import QPushButton, QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout
from photoshop import win2, app2
from victorina import main_window, app3
from chislo import win4, app4
from clicker import clicker
#Создание окна
app =QApplication([])
win = QWidget()
win.resize(250, 200)
win.setWindowTitle('Выбери что тебе надо:')

x1 = QLabel('           Выбери что вам нужно:')
foto_btn = QPushButton('Фотошоп')
wic_btn = QPushButton('Викторина')
chslo_btn = QPushButton('Угадай число')
clicker_btn = QPushButton('Кликер')


main_win = QHBoxLayout()
winn = QVBoxLayout()
winn.addWidget(x1)

def photoshop():
    win2.show()
    app2.exec_()
def victorina():
    main_window.show()
    app3.exec_()
def chislo():
    win4.show()
    app4.exec_()

def clicker1():
    clicker()

winn.addLayout(main_win)
main_win.addWidget(foto_btn)
main_win.addWidget(wic_btn)
main_win.addWidget(chslo_btn)
main_win.addWidget(clicker_btn)

win.setLayout(winn)

foto_btn.clicked.connect(photoshop)
wic_btn.clicked.connect(victorina)
chslo_btn.clicked.connect(chislo)
clicker_btn.clicked.connect(clicker1)

    












win.show()
app.exec_()




