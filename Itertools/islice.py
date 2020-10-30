import itertools
if __name__ == "__main__":
    """
    Remember that files are ITERATORS and whenever you call NEXT on them, it gives the next LINE, so we can take
    some lines without loading the entire file from memory.
    """
    print("____ itertools.islice(range, start=0, end, step) _____")
    results = itertools.islice(range(10), 5)  # start from 0 and at 4, 5 - 1
    print(list(results))  # [0, 1, 2, 3, 4]
    print("+++")
    results = itertools.islice(range(10), 1, 5)  # start from 1 and at 4, 5 - 1
    print(list(results))  # [1, 2, 3, 4]
    print("+++")
    results = itertools.islice(range(10), 1, 5, 2)  # start from 1 and at 4, 5 - 1, by STEP of 2
    print(list(results))  # [1, 3]


    with open('test.log', 'r') as f:
        header = itertools.islice(f, 3) # start from the first line and end at the third line.
        for line in header:
            print(line, end='')