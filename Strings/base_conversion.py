def convert_base(num_as_str, b1, b2):
    is_neg = True if num_as_str[0] == "-" else False
    if is_neg:
        num_as_str = num_as_str[1:]
    num = sum(int(e) * (b1 ** i) for i, e in enumerate(num_as_str[::-1]))
    b2_num = ""
    ddict = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
    i = 0
    while num != 0:
        remainder = num % b2
        e = remainder * (b2 ** i)
        if e in ddict:
            e = ddict[e]
        b2_num = str(e) + b2_num
        num = num // b2
    return "-" + b2_num if is_neg else b2_num
if __name__ == "__main__":
    print(convert_base("615", 7, 13))
    print(convert_base("-615", 7, 13))