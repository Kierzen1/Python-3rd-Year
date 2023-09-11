"""
    A program that would display a menu
    -------Main Menu--------
    1. Multiplication
    2. Division
    3.Addition
    4. Subtraction
    0. Quit
    ------------------------
     Enter Option
     (0...4)
     Add funtionality to its option using module for each opperation
     version 1.0
     
"""
from os import system 

a:int = 0
b:int = 0
def multiply()->int:
    a:int = 0
    b:int = 0
    a,b = getinput()
    print("The product of %d and %d is %d" % (a,b,(a*b)))
def division()->float:
    a:int = 0
    b:int = 0
    a,b = getinput()
    print("The quotient of %d and %d is %f" % (a,b,(a/b)))
def addition()->int:
    a:int = 0
    b:int = 0
    a,b = getinput()
    print("The sum of %d and %d is %d" % (a,b,(a+b)))
def subtraction()->int:
    a:int = 0
    b:int = 0
    a,b = getinput()
    print("The difference of %d and %d is %d" % (a,b,(a-b)))
def terminate()->None:
    print("Program Terminated")
    
#lambda of the operation
product = lambda a,b: a*b
quotient = lambda a,b: a/b
sum = lambda a,b: a+b
difference = lambda a,b: a-b
    
#create an input utility module that facilitate the inpt
def getinput()->int:
    a:int = int(input("Enter First Value: "))
    b:int = int(input("Enter Second Value: "))
    return a,b
    
#module to display the menuoptions
def displayMenu()->None:
    system("cls")
    menuitems:list = [
        "-------Main Menu--------",
        "1. Multiplication",
        "2. Division",
        "3.Addition",
        "4. Subtraction",
        "0. Quit",
        "------------------------"
    ]
    #using list comprehension
    [print(item)for item in menuitems]
    
def main()->None:
    option:int = -1
    menudict:dict ={
        1:multiply,
        2:division,
        3:addition,
        4:subtraction,
        0:terminate,
        
    }
    
    while option != 0:
        displayMenu()
        option = int(input("Enter Option (0..4)"))
        
        menudict.get(option)()
        
        input("Press any key to continue...")
        """match option:
            case 1:     
                system("cls")
                print("Multiply two(2) integers")
                a,b = getinput()
                print("The product of %d and %d is %d" % (a,b,product(a,b)))     
            case 2:
                system("cls")
                print("Divide two(2) integers")
                a,b = getinput()
                print("The quotient of %d and %d is %d" % (a,b,quotient(a,b)))
            case 3:
                system("cls")
                print("Add two(2) integers")
                a,b = getinput()
                print("The difference of %d and %d is %d" % (a,b,sum(a,b)))
            case 4:
                system("cls")
                print("Subtract two(2) integers")
                a,b = getinput()
                print("The difference of %d and %d is %d" % (a,b,difference(a,b)))
            case 0: print("Program Terminated!!")
            case _: print("Invalid input")
        input("Press any key to continue...")"""

        """
        if option == 0: print("Program Terminated")
        elif option == 1: 
            system("cls")
            print("Multiply two(2) integers")
            a,b = getinput()
            print("\nprint the product of %d and %d is %d" % (a,b,multiply(a,b))) 
        elif option == 2: 
            system("cls")
            print("Divide two(2)integers")
            a,b = getinput()
            print("\nprint the quotient of %d and %d is %d" % (a,b,division(a,b)))
        elif option == 3: 
            system("cls")
            print("Add two(2)integers")
            a,b = getinput()
            print("\nprint the quotient of %d and %d is %d" % (a,b,addition(a,b)))
        elif option == 4: 
            system("cls")
            print("Divide two(2)integers")
            a,b = getinput()
            print("\nprint the quotient of %d and %d is %d" % (a,b,subtraction(a,b)))
        input("Press any key to continue")
       """
     
       
       
       
if __name__=="__main__":
    main()