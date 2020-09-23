from BinaryTree.BinaryTreeNode import Tree
def sum_root_to_leaf_driver(tree):
    summ = 0
    lst = []
    return sum_root_to_leaf(tree, summ, lst)
def sum_root_to_leaf(tree, summ, lst):
    if tree is None:
        return
    if is_leaf(tree):
        lst.append(summ + tree.data)
    else:
        sum_root_to_leaf(tree.left, summ + tree.data, lst)
        sum_root_to_leaf(tree.right, summ + tree.data, lst)
    return lst


def is_leaf(tree):
    return tree.left is None and tree.right is None

if __name__ == "__main__":
    B = Tree("f", 561, None, Tree("g", 3, Tree("h", 17)))
    lefty = Tree("a", 6, Tree("c", 271, Tree("d", 28), Tree("e", 0)), B)
    C = Tree("k", 1, Tree("l", 401, None, Tree("m", 641)), Tree("n", 257))
    righty = Tree("i", 6, Tree("j", 2, None, C), Tree("o", 271, None, Tree("p", 28)))
    tree = Tree("a", 314, lefty, righty)
    lst = sum_root_to_leaf_driver(tree)
    print(lst)

