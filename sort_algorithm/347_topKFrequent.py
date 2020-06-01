import collections
import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)
        heap = []
        for key, val in count.items():
            if len(heap) < k:
                heapq.heappush(heap, (val, key))
            elif val > heap[0][0]:
                heapq.heapreplace(heap, (val, key))
        ans = []
        while heap:
            ans.append(heapq.heappop(heap)[1])
        return ans


if __name__ == '__main__':
    nums = [4, 1, -1, 2, -1, 2, 3]
    k = 2
    test = Solution()
    print(test.topKFrequent(nums, k))
