from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        ans = []
        for interval in intervals:
            if not ans or interval[0] > ans[-1][1]:
                ans.append(interval)
            else:
                ans[-1][1] = min(interval[1], ans[-1][1])

        return ans


if __name__ == '__main__':
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    test = Solution()
    print(test.merge(intervals))
