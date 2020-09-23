from StacksQueues.Tree import Tree
def binary_tree_depth_order_value(tree):
    level = 0
    lst = []
    return get_value_depth_wise(tree, level, lst)

def get_value_depth_wise(tree, level, lst):
    if tree == None:
        return

    value = tree.data
    if len(lst) > level:
        lst[level].append(value)
    else:
        lst.append([value])

    get_value_depth_wise(tree.left, level + 1, lst)
    get_value_depth_wise(tree.right, level + 1, lst)

    return lst

# def get_value_depth_wise_iteratively(tree):
#     lst = []
#     level = 0
#     trees = [tree]
#     while len(trees) > 0:
#         trees2 = []
#         for t in trees:
#             value = t.data
#             if len(lst) > level:
#                 lst[level].append(value)
#             else:
#                 lst.append([value])
#             trees2.append([tr for tr in [t.left, t.right] if tr != None])
#         level += 1
#         trees = trees2[:]
#
#     return lst

if __name__ == "__main__":
    a = Tree(271, Tree(28), Tree(0))
    b = Tree(561, None, Tree(3, Tree(17), None))
    c = Tree(2, None, Tree(1, Tree(401, None, Tree(641)), Tree(257)))
    d = Tree(271, None, Tree(28))
    tree = Tree(314, Tree(6, a, b), Tree(6, c, d))
    # lst = binary_tree_depth_order_value(tree)
    # print(lst)
    lst2 = get_value_depth_wise_iteratively(tree)
    print(lst2)