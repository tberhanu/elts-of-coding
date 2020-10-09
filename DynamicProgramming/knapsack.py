from collections import namedtuple
def optimum_object_to_capacity(items, capacity):
    matrix = [[None for _ in range(capacity + 1)] for _ in range(len(items) + 1)]
    fill_matrix_first_row_and_first_col_with_0(matrix, len(matrix), len(matrix[0]))
    # Just a placeholder since index start from 1, not 0, inside the ffing loop. Otherwise need to use items[i - 1]
    items.insert(0, Item(price=0, weight=0))
    for i in range(1, len(matrix)):
        for w in range(1, len(matrix[0])):
            if items[i].weight <= w:
                matrix[i][w] = max(matrix[i - 1][w], matrix[i - 1][w - items[i].weight] + items[i].price)
            else:
                matrix[i][w] = matrix[i - 1][w]

    return matrix[i][w]


def fill_matrix_first_row_and_first_col_with_0(matrix, row, col):
    matrix[0] = [0 for _ in range(col)]
    for j in range(row):
        matrix[j][0] = 0


if __name__ == "__main__":
    Item = namedtuple('Item', ("price", "weight"))
    items = [Item(price=1, weight=2), Item(price=2, weight=3), Item(price=5, weight=4), Item(price=6, weight=5)]
    capacity = 8
    result = optimum_object_to_capacity(items, capacity)
    print(result) # 8