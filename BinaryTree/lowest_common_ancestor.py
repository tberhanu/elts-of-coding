from BinaryTree.BinaryTreeNode import Tree
def lca_driver(tree, node1, node2):
    if tree == node1 or tree == node2:
        return tree
    return lca(tree, node1, node2)

def lca(tree, node1, node2):
    """
    The lowest common ancestor(LCA) of any two nodes in a binary tree is the
    node furthest from the root that is an ancestor of both nodes.

    Note: Reference for this tree is on page 113.

    Strategy:
        1. Call recursively for the left tree and right tree back to back.
        2. If we found the node on the way, then it will return it, otherwise the recursion will continue
           until reaching the end where it will return None.
        3. As a result, even though most of the branches return None after bouncing back from the end,
           we definitely will have two of the branches returning the NODE.
        4. The Node that recieved from it's right and left branch other than None, then that's the LCA Node.

    """
    if tree == node1 or tree == node2:
        return tree
    if tree is None:
        return None
    lefty = lca(tree.left, node1, node2)
    righty = lca(tree.right, node1, node2)
    if lefty and righty:
        print("We found the common ancestor")
        return tree
    if lefty:
        return lefty
    if righty:
        return righty

def is_leaf(tree):
    return tree.left is None and tree.right is None


if __name__ == "__main__":
    """
    Note: Reference for this tree is on page 113.
    """
    B = Tree("f", 561, None, Tree("g", 3, Tree("h", 17)))
    lefty = Tree("a", 6, Tree("c", 271, Tree("d", 28), Tree("e", 0)), B)
    C = Tree("k", 1, Tree("l", 401, None, Tree("m", 641)))
    righty = Tree("i", 6, Tree("j", 2, None, C), Tree("o", 271, None, Tree("p", 28)))
    tree = Tree("a", 314, lefty, righty)

    result = lca_driver(tree, B, C)
    print(result.data)
    print("+++++++++++++")
    B = Tree("f", 561, None, Tree("g", 3, Tree("h", 17)))
    lefty = Tree("a", 6, Tree("c", 271, Tree("d", 28), Tree("e", 0)), B)
    node1 = Tree("l", 401, None, Tree("m", 641))
    C = Tree("k", 1, node1)
    node2 = Tree("p", 28)
    righty = Tree("i", 6, Tree("j", 2, None, C), Tree("o", 271, None, node2))
    tree = Tree("a", 314, lefty, righty)

    result = lca_driver(tree, node1, node2)
    print(result.data)

