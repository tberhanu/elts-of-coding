from LinkedList.LL import LL
def remove_duplicates_from_sorted(ll):
    head = ll
    while ll.next:
        if ll.value == ll.next.value:
            ll.next = ll.next.next
        else:
            ll = ll.next

    return head
if __name__ == "__main__":
    ll = LL(1, LL(3, LL(3, LL(6, LL(6, LL(6))))))
    kk = remove_duplicates_from_sorted(ll)
    kk.print_all()
