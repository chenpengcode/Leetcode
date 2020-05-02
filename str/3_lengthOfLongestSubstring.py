class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        ans = 1
        for i in range(len(s)):
            for j in range(i, len(s)):
                sub_str = s[i:j + 1]
                if len(sub_str) == len(set(sub_str)):
                    ans = max(ans, len(sub_str))

        return ans

    def lengthOfLongestSubstring_2(self, s: str) -> int:
        pass


if __name__ == '__main__':
    s = "abcabcbb"
    test = Solution()
    print(test.lengthOfLongestSubstring_2(s))
