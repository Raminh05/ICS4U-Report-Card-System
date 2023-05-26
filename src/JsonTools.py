import json
# master_dict is main file with all nested information
# it is the one being written to a json when report card is saved
# currently all file paths assume json_utils.py in same folder as student_file.json

def write_data(master_dict) -> None:
	""" Writing the master dictionary containing all classes and students into the json database """
	json_dict = json.dumps(master_dict, indent = 4)
	with open("data//student_file.json", "w") as outfile:
		outfile.write(json_dict)
		outfile.close()

def load_data() -> dict:
	""" Reading all data from the json database and packaging it into a python-readable dictionary """
	with open("data//student_file.json", "r") as infile:
		master_dict = json.load(infile)
		infile.close()
	return master_dict