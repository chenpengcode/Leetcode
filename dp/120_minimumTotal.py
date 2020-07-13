from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        f = [[0] * n for _ in range(n)]
        f[0][0] = triangle[0][0]
        for i in range(1, n):
            f[i][0] = f[i - 1][0] + triangle[i][0]
            for j in range(1, i):
                f[i][j] = min(f[i - 1][j], f[i - 1][j - 1]) + triangle[i][j]
            f[i][i] = f[i - 1][i - 1] + triangle[i][i]
        return min(f[n - 1])

    def minimumTotal_2(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        f = [[0] * n for _ in range(2)]
        f[0][0] = triangle[0][0]

        for i in range(1, n):
            curr, prev = i % 2, 1 - i % 2
            f[curr][0] = f[prev][0] + triangle[i][0]
            for j in range(1, i):
                f[curr][j] = min(f[prev][j - 1], f[prev][j]) + triangle[i][j]
            f[curr][i] = f[prev][i - 1] + triangle[i][i]

        return min(f[(n - 1) % 2])
