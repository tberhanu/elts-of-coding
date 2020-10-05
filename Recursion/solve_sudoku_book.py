import math, itertools

def solve_sudoku(partial_assignment):
    def solve_partial_sudoku(i, j):
        if i == len(partial_assignment):
            i = 0
            j += 1
            if j == len(partial_assignment[i]):
                return True

        if partial_assignment[i][j] != 0:
            return solve_partial_sudoku(i + 1, j)

        def valid_to_add(i, j, val):
            if any(val == partial_assignment[k][j] for k in range(len(partial_assignment))):
                return False
            if val in partial_assignment[i]:
                return False

            region_size = int(math.sqrt(len(partial_assignment)))
            I = i // region_size
            J = j // region_size
            return not any(
                    val == partial_assignment[region_size * I + a][region_size * J + b]
                    for a, b in itertools.product(range(region_size), repeat=2)
            )
        for val in range(1, len(partial_assignment) + 1):
            if valid_to_add(i, j, val):
                partial_assignment[i][j] = val
                if solve_partial_sudoku(i + 1, j):
                    return True
        partial_assignment[i][j] = 0
        return False
    return solve_partial_sudoku(0, 0)

if __name__ == "__main__":
    N = 9
    matrix = [[0 for _ in range(N)] for _ in range(9)]
    matrix[0][0], matrix[0][1], matrix[0][4] = 5, 3, 7
    matrix[1][0], matrix[1][3], matrix[1][4], matrix[1][5] = 6, 1, 9, 5
    matrix[2][1], matrix[2][2], matrix[2][7] = 9, 8, 6
    matrix[3][0], matrix[3][4], matrix[3][8] = 8, 6, 3
    matrix[4][0], matrix[4][3], matrix[4][5], matrix[4][8] = 4, 8, 3, 1
    matrix[5][0], matrix[5][4], matrix[5][8] = 7, 2, 6
    matrix[6][1], matrix[6][6], matrix[6][7] = 6, 2, 8
    matrix[7][3], matrix[7][4], matrix[7][5], matrix[7][8] = 4, 1, 9, 5
    matrix[8][4], matrix[8][7], matrix[8][8] = 8, 7, 9
    # print(matrix)
    result = solve_sudoku(matrix)
    print(matrix)

