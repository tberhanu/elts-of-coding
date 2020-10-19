from collections import namedtuple
WHITE, BLACK = range(2)
Coordinate = namedtuple('Coordinate', ('x', 'y'))
def search_maze_driver(maze, start, end):
    if search_maze(maze, start, end):
        return paths
    else:
        return []

def search_maze(maze, start, end):
    """
    Consider a black and white digitized image of a maze-white pizels represent open areas and black spaces are walls.
    There are two special white pixels: one is designated the ENTRANCE and the other is the EXIT.
    Given a 2D array of black and white entries representing a maze, Find a way of getting from ENTRANCE to the EXIT.

    Strategy: DFS
    Time: O(|V| + |E|) ????????? Of course, we touched almost all vertices and edges.????
    Space: O(|V|) since we've an array, path, of maximum size of |V|
    """
    if 0 > start.x or start.x >= len(maze) or 0 > start.y or start.y >= len(maze):
        return False

    if maze[start.x][start.y] == BLACK:
        return False

    paths.append(start)
    maze[start.x][start.y] = BLACK
    if start == end:
        return True

    going_left = search_maze(maze, Coordinate(x=start.x, y=start.y - 1), end)
    going_right = search_maze(maze, Coordinate(x=start.x, y=start.y + 1), end)
    going_down = search_maze(maze, Coordinate(x=start.x - 1, y=start.y), end)
    going_up = search_maze(maze, Coordinate(x=start.x + 1, y=start.y), end)

    if not any([going_left, going_right, going_down, going_up]):
        paths.pop()
        return False
    else:
        return True

if __name__ == "__main__":
    matrix = [[WHITE] * 10 for _ in range(10)]
    matrix[0][0], matrix[0][6], matrix[0][7] = BLACK, BLACK, BLACK
    matrix[1][2] = BLACK
    matrix[2][0], matrix[2][2], matrix[2][5], matrix[2][6], matrix[2][8], matrix[2][9] = BLACK, BLACK, BLACK, BLACK, BLACK, BLACK
    matrix[3][3], matrix[3][4], matrix[3][5], matrix[3][8] = BLACK, BLACK, BLACK, BLACK
    matrix[4][1], matrix[4][2] = BLACK, BLACK
    matrix[5][1], matrix[5][2], matrix[5][5], matrix[5][7], matrix[5][8] = BLACK, BLACK, BLACK, BLACK, BLACK
    matrix[6][4] = BLACK
    matrix[7][0], matrix[7][2], matrix[7][4], matrix[7][6] = BLACK, BLACK, BLACK, BLACK
    matrix[8][0], matrix[8][2], matrix[8][3], matrix[8][7], matrix[8][8], matrix[8][9] = BLACK, BLACK, BLACK, BLACK, BLACK, BLACK
    matrix[9][7], matrix[9][8] = BLACK, BLACK
    for mat in matrix:
        print(mat)
    print("____________________________")
    start = Coordinate(x=9, y=0)
    end = Coordinate(x=0, y=9)
    paths = []
    search_maze_driver(matrix, start, end)
    for path in paths:
        print((path.x, path.y))
