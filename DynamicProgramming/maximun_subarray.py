# STAR STAR Questions
import itertools
def get_maximum_subarray(arr):
    """
    Strategy: DYNAMIC PROGRAMMING
              Traverse through the arr while getting the maximum amount ending at index 0, 1, 2, ....
              and also keep tracking the largest so far including it's index.
              In the second loop, traverse back starting from the END index of the largest subarray until you reach
              the right amount where you get the START index.

    Time: O(N)
    Space: O(1)
    """
    so_far = arr[0]
    k = 1
    result = [so_far]
    largest = float("-inf")
    end = 0
    while k < len(arr):
        now = arr[k]
        so_far = max(so_far + now, now)
        result.append(so_far)
        if so_far > largest:
            largest = so_far
            end = k
        k += 1
    summed = 0
    start = end
    while summed != largest:
        summed = summed + arr[start]
        start = start - 1
    return result, largest, (start + 1, end)

def get_maximum_subarray_book(arr):
    """
    Strategy: DYNAMIC PROGRAMMING
    Time: O(N)
    Space: O(1)
    """
    min_sum = max_sum = 0
    for running_sum in itertools.accumulate(arr):
        min_sum = min(min_sum, running_sum)
        max_sum = max(max_sum, running_sum - min_sum) # subtraction happens only if min_sum is Negative Value.
    return max_sum

def get_maximum_subarray_using_divide_and_conquer_driver(arr):
    start, end = 0, len(arr) - 1
    return get_maximum_subarray_using_divide_and_conquer(arr, start, end)

def get_maximum_subarray_using_divide_and_conquer(arr, start, end):
    """
    Strategy: DIVIDE AND CONQUER:
        1. Get the mid point and divide the array in two halves.
        2. Lefty: Assume you know the LEFT array's maximum summed subarrays, and
        3. Righty: Assume also you RIGHT array's maximum summed subarrays
        4. Crossy: Then get the maximum subarray ENDING at the END of the LEFT array,
           and also get the maximum subarray STARTING at the START of the RIGHT array.
        5. Then return the max(Lefty, Righty, Crossy)

    Time: O(N log N) just like the QuickSort
    """
    if start == end:
        return arr[0]

    mid = start + (end - start) // 2
    lefty = get_maximum_subarray_using_divide_and_conquer(arr, start, mid)
    righty = get_maximum_subarray_using_divide_and_conquer(arr, mid + 1, end)
    cross = get_max_across_center(arr, mid)

    return max(lefty, righty, cross)


def get_max_across_center(arr, mid):
    left_max = float("-inf")
    summed = 0
    for i in range(mid, -1, -1):
        summed = summed + arr[i]
        if summed > left_max:
            left_max = summed
    right_max = float("-inf")
    summed = 0
    for j in range(mid + 1, len(arr)):
        summed = summed + arr[j]
        if summed > right_max:
            right_max = summed
    return left_max + right_max


if __name__ == "__main__":
    arr = [-9, 8, 2, 3, -4, 8]
    result, largest, index = get_maximum_subarray(arr)
    print(result, "largest: ", largest, "(start, end): ", index)
    print("______")
    print(get_maximum_subarray_book(arr))
    print(get_maximum_subarray_using_divide_and_conquer_driver(arr))
    # start, end = 0, len(arr) - 1
    #     # mid = start + (end - start) // 2
    #     # print("mid: ", mid)
    #     # print(get_max_across_center(arr, mid))