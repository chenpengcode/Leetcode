class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        n = len(self.nums)
        if n == 0:
            return 0
        dp = [0] * n
        dp[0] = self.nums[0]

        for i in range(1, n):
            dp[i] = dp[i - 1] + self.nums[i]

        return dp[j] - dp[i] + self.nums[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

if __name__ == '__main__':
    nums = [-2, 0, 3, -5, 2, -1]
    test = NumArray(nums)
    print(test.sumRange(0, 2))
