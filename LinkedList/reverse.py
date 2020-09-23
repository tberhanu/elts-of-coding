from LinkedList.LL import LL
def reverse(ll):
    nxt = None
    while ll:
        node = LL(ll.value)
        node.next = nxt
        nxt = node
        ll = ll.next

    return nxt

def reverse_sublist(ll, start, finish):
    a = ll
    for i in range(start - 1):
        ll = ll.next
    b = ll
    c = ll.next
    ll = ll.next
    for i in range(finish - start):
        ll = ll.next
    d = ll
    e = d.next
    d.next = None
    reverse_b = reverse(c)
    rev_b = reverse_b
    while reverse_b.next:
        reverse_b = reverse_b.next
    reverse_b.next = e
    b.next = rev_b
    return a
if __name__ == "__main__":
    # ll = LL(1, LL(2, LL(3, LL(4, LL(5)))))
    # print(ll.print_all2(reverse(ll)))
    ll = LL(11, LL(12, LL(3, LL(5, LL(7, LL(2, LL(8)))))))
    ll.print_all2(reverse_sublist(ll, 1, 4))
    print("border: +++++++++++++++++++++++++++++++")
    ll = LL(11, LL(12, LL(3, LL(5, LL(7, LL(2, LL(8)))))))
    ll.print_all2(reverse_sublist(ll, 2, 4))