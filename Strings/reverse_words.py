def reverse_words(statement):
    s = statement.split()
    s.reverse()
    return " ".join(s)

if __name__ == "__main__":
    print(reverse_words("ram is costly"))