class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        l = list()
        for c in s.upper():
            if c.isdigit() or c.isalpha():
                l.append(c)
        if not l:
            return True
        print(l)
        return l == l[::-1]
