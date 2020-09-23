def roman_to_integer(s):
    """
    Rules:
        1. I can immediately precede V and X
        2. X can immediately preced L and C
        3. C can immediately precede D and M
        4. Back to Back exception s are not allowed liek IXC or CDM
        5. A valid complex Roman number string represents the integer which is the sum of the symbols
        5. For single exceptions add the difference of the larger and smaller i.e IX is (10 - 1 = 9)
    """
    ddict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    i = 1
    num = ddict[s[0]]
    warning = 0
    while i < len(s):
        prev, curr = ddict[s[i-1]], ddict[s[i]]
        if prev < curr:
            num = (num - prev) + (curr - prev)
            warning += 1
            if warning > 1:
                return "INVALID"
        else:
            num = num + curr
            warning = 0
        i += 1

    return num


if __name__ == "__main__":
    print(roman_to_integer("XXXXXIIIIIIIII")) #59
    print(roman_to_integer("LVIIII"))
    print(roman_to_integer("LIX"))
    print(roman_to_integer("IXC"))
    print(roman_to_integer("CDM"))