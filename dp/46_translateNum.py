class Solution:
    def translateNum(self, num: int) -> int:
        s = str(num)

        def dfs(s, p):
            if p >= len(s) - 1:
                return 1
            tmp = int(s[p] + s[p + 1])
            if 10 <= tmp <= 25:
                return dfs(s, p + 1) + dfs(s, p + 2)
            else:
                return dfs(s, p + 1)

        return dfs(s, 0)

    def translateNum_dp(self, num: int) -> int:
        s = str(num)
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1
        for i in range(2, n + 1):
            tmp = int(s[i - 2] + s[i - 1])
            if 10 <= tmp <= 25:
                dp[i] = dp[i - 1] + dp[i - 2]
            else:
                dp[i] = dp[i - 1]
        return dp[n]

    def translateNum_dp_better(self, num: int) -> int:
        s = str(num)
        n = len(s)
        pre = cur = 1
        for i in range(2, n + 1):
            tmp = int(s[i - 2] + s[i - 1])
            if 10 <= tmp <= 25:
                t = cur
                cur = pre + cur
                pre = t
            else:
                pre = cur
        return cur


if __name__ == '__main__':
    num = 1223
    solution = Solution()
    print(solution.translateNum_dp_better(num))
