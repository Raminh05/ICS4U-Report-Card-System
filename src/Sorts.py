"""
master_dict dictionary contains all information imported from JSON
selected_student will be a string containing first and last name of student selected in UI
selected_course will be a string containing course code of course selected in UI

Dictionary is nested as such: master_dict will contain multiple dictionaries for each course (named by their course code) which can be dynamically added through UI
Each course dictionary will have x number of individual student dictionaries (named by their first and last name) which can also be dynamically added through UI
Each student dictionary will contain misc student info (first/last name, grade, etc) as well as another dictionary with all their assignments and respective marks (can be dynamically added through UI)

This file contains various sort methods for:
	- Sorting by first or last name alphabetically
	- Sorting by all students' average class mark
	- Sorting individual student's assignment marks
"""

master_dict = {
	"ICS4U1": {
		"Kelvin Hall": {
			"first_name": "Kelvin",
			"last_name": "Hall",
			"grade": 12,
			"student_marks": {
				"first_assignment": 97,
				"second_assignment": 91
			}
		},
		"Minh Nguyen": {
			"first_name": "Minh",
			"last_name": "Hall",
			"grade": 12,
			"student_marks": {
				"first_assignment": 78,
				"second_assignment": 81
			}
		},
		"Nathan Hellems": {
			"first_name": "Nathan",
			"last_name": "Hellems",
			"grade": 12,
			"student_marks": {
				"first_assignment": 88,
				"second_assignment": 90
			}
		}
	},
	"ENG4U": {
		"Kelvin Hall": {
			"first_name": "Kelvin",
			"last_name": "Hall",
			"grade": 12,
			"student_marks": {
				"first_assignment": 107,
				"second_assignment": 102
			}
		},
		"Minh Nguyen": {
			"first_name": "Minh",
			"last_name": "Hall",
			"grade": 12,
			"student_marks": {
				"first_assignment": 68,
				"second_assignment": 73
			}
		},
		"Nathan Hellems": {
			"first_name": "Nathan",
			"last_name": "Hellems",
			"grade": 12,
			"student_marks": {
				"first_assignment": 93,
				"second_assignment": 79
			}
		}
	}
}

selected_student = input("Pick student to sort ")

master_list = list(master_dict.items())
sorted_marks = sorted(master_list, key=lambda x: x[1][selected_student]["student_marks"]["first_assignment"])
print(sorted_marks)
