import JsonTools

# Function to calculate class average (PLEASE OPTIMIZE THIS TO HAVE LESS READ/WRITE OPERATIONS)
def class_avg(course_code: str) -> None:
    marksum = 0
    master_dict = JsonTools.load_data()
    student_data_list = list(master_dict[course_code]["students"].values())

    print(student_data_list)

    for student in student_data_list:
        marksum += student["mark"]

    master_dict[course_code]["class_average"] = round(marksum / len(student_data_list))

    JsonTools.write_data(master_dict)

# -- Class to store course data -- #
class Course():
    def __init__(self, course_code: str, course_name: str):
        self.course_code = course_code
        self.course_name = course_name      