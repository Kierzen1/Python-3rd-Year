def lists()->None:
    letters = ["a", "b", "c"]
    matrix = [[0,1],[2,3]]
    zeros=[0]*5
    combined = zeros + letters
    print(combined)
    numbers = list(range(20))
    print(numbers)
    chars = list("Hello World")
    print(chars)
    print(len(chars))

def main()->None:
    lists()
if __name__ == "__main__":
    main()