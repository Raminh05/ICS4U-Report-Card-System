"""
master_dict dictionary contains all information imported from JSON
selected_student will be a string containing first and last name of student selected in UI
selected_course will be a string containing course code of course selected in UI

Dictionary is nested as such: master_dict will contain multiple dictionaries for each course (named by their course code) which can be dynamically added through UI
Each course dictionary will have x number of individual student dictionaries (named by their first and last name) which can also be dynamically added through UI
Each student dictionary will contain misc student info (first/last name, Grade, etc) as well as another dictionary with all their assignments and respective marks (can be dynamically added through UI)

This file contains various sort methods for:
	- Sorting by first or last name alphabetically
	- Sorting by all students' average class mark
	- Sorting individual student's assignment marks
"""

selected_course = "ENG4U"
selected_student = "Kelvin Hall"

master_dict = {
	"ICS4U1": {
		"Kelvin Hall": {
			"Student ID": 362981425,
			"First name": "Kelvin",
			"Last name": "Hall",
			"Grade": 12,
			"Student marks": {
				"first_assignment": 97,
				"second_assignment": 91
			}
		},
		"Minh Nguyen": {
			"Student ID": 363084575,
			"First name": "Minh",
			"Last name": "Nguyen",
			"Grade": 12,
			"Student marks": {
				"first_assignment": 78,
				"second_assignment": 81
			}
		},
		"Nathan Hellems": {
			"Student ID": 339354771,
			"First name": "Nathan",
			"Last name": "Hellems",
			"Grade": 12,
			"Student marks": {
				"first_assignment": 88,
				"second_assignment": 90
			}
		}
	},
	"ENG4U": {
		"Kelvin Hall": {
			"Student ID": 362981425,
			"First name": "Kelvin",
			"Last name": "Hall",
			"Grade": 12,
			"Student marks": {
				"first_assignment": 107,
				"second_assignment": 102
			}
		},
		"Minh Nguyen": {
			"Student ID": 363084575,
			"First name": "Minh",
			"Last name": "Nguyen",
			"Grade": 12,
			"Student marks": {
				"first_assignment": 68,
				"second_assignment": 73
			}
		},
		"Nathan Hellems": {
			"Student ID": 339354771,
			"First name": "Nathan",
			"Last name": "Hellems",
			"Grade": 12,
			"Student marks": {
				"first_assignment": 93,
				"second_assignment": 79
			}
		}
	}
}

print(sorted(master_dict[selected_course][selected_student]["Student marks"].items(), key = lambda x: x[1])) # Sorts selected student's marks in ascending order

print(sorted(master_dict[selected_course][selected_student]["Student marks"].items(), key = lambda x: x[1], reverse = True)) # Sorts selected student's marks in descending order

print(sorted(master_dict[selected_course].items(), key = lambda x: x[1])) # Sorts selected course's students in alphabetically ascending order
