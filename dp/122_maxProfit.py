from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        dp = [[0] * 2 for _ in range(len(prices))]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
        return dp[len(prices) - 1][0]

    def maxProfit_better(self, prices: List[int]) -> int:
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
