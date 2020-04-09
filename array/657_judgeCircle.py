import collections


class Solution:
    def judgeCircle(self, moves: str) -> bool:
        n = len(moves)
        if n % 2 != 0:
            return False
        cnt = collections.Counter(moves)
        L = cnt.get('L')
        R = cnt.get('R')
        U = cnt.get('U')
        D = cnt.get('D')
        return L == R and U == D



if __name__ == '__main__':
    moves = "DL"
    test = Solution()
    print(test.judgeCircle(moves))
