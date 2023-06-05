import json, os

# master_dict is main file with all nested information
# it is the one being written to a json when report card is saved
# currently all file paths assume json_utils.py in same folder as student_file.json

# Making sure that the path to the data folder works on all OSes by using os module to assemble paths

if os.name == "nt":
	joined_database_path = "\\data\\student_file.json"
else:
	joined_database_path = "/data/student_file.json"

def load_data() -> dict:
	""" Reading all data from the json database and packaging it into a python-readable dictionary """
	with open(f"{os.getcwd()}{joined_database_path}", "r") as infile:
		master_dict = json.load(infile)
		infile.close()
	return master_dict
	
def write_data(master_dict: dict) -> None:
	""" Writing the master dictionary containing all classes and students into the json database """
	json_dict = json.dumps(master_dict, indent = 4)
	try:
		with open(f"{os.getcwd()}{joined_database_path}", "w") as outfile:
			outfile.write(json_dict)
			outfile.close()
	except OSError:
		print("File not found!")
	
