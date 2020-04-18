from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0

        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                max_area = max((j - i) * min(height[i], height[j]), max_area)

        return max_area

    def maxArea_2(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        max_area = 0

        while i < j:
            max_area = max((j - i) * min(height[i], height[j]), max_area)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return max_area


if __name__ == '__main__':
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    test = Solution()
    print(test.maxArea_2(height))
