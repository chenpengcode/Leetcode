from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        ans = float('inf')
        for i in range(len(nums) - 1):
            left, right = i + 1, len(nums) - 1
            while left < right:
                three_sum = nums[i] + nums[left] + nums[right]
                if abs(ans - target) > abs(three_sum - target):
                    ans = three_sum
                if three_sum > target:
                    right -= 1
                elif three_sum < target:
                    left += 1
                else:
                    return target
        return ans


if __name__ == '__main__':
    nums = [1, 1, 1, 0]
    target = -100
    solution = Solution()
    print(solution.threeSumClosest(nums, target))
