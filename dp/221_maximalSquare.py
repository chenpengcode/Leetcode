from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        max_side = 0
        rows, columns = len(matrix), len(matrix[0])

        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == '1':
                    max_side = max(max_side, 1)

                    cur_max_side = min(rows - i, columns - j)

                    for k in range(1, cur_max_side):
                        flag = True
                        if matrix[i + k][j + k] == '0':
                            break

                        for m in range(k):
                            if matrix[i + k][j + m] == '0' or matrix[i + m][j + k] == '0':
                                flag = False
                                break

                        if flag:
                            max_side = max(max_side, k + 1)
                        else:
                            break

        max_square = max_side * max_side
        return max_square

    def maximalSquare_dp(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        max_side = 0
        rows, columns = len(matrix), len(matrix[0])
        dp = [[0] * columns for _ in range(rows)]

        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1

                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

                    max_side = max(max_side, dp[i][j])

        return max_side * max_side

