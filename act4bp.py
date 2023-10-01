"""
    <Kierzen Ivan Jay Booc>
    <MW 8:00-10:30>
    <13953>
    Student List
    --------------------
    1. Add Student
    2. Find Student
    3. Delete Student
    4. Update Student
    5. Display All Student
    0. Quit/End
    ---------------------
    Enter Option(0..5):
    * Provide functionality for each option
    * use 'student.txt' as filename 
    * store the structure of the student dictionary(key-value pair )
    
    student = {
        'idno':'0001',
        'lastname':'durano',
        'firstname':'dennis',
        'course':'bscpe',
        'level':'4',
    }

"""
from os import system, path


students = []
filename = "student.txt"

def addStudent() -> None:
    system("cls")
    print("Add Student")
    print("----------------")
    idno:int = input("IDNO:")
    lastname = input("LASTNAME:")
    firstname = input("FIRSTNAME:")
    course = input("COURSE:")
    level:int = input("LEVEL:")
    
    f = open(filename, 'a')
    f.write(f"{idno},{lastname},{firstname},{course},{level}\n")
    f.close()
    
    print("New Student Added")
        
    print("Data has been written to the file.")

def findStudent() -> None:
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
    
def deleteStudent() -> None:
    system("cls")
    print("Delete Student")
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
   

def updateStudent() -> None:
    system("cls")
    print("Update Student")
    print("----------------")
    updater_id_ln = input("Enter IDNO or lastname to update: ")
    f = open(filename, "r")
    studentlist = f.readlines()

    updated = False
    update_student_data = []
    for student in studentlist:
        fields = student.strip().split(",")
        if updater_id_ln in fields[0] or updater_id_ln in fields[1]: 
            print("Student Found:")
            print(f"IDNO: {fields[0]}")
            print(f"LASTNAME: {fields[1]}")
            print(f"FIRSTNAME: {fields[2]}")
            print(f"COURSE: {fields[3]}")
            print(f"LEVEL: {fields[4]}")
            updateidno = input("Enter new ID number:")
            updatelastname = input("Enter new lastname:")
            updatefirstname = input("Enter new firstname:")
            updateCourse = input("Enter new course:")
            updateLevel = input("Enter new level:")

            if not updateidno:
                updateidno = fields[0]
            if not updatelastname:
                updatelastname = fields[1]
            if not updatefirstname:
                updatefirstname = fields[2]
            if not updateCourse:
                updateCourse = fields[3]
            if not updateLevel:
                updateLevel = fields[4]

            updated_student = f"{updateidno},{updatelastname},{updatefirstname},{updateCourse},{updateLevel}\n"
            update_student_data.append(updated_student)
            updated = True
        else:
            update_student_data.append(student)

    if updated:
        f.close() 
        f = open(filename, "w")
        f.writelines(update_student_data)
        f.close()
        print("Student Record updated successfully")
    else:
        f.close()
        print("Student not found")


def displayAllStudent() -> None:
    system("cls")
    print("Display All Students")
    print("----------------")
    f = open("student.txt","r")
    data1:str = f.read()
    print(data1)
    print("\n")
    f.close()
   

def terminate() -> None:
    print("Program Terminated")

def displayMenu() -> None:
    system("cls")
    menu_options = [
        "----------- Student List -----------",
        "1. Add Student",
        "2. Find Student",
        "3. Delete Student",
        "4. Update Student",
        "5. Display All Students",
        "0. Quit/End",
        "------------------------------------",
    ]
    
    [print(option) for option in menu_options]
    
def main() -> None:
    option:int = -1
    menudict:dict ={
        1:addStudent,
        2:findStudent,
        3:deleteStudent,
        4:updateStudent,
        5:displayAllStudent,
        0:terminate, 
    }
    
    while option != 0:
        displayMenu()
        option = int(input("Enter Option (0..5)"))
        
        menudict.get(option)()
        
        input("Press any key to continue...")
if __name__ == "__main__":
    main()
