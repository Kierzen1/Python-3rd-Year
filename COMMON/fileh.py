"""
	accesing text file in python
"""
from os import system

system("cls")
f = open("student.txt")
data1:str = f.read() #read all content
print(data1)
f.close()
print()
f = open("student.txt")
data2:str = f.readline()# read one line at a time
print(data2)
f.close()
print()
f = open("student.txt")
data3:list = f.readlines() # read all data as a list
#display the 2nd item of the list
print(data3[2])

fields:list = data3[2].split(",")
print(fields)
f.close()

#write this data('0006','tango','uniform','bsis','3') to the file
f = open("student.txt","a")
f.write('0006')
f.write(',')
f.write('tango')
f.write(',')
f.write('uniform')
f.write(',')
f.write('bsis')
f.write(',')
f.write('3')
f.write('\n')
f.close()

print()

f = open("student.txt")
data1:str = f.read() #read all content
print(data1)
f.close()
print()













