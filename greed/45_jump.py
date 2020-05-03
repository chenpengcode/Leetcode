from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        ans, pos = 0, len(nums) - 1

        while pos:
            for i in range(pos):
                if nums[i] + i >= pos:
                    pos = i
                    ans += 1
                    break

        return ans

    def jump_2(self, nums):
        ans, max_pos, end = 0, 0, 0

        for i in range(len(nums) - 1):
            max_pos = max(max_pos, i + nums[i])
            if i == end:
                end = max_pos
                ans += 1

        return ans

    def jump_3(self, nums):
        ans = 0
        max_pos, end = 0, 0

        for i in range(len(nums) - 1):
            max_pos = max(max_pos, i + nums[i])
            if max_pos >= len(nums) - 1:
                ans += 1
                break
            if i == end:
                ans += 1
                end = max_pos
        return ans


if __name__ == '__main__':
    nums = [2, 3, 1, 1, 4]
    test = Solution()
    print(test.jump_3(nums))
