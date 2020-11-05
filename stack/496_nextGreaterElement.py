from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        len_n2 = len(nums2)
        right = dict()

        for i in range(len_n2):
            value = -1
            for j in range(i + 1, len_n2):
                if nums2[j] > nums2[i]:
                    value = nums2[j]
                    break
            right[nums2[i]] = value

        ans = []
        for i in range(len(nums1)):
            ans.append(right[nums1[i]])
        return ans

    def nextGreaterElement_stack(self, nums1: List[int], nums2: List[int]) -> List[int]:
        len_n2 = len(nums2)
        right = dict()
        stack = [0] * len_n2

        for i in range(len_n2):
            while stack and nums2[i] > stack[-1]:
                right[stack.pop()] = nums2[i]
            stack.append(nums2[i])
        while stack:
            right[stack.pop()] = -1

        ans = []
        for i in range(len(nums1)):
            ans.append(right[nums1[i]])
        return ans
