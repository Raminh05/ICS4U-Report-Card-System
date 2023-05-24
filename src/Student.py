from Course import Course
from JsonTools.JsonTools import *

class Student(Course):
    def __init__(self, course_code: str, course_name: str, firstname: str, lastname: str, student_id: int, mark: int, assignments: dict) -> None:
        super().__init__(course_code, course_name)
        self.firstname = firstname
        self.lastname = lastname
        self.student_id = student_id
        self.mark = mark
        self.assignments = assignments

        master_dict = load_data()

        master_dict[course_code.upper()][f'{self.firstname} {self.lastname}']

    
        
    



    
    