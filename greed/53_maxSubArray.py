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

    def max_sub_array(self, nums):
        n = len(nums)

        if not nums:
            return float('-inf')
        for i in range(1, n):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]

        return max(nums)

    def max_sub_array_2(self, nums):
        left, right = 0, len(nums) - 1
        return self.helper(nums, left, right)

    def helper(self, nums, left, right):

        if left == right:
            return nums[left]

        mid = left + (right - left) // 2
        left_sum = self.helper(nums, left, mid)
        right_sum = self.helper(nums, mid + 1, right)
        cross = self.cross_sum(nums, left, right, mid)
        return max(left_sum, right_sum, cross)

    def cross_sum(self, nums, left, right, mid):
        left_sum, curr_sum = 0, 0
        for i in reversed(range(left, mid)):
            curr_sum += nums[i]
            left_sum = max(left_sum, curr_sum)

        right_sum, curr_sum = 0, 0
        for i in range(mid + 1, right + 1):
            curr_sum += nums[i]
            right_sum = max(right_sum, curr_sum)

        return left_sum + nums[mid] + right_sum


if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    test = Solution()
    print(test.max_sub_array_2(nums))
