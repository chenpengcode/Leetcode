from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)

        def check(mid):
            i, j = n - 1, 0
            total = 0
            while i >= 0 and j < n:
                if matrix[i][j] <= mid:
                    total += i + 1
                    j += 1
                else:
                    i -= 1
            return total >= k

        def check_1(mid):
            i, j = 0, n - 1
            total = 0
            while j >= 0 and i < n:
                if matrix[i][j] <= mid:
                    total += j + 1
                    i += 1
                else:
                    j -= 1
            return total >= k

        left, right = matrix[0][0], matrix[-1][-1]
        while left < right:
            mid = (left + right) // 2
            if check_1(mid):
                right = mid
            else:
                left = mid + 1
        return left


if __name__ == '__main__':
    matrix = [[1, 5, 9],
              [10, 11, 13],
              [12, 13, 15]]
    k = 8
    solution = Solution()
    print(solution.kthSmallest(matrix, k))
