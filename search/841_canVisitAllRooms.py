import collections
from typing import List


class Solution:
    def canVisitAllRooms_bfs(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        vis = {0}
        q = collections.deque()
        q.append(0)
        num = 0

        while q:
            x = q.popleft()
            num += 1

            for i in rooms[x]:
                if i not in vis:
                    vis.add(i)
                    q.append(i)

        return num == n

    def canVisitAllRooms_dfs(self, rooms: List[List[int]]) -> bool:
        def dfs(x):
            vis.add(x)
            nonlocal num
            num += 1
            for it in rooms[x]:
                if it not in vis:
                    dfs(it)

        n = len(rooms)
        vis = set()
        num = 0
        dfs(0)
        return n == num
