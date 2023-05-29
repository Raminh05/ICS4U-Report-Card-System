from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QComboBox, QTableWidget, QTableWidgetItem, QStackedLayout
import sys

#Allows for command line arguments
app = QApplication(sys.argv)

#Class for the main window
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
    #Set the window title
        self.setWindowTitle("Temporary")
    #Making the Table
        tableWidget = QTableWidget(10, 6)
    #Return to class selection
        exitButton = QPushButton("Return to class selection")
    #Delete buttons
        deleteButton = QPushButton("Delete Student")
    #View buttons
        viewButton = QPushButton("View Student")
    #Student name
        studentFirstName = QTableWidgetItem(" " + "Nathan" + " ")
        studentLastName = QTableWidgetItem(" " + "Hellems" + " ")
    #Student number
        studentNumber = QTableWidgetItem("354339771")
    #Student Grade
        studentGrade = QTableWidgetItem("100" + "%")
    #Class information
        classCode = QLabel("temp class code")
        classAverage = QLabel("Class Average:" + " temp average")
    #Home window
        homeWindow = QWidget()
    #Class view
        classWindow = QWidget()
    #Deleting class
        deleteClass = QPushButton("Delete Class")
    #Adding student
        addStudent = QPushButton("Add Student")
        addStudent.clicked.connect(self.addNewStudent)
    #Sorting the class
        sortClass = QComboBox()
        sortClass.addItems(["Sort Class", "First Name", "Last Name", "Grade"])
    #Base layouts
        primaryLayout = QVBoxLayout()
        secondaryLayout = QHBoxLayout()
        tertiaryLayout = QHBoxLayout()
        quartinaryLayout = QVBoxLayout()
        self.stacklayout = QStackedLayout()
    #Adding widgets to layout
        secondaryLayout.addWidget(classCode)
        secondaryLayout.addWidget(classAverage)
        secondaryLayout.addWidget(exitButton)
        tertiaryLayout.addWidget(tableWidget)
        quartinaryLayout.addWidget(sortClass)
        quartinaryLayout.addWidget(addStudent)
        quartinaryLayout.addWidget(deleteClass)
    #Nesting layouts
        tertiaryLayout.addLayout(quartinaryLayout)
        primaryLayout.addLayout(secondaryLayout)
        primaryLayout.addLayout(tertiaryLayout)
    #Setting up the back and forth between home screen and class view
        classWindow.setLayout(primaryLayout)
        self.stacklayout.addWidget(homeWindow)
        self.stacklayout.addWidget(classWindow)
    #Adding delete buttons
        tableWidget.setCellWidget(0, 0, deleteButton)
    #Adding View Buttons
        tableWidget.setCellWidget(0, 1, viewButton)
    #adding student number
        tableWidget.setItem(0, 2, studentNumber)
    #Adding student first name
        tableWidget.setItem(0, 3, studentFirstName)
    #Adding student last name
        tableWidget.setItem(0, 4, studentLastName)
    #Adding student average
        tableWidget.setItem(0, 5, studentGrade)
    #Resizing the table around contents
        tableWidget.resizeColumnToContents(2)
        tableWidget.resizeColumnToContents(3)
        tableWidget.resizeColumnToContents(4)
        tableWidget.resizeColumnToContents(5)
    #Making the student view pop-up appear
        viewButton.clicked.connect(self.studentWindow)

    #Home Screen Stuff
        homeWindowLayout = QVBoxLayout()
        mainTitle = QLabel("Temporary Title")
    #Add Class Button
        addClass = QPushButton("New Class")
    #Setting up drop down of classes
        classList = QComboBox()
        classList.addItems(["No Selection", "First", "Second", "Third"])
    #Adding Widgets to the screen
        homeWindowLayout.addWidget(mainTitle)
        homeWindowLayout.addWidget(classList)
        homeWindowLayout.addWidget(addClass)
        homeWindow.setLayout(homeWindowLayout)
    #Calling the class selection method
        classList.currentTextChanged.connect(self.classSelection)
    
    #Returning to the home screen
        exitButton.clicked.connect(self.returnToHome)
    
    #A widget must exist to create the window
        widget = QWidget()
        widget.setLayout(self.stacklayout)
    #Declaring it as the main widget
        self.setCentralWidget(widget)
