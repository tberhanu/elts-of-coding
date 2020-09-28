def test_collatz_conjecture_driver(num):
    s = {1: 1}
    i = 2
    return test_collatz_conjecture(i, num, s)

def test_collatz_conjecture(i, num, s):
    """
    Coolatz conjecture is: Taking any natural number, and halve it if it's even, or multiply it by 3 and add 1 if it's
                          odd number. If doing this repeatedly will end up in number 1 (neither proved or disproved).

    Question: Test the Collatz conjecture for the first N positive integers.
    Challenge: How will you test for the first billion integers? How will you ACCELERATE the process?
        Hints: 1. Reuse Computation via hashTable just like you did with fibonnaci sequences.
               2. To save time, skip EVEN numbers, since they will be halved, and the resulting number
                  must have already been checked.
               3. Using BIT SHIFTING for Mathematical Operation like multiplication and addition.
               4. Partition the search set and use many computers in PARALLEL.
               Note: Since the numbers in sequence may grow beyond 32-bits, you should use 64-bit integer and
                     keep testing for overflow; alternately, you can use arbitrary precision integers.

    Time Complexity: We can not say much about time complexity beyond the obvious, namely that it is at least
                     proportional to N.
    """
    if i > num:
        return s
    if i in s:
        return s[i]
    ii = i
    while i != 1:
        if i % 2 == 0:
            i = i // 2
        else:
            i = 3 * i + 1
        # print(i)
        if i == 1:
            s[ii] = 1
            print("Number : ", ii, "reached ", 1)

    return test_collatz_conjecture(ii + 1, num, s) # skipping the evens since evens will end up to 1

if __name__ == "__main__":
    num = 7
    result = test_collatz_conjecture_driver(num)
    # print(result)
