# Star Question
from BST import sample_bst
def find_k_largest_in_bst_recursively(tree, k):
    """
    Write a program that takes as input a BST and an interger k, and returns the k largest elements in the BST
    in decreasing order.
    Brute-force: While doing Inorder traversal, collect the Node data like in Queue or Array, and return the last K
                 visited Nodes.
                Time: O(N)
                Drawback: Forced to touch ALL the NODES is a waste especially if K is small and the LEFT subtree is
                          large as when waste our time visiting all the left nodes with small data while we look for
                          the nodes with largest k data.
    Recursive: will solve the above drawback as we start collecting from the largest Node datas, and we can
               stop the search process as we know we collect the K largest values.
               Time: O(H + K) where H is the Height of the tree we go down recursively to the RIGHT, and
                                    K is the Height we go back on recursion while collecting K Node datas.


    """

    def find_k_largest_in_bst_helper(tree):
        if tree and len(k_largest_elements) < k: # Smart: Recursion iff we don't have K largest elements collected
            find_k_largest_in_bst_helper(tree.right)
            if len(k_largest_elements) < k:
                k_largest_elements.append(tree.data)
                find_k_largest_in_bst_helper(tree.left)

    k_largest_elements = []
    find_k_largest_in_bst_helper(tree)
    return k_largest_elements


if __name__ == "__main__":

    result = find_k_largest_in_bst_recursively(sample_bst, 7)
    print(result)