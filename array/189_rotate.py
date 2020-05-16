from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        self.reverse(nums, 0, len(nums))
        self.reverse(nums, 0, k)
        self.reverse(nums, k, len(nums))

    def reverse(self, nums, start, end):
        while start < end - 1:
            nums[start], nums[end - 1] = nums[end - 1], nums[start]
            start += 1
            end -= 1


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    test = Solution()
    test.rotate(nums, 2)
    print(nums)
