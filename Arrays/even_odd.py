def even_odd(arr):
    """
    Page 37.
    Rearranging evens first and odds later.
    Time Complexity: O(N)
    Space Complexity: O(1)
    arr =     [2, 3, 4, 5, 6, 7, 8, 3, 0, 2, 4, 5]
    :returns: [2, 4, 6, 8, 0, 2, 4, 3, 5, 7, 5, 5]
    """
    i, j = 0, 0
    while j < len(arr) - 1:
        if arr[i] % 2 == 0:
            i += 1
        else:
            e = arr.pop(i)
            arr.append(e)
        j += 1
    return arr

def array_propeties():
    import copy
    arr = [9, 8, 7]
    k = arr[::-1]
    print(arr, k)
    arr2 = list(arr)
    arr3 = list(arr)
    d = {1: 2, 3: 4}
    dd = dict.copy(d)
    ddd = arr[:]
    ddd.pop()
    print(dd)
    print(ddd)
    print(arr)
    print(id(arr), id(arr2), id(arr3), id(k))


if __name__ == "__main__":
    # arr = [2, 3, 4, 5, 6, 7, 8, 3, 0, 2, 4, 5]
    # print(even_odd(arr))
    array_propeties()