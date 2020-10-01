from BST import BSTNode, print_bst_in_preorder_sequence
def build_min_height_bst_from_sorted_array(arr):
    """
    Time: O(N)
    """

    if not arr:
        return None
    mid = len(arr) // 2
    root = arr[mid]
    return BSTNode(root, build_min_height_bst_from_sorted_array(arr[:mid]),
                         build_min_height_bst_from_sorted_array(arr[mid+1:]))
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    bst = build_min_height_bst_from_sorted_array(arr)
    print_bst_in_preorder_sequence(bst)