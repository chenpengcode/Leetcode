import collections
from functools import reduce
from typing import List


class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        from math import gcd
        vals = collections.Counter(deck).values()
        return reduce(gcd, vals) >= 2


if __name__ == '__main__':
    test = Solution()
    a = [1, 1, 2, 2, 2, 2, 3]
    print(test.hasGroupsSizeX(a))
