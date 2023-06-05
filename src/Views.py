import texttable, platform, os
from src.Course import Course

# Generic function to clear output console before running
def clearConsole(): 
    osType = platform.system()
    if osType == "Darwin" or osType == "Linux":
        os.system("clear")
    elif osType == "Windows":
        os.system("cls")

def course_table(selected_course: Course):
	table = texttable.Texttable()
	table.set_cols_dtype(["t", "t", "t", "t", "t"])
	table.set_cols_align(["c", "c", "c", "c", "c"])
	table.set_cols_valign(["m", "m", "m", "m", "m"])
	table.header(["", "Student ID", "First name", "Last name", "Course average"])
	for count, student in enumerate(selected_course.students):
		table.add_row([count, student.id, student.firstname, student.lastname, student.mark])
	print(table.draw())

def individual_student_table():
	table = texttable.Texttable()
	table.set_cols_dtype(["t", "t"])
	table.set_cols_align(["c", "c"])
	table.set_cols_valign(["m", "m"])
	table.header(["Assignment", "Mark"])
	assignments = master_dict["ICS4U"].students[0].assignments
	for key in list(assignments.keys()):
		table.add_row([key, assignments[key]])
	print(table.draw())
