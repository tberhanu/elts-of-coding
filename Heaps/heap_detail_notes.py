from itertools import islice
import heapq

"""
    Heap:
        1. minHeap: is the default Heap where the Parent >= Children
           Therefore, heapq.heapfily(lst) will convert the lst into minHeap, not maxHeap
           and heapq.pop(heap) will pop the smallest element from the heap
           Tricky Note: 
                    heapq.heappushpop(heap, e): will push "e", and pop out the SMALLEST element, not the LARGEST.
           Obviously, heap[0] will give the smallest element without popping out.
        2. maxHeap: need customization like
                    (a) for Numbers, multiply by "-1"
                    (b) for objects, define "_lt()_"
                    (c) usually use tuple as heap element with the first tuple element being one
                        that accepts normal Python comparisons like (len(string), string) as shown
                        in the example below.

    Notes:
        Use a heap when all you care about is the LARGEST or SMALLEST elements, and you DO NOT NEED to support fast
        lookup, delete, or search operations for arbitrary elements.
        Tricky Stuffs: heapq.heappushpop(heap, e)
            A heap is a good choice when you need to compute the K LARGEST or K SMALLEST elements in a collection.
            For K LARGEST, use minHeap as you frequently heappushpop() to pop out the smallest and replace with largest
            For K SMALLEST, use maxHeap as you frequently pop out the largest and replace by the smallest

    Libraries:
    1. heapq.heapify(lst) - transforms the elts in lst into a heap in-place
    2. heapq.nlargest(k, lstHeap) - returns the K largest elements in lstHeap
    3. heapq.nsmallest(k, lstHeap) - returns the K smallest elements in lstHeap
    4. heapq.heappush(myheap, elt) - pushes a new element on the heap
    5. heapq.heapop(myheap) - pops the smallest element from the heap
    6. heapq.heappushpop(myheap, elt) - pushes new elt on the heap, and pops out the smallest elt
    7. e = h[0] - returns the smallest element on the heap without popping it out or without deleting.
    Time Complexity:
        Insertion: O(logN)
        Lookup(max/min): O(1)
        Deletion(max/min): O(logN) as it needs rearrangement after deleting the max/min
        Searching arbitrary key: O(N)
"""


def k_longest_strings(k, stream):
    """
    Question: Computer the K LONGEST strings seen so far in the stream of strings.
    Answer: Since dealing with the K LARGEST, minHeap is a good candidate as we replace the min by the newly added elt
    """
    min_heap = [(1, "a") for _ in range(k)]  # k size temporary placeholder lst to be converted to minHeap later
    heapq.heapify(min_heap)
    for string in stream:
        heapq.heappushpop(min_heap, (len(string), string))

    a = [p[1] for p in heapq.nsmallest(k, min_heap)]
    b = [p[1] for p in heapq.nlargest(k, min_heap)]
    return a, b


if __name__ == "__main__":
    stream = ["a", "ab", "abc", "abcd", "abcde", "abcdef", "abcdefg", "abcdefgh", "abcdefghi"]
    k = len(stream)
    a, b = k_longest_strings(k, stream)
    print("k smallest: ", a)
    print("k largest: ", b)
    print("_________________________________")
    """
        Note: Remember k should be equal to the length of the stream to see what you expect.
        If k <= len(stream), then heapq.heappushpop() will pop out the extra smaller elements.
        For ex. if k = len(stream) - 2 = 7, we won't see the smallest elements "a" and "ab".
    """
    stream = ["a", "ab", "abc", "abcd", "abcde", "abcdef", "abcdefg", "abcdefgh", "abcdefghi"]
    k = len(stream) - 2
    a, b = k_longest_strings(k, stream)
    print("k smallest: ", a)
    print("k largest: ", b)


