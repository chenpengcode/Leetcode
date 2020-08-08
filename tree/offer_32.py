# Definition for a binary tree node.
import collections
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []

        def helper(root, level):
            if not root:
                return
            if not ans or level >= len(ans):
                ans.append([])
            ans[level].append(root.val)
            helper(root.left, level + 1)
            helper(root.right, level + 1)

        helper(root, 0)
        return ans

    def levelOrder_iter(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        deq = collections.deque()
        deq.append(root)

        ans = []
        while deq:
            size = len(deq)
            tmp = []
            for i in range(size):
                node = deq.popleft()
                tmp.append(node.val)
                if node.left:
                    deq.append(node.left)
                if node.right:
                    deq.append(node.right)
            ans.append(tmp)
        return ans
