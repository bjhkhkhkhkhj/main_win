from PyQt5.QtWidgets import*
from PyQt5.QtCore import Qt
app=QApplication([])

q=QLabel("Введіть запит")
q_red=QLineEdit()
a=QLabel("Ввудіть вірну відповдь")
a_red=QLineEdit()
w1=QLabel("Введіть 1 хибну відповідь")
w1_red=QLineEdit()
w2=QLabel("Введіть 2 хибну відповідь")
w2_red=QLineEdit()
w3=QLabel("Введіть 3 хибну відповідь")
w3_red=QLineEdit()

btn_add = QPushButton("Додати запит")
btn_clear=QPushButton("очистити")
btn_back=QPushButton("Назад")

stat=QLabel("Статистика")
stat_info=QLabel("Інфо")

line_menu=QVBoxLayout()
line1_meny=QVBoxLayout()
line2_meny=QVBoxLayout()

line1_meny.addWidget(q)
line1_meny.addWidget(a)
line1_meny.addWidget(w1)
line1_meny.addWidget(w2)
line1_meny.addWidget(w3)

line2_meny.addWidget(q_red)
line2_meny.addWidget(a_red)
line2_meny.addWidget(w1_red)
line2_meny.addWidget(w2_red)
line2_meny.addWidget(w3_red)

line_hor=QHBoxLayout()
line2_hor=QHBoxLayout()

line_hor.addLayout(line1_meny)
line_hor.addLayout(line2_meny)
line2_hor.addLayout(btn_add)
line2_hor.addLayout(btn_clear)


line_menu.addLayout(line_hor)
line_menu.addLayout(line2_hor)

line_menu.addWidget(stat)
line_menu.addWidget(stat_info)
line_menu.addWidget(btn_back)

menu_win=QWidget()
menu_win.setLayout()
menu_win.show()


app.exec()

