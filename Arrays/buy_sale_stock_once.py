def buy_and_sell_stock_once(prices):

    maxx = float("-inf")
    i = 0
    while i < len(prices) - 1:
        buy = prices[i]
        sale = max(prices[i+1:])
        profit = sale - buy
        if profit > maxx:
            maxx = profit
        i += 1
    return maxx

def buy_and_sell_stock(prices):
    """
    This solution needs some improvement as it is giving all the profits without restricting
    the buying/selling limit. But if we limit to two need more work.
    :param prices:
    :return:
    """
    i = 0
    collector = []
    while i < len(prices) - 1:
        if prices[i] < prices[i + 1]:
            j = i + 1
            profit = 0
            while j < len(prices):
                if prices[j] > prices[j-1]:
                    profit = profit + prices[j] - prices[j-1]
                    print("Profit: ", profit)
                else:
                    break
                j += 1
            collector.append(profit)
            i = j
        else:
            i += 1
    print("All the profits without buy/sell limit: ", collector)
    return sorted(collector)[-2:]

def get_max_profit(prices):
    i = 0
    max_profit = 0
    smallest = float("inf")
    while i < len(prices):
        if prices[i] < smallest:
            smallest = prices[i]
        profit = prices[i] - smallest
        if profit > max_profit:
            max_profit = profit
        i += 1
    return max_profit

def buy_and_sell_stock_twice(prices):
    """
    This Script of mine works great!!!
    Time: O(N)
    Space: O(N)
    Bonus Question: Try to use O(1) Space.
    """
    collector = []
    for i in range(len(prices)):
        e1 = prices[:i+1]  # Slicing & having prices to the left of day i+1
        profit_on_or_before_day_i = get_max_profit(e1)
        if i + 1 > len(prices) - 1:
            profit_on_or_after_next_day = 0
        else:
            e2 = prices[i+1:]
            profit_on_or_after_next_day = get_max_profit(e2)
        max_profit_on_day_i = profit_on_or_before_day_i + profit_on_or_after_next_day
        collector.append(max_profit_on_day_i)

    return max(collector)




if __name__ == "__main__":
    # prices = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
    # print(buy_and_sell_stock_once(prices))
    prices = [12, 11, 13, 9, 12, 8, 14, 13, 15]
    print("The max profit by selling twice: ", buy_and_sell_stock_twice(prices))
    prices = [12, 11, 13, 9, 12, 8, 14, 13, 15, 18]
    print("The max profit by selling twice: ", buy_and_sell_stock_twice(prices))
    prices = [12, 11, 13, 9, 8, 12, 14, 13, 15]
    print("The max profit by selling twice: ", buy_and_sell_stock_twice(prices))
