def encode(s):
    i = 1
    count = 1
    prev = s[0]
    result = ""
    while i < len(s):
        curr = s[i]
        if curr == prev:
            count += 1
        else:
            result += str(count) + prev
            prev = curr
            count = 1
        i += 1
    result += str(count) + prev

    return result

def decode(s):
    i = 0
    result = ""
    while i < len(s) - 1:
        num = int(s[i])
        letter = s[i+1]
        result += letter * num
        i += 2
    return result



if __name__ == "__main__":
    print(encode("aaabcccaab"))
    print(decode("3e4f2e"))