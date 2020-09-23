def delete_duplicates(arr):
    """
    Page 45.
    (5.5) Deleting repeated elements from a sorted array
    :param arr: [2, 3, 5, 5, 7, 11, 11, 11, 13]
    :return: [2, 3, 5, 7, 11, 13, 0, 0, 0]
    Time: O(N)
    Space: O(1)

    """
    if len(arr) == 1:
        return arr
    i, j, k = 0, 1, 0
    length = len(arr)
    while k < length - 1:
        k += 1
        if arr[i] == arr[j]:
            del arr[i]
            arr.append(0)
        else:
            i += 1
            j += 1
    return arr
if __name__ == "__main__":
    arr = [2, 3, 5, 5, 7, 11, 11, 11, 13]
    print(delete_duplicates(arr))