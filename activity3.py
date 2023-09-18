"""
    Activity#3
    Kierzen Ivan Jay
    8:00-10:30 MW 
	A program that would display a menu
	shown below
	------- Main Menu -------
	1. Add Name
	2. Find Name
	3. Delete Name
	4. Update Name
	5. Display All Names
	0. Quit/Exit
	-------------------------
	Enter Option(0..5):
	provide functionalities of the menu options
"""

from os import system


myNames = []


def displaymenu()-> None:
	system("cls")
	menuitems:tuple = (
        "--------- Main Menu ----------",
        "1.Add Name",
        "2.Find Name",
        "3.Update Name",
        "4.Remove Name",
        "5.Display All Name",
        "0.Quit/End",
        "-------------------------------"
	)
	[print(item) for item in menuitems]
	

def addname()->None: 
	system("cls")
	name:str = input("Enter a new name: ")
	myNames.append(name) # add a new string to the array names
	print(f"{name} Added on the list")
	
	
def findname()->None:
	system("cls")
	name:str = input("Enter name to search: ")
	if name in myNames:
		print(f"{name} is found in the name list")
	else:
		print(f"{name} is NOT found in the name list")


def updatename()->None:
	system("cls")
	name:str = input("Enter name to search: ")
	if name in myNames:
		index:int = myNames.index(name)
		print(f"{name} is found in the name list")
		option:string = "N"
		option = input("Do you really want to update this(Y)?")
		option = option.upper()
		if option == "Y":
			name = input("Enter new name to replace: ")
			myNames[index] = name
			print("Name successfully updated !!")
		else:
			print("Name unsuccessfully updated !!!")
	else:
		print(f"{name} is NOT found in the name list")



def removename()->None:
	system("cls")
	name:str = input("Enter name to REMOVE: ")
	if name in myNames:
		print("%s is found in the name list" % name)
		option:str = input("Do you really want to delete this(Y)?")
		option = option.upper()
		if option == "Y":
			myNames.remove(name)
			print(f"{name} is successfully removed from the list")
		else:
			print(f"{name} was unsuccessfully removed from the list")
	
		
	else:
		print(f"{name} is NOT found in the name list")
	

def displayAllnames()->None: 
	system("cls")
	[print(name) for name in myNames]
	
	
def terminate()->None: pass
	
def main()->None:
	option:int = -1
	mymenu:dict = {
		1:addname,
		2:findname,
		3:updatename,
		4:removename,
		5:displayAllnames,
		0:terminate,
	}
	
	while option !=0:
		displaymenu()
		option = int (input("Enter Option(0..5): "))
		mymenu.get(option)()
		input("Press any key to continue...")


if __name__ == "__main__":
	main()