class Tree:
    """
    Basic Formula for a tree constructed as a list where N is the array index:
         𝑙𝑒𝑓𝑡𝑐ℎ𝑖𝑙𝑑=2𝑛+1
         𝑟𝑖𝑔ℎ𝑡𝑐ℎ𝑖𝑙𝑑=2𝑛+2
    """
    def __init__(self, name=None, data=None, left=None, right=None, sibling=None):
        self.name = name
        self.data = data
        self.left = left
        self.right = right
        self.sibling = sibling

def postorder(root):
    """
    POSTORDER: from LEFT TO RIGHT, but starting from LEFT and RIGHT nodes.
    1st. left node
    2nd. right node
    3rd. center/top node
    """
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data)
def preorder(root):
    """
    PREORDER: from LEFT TO RIGHT, but starting from the TOP or CENTER.
    """
    if root:
        print(root.data)
        preorder(root.left)
        preorder(root.right)
def inorder(root):
    """
    INORDER: is the natural order i.e. from LEFT TO RIGHT starting from LEFT MOST NODE:
    1st. left node
    2nd. center/top node
    3rd. right node
    """
    if root:
        inorder(root.left)
        if root.sibling:
            print(root.data, ">>> sibling: ", root.sibling.data)
        else:
            print(root.data, ">>> sibling: ", None)
        inorder(root.right)

if __name__ == "__main__":
    l = Tree("e", 2, Tree("f", 4), Tree("g", 5))
    r = Tree("b", 3, Tree("c", 6), Tree("d", 7))
    tree = Tree("a", 1, l, r)
    # postorder(tree)
    preorder(tree)
    # inorder(tree)

