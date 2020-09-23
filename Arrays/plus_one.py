def plus_one(arr):
    """
    :param arr: [1, 2, 9]
    :return: [1, 3, 0] after 129 + 1 = 130 >> [1, 3, 0]
    """
    i = len(arr) - 1
    j = i
    r = 0
    while i >= 0:
        e = arr[i] + r + 1 if i == j else arr[i] + r
        r = e // 10
        arr[i] = e % 10 if (i > 0 and e > 9) else e
        # if i > 0 and e > 9:
        #     arr[i] = e % 10
        # else:
        #     arr[i] = e
        i -= 1
    return arr

if __name__ == "__main__":
    arr = [1, 2, 9]
    print(plus_one(arr))
    arr = [9, 9, 9]
    print(plus_one(arr))