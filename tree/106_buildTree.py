# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def build(in_left, in_right, post_left, post_right):
            if post_left > post_right:
                return None

            post_root = post_right
            in_root = index[postorder[post_root]]

            root = TreeNode(postorder[post_root])
            size_left = in_root - in_left
            root.left = build(in_left, in_root - 1, post_left, post_left + size_left - 1)
            root.right = build(in_root + 1, in_right, post_left + size_left, post_right - 1)
            return root

        n = len(inorder)
        index = {ele: i for i, ele in enumerate(inorder)}
        return build(0, n - 1, 0, n - 1)
