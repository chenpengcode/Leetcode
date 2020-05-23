import collections


class Solution:
    def minWindow_brute(self, s: str, t: str) -> str:
        s_dict = {}
        t_dict = collections.Counter(t)
        begin, min_len = 0, len(s) + 1

        for i in range(len(s)):
            for j in range(i, len(s)):
                if j - i + 1 < len(t):
                    continue
                for key in t_dict.keys():
                    s_dict[key] = 0

                for k in range(i, j + 1):
                    if s[k] in t:
                        s_dict[s[k]] += 1
                if self.check(s_dict, t_dict) and j - i + 1 < min_len:
                    begin, min_len = i, j - i + 1
        if min_len == len(s) + 1:
            return ""
        return s[begin: begin + min_len]

    def check(self, s_dict, t_dict):
        for key in t_dict.keys():
            if s_dict[key] < t_dict[key]:
                return False
        return True

    def min_window_sliding_window(self, s: str, t: str) -> str:
        s_len, t_len = len(s), len(t)
        if not s or not t or s_len < t_len:
            return ""

        s_dict = {}
        t_dict = collections.Counter(t)
        for key in t_dict.keys():
            s_dict[key] = 0

        left, right = 0, 0
        begin, min_len = 0, s_len + 1
        distance = 0

        while right < s_len:
            if s[right] not in t_dict.keys():
                right += 1
                continue

            if s_dict[s[right]] < t_dict[s[right]]:
                distance += 1

            s_dict[s[right]] += 1
            right += 1

            while distance == t_len:
                if right - left < min_len:
                    begin, min_len = left, right - left

                if s[left] not in t_dict.keys():
                    left += 1
                    continue

                if s_dict[s[left]] == t_dict[s[left]]:
                    distance -= 1

                s_dict[s[left]] -= 1
                left += 1

        if min_len == s_len + 1:
            return ""
        return s[begin: begin + min_len]


if __name__ == '__main__':
    s = "ADOBECODEBANC"
    t = "ABC"
    test = Solution()
    print(test.min_window_sliding_window(s, t))
