def search_sorted_matrix(matrix, num):
    """
    Question: Given a sorted 2D array, matrix, search for NUM
    SORTED MATRIX: means each ROW is increasing, and each COL is increasing
    Solution:
        Brute-force approach of looping thru the double array takes O(N * N)
        Smart approach is:
            1. Grab the TOP RIGHT element, and return the indexes if it is equal to the NUM
            2. If NUM is greater than the TOP RIGHT element, then the number we are searching
               won't be in that row, so remove that row by incrementing index i.
            3. If NUM is less than the TOP RIGHT element, then the number we are searching
               won't be in that col, so remove that col by decrementing index j.
            4. If row index i > len(matrix) or col index j < 0, then NUM is not found in
               the MATRIX, so return (-1, -1)

            Time Complexity: O(row + col) since every step, we do one comparison to remove one row or one col
                            so in the worst situation we remove all row/col and left with empty matrix.
    """
    row = len(matrix)
    col = len(matrix[0])
    i, j = 0, col - 1
    while i < row and j >= 0:
        corner = matrix[i][j]
        if num == corner:
            return (i, j)
        elif num > corner: # can't find in that row, so remove it
            i += 1
        else: # can't find in that col, so remove it
            j -= 1
    return (-1, -1)


if __name__ == "__main__":
    matrix = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]]
    result = search_sorted_matrix(matrix, 11)
    print(result)
    result = search_sorted_matrix(matrix, 1)
    print(result)
    result = search_sorted_matrix(matrix, 16)
    print(result)
    result = search_sorted_matrix(matrix, 99)
    print(result)

