from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        ans = [0] * n
        for i in reversed(range(n - 1)):
            ans[i] = max(arr[i + 1], ans[i + 1])
        ans[-1] = -1
        return ans


if __name__ == '__main__':
    arr = [17, 18, 5, 4, 6, 1]
    test = Solution()
    print(test.replaceElements(arr))
