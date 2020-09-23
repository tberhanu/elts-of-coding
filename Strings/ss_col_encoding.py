def ss_column_encoding(col):
    """
    A, B, C, ..., X, Y, Z, AA, AB, ..., ZZ, AAA, AAB ...
    Assume A stands for 1, B for 2, Z for 26, AA for 27, and ZZ for 702

    Solution: is using base 26
    """
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    char_map_num = {char: i+1 for i, char in enumerate(letters)}
    print(char_map_num)
    result = sum(char_map_num[e] * (26 ** i) for i, e in enumerate(col[::-1]))
    return result
if __name__ == "__main__":
    print(ss_column_encoding("ZZ"))
