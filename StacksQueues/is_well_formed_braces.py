def is_well_formed(braces):
    """
    input: "{}[]({[]})"
    output: True
    input: "{(})"
    output: False
    """
    lookup = {"}": "{", "]": "[", ")": "("}
    stack = []
    for brace in braces:
        lst = list(lookup.values())
        if brace in lst:
            stack.append(brace)
        else:
            if stack[-1] == lookup[brace]:
                stack.pop()
            else:
                stack.append(brace)

    return len(stack) == 0

if __name__ == "__main__":
    print(is_well_formed("{}[]({[]})"))
    print(is_well_formed("{(})"))
