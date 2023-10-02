"""
	
    <DIOVIC B. SOLON>
    <7:30-9:00 AM TTH>
    <14092>
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
"""
from os import system
from os.path import exists, join

filename = "Student.txt"

def topmessage(message: str) -> None:
    system("cls")
    print(message)
    print("---------------")

def addStudent() -> None:
    system("cls")
    topmessage("Add Student")
    idno = input("IDNO :")
    lastname = input("LASTNAME:")
    firstname = input("FIRSTNAME:")
    course = input("COURSE:")
    level = input("LEVEL:")

    with open(filename, "a") as f:
        f.write(f"{idno},{lastname},{firstname},{course},{level}\n")
    print("New Student Added")

def findstudent() -> None:
    topmessage("Find Student")

    with open(filename) as f:
        studentlist = f.readlines()
    index = input("Enter IDNO to search: ")
    for student in studentlist:
        fields = student.split(",")
        if fields[0] == index or fields[1] == index:
            print(student)
            break
    else:
        print("Student not found")

def deletestudent() -> None:
    topmessage("Delete Student")
    id_to_delete = input("Enter IDNO to delete: ")
    with open(filename, "r") as f:
        lines = f.readlines()
    with open(filename, "w") as f:
        for line in lines:
            fields = line.strip().split(",")
            if fields[0] != id_to_delete:
                f.write(line)
    print(f"Student with IDNO {id_to_delete} deleted")

def updatestudent() -> None:
    topmessage("Update Student")
    id_to_update = input("Enter IDNO to update: ")
    updated_student_info = {}
    updated_student_info["IDNO"] = input("Enter updated IDNO: ")
    updated_student_info["LASTNAME"] = input("Enter updated LASTNAME: ")
    updated_student_info["FIRSTNAME"] = input("Enter updated FIRSTNAME: ")
    updated_student_info["COURSE"] = input("Enter updated COURSE: ")
    updated_student_info["LEVEL"] = input("Enter updated LEVEL: ")
    with open(filename, "r") as f:
        lines = f.readlines()
    
    updated_lines = []
    for line in lines:
        fields = line.strip().split(",")
        if fields[0] == id_to_update:
       
            fields[0] = updated_student_info['IDNO']
            fields[1] = updated_student_info['LASTNAME']
            fields[2] = updated_student_info['FIRSTNAME']
            fields[3] = updated_student_info['COURSE']
            fields[4] = updated_student_info['LEVEL']
            updated_lines.extend([f"{field}\n" for field in fields])
        else:
            updated_lines.append(line)
    
    with open(filename, "w") as f:     
        for line in lines:
            fields = line.strip().split(",")
            if fields[0] == id_to_update:
                f.write(f"{updated_student_info}\n")
            else:
                f.write(line)
    print(f"Student with IDNO {id_to_update} updated")

def displaystudent() -> None:
    topmessage("Display Student")

    if exists(filename):
        with open(filename) as f:
            print(f.read())
        print("Nothing Follows....")
    else:
        print("No such File...")

def terminate() -> None:
    topmessage("Program Terminate")
    exit()

def invalid() -> None:
    print("Invalid Option")

def display_menu() -> None:
    system("cls")
    menu = (
        "Student List",
        "------------------",
        "1. Add Student",
        "2. Find Student",
        "3. Delete Student",
        "4. Update Student",
        "5. Display All Student",
        "0. Quit/end",
        "-------------------"
    )

    [print(menuitem) for menuitem in menu]

def main() -> None:
    option = -1
    menuoption = {
        1: addStudent,
        2: findstudent,
        3: deletestudent,
        4: updatestudent,
        5: displaystudent,
        0: terminate
    }
    while option != 0:
        display_menu()
        option = int(input("Enter Option(0..5):"))
        function = menuoption.get(option, invalid)()
        input("Press any key to continue")

if name == "main":
    main()