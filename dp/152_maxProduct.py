from typing import List


class Solution:
    def maxProduct_violent(self, nums: List[int]) -> int:
        max_product = nums[0]
        for i in range(len(nums)):
            cur_product = nums[i]
            max_product = max(max_product, cur_product)
            for j in range(i + 1, len(nums)):
                cur_product *= nums[j]
                max_product = max(max_product, cur_product)
        return max_product

    def maxProduct_dptable(self, nums: List[int]) -> int:
        dp_max = [x for x in nums]
        dp_min = [x for x in nums]
        for i in range(1, len(nums)):
            dp_max[i] = max(dp_max[i - 1] * nums[i], max(dp_min[i - 1] * nums[i], nums[i]))
            dp_min[i] = min(dp_min[i - 1] * nums[i], min(dp_max[i - 1] * nums[i], nums[i]))
        return max(dp_max)

    def maxProduct_dp(self, nums: List[int]) -> int:
        dp_max = dp_min = ans = nums[0]
        for i in range(1, len(nums)):
            mx, mi = dp_max, dp_min
            dp_max = max(mx * nums[i], max(mi * nums[i], nums[i]))
            dp_min = min(mi * nums[i], min(mx * nums[i], nums[i]))
            ans = max(ans, dp_max)
        return ans


if __name__ == '__main__':
    nums = [-2, 3, -4]
    test = Solution()
    print(test.maxProduct_dp(nums))
