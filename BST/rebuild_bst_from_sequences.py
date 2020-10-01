from BST import BSTNode
"""
Given the sequence in which keys are visited INORDER traversal of a BST, and all keys are distinct, reconstruct
the BST from the sequence.
Solve the same problem for PREORDER and POSTORDER traversal sequences.

"""
def rebuild_bst_from_inorder(inorder_sequence):
    # IMPOSSIBLE because for multiple bst trees, we may have same inorder sequence
    pass

def rebuild_bst_from_preorder(preorder_sequence):
    """
    Example: [43, 23, 37 29, 31, 41, 47, 53], then the 43 is the ROOT, and [23, 37 29, 31, 41] are the left child
             since they are all less than 43, and also [47, 53] are the right child as they are all greater than or
             equal to the root, 43.
    Time Complexity: Page 209
    Improved Strategy: Page 210
    """
    if not preorder_sequence:
        return None
    root = preorder_sequence[0]
    left_sequence = [e for e in preorder_sequence[1:] if e < root]
    right_sequence = [e for e in preorder_sequence[len(left_sequence) + 1:] if e >= root]
    return BSTNode(root, rebuild_bst_from_preorder(left_sequence),
                         rebuild_bst_from_preorder(right_sequence))


def rebuild_bst_from_postorder(postorder_sequence):
    pass

def print_bst_in_preorder_sequence(tree, preorder_sequence=[]):
    if tree:
        print(tree.data)
        preorder_sequence.append(tree.data)
        print_bst_in_preorder_sequence(tree.left, preorder_sequence)
        print_bst_in_preorder_sequence(tree.right, preorder_sequence)
    return preorder_sequence
if __name__ == "__main__":
    preorder_sequence = [43, 23, 37, 29, 31, 41, 47, 53]
    bst = rebuild_bst_from_preorder(preorder_sequence)
    result = print_bst_in_preorder_sequence(bst)
    print(result)