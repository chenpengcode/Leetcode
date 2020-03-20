import collections


class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = collections.Counter(s)

        ans = 0

        for value in count.values():
            ans += value // 2 * 2
            if value % 2 == 1 and ans % 2 == 0:
                ans += 1

        return ans


if __name__ == '__main__':
    s: str = "abccccdd"
    test = Solution()
    print(test.longestPalindrome(s))
