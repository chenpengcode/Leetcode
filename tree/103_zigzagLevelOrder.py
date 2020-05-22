# Definition for a binary tree node.
from collections import deque
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder_dfs(self, root: TreeNode) -> List[List[int]]:
        levels = []

        def dfs(node, level):
            if not node:
                return
            if level >= len(levels):
                levels.append(deque([node.val]))
            else:
                if level % 2 == 0:
                    levels[level].append(node.val)
                else:
                    levels[level].appendleft(node.val)
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 0)
        ans = []
        for level in levels:
            ans.append(list(level))
        return ans

    def zigzag_level_order_bfs(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        ans = []
        is_left = True
        level = deque()
        queue = deque([root, None])

        while queue:
            node = queue.popleft()
            if node:
                if is_left:
                    level.append(node.val)
                else:
                    level.appendleft(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            else:
                ans.append(list(level))

                if queue:
                    queue.append(None)
                level = deque()
                is_left = not is_left

        return ans

