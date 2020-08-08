"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ans = []

        def helper(root):
            if not root:
                return
            for child in root.children:
                helper(child)
            ans.append(root.val)

        helper(root)
        return ans

    def postorder_iter(self, root: 'Node') -> List[int]:
        if not root:
            return []
        stack = [root]
        ans = []

        while stack:
            root = stack.pop()
            ans.append(root.val)
            for child in root.children:
                stack.append(child)
        return ans[::-1]
