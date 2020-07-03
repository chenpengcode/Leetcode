# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasPathSum_iter(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False

        stack = [(root, 0)]
        while stack:
            node, total = stack.pop()
            total += node.val
            if not node.left and not node.right and total == sum:
                return True

            if node.left:
                stack.append((node.left, total))
            if node.right:
                stack.append((node.right, total))
        return False

    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False

        sum -= root.val
        if not root.left and not root.right:
            return sum == 0
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)
