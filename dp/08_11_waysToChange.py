class Solution:
    def waysToChange(self, n: int) -> int:
        mod = 10 ** 9 + 7
        coins = [25, 10, 5, 1]

        f = [1] + [0] * n
        for coin in coins:
            for i in range(coin, n + 1):
                f[i] += f[i - coin]
        return f[n] % mod


if __name__ == '__main__':
    n = 30
    test = Solution()
    print(test.waysToChange(n))
