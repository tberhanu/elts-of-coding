from BST.detail_note import BSTNode
from BST import detail_note
def is_binary_tree_bst(tree, low_range=float('-inf'), high_range=float('inf')):
    """
    Strategy 1: Checking left and right, and calling functions recursively
        Time: O(N) as we traverse each of the N Nodes.
        Space: O(H) where H is the BST height(=log N), since we have H RECURSIVE CALLS, I guess.
        Drawback: Even though we found the tree is not a bst at early stage, we still need to finish
                  the recursion for all the nodes.
    Strategy 2: If Inorder traversal, O(N), visits all keys in SORTED ORDER, then it's BST.
    Strategy 3: By searching for violations of BST property in a BFS manner, thereby to reduce the time
                    complexity whene the property is violated at a anode whose depth is small. Page 204, 205


    """
    if not tree:
        return True
    elif not low_range <= tree.data <= high_range:
        return False
    return (is_binary_tree_bst(tree.left, low_range, tree.data) and
           is_binary_tree_bst(tree.right, tree.data, high_range))


if __name__ == "__main__":
    tree1 = BSTNode(99, BSTNode(200), BSTNode(80))
    print(is_binary_tree_bst(tree1)) # False
    tree2 = BSTNode(99, BSTNode(80), BSTNode(200))
    print(is_binary_tree_bst(tree2)) # True

