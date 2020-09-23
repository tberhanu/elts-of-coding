from LinkedList.LL import LL
def delete_this_node(node_to_be_deleted):
    node = node_to_be_deleted
    node.value = node.next.value
    node.next = node.next.next

if __name__ == "__main__":
    ll, b, c, d, e, f, g, h = LL(1), LL(2), LL(3), LL(4), LL(5), LL(6), LL(7), LL(8)
    ll.next, b.next, c.next, d.next, e.next, f.next, g.next, h.next = b, c, d, e, f, g, h, None
    ll.print_all()
    print("After deletion:")
    delete_this_node(b)
    ll.print_all()