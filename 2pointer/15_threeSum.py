from typing import List


class Solution:
    def threeSum_brute(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)

        if length < 3:
            return []

        sets = set()
        for i in range(length):
            for j in range(i + 1, length):
                for k in range(j + 1, length):
                    if nums[i] + nums[j] + nums[k] == 0:
                        tmp = [nums[i], nums[j], nums[k]]
                        tmp.sort()
                        sets.add(tuple(tmp))

        ans = []
        for s in sets:
            ans.append([s[0], s[1], s[2]])
        return ans

    def threeSum_better(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        length = len(nums)

        if length < 3:
            return []

        ans = []
        for i in range(length):
            if nums[i] > 0:
                return ans
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            right = length - 1
            target = -nums[i]
            for left in range(i + 1, length):
                if left > i + 1 and nums[left - 1] == nums[left]:
                    continue
                while left < right and nums[left] + nums[right] > target:
                    right -= 1
                if left == right:
                    break
                if nums[left] + nums[right] == target:
                    ans.append([nums[i], nums[left], nums[right]])

        return ans

    def threeSum_2p(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        length = len(nums)
        if length < 3:
            return []
        ans = []
        for i in range(length):
            if nums[i] > 0:
                return ans
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            target = -nums[i]
            ans += self.two_sum(nums, i + 1, length - 1, target, nums[i])
        return ans

    def two_sum(self, nums, left, right, target, val) -> List[List[int]]:
        res = []
        while left < right:
            if nums[left] + nums[right] == target:
                res.append([val, nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                right -= 1
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                left += 1

        return res


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    solution = Solution()
    print(solution.threeSum_2p(nums))
