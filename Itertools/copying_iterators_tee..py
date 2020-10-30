import itertools
if __name__ == "__main__":

    print("________ replicating iterators: itertools.tee() __________")
    numbers = [3, 4, 2, 2, 1]
    results = itertools.accumulate(numbers)
    # Once you made copy, don't use the original iterator, results.
    copy1, copy2 = itertools.tee(results)
    print("replica_1 of results :", list(copy1))
    print("replica_2 of results :", list(copy2))