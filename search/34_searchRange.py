from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        left, right = 0, len(nums)
        while left < right:
            mid = left + ((right - left) >> 1)
            if target > nums[mid]:
                left = mid + 1
            else:
                right = mid
        start = left if left < len(nums) and nums[left] == target else -1

        left, right = 0, len(nums)
        while left < right:
            mid = left + ((right - left) >> 1)
            if target < nums[mid]:
                right = mid
            else:
                left = mid + 1
        end = left - 1 if left > 0 and nums[left - 1] == target else -1

        return [start, end]


if __name__ == '__main__':
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    solution = Solution()
    print(solution.searchRange(nums, target))
