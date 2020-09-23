from BinaryTree.BinaryTreeNode import Tree

def is_balanced(tree):
    if tree is None:
        return 0

    lefty = is_balanced(tree.left)
    righty = is_balanced(tree.right)
    if abs(lefty - righty) > 1:
        return 99999
    return max(lefty, righty) + 1


if __name__ == "__main__":
    l = Tree("c", 22, Tree("d", 33, Tree("e", 44), None), Tree("f", 555))
    tree = Tree("a", 11, l, Tree("b", 58, Tree("k", 9, Tree("kk", 99, Tree("kkk", 999)))))
    print(is_balanced(tree)) # False

    # l = Tree("d", 2, Tree("e", 3, Tree("f", 4), None), Tree("g", 55))
    # tree2 = Tree("a", 1, l, Tree("b", 5, None, Tree("c", 99)))
    # print(is_balanced(tree2)) # True