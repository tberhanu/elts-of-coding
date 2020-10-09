def number_of_ways_from_left_top_to_right_bottom_corner(matrix):
    """
    Write a program that counts how many ways can you go from the top-left to the bottom-right in a 2D array.
    All moves are either RIGHT or DOWN.
    Strategy:
        1. Picking any BOX, the number of ways to reach that particular box is the summation of number of ways to reach
           the box just ABOVE it and the box just to the LEFT of it.
        2. Start by filling the first row and col to be one, as starting form (0, 0), it has only ONE WAY to reach them.

    Time: ????
    Space: O(N * N) as we're using the N by N matrix as our CACHE.
    """
    def fill_matrix_first_row_and_first_col_with_1():
        N = len(matrix)
        matrix[0] = [1 for _ in range(N)]
        for j in range(N):
            matrix[j][0] = 1

    fill_matrix_first_row_and_first_col_with_1()
    for i in range(1, N):
        for j in range(1, N):
            matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]
    return matrix[i][j]
if __name__ == "__main__":
    N = 5
    matrix = [[None for _ in range(N)] for _ in range(N)]
    result = number_of_ways_from_left_top_to_right_bottom_corner(matrix)
    print(result) # 70
    print(matrix)
    print("_________")
    N = 4
    matrix = [[None for _ in range(N)] for _ in range(N)]
    result = number_of_ways_from_left_top_to_right_bottom_corner(matrix)
    print(result) # 20
    print(matrix)
