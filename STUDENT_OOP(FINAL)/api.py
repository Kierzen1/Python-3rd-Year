"""
	Student API(application program interface)
"""
from Student import * #import all properties from Student file
from os import system, path
import os

students:list = []
filename:str = "student.csv" 

def header(message: str) -> None:
    system("cls")
    print("---------------------------")
    print(message)
    print("---------------------------")

	
def checkid(idno: str) -> bool:
    f = open(filename, 'r')
    for line in f:
        student = line.strip().split(',')
        existing_idno = student[0]
        if idno == existing_idno:
            f.close()  # Close the file once the match is found
            return True
    f.close()  # Make sure to close the file even if the match is not found
    return False

	
def addStudent(idno:str="") -> None:
    header("Add Student")
    idno:str = input        ("Enter      IDNO :")
    lastname:str = input    ("Enter  LASTNAME :")
    firstname:str = input   ("Enter FIRSTNAME :")
    course:str = input      ("Enter    COURSE :")
    level:str = input       ("Enter     LEVEL :")
    # call checkid for duplicate student entry
    if checkid(idno):
        print("---------------------------")
        print("Duplicate Entry")
        print("Adding studdent Failed...")
        print("---------------------------")
        return
    student = Student(idno, lastname, firstname, course, level)
    
    f = open(filename, "a") 
    f.write(student.__str__())
    f.write("\n")
    f.close()
    
    print()
    print("New Student Added")
	
def findStudent()->None:
    system("cls")
    header("Find Student")
    message = "\nFile Not Found"
    if path.exists(filename):
        id_finder = input("Enter IDNO of the student to find: ")
        f = open(filename, 'r')
        for line in f:
            student = line.strip().split(',')
            idno, lastname, firstname, course, level = student
            if idno == id_finder:
                header("Student Found")
                print(f"IDNO:       {idno}")
                print(f"LASTNAME:   {lastname}")
                print(f"FIRSTNAME:  {firstname}")
                print(f"COURSE:     {course}")
                print(f"LEVEL:      {level}")
                f.close()
                return
        
        f.close()
        print(f"No student found.")
    else:
        print(message)
def deleteStudent() -> None:
    system("cls")
    header("Delete Student")
    message = "\nFile Not Found"
    if path.exists(filename):
        id_deleter = input("Enter IDNO or lastname to delete: ")

        f = open(filename, "r")
        slist = f.readlines()
   
        f = open(filename, "w")
        deleted = False
        validation = input("Are you really sure you want to delete this? (y/n): ").strip().lower()
        if validation == "y":
            for student in slist:
                fields = student.strip().split(",")
                if id_deleter not in fields[0] and id_deleter not in fields[1]:
                    f.write(student.__str__())
                else:
                    deleted = True
            if deleted:
                print("Student deleted successfully!!")
            else:
                print("Student not found")
        elif validation == "n":
            for student in slist:
                f.write(student.__str__())
            print("Cancelled deleting the student")
        else:
            print("Cancelled deleting the student")
    else:
        print(message)

    
def updateStudent() -> None:
    header("Update Student")
    message:str = "\nFile Not Found"
    if path.exists(filename):
        id_updater = input("Enter IDNO of the student to update: ")
        system("cls")
        f = open(filename, 'r')
        slist = f.readlines()
        f.close()

        updated = False
        
        f = open(filename, 'w')
        student_found = False  # Add a flag to track if a student was found
        for student in slist:
            fields = student.strip().split(',')
            idno, lastname, firstname, course, level = fields
            if idno == id_updater:
                print("Student Found")
                print("----------------")
                print(f"IDNO: {idno}")
                print(f"LASTNAME: {lastname}")
                print(f"FIRSTNAME: {firstname}")
                print(f"COURSE: {course}")
                print(f"LEVEL: {level}")
                print("----------------")
                print("Pressing Enter retains the value")
                new_lastname = input("Enter new LASTNAME: ")
                new_firstname = input("Enter new FIRSTNAME: ")
                new_course = input("Enter new COURSE: ")
                new_level = input("Enter new LEVEL: ")
                if new_lastname:
                    lastname = new_lastname
                if new_firstname:
                    firstname = new_firstname
                if new_course:
                    course = new_course
                if new_level:
                    level = new_level
                    
                updated_student = Student(idno, lastname, firstname, course, level)
                
                validation = input("Are you really sure you want to update this? (y/n): ").lower()
                if validation == "y":
                    f.write(updated_student.__str__())
                    f.write("\n")
                    updated = True
                else:
                    f.write(student)
                student_found = True  # Set the flag to indicate a student was found
            else:
                f.write(student)
        
        f.close()
        
        if student_found:
            if updated:
                print("Student updated successfully!!")
            else:
                print("Student not updated")
        else:
            print("No student found")  # Print this message when no matching student was found
    else:
        print(message)



def displayAllStudent() -> None:
    header("Display All Student")
    message:str = "\nFile Not Found"
    # Check if the file exists before trying to open it
    if path.exists(filename):
        f = open(filename)
        slist = f.readlines()
        f.close()
        if len(slist)>0:
            for student_data in slist:
                student_info = student_data.strip().split(',')
                idno, lastname, firstname, course, level = student_info
                
                print(f"IDNO:       {idno}")
                print(f"LASTNAME:   {lastname}")
                print(f"FIRSTNAME:  {firstname}")
                print(f"COURSE:     {course}")
                print(f"LEVEL:      {level}")
                print("---------------------------")
            message = "Nothing Follows..."
        else:
            message = "\nThe list is empty!!"
    
    print(message)

def quit()->None:
	header("Program Terminated")
	
