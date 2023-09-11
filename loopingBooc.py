"""
	Looping practice
	----------------
	A program that would display values 1 to 10
    output 1 2 3 4 5
"""
from os import system
def main()->None:
     system("cls")
#using the while loop
     #initializatio
     
     row:int = int(input("Enter the row: "))
     #i:int = 10
     while row<0:
        print(row,end=" ")
        row += 2

if __name__=="__main__":
	main()