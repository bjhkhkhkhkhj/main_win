from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import*
def switch_screen():
    if btn_answer.text()=="Відповісти":
        qwestion_group.hide()
        answer_group.show()
        btn_answer.setText("Наступне питання")
    else:
        qwestion_group.hide()
        answer_group.show()
        btn_answer.setText("Відповісти")

btn_menu=QPushButton("Меню")
btn_sleep=QPushButton("Відпочити")
btn_answer=QPushButton("Відповісти")
timer=QSpinBox()
timer.setValue(30)
timer_text=QLabel("Хвилин")

right_aswer=QLabel("Питання")
text_qwestion=QLabel("Відповідь")
text_result=QLabel("Результат")

rbtn1=QRadioButton("1")
rbtn2=QRadioButton("2")
rbtn3=QRadioButton("3")
rbtn4=QRadioButton("4")

radiogroup =QButtonGroup()

radiogroup.addButton(rbtn1)
radiogroup.addButton(rbtn2)
radiogroup.addButton(rbtn3)
radiogroup.addButton(rbtn4)

qwestion_group=QGroupBox("Варіанти відповідей")
answer_group=QGroupBox("Результат тесту")

line=QVBoxLayout()
line1=QVBoxLayout()
line2=QVBoxLayout()
line3=QVBoxLayout()
line3_q=QVBoxLayout()
line3_a=QVBoxLayout()
line4=QVBoxLayout()

line_v1=QVBoxLayout()
line_v2=QVBoxLayout()


line_v1.addWidget(rbtn1)
line_v1.addWidget(rbtn2)
line_v2.addWidget(rbtn3)
line_v2.addWidget(rbtn4)

line3_q.addLayout(line_v1)

line3_q.addLayout(line_v2)
