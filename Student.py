# -- Class to store student data -- #
class Course():
    def __init__(self, course_code: str, course_name: str):
        self.course_code = course_code
        self.course_name = course_name

class Student(Person):
    def __init__(self, course_code: str, course_name: str, firstname: str, lastname: str, student_id: int, mark: int, assignments: dict) -> None:
        super().__init__(course_code, course_name)
        self.firstname = firstname
        self.lastname = lastname
        self.student_id = student_id
        self.mark = mark
        self.assignments = assignments
    
    # Temp method to represent the characteristics of a student object
    def __str__(self):
        return f'{self.firstname} {self.lastname} with student ID {self.student_id} currently has a {self.mark} in the course.'
    
    # call json methods here








