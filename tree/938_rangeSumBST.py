# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if not root:
            return 0
        if L > root.val:
            return self.rangeSumBST(root.right, L, R)
        if R < root.val:
            return self.rangeSumBST(root.left, L, R)
        return root.val + self.rangeSumBST(root.left, L, root.val) + self.rangeSumBST(root.right,
                                                                                      root.val, R)

    def rangeSumBST_iter(self, root: TreeNode, L: int, R: int) -> int:
        ans = 0
        stack = [root]

        while stack:
            node = stack.pop()
            if node:
                if L <= node.val <= R:
                    ans += node.val
                if L < node.val:
                    stack.append(node.left)
                if R > node.val:
                    stack.append(node.right)
        return ans
