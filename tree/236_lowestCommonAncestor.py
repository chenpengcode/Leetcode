# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.ans = TreeNode(0)

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.dfs(root, p, q)
        return self.ans

    def dfs(self, root, p, q):
        if not root:
            return False

        left = self.dfs(root.left, p, q)
        right = self.dfs(root.right, p, q)

        if (left and right) or ((root.val == p.val or root.val == q.val) and (left or right)):
            self.ans = root

        return left or right or (root.val == p.val or root.val == q.val)
