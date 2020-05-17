import collections
from typing import List


class Solution:
    def findOrder_dfs(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 存储有向图
        edges = collections.defaultdict(list)
        # 标记每个节点的状态：0=未搜索，1=搜索中，2=已完成
        visited = [0] * numCourses
        # 用数组来模拟栈，下标 0 为栈底，n-1 为栈顶
        result = list()
        # 判断有向图中是否有环
        invalid = False

        for info in prerequisites:
            edges[info[1]].append(info[0])

        def dfs(u: int):
            nonlocal invalid
            # 将节点标记为「搜索中」
            visited[u] = 1
            # 搜索其相邻节点
            # 只要发现有环，立刻停止搜索
            for v in edges[u]:
                # 如果「未搜索」那么搜索相邻节点
                if visited[v] == 0:
                    dfs(v)
                    if invalid:
                        return
                # 如果「搜索中」说明找到了环
                elif visited[v] == 1:
                    invalid = True
                    return
            # 将节点标记为「已完成」
            visited[u] = 2
            # 将节点入栈
            result.append(u)

        # 每次挑选一个「未搜索」的节点，开始进行深度优先搜索
        for i in range(numCourses):
            if not invalid and not visited[i]:
                dfs(i)

        if invalid:
            return list()

        # 如果没有环，那么就有拓扑排序
        # 注意下标 0 为栈底，因此需要将数组反序输出
        return result[::-1]

    def findOrder_bfs(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 存储有向图
        edges = collections.defaultdict(list)
        # 存储每个节点的入度
        indeg = [0] * numCourses
        # 存储答案
        result = list()

        for info in prerequisites:
            edges[info[1]].append(info[0])
            indeg[info[0]] += 1

        # 将所有入度为 0 的节点放入队列中
        q = collections.deque([u for u in range(numCourses) if indeg[u] == 0])

        while q:
            # 从队首取出一个节点
            u = q.popleft()
            # 放入答案中
            result.append(u)
            for v in edges[u]:
                indeg[v] -= 1
                # 如果相邻节点 v 的入度为 0，就可以选 v 对应的课程了
                if indeg[v] == 0:
                    q.append(v)

        if len(result) != numCourses:
            result = list()
        return result

    def findOrder_try(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        edges = collections.defaultdict(list)
        indegree = [0] * numCourses

        result = []
        for info in prerequisites:
            edges[info[1]].append(info[0])
            indegree[info[0]] += 1

        q = collections.deque([u for u in range(numCourses) if indegree[u] == 0])
        while q:
            u = q.popleft()
            result.append(u)
            for v in edges[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)
        if len(result) != numCourses:
            return []
        return result


if __name__ == '__main__':
    numCourses = 4
    prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
    test = Solution()
    print(test.findOrder_try(numCourses, prerequisites))
