import time
from typing import List


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] > nums[j]:
                    ans += 1

        return ans

    def reversePairs_2(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
        copy_list = [x for x in nums]
        return self.reverse_pairs(copy_list, 0, n - 1)

    def reverse_pairs(self, nums: List[int], left: int, right: int) -> int:
        if left == right:
            return 0

        mid = left + (right - left) // 2
        left_pairs = self.reverse_pairs(nums, left, mid)
        right_pairs = self.reverse_pairs(nums, mid + 1, right)

        if nums[mid] <= nums[mid + 1]:
            return left_pairs + right_pairs

        cross_pairs = self.merge_and_count(nums, left, mid, right)
        return left_pairs + right_pairs + cross_pairs

    def merge_and_count(self, nums: List[int], left: int, mid: int, right: int) -> int:
        temp_list = [x for x in nums]
        low, high = left, mid + 1

        cnt = 0
        for i in range(left, right + 1):
            if low == mid + 1:
                nums[i] = temp_list[high]
                high += 1
            elif high == right + 1:
                nums[i] = temp_list[low]
                low += 1
            elif temp_list[low] <= temp_list[high]:
                nums[i] = temp_list[low]
                low += 1
            else:
                nums[i] = temp_list[high]
                high += 1
                cnt += (mid - low + 1)
        return cnt

    def merge_sort(self, nums: List[int], tmp: List[int], left, right):
        if left >= right:
            return 0
        mid = left + (right - left) // 2
        cnt = self.merge_sort(nums, tmp, left, mid) + self.merge_sort(nums, tmp, mid + 1, right)
        i, j, pos = left, mid + 1, left
        while i <= mid and j <= right:
            if nums[i] <= nums[j]:
                tmp[pos] = nums[i]
                i += 1
                cnt += (j - (mid + 1))
            else:
                tmp[pos] = nums[j]
                j += 1
            pos += 1

        for k in range(i, mid + 1):
            tmp[pos] = nums[k]
            cnt += (j - (mid + 1))
            pos += 1
        for k in range(j, right + 1):
            tmp[pos] = nums[k]
            pos += 1
        nums[left: right + 1] = tmp[left: right + 1]
        return cnt

    def reversePairs_3(self, nums: List[int]) -> int:
        n = len(nums)
        tmp = [0] * n
        return self.merge_sort(nums, tmp, 0, n - 1)


if __name__ == '__main__':
    nums = [7, 5, 6, 4]
    test = Solution()
    print(test.reversePairs_3(nums))
