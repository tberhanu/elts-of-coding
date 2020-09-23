from LinkedList.LL import LL
def kth_node_from_tail(ll, k):
    p = ll
    for i in range(k):
        ll = ll.next
    q = ll
    while q:
        p = p.next
        q = q.next
    return p

if __name__ == "__main__":
    ll = LL(1, LL(2, LL(3, LL(4, LL(5, LL(6))))))
    p = kth_node_from_tail(ll, 4)
    print(p.value)