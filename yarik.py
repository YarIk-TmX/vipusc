from PyQt5.QtWidgets import QPushButton, QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout
from photoshop import win2, app2
from victorina import main_window, app3


#Создание окна
app =QApplication([])
win = QWidget()
win.resize(250, 200)
win.setWindowTitle('Выбери что тебе надо:')

x1 = QLabel('           Выбери что вам нужно:')
foto_btn = QPushButton('Фотошоп')
wic_btn = QPushButton('Викторина')



main_win = QHBoxLayout()
winn = QVBoxLayout()
winn.addWidget(x1)

def photoshop():
    win2.show()
    app2.exec_()
def victorina():
    main_window.show()
    app3.exec_()


winn.addLayout(main_win)
main_win.addWidget(foto_btn)
main_win.addWidget(wic_btn)

win.setLayout(winn)

foto_btn.clicked.connect(photoshop)
wic_btn.clicked.connect(victorina)


    












win.show()
app.exec_()
