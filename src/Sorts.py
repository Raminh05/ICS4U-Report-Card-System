def mark_sort(reverse_sort):
	master_dict["ICS4U"].students.sort(key=lambda student: student.mark, reverse = reverse_sort)

def firstname_sort():
	master_dict["ICS4U"].students.sort(key=lambda student: student.firstname, reverse = reverse_sort)

def lastname_sort():
	master_dict["ICS4U"].students.sort(key=lambda student: student.firstname, reverse = reverse_sort)

# def marks_sort(selected_student):
# 	master_dict["ICS4U"].students[selected_student].assignments.values().sort(key=lambda student: student.lastname, reverse = reverse_sort)
