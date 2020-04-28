import collections
import functools
from typing import List


class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        tmp_dict = collections.Counter(nums)
        ans = []
        for key, val in tmp_dict.items():
            if val == 1:
                ans.append(key)

        return ans

    def singleNumbers_2(self, nums: List[int]) -> List[int]:
        ret = functools.reduce(lambda x, y: x ^ y, nums)
        div = 1

        while div & ret == 0:
            div <<= 1

        a, b = 0, 0
        for n in nums:
            if n & div:
                a ^= n
            else:
                b ^= n
        return [a, b]


if __name__ == '__main__':
    nums = [1, 2, 10, 4, 1, 4, 3, 3]
    test = Solution()
    print(test.singleNumbers_2(nums))
