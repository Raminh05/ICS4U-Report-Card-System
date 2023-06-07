from src.People import Teacher, Student
from statistics import mean
from src.JsonTools import *
from InquirerPy import inquirer
from InquirerPy.validator import EmptyInputValidator
from src.Views import individual_student_table, course_table

# -- Class to store course data -- #
class Course():
	def __init__(self, course_code: str, course_name: str, teacher: Teacher, students: list):
		"""Constructor for the Course class

		Args:
			course_code (str): The identification code of the course
			course_name (str): The string literal name of the course
			teacher (Teacher): The teacher of the course represented by a Teacher object
			students (list): A list of student objects that attend the course
		"""
		self.course_code = course_code.upper()
		self.course_name = course_name
		self.teacher = teacher
		self.average = None
		self.students = students
		self.class_average()

	def __repr__(self):
		""" Provides a string representation of a course object"""
		return f'Course({self.course_code}, {self.course_name}, {self.teacher}, {self.students})'

	# I tried to convert the entirety of the course class into a dictionary (so that I can write it into the json) :skull: (POTENTIALLY CLEAN THIS UP WITH Object.__DICT__)
	def write_to_json(self) -> None:
		# Before writing class to json, update class average
		self.class_average() 
		master_dict = load_data()
		course_dict = master_dict[self.course_code] = {}
		course_dict["Course name"] = self.course_name
		course_dict["Teacher"] = f'{self.teacher}'
		course_dict["Class average"] = self.average
		students_dict = course_dict["Students"] = {}
		
		# Goes through all the student objects in the Course.students and turns them into sub-dictionaries for the json
		for student in self.students:
			student_dict = students_dict[f"{student.firstname} {student.lastname}"] = {}
			student_dict["First name"] = student.firstname
			student_dict["Last name"] = student.lastname
			student_dict["Student ID"] = student.id
			student_dict["Mark"] = student.mark
			student_dict["Student marks"] = student.assignments

		write_data(master_dict)

	def remove_from_json(self) -> None:
		"""Remove course from json database"""
		master_dict = load_data()
		del master_dict[self.course_code]
		write_data(master_dict)
	
	def add_student(self) -> None:
		"""Add new student object to student list (Course.students) of the course"""
		firstname = inquirer.text(message = "Enter Student's First Name: ").execute()
		lastname = inquirer.text(message = "Enter Student's Last Name: ").execute()
		id = int(inquirer.text(message = "Enter Student's ID: ").execute())
		self.students.append(Student(firstname, lastname, id, {}))
	
	def view_edit_student(self) -> None:
		"""Calls out the student information table to be rendered and provides action list for student view"""
		index = inquirer.number(
			message = "What student do you want to view/edit? (Enter in student's index in the table): ",
			min_allowed = 0,
			max_allowed = len(self.students) - 1,
			validate = EmptyInputValidator(),
		).execute()

		selected_student = self.students[int(index)]
		individual_student_table(selected_student) # Renders table to display individual student information

		action = inquirer.select(
		message="Select an action:",
		choices=[
			"Add Assignment",
			"Remove Assignment",
			"Edit Assignment Mark",
			"Edit Student Info",
			"Return to Class View",
		],
		default=None,
	).execute()

		# Return "5" is the status code for this match case to return to the class selection view, code 5 is passed into the class_list_action_view to trigger code 4 from there (yes the code is stupid but hey it works)
		match action:
			case "Add Assignment":
				assignment_name = inquirer.text(message = "Enter in assignment name: ").execute()
				assignment_mark = int(inquirer.text(message = "Enter in assignment mark: ").execute())
				selected_student.add_assignment(assignment_name, assignment_mark)
				
			case "Edit Student Info":
				firstname = inquirer.text(message = "Enter Student's First Name: ").execute()
				lastname = inquirer.text(message = "Enter Student's Last Name: ").execute()
				id = int(inquirer.text(message = "Enter Student's ID: ").execute())

				selected_student.firstname = firstname
				selected_student.lastname = lastname
				selected_student.id = id

			case "Return to Class View":
				course_table(self)
				self.class_view_action_list()

			case _:
				selectables = {}
				for key in list(selected_student.assignments.keys()):
					selectables[key] = None

				assignment_name = inquirer.text(
					message = "Which assignment?",
					completer = selectables,
					multicolumn_complete = True,
				).execute()

				if action == "Remove Assignment":
					selected_student.remove_assignment(assignment_name)
					
				elif action == "Edit Assignment Mark":
					selected_student.assignments[assignment_name] = int(input(f"Enter in the new mark for {assignment_name}: "))
					selected_student.average()
				
		individual_student_table(selected_student)
		
	def class_view_action_list(self):
		"""Action list for the student information view"""
		action = inquirer.select(
        message="Select an action:",
        choices=[
            "Add New Student",
            "View/Edit Student",
            "Sort Student Data",
	    	"Delete Student From Class",
		    "Add an Assignment to all Students in Class",
		    "Return to Class Selection",
		    "Manually Save to Database",
            "Exit",
        ],
        default=None,
    ).execute()
		
		# Return "4" is a status code that tells the program to go back to class selection view
		match action:
			case "Add New Student":
				self.add_student()
			case "View/Edit Student":
				self.view_edit_student()
				self.write_to_json()
			case "Sort Student Data":
				sorts = inquirer.select(
					message="Select an action:",
					choices=[
						"Sort by first name (A-Z)",
						"Sort by first name (Z-A)",
						"Sort by last name (A-Z)",
						"Sort by last name (Z-A)",
						"Sort by course average (descending)",
						"Sort by course average (ascending)",
					],
					default=None,
				).execute()
				match sorts:
					case "Sort by first name (A-Z)":
						self.firstname_sort(reverse_sort = False)
					case "Sort by first name (Z-A)":
						self.firstname_sort(reverse_sort = True)
					case "Sort by last name (A-Z)":
						self.lastname_sort(reverse_sort = False)
					case "Sort by last name (Z-A)":
						self.lastname_sort(reverse_sort = True)
					case "Sort by course average (ascending)":
						self.mark_sort(reverse_sort = False)
					case "Sort by course average (descending)":
						self.mark_sort(reverse_sort = True)
			case "Delete Student From Class":
				self.remove_student()
			case "Add an Assignment to all Students in Class":
				self.add_assignment()
			case "Return to Class Selection":
				return "4"
			case "Manually Save to Database":
				self.write_to_json()
			case "Exit":
				self.write_to_json()
				quit()
		
		course_table(self)
		self.class_view_action_list()
			
	def remove_student(self) -> None:
		"""Removes student object from the course object"""
		index = inquirer.number(
			message = "What student do you want to remove? (Enter in student's index in the table): ",
			min_allowed = 0,
			max_allowed = len(self.students) - 1,
			validate = EmptyInputValidator(),
		).execute(0)

		self.students.remove(self.students[int(index)])
		
	# Add an assignment to ALL students' assignment dictionary
	def add_assignment(self) -> None:
		assignment_name = inquirer.text(message = "What is the name of the new assignment?").execute()
		for student in self.students:
			student.assignments[assignment_name] = 0
			student.average()
	
	# Remove an assignment from ALL students' assignment dictionary
	def remove_assignment(self, assignment_name: str) -> None:
		for student in self.students:
			del student.assignments[assignment_name]
			student.average()
	
	# Fetches selected student object
	def student_list_prompt(self) -> Student:
		for count, student in enumerate(self.students):
			print(f"{count}. {student.firstname} {student.lastname}")
			
		index = inquirer.number(
			message="Which student do you want to select? (Enter in student's displayed list number)",
			min_allowed = 0,
			max_allowed = len(self.students) - 1,
			validate = EmptyInputValidator(),
		).execute()

		return self.students[int(index)]
	
	# Calculate class average
	def class_average(self) -> None:
		sum = 0
		if len(self.students) > 0:
			for student in self.students:
				sum += student.mark
			self.average = round(sum / len(self.students), 1)
		else:
			self.average = 0
	
	def mark_sort(self, reverse_sort):
		self.students.sort(key=lambda student: student.mark, reverse = reverse_sort)
	
	def firstname_sort(self, reverse_sort):
		self.students.sort(key=lambda student: student.firstname, reverse = reverse_sort)
	
	def lastname_sort(self, reverse_sort):
		self.students.sort(key=lambda student: student.lastname, reverse = reverse_sort)