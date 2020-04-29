# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
class MountainArray:
    def __init__(self, nums):
        self.mountain_array = nums

    def get(self, index: int) -> int:
        return self.mountain_array[index]

    def length(self) -> int:
        return len(self.mountain_array)


class Solution:
    def findInMountainArray(self, target: int, mountain_arr: "MountainArray") -> int:
        arr_len = mountain_arr.length()

        peak_index = self._find_peak_index(mountain_arr, 0, arr_len - 1)

        if mountain_arr.get(peak_index) == target:
            return peak_index

        res = self._find_sorted_array(mountain_arr, 0, peak_index - 1, target)

        if res != -1:
            return res

        return self._find_reversed_array(mountain_arr, peak_index + 1, arr_len - 1, target)

    def _find_peak_index(self, mountain_arr, left, right):
        while left < right:
            mid = left + (right - left) // 2
            if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                left = mid + 1
            else:
                right = mid
        return left

    def _find_sorted_array(self, mountain_arr, left, right, target):
        while left < right:
            mid = left + (right - left) // 2
            if target > mountain_arr.get(mid):
                left = mid + 1
            else:
                right = mid
        if target == mountain_arr.get(left):
            return left
        return -1

    def _find_reversed_array(self, mountain_arr, left, right, target):
        while left < right:
            mid = left + (right - left + 1) // 2
            if target > mountain_arr.get(mid):
                right = mid - 1
            else:
                left = mid
        if target == mountain_arr.get(left):
            return left
        return -1


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 3, 1]
    target = 3
    mountain_arr = MountainArray(nums)
    test = Solution()
    print(test.findInMountainArray(target, mountain_arr))
