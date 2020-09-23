def multiply(arr1, arr2):
    """
    Page 43.
    (5.3):
    :param arr1: [1, 2, 3]
    :param arr2: [4, 5, 6]
    :return: 123 * 456 = 56088
    """
    num1 = 0
    ii = 0
    for i in range(len(arr1) - 1, -1, -1):
        num1 = num1 + arr1[ii] * (10 ** i)
        ii += 1
    num2 = 0
    jj = 0
    for i in range(len(arr2) - 1, -1, -1):
        num2 = num2 + arr2[jj] * (10 ** i)
        jj += 1
    print("num1: ", num1, "num2: ", num2)
    print("num1 * num2: ", num1 * num2)

if __name__ == "__main__":
    arr1 = [1, 2, 3]
    arr2 = [4, 5, 6]
    print(123*456)
    multiply(arr1, arr2)