def two_sum(arr, target):
    """
    Given a sorted array of integers, and a target value, get two numbers that adds up to the TARGET.
    Strategy 1: Brute-force: Double for loop checking each and every pair: O(N * N)
    Strategy 2: HashTable: Putting the arr in HashTable or SET, and check if (Target - e) found in HashTable where e
                is each element of the array. O(N) for converting ARR to SET.
    Strategy 3: Use two pointers i.e at index=0 and at index=len(arr)-1, then if the start and end add up to be greater
                than the TARGET, then decrement the end_index; otherwise increment the start_index until getting equal.
                O(N)
    """

    i, j = 0, len(arr) - 1
    while i < j: # i <= j if want to consider DUPLICATION TO BE ALLOWED
        summed = arr[i] + arr[j]
        if summed == target:
            return (arr[i], arr[j])
        elif summed > target:
            j -= 1
        else:
            i += 1

    return False


if __name__ == "__main__":
    arr = [4, 3, 5, 6, 9, 9, -3, -2]
    target = 12
    result = two_sum(sorted(arr), target)
    print(result)
    target = 0
    result = two_sum(sorted(arr), target)
    print(result)
    arr = [3, 5, 6, 9, 9, -3, -2]
    target = 10
    result = two_sum(sorted(arr), target)
    print(result) # Not found since DUPLICATION NOT ALLOWED (while i < j) not (while i <= j)


