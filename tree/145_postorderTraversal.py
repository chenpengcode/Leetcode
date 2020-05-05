# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        self.helper(root, ans)
        return ans

    def helper(self, root, ans):
        if not root:
            return

        self.helper(root.left, ans)
        self.helper(root.right, ans)
        ans.append(root.val)

    def postorderTraversal_iter(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        ans, stack = [], []
        stack.append(root)
        while stack:
            if root:
                node = stack.pop()
                ans.append(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)

        return ans[::-1]

    def postorderTraversal_iter_2(self, root: TreeNode) -> List[int]:
        ans, stack = [], []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left if root.left else root.right

            root = stack.pop()
            ans.append(root.val)
            if stack and root == stack[-1].left:
                root = stack[-1].right
            else:
                root = None
        return ans
