from Course import Course
from statistics import mean, median
import JsonTools

## -- Student subclass inherit course details from course class -- ##
class Student(Course):
    def __init__(self, course_code: str, course_name: str, firstname: str, lastname: str, student_id: int, assignments: dict) -> None:
        super().__init__(course_code, course_name)
        self.firstname = firstname
        self.lastname = lastname
        self.student_id = student_id
        self.mark = None # No mark at first initialization
        self.assignments = assignments
        self.add() # Add student to json database upon initialization of the object

    # Add or append student information in json database
    def add(self) -> None:
        # Read json data into a master dictionary
        master_dict = JsonTools.load_data()

        # If student's course does not exist yet, add course to json
        if self.course_code.upper() not in master_dict:
            master_dict[self.course_code.upper()] = {}
            master_dict[self.course_code.upper()]["class_average"] = None
            master_dict[self.course_code.upper()]["students"] = {}

        # Add student to master dictionary as part of the constructor
        master_dict[self.course_code.upper()]["students"][f'{self.firstname} {self.lastname}'] = {
            "first_name": self.firstname,
            "last_name": self.lastname,
            "id": self.student_id,
            "mark": self.mark,
            "assignments": self.assignments
        }

        JsonTools.write_data(master_dict) # Leave it to the garbage collector to delete master_dict after the constructor is done

    # Method to remove students from json datbase
    def remove(self) -> None:
        master_dict = JsonTools.load_data()
    
        if f'{self.firstname} {self.lastname}' in master_dict[self.course_code.upper()]:
            del master_dict[self.course_code.upper()][f'{self.firstname} {self.lastname}']
        else:
            print("Student and/or course does not exist in json!")
        
        JsonTools.write_data(master_dict)
    
    # Add an assignment to student's assignment dictionary (maybe implement weightings here in the future)
    def add_assignment(self, assignment_name: str, assignment_mark: int) -> None:
        self.assignments[assignment_name] = assignment_mark
        self.average()
        
    # Calculate student's average and update class average at the same time
    def average(self) -> None:
        self.mark = round(mean(self.assignments.values()))
        self.add()
        
    # Calcualte student's median
    def median(self) -> int:
        return median(self.assignments.values())
    
    # Method to represent the student object as a string
    def __str__(self) -> str:
        return f'{self.firstname} {self.lastname} has a {self.mark}% in {self.course_name}.'