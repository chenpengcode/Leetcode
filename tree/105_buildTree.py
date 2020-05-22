# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def build(pre_left, pre_right, in_left, in_right):
            if pre_left > pre_right:
                return None

            pre_root = pre_left
            ino_root = index[preorder[pre_root]]

            root = TreeNode(preorder[pre_root])
            size_left = ino_root - in_left
            root.left = build(pre_left + 1, pre_left + size_left, in_left, ino_root - 1)
            root.right = build(pre_left + size_left + 1, pre_right, ino_root + 1, in_right)
            return root

        n = len(preorder)
        index = {key: val for val, key in enumerate(inorder)}
        return build(0, n - 1, 0, n - 1)

    def buildTree_iter(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        stack = [root]
        index = 0

        for i in range(1, len(preorder)):
            node = stack[-1]
            if node.val != inorder[index]:
                node.left = TreeNode(preorder[i])
                stack.append(node.left)
            else:
                while stack and stack[-1].val == inorder[index]:
                    node = stack.pop()
                    index += 1
                node.right = TreeNode(preorder[i])
                stack.append(node.right)
        return root
