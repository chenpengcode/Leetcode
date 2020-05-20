from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        pre = [0] * len(nums)
        pre[0] = nums[0] % 2
        for i in range(1, len(nums)):
            pre[i] = pre[i - 1] + nums[i] % 2

        ans = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if (i - 1 < 0 and pre[j] == k) or (pre[j] - pre[i - 1] == k):
                    ans += 1
        return ans

    def number_sub(self, nums, k):
        cnt = [0] * (len(nums) + 1)
        cnt[0] = 1
        odd, ans = 0, 0

        for num in nums:
            if num % 2 == 1:
                odd += 1
            cnt[odd] += 1
            if odd >= k:
                ans += cnt[odd - k]
        return ans


if __name__ == '__main__':
    nums = [1, 1, 2, 1, 1]
    k = 3
    test = Solution()
    print(test.number_sub(nums, k))
