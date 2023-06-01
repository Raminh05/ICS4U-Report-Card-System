import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, \
    QPushButton, QHBoxLayout
from People import Student


def main():
    app = QApplication(sys.argv)

    # main window
    win = QMainWindow()
    win.setGeometry(100, 100, 460, 80)
    win.setWindowTitle("My great app")

    # layout
    box = QWidget()                               #(win)
    box.setGeometry(0, 0, 460, 80)
    layout = QHBoxLayout(box)                     #(win)
#    box.setLayout(layout)                        # ---
    win.setCentralWidget(box)                     # +++

    btns = []

    student_list = [
        Student("Kelvin", "Hall", 23423, {"Assignment 1": 93}),
        Student("Minh", "Nguyen", 23432, {"Assignment 2": 95})
    ]

    # creating 10 buttons
    for count, student in enumerate(student_list):
        btn = QPushButton(f'{student.firstname} {student.lastname}') #, box)
        btns.append(btn)
        layout.addWidget(btns[count], count)

    # accessing buttons text
#       btn.clicked.connect(lambda: print(btn.text()))                 # ---
        btn.clicked.connect(lambda ch, text=btn.text(): print(text))   # +++

    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()