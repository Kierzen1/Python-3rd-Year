def create_lists()->None:
    numbers = ["a", "b", "c"]
    numbers.append("d")
    numbers.count("b")
    if "c" in numbers:
        print(numbers.index("c"))#FINDING THE INDEX
    return numbers
    
    
def print_lists(lst):
    for items in lst:
        print(items)
def printlists()->None:
    new_list = create_lists()
    print_lists(new_list)
    
def main()->None:   
    printlists()
if __name__ == "__main__":
    main()
     