"""
In built Binary Search Libraries:
    1. bisect.bisect_left(arr, e): return the first index whose value is >= e, else return len(arr)
        arr = [0, 1, 2, 4]
       bisect.bisect_left(arr, 2): return 2
       bisect.bisect_left(arr, 3): return 3

       num = [0, 1, 2, 2, 2, 2, 4, 5]
       bisect.bisect_left(num, 2): return 2

    2. bisect.bisect_right(arr, e): return the first index whose value is > e, else return len(arr)
        arr = [0, 1, 2, 3]
       bisect.bisect_left(arr, 2): return 3

       num = [0, 1, 1, 5]
       bisect.bisect_left(num, 2): return 3

Question: Given a SORTED ARRAY, use BINARY SEARCH ALGORITHM to search for an element.
Time Complexity: T(n) = T(n/2) + C, so O(log N), but still Binary Search expect the array to be
                 already sorted which may take O(N log N) time.
"""
def binary_search_iterative(e, arr):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2 # the trick to avoid potential overflow
        # mid = (left + right) // 2
        if e > arr[mid]:
            left = mid + 1
        elif e < arr[mid]:
            right = mid - 1
        else:
            return mid
    return -1

def binary_search_recursive_driver(e, arr):
    left_array_size = 0
    return binary_search_recursive(e, arr, left_array_size)

def binary_search_recursive(e, arr, left_array_size):
    if len(arr) == 0:
        return -1
    mid = len(arr) // 2
    if e == arr[mid]:
        return mid + left_array_size
    if e < arr[mid]:
        return binary_search_recursive(e, arr[:mid], left_array_size)
    else:
        left_array_size = len(arr[:mid+1])
        return binary_search_recursive(e, arr[mid + 1:], left_array_size)

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 9, 90, 99, 999]
    e = 5
    print(binary_search_iterative(e, arr)) # 4
    arr = [1, 2, 3, 4, 5, 9, 90, 99, 999]
    e = 55
    print(binary_search_iterative(e, arr)) # -1

    print("+++++++++++")

    arr = [1, 2, 3, 4, 5, 9, 90, 99, 999] # 4
    e = 5
    print(binary_search_recursive_driver(e, arr))
    arr = [1, 2, 3, 4, 5, 9, 90, 99, 999]
    e = 55
    print(binary_search_recursive_driver(e, arr)) # -1
    print("___________")
    arr = [1, 2, 3]
    print(binary_search_recursive_driver(1, arr)) # 0
    arr = [1, 2, 3]
    print(binary_search_recursive_driver(2, arr)) # 1
    arr = [1, 2, 3]
    print(binary_search_recursive_driver(3, arr)) # 2
    arr = [1, 2, 3]
    print(binary_search_recursive_driver(4, arr)) # -1