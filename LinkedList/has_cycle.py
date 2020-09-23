from LinkedList.LL import LL
def has_cycle(ll):
    """
    This solution is based on FLOYD ALGORITHM.
    1. Starting from head, while p steps twice and q steps once, eventually they
       will meet inside the loop if any, otherwise p will reach the NULL value.
    2. If p & q MEET inside the loop, then ptr1 starting from the HEAD and ptr2 starting
       from the MEET point, then it's easily proved that they will meet at the STARTING
       POINT of the LOOP.
    """
    head = ll
    p, q = ll, ll
    while p:
        p = p.next.next
        q = q.next
        if p == q:
            break
    if p:
        print("Loop found")
        p = head
        while True:
            if p == q:
                break
            p = p.next
            q = q.next
        return p
    else:
        print("No loop found")

if __name__ == "__main__":
    a, b, c, d, e, f, g, h = LL(1), LL(2), LL(3), LL(4), LL(5), LL(6), LL(7), LL(8)
    a.next, b.next, c.next, d.next, e.next, f.next, g.next, h.next  = b, c, d, e, f, g, h, d
    result = has_cycle(a)
    if result:
        print(result.value)
    print("++++++++++++++")
    a, b, c, d, e, f, g, h = LL(1), LL(2), LL(3), LL(4), LL(5), LL(6), LL(7), LL(8)
    a.next, b.next, c.next, d.next, e.next, f.next, g.next, h.next = b, c, d, e, f, g, h, None
    result = has_cycle(a)
    if result:
        print(result.value)
