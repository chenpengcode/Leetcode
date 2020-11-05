from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans, n = 0, len(heights)
        for i in range(n):
            height = heights[i]
            left = right = i
            while left - 1 >= 0 and heights[left - 1] >= height:
                left -= 1

            while right + 1 < n and heights[right + 1] >= height:
                right += 1

            ans = max(ans, (right - left + 1) * height)
        return ans

    def largestRectangleArea_stack(self, heights: List[int]) -> int:
        n = len(heights)
        left, right = [0] * n, [0] * n

        stack = list()
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)

        stack = list()
        for i in reversed(range(n)):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            right[i] = stack[-1] if stack else n
            stack.append(i)

        ans = max((right[i] - left[i] - 1) * heights[i] for i in range(n)) if n > 0 else 0
        return ans

    def largestRectangleArea_stack_more(self, heights: List[int]) -> int:
        n = len(heights)
        left, right = [0] * n, [n] * n

        stack = list()
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                right[stack[-1]] = i
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)

        ans = max((right[i] - left[i] - 1) * heights[i] for i in range(n)) if n > 0 else 0
        return ans


if __name__ == '__main__':
    heights = [1]
    test = Solution()
    print(test.largestRectangleArea_stack_more(heights))
