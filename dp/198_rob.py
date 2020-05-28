from typing import List


class Solution:
    def rob_dptable(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        dp = [nums[0], max(nums[0], nums[1])]
        for i in range(2, len(nums)):
            dp.append(max(dp[i - 2] + nums[i], dp[i - 1]))
        return dp[-1]

    def rob_dp(self, nums: List[int]) -> int:
        pre_max = cur_max = 0

        for i in range(len(nums)):
            tmp = cur_max
            cur_max = max(cur_max, pre_max + nums[i])
            pre_max = tmp

        return cur_max


if __name__ == '__main__':
    nums = [2, 7, 9, 3, 1]
    test = Solution()
    print(test.rob_dp(nums))
