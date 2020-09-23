def int_to_str(num):
    unicode_for_zero = ord('0')
    str = ""
    is_neg = True if num < 0 else False
    num = abs(num)
    while num != 0:
        digit = num % 10
        num = num // 10

        unicode_for_num = unicode_for_zero + digit
        chr_repr = chr(unicode_for_num)
        str = str + chr_repr
    str = str[::-1]
    return "-" + str if is_neg else str

def str_to_int(str):
    lst = [int(x) * (10 ** i) for i, x in enumerate(str[::-1])]
    print(lst)
    print(sum(lst))
    return lst

if __name__ == "__main__":
    # result = int_to_str(-879)
    # print(result)
    # print(type(result))
    str_to_int("9876")
