import bisect
def search_insert(nums, target):
    """
    Given a sorted array of integers and a target number, return the INDEX where the target number is located. If the
    target number is not found inside the array, return the INDEX it is supposed to be inserted.
    Strategy: Whenever we have a sorted collection, and searching an element out of it, the best algorithm is
              Binary Search, O(log N).
              Remember, bisect_left will give us the INDEX of the element that is greater than or equal to the target
              which is the index the target is or is supposed to be (if not there).
              If all the elements are less than the target, then it will return len(nums) which is aslo the index the
              target is supposed to be.
    """
    return  bisect.bisect_left(nums, target)

def myPow(x, n):
    """
    Best Example for Divide and Conquer Technique, and also memoization.
    """

    def helper(x, n, memo):
        if n in memo:
            return memo[n]
        if n == 0:
            return 1
        if n < 0:
            return helper(1/x, -n, memo)
        if n == 1:
            return x

        if n % 2 == 0:
            half = helper(x, n/2, memo)
            half = half * half
            memo[n/2] = half
            return half
        else:
            half = helper(x, (n - 1)/2, memo)
            half = half * half * x
            memo[(n - 1)/2] = half
            return half

    memo = {0: 1}
    return helper(x, n, memo)

if __name__ == "__main__":
    print(myPow(2.00, 1000))
    # 1.0715086071862673e+301
