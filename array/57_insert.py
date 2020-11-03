from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left, right = newInterval
        ans = list()
        placed = False

        for li, ri in intervals:
            if li > right:
                if not placed:
                    ans.append([left, right])
                    placed = True
                ans.append([li, ri])
            elif ri < left:
                ans.append([li, ri])
            else:
                left = min(left, li)
                right = max(right, ri)

        if not placed:
            ans.append([left, right])
        return ans


if __name__ == '__main__':
    solution = Solution()
    intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    new_interval = [4, 8]
    print(solution.insert(intervals, new_interval))
