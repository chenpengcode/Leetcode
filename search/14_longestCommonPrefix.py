from typing import List


class Solution:
    def longestCommonPrefix_horizontal(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix = strs[0]
        for i in range(1, len(strs)):
            for j in range(len(prefix)):
                if j == len(strs[i]) or prefix[j] != strs[i][j]:
                    prefix = prefix[:j]
                    break
        return prefix

    def longestCommonPrefix_vertical(self, strs: List[str]) -> str:
        if not strs:
            return ""

        length, count = len(strs[0]), len(strs)

        for i in range(length):
            c = strs[0][i]
            for j in range(1, count):
                if i >= len(strs[j]) or strs[j][i] != c:
                    return strs[0][:i]
        return strs[0]

    def longestCommonPrefix_dac(self, strs: List[str]) -> str:
        if not strs:
            return ""

        def lcp(start, end):
            if start == end:
                return strs[start]

            mid = (start + end) // 2
            left, right = lcp(start, mid), lcp(mid + 1, end)
            return prefix(left, right)

        def prefix(left, right):
            pre = left
            for i in range(len(left)):
                if i >= len(right) or left[i] != right[i]:
                    pre = pre[:i]
                    break
            return pre

        return lcp(0, len(strs) - 1)

    def longestCommonPrefix_half(self, strs: List[str]) -> str:
        if not strs:
            return ""

        def is_cp(index):
            pre = strs[0][:index]
            for i in range(1, len(strs)):
                if index > len(strs[i]) or pre != strs[i][:index]:
                    return False
            return True

        length = min(len(s) for s in strs)
        lo, hi = 0, length
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if is_cp(mid):
                lo = mid
            else:
                hi = mid - 1
        return strs[0][:lo]


if __name__ == '__main__':
    strs = ["a", "a"]
    solution = Solution()
    print(solution.longestCommonPrefix_half(strs))
