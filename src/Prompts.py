from InquirerPy import inquirer
from src.JsonTools import load_data
from src.DecryptJson import decrypt_json

# If code 1 is returned because the course does not yet exist in the database, prompt user to make new course in main.py 
def class_selection() -> tuple:
	"""Prompt to select which class you want to access"""
	master_dict = decrypt_json(load_data())
	selectables = {}
	for key in list(master_dict.keys()):
		selectables[key] = None
	
	selected_class = inquirer.text(
		message="What class do you want to open?",
		completer=selectables,
		multicolumn_complete=True,
	).execute()

	if selected_class in master_dict:
		return 0, master_dict[selected_class]
	else:
		return 1, selected_class

# A function to prompt the user if they want to make a new class
def make_new_class() -> bool:
	selection = inquirer.confirm(message="You have entered in a non-existent class! Would you like to make a new one?", default=True).execute()
	return selection