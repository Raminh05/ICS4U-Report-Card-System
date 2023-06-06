from src.People import Teacher, Student
from statistics import mean, median
from src.JsonTools import write_data, load_data
from InquirerPy import inquirer
from InquirerPy.validator import EmptyInputValidator
from src.Views import individual_student_table

# -- Class to store course data -- #
class Course():
	def __init__(self, course_code: str, course_name: str, teacher: Teacher, students: list):
		self.course_code = course_code.upper()
		self.course_name = course_name
		self.teacher = teacher
		self.average = None
		self.students = students

	def __repr__(self):
		return f'Course({self.course_code}, {self.course_name}, {self.teacher}, {self.students})'

	# I tried to convert the entirety of the course class into a dictionary :skull:
	def write_to_json(self) -> None:
		master_dict = load_data()
		course_dict = master_dict[self.course_code] = {}
		course_dict["Course name"] = self.course_name
		course_dict["Teacher"] = f'{self.teacher}'
		course_dict["Class average"] = self.average
		students_dict = course_dict["Students"] = {}

		for student in self.students:
			student_dict = students_dict[f"{student.firstname} {student.lastname}"] = {}
			student_dict["First name"] = student.firstname
			student_dict["Last name"] = student.lastname
			student_dict["Student ID"] = student.id
			student_dict["Mark"] = student.mark
			student_dict["Student marks"] = student.assignments

		write_data(master_dict)
	
	def remove_from_json(self) -> None:
		master_dict = load_data()
		del master_dict[self.course_code]
		write_data(master_dict)
	
	def add_student(self) -> None:
		firstname = input("Enter Student's First Name: ")
		lastname = input("Enter Student's Last Name: ")
		id = int(input("Enter Student's ID: "))
		self.students.append(Student(firstname, lastname, id, {}))
	
	def view_edit_student(self) -> None:
		index = int(input("What student do you want to view/edit? (Enter in student's index in the table): "))
		selected_student = self.students[index]
		individual_student_table(selected_student)

		print("1. Add Assignment\n2. Remove Assignment\n3. Edit assignment\n4. Edit student info\n5. Return to class view")
		selected_action = inquirer.number(
			message = "What action do you want to do?",
			min_allowed = 1,
			max_allowed = 4,
			validate = EmptyInputValidator()
		).execute()

		match selected_action:
			case "1":
				assignment_name = input("Enter in assignment name: ")
				assignment_mark = int(input("Enter in assignment mark: "))
				selected_student.add_assignment(assignment_name, assignment_mark)
			case "4":
				firstname = input("Enter Student's First Name: ")
				lastname = input("Enter Student's Last Name: ")
				id = int(input("Enter Student's ID: "))

				selected_student.firstname = firstname
				selected_student.lastname = lastname
				selected_student.id = id
			case _:
				selectables = {}
				for key in list(selected_student.assignments.keys()):
					selectables[key] = None

				assignment_name = inquirer.text(
					message = "Which assignment?",
					completer = selectables,
					multicolumn_complete = True,
				).execute()

				if selected_action == "2":
					selected_student.remove_assignment(assignment_name)
				elif selected_action == "3":
					selected_student.assignments[assignment_name] = int(input(f"Enter in the new mark for {assignment_name}: "))
	
	def remove_student(self) -> None:
		index = int(input("What student do you want to remove? (Enter in student's index in the table): "))
		self.students.remove(self.students[index])

	# Add an assignment to ALL students' assignment dictionary
	def add_assignment(self, assignment_name: str) -> None:
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
		for student in self.students:
			sum += student.mark
		self.average = round(sum / len(self.students), 1)

			
		
		