from os import system

students = []
filename = "student.txt"

def addStudent() -> None:
    system("cls")
    print("Add Student")
    print("----------------")
    idno = input("IDNO:")
    lastname = input("LASTNAME:")
    firstname = input("FIRSTNAME:")
    course = input("COURSE:")
    level = input("LEVEL:")

    # Create a dictionary for the new student
    student_data = {
        'IDNO': idno,
        'LASTNAME': lastname,
        'FIRSTNAME': firstname,
        'COURSE': course,
        'LEVEL': level
    }

    # Append the new student dictionary to the list
    students.append(student_data)

    # Open the file in append mode and write the student data
    with open(filename, 'a') as file:
        file.write(f"{idno},{lastname},{firstname},{course},{level}\n")

    print("New Student Added")
    print("Data has been written to the file.")

def findStudent() -> None:
    system("cls")
    print("Find Student")
    print("----------------")
    id_finder = input("Enter IDNO of the student to find: ")
    
    for student_data in students:
        if student_data['IDNO'] == id_finder:
            print("Student Found:")
            print(f"IDNO: {student_data['IDNO']}")
            print(f"LASTNAME: {student_data['LASTNAME']}")
            print(f"FIRSTNAME: {student_data['FIRSTNAME']}")
            print(f"COURSE: {student_data['COURSE']}")
            print(f"LEVEL: {student_data['LEVEL']}")
            return
    
    print(f"No student with IDNO {id_finder} found.")

def deleteStudent() -> None:
    system("cls")
    print("Delete Student")
    print("----------------")
    id_deleter = input("Enter IDNO or lastname to delete: ")

    deleted = False
    updated_students = []
    for student_data in students:
        if (
            id_deleter != student_data['IDNO'] and id_deleter.lower() != student_data['LASTNAME'].lower()  # Case-insensitive comparison
        ):
            updated_students.append(student_data)
        else:
            deleted = True

    if deleted:
        # Update the list of students
        students[:] = updated_students
        # Overwrite the file with updated student data
        with open(filename, 'w') as file:
            for student_data in students:
                file.write(f"{student_data['IDNO']},{student_data['LASTNAME']},{student_data['FIRSTNAME']},{student_data['COURSE']},{student_data['LEVEL']}\n")
        print("Student deleted successfully")
    else:
        print("Student not found")



def updateStudent() -> None:
    system("cls")
    print("Update Student")
    print("----------------")
    updater_id_ln = input("Enter IDNO or lastname to update: ")

    updated = False
    for student_data in students:
        if updater_id_ln == student_data['IDNO'] or updater_id_ln == student_data['LASTNAME']:
            print("Student Found:")
            print(f"IDNO: {student_data['IDNO']}")
            print(f"LASTNAME: {student_data['LASTNAME']}")
            print(f"FIRSTNAME: {student_data['FIRSTNAME']}")
            print(f"COURSE: {student_data['COURSE']}")
            print(f"LEVEL: {student_data['LEVEL']}")

            student_data['IDNO'] = input("Enter new IDNO:") or student_data['IDNO']
            student_data['LASTNAME'] = input("Enter new LASTNAME:") or student_data['LASTNAME']
            student_data['FIRSTNAME'] = input("Enter new FIRSTNAME:") or student_data['FIRSTNAME']
            student_data['COURSE'] = input("Enter new COURSE:") or student_data['COURSE']
            student_data['LEVEL'] = input("Enter new LEVEL:") or student_data['LEVEL']

            updated = True

    if updated:
        # Overwrite the file with updated student data
        with open(filename, 'w') as file:
            for student_data in students:
                file.write(f"{student_data['IDNO']},{student_data['LASTNAME']},{student_data['FIRSTNAME']},{student_data['COURSE']},{student_data['LEVEL']}\n")
        print("Student Record updated successfully")
    else:
        print("Student not found")

def displayAllStudent() -> None:
    system("cls")
    print("Display All Students")
    print("----------------")
    with open(filename, "r") as file:
        data1 = file.read()  # read all content
        print(data1)
        print("\n")

def terminate() -> None:
    print("Program Terminated")

def displayMenu() -> None:
    system("cls")  # Clear the console (Windows specific)
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
