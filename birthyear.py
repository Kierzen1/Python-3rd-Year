from os import system

def main():
    system("cls")
    birth_year = input("What is your Birth Year: ")
    print(type(birth_year))
    age = 2023 - int(birth_year)
    print(type(age))
    print(f"Your age is {age}")
    
if __name__ == "__main__":
    main()