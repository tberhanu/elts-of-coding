import itertools
if __name__ == "__main__":
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