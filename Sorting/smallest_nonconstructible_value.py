# Star Question
def smallest_nonconstructible_value(A):
    """
    Given a set of coins, there are some amounts of change that you may not be able to make with them, e.g. you cannot
    create a change amount greater than the sum of your coins. For example, if coins are [1, 1, 1, 1, 1, 5, 10 ,25],
    then the smallest value of change which cannot be made is 21.
    Write a program which takes an array of POSITIVE integers and returns the smallest number which is can not be made
    by the sum of the subset of elements of the array.

    Strategy: 1. Sort it first
              2. If the minimum num is greater than 1, DONE, so return 1
              3. Else, keep adding nums as long as the next num is NOT greater by more than ONE from the SUM so far.
              4. If the next number is greater than the SUM by more than one, then return it as it can't be written
                 as a sum of the previous numbers.
    Time: O(N log N) to Sort, and O(N) to iterate so overall is: O(N log N)
    Space: O(1)
    """
    sum_so_far = 0
    sorted_A = sorted(A)
    for a in sorted_A:
        if a > sum_so_far + 1:
            break
        sum_so_far += a
    return sum_so_far + 1

if __name__ == "__main__":

    A = [1, 1, 1, 1, 1, 5, 10, 25]
    print(smallest_nonconstructible_value(A)) # 21

    A = [1, 1, 3, 5, 11, 23]
    print(smallest_nonconstructible_value(A)) # 22

    A = [1, 2, 4, 5, 10]
    print(smallest_nonconstructible_value(A)) # 23

