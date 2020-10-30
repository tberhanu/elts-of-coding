import itertools
if __name__ == "__main__":
    print("___ itertools.compress() ______")
    letters = ['a', 'b', 'c', 'd']
    numbers = [0, 1, 2, 3]
    names = ["John", "James"]

    selectors = [True, True, False, True]
    results = itertools.compress(letters, selectors)  # slightly looks like FILTER
    print(list(results))

    print("_______ filter ________")
    numbers = [0, 1, 2, 3, 4, 5, 6, 7]


    def lt_4(n):
        if n < 4:
            return True
        else:
            return False


    results = filter(lt_4, numbers)
    print(list(results))  # [0, 1, 2, 3]
    results = itertools.filterfalse(lt_4, numbers)
    print(list(results))  # [4, 5, 6, 7]