from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(32):
            cnt = 0
            for num in nums:
                cnt += (num >> i) & 1
            ans ^= (cnt % 3) << i
        return ans - 2 ** 32 if ans > 2 ** 31 - 1 else ans


if __name__ == '__main__':
    nums = [2, 3, 2, 2]
    test = Solution()
    print(test.singleNumber(nums))
