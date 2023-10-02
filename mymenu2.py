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
names:list = []
def printmenu()->None:
	menu:tuple = (
		"------- Main Menu -------",
		"1. Add Name",
		"2. Find Name",
		"3. Delete Name",
		"4. Update Name",
		"5. Display All Names",
		"0. Quit/Exit",
		"-------------------------"
	)
	[print(item) for item in menu]
	

def addname()->None:
	name:str = input("Enter name to add in the list: ")
	names.append(name)
	print(f"Successfully added {name} in the list")
	
def findname()->None:
	name:str = input("Enter name to search in the list: ")
	if name in names:
		print(f"{name} is FOUND in the list")
	else:
		print(f"{name} is NOT FOUND in the list")
		
def deletename()->None:
	name:str = input("Enter name to delete in the list: ")
	if name in names:
		print(f"{name} is FOUND in the list")
		opt:str = input(f"Are you really really sure to delete {name} in the list? (y/n)")
		opt = opt[0].upper()
		if opt == "Y":
			names.remove(name)
			print(f"Successfully removed {name} from the list")
	else:
		print(f"{name} is NOT FOUND in the list")
		
def updatename()->None:
	name:str = input("Enter name to update in the list: ")
	if name in names:
		print(f"{name} is FOUND in the list")
		opt:str = input(f"Do you really really want to update {name} in the list? (y/n)")
		opt = opt[0].upper()
		if opt == "Y":
			newName:str = input("Enter new name: ")
			index:int = names.index(name)
			names[index] = newName
			print(f"Successfully update {name} to {newName} in the list")
	else:
		print(f"{name} is NOT FOUND in the list")

def displayAllNames()->None:
	if len(names) <= 0:
		print("List is empty!")
	else:
		print("Names in the list are:")
		[print(name) for name in names]
	
def terminate()->None:
	print("Program Ended Bye Bye!")


def main()->None:
	menuModules:dict = {
			1:addname,
			2:findname,
			3:deletename,
			4:updatename,
			5:displayAllNames,
			0:terminate,
		}
	option:int = -1
	while option != 0:
		system("cls")
		printmenu()
		option = int(input("Enter Option(0..5): "))
		if option >= 0 and option <= 5:
			system("cls")
			menuModules.get(option)()
		else:
			print("Invalid Option!")
		input("Press any key to continue...")
	

if __name__ =="__main__":
	main()



