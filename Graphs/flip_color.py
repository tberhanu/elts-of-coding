"""
Given a Boolean 2D array encoding a black and white image.
- Adjacent: Two entries called adjacent if one is to the left, right, above or below the other.
- Path: A path from entry A to entry B is a sequence of Adjacent entries.
- Region: is all the entries connected by Path and having same color.

Question: Given N x M Boolean array A together with a specific Entry (x, y), your task is to flip the color of the
          region associated with Entry (x, y).

Tess Strategy: Recursion like DFS
Time: O(MN) just like DFS
Space: O(V) = O(M + N) as M + N is total vertex count as we use Stack of Recuresive Calls
"""
WHITE, BLACK = range(2)
def flip_color(board, x, y):
    color = board[x][y]
    def flip_color_helper(x, y):
        board[x][y] = 1 - board[x][y]

        if y - 1 >= 0 and board[x][y - 1] == color :
            flip_color_helper(x, y - 1)
        if y + 1 < len(board[x]) and board[x][y + 1] == color:
            flip_color_helper(x, y + 1)
        if x - 1 >= 0 and board[x - 1][y] == color:
            flip_color_helper(x - 1, y)
        if x + 1 < len(board) and board[x + 1][y] == color:
            flip_color_helper(x + 1, y)

    return flip_color_helper(x, y)

if __name__ == "__main__":
    matrix = [[WHITE] * 10 for _ in range(10)]
    matrix[0][0], matrix[0][2], matrix[0][6], matrix[0][7], matrix[0][8], matrix[0][9] = BLACK, BLACK, BLACK, BLACK, BLACK, BLACK
    matrix[1][2], matrix[1][5], matrix[1][8], matrix[1][9] = BLACK, BLACK, BLACK, BLACK
    matrix[2][0], matrix[2][1], matrix[2][2], matrix[2][5], matrix[2][6], matrix[2][8], matrix[2][9] = BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK
    matrix[3][1], matrix[3][3], matrix[3][4], matrix[3][5], matrix[3][6], matrix[3][8] = BLACK, BLACK, BLACK, BLACK, BLACK, BLACK
    matrix[4][0], matrix[4][2], matrix[4][7] = BLACK, BLACK, BLACK
    matrix[5][0], matrix[5][2], matrix[5][5], matrix[5][7], matrix[5][8], matrix[5][9] = BLACK, BLACK, BLACK, BLACK, BLACK, BLACK
    matrix[6][4], matrix[6][6], matrix[6][9] = BLACK, BLACK, BLACK
    matrix[7][0], matrix[7][2], matrix[7][4], matrix[7][6] = BLACK, BLACK, BLACK, BLACK
    matrix[8][0], matrix[8][2], matrix[8][3], matrix[8][7], matrix[8][8], matrix[8][9] = BLACK, BLACK, BLACK, BLACK, BLACK, BLACK
    matrix[9][7], matrix[9][8] = BLACK, BLACK
    print("________ before flip ________")
    for mat in matrix:
        print(mat)
    print("_____________ after first flip_______________")
    x, y = 5, 4
    paths = []
    flip_color(matrix, x, y)
    for mat in matrix:
        print(mat)

    print("_____________ after second flip_______________")
    x, y = 3, 6
    paths = []
    flip_color(matrix, x, y)
    for mat in matrix:
        print(mat)

