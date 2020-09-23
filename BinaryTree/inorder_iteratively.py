from BinaryTree.BinaryTreeNode import Tree
def inorder_iteratively(tree):
    """
    Page 122
    """
    path = []
    result = []
    while tree or path:
        if tree:
            path.append(tree)
            tree = tree.left
        else:
            tree = path.pop()
            e = tree.data
            result.append(e)
            tree = tree.right
    return result


if __name__ == "__main__":
    l = Tree("e", 2, Tree("f", 4), Tree("g", 5))
    r = Tree("b", 3, Tree("c", 6), Tree("d", 7))
    tree = Tree("a", 1, l, r)
    result = inorder_iteratively(tree)
    print(result)



