from LinkedList.LL import LL
def overlapping_list(ll1, ll2):
    saved_ll2 = ll2
    while ll1:
        ll2 = saved_ll2
        while ll2:
            if ll1 == ll2:
                return ll1
            ll2 = ll2.next
        ll1 = ll1.next
    return None

if __name__ == "__main__":
    ll1, b, c, d, e, f, g, h = LL(1), LL(2), LL(3), LL(4), LL(5), LL(6), LL(7), LL(8)
    ll1.next, b.next, c.next, d.next, e.next, f.next, g.next, h.next = b, c, d, e, f, g, h, None
    ll2 = LL(99, LL(88, LL(77, f)))

    node = overlapping_list(ll1, ll2)
    if node:
        print("Here's the overlapped list: ")
        node.print_all()