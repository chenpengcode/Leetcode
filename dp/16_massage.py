from typing import List


class Solution:
    def massage(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        pre_max = 0
        cur_max = nums[0]

        for i in range(1, len(nums)):
            tmp = cur_max
            cur_max = max(cur_max, pre_max + nums[i])
            pre_max = tmp

        return cur_max

    def massage_2(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        ans = [0] * len(nums)
        ans[0] = nums[0]
        ans[1] = nums[1]
        for i in range(2, len(nums)):
            ans[i] = max(ans[i - 2] + nums[i], ans[i - 1])

        return ans[len(nums) - 1]


if __name__ == '__main__':
    test = Solution()
    nums = [1, 2, 3, 1]
    print(test.massage_2(nums))
