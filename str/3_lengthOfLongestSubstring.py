class Solution:
    def lengthOfLongestSubstring_brute(self, s: str) -> int:
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

        right, ans = -1, 0

        for left in range(n):
            if left > 0:
                tmp.remove(s[left - 1])
            while right + 1 < n and s[right + 1] not in tmp:
                right += 1
                tmp.add(s[right])
            ans = max(ans, right - left + 1)

        return ans


if __name__ == '__main__':
    s = "abcaabb"
    test = Solution()
    print(test.lengthOfLongestSubstring_2(s))
