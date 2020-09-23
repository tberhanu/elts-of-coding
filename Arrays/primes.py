import math
def is_prime(n):
    if n == 2:
        return True
    if n < 2:
        return False
    i = 2
    while i <= math.sqrt(n):
        if n % i == 0:
            return False
        i += 1
    return True

def list_all_primes_upto(n):
    """
    Getting all the prime numbers upto number N.
    Note: Rather than going through each number upto N and calling is_prime
          function N times, it's much better to get prime numbers and assign
          False for all the other numbers that are multiple of that prime number
          as well as for all the even numbers.
    """
    ddict = {2: True}
    for i in range(3, n+1):
        if i % 2 == 0:
            ddict[i] = False # Assigning False for Even Numbers
        else:
            ddict[i] = True # Assigning True for Odd Numbers
    curr = 3
    while curr <= n:
        if is_prime(curr):
            i = 2
            while i * curr <= n:
                ddict[i * curr] = False
                i += 1
        curr += 2 # Incrementing by 2 since we consider only Odds to be prime.
    return ddict


if __name__ == "__main__":
    # for i in range(10):
    #     print(i, is_prime((i)))

    print(list_all_primes_upto(19))
