# Star Star Question
"""
Take Away: While looping to check for a solution and call the function recursively once you got one solution from the
loop, REMEMBER not to RETURN or JUST CALL the recursive function as this will hinder the ability to loop for other
options in case of the BACKTRACKING. Therefore, call the recursive function within the if ... else close via line# 27.
If things works fine and every time it return TRUE, then the overall all function will finish smoothly.
Otherwise, the function will fix itself via BACKTRACKING i.e. it will get out of the FOR LOOP, and UNDO the previously
filled spots via matrix[i][j] = 0 (line # 30) and will continue the loop for searching the right value.
"""
import math
def solve_sudoku_driver(matrix):
    i, j = 0, 0
    return solve_sudoku(matrix, i, j)

def solve_sudoku(matrix, i, j):
        if j == len(matrix):
            i += 1
            j = 0
            if i == len(matrix):
                return True
        if matrix[i][j] != 0:
            return solve_sudoku(matrix, i, j + 1)

        for val in range(1, len(matrix) + 1):
            if is_valid(val, i, j):
                matrix[i][j] = val
                if solve_sudoku(matrix, i, j + 1): # VITAL STEP so that loop will continue in case of BACKTRACKING !!!
                    return True

        matrix[i][j] = 0 # Vital Step: UNDO previously filled spot while BACKTRACKING since it didn't work.
        return False

def is_valid(val, i, j):
    # Checking if found in the same row
    row = matrix[i]
    if val in row:
        return False
    # Checking if found in the same column
    cols = [matrix[index][j] for index in range(9)]
    if val in cols:
        return False

    # Getting the size of the SMALL BOX inside the matrix
    size = int(math.sqrt(len(matrix)))
    region_i = int(i // size)
    region_j = int(j // size)

    # Getting the BOX INDEX the (i, j) belongs to.
    start_i = 0
    end_i = size
    for region in range(region_i):
        start_i += size
        end_i += size

    start_j = 0
    end_j = size
    for region in range(region_j):
        start_j += size
        end_j += size

    box = [matrix[ii][jj] for ii in range(start_i, end_i) for jj in range(start_j, end_j)]
    # Checking if found in the small BOX.
    if val in box:
        return False
    return True


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
    result = solve_sudoku_driver(matrix)
    print(matrix)

