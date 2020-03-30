from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quick_sort(nums, 0, len(nums) - 1)
        return nums

    def quick_sort(self, nums: List[int], left: int, right: int):
        if right <= left:
            return
        mid = self.partion(nums, left, right)
        self.quick_sort(nums, left, mid - 1)
        self.quick_sort(nums, mid + 1, right)

    def partion(self, nums: List[int], left: int, right: int) -> int:
        povit = nums[right]
        povit_index = left - 1

        for i in range(left, right):
            if nums[i] < povit:
                povit_index += 1
                nums[i], nums[povit_index] = nums[povit_index], nums[i]
        povit_index += 1
        nums[povit_index], nums[right] = nums[right], nums[povit_index]

        return povit_index


if __name__ == '__main__':
    test = Solution()
    print(test.sortArray([5, 2, 3, 1]))
