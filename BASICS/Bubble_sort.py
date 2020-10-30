def bubble_sort(arr):
    """
    Bubble Sort Algorithm:
    Time: O(N * N)
    Space: O(1)
    """
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            left, right = arr[j], arr[j + 1]
            if left > right:
                arr[j], arr[j + 1] = right, left
            j += 1
    return arr


if __name__ == "__main__":
    arr = [9, 6, 2, 3, 4, 9, 0, 4, 5]
    print(bubble_sort(arr))