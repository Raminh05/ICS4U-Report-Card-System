def mark_sort(reverse_sort):
	master_dict["ICS4U"].students = sorted(master_dict["ICS4U"].students, key=lambda student: student.mark, reverse = reverse_sort)
	selected_class = class_selection(master_dict)

def firstname_sort():
	master_dict["ICS4U"].students = sorted(master_dict["ICS4U"].students, key=lambda student: student.firstname, reverse = reverse_sort)
	selected_class = class_selection(master_dict)

def lastname_sort():
	master_dict["ICS4U"].students = sorted(master_dict["ICS4U"].students, key=lambda student: student.lastname, reverse = reverse_sort)
	selected_class = class_selection(master_dict)
