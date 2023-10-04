"""
	Student API(application program interface)
"""
from Student import * #import all properties from Student file
from os import system

students:list = []
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
	
	
	
def findStudent()->None:
    system("cls")
    print("Find Student")
    print("----------------")
    id_finder = input("Enter IDNO of the student to find: ")
    system("cls")
    f = open(filename, 'r')
    for line in f:
        student_data = line.strip().split(',')
        idno, lastname, firstname, course, level = student_data
        if idno == id_finder:
            print("Student Found")
            print("----------------")
            print(f"IDNO: {idno}")
            print(f"LASTNAME: {lastname}")
            print(f"FIRSTNAME: {firstname}")
            print(f"COURSE: {course}")
            print(f"LEVEL: {level}")
            f.close()
            return
    
    f.close()
    print(f"No student with IDNO {id_finder} found.")
    """header("Find Student")
    search_id = input("Enter ID of the student to find: ")
    found = False
    for student in students:
        if student['idno'] == search_id:
            print("Student found:")
            print_student_info(student)
            found = True
            break
    if not found:
        print(f"Student with ID {search_id} not found.")
    input("Press Enter to continue...")"""

    
def deleteStudent()->None:
    header("Delete Student")
    system("cls")
    print("----------------")
    id_deleter = input("Enter IDNO or lastname to delete: ")

    f = open(filename, "r")
    studentlist = f.readlines()
        
    f = open(filename, "w")
    deleted = False
    for student in studentlist:
        fields = student.strip().split(",")
        if id_deleter not in fields[0] and id_deleter not in fields[1]:
            f.write(student)
        else:
            deleted = True

    if deleted:
        print("Student deleted successfully")
    else:
        print("Student not found")
 
def updateStudent()->None: 
    header("Update Student")
    
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
	
