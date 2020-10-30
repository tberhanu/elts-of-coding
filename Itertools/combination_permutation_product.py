import itertools
if __name__ == "__main__":
    print("____ itertools.combinations() __ itertools.permutations() __")
    letters = ['a', 'b', 'c', 'd']
    numbers = [0, 1, 2, 3]
    names = ["John", "James"]
    print("___ comb 2 of them ___")
    comb_elts = itertools.combinations(letters, 2)
    print(comb_elts)

    print("_____ perm 3 of them ___")
    perm_elts = itertools.permutations(letters, 3)
    print(list(perm_elts))

    print("____ itertools.product() ___ perm with repeat ____")
    prod_elts = itertools.product(numbers, repeat=3)
    print(list(prod_elts))

    print("____ itertools.combinations_with_replacement()_____")
    results = itertools.combinations_with_replacement(numbers, 3)
    print(list(results))