def fill_surrounded_regions(board):
    n, m = len(board), len(board[0])
    row_edges = {(i, j) for k in range(n) for (i, j) in ((k, 0), (k, m - 1))} # outer loop ... inner loop
    col_edges = {(i, j) for k in range(m) for (i, j) in ((0, k), (n - 1, k))}
    edges = row_edges.union(col_edges)
    # inner loop ... outer loop
    board[:] = [["Black" if (row, col) not in edges else board[row][col] for col in range(n)] for row in range(m)]


if __name__ == "__main__":
    N = 4
    board = [["Black"] * N for _ in range(N)]
    board[1][0], board[1][2] = "White", "White"
    board[2][1], board[2][2] = "White", "White"
    print("_________ before operation ________")
    for b in board:
        print(b)

    fill_surrounded_regions(board)
    print("_________ after operation __________")
    for b in board:
        print(b)

