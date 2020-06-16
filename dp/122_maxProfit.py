from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        n = len(prices)
        sell = [0] * n
        buy = [0] * n
        buy[0] = -prices[0]
        for i in range(1, n):
            sell[i] = max(sell[i - 1], buy[i - 1] + prices[i])
            buy[i] = max(buy[i - 1], sell[i - 1] - prices[i])
        return sell[-1]

    def maxProfit_better(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        sell = 0
        buy = -prices[0]
        for i in range(n):
            t = sell
            sell = max(sell, buy + prices[i])
            buy = max(buy, t - prices[i])
        return sell


if __name__ == '__main__':
    prices = [1, 2, 3, 4, 5]
    solution = Solution()
    print(solution.maxProfit_better(prices))
