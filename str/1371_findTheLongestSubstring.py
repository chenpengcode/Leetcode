class Solution:
    def findTheLongestSubstring_brutu(self, s: str) -> int:
        n = len(s) - 1

        def helper(left, right):
            d = {'a': 0,
                 'e': 0,
                 'i': 0,
                 'o': 0,
                 'u': 0}
            for i in range(left, right + 1):
                if s[i] == 'a':
                    d['a'] += 1
                if s[i] == 'e':
                    d['e'] += 1
                if s[i] == 'i':
                    d['i'] += 1
                if s[i] == 'o':
                    d['o'] += 1
                if s[i] == 'u':
                    d['u'] += 1
            if d['a'] % 2 == 0 and d['e'] % 2 == 0 and d['i'] % 2 == 0 and d['o'] % 2 == 0 and d[
                'u'] % 2 == 0:
                return True
            return False

        max_len = 0
        for i in range(0, n + 1):
            for j in reversed(range(i, n + 1)):
                if helper(i, j):
                    max_len = max(max_len, j - i + 1)
        return max_len

    def findTheLongestSubstring_prefix(self, s: str) -> int:
        ans, status, n = 0, 0, len(s)
        pos = [-1] * (1 << 5)

        pos[0] = 0
        for i in range(n):
            if s[i] == 'a':
                status ^= 1 << 0
            elif s[i] == 'e':
                status ^= 1 << 1
            elif s[i] == 'i':
                status ^= 1 << 2
            elif s[i] == 'o':
                status ^= 1 << 3
            elif s[i] == 'u':
                status ^= 1 << 4

            if pos[status] != -1:
                ans = max(ans, i - pos[status] + 1)
            else:
                pos[status] = i + 1

        return ans


if __name__ == '__main__':
    s = "eleetminicoworoep"
    test = Solution()
    print(test.findTheLongestSubstring_prefix(s))
