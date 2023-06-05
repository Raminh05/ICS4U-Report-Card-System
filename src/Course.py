from src.People import Teacher, Student
from statistics import mean, median
from src.JsonTools import write_data, load_data
from InquirerPy import inquirer
from InquirerPy.validator import EmptyInputValidator

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
	
	def class_view_action_list(self):
		print("1. Add New Student\n2. View/Edit Student\n3. Delete Student From Class")

		selected_action = inquirer.number(
				message="What action do you want to do? (Enter in student's displayed list number)",
				min_allowed = 1,
				max_allowed = 3,
				validate = EmptyInputValidator(),
			).execute()
		
		match selected_action:
			case "1":
				self.add_student()
			case "2":
				pass
			case "3":
				pass
	
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

			
		
		