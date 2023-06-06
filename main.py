from src.JsonTools import load_data
from src.DecryptJson import decrypt_json
from src.Prompts import *
from src.Views import *
import src.Sorts

master_dict = decrypt_json(load_data())
clearConsole()

def main():
	selected_class = class_selection(master_dict)
	course_table(selected_class)
	print(selected_class)
	
if __name__ == "__main__":
	main()
