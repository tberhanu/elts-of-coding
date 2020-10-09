# Start Question
def fibonnaci_stairs_upto_two_steps(N, cache):
    """
    Given N stairs, and you are allowed to step 1 or 2 stairs at a time, then return the total number of ways you have.
    fib(N) = fib(N-1) + fib(N-2)
    with a base case of: fib(0) == 0 and fib(1) == 1
    If the allowed steps are 1 or 2 or 3, then: fib(N) = fib(N-1) + fib(N-2) + fib(N-3)
    With the similar concept, we can work on for k STEPS as shown below.

    So, this is DP problem as you just need a CACHE to store already calculated values.
    """
    if N == 0 or N == 1:
        return 1
    if N < 0:
        return 0
    if N in cache:
        return cache[N]
    result = fibonnaci_stairs_upto_two_steps(N - 1, cache) + fibonnaci_stairs_upto_two_steps(N - 2, cache)
    cache[N] = result
    return result

def fibonnaci_stairs_upto_three_steps(N, cache):
    if N == 0 or N == 1:
        return 1
    if N < 0:
        return 0
    if N in cache:
        return cache[N]
    result = fibonnaci_stairs_upto_three_steps(N - 1, cache) + \
             fibonnaci_stairs_upto_three_steps(N - 2, cache) + \
             fibonnaci_stairs_upto_three_steps(N - 3, cache)
    cache[N] = result
    return result
def number_of_ways_to_climb_stairs_driver(n, k):
    cache = {}
    return number_of_ways_to_climb_stairs(n, k, cache)

def number_of_ways_to_climb_stairs(n, k, cache):
    """
    Question: You are climbing stair. You can advance 1 to K steps at a time. Your destination is exactly N steps up.
              Write a program which takes as inputs N as number of stairs, adn K the maximum number of steps allowed,
              and returns the number of ways in which you can get your destination which is the top of the stair.
    Tess Strategy:
    1. For N, we need to loop over 1, 2, 3 ... k as a starting step, and call recursively for the rest of the stairs.
    2. If we arrive at Stair N == 0, which means reached successfully at the top so return 1 to count it
    3. If we arrive at Stair N < 0, then we should not count that as the combined steps doesn't take us to the top stair.
    4. Whenever we successfully solve for some stair N, we save it in our CACHE to use it later.

    Time: We visit all the N stairs, and for each of them we tried K different STEPS, so O(k * N)
    Space: O(N) as my CACHE is saving values for each of the N Stairs.

    """
    if n < 0:
        return 0
    if n == 0:
        return 1
    if n in cache:
        return cache[n]
    total = 0
    for steps in range(1, k + 1):
        # total = fib(n - 1) + fib(n - 2) + fib(n - 3) + ... + fib(n - k)
        total = total + number_of_ways_to_climb_stairs(n - steps, k, cache)
        cache[n] = total
    return total

if __name__ == "__main__":
    print("The following two functions are doing the same thing: ")
    n, k = 4, 2
    result = number_of_ways_to_climb_stairs_driver(n, k)
    print(result) # 5
    N = 4
    cache = {}
    print(fibonnaci_stairs_upto_two_steps(N, cache))  # 5
    print("The following two functions are doing the same thing: ")
    n, k = 4, 3
    result = number_of_ways_to_climb_stairs_driver(n, k)
    print(result) # 7
    cache = {}
    N = 4
    print(fibonnaci_stairs_upto_three_steps(N, cache)) # 7
