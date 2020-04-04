from random import randint
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.select(nums, 0, len(nums) - 1, len(nums) - k)

    def partition(self, nums, left, right, pivot_index):
        pivot = nums[pivot_index]
        nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
        store_index = left

        for i in range(left, right):
            if nums[i] < pivot:
                nums[i], nums[store_index] = nums[store_index], nums[i]
                store_index += 1
        nums[right], nums[store_index] = nums[store_index], nums[right]
        return store_index

    def select(self, nums, left, right, k):
        if left == right:
            return nums[left]
        pivot_index = randint(left, right)
        pivot_index = self.partition(nums, left, right, pivot_index)
        if k < pivot_index:
            return self.select(nums, left, pivot_index - 1, k)
        elif k > pivot_index:
            return self.select(nums, pivot_index + 1, right, k)
        return nums[k]

    def build_heap(self, nums):
        for i in reversed(range(len(nums))):
            self.max_heapify(nums, i, len(nums))

    def max_heapify(self, heap, root, heap_len):
        p = root

        child_pos = p * 2 + 1
        while child_pos < heap_len:
            right_pos = child_pos + 1
            if right_pos < heap_len and heap[child_pos] < heap[right_pos]:
                child_pos = right_pos

            if heap[p] < heap[child_pos]:
                heap[p], heap[child_pos] = heap[child_pos], heap[p]
                p = child_pos
                child_pos = p * 2 + 1
            else:
                break


if __name__ == '__main__':
    test = Solution()
    nums = [3, 2, 1, 5, 6, 4]
    print(test.findKthLargest(nums, 2))
