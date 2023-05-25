from Course import Course
import JsonTools
import time

## -- Student subclass inherit course details from course class -- ##
class Student(Course):
    def __init__(self, course_code: str, course_name: str, firstname: str, lastname: str, student_id: int, mark: int, assignments: dict) -> None:
        super().__init__(course_code, course_name)
        self.firstname = firstname
        self.lastname = lastname
        self.student_id = student_id
        self.mark = mark
        self.assignments = assignments

        # Read json data into a master dictionary
        master_dict = JsonTools.load_data()

        # If student's course does not exist yet, add course to json
        if course_code.upper() not in master_dict:
            master_dict[course_code.upper()] = {}

        # Add student to master dictionary as part of the constructor
        master_dict[course_code.upper()][f'{self.firstname} {self.lastname}'] = {
            "first_name": self.firstname,
            "last_name": self.lastname,
            "id": self.student_id,
            "mark": self.mark,
            "assignments": self.assignments
        }

        JsonTools.write_data(master_dict) # Leave it to the garbage collector to delete master_dict after the constructor is done
    
    # Method to represent the student object as a string
    def __str__(self) -> str:
        return f'{self.firstname} {self.lastname} has a {self.mark}% in {self.course_name}.'
    
    # Method to remove students from json datbase
    def remove(self) -> None:
        master_dict = JsonTools.load_data()
    
        if f'{self.firstname} {self.lastname}' in master_dict[self.course_code.upper()]:
            del master_dict[self.course_code.upper()][f'{self.firstname} {self.lastname}']
        else:
            print("Student and/or course does not exist in json!")
        
        JsonTools.write_data(master_dict)
    
        
    



    
    