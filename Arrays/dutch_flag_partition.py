def dutch_flag_partition(i, arr):
    """
    Page 39.
    (5.1) The Dutch National Flag Problem:
    Simulating Some part of Quick Sort Algorithm: Arrange number < pivot to the right,
    and number > pivot to the left.
    Time Complexity: O(N)
    Space Complexity: O(1)
    arr = [7, 6, 4, 9, 8, 4, 11, 2]
    i = 1 so that the pivot will be arr[1] which is 6
    result: [2, 4, 4, 6, 7, 9, 8, 11]


    """
    pivot = arr[i]
    j, index = 0, 0
    while j < len(arr):
        if arr[index] > pivot:
            e = arr.pop(index)
            arr.append(e)
        elif arr[index] < pivot:
            e = arr.pop(index)
            arr.insert(0, e)
            index += 1
        else:
            index += 1
        j += 1


    return arr



if __name__ == "__main__":
    arr = [7, 6, 4, 9, 8, 4, 11, 2]
    arr2 = arr[:]
    for i in range(len(arr)):
        print(i, dutch_flag_partition(i, arr))
        arr = arr2[:]