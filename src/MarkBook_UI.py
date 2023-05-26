from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QTableView, QTableWidget
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
        tableWidget = QTableWidget(12, 3)
        #Return to class selection
        exitButton = QPushButton("Return to class selection")
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
        #A widget must exist to create the window
        widget = QWidget()
        #Adding layout to the widget
        widget.setLayout(primaryLayout)
        #Declaring it as the main widget
        self.setCentralWidget(widget)

#Windows are hidden by default and must be told to show up
w = MainWindow()
w.show()
#Continuously running the window
app.exec()