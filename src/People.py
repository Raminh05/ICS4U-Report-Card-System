from statistics import mean

## -- Person superclass that contains firstname and lastname for all persons (since we all have names) -- ##
class Person():
	def __init__(self, firstname: str, lastname: str) -> None:
		self.firstname = firstname
		self.lastname = lastname
	
## -- Simple sub class for teachers -- ##    
class Teacher(Person):
	def __init__(self, firstname: str, lastname: str) -> None:
		super().__init__(firstname, lastname)
	
	def __repr__(self) -> str:
		return f'{self.firstname} {self.lastname}'

## -- Student subclass inherit first and last names from Person class -- ##
class Student(Person):
	def __init__(self, firstname: str, lastname: str, id: int, assignments: dict) -> None:
		super().__init__(firstname, lastname)
		self.id = id
		self.assignments = assignments
		self.mark = 0 # No mark at initialization
		self.average() # Calculate mark if there are assignments pre-loaded with student object
	   
	# Calculate student's average
	def average(self) -> None:
		if len(self.assignments.values()) == 0:
			self.mark = 0
		else:
			self.mark = round(mean(self.assignments.values()), 1)
	
	# "Local" student implementation of the add assignment function where details such as assignment grades can be adjusted for each student
	def add_assignment(self, assignment_name: str, assignment_mark: int) -> None:
		self.assignments[assignment_name] = assignment_mark
		self.average()
	
	# "Local" student implementation of the remove assignment function where details such as assignment grades can be adjusted for each student
	def remove_assignment(self, assignment_name: str) -> None:
		del self.assignments[assignment_name]
		self.average()

	# Returns a representation of the student object
	def __repr__(self) -> str:
		return f'Student({self.firstname}, {self.lastname}, {self.id}, {self.assignments}, {self.mark})'