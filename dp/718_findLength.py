from typing import List


class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        if not A or not B:
            return 0

        ans = 0
        for i in range(len(A)):
            for j in range(len(B)):
                if A[i] != B[j]:
                    continue
                p1, p2, cnt = i, j, 0
                while p1 < len(A) and p2 < len(B) and A[p1] == B[p2]:
                    cnt += 1
                    p1 += 1
                    p2 += 1

                ans = max(ans, cnt)
        return ans

    def findLength_dp(self, A: List[int], B: List[int]) -> int:
        dp = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
        for i in range(1, len(A) + 1):
            for j in range(1, len(B) + 1):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
        return max(max(row) for row in dp)


if __name__ == '__main__':
    A = [1, 2, 3, 2, 1]
    B = [3, 2, 1, 4, 7]
    solution = Solution()
    print(solution.findLength_dp(A, B))
