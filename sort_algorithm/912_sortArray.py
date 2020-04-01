from typing import List


class SortAlg:
    def quick_sort(self, nums, left, right):
        if left >= right:
            return
        mid = self.partition(nums, left, right)
        self.quick_sort(nums, left, mid - 1)
        self.quick_sort(nums, mid + 1, right)

    def partition(self, nums, left, right):
        pivot = nums[right]
        pivot_index = left - 1

        for i in range(left, right):
            if nums[i] < pivot:
                pivot_index += 1
                nums[i], nums[pivot_index] = nums[pivot_index], nums[i]

        pivot_index += 1
        nums[right], nums[pivot_index] = nums[pivot_index], nums[right]
        return pivot_index

    def heap_sort(self, nums):
        self.build_heap(nums)
        for i in range(len(nums) - 1, -1, -1):
            nums[0], nums[i] = nums[i], nums[0]
            self.max_heapify(nums, 0, i)

    def build_heap(self, nums):
        for i in range(len(nums) - 1, -1, -1):
            self.max_heapify(nums, i, len(nums))

    def max_heapify(self, heap, root, heap_len):
        p = root
        while p * 2 + 1 < heap_len:
            left, right = p * 2 + 1, p * 2 + 2

            if right >= heap_len or heap[right] < heap[left]:
                nex = left
            else:
                nex = right

            if heap[p] < heap[nex]:
                heap[p], heap[nex] = heap[nex], heap[p]
                p = nex
            else:
                break

    def merge_sort(self, nums, left, right):
        if left >= right:
            return
        mid = left + (right - left) // 2
        self.merge_sort(nums, left, mid)
        self.merge_sort(nums, mid + 1, right)
        if nums[mid] > nums[mid + 1]:
            self.merge(nums, left, mid, right)

    def merge_sort_2(self, nums):
        n = 1
        while n < len(nums) * 2:
            left = 0
            right = left + n - 1
            mid = left + (right - left) // 2

            while right < len(nums):
                self.merge(nums, left, mid, right)
                left = right + 1
                right = left + n - 1
                mid = left + (right - left) // 2

            if mid < len(nums):
                self.merge(nums, left, mid, len(nums) - 1)
            n += n

    def merge(self, nums, left, mid, right):
        tmp = []
        i, j = left, mid + 1
        while i <= mid and j <= right:
            if nums[i] < nums[j]:
                tmp.append(nums[i])
                i += 1
            else:
                tmp.append(nums[j])
                j += 1
        while i <= mid:
            tmp.append(nums[i])
            i += 1
        while j <= right:
            tmp.append(nums[j])
            j += 1
        nums[left: right + 1] = tmp


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        ins = SortAlg()
        ins.heap_sort(nums)
        return nums


if __name__ == '__main__':
    test = Solution()
    print(test.sortArray([5, 2, 3, 1]))
