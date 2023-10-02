"""
	Set - a linear collection of distinct(unique) elements
        - unordered (un-indexed)
"""
from os import system

def main()->None:
    system("cls")
    a:set = {1,2,3,4,5}
    b:set = {4,5,6,7,8,9}
    
    mylist:list = [1,2,1,3,3,4,5,6,7,4,8,9]
    
    print(f"set A : {a}")
    print(f"set B : {b}")
    
    #print the 3rd element of the set
    slist:list = list(a)
    print(slist[2])
    
    print(f"original list with duplicates {mylist}")
    #remove all duplicates of the list mylist
    myset:set = set(mylist) #ordering will be removed from the feature
    print(f"updated list with NO duplicates {myset}")
    print()
    
    #operations in set
    #c:set = a.union(b)
    c:set = a | b
    print(f"union of set{a} and set{b} is {c}")
    c:set = a & b
    print(f"intersection of set{a} and set{b} is {c}")
    c:set = a & b
    print(f"intersection of set{a} and set{b} is {c}")
    c:set =  a.difference(b)
    c:set =  a-b
    print(f"subtract of set{a} and set{b} is {c}")
    
    
    
if __name__=="__main__":
    main()
