
def create_lists()->None:
    numbers = [1, 2, 3]
    return numbers
    
def print_lists(lst)->None:
    for item in lst:
        print(item,end=" ")
    print("")
    
def printlists()->None:
    new_list = create_lists()
    print_lists(new_list)
    
def main()->None:   
    printlists()
if __name__ == "__main__":
    main()