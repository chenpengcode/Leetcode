from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n < k:
            return 0

        ans = 0
        for i in range(n):
            cnt = 0
            for j in range(i, n):
                if nums[j] % 2 == 1:
                    cnt += 1
                if cnt == k:
                    ans += 1
        return ans

    def numberOfSubarrays_2(self, nums: List[int], k: int) -> int:
        n = len(nums)
        odd = [-1]
        ans = 0
        for i in range(n):
            if nums[i] % 2 == 1:
                odd.append(i)
        odd.append(n)
        print(odd)
        for i in range(1, len(odd) - k):
            ans += (odd[i] - odd[i - 1]) * (odd[i + k] - odd[i + k - 1])
        return ans


if __name__ == '__main__':
    nums = [2, 2, 2, 1, 2, 2, 1, 2, 2, 2]
    k = 2
    test = Solution()
    print(test.numberOfSubarrays_2(nums, k))
