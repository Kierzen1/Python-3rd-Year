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
student = {
    'idno': '',
    'lastname': '',
    'firstname': '',
    'course': '',
    'level': '',
}

def addStudent() -> None:
    system("cls")
    print("Add Student")
    print("----------------")

    for key, value in student.items():
        student[key] = input(f"{key}: ")

    f = open(filename, 'a')
    f.write(f"{student['idno']},{student['lastname']},{student['firstname']},{student['course']},{student['level']}\n")
    f.close() 

    print("New Student Added")
    print("Data has been written to the file.")
    
def findStudent() -> None:
    system("cls")
    print("Find Student")
    print("----------------")
    id_finder = input("Enter the ID number of the student: ")
    
    f = open(filename, 'r')
    for line in f:
        student_data = line.strip().split(',')
        idnumber, lastName, firstName, course, level = student_data
        if idnumber == id_finder:
            print("Student Found:")
            print(f"IDNO: {idnumber}")
            print(f"LASTNAME: {lastName}")
            print(f"FIRSTNAME: {firstName}")
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
    f.close()             

def updateStudent() -> None:
    system("cls")
    print("Update Student")
    print("----------------")

    updater_id_ln = input("Enter IDNO or lastname to update: ")

    f = open(filename, "r")
    studentlist = f.readlines()
    f.close()

    updated = False
    update_student_data = []
    for student_data in studentlist:
        fields = student_data.strip().split(",")
        if updater_id_ln in fields[0] or updater_id_ln in fields[1]:
            print("Student Found:")
            print(f"IDNO: {fields[0]}")
            print(f"LASTNAME: {fields[1]}")
            print(f"FIRSTNAME: {fields[2]}")
            print(f"COURSE: {fields[3]}")
            print(f"LEVEL: {fields[4]}")

            for key in student:
                student[key] = input(f"{key}: ")

            updated_student = f"{student['idno']},{student['lastname']},{student['firstname']},{student['course']},{student['level']}\n"
            update_student_data.append(updated_student)
            updated = True
        else:
            update_student_data.append(student_data)

    if updated:
        f = open(filename, "w")
        f.writelines(update_student_data)
        f.close()
        print("Student Record updated successfully")
    else:
        print("Student not found")

        
def displayAllStudent() -> None:
    system("cls")
    print("Display Student")
    print("---------------")
    
    if path.exists(filename):
        f = open(filename)
        print(f.read())
        f.close()
        print("Nothing Follows....")
    else:
        print("No such File...")


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
    option = -1
    menudict = {
        1: addStudent,
        2: findStudent,
        3: deleteStudent,
        4: updateStudent,
        5: displayAllStudent,
        0: terminate,
    }

    while option != 0:
        displayMenu()
        option = int(input("Enter Option (0..5)"))
        
        menudict.get(option)()
        
        input("Press any key to continue...")
if __name__ == "__main__":
    main()
