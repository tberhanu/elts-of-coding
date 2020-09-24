def square_root(k):
    """
    Question: Given a non negative integer, k , return the largest integer whose square is <= the given integer.
    Ex. K = 300
        17 * 17 = 289 < K=300
        18 * 18 = 324 > K=300
        Therefore, return 17
    Answer: Brute-force is iterating through the numbers and checking if num * num <= K which takes: O(N)
    Using Binary Search Concept: O(log K)
    """
    i = 0
    j = k // 2 # Reducing by half doesn't hurt but efficient!!!
    while i <= j:
        mid = (i + j) // 2
        sq = mid * mid
        # print(sq)
        if sq == k:
            return mid
        if sq > k:
            j = mid - 1
        if sq < k:
            i = mid + 1

    # If K doesn't have perfect sqrt, then j > i >>> return the previous lesser value which is "i - 1"
    return i - 1


if __name__ == "__main__":
    k = 300
    print(square_root(k))

    k = 64
    print(square_root(k))



