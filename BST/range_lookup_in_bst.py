from collections import namedtuple
from BST import sample_bst
Interval = namedtuple('Interval', ('start', 'end'))
def range_lookup_in_bst_driver(tree, interval):
    """
    Write a program that takes as input a BST and an interval and returns the BST keys that lies in the
    interval. For ex. if interval is [16, 31], then return other keys >= 16 and <= 31.
    Brute-force:
        traversing, inorder or preorder or postorder, and get nodes within the range, O(N)
    Strategy using bst property:
        1. If the ROOT is greater than the interval END, call recursively to the right without doing anything.
        2. If the ROOT is less than the interval START, call recursively to the left without doing anything.
        3. Otherwise, the ROOT is DEFINITELY within the range, and the range is distributed on both sides.
           So, we can recursively call both sides while collecting the ROOT.
        4. At last, return the collected ROOTS.

    """
    def range_lookup_in_bst_helper(tree, interval, collector):
        if tree is None:
            return None
        if tree.data > interval.end:
            range_lookup_in_bst_helper(tree.left, interval, collector)
        elif tree.data < interval.start:
            range_lookup_in_bst_helper(tree.right, interval, collector)
        else:
            collector.append(tree.data)
            range_lookup_in_bst_helper(tree.right, interval, collector)
            range_lookup_in_bst_helper(tree.left, interval, collector)

    collector = []
    range_lookup_in_bst_helper(tree, interval, collector)
    return collector

if __name__ == "__main__":
    interval = Interval(start=11, end=37)
    result = range_lookup_in_bst_driver(sample_bst, interval)
    print(result) # [19, 23, 37, 29, 31, 11, 17, 13]
