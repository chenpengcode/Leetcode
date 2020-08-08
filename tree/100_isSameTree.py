# Definition for a binary tree node.
import collections
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False

        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right,
                                                                                      q.right)

    def isSameTree_iter(self, p: TreeNode, q: TreeNode) -> bool:
        def check(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False

            if p.val != q.val:
                return False
            return True

        deq = deque([(p, q), ])
        while deq:
            (p, q) = deq.popleft()
            if not check(p, q):
                return False

            if p:
                deq.append((p.left, q.left))
                deq.append((p.right, q.right))

        return True

    def isSameTree_iter2(self, p: TreeNode, q: TreeNode) -> bool:
        deq = collections.deque()
        deq.append((p, q))

        while deq:
            t1, t2 = deq.popleft()
            if not t1 and not t2:
                continue
            if not t1 or not t2:
                return False
            if t1.val != t2.val:
                return False
            deq.append((t1.left, t2.left))
            deq.append((t1.right, t2.right))
        return True
