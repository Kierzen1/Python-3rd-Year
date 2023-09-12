def add_number(firstnum, secondnum)->None:
    result = firstnum + secondnum
    return result
    

def main()->None:
    firstnum = 5
    secondnum = 10
    result = add_number(firstnum, secondnum)
    print("The sum is", result)
    
if _name_ == "_main_":
	main()