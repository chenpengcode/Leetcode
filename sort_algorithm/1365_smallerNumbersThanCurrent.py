from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)
        cnt, vec = [0] * 101, [0] * n
        for num in nums:
            cnt[num] += 1
        for i in range(1, 101):
            cnt[i] += cnt[i - 1]
        for i in range(n):
            if nums[i]:
                vec[i] = cnt[nums[i] - 1]
        return vec


if __name__ == '__main__':
    nums = [6, 5, 4, 8, 0]
    test = Solution()
    print(test.smallerNumbersThanCurrent(nums))
