from typing import List


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        n = len(T)
        ans = [0] * n

        for i in range(n):
            cnt = 0
            for j in range(i + 1, n):
                cnt += 1
                if T[j] > T[i]:
                    break
                if j == n - 1 and cnt != 0:
                    cnt = 0
            ans[i] = cnt

        return ans

    def dailyTemperatures_2(self, T: List[int]) -> List[int]:
        n = len(T)

        ans = [0] * n
        stack = []

        for i in range(n):
            t = T[i]

            while stack and t > T[stack[-1]]:
                pre_index = stack.pop()
                ans[pre_index] = i - pre_index
            stack.append(i)
        return ans


if __name__ == '__main__':
    T = [73, 74, 75, 71, 69, 72, 76, 73]
    solution = Solution()
    print(solution.dailyTemperatures(T))
