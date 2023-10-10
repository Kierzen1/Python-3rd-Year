import mysql.connector as connectSQL

mySQL = connectSQL.connect(
    host="localhost",
    user="root",
    password="",
    database="student"
)

if mySQL.is_connected():
    print("Connected Successfuly")

else: print("failed to connect")

mySQL.close()
