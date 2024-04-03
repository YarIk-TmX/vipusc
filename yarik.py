from PyQt5.QtWidgets import QPushButton, QApplication, QWidget, QLabel, QListWidget, QVBoxLayout, QHBoxLayout, QFileDialog
from PyQt5.QtGui import QPixmap
from PIL import Image
import os
from PIL import ImageFilter
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



winn.addLayout(main_win)
main_win.addWidget(foto_btn)
main_win.addWidget(wic_btn)

win.setLayout(winn)




















win.show()
app.exec_()
