def merge_sort(nums, left, right):
    if left >= right:
        return

    mid = left + (right - left) // 2
    merge_sort(nums, left, mid)
    merge_sort(nums, mid + 1, right)
    if nums[mid] > nums[mid + 1]:
        merge(nums, left, mid, right)


def merge(nums, left, mid, right):
    i, j = left, mid + 1

    tmp = []
    while i <= mid and j <= right:
        if nums[i] < nums[j]:
            tmp.append(nums[i])
            i += 1
        else:
            tmp.append(nums[j])
            j += 1

    while i <= mid:
        tmp.append(nums[i])
        i += 1
    while j <= right:
        tmp.append(nums[j])
        j += 1
    nums[left: right + 1] = tmp


if __name__ == '__main__':
    nums = [3, 6, 1, 5, 2, 4]
    left, right = 0, 5
    merge_sort(nums, left, right)
    print(nums)
