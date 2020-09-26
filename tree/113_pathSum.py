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
        stack = [(root, [root.val])]
        while stack:
            node, tmp = stack.pop()
            if not node.left and not node.right and sum(tmp) == total:
                print(tmp)
                ans.append(tmp[:])
            if node.right:
                stack.append((node.right, tmp + [node.right.val]))
            if node.left:
                stack.append((node.left, tmp + [node.left.val]))
        return ans

    def pathSum_dfs(self, root: TreeNode, total: int) -> List[List[int]]:
        ans = []
        tmp = []

        def helper(root, total):
            if not root:
                return
            tmp.append(root.val)
            # print(tmp)
            if not root.left and not root.right and sum(tmp) == total:
                # print(tmp)
                ans.append(tmp[:])
            helper(root.left, total)
            helper(root.right, total)
            tmp.pop()

        helper(root, total)
        return ans

    def pathSum_dfs_2(self, root: TreeNode, total: int) -> List[List[int]]:
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
