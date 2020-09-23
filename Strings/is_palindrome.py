def is_palindrome(str):
    i, j = 0, len(str) - 1
    while i < j:
        if not str[i].isalnum():
            i += 1
            continue
        if not str[j].isalnum():
            j -= 1
            continue
        if str[i].lower() != str[j].lower():
            return False
        i += 1
        j -= 1
    return True


if __name__ == "__main__":
    str = "Able was I, ere I saw Elba"
    print(is_palindrome(str))
    str = "Ray a Ray"
    print(is_palindrome(str))
