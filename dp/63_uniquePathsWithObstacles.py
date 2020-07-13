from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or not obstacleGrid[0]:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n] * m
        for i in range(n):
            if obstacleGrid[0][i] == 1:
                dp[0][i] = 0
                break
            else:
                dp[0][i] = 1
        for i in range(m):
            if obstacleGrid[i][0] == 1:
                dp[i][0] = 0
                break
            else:
                dp[i][0] = 1
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]


if __name__ == '__main__':
    obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    solution = Solution()
    print(solution.uniquePathsWithObstacles(obstacleGrid))
