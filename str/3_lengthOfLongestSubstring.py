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
        tmp = set()
        n = len(s)

        right_k, ans = -1, 0

        for i in range(n):
            if i > 0:
                tmp.remove(s[i - 1])
            while right_k + 1 < n and s[right_k + 1] not in tmp:
                right_k += 1
                tmp.add(s[right_k])
            ans = max(ans, right_k - i + 1)

        return ans


if __name__ == '__main__':
    s = "abcabcbb"
    test = Solution()
    print(test.lengthOfLongestSubstring_2(s))
