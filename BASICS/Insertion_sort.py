def insertion_sort(arr):
    """
    Insertion Sort Algorithm:
    Time: O(N * N) for comparison and swap
    Space: In place: O(1)
    Note: Though it looks slower, it's preferable for smaller collections with <= 15 elements.
          So, Insertion Sort is mostly used together with Merge Sort while dealing with smaller elements sorting.

    """
    for i in range(len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
    return arr


if __name__ == "__main__":
    arr = [9, 6, 2, 3, 4, 9, 0, 4, 5]
    print(insertion_sort(arr))