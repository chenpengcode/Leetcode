def digitsum(n):
    ans = 0
    while n:
        ans += n % 10
        n //= 10
    return ans


class Solution:
    def movingCount_dfs(self, m: int, n: int, k: int) -> int:
        visited = set()

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or (i, j) in visited or digitsum(
                    i) + digitsum(j) > k:
                return
            else:
                visited.add((i, j))
                dfs(i - 1, j)
                dfs(i + 1, j)
                dfs(i, j - 1)
                dfs(i, j + 1)

        dfs(0, 0)
        return len(visited)

    def movingCount(self, m: int, n: int, k: int) -> int:
        """
        可以只搜索向右和向下
        :param m:
        :param n:
        :param k:
        :return:
        """
        visited = set()

        def dfs(i, j):
            if i >= m or j >= n or (i, j) in visited or digitsum(i) + digitsum(j) > k:
                return
            else:
                visited.add((i, j))
                dfs(i + 1, j)
                dfs(i, j + 1)

        dfs(0, 0)
        return len(visited)

    def movingCount_iter(self, m: int, n: int, k: int) -> int:
        vis = {(0, 0)}
        for i in range(m):
            for j in range(n):
                if ((i - 1, j) in vis or (i, j - 1) in vis) and digitsum(i) + digitsum(j) <= k:
                    vis.add((i, j))
        return len(vis)

    def movingCount_bfs(self, m: int, n: int, k: int) -> int:
        from queue import Queue
        q = Queue()
        q.put((0, 0))
        s = set()
        while not q.empty():
            x, y = q.get()
            if (x, y) not in s and 0 <= x < m and 0 <= y < n and digitsum(x) + digitsum(y) <= k:
                s.add((x, y))
                for nx, ny in [(x + 1, y), (x, y + 1)]:
                    q.put((nx, ny))
        return len(s)
