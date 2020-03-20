class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        if not cost:
            return 0
        if len(cost) == 1:
            return cost[0]

        dp = [0] * len(cost)
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, len(cost)):
            dp[i] = min(dp[i - 2], dp[i - 1]) + cost[i]

        return min(dp[len(cost) - 2], dp[len(cost) - 1])


if __name__ == '__main__':
    cost = [0, 1, 1, 0]
    test = Solution()
    print(test.minCostClimbingStairs(cost))
