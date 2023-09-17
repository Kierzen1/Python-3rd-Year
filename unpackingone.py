def create_lists()->None:
    numbers = [1, 2, 3, 4, 4, 4, 4]
    return numbers
    
    
def print_lists(lst):
    if len(lst)>0:
        print("Item is/are:", lst[2])
        print("Item is/are:", lst[0])
        print("excess items are:", lst[3:])
    
    print(" ")
def printlists()->None:
    new_list = create_lists()
    print_lists(new_list)
    
def main()->None:   
    printlists()
if __name__ == "__main__":
    main()
    