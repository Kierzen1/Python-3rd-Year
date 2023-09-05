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
def multiply(a:int,b:int)->int:
    return a*b
def division(a:int,b:int)->float:
    return a/b
def addition(a:int,b:int)->int:
    return a+b
def subtraction(a:int,b:int)->int:
    return a-b
    
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
    while option != 0:
        displayMenu()
        option = int(input("Enter Option (0..4)"))
        
        match option:
            case 1:     
                system("cls")
                print("Multiply two(2) integers")
                a,b = getinput()
                print("The product of %d and %d is %d" % (a,b,multiply(a,b)))     
            case 2:
                system("cls")
                print("Divide two(2) integers")
                a,b = getinput()
                print("The quotient of %d and %d is %d" % (a,b,division(a,b)))
            case 3:
                system("cls")
                print("Add two(2) integers")
                a,b = getinput()
                print("The difference of %d and %d is %d" % (a,b,addition(a,b)))
            case 4:
                system("cls")
                print("Subtract two(2) integers")
                a,b = getinput()
                print("The difference of %d and %d is %d" % (a,b,subtraction(a,b)))
            case 0: print("Program Terminated!!")
            case _: print("Invalid input")
        input("Press any key to continue...")

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