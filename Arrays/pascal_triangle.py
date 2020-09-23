def generate_pascal_triangle(n):
    """
    Generate pascal triangle of row size N
    Note: This is solved using Dynamic Programming.
    Note: This also solves the COMBINATION problem
    :param n:
    :return:
    """
    # Let's create a normal triangle filled with number 1.
    triangle = [[1] * (i + 1) for i in range(n)]
    print(triangle)
    for i in range(n):
        for j in range(1, i): # skip when i is 0 and 1 as already filled with number 1
            triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]
    return triangle



if __name__ == "__main__":
    triangle = generate_pascal_triangle(6)
    print("Pascal Triangle :", triangle)
    print("5 Combination to 2: ", triangle[5][2])
    print("4 Combination to 3: ", triangle[4][3])