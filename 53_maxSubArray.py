class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_cur = nums[0]
        max_sum = nums[0]

        for i in range(1, len(nums)):
            max_cur = max(nums[i], max_cur + nums[i])
            max_sum = max(max_cur, max_sum)

        return max_sum


if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    test = Solution()
    print(test.maxSubArray(nums))
