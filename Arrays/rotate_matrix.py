import copy
def rotate_brute_force(matrix):
    """
    Page 64
    (5.19) Write a function that takes as input an n*n 2D array,
    and rotates the array by 90 degrees clockwise.
    Note: This solution uses extra space - brute force
    :param matrix:
    :return:
    """
    mat = copy.deepcopy(matrix)
    N = len(matrix)
    for i in range(N):
        for j in range(N):
            mat[i][j] = matrix[N-1-j][i]
    return mat

def rotate_in_place(matrix):
    """
    In place:
    1. First Transpose the matrix
    2. Then swap the columns for ex. if 4 columns, then swap 1st and 4th, and 2nd and 3rd.
        if 3 columns, then only swap 1st and 3rd columns.
    """
    # Let's transpose the matrix
    N = len(matrix)
    print("original matrix: ", matrix)

    for i in range(N):
        for j in range(i, N, 1):
            temp = matrix[j][i]
            matrix[j][i] = matrix[i][j]
            matrix[i][j] = temp

    print("transposed matrix: ", matrix)
    col1, col2 = 0, N - 1
    while col1 < col2:
        for row in range(N):
            matrix[row][col1], matrix[row][col2] = matrix[row][col2], matrix[row][col1]
        col1 += 1
        col2 -= 1
    return matrix
if __name__ == "__main__":
    matrix1 = [
        [1,  2,  3,  4],
        [5,  6,  7,  8],
        [9,  10, 11, 12],
        [13, 14, 15, 16]
    ]
    print("rotated brute force: ", rotate_brute_force(matrix1))
    print("rotated in place: ", rotate_in_place(matrix1))
    print("___________________________")
    matrix2 = [[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]]
    print("rotated brute force: ", rotate_brute_force(matrix2))
    print("rotated in place: ", rotate_in_place(matrix2))
    print("___________________________")

    matrix3 = [
        [1,  2,  3,  4,  5,  6],
        [20, 21, 22, 23, 24, 7],
        [19, 32, 33, 34, 25, 8],
        [18, 31, 36, 35, 26, 9],
        [17, 30, 29, 28, 27, 10],
        [16, 15, 14, 13, 12, 11]
    ]
    print("rotated brute force: ", rotate_brute_force(matrix3))
    print("rotated in place: ", rotate_in_place(matrix3))
