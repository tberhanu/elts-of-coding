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
