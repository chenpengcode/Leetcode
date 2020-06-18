from typing import List


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if m * k > n:
            return -1
        day_set = set(bloomDay)
        days = sorted(list(day_set))

        def check(val):
            serial, cnt, t = 0, 0, 0
            for day in bloomDay:
                if day <= val:
                    serial += 1
                    t += 1
                    if t == k:
                        cnt += 1
                        t = 0
                    if serial >= m * k or cnt >= m:
                        return True
                else:
                    serial = 0
                    t = 0
            return False

        left, right = 0, len(days)
        while left < right:
            mid = (left + right) // 2
            if check(days[mid]):
                right = mid
            else:
                left = mid + 1
        return days[left]


if __name__ == '__main__':
    bloom_day = [1, 10, 3, 10, 2]
    m, k = 3, 1
    solution = Solution()
    print(solution.minDays(bloom_day, m, k))
