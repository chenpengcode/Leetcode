from typing import List


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        good = set(words)
        for word in words:
            for k in range(1, len(word)):
                good.discard(word[k:])

        return sum(len(word) + 1 for word in good)


if __name__ == '__main__':
    test = Solution()
    a = ["time", "me", "bell"]
    print(test.minimumLengthEncoding(a))
