from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mutil_left, mutil_right, ans = [0] * len(nums), [0] * len(nums), [0] * len(nums)

        mutil_left[0], mutil_right[len(nums) - 1] = 1, 1
        for i in range(1, len(nums)):
            mutil_left[i] = mutil_left[i - 1] * nums[i - 1]
        for i in reversed(range(len(nums) - 1)):
            mutil_right[i] = mutil_right[i + 1] * nums[i + 1]

        for i in range(len(nums)):
            ans[i] = mutil_left[i] * mutil_right[i]

        return ans

    def productExceptSelf_O1(self, nums: List[int]) -> List[int]:
        length = len(nums)
        ans = [0] * length

        ans[0] = 1
        for i in range(1, length):
            ans[i] = ans[i - 1] * nums[i - 1]

        right = 1
        for i in reversed(range(length)):
            ans[i] *= right
            right *= nums[i]
        return ans


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    test = Solution()
    print(test.productExceptSelf_O1(nums))
