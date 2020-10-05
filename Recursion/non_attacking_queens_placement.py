# Star Question
"""
Write a program which returns all distinct Non-attacking Placements of N Queens on an N * N chessboard, where N is an
input to the program.
A Non-attacking placement of queens is one in which no two qeens are in the same row, column or diagonal.

Tess Strategy:
    Here's how to check if the two locations are within the same right or left diagonal.
        1. Given (a, b) if a + b is equal to any other x + y then they are in the same right inclined diagonal.
        2. Given (a, b) if b - a is equal to any other y - x then they are in the same right declined diagonal.

*Much less line of code for the same problem on page 229.
"""
def find_non_attacking_queens_placement_driver(N):
    row = 0
    col = 0
    locations = []
    visited_rows = []
    visited_cols = []

    return find_non_attacking_queens_placement(N, row, col, locations, visited_rows, visited_cols)

def find_non_attacking_queens_placement(N, row, col, locations, visited_rows, visited_cols):
   if len(locations) == N:
       return locations

   for i in range(col, N):
       location = (row, i)
       if is_location_safe(location, locations):
           locations.append(location)
           visited_rows.append(row)
           visited_cols.append(i)
           col = 0
           return find_non_attacking_queens_placement(N, row + 1, col, locations, visited_rows, visited_cols)
   locations.pop()
   prev_row = visited_rows.pop()
   prev_col = visited_cols.pop()
   return find_non_attacking_queens_placement(N, prev_row, prev_col + 1, locations, visited_rows, visited_cols)

def is_location_safe(location, locations):
    visited_rows = [location[0] for location in locations]
    visited_cols = [location[1] for location in locations]
    if location[0] in visited_rows or location[1] in visited_cols:
        return False
    summed_visited = [v[0] + v[1] for v in locations]
    subtracted_visited = [v[1] - v[0] for v in locations]

    if location[0] + location[1] in summed_visited or location[1] - location[0] in subtracted_visited:
        return False
    return True

if __name__ == "__main__":

    result = find_non_attacking_queens_placement_driver(4)
    print(result)

    result = find_non_attacking_queens_placement_driver(5)
    print(result)

    result = find_non_attacking_queens_placement_driver(6)
    print(result)