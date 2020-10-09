def compute_binomial_coefficients_without_overflow(n, k):
    """
    N combination of K = N! /  k! (N - K)!  is the number of ways to choose a K element subset from an N element set
    whose numerator or denominator OVERFLOWING if INTEGER TYPE is used, even if the final result fits in a 32 bit
    integer.
    Therefore, design an efficient algorithm for computing 'N comb of K' which has the property that it never
    overflow if the final result fits in the integer word size.

    Strategy:
        1. Use formula: N comb K = [(N - 1) comb (K)] + [(N - 1) comb (K - 1)] which leads to recursion
        2. Base Case: if N == k, or K == 0, or K == 1, returns 0, 0, and 1 respectively.

    Time: ???
    Space: ???
    """
    if n == k or k == 0:
        return 1
    if k == 1: # this is optional base case so you can remove it if you want
        return n
    return compute_binomial_coefficients_without_overflow(n - 1, k) + \
           compute_binomial_coefficients_without_overflow(n - 1, k - 1 )

if __name__ == "__main__":
    result = compute_binomial_coefficients_without_overflow(4, 2)
    print(result)
    result = compute_binomial_coefficients_without_overflow(6, 2)
    print(result)