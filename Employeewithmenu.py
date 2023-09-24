"""
	file handling with menu
"""
from os import system
def readFileContent()->None:
    filename:str = 'employee.txt'

    system("cls")  
    
    #read the content line-by-line using loop string manipulation (Splitting Screen)
    f = open(filename)
    index=1
    for item in f:
        fields:list = item.split(",")
        print("INDEX: %d" % index)
        print("IDNO          :", fields[0])
        print("LASTNAME      :", fields[1])
        print("FIRSTNAME     :", fields[2])
        print("POSITION CODE :", fields[3])
        print()
        index +=1
    f.close() 
    
def displayMenu()->None:
    system("cls")
    menuitems:list = [
        "-------Main Menu--------",
        "1. Find Employee",
        "2. Display all Employee",
        "3.Add numbers of day(s) worked",
        "4. Generate Payroll",
        "0. Quit",
        "------------------------"
    ]
    #using list comprehension
    [print(item)for item in menuitems]
def main()->None:
    option:int = -1
    while option != 0:
        displayMenu()
        option = int(input("Enter Option (0..4)"))
        
        match option:
            case 1:     
                system("cls")
                print("Lorem")   
            case 2:
                system("cls")
                readFileContent() 
            case 3:
                system("cls")
                print("Lorem")
            case 4:
                system("cls")
                print("Lorem")
            case 0: print("Program Terminated!!")
            case _: print("Invalid input")
        input("Press any key to continue...")
        
if __name__=="__main__":
    main()