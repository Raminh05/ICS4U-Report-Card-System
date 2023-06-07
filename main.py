from src.Prompts import *
from src.Views import *
import src.Sorts
from src.Course import Course
from src.People import Teacher

def main():
	""" Main program event """
	clearConsole()
	selected_class = class_selection()

	# If entered in course code does not exist in the database (code 1)
	if selected_class[0] == 1:
		if make_new_class():
			course_name = input("What is the name of the course? ")
			teacher_first_name = input("What is the first name of the teacher? ")
			teacher_last_name = input("What is the last name of the teacher? ")
			confirmed_class = Course(selected_class[1], course_name, Teacher(teacher_first_name, teacher_last_name), []) # Makes new course object
		else:
			main()

	# If the course code does exist (code 0), confirmed_class IS the class object straight from the dictionary
	else:
		confirmed_class = selected_class[1]

	course_table(confirmed_class)

	if confirmed_class.class_view_action_list() == "4":
		confirmed_class.write_to_json()
		main()
	
if __name__ == "__main__":
	main()
