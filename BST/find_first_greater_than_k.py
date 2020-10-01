from BST.detail_note import BSTNode
from BST import is_binary_tree_bst
from BST import sample_bst
def find_first_greater_than_k(tree, k):
    """
    Given a BST TREE and value K, return the closest number that is greater than K from the BST.
    Strategy:
        If the node value is less than k, COMPLETELY IGNORE IT, and continue searching to the RIGHT, but
        if the node value is greater than k, that is a POSSIBLE CANDIDATE, so save that SUBTREE or VALUE,
        and keep searching to the LEFT in case you get another node with value greater than k but less
        than the previously saved node value, which means if we get another value greater than K but more
        closer to K.

    Time: O(H) where H is the BST tree height, O(log N).
    Space: O(1)
    """
    best_value_so_far = None
    while tree:
        if tree.data > k:
            best_value_so_far = tree.data
            tree = tree.left
        else:
            tree = tree.right
    return best_value_so_far


if __name__ == "__main__":
    bst = BSTNode(990, BSTNode(200, BSTNode(188), BSTNode(299)), BSTNode(1000, BSTNode(999), BSTNode(1001)))
    print(is_binary_tree_bst.is_binary_tree_bst(bst))
    result = find_first_greater_than_k(bst, 299)
    print(result)
    print(is_binary_tree_bst.is_binary_tree_bst(sample_bst))
    print(find_first_greater_than_k(sample_bst, 99))

