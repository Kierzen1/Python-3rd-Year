"""
    <name>
    <schedule>
    <edpcode>
	create a file 'student.txt', read,write and update this file
	for the student list
	Create the student list with a menu provided below
	----------- Student List -----------
    1. Add Student
    2. Find Student
    3. Delete Student
    4. Update Student
    5. Display All Student
    0. Quit/End
    ------------------------------------
    Enter Option(0..5):
    sample student entry below
    
    student:dict = {
        'idno':'0001',
        'lastname':'alpha',
        'firstname':'bravo',
        'course':'bsit',
        'level':'3',
    }
"""
from os import system

names:list = []

def displayMenu() -> None:
    system("cls")
    menu_options = [
        "------- Main Menu -------",
        "1. Add Student",
        "2. Find Student",
        "3. Delete Student",
        "4. Update Student",
        "5. Display All Student",
        "0. Quit/Exit",
        "-------------------------"
    ]
    for menu in menu_options:
        print(menu)

def main() -> None:
    option