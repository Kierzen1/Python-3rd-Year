
"""
    Activity#3
    <name>
    <schedule>
	A program that would display a menu
	shown below
	------- Main Menu -------
	1. Add Student
	2. Find Student
	3. Delete Student
	4. Update Student
	5. Display All Students
	0. Quit/Exit
	-------------------------
	Enter Option(0..5):
	provide functionalities of the menu options
"""
from os import system

names:list = []

def addStudent()->None:
	system("cls")
	name = input("Enter name:")
	names.append(name)
	
def findStudent()->None:
	system("cls")
	name = input("Enter name to SEARCH:")
		if name in names:
			print(f"{names} is in the list")
		else
			print(f"{names} NOT FOUND in the list")
		
def deleteStudent()->None:
	system("cls")
	name = input("Enter name to DELETE:")
		if name in names:
			print(f"{names} is in the list")
			opt:str = input(f"Do you really want to remove {names} in the list? (y,n)")
			opt = opt.upper()
			if opt == "Y":
				names.remove()
	
		else:
			print(f"{names} is not in the list")
	
def updateStudent()->None:
	system("cls")
	name = input("Enter name to UPDATE:")
		if name in names:
			print(f"{names} is in the list")
			index:int = names.index(name)
			opt:str = input(f"Do you really want to update {names} in the list? (y,n)")
			opt = opt.upper()
				if opt == "Y":
					newname:str = input("Enter New Name:")
					names[index] = newname
					print(f"{names} is update to {newname} from the list")		
		else 
			print(f"{names} NOT FOUND in the list")
			
def displayallStudent()->None:
system("cls")
menuoption:tuple = (

	"------- Main Menu -------",
		"1. Add Name",
		"2. Find Name",
		"3. Delete Name",
		"4. Update Name",
		"5. Display All Names",
		"0. Quit/Exit",
	"-------------------------"

)

def terminate()->None:
 print("Program Ended")

[print(menu) for menu in menuoptions]

def main()->None:
displaymenu()
	option:int = -1
	menuitems:dict = {
		1:addname,
		2:findname,
		3:deletename,
		4:updatename,
		5:displayAllname,
		0:terminate,
	}

while option !=0:
 displaymenu()
	option = int(input("Enter Option(0...5):"))
	menuitems.get(option)()
	input("Press any key to continue....")
	
if__name__=="__main__":
	main()
