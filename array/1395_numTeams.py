from typing import List


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        ans = 0
        # 枚举三元组中的 j
        for j in range(1, n - 1):
            iless = imore = kless = kmore = 0
            for i in range(j):
                if rating[i] < rating[j]:
                    iless += 1
                # 注意这里不能直接写成 else
                # 因为可能有评分相同的情况
                elif rating[i] > rating[j]:
                    imore += 1
            for k in range(j + 1, n):
                if rating[k] < rating[j]:
                    kless += 1
                elif rating[k] > rating[j]:
                    kmore += 1
            ans += iless * kmore + imore * kless
        return ans
