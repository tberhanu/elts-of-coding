import itertools
if __name__ == "__main__":
    def lt_4(n):
        if n < 4:
            return True
        else:
            return False

    print("___ itertools.dropwhile()___ ")
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 0, 1, 2]
    results = itertools.dropwhile(lt_4, numbers)  # give every element after you get lt_4 once for the first time
    print(list(results))  # [4, 5, 6, 7, 0, 1, 2]
    print("___ itertools.takewhile()___ ")
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 0, 1, 2]
    results = itertools.takewhile(lt_4, numbers)  # opposite of itertools.dropwhile()
    print(list(results))  # [0, 1, 2, 3]