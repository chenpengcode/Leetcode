from typing import List

"""
首先将待排序的数组构造出一个大根堆
取出这个大根堆的堆顶节点(最大值)，与堆的最下最右的元素进行交换，然后把剩下的元素再构造出一个大根堆
重复第二步，直到这个大根堆的长度为1，此时完成排序。
"""


def heap_sort(nums: List[int]):
    build_heap(nums)
    for i in reversed(range(len(nums))):
        nums[0], nums[i] = nums[i], nums[0]
        lens = i
        heapify(nums, 0, lens)


def build_heap(nums: List[int]):
    # 从第一个非叶子节点
    for i in reversed(range(len(nums))):
        heapify(nums, i, len(nums))


def heapify(heap, start_pos, lens):
    p = start_pos
    while p * 2 + 1 < lens:
        left, right = p * 2 + 1, p * 2 + 2
        if right >= lens or heap[right] < heap[left]:
            nex = left
        else:
            nex = right

        if heap[p] < heap[nex]:
            heap[p], heap[nex] = heap[nex], heap[p]
            p = nex
        else:
            break


if __name__ == '__main__':
    nums = [6, 3, 1, 5, 2, 4]
    heap_sort(nums)
    print(nums)
