#this is a line comment
"""
	this is block(more than one line) comment
	comments are not included in the translation to code
	
	A program that would clear the screen and accept two(2)
	integers put them to variable a and b respectively 
	and display respectively the sum, difference,product,quotient
		
"""
#import the necessary library for screen management
import os
#invoke the command to clear the screen
os.system("cls")

#accept the integer inputs
a = int(input("Enter First value:")) #CTRL-D repeat the line i notepad++
b = int(input("Enter Second value:")) 
#process section
sum = a+b
diff = a-b
prod = a*b
quot = a/b
#display the result
print("The sum of %d and %d is %d" % (a,b,sum))
print("The difference of %d and %d is %d" % (a,b,diff))
print("The product of %d and %d is %d" % (a,b,prod))
print("The quotient of %d and %d is %f" % (a,b,quot))





