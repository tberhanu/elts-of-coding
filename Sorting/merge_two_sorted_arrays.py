def merge_two_sorted_arrays(A, B):
    """
    Given two sorted arrays, update the FIRST to the combined entries of the two arrays in sorted order. Assume the
    first array has enough empty entries at it's end to hold the result.
    Challenge: is writing the result back into the first array without repeatedly moving the entries.
    Time: O(A + B)
    Space: O(1)
    """

    b_len = len(B)
    a_len = len(A) - b_len
    i = a_len - 1
    j = b_len - 1
    k = -1
    while i >= 0 and j >= 0:
        a, b = A[i], B[j]
        if a > b:
            A[k] = a
            i -= 1
        else:
            A[k] = b
            j -= 1
        k = k - 1

    while j >= 0:
        A[k] = B[j]
        k -= 1
        j -= 1

    return A


if __name__ == "__main__":
    A = [5, 13, 17, None, None, None, None]
    B = [3, 7, 11, 19]
    result = merge_two_sorted_arrays(A, B)
    print(result)

    A = [2, 5, 13, 17, None, None, None, None]
    B = [3, 7, 11, 19]
    result = merge_two_sorted_arrays(A, B)
    print(result)