#Using the Class Selection
    def classSelection(self, i):
        print(i)
        self.stacklayout.setCurrentIndex(1)
#Showing the student view
    def studentWindow(self, checked):
        self.w2 = studentView()
        self.w2.show()
#Showing new student window
    def addNewStudent(self, checked):
        self.w4 = addingStudent()
        self.w4.show()
#Returning to the main screen
    def returnToHome(self):
        self.stacklayout.setCurrentIndex(0)
#Going to class view screen
    def classView(self):
        self.stacklayout.setCurrentIndex(0)

#Student view window
class studentView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student View")
    #Table for the assignments
        assignmentTable = QTableWidget(10, 3)
    #Chosen student display
        studentSubject = QLabel("Student: " + "Temp Student Name")
    #Student's grade
        subjectGrade = QLabel("Grade:" + " 50%")
    #New assignment
        addAssignment = QPushButton("Add Assignment")
        addAssignment.clicked.connect(self.openNewAssignment)
    #Delete assignment
        deleteAssignment = QPushButton("Delete")
        assignmentTable.setCellWidget(0, 0, deleteAssignment)
    #Assignment name
        assignmentName = QTableWidgetItem("Group Project")
        assignmentTable.setItem(0, 1, assignmentName)
    #Grade achieved
        gradeAchieved = QTableWidgetItem("110" + "%")
        assignmentTable.setItem(0, 2, gradeAchieved)
    #Layout of window
        halfLayout = QVBoxLayout()
        topLayout = QHBoxLayout()
        bottomLayout = QHBoxLayout()
    #Adding widgets to layouts
        topLayout.addWidget(studentSubject)
        topLayout.addWidget(subjectGrade)
        bottomLayout.addWidget(assignmentTable)
        bottomLayout.addWidget(addAssignment)
    #Nesting layouts
        halfLayout.addLayout(topLayout)
        halfLayout.addLayout(bottomLayout)
        self.setLayout(halfLayout)
    #Resizing columns
        assignmentTable.resizeColumnToContents(1)
        assignmentTable.resizeColumnToContents(2)
#Opening new assignment window
    def openNewAssignment(self, checked):
        self.w3 = addingAssignment()
        self.w3.show()

#Window for adding an assignment to a student
class addingAssignment(QWidget):
    def __init__(self):
        super().__init__()
    #Window title
        self.setWindowTitle("New Assignment For Selected Student")
    #widgets for window
        assignmentName = QLineEdit()
        gradeAchieved = QLineEdit()
    #Instructional text
        assignmentName.setPlaceholderText("Assignment Name")
        gradeAchieved.setPlaceholderText("Grade Achieved")
    #Layout
        assignmentWindowLayout = QVBoxLayout()
        assignmentWindowLayout.addWidget(assignmentName)
        assignmentWindowLayout.addWidget(gradeAchieved)
        self.setLayout(assignmentWindowLayout)

#Window for adding a student
class addingStudent(QWidget):
    def __init__(self):
        super().__init__()
    #Window title
        self.setWindowTitle("New Student")
    #Widgets for the window
        studentNumber = QLineEdit()
        studentFirstName = QLineEdit()
        studentLastName = QLineEdit()
    #Instructional text
        studentNumber.setPlaceholderText("Student Number")
        studentFirstName.setPlaceholderText("Student First Name")
        studentLastName.setPlaceholderText("Student Last Name")
    #Layout
        studentWindowLayout = QVBoxLayout()
        studentWindowLayout.addWidget(studentNumber)
        studentWindowLayout.addWidget(studentFirstName)
        studentWindowLayout.addWidget(studentLastName)
        self.setLayout(studentWindowLayout)

#Windows are hidden by default and must be told to show up
w = MainWindow()
w.show()
#Continuously running the window
app.exec()