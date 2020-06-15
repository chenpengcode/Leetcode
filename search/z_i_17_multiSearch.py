from typing import List


class Solution:
    def multiSearch(self, big: str, smalls: List[str]) -> List[List[int]]:
        if not smalls:
            return []
        if not big:
            return [[] for _ in range(len(smalls))]
        ans = []
        for i in range(len(smalls)):
            ans.append([])
            if smalls[i]:
                length = len(smalls[i])
                for j in range(len(big)):
                    if j + length > len(big):
                        break
                    if smalls[i] == big[j:j + length]:
                        ans[i].append(j)
        return ans


if __name__ == '__main__':
    big = "abc"
    smalls = [""]
    solution = Solution()
    print(solution.multiSearch(big, smalls))
