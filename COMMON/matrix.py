"""
	A program that would accept a positive integer value
	not greater than 20, display the multiplication table
	matrix
	
	example:
		input (n): 5
		
		1   2   3   4   5
		2   4   6   8  10
		3   6   9  12  15
		4   8  12  16  20
		5  10  15  20  25	
"""
from os import system
def main()->None:
    system("cls")
    n:int = int(input("Enter value(n):"))
    #validation, must be a positive value not greater than 20
    if n>0 and n<=20:
        #display the matrix result
        #using a nested loop
        for i in range(1,n):   #outer loop
            for j in range(1,n):#inner loop
                print("%4d" % (i*j),end=" ")
            print("")
    else:
        print("Accepts positive integer not greater than 20")
#main trigger
if __name__=="__main__":
    main()
    
    
    
    
    
    


