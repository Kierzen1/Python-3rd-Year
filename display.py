"""
	a program that would accept a string and display 
	hello, and the inputted string
"""
#imprt the necessary libraary for clearing the console screen
import os 

os.system("cls")
#accept a string, put it in a variable called name
name = input("what is your name ")


print("hello, " + name)