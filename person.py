"""
    Python Class/Object
    Class - a template of an object
    Object - is an instance of a class
"""
from os import system
#person class

class Person(object):
    lastname = "alpha"
    firstname = "bravo"
    
    #python class constructor
    def __init__(self,lastname,firstname):
        self.lastname = lastname
        self.firstname = firstname
        
    def __eq__(self,otherobject):
        if self is otherobject: return True
        if type(self) != type(otherobject): return False
        return self.lastname == otherobject.lastname
        
    def __str__(self)->str:
        return f"{self.lastname} {self.firstname}"
    

def main()->None:
    system("cls")
    print("Python Class/Object")
    #instantiating a python class
    
    person1 = Person("hello","world")
    person2 = Person("hello","durano")
    
    print(f"Person 1 lastname :{person1.lastname}")
    print(f"Person 1 firstname :{person1.firstname}")
    print()
    print(f"Person 2 lastname :{person2.lastname}")
    print(f"Person 2 firstname :{person2.firstname}")
    print()
    print(person1.__eq__(person2))
    print()
    print(person1)
    print(person2)
    

if __name__=="__main__":
    main()


