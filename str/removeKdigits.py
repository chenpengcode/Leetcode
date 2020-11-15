class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = list()

        for i in range(len(num)):
            digit = num[i]
            while stack and k and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)

        while k > 0:
            stack.pop()
            k -= 1

        return ''.join(stack).lstrip('0') or "0"
