from typing import List


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        minfreq = [float("inf")] * 26

        for word in A:
            freq = [0] * 26
            for ch in word:
                freq[ord(ch) - ord("a")] += 1

            for i in range(26):
                minfreq[i] = min(minfreq[i], freq[i])

        ans = list()
        for i in range(26):
            ans.extend([chr(i + ord("a"))] * minfreq[i])
        return ans


if __name__ == '__main__':
    A = ["bella", "label", "roller"]
    solution = Solution()
    print(solution.commonChars(A))
