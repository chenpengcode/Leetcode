import collections
from typing import List


class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        ans = [[i, j] for i in range(R) for j in range(C)]
        ans.sort(key=lambda x: abs(x[0] - r0) + abs(x[1] - c0))
        return ans

    def allCellsDistOrder_2(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        maxDist = max(r0, R - 1 - r0) + max(c0, C - 1 - c0)
        bucket = collections.defaultdict(list)
        dist = lambda r1, c1, r2, c2: abs(r1 - r2) + abs(c1 - c2)

        for i in range(R):
            for j in range(C):
                bucket[dist(i, j, r0, c0)].append([i, j])

        ret = list()
        for i in range(maxDist + 1):
            ret.extend(bucket[i])

        return ret

    def allCellsDistOrder_3(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        dirs = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
        maxDist = max(r0, R - 1 - r0) + max(c0, C - 1 - c0)
        row, col = r0, c0
        ret = [[row, col]]
        for dist in range(1, maxDist + 1):
            row -= 1
            for i, (dr, dc) in enumerate(dirs):
                while (i % 2 == 0 and row != r0) or (i % 2 != 0 and col != c0):
                    if 0 <= row < R and 0 <= col < C:
                        ret.append([row, col])
                    row += dr
                    col += dc
        return ret


if __name__ == '__main__':
    R, C, r0, c0 = 3, 3, 1, 2
    solution = Solution()
    print(solution.allCellsDistOrder_3(R, C, r0, c0))
