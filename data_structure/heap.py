from typing import List
import heapq


def build_heap(nums):
    for i in reversed(range(len(nums))):
        max_heapify(nums, i, len(nums))


def max_heapify(heap, root, heap_len):
    p = root
    while p * 2 + 1 < heap_len:
        left, right = p * 2 + 1, p * 2 + 2

        nex = left
        if right < heap_len and heap[right] > heap[left]:
            nex = right

        if heap[p] < heap[nex]:
            heap[p], heap[nex] = heap[nex], heap[p]
            p = nex
        else:
            break


def heap_sort(nums: List[int]):
    build_heap(nums)
    for i in reversed(range(len(nums))):
        nums[i], nums[0] = nums[0], nums[i]
        max_heapify(nums, 0, i)


if __name__ == '__main__':
    nums = [3, 5, 6, 2, 1, 4]
    heap_sort(nums)
    print(nums)
