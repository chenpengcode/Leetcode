from typing import List


class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        ans = 0
        # 白车坐标
        x, y = 0, 0
        # 方向元组
        dx, dy = (0, 1, 0, -1), (1, 0, -1, 0)
        for i in range(8):
            for j in range(8):
                if board[i][j] == "R":
                    x, y = i, j
                    break

        for i in range(4):
            step = 0
            while True:
                tx = x + step * dx[i]
                ty = y + step * dy[i]
                if tx < 0 or tx > 7 or ty < 0 or ty > 7 or board[tx][ty] == "B":
                    break
                if board[tx][ty] == "p":
                    ans += 1
                    break
                step += 1
        return ans


if __name__ == '__main__':
    test = Solution()
    t_list = [[".", ".", ".", ".", ".", ".", ".", "."],
              [".", ".", ".", "p", ".", ".", ".", "."],
              [".", ".", ".", "R", ".", ".", ".", "p"],
              [".", ".", ".", ".", ".", ".", ".", "."],
              [".", ".", ".", ".", ".", ".", ".", "."],
              [".", ".", ".", "p", ".", ".", ".", "."],
              [".", ".", ".", ".", ".", ".", ".", "."],
              [".", ".", ".", ".", ".", ".", ".", "."]]
    print(test.numRookCaptures(t_list))
