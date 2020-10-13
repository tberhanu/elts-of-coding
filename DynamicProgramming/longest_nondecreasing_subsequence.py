# Hard
"""
Write a program that takes as input an array of numbers and returns the length of a longest nondecreasing
subsequence in the array.
Example: arr = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9]
Longest: [0, 4, 10, 14] or [0, 2, 6, 9]

Hint: Express the longest nondecreasing subsequence ending at entry in terms of the longest nondecreasing
subsequence appearing in the subarray consisting of preceding elements.

Strategy:
    1. Have a dictionary: the arr index as a KEY and the longest subsequence ENDING AT that index as a VALUE.
    2. By default, fill out all the values of the dictionary as 1 since each letter has at least 1 long subsequent.
    3. Since the max length of subsequent ending at index 0 is always 1, skip it and start from index j = 1.
    4. So, start the ptr i from 0, and count if any elt arr[i] <= the arr[j], and if the corresponding subsequent
       values, lookup[i] >= lookup[j], then increment the lookup[j] by one. N.B: Everytime you update the lookup[j],
       make sure to update the prev_subsequent_index[j] so that you can track the previous index or from where it comes.
    5. Sort the lookup_subseq_length by the VALUE, and get the highest value INDEX.
    6. Once getting the highest value INDEX, track the previous indices index by index, and get all the subsequent
       elements.
"""
def longest_increasing_subsequents(arr):
    lookup_subsequent_length = {i: 1 for i, e in enumerate(arr)}
    prev_subsequent_index = [None for _ in range(len(arr))]
    i, j = 0, 1
    while j < len(arr):
        left = arr[i]
        right = arr[j]
        if left < right: # left <= right if you want the longest nondecreasing subsequents
            if lookup_subsequent_length[i] >= lookup_subsequent_length[j]:
                lookup_subsequent_length[j] += 1
                prev_subsequent_index[j] = i
        i += 1
        if i == j:
            i = 0
            j += 1
    sorted_keys_by_longer_subsequent = sorted(lookup_subsequent_length,
                                              key=lambda key: lookup_subsequent_length[key],
                                              reverse=True)
    index = sorted_keys_by_longer_subsequent[0]
    subsequents = []
    while True:
        subsequents = [arr[index]] + subsequents
        index = prev_subsequent_index[index]
        if index is None:
            break
        if index == 0:
            subsequents = [arr[index]] + subsequents
            break

    return subsequents

def longest_nondecreasing_subsequents(arr):
    lookup_subsequent_length = {i: 1 for i, e in enumerate(arr)}
    prev_subsequent_index = [None for _ in range(len(arr))]
    i, j = 0, 1
    while j < len(arr):
        left = arr[i]
        right = arr[j]
        if left <= right:
            if lookup_subsequent_length[i] >= lookup_subsequent_length[j]:
                lookup_subsequent_length[j] += 1
                prev_subsequent_index[j] = i
        i += 1
        if i == j:
            i = 0
            j += 1
    sorted_keys_by_longer_subsequent = sorted(lookup_subsequent_length,
                                              key=lambda key: lookup_subsequent_length[key],
                                              reverse=True)
    index = sorted_keys_by_longer_subsequent[0]
    subsequents = []
    while True:
        subsequents = [arr[index]] + subsequents
        index = prev_subsequent_index[index]
        if index is None:
            break
        if index == 0:
            subsequents = [arr[index]] + subsequents
            break

    return subsequents


if __name__ == "__main__":
    arr = [3, 4, -1, 0, 6, 2, 3]
    longest_subsequent = longest_increasing_subsequents(arr)
    print(longest_subsequent)

    arr = [3, 4, -1, 0, 0, 6, 2, 3]
    print(longest_nondecreasing_subsequents(arr))

    arr = [0, 4, 12, 2, 10, 6, 6, 9, 13, 3, 11, 7, 15]
    longest_subsequents = longest_increasing_subsequents(arr)
    print(longest_subsequents)

    arr = [0, 4, 12, 2, 10, 6, 6, 9, 13, 3, 11, 7, 15]
    print(longest_nondecreasing_subsequents(arr))