def spiral_order(matrix):
    """
    Page 61.
    (5.18)
    Need some fix:
    matrix1 and matrix2 works fine, but matrix3 is of by one round -- just a lighter fix needed.
    """
    n = len(matrix)
    i, j = 0, 0
    collector = []
    return get_spiral_order(matrix, i, j, n, collector)

def get_spiral_order(matrix, i, j, n, collector):
    ii = i
    jj = j
    if n == 2:
        collector.append(matrix[i][j])
        collector.append(matrix[i][j+1])
        collector.append(matrix[i+1][j+1])
        collector.append(matrix[i+1][j])
        return collector
    if n == 1:
        collector.append(matrix[i][j])
        return collector
    if n == 0:
        return collector

    k = 1
    while k <= 4:
        while (k == 1 and j < n - 1) or (k == 2 and i < n - 1) or (k == 3 and j > 0) or (k == 4 and i > 0):
            e = matrix[i][j]
            if k == 1:
                j += 1
            if k == 2:
                i += 1
            if k == 3:
                j -= 1
            if k == 4:
                i -= 1
            collector.append(e)
        k = k + 1

    return get_spiral_order(matrix, ii+1, jj+1, n-2, collector)

if __name__ == "__main__":
    matrix1 = [
        [1, 2, 3, 33],
        [4, 5, 6, 66],
        [7, 8, 9, 77],
        [4, 5, 6, 7]
    ]
    print(spiral_order(matrix1))

    matrix2 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]
    print(spiral_order(matrix2))

    matrix3 = [
        [1,  2,  3,  4,  5,  6],
        [20, 21, 22, 23, 24, 7],
        [19, 32, 33, 34, 25, 8],
        [18, 31, 36, 35, 26, 9],
        [17, 30, 29, 28, 27, 10],
        [16, 15, 14, 13, 12, 11]
    ]
    print(spiral_order(matrix3))
