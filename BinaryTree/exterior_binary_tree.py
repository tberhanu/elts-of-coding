from BinaryTree.BinaryTreeNode import Tree
from BinaryTree import create_list_of_leaves
def exterior_binary_tree(tree):
    leaves = create_list_of_leaves.create_list_of_leaves(tree)
    tree2 = tree
    lefties = [tree.data]
    righties = []
    while tree:
        if tree.left:
            lefties.append(tree.left.data)
        tree = tree.left

    while tree2:
        if tree2.right:
            righties.append(tree2.right.data)
        tree2 = tree2.right

    result = lefties[:-1] + leaves + righties[:-1]
    return result


if __name__ == "__main__":
    l = Tree("e", 2, Tree("f", 4), Tree("g", 5))
    r = Tree("b", 3, Tree("c", 6), Tree("d", 7))
    tree = Tree("a", 1, l, r)
    result = exterior_binary_tree(tree)
    print(result)