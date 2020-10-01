import bintrees
from collections import Counter
def most_visited_pages(file):
    """
    Here's below a simpler solution of mine using hash table, but there is also another suggested
    strategy using BST and Hash table on page 214.
    :param file:
    :return:
    """
    chars = file.split(",")
    x = Counter(chars)
    c = {k: v for k, v in sorted(x.items(), key=lambda item: item[1], reverse=True)}
    result = []
    for k, v in c.items():
        result.append(k)
    return result

if __name__ == "__main__":
    # bst = bintrees.BinaryTree([(5, "Alfa"), (2, "Bravo"), (7, "Charlie"), (3, "Delta"), (6, "Echo")])
    file = "a,b,c,c,c,c,b,a,d,d,d"
    r = most_visited_pages(file)
    print(r)