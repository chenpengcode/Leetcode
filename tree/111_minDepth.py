# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        if not root.left and root.right:
            return self.minDepth(root.right) + 1
        if root.left and not root.right:
            return self.minDepth(root.left) + 1
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

    def minDepth_dfs(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack = [(1, root)]
        depth = float('inf')
        while stack:
            cur_depth, root = stack.pop()
            if not root.left and not root.right:
                depth = min(cur_depth, depth)
            if root.left:
                stack.append((cur_depth + 1, root.left))
            if root.right:
                stack.append((cur_depth + 1, root.right))
        return depth

    def minDepth_bfs(self, root: TreeNode) -> int:
        if not root:
            return 0

        deq = collections.deque()
        deq.append((1, root))
        while deq:
            depth, root = deq.popleft()
            if not root.left and not root.right:
                return depth
            if root.left:
                deq.append((depth + 1, root.left))
            if root.right:
                deq.append((depth + 1, root.right))
