import heapq
from random import randint
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.select(nums, 0, len(nums) - 1, k)

    def select(self, nums, left, right, k):
        if left == right:
            return nums[left]
        povit_index = self.partition(nums, left, right)
        if povit_index > k - 1:
            return self.select(nums, left, povit_index - 1, k)
        if povit_index < k - 1:
            return self.select(nums, povit_index + 1, right, k)
        return nums[povit_index]

    def partition(self, nums, left, right):
        pivot_index = left
        pivot = nums[pivot_index]
        for i in range(left + 1, right + 1):
            if nums[i] > pivot:
                pivot_index += 1
                nums[i], nums[pivot_index] = nums[pivot_index], nums[i]
        nums[left], nums[pivot_index] = nums[pivot_index], nums[left]
        return pivot_index

    # def partition(self, nums, left, right, pivot_index):
    #     pivot = nums[pivot_index]
    #     nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
    #     store_index = left
    #
    #     for i in range(left, right):
    #         if nums[i] < pivot:
    #             nums[i], nums[store_index] = nums[store_index], nums[i]
    #             store_index += 1
    #     nums[right], nums[store_index] = nums[store_index], nums[right]
    #     return store_index
    #
    # def select(self, nums, left, right, k):
    #     if left == right:
    #         return nums[left]
    #     pivot_index = randint(left, right)
    #     pivot_index = self.partition(nums, left, right, pivot_index)
    #     if k < pivot_index:
    #         return self.select(nums, left, pivot_index - 1, k)
    #     elif k > pivot_index:
    #         return self.select(nums, pivot_index + 1, right, k)
    #     return nums[k]

    def build_heap(self, nums, k):
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heapq.heappop(heap)


if __name__ == '__main__':
    test = Solution()
    nums = [3, 2, 1, 5, 6, 4]
    print(test.findKthLargest(nums, 2))
