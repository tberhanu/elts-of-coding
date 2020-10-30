import itertools
if __name__ == "__main__":
    print("______ itertools.repeat() _____")
    repeat_counter = itertools.repeat("Here", times=3) # throws StopIteration exception if called more than twice
    print(next(repeat_counter))
    print(next(repeat_counter))
    print(next(repeat_counter))

    print("_____ map and itertools.repeat() ________")
    squares = map(pow, range(4), itertools.repeat(3))
    print(list(squares)) # [0, 1, 8, 27]

    print("_____ itertools.starmap() ________")
    squares = map(pow, range(3), itertools.repeat(2))
    print(list(squares)) # [0, 1, 4]
    squares = itertools.starmap(pow, [(0, 2), (1, 2), (2, 2)])
    print(list(squares)) # [0, 1, 4]