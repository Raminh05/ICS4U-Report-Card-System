import texttable, platform, os
from src.Prompts import *

# Generic function to clear output console before running
def clearConsole() -> None: 
    osType = platform.system()
    if osType == "Darwin" or osType == "Linux":
        os.system("clear")
    elif osType == "Windows":
        os.system("cls")

# Renders the view to display all information about a specific course
def course_table(selected_course) -> None:
	clearConsole()
	print("Course name: "+selected_course.course_name+"\nCourse Code: "+selected_course.course_code+"\nTeacher: "+str(selected_course.teacher)+"\nCourse average: "+str(selected_course.average)+"%")
	table = texttable.Texttable()
	table.set_cols_dtype(["t", "t", "t", "t", "t"])
	table.set_cols_align(["c", "c", "c", "c", "c"])
	table.set_cols_valign(["m", "m", "m", "m", "m"])
	table.header(["", "Student ID", "First name", "Last name", "Student average"])
	for count, student in enumerate(selected_course.students):
		table.add_row([count, student.id, student.firstname, student.lastname, f"{student.mark}%"])
	print(table.draw())

# Renders the view to display all information about a specific student
def individual_student_table(student) -> None:
	clearConsole()
	print("Student Name: " + student.firstname + " " + student.lastname + "\n" + "Student Average: " + str(student.mark) + "%")
	table = texttable.Texttable()
	table.set_cols_dtype(["t", "t"])
	table.set_cols_align(["c", "c"])
	table.set_cols_valign(["m", "m"])
	table.header(["Assignment", "Mark"])
	assignments = student.assignments
	for key in list(assignments.keys()):
		table.add_row([key, str(assignments[key]) + "%"])
	print(table.draw())
