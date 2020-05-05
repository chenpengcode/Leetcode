# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        self.helper(root, ans)
        return ans

    def helper(self, root, ans):
        if not root:
            return
        ans.append(root.val)
        self.helper(root.left, ans)
        self.helper(root.right, ans)

    def preorderTraversal_iter(self, root: TreeNode) -> List[int]:
        ans, stack = [], [root]

        while stack:
            root = stack.pop()
            if root:
                ans.append(root.val)
                if root.right:
                    stack.append(root.right)
                if root.left:
                    stack.append(root.left)

        return ans
