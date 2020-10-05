"""
Computer all palindromic decompositions of a given string. For ex, if "0204451881", then decomposition 020, 44, 5, 1881
is palindromic, and also 020, 44, 5, 1, 88, 1. However, 02044, 5, 1881 is not palindromic decomposition.
"""
def palindrome_partitioning_driver(input):
    result = []
    collector = []
    return palindrome_partitioning(input, result, collector)

def palindrome_partitioning(input, result, collector):
    if input == "":
        collector.append(result)

    i = 1
    while i <= len(input):
        if is_palindromic(input[:i]):
            palindrome_partitioning(input[i:], result + [input[:i]], collector)
        i += 1

    return collector


def is_palindromic(input):
    return input == input[::-1]

if __name__ == "__main__":
    input = "0204451881"
    result = palindrome_partitioning_driver(input)
    print(result)
