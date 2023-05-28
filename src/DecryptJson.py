from Course import Course
from People import *

# Decrypt json deserialzied output back into Course, Teacher, and Student objects	
def decrypt_json(master_dict: dict) -> list:
	data = {}
	# Piss poor nested for loop that will break your computer if there are more than 3 courses with 30 students each
	for course in list(master_dict.keys()):
		student_list = []
		for student in list(master_dict[course]["Students"].values()):
			student_list.append(Student(student["First name"], student["Last name"], student["Student ID"], student["Student marks"]))

		data[course] = (Course(course, master_dict[course]["Course name"], Teacher(master_dict[course]["Teacher"].split()[0], master_dict[course]["Teacher"].split()[1]), student_list))

	return data