"""
	A program that would accept a positive integer value
	not greater than 20, display a number format similar to
    the one shown below
	example:
		input (n): 5
		
		1   2   3   4   5
		2   3   4   
		3          
		      
		
"""
from os import system
def main()->None:
    system("cls")
    n:int = int(input("Enter value(n):"))
    start:int = 1
    #validation, must be a positive value not greater than 20
    if n>0 and n<=20:
        #display the matrix result
        #using a nested loop
        for i in range(n,start,-1):
            for j in range(start,i):
                print("%3d" % j,end=" ")
            start += 1
            print("")
    else:
        print("Accepts positive integer not greater than 20")
#main trigger
if __name__=="__main__":
    main()
    
    
    
    
    
    


