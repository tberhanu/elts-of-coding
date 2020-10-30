import itertools
if __name__ == "__main__":
    print("_____ itertools.chain()______")
    letters = ['a', 'b', 'c', 'd']
    numbers = [0, 1, 2, 3]
    names = ["John", "James"]
    combined = itertools.chain(letters, numbers, names)  # like combined = letters + numbers + names w/o memory need
    print(list(combined))