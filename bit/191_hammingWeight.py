class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n > 0:
            n = n & (n - 1)
            ans += 1
        return ans


if __name__ == '__main__':
    test = Solution()
    n = 5
    print(test.hammingWeight(n))
