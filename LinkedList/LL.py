class LL:
    """
    1. Linked List problems often have a simple brute force solution that uses O(N) space.
    2. Mostly conceptually simple, and is more about cleanly coding what is specified, rather
       than designing an algorithm.
    3. Consider using DUMMY HEAD
    4. For singly linked lists, often take advantage of TWO ITERATORS or TWO POINTERS one ahead of
       the other, or one stepping forward quicker than the other.


       Question: Why Linked List? Real life implementation?
       Answer: Anything chain one another like train, BART.
    """
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    def search_list(self, ll, value):
        while ll:
            if ll.value == value:
                return ll
            ll = ll.next
        return ll
    def insert_node_after_head(self, node):
        node.next = self.next
        self.next = node

    def delete_node_after(self, node):
         node.next = node.next.next

    def print_all(self):
        while self:
            print(self.value)
            self = self.next

    def print_all2(self, node):
        while node:
            print(node.value)
            node = node.next

if __name__ == "__main__":
    ll = LL(1, LL(2, LL(3)))
    ll.print_all()
    print("------")
    ll2 = LL(99)
    ll.insert_node_after_head(ll2)
    ll.print_all()
    print("_____")
    ll.delete_node_after(ll)
    ll.print_all2(ll)



