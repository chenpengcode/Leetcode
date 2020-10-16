from typing import List


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        ans = []
        n = len(A)
        right = 0
        while right < n and A[right] < 0:
            right += 1
        if right == 0:
            return [x * x for x in A]
        if right == n:
            return [x * x for x in reversed(A)]

        left = right - 1
        while left >= 0 and right < n:
            if abs(A[left]) > A[right]:
                ans.append(A[right] * A[right])
                right += 1
            else:
                ans.append(A[left] * A[left])
                left -= 1
        while left >= 0:
            ans.append(A[left] * A[left])
            left -= 1
        while right < n:
            ans.append(A[right] * A[right])
            right += 1
        return ans

    def sortedSquares_2(self, A: List[int]) -> List[int]:
        left, right = 0, len(A) - 1

        ans = []
        while left <= right:
            if abs(A[left]) > A[right]:
                ans.append(A[left] * A[left])
                left += 1
            else:
                ans.append(A[right] * A[right])
                right -= 1
        return list(reversed(ans))


if __name__ == '__main__':
    A = [-4, -1, 0, 3, 10]
    solution = Solution()
    print(solution.sortedSquares(A))
