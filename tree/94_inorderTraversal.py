from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack, ans = [], []

        while stack or root:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            ans.append(root.val)
            root = root.right

        return ans

    def inorderTraversal_recur(self, root: TreeNode) -> List[int]:
        ans = []
        self.helper(root, ans)
        return ans

    def helper(self, root, ans):
        if not root:
            return
        if root.left:
            self.helper(root.left, ans)
        ans.append(root.val)
        if root.right:
            self.helper(root.right, ans)
