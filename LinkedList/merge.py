from LinkedList.LL import LL
def merge_two_sorted_lists(ll1, ll2):

    dummy = LL(9999)
    head = dummy

    while ll1 and ll2:
        value1 = ll1.value
        value2 = ll2.value
        if value1 <= value2:
            ll = LL(value1)
            dummy.next = ll
            ll1 = ll1.next
            dummy = dummy.next
        else:
            ll = LL(value2)
            dummy.next = ll
            ll2 = ll2.next
            dummy = dummy.next

    if ll1:
        dummy.next = ll1
    else:
        dummy.next = ll2

    return head.next


if __name__ == "__main__":
    ll1 = LL(1, LL(3, LL(5)))
    ll2 = LL(2, LL(3, LL(4, LL(9))))
    ll = merge_two_sorted_lists(ll1, ll2)
    ll.print_all()