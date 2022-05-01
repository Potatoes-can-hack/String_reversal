while True:
    sample = input("Enter a string to reverse: ")
    data = []
    for letter in sample:
        data.append(letter)
    data.reverse()
    for alphabet in data:
        print(alphabet, end = "")
    print()