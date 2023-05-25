from Course import Course
import JsonTools

class Student(Course):
    def __init__(self, course_code: str, course_name: str, firstname: str, lastname: str, student_id: int, mark: int, assignments: dict) -> None:
        super().__init__(course_code, course_name)
        self.firstname = firstname
        self.lastname = lastname
        self.student_id = student_id
        self.mark = mark
        self.assignments = assignments

        master_dict = JsonTools.load_data()

        if course_code.upper() not in master_dict:
            master_dict[course_code.upper()] = {}

        master_dict[course_code.upper()][f'{self.firstname} {self.lastname}'] = {
            "id": self.student_id,
            "mark": self.mark,
            "assignments": self.assignments
        }

        JsonTools.write_data(master_dict)
    
    def __str__(self):
        return f'{self.firstname} {self.lastname} has a {self.mark}% in {self.course_name}.'

student1 = Student("ICS4U", "Grade 12 CS", "Kelvin", "Hall", 1234567, 98, {"Assignment 1": 98, "Assignment 2": 95})
print(student1)

    
        
    



    
    