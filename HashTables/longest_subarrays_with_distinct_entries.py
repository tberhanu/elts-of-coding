def longest_subarray_with_distinct_entries(arr):
    """
    Input: arr = [f, s, f, e, t, w, e, n, w, e]
    Output: [s, f, e, t, w] all distict and located next to one another

    Tess Strategy: Traverse until you get the duplicate while saving the elt vs it's index via hashtable.
                   Once getting the duplicate, save what you've so far, and retrieve the previous_index of the
                   duplicate so that you may start traversing at previous_index + 1, and by clearing the hashtable
                   to start from empty dictionary.
    Time Complexity: O(N) as we do constant number of operations per element (looks TRICKY ....????)
    Space Complexity: O(N) at worst case
    """
    i, j = 0, 0
    length = -1
    hashtable = {}
    indexes = [(0, len(arr) - 1)]
    while j < len(arr):
        e = arr[j]
        if e not in hashtable:
            hashtable[e] = j
            j += 1
        else:
            j -= 1
            if j - i > length:
                indexes = [(i, j)]
                length = j - i
            index = hashtable[e]
            i = index + 1
            j = i
            hashtable = {}

    return arr[indexes[0][0]: indexes[0][1]+1]

if __name__ == "__main__":
    arr = ["f", "s", "f", "e", "t", "w", "e", "n", "w", "e"]
    indexes = longest_subarray_with_distinct_entries(arr)
    print(indexes)

    arr = ["f", "s", "e", "e", "t", "w", "e", "n", "w", "e"]
    indexes = longest_subarray_with_distinct_entries(arr)
    print(indexes)

    arr = ["f", "s", "t", "w", "e", "n"]
    indexes = longest_subarray_with_distinct_entries(arr)
    print(indexes)





