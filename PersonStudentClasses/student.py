"""
	Student Class Structure
	-----------------------
	String idno
	String course
	String level
"""

from os import system
from person import Person

#creating the student class
class Student(Person):
    
    def __init__(self,idno,lastname,firstname,course,level):
    #invoke the parent constructor
        super().__init__(lastname,firstname)
        self.idno = idno
        self.course = course
        self.level = level
    
    def __str__(self)->str:
        return f"{self.idno} {super().__str__()} {self.course} {self.level} "
        
def main()->None:
    s = Student("0001","Booc","Kierzen","BSIT","2")
    print(s)
    
if __name__=="__main__":
    main()