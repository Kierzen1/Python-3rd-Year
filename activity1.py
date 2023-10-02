"""
	Name :<Carpentero Krystel Kaye> 
	Lab Schedule:<9:00 - 10:30>
	
	Create a python program that would accept two(2)
	integers not greater 10 and not less than 0,(1 to 10 only),
	each inputted value respectively represents the row and the 
	column value of the size of a multiplication table matrix
	example:
		row : 5
		column : 5
		
		output :
		1  2  3  4  5
		2  4  6  8 10
		3  6  9 12 15
		4  8 12 16 20
		5 10 15 20 25
"""

def generate_multiplication_table(row, column):
	
	
    if row < 1 or row > 10 or column < 1 or column > 10:
        print("Both row and column values should be between 1 and 10.")
        return

    for i in range(1, row + 1):
        for j in range(1, column + 1):
            print(f"{i * j:2}", end="  ")
        print()  


row = int(input("Enter the number of rows (1 to 10): "))
column = int(input("Enter the number of columns (1 to 10): "))

for i in range(1, row + 1):
	for j in range(1, column + 1):
		print(f"{i * j:2}", end="  ")
	print()

