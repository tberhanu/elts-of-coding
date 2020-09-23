from BinaryTree.BinaryTreeNode import Tree
def postorder_iteratively(tree):
    """
    Done by Tess !!!
    """
    visited = []
    path = [tree]
    result = []
    while len(path) > 0:
        t = path[-1]
        if t not in visited:
            if t.right:
                path = path + [t.right]
            if t.left:
                path = path + [t.left]
            visited.append(t)
        else:
            path.pop()
            result.append(t.data)

    return result

if __name__ == "__main__":
    l = Tree("e", 2, Tree("f", 4), Tree("g", 5))
    r = Tree("b", 3, Tree("c", 6), Tree("d", 7))
    tree = Tree("a", 1, l, r)
    result = postorder_iteratively(tree)
    print(result)
