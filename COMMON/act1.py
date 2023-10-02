"""
	A program that would accept a positive integer value
	not greater than 20, display a numbers in a format similar to
    the one shown below
	example:
		input (n): 5
		
		1   2   3   4   5
		2   3   4   
		3          	
"""
from os import system
def main()->None:
    start:int = 1
    system("cls")
    n:int = int(input("Enter value(n):"))
    #
    if n>0 and n<=20:
        for i in range((n+1),start,-1):
            for j in range(start,i):
                print(j,end=" ")
            print("")
            start += 1
    
    
if __name__=="__main__":
    main()

