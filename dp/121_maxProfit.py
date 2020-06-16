from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        dp = [[0] * 2 for _ in range(n)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], -prices[i])
        return dp[n - 1][0]

    def maxProfit_2(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        buy = [0] * n
        sell = [0] * n
        buy[0] = -prices[0]
        for i in range(1, len(prices)):
            buy[i] = max(buy[i - 1], -prices[i])
            sell[i] = max(sell[i - 1], buy[i - 1] + prices[i])

        return sell[-1]

    def maxProfit_better(self, prices: List[int]) -> int:
        if not prices:
            return 0
        sell = 0
        buy = -prices[0]
        for i in range(len(prices)):
            sell = max(sell, buy + prices[i])
            buy = max(buy, -prices[i])

        return sell


if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    solution = Solution()
    print(solution.maxProfit_better(prices))
