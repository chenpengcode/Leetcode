import collections
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = collections.Counter(arr)

        s = set()
        for value in d.values():
            s.add(value)
        return len(s) == len(d)
