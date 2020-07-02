# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, total: int) -> List[List[int]]:
        if not root:
            return []
        ans = []
        stack = [([root.val], root)]
        while stack:
            path, node = stack.pop()
            if not node.left and not node.right and sum(path) == total:
                ans.append(path)
            if node.right:
                stack.append((path + [node.right.val], node.right))
            if node.left:
                stack.append((path + [node.left.val], node.left))
        return ans

    def pathSum_dfs(self, root: TreeNode, total: int) -> List[List[int]]:
        def dfs(root, tmp, total):
            if not root:
                return
            if not root.left and not root.right and root.val == total:
                tmp += [root.val]
                ans.append(tmp)
            dfs(root.left, tmp + [root.val], total - root.val)
            dfs(root.right, tmp + [root.val], total - root.val)

        ans = []
        dfs(root, [], total)
        return ans


if __name__ == '__main__':
    lst = [1, 2, 3]
    lst_2 = [4, 5, 6]
    print(lst + lst_2)
