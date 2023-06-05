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

def main():
	clearConsole()
	master_dict = decrypt_json(load_data())
	table = texttable.Texttable()
	table.set_deco(table.HEADER | table.HLINES)
	table.set_cols_dtype(["i", "t", "t", "t"])
	table.set_cols_align(["c", "c", "c", "c"])
	table.set_cols_align(["c", "c", "c", "c"])
	table.header(["Student ID", "First name", "Last name", "Course average"])
	for student in master_dict["ICS4U"].students:
		table.add_row([student.id, student.firstname, student.lastname, student.mark])
	print(table.draw())

if __name__ == "__main__":
	main()
