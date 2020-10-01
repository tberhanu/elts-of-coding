class BSTNode:
    def __init__(self, data=None, left=None, right=None):
        self.data, self.left, self.right = data, left, right

def print_bst_in_preorder_sequence(tree, preorder_sequence=[]):
    if tree:
        print(tree.data)
        preorder_sequence.append(tree.data)
        print_bst_in_preorder_sequence(tree.left, preorder_sequence)
        print_bst_in_preorder_sequence(tree.right, preorder_sequence)
    return preorder_sequence

A = BSTNode(37, BSTNode(29, None, BSTNode(31)), BSTNode(41))
Z = BSTNode(53)
K = BSTNode(47, None, Z)
D = BSTNode(11, None, BSTNode(17, BSTNode(13), None))
sample_bst = BSTNode(19, BSTNode(7, BSTNode(3, BSTNode(2), BSTNode(5)), D),
             BSTNode(43, BSTNode(23, None, A), K))

"""
                                          19
                                        
                            7                                     43
                                                     
                                                     23                          47=K
                    3            11=D
                                                           37=A                            53
                2      5              17              29           41
                                                 
                                13                        31
"""