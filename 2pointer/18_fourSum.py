from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        # 如果nums为空数组或者长度小于4，解为空
        if n < 4:
            return []

        # 排序
        nums.sort()

        ans = []
        for i in range(n):
            # 去重
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n):
                # 去重
                if j > i + 1 and nums[j - 1] == nums[j]:
                    continue
                t = target - nums[i] - nums[j]
                ans += self.two_sum(nums, nums[i], nums[j], j + 1, n - 1, t)
        return ans

    def two_sum(self, nums, v1, v2, left, right, t):
        res = []
        while left < right:
            if nums[left] + nums[right] == t:
                res.append([v1, v2, nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                right -= 1
            elif nums[left] + nums[right] < t:
                left += 1
            else:
                right -= 1
        return res


if __name__ == '__main__':
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    solution = Solution()
    print(solution.fourSum(nums, target))
