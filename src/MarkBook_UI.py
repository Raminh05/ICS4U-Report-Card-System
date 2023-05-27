from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QTableView, QTableWidget, QTableWidgetItem
import sys
from Student import Student
#Allows for command line arguments
app = QApplication(sys.argv)
#Class for the main window
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
    #Set the window title
        self.setWindowTitle("Temporary")
    #Making the Table
        tableWidget = QTableWidget(10, 4)
    #Return to class selection
        exitButton = QPushButton("Return to class selection")
    #Delete buttons
        deleteButton = QPushButton("Delete Student")
    #View buttons
        viewButton = QPushButton("View Student")
    #Student name
        studentName = QTableWidgetItem("Temp Student name")
    #Student Grade
        studentGrade = QTableWidgetItem("50" + "%")
    #Class information
        classCode = QLabel("temp class code")
        classAverage = QLabel("temp average")
    #Layout of the page
        primaryLayout = QVBoxLayout()
        secondaryLayout = QHBoxLayout()
        secondaryLayout.addWidget(classCode)
        secondaryLayout.addWidget(classAverage)
        secondaryLayout.addWidget(exitButton)
        primaryLayout.addLayout(secondaryLayout)
        primaryLayout.addWidget(tableWidget)
    #Adding delete buttons
        tableWidget.setCellWidget(0, 0, deleteButton)
    #Adding View Buttons
        tableWidget.setCellWidget(0, 1, viewButton)
    #Adding student name
        tableWidget.setItem(0, 2, studentName)
    #Adding student average
        tableWidget.setItem(0, 3, studentGrade)
    #Resizing the table to fit names
        tableWidget.resizeColumnToContents(2)
    #Making the student view pop-up appear
        viewButton.clicked.connect(self.studentWindow)
    #A widget must exist to create the window
        widget = QWidget()
    #Adding layout to the widget
        widget.setLayout(primaryLayout)
    #Declaring it as the main widget
        self.setCentralWidget(widget)
    #Showing the student view
    def studentWindow(self, checked):
        self.w2 = studentView()
        self.w2.show()
#Student view window
class studentView(QWidget):
    def __innit__(self):
        super().__innit__()
        self.setWindowTitle("Student View")
        layout = QVBoxLayout()
        presentLabel = QLabel("OH My GOD")
        layout.addWidget(presentLabel)
        self.setLayout(layout)

#Windows are hidden by default and must be told to show up
w = MainWindow()
w.show()
#Continuously running the window
app.exec()