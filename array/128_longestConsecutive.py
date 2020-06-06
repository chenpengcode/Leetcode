from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            cnt = 1
            povit = nums[i] + 1
            while povit in nums:
                cnt += 1
                povit += 1
            ans = max(ans, cnt)
        return ans

    def longestConsecutive_hash(self, nums: List[int]) -> int:
        ans = 0
        nums_set = set(nums)

        for num in nums_set:
            if num - 1 not in nums_set:
                cnt = 1
                curr_num = num

                while curr_num + 1 in nums_set:
                    cnt += 1
                    curr_num += 1
                ans = max(ans, cnt)

        return ans


if __name__ == '__main__':
    nums = [100, 4, 200, 1, 3, 2]
    test = Solution()
    print(test.longestConsecutive_hash(nums))
