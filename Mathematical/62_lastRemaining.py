import sys

sys.setrecursionlimit(100000)


class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        def f(n):
            if n == 0:
                return 0
            return (f(n - 1) + m) % n

        return f(n)

    def last_remaining(self, n: int, m: int) -> int:
        res = 0

        for i in range(2, n + 1):
            res = (res + m) % i

        return res


if __name__ == '__main__':
    test = Solution()
    n = 5
    m = 3
    print(test.last_remaining(n, m))
