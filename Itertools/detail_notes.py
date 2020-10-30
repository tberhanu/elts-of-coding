import itertools
if __name__ == "__main__":
    print("______ zip(itertools.count()) _________")
    counter = itertools.count() # Gernerator: generates numbers starting from 0, 1, 2 ....
    print(next(counter)) # 0
    print(next(counter)) # 1
    print(next(counter)) # 2
    print("_________start, step __")
    counter = itertools.count(start=5, step=10)  # Generator: starts at 5 and increment by 10 each time
    print(next(counter))  # 5
    print(next(counter))  # 15
    print(next(counter))  # 25
    print("___________")
    counter = itertools.count(start=5, step=-2.5)  # Generator: starts at 5 and decrement by 2.5 each time
    print(next(counter))  # 5
    print(next(counter))  # 2.5
    print(next(counter))  # 0
    print(next(counter))  # -2.5
    print("______ zip(itertools.count()) __vs range__vs zip_longest___")
    data = [100, 200., 300, 400]
    daily_data_count = list(zip(itertools.count(), data))
    print("via count: ", daily_data_count)
    daily_data_range = list(zip(range(10), data))
    print("via range: ", daily_data_range)
    daily_data_zip_longest = list(itertools.zip_longest(range(10), data))
    print("zip longest: ", daily_data_zip_longest)
    lookup_index = {data: index for (index, data) in daily_data_count}
    print("lookup index: ", lookup_index)
    lookup_value = {index: data for index, data in daily_data_range}
    print("lookup value: ", lookup_value)

    print("______ itertools.cycle()_________")
    cycle_counter = itertools.cycle([1, 2, 3])
    print(next(cycle_counter))
    print(next(cycle_counter))
    print(next(cycle_counter))
    print(next(cycle_counter))
    print(next(cycle_counter))
    print(next(cycle_counter))
    print("__ on/off __")
    cycle_counter = itertools.cycle(("on", "off"))
    print(next(cycle_counter))
    print(next(cycle_counter))
    print(next(cycle_counter))
    print(next(cycle_counter))

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

    print("_____ itertools.chain()______")
    letters = ['a', 'b', 'c', 'd']
    numbers = [0, 1, 2, 3]
    names = ["John", "James"]
    combined = itertools.chain(letters, numbers, names) # like combined = letters + numbers + names w/o memory need
    print(list(combined))

    print("____ itertools.islice(range, start=0, end, step) _____")
    results = itertools.islice(range(10), 5) # start from 0 and at 4, 5 - 1
    print(list(results)) # [0, 1, 2, 3, 4]
    print("+++")
    results = itertools.islice(range(10), 1, 5)  # start from 1 and at 4, 5 - 1
    print(list(results)) # [1, 2, 3, 4]
    print("+++")
    results = itertools.islice(range(10), 1, 5, 2)  # start from 1 and at 4, 5 - 1, by STEP of 2
    print(list(results)) # [1, 3]

    print("___ itertools.compress() ______")
    letters = ['a', 'b', 'c', 'd']
    numbers = [0, 1, 2, 3]
    names = ["John", "James"]

    selectors = [True, True, False, True]
    results = itertools.compress(letters, selectors) # slightly looks like FILTER
    print(list(results))

    print("_______ filter ________")
    numbers = [0, 1, 2, 3, 4, 5, 6, 7]
    def lt_4(n):
        if n < 4:
            return True
        else:
            return False

    results = filter(lt_4, numbers)
    print(list(results)) # [0, 1, 2, 3]
    results = itertools.filterfalse(lt_4, numbers)
    print(list(results)) # [4, 5, 6, 7]

    print("___ itertools.dropwhile()___ ")
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 0, 1, 2]
    results = itertools.dropwhile(lt_4, numbers) # give every element after you get lt_4 once for the first time
    print(list(results)) # [4, 5, 6, 7, 0, 1, 2]
    print("___ itertools.takewhile()___ ")
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 0, 1, 2]
    results = itertools.takewhile(lt_4, numbers)  # opposite of itertools.dropwhile()
    print(list(results))  # [0, 1, 2, 3]

    print("_____ itertools.accumulate() __ and operator.mul ___")
    numbers = [3, 4, 2, 2, 1]
    results = itertools.accumulate(numbers)
    print(list(results))
    import operator
    results = itertools.accumulate(numbers, operator.mul)
    print(list(results))

    print("________ replicating iterators: itertools.tee() __________")
    numbers = [3, 4, 2, 2, 1]
    results = itertools.accumulate(numbers)
    # Once you made copy, don't use the original iterator, results.
    copy1, copy2 = itertools.tee(results)
    print("replica_1 of results :", list(copy1))
    print("replica_2 of results :", list(copy2))















