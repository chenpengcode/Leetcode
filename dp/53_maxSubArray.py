from typing import List


class Solution:
    def maxSubArray_dp(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [nums[0]] * n
        ans = dp[0]
        for i in range(1, n):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
            ans = max(dp[i], ans)

        return ans

    def maxSubArray_dp1(self, nums: List[int]) -> int:
        n = len(nums)
        ans = cur = nums[0]
        for i in range(1, n):
            cur = max(cur + nums[i], nums[i])
            ans = max(ans, cur)
        return ans

    def maxSubArray_greed(self, nums: List[int]) -> int:
        if not nums:
            return float('-inf')
        cur_sum = max_sum = nums[0]

        for i in range(1, len(nums)):
            cur_sum = max(cur_sum + nums[i], nums[i])
            max_sum = max(cur_sum, max_sum)
        return max_sum


if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    solution = Solution()
    print(solution.maxSubArray_greed(nums))
