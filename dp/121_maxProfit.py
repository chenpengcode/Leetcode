from typing import List


class Solution:
    def maxProfit_1(self, prices: List[int]) -> int:
        if not prices:
            return 0
        max_profit = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                max_profit = max(max_profit, prices[j] - prices[i])
        return max_profit

    def maxProfit_dp(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        # 创建两个数组，一个记录每次卖出的最大收益，一个记录每次买入最大收益
        buy = [0] * n
        sell = [0] * n
        buy[0] = -prices[0]
        for i in range(1, n):
            # 第i天卖出收益 = max(第i - 1天卖出收益，第i - 1天买入收益 + 当天股价)
            sell[i] = max(sell[i - 1], buy[i - 1] + prices[i])
            # 第i天买入收益 = max(第i - 1天买入收益，-当天股价)
            buy[i] = max(buy[i - 1], -prices[i])
        return sell[-1]

    def maxProfit_dp_1(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        dp = [[0 for _ in range(2)] for _ in range(n)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], -prices[i])
        return dp[-1][0]

    def maxProfit_dp_2(self, prices: List[int]) -> int:
        if not prices:
            return 0

        n = len(prices)
        sell = 0
        buy = -prices[0]
        for i in range(1, n):
            sell = max(sell, buy + prices[i])
            buy = max(buy, -prices[i])
        return sell

    def maxProfit_greed(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        min_price = prices[0]
        max_profit = 0
        for i in range(1, n):
            max_profit = max(max_profit, prices[i] - min_price)
            min_price = min(min_price, prices[i])
        return max_profit

    # =============================================
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
    print(solution.maxProfit_greed(prices))
