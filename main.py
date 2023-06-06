from src.JsonTools import load_data
from src.DecryptJson import decrypt_json
from src.Prompts import *
from src.Views import *
import src.Sorts

def main():
	clearConsole()
	master_dict = decrypt_json(load_data())
	selected_class = class_selection(master_dict)
	course_table(selected_class)

	if selected_class.class_view_action_list() == "4":
		main()

if __name__ == "__main__":
	main()
