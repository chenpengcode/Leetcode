import collections
from typing import List


class Solution:
    def canFinish_bfs(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = collections.defaultdict(list)
        indeg = [0] * numCourses

        for info in prerequisites:
            edges[info[1]].append(info[0])
            indeg[info[0]] += 1

        q = collections.deque([u for u in range(numCourses) if indeg[u] == 0])

        while q:
            u = q.popleft()
            numCourses -= 1
            for v in edges[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)

        return not numCourses

    def canFinish_dfs(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = collections.defaultdict(list)
        visited = [0] * numCourses
        invalid = False

        for info in prerequisites:
            edges[info[1]].append(info[0])

        def dfs(u: int):
            nonlocal invalid
            visited[u] = 1
            for v in edges[u]:
                if visited[v] == 0:
                    dfs(v)
                    if invalid:
                        return
                elif visited[v] == 1:
                    invalid = True
                    return
            visited[u] = 2

        for i in range(numCourses):
            if not visited[i]:
                dfs(i)
                if invalid:
                    return False
        return True

    def canFinish_dfs_2(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(u, edges, visited):
            if visited[u] == 1:
                return False
            if visited[u] == 2:
                return True
            visited[u] = 1
            for v in edges[u]:
                if not dfs(v, edges, visited):
                    return False
            visited[u] = 2
            return True

        edges = collections.defaultdict(list)
        visited = [0] * numCourses
        for info in prerequisites:
            edges[info[1]].append(info[0])

        for i in range(numCourses):
            if not dfs(i, edges, visited):
                return False
        return True


if __name__ == '__main__':
    numCourses = 2
    prerequisites = [[1, 0], [0, 1]]
    test = Solution()
    print(test.canFinish_dfs_2(numCourses, prerequisites))
