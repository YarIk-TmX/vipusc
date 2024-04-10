from PyQt5.QtWidgets import QRadioButton, QHBoxLayout, QApplication, QWidget, QLabel, QGroupBox, QVBoxLayout, QPushButton, QButtonGroup
from random import *

class Question:

    def __init__(self,question,right_answer, worng1, worng2, worng3):
        self.question = question
        self.right_answer = right_answer
        self.worng1 = worng1
        self.worng2 = worng2
        self.worng3 = worng3



app3 = QApplication([])
main_window = QWidget()
main_window.cg = -1
main_window.total = 0
main_window.score = 0


lal = QLabel('Какая лучшая игра?')
b = QPushButton('ОТВЕТ')

ml = QVBoxLayout()
ml1 = QHBoxLayout()
ml2 = QHBoxLayout()

ml1.addWidget(lal)
ml2.addWidget(b)


RGB = QGroupBox('ВАРИАНТЫ')
r1 = QRadioButton('Fortnite')
r2 = QRadioButton('Pubg')
r3 = QRadioButton('Brawl Stars')
r4 = QRadioButton('Standoff 2')

rg = QButtonGroup()
rg.addButton(r1)
rg.addButton(r2)
rg.addButton(r3)
rg.addButton(r4)

lal1 = QHBoxLayout()
lal2 = QVBoxLayout()
lal3 = QVBoxLayout()



lal2.addWidget(r1)
lal2.addWidget(r2)
lal3.addWidget(r3)
lal3.addWidget(r4)
lal1.addLayout(lal2)
lal1.addLayout(lal3)

RGB.setLayout(lal1)

RGB1 = QGroupBox('Ответ:')

f1 = QLabel('неправельно/правельно')
f2 = QLabel('Правильный ответ будет тут')


ll2 = QVBoxLayout()

ll2.addWidget(f1)
ll2.addWidget(f2)

RGB1.setLayout(ll2)

ml.addLayout(ml1)
ml.addWidget(RGB)
ml.addWidget(RGB1)
ml.addLayout(ml2)


RGB1.hide()

def sres():
    RGB.hide()
    RGB1.show()
    b.setText('Далее')
def sre():
    RGB1.hide()
    RGB.show()
    b.setText('ОТВЕТ')
    rg.setExclusive(False)
    r1.setChecked(False)
    r2.setChecked(False)
    r3.setChecked(False)
    r4.setChecked(False)
    rg.setExclusive(True)



rrrr = [r1, r2, r3, r4]
ques = []
q = Question('какая планета больше?', 'меркурий', 'венера', 'марс', 'юпитер')
ques.append(q)
q = Question('В каком году была основана Москва?', '1147', '1242', '1945', '1488')
ques.append(q)
q = Question('2 +2?', '4', '3', '21', 'А?')
ques.append(q)
q = Question('Какая лучшая ига?', 'Fortnite', 'Для каждого человека есть собственна ялюбимая игра', 'Dota 2', 'Minecraft')
ques.append(q)
q = Question('3000 + 5000 : 5601 : 34 * 123 : 0?', '0', '68903', '5698', '3478')
ques.append(q)
q = Question('В какой стране мы живём?', 'Россия', 'Где-то', 'В Аерике', 'беспонятия')
ques.append(q)
q = Question('В како году было ледовое побоище?', '1242', '1488', '0', 'беспонятия')
ques.append(q)
q = Question('Когда была война с китаем и китаем?', 'никогда', '1200', '1488', '1230')
ques.append(q)
q = Question('В каком году была куликовская битва?', '1380', '1488', '1506', 'беспонятия')
ques.append(q)
def ask(q):
    shuffle(rrrr)
    rrrr[0].setText(q.right_answer)
    rrrr[1].setText(q.worng1)
    rrrr[2].setText(q.worng2)
    rrrr[3].setText(q.worng3)
    lal.setText(q.question)
    f2.setText(q.right_answer)
    sre() 

def cec():
    if rrrr[0].isChecked():
        f1.setText('Верно')
        main_window.score += 1
        sres()
    else:
        if rrrr[1].isChecked() or rrrr[2].isChecked() or rrrr[3].isChecked():
            f1.setText('неправельно')
            sres()
def ng():
    main_window.cg += 1 
    main_window.total += 1 
    print('Статистика теста')
    print('Всего вопросов', main_window.total)
    print('Правельных ответов', main_window.score)
    print('Рейтинг', main_window.score/main_window.total*100)
    if main_window.cg >= len(ques):
        main_window.cg = 0  
 

    q = ques[main_window.cg]
    ask(q)

def helper():
    if b.text() == 'ОТВЕТ':
        cec()
    else:
        ng()
    




b.clicked.connect(helper)
ng()

main_window.setLayout(ml)
















