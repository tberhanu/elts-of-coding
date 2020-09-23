from BinaryTree.BinaryTreeNode import Tree
def has_path_sum_driver(tree, k):
    """
    Question: Check if there is a path to the leaf whose data sum is equal to K.
    """
    summ = 0
    return has_path_sum(tree, k, summ)

def has_path_sum(tree, k):
    if tree is None:
        return False
    if is_leaf(tree) and k - tree.data == 0:
        return True

    lefty = has_path_sum(tree.left, k - tree.data)
    righty = has_path_sum(tree.right, k - tree.data)
    if lefty or righty:
        return True
    else:
        return False

def is_leaf(tree):
    return tree.left is None and tree.right is None

if __name__ == "__main__":
    # [619, 591, 901, 1365, 580, 619]
    B = Tree("f", 561, None, Tree("g", 3, Tree("h", 17)))
    lefty = Tree("a", 6, Tree("c", 271, Tree("d", 28), Tree("e", 0)), B)
    C = Tree("k", 1, Tree("l", 401, None, Tree("m", 641)), Tree("n", 257))
    righty = Tree("i", 6, Tree("j", 2, None, C), Tree("o", 271, None, Tree("p", 28)))
    tree = Tree("a", 314, lefty, righty)
    result = has_path_sum(tree, 591)
    print(result) # True
    result = has_path_sum(tree, 619)
    print(result) # True
    result = has_path_sum(tree, 1366)
    print(result) # False