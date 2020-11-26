# Definition for a binary tree node.
import collections
from collections import deque
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.ans = []

    def rightSideView(self, root):
        rightmost_value_at_depth = dict()  # 深度为索引，存放节点的值
        max_depth = -1

        stack = [(root, 0)]
        while stack:
            node, depth = stack.pop()

            if node is not None:
                # 维护二叉树的最大深度
                max_depth = max(max_depth, depth)

                # 如果不存在对应深度的节点我们才插入
                rightmost_value_at_depth.setdefault(depth, node.val)

                stack.append((node.left, depth + 1))
                stack.append((node.right, depth + 1))

        return [rightmost_value_at_depth[depth] for depth in range(max_depth + 1)]

    def rightSideView_2(self, root):
        rightmost_value_at_depth = dict()  # 深度为索引，存放节点的值
        max_depth = -1

        queue = deque([(root, 0)])
        while queue:
            node, depth = queue.popleft()

            if node is not None:
                # 维护二叉树的最大深度
                max_depth = max(max_depth, depth)

                # 由于每一层最后一个访问到的节点才是我们要的答案，因此不断更新对应深度的信息即可
                rightmost_value_at_depth[depth] = node.val

                queue.append((node.left, depth + 1))
                queue.append((node.right, depth + 1))

        return [rightmost_value_at_depth[depth] for depth in range(max_depth + 1)]

    def rightSideView_3(self, root):
        if not root:
            return []
        ans = []
        deq = collections.deque([root])
        while deq:
            size = len(deq)
            for i in range(size):
                node = deq.popleft()
                if i == size - 1:
                    ans.append(node.val)
                if node.left:
                    deq.append(node.left)
                if node.right:
                    deq.append(node.right)
        return ans

    def rightSideView_4(self, root):
        def helper(root, level):
            if not root:
                return
            if len(self.ans) == level:
                self.ans.append(root.val)
            helper(root.right, level + 1)
            helper(root.left, level + 1)

        helper(root, 0)
        return self.ans


if __name__ == '__main__':
    solution = Solution()
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node1.left = node2
    node1.right = node3
    node2.right = node5
    node3.right = node4
    print(solution.rightSideView_4(node1))
