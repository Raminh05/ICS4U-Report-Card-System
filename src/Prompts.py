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

def class_view_action_list(selected_course):
		print("1. Add New Student\n2. View/Edit Student\n3. Delete Student From Class\n4. Return to class selection\n5. Quit Program")

		selected_action = inquirer.number(
				message="What action do you want to do? (Enter in student's displayed list number)",
				min_allowed = 1,
				max_allowed = 5,
				validate = EmptyInputValidator(),
			).execute()
		
		match selected_action:
			case "1":
				selected_course.add_student()
			case "2":
				selected_course.view_edit_student()
			case "3":
				selected_course.remove_student()
			case "4":
				class_selection()
			case "5":
				quit()
	





	
