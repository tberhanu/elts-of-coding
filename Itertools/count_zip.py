import itertools
if __name__  == "__main__":
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