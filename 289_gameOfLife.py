from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        neighbors = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1),
                     (0, 1), (1, 1)]
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                live_neighbors = 0
                for neighbor in neighbors:
                    r = i + neighbor[0]
                    c = j + neighbor[1]
                    if (m > r >= 0) and (n > c >= 0) and (abs(board[r][c]) == 1):
                        live_neighbors += 1
                if board[i][j] == 1 and (
                        live_neighbors < 2 or live_neighbors > 3):
                    board[i][j] = -1

                elif board[i][j] == 0 and live_neighbors == 3:
                    board[i][j] = 2

        for i in range(m):
            for j in range(n):
                if board[i][j] > 0:
                    board[i][j] = 1
                else:
                    board[i][j] = 0
