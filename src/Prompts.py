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

def class_view_action_list():
	print("1. Add New Student\n 2. View/Edit Student\n 3. Delete Student From Class")

	selected_action = inquirer.number(
			message="Which student do you want to select? (Enter in student's displayed list number)",
			min_allowed = 1,
			max_allowed = 3,
			validate = EmptyInputValidator(),
		).execute()

	match selected_action:
		case 1:
			pass
		case 2:
			pass
		case 3:
			pass
	
	





	
