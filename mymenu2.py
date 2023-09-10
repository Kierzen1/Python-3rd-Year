"""
	A program that would display a menu
	------ Main Menu ------
	1. Multiplication
	2. Division
	3. Addition
	4. Subtraction
	0. Quit/End
	-----------------------
	 Enter Option(0..4):
	Add functionality to each option using a module
	for each operation version 1.0
"""
#import the necessary library for clearing the screen
from os import system

#define the modules for the math operation
def multiply(a:int,b:int)->int: 
	return a*b
def divide(a:int,b:int)->float: 
	return a/b
def add(a:int,b:int)->int: 
	return a+b
def subtract(a:int,b:int)->int: 
	return a-b
	
#lambda of the operation
product = lambda a,b: a*b
quotient = lambda a,b: a/b
sum = lambda a,b: a+b
difference = lambda a,b: a-b

	
	
#create an input utility module that facilitate the input
def getinput()->int:
	a:int = int(input("Enter First Value:"))
	b:int = int(input("Enter Second Value:"))
	return a,b

#module to display the menuoptions
def displaymenu()->None:
	system("cls")
	menuitems:list = [
		"------ Main Menu ------",
		"1. Multiplication",
		"2. Division",
		"3. Addition",
		"4. Subtraction",
		"0. Quit/End",
		"-----------------------"
	]
	#using list comprehension
	[print(item) for item in menuitems] 

#module main
def main()->None:
	#define the option variable
	option:int = -1 # set default option to -1
	while option != 0:
		displaymenu()
		option = int(input("Enter Option(0..4):"))
		#
		match option:
			case 1:
				system("cls")
				print("Multiply two(2) integers")
				a,b = getinput()
				#print("\nThe product of %d and %d is %d" % (a,b,multiply(a,b)))
				print("\nThe product of %d and %d is %d" % (a,b,product(a,b)))
			case 2:
				system("cls")
				print("Divide two(2) integers")
				a,b = getinput()
				#print("\nThe quotient of %d and %d is %f" % (a,b,divide(a,b)))
				print("\nThe quotient of %d and %d is %f" % (a,b,quotient(a,b)))
			case 3:
				system("cls")
				print("Add two(2) integers")
				a,b = getinput()
				#print("\nThe sum of %d and %d is %d" % (a,b,add(a,b)))
				print("\nThe sum of %d and %d is %d" % (a,b,sum(a,b)))
			case 4:
				system("cls")
				print("Subtract two(2) integers")
				a,b = getinput()
				#print("\nThe difference of %d and %d is %d" % (a,b,subtract(a,b)))
				print("\nThe difference of %d and %d is %d" % (a,b,difference(a,b)))
			case 0: print("Program Terminated")
			case _: print("Invalid Input")
		
		#
		"""
		if option == 0: print("Program Terminated")
		elif option == 1: 
			system("cls")
			print("Multiply two(2) integers")
			a,b = getinput()
			print("\nThe product of %d and %d is %d" % (a,b,multiply(a,b)))
		elif option == 2: 
			system("cls")
			print("Divide two(2) integers")
			a,b = getinput()
			print("\nThe quotient of %d and %d is %f" % (a,b,divide(a,b)))
		elif option == 3: 
			system("cls")
			print("Add two(2) integers")
			a,b = getinput()
			print("\nThe sum of %d and %d is %d" % (a,b,add(a,b)))
		elif option == 4: 
			system("cls")
			print("Subtract two(2) integers")
			a,b = getinput()
			print("\nThe difference of %d and %d is %d" % (a,b,subtract(a,b)))
		"""
		input("Press any key to continue...")

#main module trigger
if __name__=="__main__":
	main()






