def is_palindromic(s):
    return s == s[::-1]
def is_palindromic2(s):
    return all(s[i - 1] == s[-1 * i] for i in range(1, len(s)//2 + 1))
def is_palindromic3(s):
    # s[~i] is s[-(i + 1)]
    return all(s[i] == s[~i] for i in range(len(s) // 2))
if __name__ == "__main__":
    print(is_palindromic2("aba") == is_palindromic("aba") == is_palindromic3("aba"))
    print(is_palindromic2("abba") == is_palindromic("abba") == is_palindromic3("aba"))
    print(is_palindromic2("abaa") == is_palindromic("abaa") == is_palindromic3("abaa"))
    print(is_palindromic2("akimika") == is_palindromic("akimika") == is_palindromic3("akimika"))