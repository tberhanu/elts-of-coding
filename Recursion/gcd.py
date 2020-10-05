def gcd(a, b):
    """
    Hint: Given a < b, gcd(a, b) == gcd(a, b - a) == gc(a, b % a)
    Time: O(log max(a, b)) as in each recursive step, either a or be at least halved.
    Space: O(D) w/r D is the maximum Depth of recursin, O(log max(a, b)), but you can easily converted to iterative
           one and get Space Complexity of: O(1).
    """

    if a > b:
        return gcd(b, a)
    return b if a == 0 else gcd(b % a, a)

print(gcd(12, 16))
print(gcd(48, 88))