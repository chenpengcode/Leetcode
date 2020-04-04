# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    tilt = 0

    def findTilt(self, root: TreeNode) -> int:
        self.traverse(root)
        return self.tilt

    def traverse(self, root):
        if not root:
            return 0
        left_val = self.traverse(root.left)
        right_val = self.traverse(root.right)
        self.tilt += abs(left_val - right_val)
        return left_val + left_val + root.val
