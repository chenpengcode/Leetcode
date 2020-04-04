from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        """
        时间复杂度： O(n^2)
        空间复杂度:O(1)
        :param height:
        :return:
        """
        n = len(height)
        ans = 0
        for i in range(1, n - 1):
            max_left = max_right = 0
            for j in range(i, -1, -1):
                max_left = max(max_left, height[j])
            for j in range(i, n):
                max_right = max(max_right, height[j])

            ans += min(max_left, max_right) - height[i]

        return ans

    def trap_2(self, height: List[int]) -> int:
        """
        时间复杂度： O(n)
        空间复杂度:O(n)
        :param height:
        :return:
        """
        if not height:
            return 0
        n = len(height)
        left_max = [0] * n
        right_max = [0] * n
        ans = 0

        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i])

        right_max[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])

        for i in range(1, n - 1):
            ans += min(left_max[i], right_max[i]) - height[i]

        return ans

    def trap_3(self, height: List[int]) -> int:
        """
        时间复杂度： O(n)
        空间复杂度:O(1)
        :param height:
        :return:
        """
        if not height:
            return 0

        n = len(height)
        left = 0
        right = n - 1
        left_max = height[0]
        right_max = height[n - 1]

        ans = 0
        while left <= right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            if left_max < right_max:
                ans += left_max - height[left]
                left += 1
            else:
                ans += right_max - height[right]
                right -= 1

        return ans


if __name__ == '__main__':
    test = Solution()
    a = [2, 0, 2]
    print(test.trap_3(a))
