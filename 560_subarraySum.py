from typing import List


class Solution:
    def subarraySum_violence(self, nums: List[int], k: int) -> int:
        ans = 0
        for i in range(len(nums)):
            j = i
            while j < len(nums):
                if sum(nums[i: j + 1]) == k:
                    ans += 1
                j += 1

        return ans

    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt, n = 0, len(nums)
        pre = [0] * n
        for i in range(1, n + 1):
            pre[i] = pre[i - 1] + nums[i - 1]

        for i in range(1, n + 1):
            for j in range(i, n + 1):
                if pre[j] - pre[i - 1] == k:
                    cnt += 1
        return cnt

    def subarraySum_hash(self, nums: List[int], k: int) -> int:
        cnt = pre = 0
        d = dict()

        for num in nums:
            pre += num
            if pre == k:
                cnt += 1
            if pre - k in d:
                cnt += d[pre - k]
            if pre in d:
                d[pre] += 1
            else:
                d[pre] = 1
        return cnt
