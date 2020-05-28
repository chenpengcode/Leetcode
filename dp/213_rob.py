from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        def helper(left, right):
            pre = cur = 0
            for i in range(left, right + 1):
                tmp = cur
                cur = max(pre + nums[i], cur)
                pre = tmp
            return cur

        return max(helper(1, len(nums) - 1), helper(0, len(nums) - 2))


if __name__ == '__main__':
    nums = [2, 3, 2]
    test = Solution()
    print(test.rob(nums))
