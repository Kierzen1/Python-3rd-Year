"""
	Student API(application program interface)
"""
from Student import * #import all properties from Student file
from os import system

slist:list = []
filename:str = "student.csv" #comma-separated-variables

def header(message:str)->None:
	system("cls")
	print(message)
	print("---------------------")


	
def checkid(student:Student)->bool:pass
	#######
	
def addStudent()->None:
	header("Add Student")
	idno:str = input("Enter IDNO :")
	lastname:str = input("Enter LASTNAME :")
	firstname:str = input("Enter FIRSTNAME :")
	course:str = input("Enter COURSE :")
	level:str = input("Enter LEVEL :")
	#call checkid for duplicate student entry
	student = Student(idno,lastname,firstname,course,level)
	f = open(filename,"a") 
	f.write(student.__str__())
	f.write("\n")
	f.close()
	print()
	print("New Student Added")
	
	
	
def findStudent()->None: pass
def deleteStudent()->None: pass
def updateStudent()->None: pass
def displayAllStudent()->None:
	header("Display All Student")
	#must check if file to be opened is existing
	f = open(filename)
	slist = f.readlines()
	f.close()
	for s in slist:
		print(s,end="")
	print("---------------------------")
	print("Nothing follows")
	
def quit()->None:
	header("Program Terminated")
	

