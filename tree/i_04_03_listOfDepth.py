# Definition for a binary tree node.
import collections
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def listOfDepth_dfs(self, tree: TreeNode) -> List[ListNode]:
        def dfs(tree, level, levels):
            if not tree:
                return
            node = ListNode(tree.val)
            if level < len(levels):
                p = levels[level]
                while p.next:
                    p = p.next
                p.next = node
            else:
                levels.append(node)
            dfs(tree.left, level + 1, levels)
            dfs(tree.right, level + 1, levels)

        ans = []
        dfs(tree, 0, ans)
        return ans

    def listOfDepth_bfs(self, tree: TreeNode) -> List[ListNode]:
        if not tree:
            return []

        q = collections.deque()
        level = collections.deque()
        ans = []
        q.append(tree)

        while q:
            tmp = []
            while q:
                node = q.popleft()
                tmp.append(node.val)
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            while level:
                q.append(level.popleft())
            head = p = ListNode(0)
            for i in range(len(tmp)):
                p.next = ListNode(tmp[i])
                p = p.next
            ans.append(head.next)

        return ans
