from src.JsonTools import load_data
from src.DecryptJson import decrypt_json
from src.Prompts import *
from src.Views import *
from src.Course import Course
import src.Sorts


master_dict = decrypt_json(load_data())
clearConsole()

def main():
	selected_class = class_selection(master_dict)
	course_table(selected_class)
	selected_class.class_view_action_list()
	print(selected_class)

if __name__ == "__main__":
	main()
