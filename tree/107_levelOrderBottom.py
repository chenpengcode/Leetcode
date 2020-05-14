# Definition for a binary tree node.
import collections
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        levels = []
        self.level_order(root, 0, levels)
        return levels[::-1]

    def level_order(self, root, level, levels):
        if not root:
            return
        if level < len(levels):
            levels[level].append(root.val)
        else:
            levels.append([root.val])
        self.level_order(root.left, level + 1, levels)
        self.level_order(root.right, level + 1, levels)

    def levelOrderBottom_iter(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        ans = []
        deque = collections.deque()
        level = collections.deque()
        deque.append(root)
        while deque:
            tmp = []
            while deque:
                node = deque.popleft()
                tmp.append(node.val)
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)

            while level:
                deque.append(level.popleft())
            ans.append(tmp)
        return ans[::-1]
