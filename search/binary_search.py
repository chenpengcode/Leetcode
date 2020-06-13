from typing import List


def binary_search(array: List[int], x: int, lo=0, hi=None):
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(array)
    while lo < hi:
        mid = (lo + hi) // 2
        if array[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo


if __name__ == '__main__':
    arr = [1, 3, 3, 3, 3, 5, 7, 9]
    x = 3
    print(binary_search(arr, x))
