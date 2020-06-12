from typing import List


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last = {}
        for i, c in enumerate(S):
            last[c] = i

        ans = []
        j = anchor = 0
        for i, c in enumerate(S):
            j = max(j, last[c])
            if i == j:
                ans.append(i - anchor + 1)
                anchor = i + 1
        return ans
