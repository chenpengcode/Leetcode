# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def sumNumbers(self, root: TreeNode) -> int:
        def dfs(root, value):
            if not root:
                return 0
            value = value * 10 + root.val
            if not root.left and not root.right:
                return value
            # if root.left and not root.right:
            #     return dfs(root.left, value)
            # if not root.left and root.right:
            #     return dfs(root.right, value)
            return dfs(root.left, value) + dfs(root.right, value)

        return dfs(root, 0)

    def sumNumbers_bfs(self, root: TreeNode) -> int:
        if not root:
            return 0

        q1, q2 = collections.deque(), collections.deque()
        q1.append(root)
        q2.append(root.val)

        ans = 0
        while q1:
            node = q1.popleft()
            num = q2.popleft()
            if not node.left and not node.right:
                ans += num
            else:
                if node.left:
                    q1.append(node.left)
                    q2.append(num * 10 + node.left.val)
                if node.right:
                    q1.append(node.right)
                    q2.append(num * 10 + node.right.val)
        return ans
