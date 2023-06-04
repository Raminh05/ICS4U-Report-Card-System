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

def sort_marks(selected_course, selected_student) -> list:
	sorted(master_dict[selected_course]["Students"][selected_student]["Student marks"].items(), key = lambda x: x[1], reverse = sort_reverse) # Sorts selected student's marks

def sort_lname(selected_course) -> list:
	sorted(master_dict[selected_course]["Students"].items(), key = lambda x: getitem(x[1], "Last name"), reverse = sort_reverse) # Sorts selected course's students by last name

def sort_fname(selected_course) -> list:
	sorted(master_dict[selected_course]["Students"].items(), key = lambda x: getitem(x[1], "First name"), reverse = sort_reverse) # Sorts selected course's students by first name
