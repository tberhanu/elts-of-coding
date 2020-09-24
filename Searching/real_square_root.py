import math
def real_square_root(x):
    if x > 1.0:
        left = 1.0
        right = x
    if x < 1.0:
        left = x
        right = 1.0
    while not math.isclose(left, right):
        mid = (left + right) * 0.5
        sq = mid * mid
        # print("sq: ", sq)
        if sq > x:
            right = mid
        if sq < x:
            left = mid
        if sq == x:
            return mid

    # print("left: ", left)
    # print("right: ", right)
    return left

if __name__ == "__main__":
    x = 9
    r = real_square_root(x)
    print(r)
    x = 8
    r = real_square_root(x)
    print(r)
