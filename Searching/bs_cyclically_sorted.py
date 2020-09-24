def search_smallest_from_cyclically_sorted(arr):
    """
    Question: Given a CYCLICALLY SORTED array whose values are all IDENTICAL, get the SMALLEST one.
    Example:
        Input: arr = [5, 6, 7, 8, 9, 1, 2, 3]
        Output: 1

    Brute force: Looping through until getting arr[i - 1] > arr[i], and return arr[i], else return arr[0] which takes
                 in worst scenario(when the arr is normally sorted): O(N)
    Using Binary Search Concept: O(log N)
    Solution below: @Tess break out of the loop if none of the if cases happened
    """
    # i , mid, j
    i = 0
    j = len(arr) - 1
    while i < j:
        mid = (i + j) // 2
        if arr[i] > arr[mid]:
            j = mid # keep it as the arr[mid] is a potential candidate to be the smallest
        elif arr[mid] > arr[j]:
            i = mid + 1 # just increment it as arr[mid] obviously not the smallest one
        else:
            break # breaks out if arr is normally increased array, or if eventually i equals j

    return ("index: ", i, "value: ", arr[i])


if __name__ == "__main__":
    arr = [5, 6, 7, 8, 9, 1, 2, 3]
    print(search_smallest_from_cyclically_sorted(arr))

    arr = [1, 2, 3]
    print(search_smallest_from_cyclically_sorted(arr))
