from os import system

# Create a list to store student data
students = []

def addStudent() -> None:
    system("cls")
    print("Add Student")
    print("----------------")
    file_name = "student.txt"
    with open(file_name, 'a') as file:
        user_input = input("Enter data to write to the file: \n")
        file.write(user_input)
        
# File is automatically closed when you exit the 'with' block.
print("Data has been written to the file.")
    

def findStudent() -> None:
    print("Find Student")
    print("----------------")
    
def deleteStudent() -> None:
    print("Delete Student")
    print("----------------")
   

def updateStudent() -> None:
    print("Update Student")
    print("----------------")
    

def displayAllStudent() -> None:
    system("cls")
    print("Display All Students")
    print("----------------")
    f = open("student.txt","r")
    data1:str = f.read() #read all content
    print(data1)
    print("\n")
    f.close()
   

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

    while option != 0:
        displayMenu()
        option = int(input("Enter Option (0..5): "))

        if option == 1:
            addStudent()
        elif option == 2:
            findStudent()
        elif option == 3:
            deleteStudent()
        elif option == 4:
            updateStudent()
        elif option == 5:
            displayAllStudent()
        elif option == 0:
            terminate()
        else:
            print("Invalid option. Please try again.")
        input("Press any key to continue...")

if __name__ == "__main__":
    main()
