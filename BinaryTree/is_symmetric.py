from BinaryTree.BinaryTreeNode import Tree
def is_symmetric(tree):
    """
    A binary tree is symmetric if you can draw a vertical line through the root and then
    the left subtree is the mirror image of the right subtree.
    """
    return are_symmetric(tree.left, tree.right)

def are_symmetric(tree1, tree2):
    if tree1 is None and tree2 is None:
        return True
    elif tree1 and tree2:
        so_far = tree1.data == tree2.data
        return so_far and are_symmetric(tree1.left, tree2.right) and are_symmetric(tree1.right, tree2.left)
    else:
        return False


def is_leaf(tree):
    return tree.left is None and tree.right is None

if __name__ == "__main__":
    l = Tree("d", 6, None, Tree("e", 561))
    tree = Tree("a", 314, l, Tree("b", 6, Tree("c", 561), None))
    print(is_symmetric(tree))
    l2 = Tree("f", 6, None, Tree("g", 561, None, Tree("h", 3)))
    tree2 = Tree("i", 314, l2, Tree("j", 6, Tree("k", 561), None))
    print(is_symmetric(tree2))
    l3 = Tree("l", 6, None, Tree("m", 2, None, Tree("n", 3)))
    r3 = Tree("o", 6, Tree("p", 2, Tree("q", 3), None), None)
    tree3 = Tree("r", 314, l3, r3)
    print(is_symmetric(tree3))
