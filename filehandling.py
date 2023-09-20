"""
    Simple file handling
    --------------------
    read the content of the file 'emloyee.txt'
"""
from os import system
filename:str = "employee.txt"
def main()->None: 
    system("cls")
    #readl all content of the file
    f = open(filename)
    print(f.read())
    f.close()#closes the file once close you have to open another
    print("--------------")
    
    
    #read the content line-by-line
    f = open(filename)
    print(f.readlines())
    f.close()
    
    #read the content line-by-line using loop
    f = open(filename)
    index=1
    for item in f:
        index +=1
        print(f"{index} {item}")
    f.close()    
    
    #read the content line-by-line using loop string manipulation (Splitting Screen)
    f = open(filename)
    index=1
    for item in f:
        fields:list = item.split(",")
        print("INDEX: %d" % index)
        print("IDNO          :", fields[0])
        print("LASTNAME      :", fields[1])
        print("FIRSTNAME     :", fields[2])
        print("POSITION CODE :", fields[3])
        print()
        index +=1
    f.close() 
    
if __name__=="__main__":
    main()