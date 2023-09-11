"""
	Create a python program that would accept two(2)
	integers not greater than 10 and not less than 0,1(1 to 10 only),
	each inputted value respectiveley represent the row and the 
	column value of the size of a multiplication table matrix
	example row:5
		row : 5 
		column: 5
		
		output :
		1 2 3 4 5
		2 4 6 8 10
		3 6 8 9 12 15
		4 8 12 
		5 10	
"""
from os import system

def main()->None:
    
    row:int = int(input("Enter the row: "))
    column:int = int(input("Enter the column: "))
    
    for row in range(1,row+1):
        for column in range(1,column+1):
            print("%4d " %(row*column),end=" ")
            
            
        print(" ")
        
    if row == 11:
        print(quit) 
    if column == 11:
        print(qui)
    #for column in range(0,row,):
     #   print(column,end=" ")
if __name__=="__main__":
	main()