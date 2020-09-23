from BinaryTree.BinaryTreeNode import Tree
def preorder_iteratively(tree):
    """
    Page 123
    """
    path = [tree]
    result = []
    while path:
        tree = path.pop()
        if tree:
            print(tree.data)
            result.append(tree.data)
            path = path + [tree.right, tree.left]

    return result

if __name__ == "__main__":
    l = Tree("e", 2, Tree("f", 4), Tree("g", 5))
    r = Tree("b", 3, Tree("c", 6), Tree("d", 7))
    tree = Tree("a", 1, l, r)
    # postorder(tree)
    preorder_iteratively(tree)
    # inorder(tree)

