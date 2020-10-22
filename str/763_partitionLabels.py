from typing import List


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last = {}

        for i, ch in enumerate(S):
            last[ch] = i

        ans = []
        start = end = 0

        for i, ch in enumerate(S):
            end = max(end, last[ch])
            if end == i:
                ans.append(end - start + 1)
                start = end + 1
        return ans


if __name__ == '__main__':
    S = "ababcbacadefegdehijhklij"
    solution = Solution()
    print(solution.partitionLabels(S))
