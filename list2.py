def lists()->None:
    letters = ["a", "b", "c"]
    print(letters[0])
    letters[0]="A"
    print(letters[0:3])
    print(letters[0:2])
    print(letters[0::2])

def main()->None:
    lists()
if __name__ == "__main__":
    main()