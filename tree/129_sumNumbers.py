# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def sumNumbers(self, root: TreeNode) -> int:
        def dfs(root, value):
            if not root:
                return value
            value = value * 10 + root.val
            if not root.left and not root.right:
                return value
            if root.left and not root.right:
                return dfs(root.left, value)
            if not root.left and root.right:
                return dfs(root.right, value)
            return dfs(root.left, value) + dfs(root.right, value)

        return dfs(root, 0)
