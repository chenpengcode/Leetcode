import collections


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dict = collections.Counter(s)
        t_dict = collections.Counter(t)
        for key, value in s_dict.items():
            if key not in t_dict or value != t_dict.get(key):
                return False
        return True


if __name__ == '__main__':
    s = "anagram"
    t = "nagaam"
    test = Solution()
    print(test.isAnagram(s, t))
