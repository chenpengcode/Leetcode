class Solution:
    def validPalindrome(self, s: str) -> bool:
        def helper(low, high):
            while low < high:
                if s[low] != s[high]:
                    return False
                else:
                    low += 1
                    high -= 1
            return True

        low, high = 0, len(s) - 1
        while low < high:
            if s[low] == s[high]:
                low += 1
                high -= 1
            else:
                return helper(low + 1, high) or helper(low, high - 1)

        return True
