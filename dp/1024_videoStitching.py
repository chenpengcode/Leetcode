from typing import List


class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        dp = [0] + [float("inf")] * T
        for i in range(1, T + 1):
            for aj, bj in clips:
                if aj < i <= bj:
                    dp[i] = min(dp[i], dp[aj] + 1)

        return -1 if dp[T] == float("inf") else dp[T]

    def videoStitching_greed(self, clips: List[List[int]], T: int) -> int:
        maxn = [0] * T
        last = ret = pre = 0
        for a, b in clips:
            if a < T:
                maxn[a] = max(maxn[a], b)

        for i in range(T):
            last = max(last, maxn[i])
            if i == last:
                return -1
            if i == pre:
                ret += 1
                pre = last

        return ret


if __name__ == '__main__':
    clips = [[0, 2], [4, 6], [8, 10], [1, 9], [1, 5], [5, 9]]
    T = 10
    solution = Solution()
    print(solution.videoStitching_greed(clips, T))
