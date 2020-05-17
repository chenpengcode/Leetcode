import collections
from typing import List


class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        outdegs = [0] * N
        indegs = [0] * N

        for info in trust:
            outdegs[info[0] - 1] += 1
            indegs[info[1] - 1] += 1
        for i in range(N):
            if outdegs[i] == 0 and indegs[i] == N - 1:
                return i + 1
        return -1


if __name__ == '__main__':
    N = 3
    trust = [[1, 2], [2, 3]]
    test = Solution()
    print(test.findJudge(N, trust))
