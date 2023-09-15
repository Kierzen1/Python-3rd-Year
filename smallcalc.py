"""
A program that would accept two (2)
values and display the sum, difference, product, quotient
of the inputted value
"""

from os import system

# The function main
def main():
    system("cls")
    firstnumber = int(input("Input the first number: "))
    secondnumber = int(input("Input the second number: "))
    sum_result = firstnumber + secondnumber
    difference = firstnumber - secondnumber
    product = firstnumber * secondnumber
    quotient = firstnumber / secondnumber

    print(f"The sum of {firstnumber} and {secondnumber} is {sum_result}")
    print(f"The difference of {firstnumber} and {secondnumber} is {difference}")
    print(f"The product of {firstnumber} and {secondnumber} is {product}")
    print(f"The quotient of {firstnumber} and {secondnumber} is {quotient}")

# Main trigger
if __name__ == "__main__":
    main()
