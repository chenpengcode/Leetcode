from typing import List


class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        res = []
        depth = 0
        for char in seq:
            if char == '(':
                depth += 1
                res.append(depth % 2)

            if char == ')':
                res.append(depth % 2)
                depth -= 1
        return res


if __name__ == '__main__':
    test = Solution()
    seq = "()(())()"
    print(test.maxDepthAfterSplit(seq))
