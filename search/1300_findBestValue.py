from typing import List


class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort()
        n = len(arr)
        pre_sum = [0]
        for num in arr:
            pre_sum.append(pre_sum[-1] + num)

        right = arr[-1]
        diff = target
        ans = 0
        for i in range(right + 1):
            it = self.binary_search(arr, i)
            cur_sum = pre_sum[it] + (n - it) * i
            if abs(cur_sum - target) < diff:
                ans = i
                diff = abs(cur_sum - target)
        return ans

    def findBestValue_bin(self, arr: List[int], target: int) -> int:
        arr.sort()
        n = len(arr)
        pre_sum = [0]
        for num in arr:
            pre_sum.append(pre_sum[-1] + num)

        value = 0
        left, right = 0, arr[-1] + 1
        while left < right:
            mid = (left + right) >> 1
            it = self.binary_search(arr, mid)
            cur_sum = pre_sum[it] + (n - it) * mid
            if cur_sum < target:
                value = mid
                left = mid + 1
            else:
                right = mid

        def check(x):
            return sum(x if num > x else num for num in arr)

        choose_lower = check(value)
        choose_upper = check(value + 1)

        return value if abs(choose_lower - target) <= abs(
            choose_upper - target) else value + 1

    def binary_search(self, arr, x):
        left, right = 0, len(arr)

        while left < right:
            mid = left + (right - left) // 2
            if x > arr[mid]:
                left = mid + 1
            else:
                right = mid
        return left


if __name__ == '__main__':
    arr = [4, 3, 9]
    target = 10
    solution = Solution()
    print(solution.findBestValue_bin(arr, target))
