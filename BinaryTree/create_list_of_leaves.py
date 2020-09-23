from BinaryTree.BinaryTreeNode import Tree
def create_list_of_leaves(tree):
    if tree is None:
        return []
    if is_leaf(tree):
        return [tree.data]
    lefty = create_list_of_leaves(tree.left)
    righty = create_list_of_leaves(tree.right)

    return lefty + righty

def is_leaf(tree):
    return tree.left is None and tree.right is None

if __name__ == "__main__":
    l = Tree("e", 2, Tree("f", 4), Tree("g", 5))
    r = Tree("b", 3, Tree("c", 6), Tree("d", 7))
    tree = Tree("a", 1, l, r)
    result = create_list_of_leaves(tree)
    print(result)