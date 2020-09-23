def first_occurence_of_substring(string, substr):
    if len(string) < len(substr):
        return -1
    if len(string) == len(substr):
        return 0 if string == substr else -1
    return foo(string, substr)

def foo(string, substr):

    i = 0
    size = len(substr)
    while i < len(string):
        if string[i:i + size] == substr:
            return i
        i += 1
    return -1

if __name__ == "__main__":
    print(first_occurence_of_substring("statement", "men"))

