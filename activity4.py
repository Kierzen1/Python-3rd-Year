import os

students = []

def displayMenu():
    os.system("cls")
    menu_options = [
        "----------- Student List -----------",
        "1. Add Student",
        "2. Find Student",
        "3. Delete Student",
        "4. Update Student",
        "5. Display All Students",
        "0. Quit/End",
        "------------------------------------"
    ]
    for menu in menu_options:
        print(menu)

def main():
    option = -1
    menu_items = {
        1: add_student,
        2: find_student,
        3: delete_student,
        4: update_student,
        5: display_all_students,
        0: terminate,
    }
    while option != 0:
        displayMenu()
        option = int(input("Enter Option(0..5): "))
        if option in menu_items:
            menu_items[option]()

def add_student():
    os.system("cls")
    student = {
        'idno': input("Enter ID: "),
        'lastname': input("Enter Last Name: "),
        'firstname': input("Enter First Name: "),
        'course': input("Enter Course: "),
        'level': input("Enter Level: "),
    }
    students.append(student)
    print(f"Student {student['idno']} has been added.")
    input("Press Enter to continue...")

def find_student():
    os.system("cls")
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
    input("Press Enter to continue...")

def delete_student():
    os.system("cls")
    delete_id = input("Enter ID of the student to delete: ")
    found = False
    for student in students:
        if student['idno'] == delete_id:
            students.remove(student)
            print(f"Student with ID {delete_id} has been deleted.")
            found = True
            break
    if not found:
        print(f"Student with ID {delete_id} not found.")
    input("Press Enter to continue...")

def update_student():
    os.system("cls")
    update_id = input("Enter ID of the student to update: ")
    found = False
    for student in students:
        if student['idno'] == update_id:
            print("Current student information:")
            print_student_info(student)
            student['lastname'] = input("Enter new Last Name: ")
            student['firstname'] = input("Enter new First Name: ")
            student['course'] = input("Enter new Course: ")
            student['level'] = input("Enter new Level: ")
            print(f"Student with ID {update_id} has been updated.")
            found = True
            break
    if not found:
        print(f"Student with ID {update_id} not found.")
    input("Press Enter to continue...")

def display_all_students():
    os.system("cls")
    print("----------- All Students -----------")
    for student in students:
        print_student_info(student)
    print("------------------------------------")
    input("Press Enter to continue...")

def terminate():
    print("Program Ended...")

def print_student_info(student):
    print(f"ID: {student['idno']}")
    print(f"Last Name: {student['lastname']}")
    print(f"First Name: {student['firstname']}")
    print(f"Course: {student['course']}")
    print(f"Level: {student['level']}")
    print("------------------------------------")

if __name__ == "__main__":
    main()