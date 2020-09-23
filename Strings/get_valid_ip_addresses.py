def driver(num):
    """
    This Recursion found to exceed the maximum allowed by Python.
    :param num:
    :return:
    """
    collector = []
    lst = []
    return foo(num, lst, collector)

def foo(num, lst, collector):

    if len(lst) == 3:
        lst.append(num[:])
        ip = ".".join(lst)
        collector.append(ip)


    for i in range(1, 4):
        digit = num[:i]
        if float(digit + ".0") > 255:
            return
        else:
            lst.append(digit)
            foo(num[i:], lst, collector)

    return collector

def get_valid_ip_iteratively(num):
    """
    Since we've 3 loops, and each loop has a max of 4 i.e. 4 ** 4 ** 4 => O(2**32)
    :param num:
    :return:
    """
    lst = []
    i = 1
    while i <= 3:
        d1 = num[:i]
        if float(d1 + ".0") > 255:
            i += 1
            continue
        j = i + 1
        while j <= 6:
            d2 = num[i:j]
            if float(d2 + ".0") > 255:
                j += 1
                continue
            k = j + 1
            while k <= 9:
                d3 = num[j:k]
                d4 = num[k:]
                if len(d4) == 0:
                    k += 1
                    continue
                if float(d3 + ".0") > 255 or float(d4 + ".0") > 255:
                    k += 1
                    continue
                else:
                    ip = d1 + "." + d2 + "." + d3 + "." + d4
                    lst.append(ip)
                k += 1
            j += 1
        i += 1
    return lst

if __name__ == "__main__":
    print(get_valid_ip_iteratively("19216811"))
