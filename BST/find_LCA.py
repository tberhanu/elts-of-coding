from BST import sample_bst, A, D, K, Z
# from BST import BSTNode
def find_LCA_for_bst_recursively(tree, node1, node2):
    """
    Question: Return the Least Common Ancestor of subtree node1 and subtree node2.
    Assume all entries are DISTINCT.
    Strategy:
        Trick:
            1. If the smallest node is greater than the tree node, both nodes are to the right so go right
            2. If the largest node is smaller than the tree node, both nodes are to the left so go left
            3. Otherwise, node1 and node2 are, then either:
                (i) they are in different direction so STOP, and return the tree, the lca. OR
                (ii) they have EQUAL DATA, so STOP, and return the tree, the lca.

    Time: O(H), w/r H is the Height of the tree as we descend one level with each iteration.
    """

    if node1.data > node2.data:
        return find_LCA_for_bst_recursively(tree, node2, node1)

    if node1.data > tree.data:
        return find_LCA_for_bst_recursively(tree.right, node1, node2)
    elif node2.data < tree.data:
        return find_LCA_for_bst_recursively(tree.left, node1, node2)
    else:
        return tree.data

def find_LCA_for_bst_iteratively(tree, node1, node2):
    if node1.data > node2.data:
        return find_LCA_for_bst_iteratively(tree, node2, node1)

    while node1.data > tree.data or node2.data < tree.data: # Then we know they are in the SAME DIRECTION
        while node1.data > tree.data:
            tree = tree.right
        while node2.data < tree.data:
            tree = tree.left

    return tree.data

if __name__ == "__main__":
    tree = sample_bst
    lca = find_LCA_for_bst_recursively(tree, D, A)
    print(lca) # 19
    lca = find_LCA_for_bst_recursively(tree, D, K)
    print(lca) # 19
    lca = find_LCA_for_bst_recursively(tree, K, A)
    print(lca) # 43
    print("___________")
    tree = sample_bst
    lca = find_LCA_for_bst_iteratively(tree, D, A)
    print(lca)  # 19
    lca = find_LCA_for_bst_iteratively(tree, D, K)
    print(lca)  # 19
    lca = find_LCA_for_bst_iteratively(tree, K, A)
    print(lca)  # 43




