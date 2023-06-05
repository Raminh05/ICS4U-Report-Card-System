from src.JsonTools import load_data
from src.DecryptJson import decrypt_json
from InquirerPy import inquirer
import texttable, platform, os

def clearConsole(): # Generic function to clear output console before running
    osType = platform.system()
    if osType == "Darwin" or osType == "Linux":
        os.system("clear")
    elif osType == "Windows":
        os.system("cls")

clearConsole()
table = texttable.Texttable()
master_dict = decrypt_json(load_data())
table.set_deco(table.HEADER | table.HLINES | table.VLINES | table.BORDER)

def course_table():
	table.reset()
	table.set_cols_dtype(["t", "t", "t", "t"])
	table.set_cols_align(["c", "c", "c", "c"])
	table.header(["Student ID", "First name", "Last name", "Course average"])
	for student in master_dict["ICS4U"].students: # temporarily hardcoded course code
		table.add_row([student.id, student.firstname, student.lastname, student.mark])
	print(table.draw())

def individual_student_table():
	table.reset()
	table.set_cols_dtype(["t", "t"])
	table.set_cols_align(["c", "c"])
	table.set_cols_valign(["m", "m"])
	table.header(["Assignment name", "Mark"])
	assignments = master_dict["ICS4U"].students[0].assignments
	for key in list(assignments.keys()):
		table.add_row([key, assignments[key]])
	print(table.draw())

def main():
	course_table()
	individual_student_table()

if __name__ == "__main__":
	main()
