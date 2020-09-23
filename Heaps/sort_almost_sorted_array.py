import heapq
def sort_almost_sorted_array(sequence, k):
    """
    Question: Write a program which takes as input a very long 'SEQUENCE' of numbers and prints the
              numbers in sorted order. Each number is at most 'K' away from its correctly sorted
              position. For ex. if sequence = [3, -1, 2, 4, 6, 5, 8], and k = 2, then the first number, 4,
              currently at index 3, can possibly placed at index: 1, 2, 3, 4, or 5 which means +/- k=2
              from the previous index.

    Answer: The brute-force approach is using one of the sorting algorithm: O(N log N), without using the
            advantage of the sequence being almost sorted.
            Best Approach, minHeap:
                Step 1. Since we know the first element is one of the numbers at index 0, 1, or 2,
                        let's create a minHeap and push sequence[:k+1] elements into it.
                Step 2. Then we can use the property of almost sorted property by looping through
                        the rest of the sequences, sequence[k+1:],
                        and do smallest = heapq.heappushpop(min_heap, e) in order to retrieve the
                        smallest elt while pushing the new element from the rest of the
                        until finishing the sequences.
                Step 3. At last, we could get the last k elements left from the minHeap by looping
                        through the minHeap using smallest = heapq.heappop(min_heap)
    Time Complexity: O(N log K) Since we are touching all N elts, and minHeap whose size K takes O(log K)
    Space Complexity: I prefer to use collector so O(N), but we can also just print out each
                      of the smallest withou collecting them so can be O(1) in this case.
    """
    myheap = []
    collector = []
    # Step 1
    for e in sequence[:k+1]:
        heapq.heappush(myheap, e)
    # Step 2
    for e in sequence[k+1:]:
        smallest = heapq.heappushpop(myheap, e)
        collector.append(smallest)
    # Step 3
    while myheap:
        smallest = heapq.heappop(myheap)
        collector.append(smallest)
    return collector


if __name__ == "__main__":
    sequence = [3, -1, 2, 4, 6, 5, 8]
    k = 2
    result = sort_almost_sorted_array(sequence, k)
    print(result)
    sequence = [3, -1, -2, 2, 4, 7, 6, 5, 8]
    k = 3
    result = sort_almost_sorted_array(sequence, k)
    print(result)