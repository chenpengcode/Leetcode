from typing import List


class Solution:
    def longestMountain(self, A: List[int]) -> int:
        if not A:
            return 0

        n = len(A)
        left = [0] * n
        for i in range(1, n):
            left[i] = left[i - 1] + 1 if A[i] > A[i - 1] else 0

        right = [0] * n
        for i in reversed(range(n - 1)):
            right[i] = right[i + 1] + 1 if A[i] > A[i + 1] else 0

        res = 0
        for i in range(n):
            if left[i] > 0 and right[i] > 0:
                res = max(res, left[i] + right[i] + 1)
        return res


if __name__ == '__main__':
    A = [2, 2, 2]
    solution = Solution()
    print(solution.longestMountain(A))
