# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth_dfs(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        min_depth = 0
        if root.left and not root.right:
            min_depth = self.minDepth_dfs(root.left)
        elif not root.left and root.right:
            min_depth = self.minDepth_dfs(root.right)
        else:
            min_depth = min(self.minDepth_dfs(root.left), self.minDepth_dfs(root.right))
        return min_depth + 1

    def minDepth_dfs_iter(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack = [(1, root)]
        ans = float('inf')

        while stack:
            depth, node = stack.pop()
            if not node.left and not node.right:
                ans = min(ans, depth)
            if node.left:
                stack.append((depth + 1, node.left))
            if node.right:
                stack.append((depth + 1, node.right))
        return ans

    def minDepth_bfs(self, root: TreeNode) -> int:
        if not root:
            return 0
        q = collections.deque()
        q.append((1, root))
        while q:
            level, node = q.popleft()
            if not node.left and not node.right:
                return level
            if node.left:
                q.append((level + 1, node.left))
            if node.right:
                q.append((level + 1, node.right))
