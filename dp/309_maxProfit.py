from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        n = len(prices)
        sell = [0] * n
        buy = [0] * n
        rest = [0] * n
        buy[0] = -prices[0]
        for i in range(1, n):
            sell[i] = max(sell[i - 1], buy[i - 1] + prices[i])
            buy[i] = max(buy[i - 1], rest[i - 1] - prices[i])
            rest[i] = max(sell[i - 1], buy[i - 1], rest[i - 1])
        return sell[-1]

    def maxProfit_2(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0
        sell = [0] * n
        buy = [0] * n
        buy[0] = -prices[0]
        buy[1] = max(buy[0], -prices[1])
        sell[1] = max(sell[0], buy[0] + prices[1])
        for i in range(2, n):
            sell[i] = max(sell[i - 1], buy[i - 1] + prices[i])
            buy[i] = max(buy[i - 1], sell[i - 2] - prices[i])
        return sell[-1]

    def maxProfit_better(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0

        buy = -prices[0]
        pre_sell = sell = 0
        for price in prices:
            pre_buy = buy
            buy = max(pre_sell - price, pre_buy)
            pre_sell = sell
            sell = max(pre_buy + price, pre_sell)
        return sell


if __name__ == '__main__':
    prices = [1, 2, 3, 0, 2]
    solution = Solution()
    print(solution.maxProfit_better(prices))
