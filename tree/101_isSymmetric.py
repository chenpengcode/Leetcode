# Definition for a binary tree node.
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

    def isSymmetric(self, root: TreeNode) -> bool:
        queue = [root, root]
        while queue:
            t1 = queue.pop()
            t2 = queue.pop()
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            if t1.val != t2.val:
                return False
            queue.append(t1.left)
            queue.append(t2.right)
            queue.append(t1.right)
            queue.append(t2.left)

        return True

