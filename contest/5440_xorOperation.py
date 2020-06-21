class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        i = 1
        ans = start
        while i < n:
            x = start + 2 * i
            ans ^= x
            i += 1
        return ans
