import collections
from typing import List


class Solution:
    def solve_dfs(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        n, m = len(board), len(board[0])

        def dfs(x, y):
            if not 0 <= x < n or not 0 <= y < m or board[x][y] == 'O':
                return
            board[x][y] = 'A'
            dfs(x - 1, y)
            dfs(x + 1, y)
            dfs(x, y - 1)
            dfs(x, y + 1)

        for i in range(n):
            dfs(i, 0)
            dfs(i, m - 1)

        for i in range(m):
            dfs(0, i)
            dfs(n - 1, i)

        for i in range(n):
            for j in range(m):
                if board[i][j] == 'A':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'

    def solve_bfs(self, board: List[List[str]]) -> None:
        if not board:
            return
        n, m = len(board), len(board[0])
        q = collections.deque()
        for i in range(n):
            if board[i][0] == 'O':
                q.append((i, 0))
            if board[i][m - 1] == 'O':
                q.append((i, m - 1))

        for i in range(1, m - 1):
            if board[0][i] == 'O':
                q.append((0, i))
            if board[n - 1][i] == 'O':
                q.append((n - 1, i))

        while q:
            x, y = q.popleft()
            board[x][y] = 'A'
            for mx, my in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if 0 <= mx < n and 0 <= my < m and board[mx][my] == 'O':
                    q.append((mx, my))
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'A':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
