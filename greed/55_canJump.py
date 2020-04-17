import collections
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n, right_most = len(nums), 0
        for i in range(n):
            if i <= right_most:
                right_most = i + nums[i]
                if right_most >= n - 1:
                    return True
        return False


if __name__ == '__main__':
    nums = [3, 2, 1, 0, 4]
    test = Solution()
    print(test.canJump(nums))
