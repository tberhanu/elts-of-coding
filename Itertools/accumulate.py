import itertools
import operator

if __name__ == "__main__":
    print("_____ itertools.accumulate() __ and operator.mul ___")
    numbers = [3, 4, 2, 2, 1]
    results = itertools.accumulate(numbers)
    print(list(results))

    results = itertools.accumulate(numbers, operator.mul)
    print(list(results))