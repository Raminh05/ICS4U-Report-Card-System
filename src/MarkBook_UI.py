from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QComboBox, QTableWidget, QTableWidgetItem, QStackedLayout
import sys
from People import Student
from JsonTools import load_data
from DecryptJson import decrypt_json

#Allows for command line arguments
app = QApplication(sys.argv)

master_dict = decrypt_json(load_data())

#Class for the main window
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        ## -- WINDOW PARAMETERS -- ##
        #Set the window title
        self.setWindowTitle("Temporary")

        ## -- UI ELEMENTS -- ##
        #Setting up drop down of classes
        classList = QComboBox()
        
        for course in list(master_dict.keys()):
            classList.addItem(f'{course}')

    #Making the Table (HARDCODED)
        tableWidget = QTableWidget(len(master_dict["ICS4U"].students), 6)
    #Return to class selection
        exitButton = QPushButton("Return to class selection")
    
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

    #Adding delete buttons (HARDCODED)
        for count, student in enumerate(master_dict["ICS4U"].students):
            #Delete buttons
            deleteButton = QPushButton("Delete Student")
        #View buttons
            viewButton = QPushButton(f'View Student')
            #Student name
            studentFirstName = QTableWidgetItem(student.firstname)
            studentLastName = QTableWidgetItem(" " + student.lastname + " ")
        #Student number
            studentNumber = QTableWidgetItem(f'{student.id}')
        #Student Grade
            studentGrade = QTableWidgetItem(f'{student.mark}%')

            tableWidget.setCellWidget(count, 0, deleteButton)
        #Adding View Buttons
            tableWidget.setCellWidget(count, 1, viewButton)
        #adding student number
            tableWidget.setItem(count, 2, studentNumber)
        #Adding student first name
            tableWidget.setItem(count, 3, studentFirstName)
        #Adding student last name
            tableWidget.setItem(count, 4, studentLastName)
        #Adding student average
            tableWidget.setItem(count, 5, studentGrade)

        #Resizing the table around contents
            tableWidget.resizeColumnToContents(0)
            tableWidget.resizeColumnToContents(1)
            tableWidget.resizeColumnToContents(2)
            tableWidget.resizeColumnToContents(3)
            tableWidget.resizeColumnToContents(4)
            tableWidget.resizeColumnToContents(5)

            #Making the student view pop-up appear
            viewButton.clicked.connect(lambda student_option, student=student: self.studentWindow(student))


    #Home Screen Stuff
        homeWindowLayout = QVBoxLayout()
        mainTitle = QLabel("Quirky Python Report Card System")
    #Add Class Button
        addClass = QPushButton("New Class")
    
        
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
        print(master_dict[i])
        self.stacklayout.setCurrentIndex(1)
#Showing the student view
    def studentWindow(self, student_object: Student):
        self.w2 = studentView(student_object)
        self.w2.show()
#Showing new student window
    def addNewStudent(self):
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
    def __init__(self, student_object: Student):
        super().__init__()
        self.student_object = student_object
        self.setWindowTitle("Student View")

        print(student_object)

        # Keys (assignment names) pulled from the assignment dictionary
        assignment_keys = list(student_object.assignments.keys())

        #Table for the assignments
        assignmentTable = QTableWidget(len(assignment_keys), 3)

        #Chosen student display
        studentSubject = QLabel(f'Student: {student_object.firstname} {student_object.lastname}')

        #Student's grade
        subjectGrade = QLabel(f'Average: {student_object.mark}%')

        #New assignment
        addAssignment = QPushButton("Add Assignment")
        addAssignment.clicked.connect(self.openNewAssignment)

		for count, assignment in enumerate(assignment_keys):
			#Delete assignment
			deleteAssignment = QPushButton("Delete")
			assignmentTable.setCellWidget(count, 0, deleteAssignment)

			#Assignment name
			assignmentName = QTableWidgetItem(assignment)
			assignmentTable.setItem(count, 1, assignmentName)

			#Grade achieved
			gradeAchieved = QTableWidgetItem(f'{student_object.assignments[assignment]}%')
			assignmentTable.setItem(count, 2, gradeAchieved)

			deleteAssignment.clicked.connect(lambda assignment_options, assignment=assignment: student_object.remove_assignment(assignment))
    
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
