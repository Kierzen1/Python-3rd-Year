"""
	get employee details
	read two(2) files
    read the 'employees.txt'
    read the 'position.txt'
    join the related fields of the two(2) files together
    to display a joint empolyee information
    
"""
from os import system,path

employee_file = "employee.txt"
position_file = "position.txt"

employee:list = []
position:list = []
def main()->None:
    system("cls")
    # read the content of the employee and put it on a list
    if path.exists(employee_file):
        employee = open(employee_file)
        employee.close()
        
    else:
        print("file does not exist")
    
    
if __name__=="__main__":
    main()

