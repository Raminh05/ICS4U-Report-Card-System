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
        classAverage = QLabel("Class Average:" + " temp average")
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
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student View")
        assingmentTable = QTableWidget(10, 3)
        studentSubject = QLabel("Temp Student Name")
        subjectGrade = QLabel("Grade:" + " 50%")
        returnButton = QPushButton("Return to class view")
        addAssignment = QPushButton("Add Assignment")
        halfLayout = QVBoxLayout()
        topLayout = QHBoxLayout()
        bottomLayout = QHBoxLayout()
        topLayout.addWidget(studentSubject)
        topLayout.addWidget(subjectGrade)
        topLayout.addWidget(returnButton)
        bottomLayout.addWidget(assingmentTable)
        bottomLayout.addWidget(addAssignment)
        halfLayout.addLayout(topLayout)
        halfLayout.addLayout(bottomLayout)
        self.setLayout(halfLayout)
        returnButton.clicked.connect(self.closeButtonClick)
        addAssignment.clicked.connect(self.openNewAssignment)
    def closeButtonClick(self, checked):
        self.w2 = studentView()
        self.w2.close()
    def openNewAssignment(self, checked):
        self.w3 = addingAssignment()
        self.w3.show()

#Window for adding an assignment to a student
class addingAssignment(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("New Assignment For Selected Student")
        assignmentName = QLineEdit()
        gradeAchieved = QLineEdit()
        finalWindowLayout = QVBoxLayout()
        assignmentName.setPlaceholderText("Assignment Name")
        gradeAchieved.setPlaceholderText("Grade Achieved")
        finalWindowLayout.addWidget(assignmentName)
        finalWindowLayout.addWidget(gradeAchieved)
        self.setLayout(finalWindowLayout)


#Windows are hidden by default and must be told to show up
w = MainWindow()
w.show()
#Continuously running the window
app.exec()