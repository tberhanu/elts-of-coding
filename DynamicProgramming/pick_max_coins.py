# Extra Star Question
def maximum_revenue_driver(coins):
    start = 0
    end = len(coins) - 1
    return get_maximum_revenue(coins, start, end)

def get_maximum_revenue(coins, start, end):
    """
    Page 261, 262
    """
    if start > end:
        return 0
    max_by_picking_start = coins[start] + min(get_maximum_revenue(coins, start + 2, end),
                                              get_maximum_revenue(coins, start + 1, end - 1))
    max_by_picking_end = coins[end] + min(get_maximum_revenue(coins, start + 1, end - 1),
                                          get_maximum_revenue(coins, start, end - 2))

    return max(max_by_picking_start, max_by_picking_end)

if __name__ == "__main__":
    coins = [3, 9, 1, 2]
    result = maximum_revenue_driver(coins)
    print("answer: ", result)
    print("_________________________")
    coins = [3, 9, 1, 2, 7]
    result = maximum_revenue_driver(coins)
    print("answer: ", result)
