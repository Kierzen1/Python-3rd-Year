
from os import system 

def main()->None:

    system("cls")
    row:int = int(input("ENter the number of rows: "))
    column:inpt = int(input("ENter the number of column: "))
    
    if row >= 10 or column >= 10:
        print("Program terminated.")
        return  # Exit the program
        
    for row in range(1,row+1):
        for column in range(1,column+1):
            print("%4d" %(row*column),end=(" "))
            
            
        print("")
if __name__ == "__main__":
	main()
    
    