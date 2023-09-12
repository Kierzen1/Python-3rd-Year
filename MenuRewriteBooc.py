from os import system

def multiply(a:int,b:int)->int:
    return a*b
def division(a:int,b:int)->float:
    return a/b
def addition(a:int,b:int)->int:
    return a+b
def subtraction(a:int,b:int)->int:
    return a-b
    
product = lambda a,b : a*b
quotient = lambda a,b : a/b
sum = lambda a,b : a+b
difference = lambda a,b : a-b

def getInput()->None:
    a:int = int(input("Enter the first value: "))
    b:int = int(input("Enter the first value: "))
    return a,b

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
    
    [print(item)for item in menuitems]

def main()->None:
    option:int = -1
    while option != 0:
        displayMenu()
        option = int(input("Enter number from 0..4: "))
        
        match option:
            case 1:
                system("cls")
                a,b = getInput()
                print("The product of %d and %d is %d" % (a,b,product(a,b)))
            case 2: 
                system("cls")
                a,b = getInput()
                print("The quotient of %d and %d is %f" % (a,b,quotient(a,b)))
            case 3: 
                system("cls")
                a,b = getInput()
                print("The sum of %d and %d is %d" % (a,b,sum(a,b)))
            case 4: 
                system("cls")
                a,b = getInput()
                print("The difference of %d and %d is %d" % (a,b,difference(a,b)))
        input("Press to continue...")
    

if __name__ == "__main__":
    main()

