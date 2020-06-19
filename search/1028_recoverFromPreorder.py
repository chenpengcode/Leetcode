# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        stack, index = [], 0
        while index < len(S):
            level = 0
            while S[index] == '-':
                level += 1
                index += 1
            value = 0
            while index < len(S) and S[index].isdigit():
                value = value * 10 + (ord(S[index]) - ord('0'))
                index += 1

            node = TreeNode(value)
            if level == len(stack):
                if stack:
                    stack[-1].left = node
            else:
                stack = stack[:level]
                stack[-1].right = node
            stack.append(node)
        return stack[0]


if __name__ == '__main__':
    s = "1-2--3--4-5--6--7"
    solution = Solution()
    print(solution.recoverFromPreorder(s))
