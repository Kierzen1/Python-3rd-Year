from os import system
def main():
    system("cls")
    weight_pounds = input("Your weight in pounds: ")
    kilogram = 0.453592
    result = int(weight_pounds) * kilogram
    print(result)
if __name__ == "__main__":
    main()