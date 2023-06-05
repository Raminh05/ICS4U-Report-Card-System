from InquirerPy import inquirer
from InquirerPy.validator import EmptyInputValidator

def class_selection(master_dict):
	selectables = {}
	for key in list(master_dict.keys()):
		selectables[key] = None
	
	selected_class = inquirer.text(
		message="What class do you want to open?",
		completer=selectables,
		multicolumn_complete=True,
	).execute()

	return master_dict[selected_class]
	
	





	
