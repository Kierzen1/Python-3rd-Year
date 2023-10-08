"""
	Student class
"""
class Person(object):
	def __init__(self,lastname,firstname):
		self.lastname = lastname
		self.firstname = firstname
	def __str__(self)->str:
		return f"{self.lastname},{self.firstname}"
##############################
class Student(Person):
	def __init__(self,idno,lastname,firstname,course,level):
		super().__init__(lastname,firstname)
		self.idno = idno
		self.course = course
		self.level = level
	
	def __eq__(self,other)->bool:
		if self is other: return True
		if type(self) != type(other): return False
		if self.idno == other.idno: return True
		else: return False
		
	def __str__(self)->str:
		return f"{self.idno},{super().__str__()},{self.course},{self.level}"
	
	
	
	
	