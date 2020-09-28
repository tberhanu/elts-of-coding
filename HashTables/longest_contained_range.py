def longest_contained_range(arr):
    """
    Question: Write a program which takes as input a set of integers represented by an array, and returns the size of
              a largest subset of integers in the array having the property that if two integers are in the subset,
              then so are all integers between them.
              Example: input: [3, -2, 7, 9, 8, 1, 2, 0, -1, 5, 8]
                       output: 6 since len([-2, -1, 0, 1, 2, 3]) is 6
              Example: input: [10, 5, 3, 11, 6, 100, 4]
                       output: 4 since len([3, 4, 5, 6]) is 4

    Brute-force: O(N log N): You can SORT, and traverse through to get the largest subset.
    Strategy: O(N): Make Use of Hashtable, set, as Insertion and Lookup is very helpful with minimum cost, O(1).
    """

    s = set(arr)
    longest = []
    max_size = 0
    i = 0
    while i < len(arr):
        ee = arr.pop(i)
        if ee in s:
            s.remove(ee)
        longest.append(ee)
        eee = ee + 1
        while eee in s:
            longest.append(s.remove(eee))
            eee += 1
        e = ee - 1
        while e in s:
            longest.insert(0, e)
            s.remove(e)
            e -= 1

        if len(longest) >= max_size:
            max_size = len(longest)
            longest = []

    return max_size

if __name__ == "__main__":
    arr = [3, -2, 7, 9, 8, 1, 2, 0, -1, 5, 8]
    size = longest_contained_range(arr) # 6 since len([-2, -1, 0, 1, 2, 3]) is 6
    print(size)
    arr = [10, 5, 3, 11, 6, 100, 4]
    size = longest_contained_range(arr)
    print(size) # 4 since len([3, 4, 5, 6]) is 4
