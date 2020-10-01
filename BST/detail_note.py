"""
BSTs are a WORKHORSE of data structure and can be used to solve almost every data structures problem reasonalbly
efficiently. They offer the ability to efficiently search for a key as well as find the MIN and MAX elements,
look for the SUCCESSOR or PREDECESSOR of a search key, and enumerate the keys in a range in sorted order.
Unlike sorted array, BST keys can be added to and deleted from a BST EFFICIENTLY.
Rules:
    1. Parent key >= keys stored at the left subtrees
    2. Parent key <= keys stored at the right subtrees

Time: Key lookup, insertion and deletion take time proportional to the height of the tree w/c mostly O(log N), and
      in the worst case O(N).
Space: O(N)

RED-BLACK TREES: are example of HEIGHT-BALANCED BSTs and are widely used in data structure libraries.

Note:???: A common mistake with BSTs is that an object that's present in BST is to updated.....
          As a rule, avoid putting mutable objects in a BST.... Page 201.

* SEARCHING: is the single most fundamental application of BSTs. Unlike hash table, BST offers the ability to find the
             MIN and MAX elements, and find the NEXT LARGEST/NEXT SMALLEST element.

                    Hash table  vs  BST:
Insertion:          O(1)      :    O(log N)
Lookup:             O(1)      :    O(log N)
Inorder Traversal: O(N log N) :    O(N)
For inorder traversal(=iterating through elements in sorted order), hash table need to SORT first, O(N log N).

*** Python DOES NOT come with a built-in BST library.
So let's use THIRD PARTY LIBRARIES:
SORTEDCONTAINERS: for sorted list, set, and dicts. Insert adn deletes is O(N ** 0.5) w/c is smaller than that of
                  the BST, O(log N).
BINTREES: a module that implements sorted sets and sorted dictionaries using balanced BSTs: O(log N)
    functionalities: insert(e) - insert new elt e in the BST
                     discard(e) - removes ...
                     min_item()/max_item() - yield smallest/largest key-value pair in BST
                     pop_min()/pop_max() - remove and return smallest/largest key-value pair in BST

"""
from sortedcontainers import SortedList, SortedDict, SortedSet
import bintrees
class BSTNode:
    def __init__(self, data=None, left=None, right=None):
        self.data, self.left, self.right = data, left, right

def search_bst(tree, key):
    """
    Strategy: As we ignore half of the tree in every step, and spends O(1) time per step/level, total time
              is O(H), where H is the Height of the tree w/c is O(log N).
    """
    if not tree or tree.data == key:
        return tree
    if key >= tree.data:
        return search_bst(tree.left, key)
    else:
        return search_bst(tree.right, key)

A = BSTNode(37, BSTNode(29, None, BSTNode(31)), BSTNode(41))
sample_bst = BSTNode(19, BSTNode(7, BSTNode(3, BSTNode(2), BSTNode(5)),
             BSTNode(11, None, BSTNode(17, BSTNode(13), None))), BSTNode(43, BSTNode(23, None, A), BSTNode(47)))
# if __name__ == "__main__":
#
#     l = BSTNode(9, BSTNode(10), BSTNode(8))
#     r = BSTNode(6, BSTNode(6), BSTNode(5))
#     tree = BSTNode(7, l, r)
#     result = search_bst(tree, 9)
#     print(result.data)
#     if result.left:
#         print(result.left.data)
#     if result.right:
#         print(result.right.data)


# if __name__ == "__main__":
#     print("+++++++++++++++++++++ SortedList: 3rd Party Library +++++++++++++++++")
#     sl = SortedList(['e', 'a', 'd', 'f', 'f', 'k'])
#     for e in sl:
#         print(e)
#     print(sl)
#     print(sl.count('f'))
#     print(sl.count('e'))
#     print(sl[-1])
#     print("________")
#     sd = SortedDict({'c': 3, 'a': 41, 'b': 2})
#     print("sd: ", sd)
#     ss = SortedSet('abracadabra')
#     print("ss: ", ss)
#     index = ss.bisect_left('r')
#     print("r index: ", index)
#     index = ss.bisect_left('zz')
#     print("z index: ", index)


# if __name__ == "__main__":
#     print("################## bintrees as Reb Black Tree and Binary Tree #####################")
#     rbt = bintrees.RBTree([(5, "Alfa"), (2, "Bravo"), (7, "Charlie"), (3, "Delta"), (6, "Echo")])
#     print(rbt[2]) # "Bravo
#     bst = bintrees.BinaryTree([(5, "Alfa"), (2, "Bravo"), (7, "Charlie"), (3, "Delta"), (6, "Echo")])
#     print(bst[2]) # Bravo
#     rbt.insert(9, "Golf")
#     rbt.discard(3)
#     bst.insert(9, "Golf")
#     bst.discard(3)
#     print(rbt)
#     print(bst)
#     print(rbt.pop_max())
#     print(bst.pop_min())
#     print(rbt)
#     print(bst)
#     print("*****")

# if __name__ == "__main__":

