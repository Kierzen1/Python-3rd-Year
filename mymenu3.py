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
def multiply()->int: 
	system("cls")
	a:int = 0
	b:int = 0
	a,b = getinput()
	print("The product of %d and %d is %d" % (a,b,(a*b)))
def divide()->float:
	system("cls")
	a:int = 0
	b:int = 0
	a,b = getinput()
	print("The quotient of %d and %d is %f" % (a,b,(a/b)))
def add()->int: 
	system("cls")
	a:int = 0
	b:int = 0
	a,b = getinput()
	print("The sum of %d and %d is " % (a,b,(a+b)))
def subtract()->int: 
	system("cls")
	a:int = 0
	b:int = 0
	a,b = getinput()
	print("The difference of %d and %d is %d" % (a,b,(a-b)))
	
def terminate()->None:
	print("Program Terminated")
	
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
	menudict:dict ={
		1:multiply,
		2:divide,
		3:add,
		4:subtract,
		0:terminate,
	}
	
	while option != 0:
		displaymenu()
		option = int(input("Enter Option(0..4):"))	
		menudict.get(option)() #transform the value into a module/function
		input("Press any key to continue...")

#main module trigger
if __name__=="__main__":
	main()






