"""
Sorting:
    1. is rearranging a collection of items into increasing or decreasing order.
    2. used to preprocess the collection to make searching faster Ex. Binary search concept is applicable
       only if the array is SORTED.
    3. Naive sorting algorithms run in O(N * N) time.
    4. O(N log N): for heapsort, mergesort, and quicksort where each has it's own adv and disadv.
                   1. Heapsort is in-place but not stable
                   2. Mergesort is stable but not in-place
                   3. Quicksort runs O(N * N) in worst cases.
                   Note: In-place means that uses O(1) space.
                         Stable means sort is one where equal entries appear in their original order.

    5. Insertion: For short arrays like 10 of fewer elements, insertion sort is easier and faster
    6. Heap: If every element is known to be at most k places from its final location, minHeap with O(N log K)
    7. Counting sort: If there are small number of distinct keys like integers in range [0..255]
    8. If there are many duplicate keys we can add the keys to a BST, with linked lists for elements which have the
       same key; then the sorted result can be derived form an in-order traversal of the BST.

    Sort:
        1. sort(key=None, reverse=False):
            Both args are optional.
            key is assumed to be a function to be applied on each elt of the collection.
            If reverse is True, then will sort in descending order.
            This will alter the original array, and will return None.
            arr = [1, 2, 4, 3, 5, 0, 11, 21, 100]
            arr.sort(key=lambda x: str(x))
            arr will be: ['0', '1', '100', '11', '2', '21', '3', '4', '5'] sorted lexicographically as elts are strings.

        2. sorted(key=None, reverse=False):
            arr = [1, 2, 4, 3, 5, 0, 11, 21, 100]
            arr2 = sorted(arr, key=lambda x: str(x))
            Here, arr won't be altered, rather arr2 will be sorted as follows:
            arr2 >> ['0', '1', '100', '11', '2', '21', '3', '4', '5'] sorted lexicographically as elts are strings.

"""
import bisect
def intersect_two_sorted_arrays(A, B):
    """
    Given two sorted arrays, return a new array containing elements that are present in both of the input arrays.
    The input array may have duplicate elements, but returned array should be free of duplicates.

    Strategy 1: O(A*B) as looping over A's elts takes O(A), and also checking if elt is found in array B takes O(B)
    Strategy 2: O(A log B): Since the arrays are already sorted, rather than checking via "a in B" which
                takes O(B), we can use Binary Search that takes O(log B) so that overall time will be O(A log B).
    Strategy 3: O(A + B): Especially if the arrays length are close or similar, we can traverse through both arrays
                and check if the elts are same and save without using "a in B" at all, so we will spend O(1) time
                per input array element so that overall time will be O(A + B).
    """
    r = [a for i, a in enumerate(A) if (i == 0 or A[i] != A[i - 1]) and a in B]
    return r

def intersect_two_sorted_arrays_via_bisect(A, B):
    """
    Improved timing using Binary Search: O(A log B)
    Note to further improve time, we may use the shorted array to the outside of the loop and the longer array to the
    nested loop so that O(log B) effect will maximize.
    """
    if len(A) > len(B):
        return intersect_two_sorted_arrays_via_bisect(B, A) # To take maximum adv of the Binary Search
    def is_present(e):
        index = bisect.bisect_left(B, e)
        return index != len(B) and B[index] == e
    r = [e for i, e in enumerate(A) if (i == 0 or A[i] != A[i - 1]) and is_present(e)]
    return r

def intersect_two_sorted_arrays_strategy_3(A, B):
    """
    Time: O(A + B) as the maximum loop is A + B, and for each loop we only have constant time O(1) comparisons and
          indexing only as we don't have sth like "a in B".
    """

    i, j = 0, 0
    commons = []
    while i < len(A) and j < len(B):
        if A[i] == B[j]:
            if i == 0 or A[i] != A[i - 1]: # skip if it's already treated element
                commons.append(A[i])
            i += 1
            j += 1
        else:
            if A[i] > B[j]: # Skip the array with the smaller elt since it won't be there anymore as it's increasing
                j += 1
            else:
                i += 1
    return commons


if __name__ == "__main__":
    A = [4, 5, 8, 8, 99]
    B = [8, 99]
    print(intersect_two_sorted_arrays(A, B))
    print(intersect_two_sorted_arrays_via_bisect(A, B))
    print(intersect_two_sorted_arrays_strategy_3(A, B))
