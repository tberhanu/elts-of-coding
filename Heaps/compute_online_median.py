import heapq
def compute_online_median(sequence):
    """
    Given a sequence of numbers, you need to output the median after reading in each new element,
    for example :
    Input: sequence = [1, 0, 3, 5, 2, 0, 1]
    Output: online medians = [1, 0.5, 1, 2, 2, 1.5, 1]
            which means: 1 for [1],
                         0.5 for [1, 0],
                         1 for [1, 0, 3],
                         2 for [1, 0, 3, 5],
                         2 for [1, 0, 3, 5, 2],
                         1.5 for [1, 0, 3, 5, 2, 0], and
                         1 for [1, 0, 3, 5, 2, 0, 1]

    Note that the median of a collection divides the collection to two equal parts. When a new
    element is added to the collection, the parts can change by at most one element, and the
    element to be moved is the largest of the smaller half or the smallest of the larger half.
    We can use two heaps, the maxHeap as the LEFT HEAP for the smallest half,
    and the minHeap as the RIGHT HEAP for the largest half.
    """
    minHeap = [] # the RIGHT HEAP to store largest numbers
    maxHeap = [] # the LEFT HEAP to store smallest numbers
    collector = []
    for e in sequence:
        # Let's push e to the minHeap, and then pop out the smallest of all to move to the LEFT HEAP
        smallest = heapq.heappushpop(minHeap, e)
        heapq.heappush(maxHeap, -smallest) # need to negate to use maxHeap
        if len(maxHeap) > len(minHeap):
            largest = heapq.heappop(maxHeap)
            heapq.heappush(minHeap, -largest) # need to neutralize the negation

        if len(maxHeap) == len(minHeap):
            largest_left_num = -maxHeap[0] # Don't forget to neutralize the negation
            smallest_right_num = minHeap[0]
            median_so_far = (largest_left_num + smallest_right_num) * 0.5
        else:
            median_so_far = minHeap[0]

        collector.append(median_so_far)

    return collector


if __name__ == "__main__":
    sequence = [1, 0, 3, 5, 2, 0, 1]
    result = compute_online_median(sequence)
    print(result)





