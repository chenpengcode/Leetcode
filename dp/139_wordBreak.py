from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and (s[j:i] in word_set):
                    dp[i] = dp[j] and (s[j:i] in word_set)
                    break
        return dp[len(s)]


if __name__ == '__main__':
    s = "leetcode"
    wordDict = ["leet", "code"]
    solution = Solution()
    print(solution.wordBreak(s, wordDict))
