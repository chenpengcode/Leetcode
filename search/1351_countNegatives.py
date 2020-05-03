from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ans = 0
        for i in range(len(grid)):
            left, right = 0, len(grid[0]) - 1
            pos = -1

            while left <= right:
                mid = left + (right - left) // 2
                if grid[i][mid] < 0:
                    right = mid - 1
                    pos = mid
                else:
                    left = mid + 1

            if pos > -1:
                ans += len(grid[0]) - pos

        return ans

    def countNegatives_2(self, grid: List[List[int]]) -> int:
        return self.helper(grid, 0, len(grid) - 1, 0, len(grid[0]) - 1)

    def helper(self, grid, low, high, left, right):
        if low > high:
            return 0
        mid = low + (high - low) // 2
        pos = -1
        for i in range(left, right + 1):
            if grid[mid][i] < 0:
                pos = i
                break

        ans = 0
        if pos != -1:
            ans += len(grid[0]) - pos
            ans += self.helper(grid, low, mid - 1, pos, right)
            ans += self.helper(grid, mid + 1, high, left, pos)

        else:
            ans += self.helper(grid, mid + 1, high, left, right)

        return ans

    def countNegatives_3(self, grid):
        ans, m, pos = 0, len(grid[0]), len(grid[0]) - 1

        for g in grid:
            while pos >= 0:
                if g[pos] >= 0:
                    ans += m - pos - 1
                    break
                pos -= 1
            if pos < 0:
                ans += m

        return ans


if __name__ == '__main__':
    nums = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
    test = Solution()
    print(test.countNegatives_3(nums))
