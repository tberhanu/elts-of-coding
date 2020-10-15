
def change_making(cash):
    """
    Given coins 1, 5, 10, 25, 50, 100 cents, get the minimum number of coins to change the CASH.
    Note: Coin Changing problem is NP-hard, but for some coinage the greedy algorithm is optimum.
    Strategy:
        Once we select the number of coins of a particular COINS value, it NEVER CHANGES that SELECTION which is the
        HALLMARK of Greedy Algorithm.

    Time: O(1) since we only have 6 Iterations regardless of the amount of CASH we have.
    Space: O(1)
    """
    COINS = [100, 50, 25, 10, 5, 1]
    num_coins = 0
    for coin in COINS:
        num_coins += cash / coin
        cash = cash % coin

    return num_coins