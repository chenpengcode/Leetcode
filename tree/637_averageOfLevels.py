# Definition for a binary tree node.
import collections
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def averageOfLevels_iter(self, root: TreeNode) -> List[float]:
        if not root:
            return []
        ans = []
        dequeue = collections.deque()
        tmp = collections.deque()

        dequeue.append(root)

        while dequeue:
            sum_tmp = 0
            cnt = 0
            while dequeue:
                node = dequeue.popleft()
                sum_tmp += node.val
                cnt += 1
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            while tmp:
                dequeue.append(tmp.popleft())

            ans.append(sum_tmp / cnt)
        return ans

    def average(self, root, h, sum_level, cnt):
        if not root:
            return
        if h < len(sum_level):
            sum_level[h] += root.val
            cnt[h] += 1
        else:
            sum_level.append(root.val)
            cnt.append(1)

        self.average(root.left, h + 1, sum_level, cnt)
        self.average(root.right, h + 1, sum_level, cnt)

    def averageOfLevels(self, root: TreeNode) -> List[float]:
        ans = []
        sum_level = []
        cnt = []
        self.average(root, 0, sum_level, cnt)
        for i in range(len(cnt)):
            ans.append(sum_level[i] / cnt[i])
        return ans
