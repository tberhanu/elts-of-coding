import random
def kth_largest_element(arr, k):
    """
    Question: Design algorithm for computing the Kth largest element in an array. Assume entries are DISTINCT.
    Proposed Solutions:
        1. Brute-force: O(N log N)
            Sort in decreasing order, O(N log N), and return the k - 1 index element.
        2. Heap: O(N log K) , slightly better than the brute-force solution above.
            Create a minHeap and PUSH each elt of arr until reaching size K, then start PUSH and POP for the
            rest of the element so that the heap will push the new element and pop out the SMALLEST, which
            at last remain a minHeap of size K of the largest elements i.e. O(N log K).
            Then return minHeap[0] which is the Kth largest element.
        3. Smart Way:
            Time Complexity: T(N) = O(N) + T(N/2)

            (1) Assuming our random PIVOT lands the center of the array, every time we have O(N) work to
            be done to REARRANGE the array around the pivot, and then we decrease our N by half.
            T(N) = O(N) + T(N/2)
                 = O(N) + O(N/2) + T(N/4)
                 = O(N) + O(N/2) + O(N/4) + T(N/8) + ... + T(N/N)
                 = O(N) + (N/2 + N/4 + N/8 + .... 0)
                 = O(N) + 1
                 = O(N + 1)
                 = O(N) which is better than Heap as well as Brute-force solution.
            Note: It's NOT O(log N) as each step has a work of O(N) and end up O(N) as proved above.
            (2) In the worst case: O(N * N)
                - If our pivot ALWAYS happen to be the LAST or FIRST ELEMENT.
                T(N) = O(N) + T(N-1)
                     = O(N) + O(N-1) + T(N-2)
                     = O(N) + O(N-1) + O(N-2) + T(N-3) + ....
                     = O(N) + O(N) + O(N) + ...
                     = N * O(N)
                     = O(N * N)
           Space Complexity: O(1) as we REARRANGE the array in-place.
    """
    if k > len(arr):
        return "Invalid Input"
    pivot = random.randint(0, len(arr) - 1)
    while True:
        pivot_value = arr[pivot]
        new_pivot = rearrange_around_pivot(arr, pivot)
        pivot = new_pivot # Since pivot is changed after the rearrangement
        # pivot = arr.index(pivot_value)
        # print(pivot, new_pivot)
        # print(pivot_value, arr)
        righties = arr[pivot + 1:]
        if len(righties) == k - 1:
            return pivot_value
        if len(righties) > k - 1: # solution is located to the right
            pivot = random.randint(pivot + 1, len(arr) - 1)
        if len(righties) < k - 1: # solution is located to the left
            pivot = random.randint(0, pivot - 1)

def rearrange_around_pivot(arr, pivot):
    i = 0
    pivot_value = arr[pivot]
    while i < len(arr):
        e = arr[i]
        if e > pivot_value and i < pivot:
            del arr[i]
            arr.append(e)
            pivot -= 1
        if e < pivot_value and i > pivot:
            del arr[i]
            arr.insert(0, e)
            pivot += 1
        i += 1
    return pivot
if __name__ == "__main__":

    arr = [2, 4, 6, 7, 5, 3, 1]
    result = kth_largest_element(arr, 5)
    print(result) # 3
    result = kth_largest_element(arr, 1)
    print(result) # 7
    result = kth_largest_element(arr, 8)
    print(result)