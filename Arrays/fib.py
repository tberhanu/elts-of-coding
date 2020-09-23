def fib_recursive(n):
    memo = {1: 1, 2: 1}
    return fib(n, memo)
def fib(n, memo):
    """
    Dynamic Programming: Recursive and Memoization
    Time: O(N)
    """

    if n in memo:
        return memo[n]
    result = fib(n-1, memo) + fib(n-2, memo)
    memo[n] = result
    return result

def fib_bottom_up(n):
    """
    Dynamic Programming: Bottom-up and memoization
    Time: O(N)
    """
    if n == 1 or n == 2:
        return 1
    memo = {1: 1, 2: 1}
    for i in range(3, n+1):
        memo[i] = memo[i-1] + memo[i-2]

    return memo[n]

def fib_naive(n):
    """
    Time: O(2**N)
    """
    if n == 1 or n == 2:
        return 1
    else:
        return fib_naive(n-1) + fib_naive(n-2)

if __name__ == "__main__":
    n = 9
    print(fib_naive(n))
    print(fib_bottom_up(n))
    print(fib_recursive(n))
