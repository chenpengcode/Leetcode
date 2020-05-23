from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def get_kth_element(k):
            """
            - 主要思路：要找到第 k (k>1) 小的元素，那么就取 pivot1 = nums1[k/2-1] 和 pivot2 = nums2[k/2-1] 进行比较
            - 这里的 "/" 表示整除
            - nums1 中小于等于 pivot1 的元素有 nums1[0 .. k/2-2] 共计 k/2-1 个
            - nums2 中小于等于 pivot2 的元素有 nums2[0 .. k/2-2] 共计 k/2-1 个
            - 取 pivot = min(pivot1, pivot2)，两个数组中小于等于 pivot 的元素共计不会超过 (k/2-1) + (k/2-1) <= k-2 个
            - 这样 pivot 本身最大也只能是第 k-1 小的元素
            - 如果 pivot = pivot1，那么 nums1[0 .. k/2-1] 都不可能是第 k 小的元素。把这些元素全部 "删除"，剩下的作为新的 nums1 数组
            - 如果 pivot = pivot2，那么 nums2[0 .. k/2-1] 都不可能是第 k 小的元素。把这些元素全部 "删除"，剩下的作为新的 nums2 数组
            - 由于我们 "删除" 了一些元素（这些元素都比第 k 小的元素要小），因此需要修改 k 的值，减去删除的数的个数
            """

            index1, index2 = 0, 0
            while True:
                # 特殊情况
                if index1 == m:
                    return nums2[index2 + k - 1]
                if index2 == n:
                    return nums1[index1 + k - 1]
                if k == 1:
                    return min(nums1[index1], nums2[index2])

                # 正常情况
                new_index1 = min(index1 + k // 2 - 1, m - 1)
                new_index2 = min(index2 + k // 2 - 1, n - 1)
                pivot1, pivot2 = nums1[new_index1], nums2[new_index2]
                if pivot1 <= pivot2:
                    k -= new_index1 - index1 + 1
                    index1 = new_index1 + 1
                else:
                    k -= new_index2 - index2 + 1
                    index2 = new_index2 + 1

        m, n = len(nums1), len(nums2)
        total_length = m + n
        if total_length % 2 == 1:
            return get_kth_element((total_length + 1) // 2)
        else:
            return (get_kth_element(total_length // 2) + get_kth_element(total_length // 2 + 1)) / 2

    def find_median_sorted_arrays(self, nums1: List[int], nums2: List[int]) -> float:
        list_1, list_2 = nums1, nums2
        if len(nums1) > len(nums2):
            list_1, list_2 = nums2, nums1

        m, n = len(list_1), len(list_2)
        total_left = (m + n + 1) // 2

        left, right = 0, m
        while left < right:
            i = left + (right - left + 1) // 2
            j = total_left - i
            if list_1[i - 1] > list_2[j]:
                right = i - 1
            else:
                left = i

        i, j = left, total_left - left
        nums1_left_max = list_1[i - 1] if i != 0 else float('-inf')
        nums1_right_min = list_1[i] if i != m else float('inf')
        nums2_left_max = list_2[j - 1] if j != 0 else float('-inf')
        nums2_right_min = list_2[j] if j != n else float('inf')
        if (m + n) % 2:
            return max(nums1_left_max, nums2_left_max)
        return (max(nums1_left_max, nums2_left_max) + min(nums1_right_min, nums2_right_min)) / 2


if __name__ == '__main__':
    nums1 = [1, 2]
    nums2 = [3, 4]
    test = Solution()
    print(test.find_median_sorted_arrays(nums1, nums2))
