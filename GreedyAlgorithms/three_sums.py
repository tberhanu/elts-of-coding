def three_sum(arr, target):
    """
    Design an algorithm that takes as input an array and a number, and determines if there are three entries in the
    array (not necessarily distinct) which add up to the specified TARGET number. Duplication of numbers allowed.
    Ex. [11,, 2, 5, 7, 3] and target = 21, then both [3, 7, 11] and [5, 5, 11] are OK.

    Strategy 1: Triple for loop: Time: O(N * N * N) and Space: O(1)
    Strategy 2: Double for loop: and use HashTable, SET, to check (target - (arr[i] + arr[j])) in HashTable
                Time: O(N * N) and Space: O(N)
    Strategy 3: For Strategy 2, we can avoid the Space used for HashTable SET by using BINARY SEARCH that takes
                O(N log N)
    Strategy 4: Time: O(N) and Space: O(1)
                1. Get start and end pointers on the array, get A as left elt and B as right elt.
                2. Then compare for each elt: if (A + B) == (target - e), Got it so DONE!!!
                3. If (A + B) > (target - e), then decrement the end index
                4. If (A + B) < (target - e), then increment the start index

                N.B: This is like traversing through the array and checking/getting if there are TWO SUMS for
                     a number that is equal to the (TARGET - e), i.e. where e for each elt of the array.
    """
    for e in arr:
        two_sums = two_sum(arr, target - e)
        if two_sums:
            return (f"target={target}", (two_sums[0], two_sums[1], e))
    return False

def three_sum_direct(arr, target):
    arr.sort()
    for e in arr:
        subtarget = target - e
        i, j = 0, len(arr) - 1
        while i <= j:
            summed = arr[i] + arr[j]
            if summed == subtarget:
                return (f"target={target}", (arr[i], arr[j], e))
            elif summed > subtarget:
                j -= 1
            else: # summed < subtarget
                i += 1
    return False


def two_sum(arr, target):
    arr.sort()
    i, j = 0, len(arr) - 1
    while i <= j: # i <= j since DUPLICATION TO BE ALLOWED
        summed = arr[i] + arr[j]
        if summed == target:
            return (arr[i], arr[j])
        elif summed > target:
            j -= 1
        else:
            i += 1

    return False

if __name__ == "__main__":

    arr = [11, 2, 5, 7, 3]
    result = three_sum(arr, 21)
    print(result) # ('target=21', (7, 11, 3))
    result = three_sum_direct(arr, 21)
    print(result) #


    arr = [11, 2, 5, 7]
    result = three_sum(arr, 21)
    print(result) # ('target=21', (5, 11, 5)) Remember DUPLICATION is allowed.
    result = three_sum_direct(arr, 21)
    print(result) #


