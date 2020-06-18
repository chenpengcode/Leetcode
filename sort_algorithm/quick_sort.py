from typing import List


def quick_sort(nums: List[int], left, right):
    if left >= right:
        return

    mid = partition(nums, left, right)
    quick_sort(nums, left, mid - 1)
    quick_sort(nums, mid + 1, right)


def partition(nums, left, right):
    # pivot = nums[right]
    # index = left - 1
    #
    # for i in range(left, right):
    #     if nums[i] < pivot:
    #         index += 1
    #         nums[i], nums[index] = nums[index], nums[i]
    # index += 1
    # nums[index], nums[right] = nums[right], nums[index]
    # return index

    pivot_index = left
    pivot_elem = nums[pivot_index]

    for i in range(left + 1, right + 1):
        if nums[i] < pivot_elem:
            pivot_index += 1
            nums[pivot_index], nums[i] = nums[i], nums[pivot_index]
    nums[left], nums[pivot_index] = nums[pivot_index], nums[left]
    return pivot_index


if __name__ == '__main__':
    nums = [3, 6, 1, 5, 2, 4]
    left, right = 0, 5
    quick_sort(nums, left, right)
    print(nums)
