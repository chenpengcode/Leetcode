from typing import List


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        n = len(T)
        ans = [0] * n

        for i in range(n):
            cnt = 0
            for j in range(i + 1, n - 1):
                cnt += 1
                if T[j] > T[i]:
                    break
            ans[i] = cnt

        return ans

    def dailyTemperatures_2(self, T: List[int]) -> List[int]:
        length = len(T)
        ans = [0] * length
        stack = []
        for i in range(length):
            temperature = T[i]
            while stack and temperature > T[stack[-1]]:
                prev_index = stack.pop()
                ans[prev_index] = i - prev_index
            stack.append(i)
        return ans


if __name__ == '__main__':
    T = [73, 74, 75, 71, 69, 72, 76, 73]
    solution = Solution()
    print(solution.dailyTemperatures_2(T))
