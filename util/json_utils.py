import json
# master_dict is main file with all nested information
# it is the one being written to a json when report card is saved
# currently all file paths assume json_utils.py in same folder as student_file.json
def write_data():
	json_dict = json.dumps(master_dict, indent = 4)
	with open("student_file.json", "w") as outfile:
	outfile.write(json_dict)

def load_data():
	with open("student_file.json", "r") as infile:
	master_dict = json.load(infile)
