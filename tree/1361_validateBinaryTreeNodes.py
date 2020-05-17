import collections
from typing import List


class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        indeg = [0] * n
        for u in leftChild:
            if u != -1:
                indeg[u] += 1
        for u in rightChild:
            if u != -1:
                indeg[u] += 1

        root = -1
        for i in range(n):
            if indeg[i] == 0:
                root = i
                break
        if root == -1:
            return False

        seen = {root}
        q = collections.deque([root])

        while q:
            u = q.popleft()
            if leftChild[u] != -1:
                if leftChild[u] in seen:
                    return False
                seen.add(leftChild[u])
                q.append(leftChild[u])
            if rightChild[u] != -1:
                if rightChild[u] in seen:
                    return False
                seen.add(rightChild[u])
                q.append(rightChild[u])

        return len(seen) == n
