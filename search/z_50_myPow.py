class Solution:
    def myPow(self, x: float, n: int) -> float:
        def pow(n):
            if n == 0:
                return 1.0
            y = pow(n // 2)
            return y * y if n % 2 == 0 else y * y * x
        return pow(n) if n > 0 else 1.0 / pow(-n)

    def myPow_iter(self, x: float, n: int) -> float:
        def pow(N):
            ans = 1.0
            x_contribute = x
            while N > 0:
                if N % 2 == 1:
                    ans *= x_contribute

                x_contribute *= x_contribute
                N //= 2
            return ans

        return pow(n) if n > 0 else 1.0 / pow(-n)


if __name__ == '__main__':
    x = 2.0
    n = 10
    test = Solution()
    print(test.myPow_iter(x, n))
