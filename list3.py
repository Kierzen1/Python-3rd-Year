

def lists()->None:
    numbers = list(range(20))
    odd = numbers[::2]
    #reverse = print(odd[::-1])
    return odd
def print_lists(lst):
    for items in lst:
        print(items)
def printlists()->None:
    new_list = lists()
    print_lists(new_list)
    
def main()->None:
    printlists()
if __name__ == "__main__":
    main()