# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        nums = list()
        self.inorder(root, nums)
        swaped = self.swap(nums)
        self.recover(root, swaped[0], swaped[1])

    def inorder(self, root, nums):
        if not root:
            return
        self.inorder(root.left, nums)
        nums.append(root.val)
        self.inorder(root.right, nums)

    def swap(self, nums):
        n = len(nums)
        x, y = -1, -1

        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                y = nums[i + 1]
                if x == -1:
                    x = nums[i]
                else:
                    break

        return [x, y]

    def recover(self, root, x, y):
        if not root:
            return
        if root.val == x:
            root.val = y
        elif root.val == y:
            root.val = x
        self.recover(root.left, x, y)
        self.recover(root.right, x, y)

    def recoverTree_stack(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack = []
        x, y, pre = None, None, None
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if pre and root.val < pre.val:
                y = root
                if not x:
                    x = pre
                else:
                    break
            pre = root
            root = root.right

        x.val, y.val = y.val, x.val
