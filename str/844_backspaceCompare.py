class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def handle(s: str):
            res = list()
            for ch in s:
                if ch != '#':
                    res.append(ch)
                elif res:
                    res.pop()
            return "".join(res)

        return handle(S) == handle(T)

    def backspaceCompare_1(self, S: str, T: str) -> bool:
        i, j = len(S) - 1, len(T) - 1
        skip0 = skip1 = 0

        while i >= 0 or j >= 0:
            while i >= 0:
                if S[i] == '#':
                    skip0 += 1
                    i -= 1
                elif skip0 > 0:
                    i -= 1
                    skip0 -= 1
                else:
                    break
            while j >= 0:
                if T[j] == '#':
                    skip1 += 1
                    j -= 1
                elif skip1 > 0:
                    j -= 1
                    skip1 -= 1
                else:
                    break
            if i >= 0 and j >= 0:
                if S[i] != T[j]:
                    return False
            elif i >= 0 or j >= 0:
                return False
            i -= 1
            j -= 1
        return True


if __name__ == '__main__':
    S = "ab#c"
    T = "ad#c"
    solution = Solution()
    print(solution.backspaceCompare_1(S, T))
