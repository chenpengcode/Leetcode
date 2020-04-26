# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def quick_sort(self, nums: List[int], left: int, right: int):
        if left >= right:
            return
        mid = self.partition(nums, left, right)
        self.quick_sort(nums, left, mid - 1)
        self.quick_sort(nums, mid + 1, right)

    def partition(self, nums: List[int], left: int, right: int):
        pivot = nums[right]
        pivot_index = left - 1

        for i in range(left, right):
            if nums[i] < pivot:
                pivot_index += 1
                nums[pivot_index], nums[i] = nums[i], nums[pivot_index]

        pivot_index += 1
        nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
        return pivot_index

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        """
        暴力解法
        :param lists:
        :return:
        """
        tmp = []
        for link_list in lists:
            while link_list:
                tmp.append(link_list.val)
                link_list = link_list.next
        left, right = 0, len(tmp) - 1
        self.quick_sort(tmp, left, right)
        head = node = ListNode(tmp[0])
        for i in range(1, len(tmp)):
            node.next = ListNode(tmp[i])
            node = node.next
        return head


if __name__ == '__main__':
    nums = [6, 5, 3, 2, 1, 4]
    test = Solution()
    test.quick_sort(nums, 0, 5)
    print(nums)
