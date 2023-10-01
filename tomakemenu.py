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
