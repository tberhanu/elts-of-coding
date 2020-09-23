def look_and_say(n):
    s = "1z" # Smart initialization to avoid indexing problem when dealing with index: i and i + 1
    collector = ['1']
    for i in range(n - 1):
        j = 0
        count = 1
        ss = ""
        while j < len(s) - 1:
            if s[j] == s[j + 1]:
                count += 1
                j += 1
            else:
                ss = ss + str(count) + s[j]
                count = 1
                j += 1
        s = ss + "z"
        collector.append(s[:-1])

    return collector

if __name__ == "__main__":
    print(look_and_say(8))