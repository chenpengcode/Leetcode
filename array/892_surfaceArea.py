from typing import List

'''
题目描述的比较拗口，读懂了还是挺简单的
第一种思路是考虑对每一个立方块相加
第二种思路是把所有立方块的表面积加起来然后减去重叠的部分
'''


class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        row = col = len(grid)

        ans = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j]:
                    ans += 2
                    if i == 0:
                        ans += grid[i][j]
                    else:
                        ans += max(grid[i][j] - grid[i - 1][j], 0)
                    if i == row - 1:
                        ans += grid[i][j]
                    else:
                        ans += max(grid[i][j] - grid[i + 1][j], 0)
                    if j == 0:
                        ans += grid[i][j]
                    else:
                        ans += max(grid[i][j] - grid[i][j - 1], 0)
                    if j == col - 1:
                        ans += grid[i][j]
                    else:
                        ans += max(grid[i][j] - grid[i][j + 1], 0)
        return ans

    def surfaceArea_2(self, grid: List[List[int]]) -> int:
        ans = 0

        row = col = len(grid)

        sum = 0
        cover = 0
        for r in range(row):
            for c in range(col):
                sum += grid[r][c]
                cover += grid[r][c] - 1 if grid[r][c] > 0 else 0
                if r > 0:
                    cover += min(grid[r - 1][c], grid[r][c])
                if c > 0:
                    cover += min(grid[r][c - 1], grid[r][c])
        ans = sum * 6 - cover * 2
        return ans


if __name__ == '__main__':
    test = Solution()
    print(test.surfaceArea_2([[2]]))
    print(test.surfaceArea_2([[1, 2], [3, 4]]))
    print(test.surfaceArea_2([[1, 0], [0, 2]]))
    print(test.surfaceArea_2([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
