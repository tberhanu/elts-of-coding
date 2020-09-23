def evaluate(rpn_expression):
    """
    input: "3,4,+,2,*,1,+"
    output: 3 + 4 => 7 * 2 => 14 + 1 => 15
    """
    ddict = {"+": lambda x, y: x + y, "-": lambda x, y: x - y,
             "*": lambda x, y: x * y, "/": lambda x, y: x / y}
    lst = rpn_expression.split(",")
    print(lst)
    i = 3
    a, b = int(lst[0]), int(lst[1])
    func = ddict[lst[2]]
    result = func(a, b)
    while i < len(lst) - 1:
        b = int(lst[i])
        func = ddict[lst[i+1]]
        result = func(result, b)
        i += 2

    return result

print(evaluate("3,4,+,2,*,1,+"))


