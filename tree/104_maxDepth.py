# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

    def maxDepth(self, root: TreeNode) -> int:
        stack = []
        if root:
            stack.append((1, root))

        depth = 0
        while stack:
            cur_depth, root = stack.pop()
            if not root:
                depth = max(depth, cur_depth)
                stack.append((cur_depth + 1, root.left))
                stack.append((cur_depth + 1, root.right))

        return depth
