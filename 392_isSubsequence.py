class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s:
            return True
        if not t:
            return False
        list_s = list(s)
        list_t = list(t)
        i = j = 0
        while i < len(list_s) and j < len(list_t):
            if list_s[i] == list_t[j]:
                i += 1
            j += 1
        if i == len(list_s):
            return True
        return False


if __name__ == '__main__':
    test = Solution()
    s = "leeeeetcode"
    t = "yyyyyyyyyyyyylyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyleeeeetcodeyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy"
    print(test.isSubsequence(s, t))
