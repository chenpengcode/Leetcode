# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.is_mirror(root, root)

    def is_mirror(self, root_1, root_2):
        if not root_1 and not root_2:
            return True
        if not root_1 or not root_2:
            return False
        return (root_1.val == root_2.val) and self.is_mirror(root_1.left, root_2.right) and self.is_mirror(root_1.right, root_2.left)

    def isSymmetric_iter(self, root: TreeNode) -> bool:
        deq = collections.deque()
        deq.append((root, root))

        while deq:
            node1, node2 = deq.popleft()
            if not node1 and not node2:
                continue
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False
            deq.append((node1.left, node2.right))
            deq.append((node1.right, node2.left))
        return True

