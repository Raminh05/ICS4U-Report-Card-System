"""
master_dict dictionary contains all information imported from JSON
selected_student will be a string containing first and last name of student selected in UI
selected_course will be a string containing course code of course selected in UI
sort_reverse will be a boolean switched in the UI to sort data in reverse or not

Dictionary is nested as such: master_dict will contain multiple dictionaries for each course (named by their course code) which can be dynamically added through UI
Each course dictionary will have x number of individual student dictionaries (named by their first and last name) which can also be dynamically added through UI
Each student dictionary will contain misc student info (first/last name, Grade, etc) as well as another dictionary with all their assignments and respective marks (can be dynamically added through UI)

This file contains various sort methods for:
	- Sorting by first or last name alphabetically
	- Sorting by all students' average class mark
	- Sorting individual student's assignment marks
"""
from operator import getitem
from statistics import mean, median

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
				"second_assignment": 102,
				"third_assignment": 69
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

print(sorted(master_dict[selected_course][selected_student]["Student marks"].items(), key = lambda x: x[1], reverse = sort_reverse)) # Sorts selected student's marks

print(sorted(master_dict[selected_course].items(), key = lambda x: getitem(x[1], "Last name"), reverse = sort_reverse)) # Sorts selected course's students by last name

print(sorted(master_dict[selected_course].items(), key = lambda x: getitem(x[1], "First name"), reverse = sort_reverse)) # Sorts selected course's students by first name

print(mean(master_dict[selected_course][selected_student]["Student marks"].values())) # Calculates average mark for selected student

print(median(master_dict[selected_course][selected_student]["Student marks"].values())) # Calculates median mark for selected student
