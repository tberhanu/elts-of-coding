import heapq
def k_largest_without_altering_heap_driver(k, heap):
    myMaxHeap = []
    heapq.heappush(myMaxHeap, heap[0])
    return k_largest_without_altering_heap(k, heap, myMaxHeap)

def k_largest_without_altering_heap(k, heap, myMaxHeap):
    """
    Question: Given an array representing a normal max heap array like [561, 314, 401, 28, 156, 359, 271], design
              an algorithm that computes the K largest elements stored in it WITHOUT MODIFYING it.

    Solution: We can just loop over the HEAP array index i, and collect the children 2i + 1 and 2i + 2 until
              collecting K of them but we are not guaranteed those K of them are all the largest as heap only
              guarantees parent >= children but doesn't guarantees which children branch is greater/less than
              which children. So we are close to the solution but not fully.
              Therefore, better to have our own maxHeap and push our earlier findings to the maxHeap and later
              retrieve the k largest via heapq.nlargest(k, lstHeap).
    """
    i = 0
    while i < len(heap):
        if 2*i + 1 < len(heap):
            heapq.heappush(myMaxHeap, heap[2*i + 1])
        if 2*i + 2 < len(heap):
            heapq.heappush(myMaxHeap, heap[2*i + 2])
        i += 1
    return heapq.nlargest(k, myMaxHeap)

if __name__ == "__main__":
    k = 3
    normal_max_heap_array = [561, 314, 401, 28, 156, 359, 271]
    result = k_largest_without_altering_heap_driver(k, normal_max_heap_array)
    print(result)
    print("++++++++++")
    k = 5
    normal_max_heap_array = [561, 314, 401, 28, 156, 359, 271]
    result = k_largest_without_altering_heap_driver(k, normal_max_heap_array)
    print(result)