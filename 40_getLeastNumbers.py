from typing import List


class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k == 0:
            return []
        self.selected(arr, 0, len(arr), k)
        return arr[:k]

    def selected(self, arr: List[int], left: int, right: int, k):
        pos = self.partition(arr, left, right)
        num = pos - left + 1

        if k < num:
            self.selected(arr, left, pos, k)
        elif k > num:
            self.selected(arr, pos + 1, right, k - num)

    def partition(self, arr: List[int], left: int, right: int):
        pivot_index = left
        val = arr[pivot_index]
        i = left + 1

        while i < right:
            if arr[i] < val:
                arr[i], arr[pivot_index + 1] = arr[pivot_index + 1], arr[i]
                pivot_index += 1
            i += 1

        arr[left], arr[pivot_index] = arr[pivot_index], arr[left]
        return pivot_index


if __name__ == '__main__':
    arr = [4, 5, 1, 6, 2, 7, 3, 8]
    test = Solution()
    test.getLeastNumbers(arr, 3)
    print(test.getLeastNumbers(arr, 1))
    print(test.getLeastNumbers(arr, 2))
    print(test.getLeastNumbers(arr, 3))
    # print(test.getLeastNumbers(arr, 4))
    # print(test.getLeastNumbers(arr, 5))
    # print(test.getLeastNumbers(arr, 6))
