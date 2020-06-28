from bisect import bisect_left

from typing import List


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        ans = len(nums) + 1
        for i in range(len(nums)):
            total = 0
            for j in range(i, len(nums)):
                total = sum(nums[i: j + 1])
                if total >= s:
                    ans = min(ans, j - i + 1)
        return ans if ans < len(nums) + 1 else 0

    def min_subarray_len(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        ans = n + 1
        sums = [0]
        for i in range(n):
            sums.append(sums[-1] + nums[i])

        for i in range(1, n + 1):
            target = s + sums[i - 1]
            bound = bisect_left(sums, target)
            if bound != len(sums):
                ans = min(ans, bound - (i - 1))

        return 0 if ans == n + 1 else ans

    def min_subarray_len_2(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        ans = n + 1
        start, end = 0, 0
        total = 0
        while end < n:
            total += nums[end]
            while total >= s:
                ans = min(ans, end - start + 1)
                total -= nums[start]
                start += 1
            end += 1
        return 0 if ans == n + 1 else ans


if __name__ == '__main__':
    s = 7
    nums = [2, 3, 1, 2, 4, 3]
    solution = Solution()
    print(solution.min_subarray_len_2(s, nums))
