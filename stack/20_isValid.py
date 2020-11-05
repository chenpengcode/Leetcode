class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}

        for c in s:
            if c in mapping.keys():
                top = stack.pop() if stack else '#'
                if top != mapping[c]:
                    return False
            else:
                stack.append(c)

        return not stack


if __name__ == '__main__':
    test = Solution()
    a = "()[]{}"
    print(test.isValid(a))
