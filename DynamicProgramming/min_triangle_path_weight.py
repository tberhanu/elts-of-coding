def min_path_weight(triangle):
    """
    Write a program that takes as input a triangle of numbers and returns the weight of a minimum weight path.
    Tess Strategy:
        Once we know the min at row 1, then we will know at row 2, and once we know the min at row 2, we will know the
        min at row 3 without the need of row 1. This concept not only leads us to the Dynamic Programming solution but
        also gives a hint to use a space of O(N) as it's enough to have an array of size N serve as our CACHE, instead
        of the CACHE TABLE, O(N * N).

    Time: 1 + 2 + 3 + ... + N = N (N + 1) / 2 which is O(N ** 2)
    Space: O(N) as we are using an array of size N for our CACHE.
    """
    last_row_size = len(triangle[len(triangle) - 1])
    cache = [float("inf") for _ in range(last_row_size)]
    cache[0] = triangle[0][0]
    temp = cache[:]
    for arr in triangle[1:]:
        for i in range(len(arr)):
            if i - 1 >= 0:
                temp[i] = min(cache[i], cache[i - 1]) + arr[i]
            else:
                temp[i] = cache[i] + arr[i]
        cache = temp[:]
    print(cache)
    return min(cache)

if __name__ == "__main__":
                   #        [2]
                   #      [4, 4]
                   #     [8, 5, 6]
                   #   [4, 2, 6, 2]
                   # [1, 5, 2, 3, 4]

    triangle = [[2],
                [4, 4],
                [8, 5, 6],
                [4, 2, 6, 2],
                [1, 5, 2, 3, 4]]

    result = min_path_weight(triangle)
    print(result) # 15, and the path is 2 > 4 > 5 > 2 > 2