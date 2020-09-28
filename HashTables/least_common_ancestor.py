def get_lca(node1, node2):
    """
    Question: Design algorithm for computing LCA of two nodes in a Binary Tree, assuming we have access to the PARENT
              of the NODE.
    Solution: Since we have access to the PARENT of the NODES, we can start from each NODE and keep going upward while
              saving the visited NODE in a set. But before saving to the set, we need to check if that NODE is already
              saved, and if so, then it means the other NODE already pass through that NODE which makes that NODE the
              LCA of both nodes.

    Time: In worst case: O(H) where H is Height of the Tree.
    """
    path_from_node_to_root = set()
    while node1 or node2:
        if node1 in path_from_node_to_root:
            return True, node1
        else:
            path_from_node_to_root.add(node1)
            node1 = node1.parent

        if node2 in path_from_node_to_root:
            return True, node2
        else:
            path_from_node_to_root.add(node2)
            node2 = node2.parent

    return False, None
