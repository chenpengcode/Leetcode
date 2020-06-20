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


def binary_search_2(array: List[int], x: int, lo=0, hi=None):
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(array) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if array[mid] < x:
            lo = mid + 1
        elif array[mid] > x:
            hi = mid - 1
    return lo


def binary_search_3(array: List[int], x: int, lo=0, hi=None):
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if not hi:
        hi = len(array) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if array[mid] == x:
            return mid
        elif array[mid] > x:
            hi = mid - 1
        else:
            lo = mid + 1
    return lo


if __name__ == '__main__':
    arr = [1, 3, 3, 3, 3, 5, 7, 9]
    x = 4
    print(binary_search_3(arr, x))
