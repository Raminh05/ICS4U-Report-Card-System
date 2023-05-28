from People import Teacher, Student
from statistics import mean, median
from JsonTools import write_data, load_data

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
	
	# Calculate class average
	def class_average(self) -> None:
		sum = 0
		for student in self.students:
			sum += student.mark
		self.average = round(sum / len(self.students))

			
		
		