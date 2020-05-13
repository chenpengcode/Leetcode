# Definition for a binary tree node.
import collections
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.ans = []

    def helper(self, root: TreeNode, level: int):
        if not root:
            return
        if len(self.ans) == level:
            self.ans.append([])
        self.ans[level].append(root.val)
        if root.left:
            self.helper(root.left, level + 1)
        if root.right:
            self.helper(root.right, level + 1)

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        self.helper(root, 0)
        return self.ans

    def levelOrder_iter(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        ans = []
        queue = collections.deque()
        queue.append(root)

        while queue:
            size = len(queue)
            level = []
            while size > 0:
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                size -= 1
            ans.append(level)
        return ans
