from LinkedList.LL import LL
def cyclically_right_shift_by_k(ll, k):
    head = ll
    p = ll
    for i in range(k):
        ll = ll.next
    q = ll
    while q:
        save_p = p
        save_q = q
        q = q.next
        p = p.next

    save_p.next = None
    save_q.next = head

    return p

if __name__ == "__main__":
    ll = LL(2, LL(3, LL(5, LL(3, LL(2)))))
    kk = cyclically_right_shift_by_k(ll, 3) # 5, 3, 2, 2, 3
    kk.print_all()
