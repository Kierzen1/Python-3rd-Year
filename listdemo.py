"""
    In the given array, display the 2nd element of  the sub list
"""
    
from os import system

def main()->None:
    names:list = ["alpha", "bravo", "charlie", "delta", "echo",["a", "b", "c"]]
    print(names)
    
    print(names[5][1])
        result = [[sum(a * b for a, b in zip(A_row, B_col))
                        for B_col in zip(*B)]
                                for A_row in A]
 
for r in result:
    print(r)
    
if __name__=="__main__":
    main()
    