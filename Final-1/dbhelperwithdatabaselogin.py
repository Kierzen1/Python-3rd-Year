# Import necessary libraries
from mysql.connector import connect
from pwinput import pwinput

# Establish a database connection
def db_connect() -> object:
    return connect(
        host="localhost",
        user="root",
        password="",
        database="python_booc"
    )


def doProcess(sql: str) -> bool:
    db = db_connect()
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()
    return True if cursor.rowcount > 0 else False


def getProcess(sql: str) -> list:
    db = db_connect()
    cursor = db.cursor(dictionary=True)
    cursor.execute(sql)
    return cursor.fetchall()

def fetch_records(table_name):
    sql = f"SELECT * FROM `{table_name}`"
    return getProcess(sql)

def getrecord(table, **kwargs) -> list:
    params = list(kwargs.items())
    flds = list(params[0])
    sql = f"SELECT * FROM `{table}` WHERE `{flds[0]}`='{flds[1]}'"
    return getProcess(sql)

def userLogin(table, **kwargs) -> list:
    keys = list(kwargs.keys())
    vals = list(kwargs.values())
    sql = f"SELECT * FROM `{table}` WHERE `{keys[0]}`='{vals[0]}' AND `{keys[1]}`='{vals[1]}'"
    return getProcess(sql)

def addrecord(table:str,**kwargs)->bool:
    flds:list = list(kwargs.keys())
    vals:list = list(kwargs.values())
    fld:str = "`,`".join(flds)
    val:str = "','".join(vals)
    sql:str = f"INSERT INTO `{table}`(`{fld}`) values('{val}')"
    print(sql)
    return doProcess(sql)
    
def updaterecord(table:str,**kwargs)->bool:
    flds:list = list(kwargs.keys())
    vals:list = list(kwargs.values())
    fld:list = []
    for i in range(1,len(flds)):
        fld.append(f"`{flds[i]}`='{vals[i]}'")
    params:str = ",".join(fld)
    sql:str = f"UPDATE `{table}` SET {params} WHERE `{flds[0]}`='{vals[0]}'"
    print(sql)
    return doProcess(sql)
    
def deleterecord(table:str,**kwargs)->bool:
    params:list = list(kwargs.items())
    flds:list = list(params[0])
    sql:str = f"DELETE FROM `{table}` WHERE `{flds[0]}`='{flds[1]}'"
    return doProcess(sql)

#print(getrecord("student",idno='0002'))
#print(getall("student"))
#updaterecord('student',idno='0004',lastname='foxtrot',firstname='gold',course='bscs',level='3')
#print(deleterecord("student",idno='0002'))

def get_all_records():
    
    table = "student"
    db = db_connect()
    cursor = db.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM `{table}`")
    header("Show Record")

    for record in cursor:
        print()
        for key, value in record.items():
            print(f"{key}: {value}".upper())
        print("--------------")  # Empty line to separate records

    cursor.close()
    db.close()
    
def get_record_by_id():
    table = "student"
    system("cls")
    header("Show Record")
    idno = input("Enter the ID to search for: ")
    records = getrecord(table, idno=idno)
    header("Show Record")
    
    if records:
        for record in records:
            for key, value in record.items():
                print(f"{key}: {value}")
            print()
    else:
        print(f"No record with ID '{idno}' found in table '{table}'.")

def add_record_menu():
    table = "student"
    system("cls")
    
    header("Add Record")
    idno = input("Enter ID number: ")
    lastname = input("Enter last name: ")
    firstname = input("Enter first name: ")
    course = input("Enter course: ")
    level = input("Enter level: ")
    
    # Create a dictionary with the collected values
    data = {
        "idno": idno,
        "lastname": lastname,
        "firstname": firstname,
        "course": course,
        "level": level
    }
    
    success = addrecord(table, **data)
    
    if success:
        print("Record added successfully.")
    else:
        print("Failed to add the record.")
        
def delete_record_menu():
    table = "student"
    header("Show Record")
    idno = input("Enter the ID to delete: ")
    success = deleterecord(table, idno=idno)
    if success:
        print("Record deleted successfully.")
    else:
        print("Failed to delete the record.")

 
def terminate()->None:
    print("Program Terminated")
    quit()

#------------------------MENU--------------------------#
def displayMenu()->None:
    system("cls")
    menu_options = [
        "----------- Student List -----------",
        "1. Show All Records",
        "2. Find Records",
        "3. Add Record",
        "4. Delete Record",
        "0. Quit/End",
        "------------------------------------",
    ]

    [print(option) for option in menu_options]

def main()->None:
    option = -1
    menudict = {
        1: get_all_records,
        2: get_record_by_id,
        3: add_record_menu,
        4: delete_record_menu,
        0: terminate
    
    }

    while option != 0:
        displayMenu()
        option = int(input("Enter Option (0..5)"))
        
        menudict.get(option)()
        
        input("Press any key to continue...")

def main() -> None:
    userLogin()

if __name__ == "__main__":
    main()
