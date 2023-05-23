# -- Class to store student data -- #
class Person():
    def __init__(self, firstname: str, lastname: str):
        self.firstname = firstname
        self.lastname = lastname

class Student(Person):
    def __init__(self, student_id: int, course: str, grade: int, assignments: dict) -> None:
        super().__init__()
        self.student_id = student_id
        self.firstname = firstname
        self.surname = surname
        self.course = course
        self.grade = grade
        self.assignments = assignments


        # json stuff here

