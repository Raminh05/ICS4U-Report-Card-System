import texttable, platform, os
from src.Prompts import *

# Generic function to clear output console before running
def clearConsole(): 
    osType = platform.system()
    if osType == "Darwin" or osType == "Linux":
        os.system("clear")
    elif osType == "Windows":
        os.system("cls")

def course_table(selected_course):
	clearConsole()
	print("Course name: "+selected_course.course_name+"\nCourse Code: "+selected_course.course_code+"\nTeacher: "+str(selected_course.teacher)+"\nCourse average: "+str(selected_course.average))
	table = texttable.Texttable()
	table.set_cols_dtype(["t", "t", "t", "t", "t"])
	table.set_cols_align(["c", "c", "c", "c", "c"])
	table.set_cols_valign(["m", "m", "m", "m", "m"])
	table.header(["", "Student ID", "First name", "Last name", "Course average"])
	for count, student in enumerate(selected_course.students):
		table.add_row([count, student.id, student.firstname, student.lastname, student.mark])
	print(table.draw())
	
def individual_student_table(student):
	clearConsole()
	table = texttable.Texttable()
	table.set_cols_dtype(["t", "t"])
	table.set_cols_align(["c", "c"])
	table.set_cols_valign(["m", "m"])
	table.header(["Assignment", "Mark"])
	assignments = student.assignments
	for key in list(assignments.keys()):
		table.add_row([key, assignments[key]])
	print(table.draw())
