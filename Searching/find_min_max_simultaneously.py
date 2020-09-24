def find_min_max_simultaneously(arr):
    """
    Question: Find the min and max numbers with only N - 1 comparisons.
        Brute-force: Looping through each element and update the min and max values which takes
                     (N - 1) + (N - 1) = 2N - 2 comparisons
    Solution:

    """
    smallest = float("inf")
    largest = float("-inf")
    i = 0
    while i < len(arr) - 1:
        a = arr[i]
        b = arr[i + 1]
        small = min(a, b)
        large = max(a, b)
        if small < smallest: # Note: You will only COMPARE small with the smallest, not with the largest
            smallest = small
        if large > largest: # Note: You will only COMPARE large with the largest, not with the smallest
            largest = large
        i += 2

    if len(arr) % 2 != 0: # Corner Case: If odd len, there is one left over
        smallest = min(smallest, arr[-1])
        largest = max(largest, arr[-1])

    return (smallest, largest)

if __name__ == "__main__":
    arr = [3, 2, 5, 1, 2, 4]
    smallest, largest = find_min_max_simultaneously(arr)
    print("Smallest: ", smallest)
    print("Largest: ", largest)
    print("____________")
    arr = [3, 2, 5, 1, 2, 4, 0]
    smallest, largest = find_min_max_simultaneously(arr)
    print("Smallest: ", smallest)
    print("Largest: ", largest)