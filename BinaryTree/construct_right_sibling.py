from BinaryTree.BinaryTreeNode import Tree
from BinaryTree import BinaryTreeNode
def construct_right_sibling(tree):
    """
    Question: Write a program that takes a perfectly binary tree, and sets each node's level-next(=SIBLING)
            field to the node on its right, if one exists.
    Solution: 1. For left child, the sibling is it's parent's right child
              2. For right child, the sibling is it's parent sibling's left child
    """
    lefty = tree.left
    righty = tree.right
    if lefty and righty:
        lefty.sibling = righty
        if tree.sibling and tree.sibling.left:
            righty.sibling = tree.sibling.left
    if tree.left:
        construct_right_sibling(tree.left)
    if tree.right:
        construct_right_sibling(tree.right)

    return tree



if __name__ == "__main__":
    l = Tree("e", 2, Tree("f", 4), Tree("g", 5))
    r = Tree("b", 3, Tree("c", 6), Tree("d", 7))
    tree = Tree("a", 1, l, r)
    tree_with_sibling = construct_right_sibling(tree)
    BinaryTreeNode.inorder(tree_with_sibling)
